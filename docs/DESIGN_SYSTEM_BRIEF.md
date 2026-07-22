# APX REVOPS — Design System Brief

Feed this to any Claude Code session that generates documents (proposals, reports,
one-pagers, decks, PDFs) so the output matches the apx-revops.com rebuild exactly.

## Identity in one paragraph

Warm premium engineering brand. Light warm cream ground (never grey, never pure
sterile white as page canvas), plum-tinted near-black text, and one violet brand
gradient used as a precise signal, not decoration: a single headline phrase, the
primary CTA, one glow. Calm, generous whitespace; engineering vocabulary; evidence
over adjectives. "Less is more, simple is king."

## Color tokens (exact)

| Token | Hex | Use |
|---|---|---|
| ink | #241C33 | primary text, warm plum-black |
| ink-soft | #3A3149 | softened headings, hover text |
| plum | #17102B | dark panel/section surface (the only dark ground) |
| paper | #FAF8F5 | page canvas, warm cream |
| surface | #FFFFFF | cards and raised elements on paper |
| line | #EAE4E0 | warm hairline borders on light |
| line-strong | #D8D0CA | stronger hairline |
| muted | #5D5470 | secondary text |
| faint | #756B87 | meta, captions, labels (AA on paper/white) |
| accent | #8E2DE2 | brand violet, flat accent |
| accent-strong | #4A00E0 | gradient end, flat deep violet |
| accent-tint | #F4EEFC | icon-tile and chip background |
| ok / warn / flag | #2FA36B / #C98A00 / #DA3B4A | sparse diagnostic status only |
| on dark: hairline | rgba(255,255,255,.10) | borders on plum |

Brand gradient: `linear-gradient(92deg, #8E2DE2 0%, #4A00E0 100%)`.
Used for: one gradient-clipped headline phrase per page/section, primary buttons,
uppercase gradient "eyebrow" kickers. Never for body text or large fills.

Ground rules: light sections alternate paper and surface. Dark sections are plum
with white text (white/70 body, white/50 meta) and glassy cards
(`background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.10)`).
Pure black is reserved for logo reproduction (per brand styleguide), never for UI.

## Typography

- Family: **Satoshi** (variable 300-900). Fallback: system sans. Mono for data/code
  labels: ui-monospace stack. A handwriting stack exists only for the founder
  signature.
- Weights run heavy: bold/extrabold headlines, semibold UI labels, regular body.
- Headline style: tight tracking (-0.02em), tight leading (1.06-1.12),
  `text-wrap: balance`. One phrase inside the headline gets the gradient clip.
- Scale (web reference): hero ~clamp(2.5rem,5.6vw,4.5rem); section H2
  ~clamp(2rem,3.6vw,3rem); card titles 1.15-1.5rem; body 15.5-19px, relaxed leading.
- Eyebrow/kicker: 11-12px, bold, uppercase, letter-spacing 0.14-0.18em, gradient-
  clipped on light (or white/60 on dark). Every major section opens with one.
- Meta labels: mono or sans 10-11px bold uppercase, faint color.
- The logo wordmark is NOT typeset: use the SVG logo assets. (Logo font is Quantify
  Bold per the brand styleguide; it exists only inside the logo files.)

## Shape and depth

- Radii: controls 0.625rem (rounded rectangle, explicitly NOT a pill), cards 1.5rem,
  large panels 2.25rem. Old-design "classic" pages also use 2rem/2.5rem card radii.
- Borders: 1px warm hairlines (line/line-strong). Chips/badges may be full-round.
- Shadows: restrained. Cards hover to a soft lift (translateY(-2px) + soft shadow).
  Primary buttons carry a violet glow (`box-shadow` in rgba(142,45,226,~.35)).
  Showcase mocks may use large soft shadow-2xl.
- Buttons: primary = white text on the brand gradient, radius 0.625rem, semibold;
  ghost = 1px line border, ink text; light = white button on dark plum.

## Signature components (reuse these patterns in documents)

- **Eyebrow -> headline -> lead** stack opening every section, centered or left.
- **Icon tile**: 40-56px rounded-xl square, accent-tint background, accent-colored
  icon (Lucide, 2px stroke); inverts to gradient bg + white icon on hover.
- **Card**: surface bg, line border, radius 1.5rem, title + short muted body.
- **Dark closing panel**: plum, big white headline with gradient phrase, price block
  (label uppercase faint + big number), one white button.
- **Stat/price display**: tabular-nums, black weight, label above in 10px uppercase.
- **Device/report mocks**: skeleton bars (paper/line rounded bars), small labeled
  rows with icon tiles, one floating stat card offset outside the frame.
- **Client logo strip**: grayscale logos, 60% opacity, multiply-blended.
- **Founder signature block**: circular photo, headline, handwriting-font
  "Alexander Knoll", uppercase accent role label ("Founder & Team Lead").

## Logo usage (from the official styleguide)

- Horizontal lockup VAR-2 (gradient triangle + "APX." in black) on light grounds;
  white variant on dark. SVGs, never re-typeset.
- The logo's own gradient runs #df4dd3 -> #933cd5 -> #442bd9 (pinker than the UI
  gradient; this is intentional, do not "fix" either direction).
- Icon-only: triangle in a light squircle (app-icon style) for avatars/favicons.
- Company name in text: "APX REVOPS LTD" (legal) or "APX." (brand short form).

## Voice and copy rules (hard)

- ABSOLUTELY NO EM DASHES or en dashes anywhere. Use commas, colons, periods.
- English: US English, direct address "you/your", short punchy sentences.
- German: informal "ihr" (formal "Sie" only in legal documents).
- Prices stated openly: "EUR 2,450, fixed" / "2.450 €, Festpreis". Five days.
  No vague ROI claims; cite research when claiming (e.g. Banker et al., GROA).
- Engineering vocabulary: audit, fix-list, metadata, org, pipeline, technical debt.
  No consulting fluff ("synergies", "journeys", "holistic transformation").

## Translating the system to documents (A4/PDF/deck)

- Page canvas paper #FAF8F5, generous margins (the web uses 7.5rem section rhythm;
  in print think 20-24mm margins, clear section breathing room).
- Headers: eyebrow + bold headline with ONE gradient phrase. Body in ink on paper.
- Use surface-white cards with 1px line borders for callouts; accent-tint chips for
  tags; the plum dark panel as a closing/CTA page or section divider.
- Tables: mono or small-caps labels in faint, tabular-nums figures, hairline rules
  (line color), no zebra striping.
- Status colors ok/warn/flag only for genuine diagnostics (findings, scores).
- Logo top-left or cover-centered from SVG; footer with legal name
  "APX REVOPS LTD" + apx-revops.com.
- Contact CTAs: calendly.com/apx-revops/intro-call (default) or /audit-scoping
  (audit offers); email support@apx-revops.com.
