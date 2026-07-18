# APX — Design Brief v3 (clean · warm · tech-pattern hero · brand gradient)

**Candidate W got the DIRECTION right (clean, warm, less-is-more, one-job header) — keep that.**
User corrections to apply on top of W:

1. **RESPECT THE BRAND GRADIENT: `#8E2DE2 → #4A00E0`** (purple → deep indigo). Use THIS exact two-stop
   gradient for the headline accent phrase, the primary CTA, and the hero glow. NOT pink/coral. Not warm-drifted.
2. **NO photo in the hero.** Replace the (wrong) Bavarian-village photo with a **tech-appealing background
   pattern** — a fading/perspective GRID or mesh with a soft brand-purple gradient glow — in the style of
   `design/refs/salesfive.desktop.png` (salesfive.com). Subtle, premium, "engineered" but clean.
3. **NEW: an industries section** — rounded-corner **square cards, each with a real-life photo** of a customer
   INDUSTRY, under a heading like **"Revenue technology for B2B software, finance, industry & more"** (user's
   words: "Revenue technology services for B2B & B2C"). This is WHERE the real imagery lives — construction/real
   estate (Zech, Hauser), finance/wealth (LIQID), education (IU), events (EventInc), B2B software/tech. Clean
   rounded-square image cards in a tidy grid, each labelled with the sector.
4. Keep everything else from W: full-width hero, big human headline + one gradient phrase, one proof line, two
   pill CTAs, airy one-job header (logo · Services/Work/About/Insights · one CTA), the spare three-discipline
   "what we do", a quiet logo strip, and a rounded closing CTA panel. Generous whitespace. Less is more.

Reference W (direction to keep): `design/candidates/W.desktop.png`.

**The user's actual taste is clean, warm, simple, tech-tasteful — with the real brand purple gradient.**

## The reference to MATCH the feeling of (study it first)
`design/refs/pocketworks.desktop.png` — **Pocketworks**. Note exactly what makes it feel great:
- A **full-bleed, atmospheric real photograph** fills the hero (warm, cinematic city scene), with a
  subtle dark gradient over the lower half so white text sits cleanly on it.
- A **big, warm, human headline**; ONE line rendered in a **warm gradient** (pink→orange) — friendly,
  confident, premium. Not cold.
- **Simple, clear copy** (one sentence of value) + **one real proof stat** ("earns ~£2m in a market
  where 80% of apps never reach £9k").
- **Two rounded-pill CTAs**: a warm-gradient primary + a clean outlined secondary.
- A **clean, airy header**: logo left · a short nav · ONE CTA pill. Nothing else. No clutter.
- Enormous breathing room. Restraint. **Less is more.**

Also beat: `design/refs/cremanski.desktop.png` (warm, human, photographic, trust-heavy — the user rates
it ABOVE cold/technical designs). Do NOT reproduce: `design/refs/current-home.desktop.png` and the
rejected cold-dashboard candidates in `design/candidates/` — no schematics, no read-outs, no terminals,
no masthead "blabber" lines, no dark engineering-instrument vibe.

## Direction (locked, corrected)
- **Warm, human, premium, spacious.** Light or photo-led — NOT dark-mode, NOT a technical dashboard.
- **Full-bleed atmospheric photography** as the hero background (warm, cinematic; a European city / human /
  workspace mood — NOT stock handshakes, NOT people-in-suits clichés). For this mockup you MAY load a
  tasteful photo from a remote URL (e.g. a warm Unsplash cityscape at golden hour) to prove the direction;
  we self-host the final image later.
- **Purple `#8E2DE2` stays the brand**, used as a **warm gradient** on ONE headline phrase and the primary
  CTA (e.g. purple→magenta/pink, or purple→warm-coral). Tasteful, confident — not a flat cold accent.
- **Big confident human headline** + one clear value sentence + **one real proof stat**. Two pill CTAs.
- **Header: does ONE thing.** Logo · a short nav (Services · Work · About · Insights) · ONE primary CTA pill.
  Remove all masthead/spec "blabber". Airy and simple.
- **Less is more** everywhere: generous whitespace, few elements, clear hierarchy, nothing overloaded.

## Voice / content (warm + clear, NOT jargon-heavy)
- Firm: **APX** — a RevOps technology firm. We build and run the revenue systems behind marketing, sales
  and service, so growing companies can actually trust their pipeline and numbers.
- Lead the hero with a **clear, human, outcome-oriented promise** (what the client GETS), not engineering
  jargon. E.g. a headline about revenue that runs smoothly / a stack you can trust / growth without the mess.
  Keep APX's substance but say it warmly and simply.
- Offer / proof anchor (use ONE real stat in the hero): **€2,450 fixed-price audit · 5 days · a fix-list
  priced in euros.** Clients: Zech, Eigenherd, LIQID, EventInc, IU, Hauser Maschinen
  (`assets/images/clients/{zech,eigenherd,liqid,eventinc_log,iu,hauser}.webp`).
- After the hero: a short, warm "what we do" (the three disciplines — architect, integrate, operate — told
  simply), a proof/logos strip, one clear CTA. Keep it spare.

## Deliverable
ONE self-contained `.html` (inline `<style>`, may `@import` Google Fonts, may load a remote hero photo).
Full-bleed photographic hero + a spare "what we do" + logos + CTA. Mobile-responsive, airy.
Then `scripts/shoot.sh "file://ABS_PATH" design/candidates/<id>`, VIEW the shots, and iterate hard until it
feels as warm, premium and effortless as Pocketworks. Do NOT ship a cold, busy, or cluttered draft.
