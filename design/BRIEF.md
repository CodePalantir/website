# APX — Design Brief (dark premium authority)

Build a homepage **hero + first fold** (hero → proof → one "practice" section) that reads as
a mature, expensive, senior RevOps **engineering** firm. It must beat the competitor and never
look like a generic SaaS/agency template or an AI-generated page.

## The competitor to beat (screenshots to STUDY first)
- Competitor bar: `design/refs/cremanski.desktop.png` — light hero + a **hexagon photo-collage**
  signature device + **gold** accent + dark proof/content sections. Competent-corporate. Beat it
  with a stronger signature device, sharper type, and a dark-premium execution that differentiates.
- Reference craft: `design/refs/linear.desktop.png`.
- What was REJECTED as "disgustingly ugly" (do NOT reproduce): `design/shots/current-home.desktop.png`
  — sterile, empty, amateur spacing, no imagery, limp. Learn from it.

**Read all three images before designing.**

## Locked direction
- **Dark premium authority.** Deep, considered dark ground (not pure black; a cool near-black with
  a slight hue — think #0A0C12 / #0C0F17). Generous whitespace. Restraint.
- **Purple `#8E2DE2` = precise signal only** (a keyword, a hairline, a small mark, one CTA). NEVER a
  full gradient wash, NEVER purple-on-white.
- **A signature visual device** — invent one as memorable as Cremanski's hexagons but on-thesis for a
  revenue-*engineering* firm: e.g. a live revenue-architecture node graph, a generative grid/mesh,
  an isometric system schematic, a data read-out. Self-authored SVG/CSS/canvas. On-brand, not a gimmick.
- **Imagery**: primarily self-authored generative/graphic art + custom diagrams. A subtle, secondary
  use of abstract/environmental imagery (evoking client worlds — construction, finance, education,
  events) is allowed but must stay quiet. No stock people, no handshakes.
- **Type**: a distinctive display face + clean text face + a mono for data/labels. For THIS mockup you
  may use Google Fonts to explore (e.g. a confident grotesque). Set a real type scale, tight tracking on
  display, proper hierarchy. No Inter/Space-Grotesk-as-default; make the type a memorable part of the design.

## Anti-slop (any of these = fail)
Centered hero over a gradient blob; three-icon-card triptych; pill eyebrows; gradient period on a
headline; animated "trusted by" marquee; emoji icons; rounded-everything; symmetrical rule-of-three copy;
"elevate/unlock/seamless/robust/cutting-edge." Remove-the-logo test: if it could be any consultancy, fail.

## Real content (use verbatim — no lorem)
- Firm: **APX** — a RevOps technology / engineering firm. Frankfurt & remote / EU. Senior engineers only.
- Core promise: **"We engineer the technology your revenue runs on."** We architect, integrate and run the
  systems behind marketing, sales and service — on the stack you already run, not the one someone wants to sell you.
- Flagship offer: **€2,450 fixed-price audit · 5 working days · a prioritised fix-list quantified in euros · no commitment.**
- Full lifecycle (breadth): Attract · Prospect · Qualify · Sell · Quote-to-Cash · Onboard · Renew & Expand.
- The practice — three disciplines (tech debt is only ONE part, not the identity):
  1. **Architect & implement** — stand up / re-architect the core: CRM, CPQ, billing, data model. (Salesforce · HubSpot)
  2. **Integrate & unify** — connect the stack, make the numbers trustworthy. (MuleSoft · Workato · warehouse · APIs)
  3. **Operate & improve** — run it as managed infrastructure; find & price technical debt in euros, then pay it down.
- Clients (real logos at `assets/images/clients/{zech,eigenherd,liqid,eventinc_log,iu,hauser}.webp`):
  Zech, Eigenherd, LIQID, EventInc, IU, Hauser Maschinen.
- Accent purple `#8E2DE2`. Honest proof anchors: €2,450 fixed audit · 5 days · senior engineers · EU.

## Deliverable
ONE self-contained `.html` file (inline `<style>`, may `@import` Google Fonts, may inline SVG/CSS art).
Full hero + proof + the three-discipline "practice" section. Mobile-responsive. Then screenshot it with
`scripts/shoot.sh "file://ABSOLUTE_PATH.html" design/candidates/<id>` at both sizes, VIEW the screenshots,
and iterate until it looks genuinely premium and beats the Cremanski reference. Do not stop at the first draft.
