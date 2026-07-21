# GOLIVE — pre-launch review + RevShort drip plan

Status: dev is 98 commits ahead of production main. This document is the launch
checklist and the daily-RevShort release design. Nothing here is deployed yet.

## 1. Decisions and reviews only Alex can settle

1. **Calendly links**: `site.cta.primary_url` and `secondary_url` in `_config.yml`
   are still TODO placeholders. Per-service `calendly:` deep links look real but
   click-test each one.
2. **About numbers band** (EN `/about` + DE `/de/ueber-uns`) is marked
   "replace with real metrics".
3. **/work case studies** run on `placeholder: true` illustrative numbers behind a
   disclaimer. Decide: launch as-is, or unlink from nav/footer until real numbers exist.
4. **Sample PDFs**: files and URLs now say APX, but the PDF interiors still say
   ApexPalantir. Regenerate when possible.
5. **German voice pass**: skim the "ihr" copy site-wide; legal review of Impressum +
   Datenschutz (including the new section 2.4 LinkedIn Insight Tag, EN + DE).
6. **Phone number**: verify +49 402 2632 0690 is correct and reachable.
7. **Design sign-off**: only the audit service page was personally approved; eyeball
   the other 10 classic service pages + /salesforce hub. Skim 3-4 English RevShort
   translations for voice.
8. **Analytics blind spot**: Fathom is gone; visitors who decline/ignore the banner
   are invisible. Accept, or re-add a cookieless counter (Fathom/Plausible) that
   needs no consent.

## 2. Small fixes to execute before the merge (Claude)

1. `about.md` JSON-LD still links `linkedin.com/company/apexpalantir` → change to
   `/company/apx-revops/`.
2. German 404: `/404.html` is English-only; make it language-aware or add a German
   line (Netlify serves one 404 for everything).
3. Final sweeps: clean build, zero em dashes, zero old-brand strings in `_site`.
4. RevShort drip implementation (section 4).

## 3. Day-of-launch verifications (after merge dev -> main)

1. Netlify build green; production branch confirmed as main.
2. Cookie banner reappears for everyone (consent cookie renamed to `apx_consent_v2`);
   Accept fires `snap.licdn.com` + `px.ads.linkedin.com/collect?pid=9400002`;
   LinkedIn Campaign Manager should flip to Active within 24h of the first real visit.
3. Netlify Forms: submit a test request on /contact and /de/kontakt (form detection
   only happens on deploy).
4. DACH steering: German-language browser gets 302 `/` -> `/de/` (homepage only);
   language switcher sets `nf_lang` override both directions.
5. Redirects: `/blog/*` -> `/articles/*`, old ApexPalantir PDF URLs -> APX PDFs.
6. **SEO churn heads-up**: live `/revshorts/*` URLs currently serve German content.
   After deploy they serve English with hreflang pairs to `/de/revshorts/*`. This is
   intended; watch Google Search Console, submit `sitemap.xml`, and spot-check
   hreflang with the URL inspector.
7. Share previews (og:image = new APX_LOGO.png), favicon (hard refresh; browser
   caches favicons aggressively), PageSpeed Insights on the live domain.

## 4. Daily RevShort release ("one a day, not hidden, no Google dump")

### Mechanism
Future-dated documents + Jekyll `future: false` (default, will be set explicitly) +
one scheduled rebuild per day.

Future-dated shorts are NOT built at all: no HTML, no URL, not in the sitemap, not in
the hub grid, not in homepage insights. They are unpublished, not hidden. A static
site only changes when rebuilt, so a daily scheduled build is what makes each short
appear on its date.

### Setup
1. **Re-date script** (`_tools/redate_revshorts.py`): the 20 newest shorts keep past
   dates (launch inventory so the hub is not thin); the remaining 100 get sequential
   future dates, one per day starting launch+1. EN and DE twins always share the same
   date so hreflang pairs go live together. Result: launch ships 40 short URLs
   (20 EN + 20 DE), then Google sees one fresh pair per day for ~100 days. Steady
   fresh-content cadence instead of a 240-URL dump.
2. **Daily rebuild**: GitHub Actions workflow (`.github/workflows/daily-build.yml`),
   cron 05:00 UTC, POSTs to a Netlify build hook.
   Manual one-time step for Alex: create the build hook in Netlify (Site settings ->
   Build & deploy -> Build hooks) and add its URL as repo secret `NETLIFY_BUILD_HOOK`.
3. **Config**: `future: false` and `timezone: Europe/Berlin` set explicitly in
   `_config.yml` so date cutoffs and the cron agree.
4. **Local preview** of unreleased shorts: `bundle exec jekyll serve --future`.

### Why not the alternatives
- `published: false` flag-flipping needs a daily bot commit: dirty history.
- Client-side hiding leaves all 240 URLs crawlable on day one: exactly the dump
  this avoids.
- Netlify scheduled functions: runtime complexity for what one cron ping does.

### Verification plan
Step 0: future-date one short, build, confirm it disappears from `_site` and
`sitemap.xml` (proves `future: false` covers collection docs). After re-dating:
exactly 40 short pages in the build, pairs share dates, hub shows 20 cards per
language, `--future` build shows all 240.
