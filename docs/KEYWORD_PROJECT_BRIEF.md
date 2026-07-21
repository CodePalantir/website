# APX REVOPS — Site Structure Brief for Keyword & Copy Strategy

You are building a keyword targeting strategy for apx-revops.com. Below is the complete
content architecture of the site as built, plus its committed direction. Map keyword
clusters to this structure: every recommended keyword must land on an existing URL or
justify a new page that fits the patterns described here.

## 1. Company and audience

APX REVOPS LTD is a RevOps technology agency (EU-based, English + German). It architects,
integrates and operates revenue systems: CRM platforms (Salesforce, HubSpot), the tools
around them (outbound, enrichment, billing, support, telephony), and the integrations
between them. Positioning: engineering discipline over consulting theater; findings before
opinion; fixed scopes priced in euros.

ICP: B2B and B2C companies from fast-growing software teams to established industrial
groups (industries served: B2B software & tech, finance & wealth, construction & real
estate, manufacturing & industry, e-commerce & retail, events & hospitality, education).
Buyers: founders, revenue leaders, RevOps leads, CFO/COO types who distrust their CRM data.

Flagship entry offer: Technical Health Audit, EUR 2,450 fixed, 5 days, prioritized fix-list
priced in euros. Nearly every conversion path funnels toward it.

## 2. Current site architecture (English, canonical / x-default)

Homepage `/` — narrative: messy stack -> revenue you can trust. Sections: hero, client
strip, industries ("who we work with"), revenue lifecycle (7 phases: attract/demand gen,
prospecting/outbound, lead management, selling/pipeline, quote-to-cash, onboarding/success,
renewal/expansion), featured services (audit flagship + Salesforce/HubSpot/integration/
managed practice areas), stack diagram, insights (pillar + RevShorts).

Hubs and standing pages:
- `/services` — full catalog, 27 services in 8 categories: Audits, Outbound, Enrichment,
  Integration, Salesforce, HubSpot, Connected Tools, Managed.
- `/salesforce` — Salesforce practice hub (engineering-led: degradation/technical-debt
  narrative, GROA impact, audit-first).
- `/work` — case studies hub (placeholder numbers today, real engagements coming).
- `/about`, `/contact` (request form), `/legal-notice`, `/privacy`.
- `/crm-technical-debt` — pillar page: CRM technical debt as a silent tax on revenue
  (facts: net-negative CRM after 5 years, 10% debt increase cuts GROA 16%, Banker et al.).

Service detail pages `/services/<slug>/`:
- 11 rich pages (bespoke sections, FAQ + FAQPage schema, Service + Breadcrumb schema,
  fixed prices): technical-health-audit, data-quality-check, gdpr-compliance,
  sales-cloud-setup, service-cloud-console, marketing-cloud, custom-development,
  custom-integration, mulesoft-architecture, managed-support, managed-partner.
- 16 lite pages (capability checklists) for tools: aircall, apollo, clay, datagma,
  docusign, hubspot-marketing-hub, hubspot-sales-hub, hubspot-service-hub,
  hubspot-operations-hub, instantly, make, n8n, salesforce-cpq, smartlead, workato, zapier.

Products (pre-launch teasers, waitlist CTAs) `/solutions/<slug>/`:
- apx-atlas — SaaS/MCP that maps a CRM's real business process from its automations and
  integrations (live revenue-architecture graph).
- tech-debt-monitor — continuous technical-debt and data-quality scoring with GROA impact
  estimates.
- apx-doppelgaenger — large-scale CRM deduplication with safe merges.

Industries `/industries/<slug>/` — 6 pages, problem-led, each ends in the audit CTA.

Content engines:
- `/revshorts/` + 120 posts `/revshorts/<slug>/` — 2-minute single-idea reads across
  categories (Data, Integration, Outbound, AI, RevOps). Fully bilingual EN/DE.
- `/articles/` — long-form pieces (currently EN only; e.g. stabilizing legacy systems,
  why multi-org architectures fail).

## 3. German tree (full mirror where it exists, hreflang-paired both ways)

`/de/` mirrors the homepage 1:1. Paired pages: `/de/leistungen/` (services hub),
`/de/kontakt/`, `/de/ueber-uns/`, `/de/impressum/`, `/de/datenschutz/`,
`/de/crm-technical-debt/`, `/de/branchen/<slug>/` (6 industries),
`/de/loesungen/<slug>/` (3 solutions), `/de/revshorts/` + 120 German originals.
Voice: informal "ihr". DACH visitors are steered to /de/ at the edge (homepage only).
NOT yet translated: the 27 service detail pages, /salesforce, /work, /articles.

Implication for keywords: German strategy targets DACH decision-makers through the German
tree; German service-page keywords should be collected NOW even though those pages ship
later (they are the committed next translation wave).

## 4. Technical SEO posture (already in place)

hreflang en/de/x-default on every paired page; jekyll-sitemap; clean 301s (old /blog ->
/articles, renamed PDFs); Service, Offer, FAQPage, BreadcrumbList, BlogPosting,
ProfessionalService JSON-LD; fast static site (cache headers, WebP, self-hosted font,
no JS frameworks). Sample PDFs as lead magnets on audit + data-quality pages.

## 5. Where this is heading (plan against future keyword inventory)

1. German versions of the 11 rich service pages plus /salesforce (next translation wave).
2. /work fills with real, numbers-approved case studies (proof keywords, "case study" +
   industry/platform modifiers).
3. Solutions go from teaser to product launch (Atlas first): product-category keywords
   (CRM process mining, revenue architecture mapping, technical debt monitoring,
   CRM deduplication software) should be seeded via pillar/article content before launch.
4. More pillar pages in the /crm-technical-debt mold are the preferred home for big
   informational clusters (candidates: revenue lifecycle, CRM data quality, lead routing,
   quote-to-cash, CRM integration architecture).
5. RevShorts continue weekly-ish in both languages: long-tail question/objection keywords
   can map to individual shorts.
6. HubSpot practice is expected to grow toward parity with Salesforce (hub pages exist as
   lite tier today).

## 6. Copy constraints (any generated copy must obey)

- Absolutely no em dashes or en dashes. Use commas, colons, periods.
- English: direct, punchy, US English, "you/your". German: informal "ihr", never "Sie"
  (except legal pages).
- Prices are named openly (EUR 2,450 audit). Engineering vocabulary, no consulting fluff.
- Claims stay evidence-flavored (cited research, concrete failure modes), never vague ROI.

## 7. Your deliverable

Produce a keyword strategy mapped to this architecture:
1. Cluster keywords by intent and assign each cluster to an existing URL (money pages:
   service details, hubs, industries; informational: pillar, articles, RevShorts).
2. Separate EN and DE strategies (DE is not a translation of EN keywords; research
   German-native phrasing for DACH, e.g. "Salesforce Beratung", "CRM aufraeumen",
   "technische Schulden CRM").
3. Flag gaps where no page fits and propose the page type from the patterns above
   (new lite service page, new industry, new pillar, new RevShort).
4. Prioritize by: proximity to the audit offer, current page strength (rich service pages
   and pillar are strongest), and the roadmap in section 5 (do not recommend building
   for pages that are already committed; feed those keywords into their briefs instead).
