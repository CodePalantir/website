/**
 * APX Lumos Light v1.0
 * Lightweight, privacy-friendly analytics
 * ~60 lines, no cookies by default
 */
(function(w, d) {
    'use strict';

    var endpoint = w.APX_ENDPOINT || 'https://lumos.apex-stack.com/api/collect';
    var siteId = w.APX_SITE || location.hostname;
    var loadTime = Date.now();

    console.log('[APX Lumos] Loaded, endpoint:', endpoint);

    // Simple hash for visitor fingerprint (no cookies needed)
    function hash(str) {
        var h = 0;
        for (var i = 0; i < str.length; i++) {
            h = ((h << 5) - h) + str.charCodeAt(i);
            h |= 0;
        }
        return Math.abs(h).toString(36);
    }

    // Generate visitor ID from browser characteristics (no storage)
    function getVisitorId() {
        var data = [
            navigator.userAgent,
            navigator.language,
            screen.width + 'x' + screen.height,
            new Date().getTimezoneOffset()
        ].join('|');
        return hash(data);
    }

    // Get referrer domain only (privacy)
    function getReferrer() {
        if (!d.referrer) return null;
        try {
            var url = new URL(d.referrer);
            if (url.hostname === location.hostname) return null;
            return url.hostname;
        } catch (e) {
            return null;
        }
    }

    // Send pageview
    function track() {
        var data = {
            s: siteId,
            v: getVisitorId(),
            p: location.pathname,
            r: getReferrer(),
            t: d.title,
            w: w.innerWidth,
            u: !!d.referrer && new URL(d.referrer).hostname !== location.hostname,
            hp: '',
            dt: Date.now() - loadTime
        };

        var payload = JSON.stringify(data);

        console.log('[APX Lumos] Sending to:', endpoint);
        console.log('[APX Lumos] Payload:', payload);

        // Use Beacon API (reliable on page exit)
        if (navigator.sendBeacon) {
            var blob = new Blob([payload], { type: 'application/json' });
            var sent = navigator.sendBeacon(endpoint, blob);
            console.log('[APX Lumos] Beacon result:', sent);
        } else {
            // Fallback for older browsers
            var xhr = new XMLHttpRequest();
            xhr.open('POST', endpoint, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(payload);
        }
    }

    // Defer tracking until browser is idle (prevents LCP impact)
    function scheduleTrack() {
        if ('requestIdleCallback' in w) {
            w.requestIdleCallback(track, { timeout: 3000 });
        } else {
            setTimeout(track, 100);
        }
    }

    // Track on load (deferred)
    if (d.readyState === 'complete') {
        scheduleTrack();
    } else {
        w.addEventListener('load', scheduleTrack);
    }

    // Handle SPA navigation
    var pushState = history.pushState;
    history.pushState = function() {
        pushState.apply(history, arguments);
        track();
    };

    w.addEventListener('popstate', track);

    // Calendly link interceptor - append visitor ID for lead attribution
    d.addEventListener('click', function(e) {
        var link = e.target.closest('a[href*="calendly.com"]');
        if (!link) return;

        var url = new URL(link.href);
        url.searchParams.set('utm_source', siteId);
        url.searchParams.set('utm_medium', 'website');
        url.searchParams.set('utm_campaign', location.pathname);
        // Use ApexPalantir UUID if available, fall back to hashed fingerprint
        var uuid = localStorage.getItem('ap_uid');
        url.searchParams.set('utm_content', uuid || getVisitorId());

        link.href = url.toString();
        console.log('[APX Lumos] Calendly link enhanced:', link.href);
    });

    // Public API
    w.ApxLumos = { track: track, getVisitorId: getVisitorId };

})(window, document);
