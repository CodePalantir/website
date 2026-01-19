# APEX PALANTIR - Website Content Audit

> **Instructions for Gemini**: Edit the `current_text` field and place your improved version in the `new_text` field. Respect the `min_chars` and `max_chars` constraints to prevent layout breaking. Keep the same tone: professional, technical, confident. Target audience: CTOs, VPs of Sales/RevOps, Salesforce Admins at mid-market to enterprise companies.

---

## SECTION: HERO (Primary Landing)
**File**: `_includes/home/hero.html`
**Purpose**: First impression. Must communicate value proposition in <3 seconds.

### HERO_BADGE
```yaml
id: HERO_BADGE
element: span.badge
current_text: "Salesforce Technical Architects"
new_text: ""
min_chars: 20
max_chars: 40
context: "Small uppercase badge above main headline. Establishes credibility/positioning."
```

### HERO_H1
```yaml
id: HERO_H1
element: h1
current_text: "Laying the Technical Foundation for Sustained Growth."
new_text: ""
min_chars: 35
max_chars: 60
context: "Main headline. Must convey: we build scalable Salesforce architecture. Avoid generic 'transform your business' language."
```

### HERO_DESCRIPTION
```yaml
id: HERO_DESCRIPTION
element: p
current_text: "Most Salesforce instances have a 5-year shelf life due to compounding technical debt. We build robust, scalable architectures that empower Sales, Marketing, and Service teams to win—forever."
new_text: ""
min_chars: 150
max_chars: 220
context: "Supporting paragraph. Explains the problem (technical debt) and our solution (scalable architecture). Should create urgency."
```

### HERO_CTA_PRIMARY
```yaml
id: HERO_CTA_PRIMARY
element: button
current_text: "Start Your Tech Audit"
new_text: ""
min_chars: 15
max_chars: 25
context: "Primary call-to-action button. Should be action-oriented."
```

### HERO_CTA_SECONDARY
```yaml
id: HERO_CTA_SECONDARY
element: button
current_text: "Our Development Approach"
new_text: ""
min_chars: 15
max_chars: 28
context: "Secondary button for users not ready to commit."
```

---

## SECTION: LOGO STRIP (Social Proof)
**File**: `_includes/shared/logo_strip.html`
**Purpose**: Build trust through implied client base.

### LOGO_STRIP_LABEL
```yaml
id: LOGO_STRIP_LABEL
element: div
current_text: "Trusted by Forward-Thinking Leaders"
new_text: ""
min_chars: 25
max_chars: 45
context: "Label above scrolling logo carousel. Should convey trust/credibility."
```

---

## SECTION: WARNINGS (Pain Points)
**File**: `_includes/home/warnings.html`
**Purpose**: Agitate pain points. Reader should recognize their own problems.

### WARNINGS_LABEL
```yaml
id: WARNINGS_LABEL
element: span
current_text: "System Diagnostics"
new_text: ""
min_chars: 12
max_chars: 25
context: "Small label above section heading."
```

### WARNINGS_H2
```yaml
id: WARNINGS_H2
element: h2
current_text: "Are you seeing these Warning Signs?"
new_text: ""
min_chars: 25
max_chars: 45
context: "Section heading. Should be a question that prompts self-reflection."
```

### WARNINGS_INTRO
```yaml
id: WARNINGS_INTRO
element: p
current_text: "If your team is encountering these revenue blockers, your org has likely entered the \"Maintenance Tax\" phase."
new_text: ""
min_chars: 80
max_chars: 130
context: "Sets up the warning cards below. Introduces 'Maintenance Tax' concept."
```

### WARNING_CARD_1_TITLE
```yaml
id: WARNING_CARD_1_TITLE
element: h3
current_text: "Slow Quote Generation"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. CPQ/quoting performance issue."
```

### WARNING_CARD_1_DESC
```yaml
id: WARNING_CARD_1_DESC
element: p
current_text: "Reps leave the platform because pricing logic takes 10+ seconds to load. Speed kills deals."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Specific, relatable problem."
```

### WARNING_CARD_2_TITLE
```yaml
id: WARNING_CARD_2_TITLE
element: h3
current_text: "Untrusted Forecasts"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. Data quality issue."
```

### WARNING_CARD_2_DESC
```yaml
id: WARNING_CARD_2_DESC
element: p
current_text: "Your dashboard numbers don't match reality due to duplicate records and data ghosts."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Relatable data trust problem."
```

### WARNING_CARD_3_TITLE
```yaml
id: WARNING_CARD_3_TITLE
element: h3
current_text: "Feature Gridlock"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. Inability to ship new features."
```

### WARNING_CARD_3_DESC
```yaml
id: WARNING_CARD_3_DESC
element: p
current_text: "Marketing campaigns are delayed weeks because \"simple\" tech updates break everything else."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Cross-team frustration."
```

### WARNING_CARD_4_TITLE
```yaml
id: WARNING_CARD_4_TITLE
element: h3
current_text: "Onboarding Nightmare"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. New hire ramp-up issues."
```

### WARNING_CARD_4_DESC
```yaml
id: WARNING_CARD_4_DESC
element: p
current_text: "New hires take 3 months to ramp up because your UI is cluttered with 5 years of unused fields."
new_text: ""
min_chars: 60
max_chars: 110
context: "Card description. UX/complexity problem."
```

### WARNING_CARD_5_TITLE
```yaml
id: WARNING_CARD_5_TITLE
element: h3
current_text: "Security Liability"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. Permission/security chaos."
```

### WARNING_CARD_5_DESC
```yaml
id: WARNING_CARD_5_DESC
element: p
current_text: "\"Who actually sees this data?\" You don't know because you have 200+ custom profiles."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Compliance/security concern."
```

### WARNING_CARD_6_TITLE
```yaml
id: WARNING_CARD_6_TITLE
element: h3
current_text: "Mobile Crashes"
new_text: ""
min_chars: 10
max_chars: 25
context: "Card title. Mobile app performance."
```

### WARNING_CARD_6_DESC
```yaml
id: WARNING_CARD_6_DESC
element: p
current_text: "Field sales stop using the mobile app because unoptimized pages time out on 5G."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Field team frustration."
```

### WARNING_CARD_7_TITLE
```yaml
id: WARNING_CARD_7_TITLE
element: h3
current_text: "Integration Black Holes"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. Data sync/integration failures."
```

### WARNING_CARD_7_DESC
```yaml
id: WARNING_CARD_7_DESC
element: p
current_text: "Leads from marketing automation vanish before reaching Sales due to silent API failures."
new_text: ""
min_chars: 60
max_chars: 100
context: "Card description. Lead leakage problem."
```

### WARNING_CARD_8_TITLE
```yaml
id: WARNING_CARD_8_TITLE
element: h3
current_text: "End-of-Quarter Freeze"
new_text: ""
min_chars: 12
max_chars: 25
context: "Card title. Performance at critical times."
```

### WARNING_CARD_8_DESC
```yaml
id: WARNING_CARD_8_DESC
element: p
current_text: "The system slows to a crawl exactly when you need it most—closing day."
new_text: ""
min_chars: 50
max_chars: 90
context: "Card description. Peak load problems."
```

---

## SECTION: METHOD (Solution Framework)
**File**: `_includes/home/method.html`
**Purpose**: Present our methodology as the solution. Build confidence.

### METHOD_LABEL
```yaml
id: METHOD_LABEL
element: span
current_text: "The Apex Protocol"
new_text: ""
min_chars: 12
max_chars: 25
context: "Branded methodology name. Should sound proprietary."
```

### METHOD_H2
```yaml
id: METHOD_H2
element: h2
current_text: "Built for Agility. Engineered for Scale."
new_text: ""
min_chars: 30
max_chars: 50
context: "Section heading. Two-part structure works well."
```

### METHOD_INTRO
```yaml
id: METHOD_INTRO
element: p
current_text: "You cannot scale a system you are afraid to touch. We replace fragile \"house of cards\" setups with industrial-grade architecture, allowing you to launch new strategies faster without breaking your existing revenue engine."
new_text: ""
min_chars: 180
max_chars: 240
context: "Sets up the three pillars below. Should address fear of change."
```

### METHOD_PILLAR_1_TITLE
```yaml
id: METHOD_PILLAR_1_TITLE
element: h3
current_text: "Total Visibility & Risk Control"
new_text: ""
min_chars: 20
max_chars: 35
context: "First pillar title. About mapping/understanding the system."
```

### METHOD_PILLAR_1_DESC
```yaml
id: METHOD_PILLAR_1_DESC
element: p
current_text: "We eliminate the \"Black Box\" problem. We map every automation and dependency, identifying exactly which processes are slowing down your sales reps and creating risk."
new_text: ""
min_chars: 130
max_chars: 180
context: "Explains discovery/audit phase value."
```

### METHOD_PILLAR_2_TITLE
```yaml
id: METHOD_PILLAR_2_TITLE
element: h3
current_text: "Modular Growth Architecture"
new_text: ""
min_chars: 20
max_chars: 35
context: "Second pillar title. About decoupled systems."
```

### METHOD_PILLAR_2_DESC
```yaml
id: METHOD_PILLAR_2_DESC
element: p
current_text: "We decouple your systems. This means you can update your Pricing Strategy without accidentally breaking your Customer Support portal. Speed without the chaos."
new_text: ""
min_chars: 130
max_chars: 180
context: "Explains modular architecture benefits."
```

### METHOD_PILLAR_3_TITLE
```yaml
id: METHOD_PILLAR_3_TITLE
element: h3
current_text: "Zero-Downtime Deployments"
new_text: ""
min_chars: 18
max_chars: 35
context: "Third pillar title. About safe deployments."
```

### METHOD_PILLAR_3_DESC
```yaml
id: METHOD_PILLAR_3_DESC
element: p
current_text: "We install automated safety nets that catch errors before they hit production. Your team can deploy new features daily with 100% confidence."
new_text: ""
min_chars: 120
max_chars: 170
context: "Explains CI/CD and testing value."
```

---

## SECTION: LIFECYCLE (Education)
**File**: `_includes/home/crm_lifecycle.html`
**Purpose**: Educate on the degradation curve. Create urgency through data.

### LIFECYCLE_LABEL
```yaml
id: LIFECYCLE_LABEL
element: span
current_text: "The CRM Lifecycle"
new_text: ""
min_chars: 12
max_chars: 25
context: "Section label."
```

### LIFECYCLE_H2
```yaml
id: LIFECYCLE_H2
element: h2
current_text: "Salesforce Degradation is Predictable."
new_text: ""
min_chars: 28
max_chars: 45
context: "Bold claim that positions us as experts."
```

### LIFECYCLE_INTRO
```yaml
id: LIFECYCLE_INTRO
element: p
current_text: "Technical shortcuts expedite initial deployment but systematically decrease system reliability. Eventually, maintenance obligations exceed new feature value, creating a net negative asset."
new_text: ""
min_chars: 140
max_chars: 200
context: "Explains the degradation concept. Should feel like insider knowledge."
```

### LIFECYCLE_STAGE_1_TITLE
```yaml
id: LIFECYCLE_STAGE_1_TITLE
element: h3
current_text: "The Sprint"
new_text: ""
min_chars: 8
max_chars: 20
context: "Stage 1 title (Years 1-2). Initial implementation."
```

### LIFECYCLE_STAGE_1_DESC
```yaml
id: LIFECYCLE_STAGE_1_DESC
element: p
current_text: "\"Expediting system deployment\" maximizes short-term gains. You use standard features. Reliability is high, but shortcuts are taken to meet market speed."
new_text: ""
min_chars: 120
max_chars: 170
context: "Describes honeymoon phase."
```

### LIFECYCLE_STAGE_2_TITLE
```yaml
id: LIFECYCLE_STAGE_2_TITLE
element: h3
current_text: "The Maintenance Tax"
new_text: ""
min_chars: 12
max_chars: 25
context: "Stage 2 title (Years 3-4). Problems emerge."
```

### LIFECYCLE_STAGE_2_DESC
```yaml
id: LIFECYCLE_STAGE_2_DESC
element: p
current_text: "Fact: The net benefit of the system to the firm turns negative after five years. Maintenance obligations now exceed new feature value."
new_text: ""
min_chars: 100
max_chars: 150
context: "The critical inflection point. Data-backed claim."
```

### LIFECYCLE_STAGE_3_TITLE
```yaml
id: LIFECYCLE_STAGE_3_TITLE
element: h3
current_text: "Performance Impairment"
new_text: ""
min_chars: 15
max_chars: 28
context: "Stage 3 title (Year 5+). Full degradation."
```

### LIFECYCLE_STAGE_3_DESC
```yaml
id: LIFECYCLE_STAGE_3_DESC
element: p
current_text: "Fact: A 10% increase in technical debt reduces GROA (Gross Return on Assets) by 16%. Innovation halts as resources shift to fixing disruptions."
new_text: ""
min_chars: 120
max_chars: 170
context: "Worst-case scenario with financial impact."
```

### LIFECYCLE_CTA
```yaml
id: LIFECYCLE_CTA
element: button
current_text: "Assess Your Inflection Point"
new_text: ""
min_chars: 20
max_chars: 35
context: "Call-to-action button for assessment."
```

---

## SECTION: EARLY WARNINGS (Alternative Pain Points)
**File**: `_includes/home/early_warnings.html`
**Purpose**: Different framing of warning signs with diagnostic visual.

### EARLY_WARNINGS_H2
```yaml
id: EARLY_WARNINGS_H2
element: h2
current_text: "Detect the Early Warning Signals."
new_text: ""
min_chars: 25
max_chars: 40
context: "Section heading."
```

### EARLY_WARNING_1_TITLE
```yaml
id: EARLY_WARNING_1_TITLE
element: h3
current_text: "Sluggish Innovation"
new_text: ""
min_chars: 12
max_chars: 25
context: "Warning sign title."
```

### EARLY_WARNING_1_DESC
```yaml
id: EARLY_WARNING_1_DESC
element: p
current_text: "Minor changes now take weeks of testing because \"everything is connected.\""
new_text: ""
min_chars: 55
max_chars: 90
context: "Describes slow delivery problem."
```

### EARLY_WARNING_2_TITLE
```yaml
id: EARLY_WARNING_2_TITLE
element: h3
current_text: "The Security Trap"
new_text: ""
min_chars: 12
max_chars: 25
context: "Warning sign title."
```

### EARLY_WARNING_2_DESC
```yaml
id: EARLY_WARNING_2_DESC
element: p
current_text: "Older configurations no longer align with GDPR or global privacy requirements."
new_text: ""
min_chars: 55
max_chars: 95
context: "Compliance/security concern."
```

### EARLY_WARNING_3_TITLE
```yaml
id: EARLY_WARNING_3_TITLE
element: h3
current_text: "Data Entropy"
new_text: ""
min_chars: 10
max_chars: 20
context: "Warning sign title."
```

### EARLY_WARNING_3_DESC
```yaml
id: EARLY_WARNING_3_DESC
element: p
current_text: "Duplicate records and fragmented reporting are eroding leadership's trust in the dashboard."
new_text: ""
min_chars: 65
max_chars: 100
context: "Data quality degradation."
```

### EARLY_WARNINGS_CTA
```yaml
id: EARLY_WARNINGS_CTA
element: button
current_text: "Book Technical Audit"
new_text: ""
min_chars: 15
max_chars: 25
context: "Call-to-action button."
```

---

## SECTION: DEBT HOOK (Dark Section)
**File**: `_includes/home/debt_hook.html`
**Purpose**: Dramatic section to create urgency. "Expiration date" framing.

### DEBT_HOOK_H2
```yaml
id: DEBT_HOOK_H2
element: h2
current_text: "Is Your Salesforce Instance Ticking Toward its Expiration Date?"
new_text: ""
min_chars: 45
max_chars: 70
context: "Provocative question. Creates urgency."
```

### DEBT_HOOK_POINT_1_TITLE
```yaml
id: DEBT_HOOK_POINT_1_TITLE
element: h3
current_text: "The Performance Drop"
new_text: ""
min_chars: 15
max_chars: 28
context: "First decay symptom."
```

### DEBT_HOOK_POINT_1_DESC
```yaml
id: DEBT_HOOK_POINT_1_DESC
element: p
current_text: "Complex triggers and unoptimized queries slowing down your team."
new_text: ""
min_chars: 45
max_chars: 75
context: "Technical performance issue."
```

### DEBT_HOOK_POINT_2_TITLE
```yaml
id: DEBT_HOOK_POINT_2_TITLE
element: h3
current_text: "The Integration Wall"
new_text: ""
min_chars: 15
max_chars: 28
context: "Second decay symptom."
```

### DEBT_HOOK_POINT_2_DESC
```yaml
id: DEBT_HOOK_POINT_2_DESC
element: p
current_text: "Data silos preventing a true 360-degree view of your customer."
new_text: ""
min_chars: 45
max_chars: 75
context: "Integration/data problem."
```

### DEBT_HOOK_POINT_3_TITLE
```yaml
id: DEBT_HOOK_POINT_3_TITLE
element: h3
current_text: "The Security Gap"
new_text: ""
min_chars: 12
max_chars: 25
context: "Third decay symptom."
```

### DEBT_HOOK_POINT_3_DESC
```yaml
id: DEBT_HOOK_POINT_3_DESC
element: p
current_text: "Aging configurations that no longer meet global privacy standards."
new_text: ""
min_chars: 45
max_chars: 75
context: "Security/compliance issue."
```

### DEBT_HOOK_CTA
```yaml
id: DEBT_HOOK_CTA
element: button
current_text: "Get Your Free Audit"
new_text: ""
min_chars: 14
max_chars: 25
context: "Primary CTA. Emphasize 'free' if appropriate."
```

---

## SECTION: SERVICES (Offerings)
**File**: `_includes/shared/services.html`
**Purpose**: Preview of service offerings with pricing anchors.

### SERVICES_LABEL
```yaml
id: SERVICES_LABEL
element: span
current_text: "Recommended Services"
new_text: ""
min_chars: 15
max_chars: 28
context: "Section label."
```

### SERVICES_H2
```yaml
id: SERVICES_H2
element: h2
current_text: "Core Strategic Solutions"
new_text: ""
min_chars: 18
max_chars: 30
context: "Section heading."
```

### SERVICES_INTRO
```yaml
id: SERVICES_INTRO
element: p
current_text: "We provide engineering excellence that turns Salesforce from a bottleneck into a catalyst. Transparent pricing models for every scale of business."
new_text: ""
min_chars: 120
max_chars: 170
context: "Introduces service cards. Emphasize transparency."
```

### SERVICES_CTA
```yaml
id: SERVICES_CTA
element: button
current_text: "View All Services"
new_text: ""
min_chars: 12
max_chars: 22
context: "Button to full services page."
```

---

## SECTION: EUROPE (Geographic)
**File**: `_includes/home/europe.html`
**Purpose**: Establish European positioning and remote-first approach.

### EUROPE_LABEL
```yaml
id: EUROPE_LABEL
element: span
current_text: "Our Salesforce Network"
new_text: ""
min_chars: 15
max_chars: 30
context: "Section label."
```

### EUROPE_H2
```yaml
id: EUROPE_H2
element: h2
current_text: "Remote First. Europe Wide."
new_text: ""
min_chars: 18
max_chars: 35
context: "Positioning statement."
```

### EUROPE_DESC
```yaml
id: EUROPE_DESC
element: p
current_text: "The best minds across Europe, assembled into one execution-focused team, built to solve complex problems at the highest level"
new_text: ""
min_chars: 100
max_chars: 150
context: "Team value proposition."
```

---

## SECTION: ABOUT (Founder)
**File**: `_includes/home/about_us_home.html`
**Purpose**: Personal credibility and company origin.

### ABOUT_H2
```yaml
id: ABOUT_H2
element: h2
current_text: "Architects, Not Administrators."
new_text: ""
min_chars: 22
max_chars: 38
context: "Differentiator statement."
```

### ABOUT_DESC
```yaml
id: ABOUT_DESC
element: p
current_text: "ApexPalantir was founded to solve the \"implementation gap\" in the Salesforce ecosystem. We bring software engineering discipline to RevOps. We don't just click buttons; we write the code that scales your business."
new_text: ""
min_chars: 170
max_chars: 230
context: "Company origin and positioning."
```

### ABOUT_FOUNDER_NAME
```yaml
id: ABOUT_FOUNDER_NAME
element: span
current_text: "Alexander Knoll"
new_text: ""
min_chars: 10
max_chars: 25
context: "Founder name. Likely unchanged."
```

### ABOUT_FOUNDER_TITLE
```yaml
id: ABOUT_FOUNDER_TITLE
element: span
current_text: "Engineering Lead & Founder"
new_text: ""
min_chars: 18
max_chars: 35
context: "Founder title."
```

---

## SECTION: CUSTOM SOLUTION (CTA)
**File**: `_includes/home/custom_solution.html`
**Purpose**: Capture edge-case prospects who don't fit standard services.

### CUSTOM_BADGE
```yaml
id: CUSTOM_BADGE
element: span
current_text: "Salesforce & Beyond"
new_text: ""
min_chars: 12
max_chars: 25
context: "Badge indicating expanded scope."
```

### CUSTOM_H2
```yaml
id: CUSTOM_H2
element: h2
current_text: "For Problems That Don't Fit a Checkbox."
new_text: ""
min_chars: 30
max_chars: 50
context: "Appealing headline for complex projects."
```

### CUSTOM_DESC
```yaml
id: CUSTOM_DESC
element: p
current_text: "Standard agencies stop at configuration. We start there. Bring us your edge cases, your 'impossible' integrations, and the technical debt no one else wants to touch."
new_text: ""
min_chars: 140
max_chars: 190
context: "Differentiator from standard consultants."
```

### CUSTOM_CTA
```yaml
id: CUSTOM_CTA
element: button
current_text: "Challenge Us"
new_text: ""
min_chars: 8
max_chars: 18
context: "Provocative CTA."
```

---

## SECTION: FOOTER
**File**: `_includes/shared/footer.html`
**Purpose**: Final CTA and navigation.

### FOOTER_BADGE
```yaml
id: FOOTER_BADGE
element: span
current_text: "The Next Chapter"
new_text: ""
min_chars: 10
max_chars: 22
context: "Small badge above CTA."
```

### FOOTER_H2
```yaml
id: FOOTER_H2
element: h2
current_text: "Ready to Build Your Foundation?"
new_text: ""
min_chars: 25
max_chars: 40
context: "Final call-to-action heading."
```

### FOOTER_CTA
```yaml
id: FOOTER_CTA
element: a
current_text: "Get in touch"
new_text: ""
min_chars: 10
max_chars: 18
context: "Contact CTA link."
```

### FOOTER_COPYRIGHT
```yaml
id: FOOTER_COPYRIGHT
element: p
current_text: "© 2026 ApexPalantir. Engineering Excellence."
new_text: ""
min_chars: 30
max_chars: 55
context: "Copyright line."
```

---

## INSTRUCTIONS FOR RETURNING EDITED CONTENT

When returning this file with edits:
1. Fill in the `new_text` field for each block you want to change
2. Leave `new_text` empty for blocks that should remain unchanged
3. Do not modify the `id` fields - these are used for placement
4. Respect `min_chars` and `max_chars` constraints strictly
5. Maintain markdown code block formatting

**Example of edited block:**
```yaml
id: HERO_H1
element: h1
current_text: "Laying the Technical Foundation for Sustained Growth."
new_text: "Engineering the Architecture That Scales Revenue."
min_chars: 35
max_chars: 60
context: "Main headline..."
```
