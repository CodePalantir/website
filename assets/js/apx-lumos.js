/**
 * APX Lumos v2.1 — Agency Analytics
 *
 * No heartbeat. No polling. All events batched and sent on page exit.
 */

(function(window, document) {
    'use strict';

    const CONFIG = {
        endpoint: window.AP_ENDPOINT || '/api/ingest',

        // Storage keys (opaque)
        cookieName: '_ax',
        localStorageKey: '_ax',
        journeyKey: '_jx',
        pageHistoryKey: '_px',

        // Session
        cookieDays: 730,
        sessionTimeoutMinutes: 30,

        // Thresholds
        scrollDepthMilestones: [25, 50, 75, 100],
        idleTimeout: 5000,

        // Download extensions to track
        downloadExtensions: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'csv'],

        debug: window.AP_DEBUG || false
    };

    const state = {
        uuid: null,
        sessionId: null,
        sessionNumber: 1,
        daysSinceLastVisit: 0,
        isReturningVisitor: false,
        pageLoadTime: Date.now(),
        lastActivityTime: Date.now(),
        isVisible: !document.hidden,
        isActive: true,
        activeTime: 0,
        maxScrollDepth: 0,
        scrollMilestones: {},
        eventQueue: []
    };

    // ─── Utilities ───────────────────────────────────────────────────────────

    function log(...args) {
        if (CONFIG.debug) console.log('%c[APX]', 'color: #8B5CF6; font-weight: bold;', ...args);
    }

    function generateUUID() {
        if (window.crypto && window.crypto.randomUUID) return window.crypto.randomUUID();
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
            const r = Math.random() * 16 | 0;
            return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
        });
    }

    function getDateKey() {
        return new Date().toISOString().split('T')[0];
    }

    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    // ─── Storage ─────────────────────────────────────────────────────────────

    const Storage = {
        get(key, defaultValue = null) {
            try {
                const item = localStorage.getItem(key);
                return item ? JSON.parse(item) : defaultValue;
            } catch (e) { return defaultValue; }
        },
        set(key, value) {
            try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) {}
        }
    };

    const Cookie = {
        set(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = `${name}=${value};expires=${expires};path=/;SameSite=Lax`;
        },
        get(name) {
            return document.cookie.split('; ').reduce((r, v) => {
                const parts = v.split('=');
                return parts[0] === name ? parts[1] : r;
            }, null);
        }
    };

    // ─── Identity ─────────────────────────────────────────────────────────────

    function initializeIdentity() {
        const localId = localStorage.getItem(CONFIG.localStorageKey);
        const cookieId = Cookie.get(CONFIG.cookieName);

        if (localId) {
            state.uuid = localId;
            if (!cookieId || cookieId !== localId) Cookie.set(CONFIG.cookieName, localId, CONFIG.cookieDays);
            return;
        }
        if (cookieId) {
            localStorage.setItem(CONFIG.localStorageKey, cookieId);
            state.uuid = cookieId;
            return;
        }
        const newId = generateUUID();
        state.uuid = newId;
        localStorage.setItem(CONFIG.localStorageKey, newId);
        Cookie.set(CONFIG.cookieName, newId, CONFIG.cookieDays);
    }

    // ─── Journey ──────────────────────────────────────────────────────────────
    // Stored fields: a=firstSeen, b=firstSeenTs, c=sessions,
    //                d=lastSession, e=lastSessionTs, f=sessionDates

    function initializeJourney() {
        const j = Storage.get(CONFIG.journeyKey, {
            a: getDateKey(),
            b: Date.now(),
            c: 0,
            d: null,
            e: null,
            f: []
        });

        const today = getDateKey();
        const isNewSession = !j.d ||
            j.d !== today ||
            (Date.now() - (j.e || 0)) > CONFIG.sessionTimeoutMinutes * 60 * 1000;

        if (isNewSession) {
            j.c++;
            if (j.d) {
                state.daysSinceLastVisit = Math.floor((new Date(today) - new Date(j.d)) / 864e5);
                state.isReturningVisitor = true;
            }
            j.d = today;
            j.e = Date.now();
            if (!j.f.includes(today)) j.f.push(today);
        }

        state.sessionNumber = j.c;
        Storage.set(CONFIG.journeyKey, j);
        return j;
    }

    // ─── Page History ─────────────────────────────────────────────────────────

    function trackPageHistory() {
        const path = window.location.pathname;
        const h = Storage.get(CONFIG.pageHistoryKey, {});
        const k = `p:${path}`;

        if (!h[k]) h[k] = { path, first: Date.now(), last: null, visits: 0, totalTime: 0 };

        h[k].visits++;
        h[k].last = Date.now();
        Storage.set(CONFIG.pageHistoryKey, h);
        return h[k];
    }

    // ─── Event Queue ──────────────────────────────────────────────────────────
    // Envelope fields: t=type, i=uid, s=sid, n=sessionNum,
    //                  q=daysSinceVisit, x=timestamp, dk=dateKey, u=url, r=ref

    function queueEvent(data) {
        state.eventQueue.push({
            ...data,
            i: state.uuid,
            s: state.sessionId,
            n: state.sessionNumber,
            q: state.daysSinceLastVisit,
            x: Date.now(),
            dk: getDateKey(),
            u: window.location.pathname,
            r: document.referrer ? new URL(document.referrer).hostname : null
        });
    }

    function flushEvents() {
        if (state.eventQueue.length === 0) return;

        const payload = JSON.stringify({
            _e: state.eventQueue,
            _m: {
                v: '2.1',
                sr: `${screen.width}x${screen.height}`,
                vp: `${window.innerWidth}x${window.innerHeight}`,
                tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
                lg: navigator.language
            }
        });

        if (navigator.sendBeacon) {
            navigator.sendBeacon(CONFIG.endpoint, payload);
        } else {
            fetch(CONFIG.endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: payload,
                keepalive: true
            }).catch(() => {});
        }
    }

    // ─── Page View ────────────────────────────────────────────────────────────

    function trackPageView() {
        const pageData = trackPageHistory();
        const j = Storage.get(CONFIG.journeyKey);

        const params = new URLSearchParams(window.location.search);
        const utm = {};
        ['source', 'medium', 'campaign', 'term', 'content'].forEach(k => {
            if (params.has(`utm_${k}`)) utm[k] = params.get(`utm_${k}`);
        });

        const w = window.innerWidth;
        queueEvent({
            t: 'pv',
            ti: document.title,
            pv: pageData.visits,
            rv: state.isReturningVisitor,
            sc: j.c,
            dv: w < 768 ? 0 : w < 1024 ? 1 : 2,  // 0=mobile, 1=tablet, 2=desktop
            utm: Object.keys(utm).length ? utm : null
        });
    }

    // ─── Time & Idle ──────────────────────────────────────────────────────────

    function updateTimeTracking() {
        const now = Date.now();
        if (state.isVisible && state.isActive) {
            state.activeTime += now - state.lastActivityTime;
        }
        state.lastActivityTime = now;
    }

    let idleTimer = null;
    function resetIdleTimer() {
        state.isActive = true;
        clearTimeout(idleTimer);
        idleTimer = setTimeout(() => { state.isActive = false; }, CONFIG.idleTimeout);
    }

    function handleVisibilityChange() {
        updateTimeTracking();
        state.isVisible = !document.hidden;
        state.lastActivityTime = Date.now();
    }

    // ─── Scroll ───────────────────────────────────────────────────────────────

    const trackScroll = throttle(function() {
        const scrollY = window.pageYOffset;
        const docHeight = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
        const depth = Math.min(100, Math.round((scrollY + window.innerHeight) / docHeight * 100));

        if (depth > state.maxScrollDepth) state.maxScrollDepth = depth;

        CONFIG.scrollDepthMilestones.forEach(m => {
            if (depth >= m && !state.scrollMilestones[m]) {
                state.scrollMilestones[m] = true;
                queueEvent({
                    t: 'sc',
                    dp: m,
                    tm: Math.round((Date.now() - state.pageLoadTime) / 1000)
                });
            }
        });
    }, 200);

    // ─── Section Visibility ───────────────────────────────────────────────────

    function setupSectionTracking() {
        if (!window.IntersectionObserver) return;

        const sections = document.querySelectorAll('section[id], [data-ap-section]');
        if (sections.length === 0) return;

        const entryTimes = {};

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const id = entry.target.id || entry.target.dataset.apSection;
                if (!id) return;

                if (entry.isIntersecting) {
                    entryTimes[id] = Date.now();
                } else if (entryTimes[id]) {
                    const dr = Date.now() - entryTimes[id];
                    delete entryTimes[id];
                    if (dr > 2000) {
                        queueEvent({
                            t: 'sv',
                            id: btoa(id).replace(/=/g, ''),
                            dr: Math.round(dr / 1000)
                        });
                    }
                }
            });
        }, { threshold: 0.5 });

        sections.forEach(s => observer.observe(s));
    }

    // ─── Copy Events ──────────────────────────────────────────────────────────

    function trackCopy() {
        const sel = window.getSelection().toString().trim();
        if (sel.length > 0 && sel.length < 500) {
            queueEvent({
                t: 'cp',
                ln: sel.length,
                pw: sel.substring(0, 50)
            });
        }
    }

    // ─── CTA & Download Clicks ────────────────────────────────────────────────

    function trackClick(e) {
        const target = e.target;

        const cta = target.closest('[data-ap-track]');
        if (cta) {
            queueEvent({
                t: 'ct',
                nm: cta.dataset.apTrack,
                cg: cta.dataset.apCategory || null,
                vl: cta.dataset.apValue || null
            });
        }

        const link = target.closest('a[href]');
        if (link) {
            const href = link.getAttribute('href') || '';
            const ext = href.split('.').pop().toLowerCase().split('?')[0];
            if (CONFIG.downloadExtensions.includes(ext)) {
                queueEvent({
                    t: 'dl',
                    hr: href.substring(0, 200),
                    ex: ext
                });
            }
        }
    }

    // ─── Page Exit ────────────────────────────────────────────────────────────

    function handlePageExit() {
        updateTimeTracking();

        const h = Storage.get(CONFIG.pageHistoryKey, {});
        const k = `p:${window.location.pathname}`;
        if (h[k]) {
            h[k].totalTime = (h[k].totalTime || 0) + Math.round(state.activeTime / 1000);
            Storage.set(CONFIG.pageHistoryKey, h);
        }

        queueEvent({
            t: 'ex',
            at: Math.round(state.activeTime / 1000),
            sd: state.maxScrollDepth
        });

        flushEvents();
    }

    // ─── Init ─────────────────────────────────────────────────────────────────

    function init() {
        log('init');

        initializeIdentity();
        initializeJourney();
        state.sessionId = `${state.sessionNumber}-${Date.now()}`;

        trackPageView();

        document.addEventListener('visibilitychange', handleVisibilityChange);
        document.addEventListener('scroll', trackScroll, { passive: true });
        document.addEventListener('copy', trackCopy);
        document.addEventListener('click', trackClick);
        window.addEventListener('beforeunload', handlePageExit);

        ['keypress', 'scroll', 'click', 'touchstart'].forEach(ev => {
            document.addEventListener(ev, resetIdleTimer, { passive: true });
        });

        if (document.readyState === 'complete') {
            setupSectionTracking();
        } else {
            window.addEventListener('load', setupSectionTracking);
        }

        log('ready', state.uuid);
    }

    // ─── Public API ───────────────────────────────────────────────────────────

    window.ApexPalantir = {
        init,
        track(name, props = {}) {
            queueEvent({ t: 'cu', nm: name, pp: props });
        },
        getUUID: () => state.uuid,
        flush: flushEvents,
        debug() {
            const j = Storage.get(CONFIG.journeyKey, {});
            const p = Storage.get(CONFIG.pageHistoryKey, {});
            return {
                uuid: state.uuid,
                session: state.sessionNumber,
                daysSince: state.daysSinceLastVisit,
                returning: state.isReturningVisitor,
                activeTime: Math.round(state.activeTime / 1000),
                scrollDepth: state.maxScrollDepth,
                queue: state.eventQueue.length,
                journey: { firstSeen: j.a, sessions: j.c, lastSession: j.d },
                pages: Object.values(p).map(v => ({ path: v.path, visits: v.visits, time: v.totalTime }))
            };
        }
    };

})(window, document);
