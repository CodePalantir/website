---
layout: default
title: Services, Audits, Integration, Salesforce, HubSpot & Managed RevOps
description: "Every APX engagement, scoped in writing and priced in euros: technical audits, outbound and enrichment infrastructure, integrations, Salesforce and HubSpot builds, and managed operations."
image: /assets/images/logos/APX_LOGO.png
lang: en
translation: /de/leistungen/
---

<!-- HERO, compact, same warm atmosphere as the homepage -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow opacity-80"></div>
  <div class="relative z-[4] px-6 pt-36 md:pt-44 pb-16 md:pb-24 text-center">
    <div class="max-w-[860px] mx-auto">
      <span class="apx-eyebrow">Services</span>
      <h1 class="mt-4 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.375rem,5.4vw,4.25rem)]" style="text-wrap:balance">
        Pick the work.<br class="hidden sm:block"> <span class="text-gradient">We make it stick.</span>
      </h1>
      <p class="mt-6 mx-auto max-w-[600px] text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted">
        Audits, integrations, platform builds and managed operations, every engagement scoped in writing, priced in euros, and left documented for your team.
      </p>
      <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
        {% include ui/cta.html label="Book the audit, €2,450" track="services-hero" no_icon=true class="w-full max-w-[340px] sm:w-auto" %}
        <a href="{{ site.cta.secondary_url }}" target="_blank" rel="noopener noreferrer" data-ap-track="book-call" data-ap-category="services-hero" class="apx-btn apx-btn-ghost w-full max-w-[340px] sm:w-auto">Book a call</a>
      </div>
    </div>
  </div>
</section>

<!-- HOW WE WORK, the four rules as a quiet strip (full version on /about) -->
<section class="px-6 pt-12 md:pt-16 bg-paper">
  <div class="max-w-wide mx-auto grid sm:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-10 rv">
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Senior only</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">The person you meet is the person who builds.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Evidence before opinion</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">We read your systems before we recommend anything.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Fixed scope, fixed price</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">Priced in euros before we start, never on the invoice.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Code you&#8217;d inherit</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">Versioned, tested, documented for the next engineer.</p>
    </div>
  </div>
</section>

<!-- OFFERINGS, one calm ledger: category on the left, tiles on the right -->
<section class="pt-10 md:pt-14 pb-20 md:pb-[7.5rem] px-6 bg-paper">
  <div class="max-w-wide mx-auto">
    <div class="space-y-16 md:space-y-20">
      {% for cat in site.data.services.categories %}
      {%- assign idx = forloop.index | prepend: "00" | slice: -2, 2 -%}
      {%- case cat.id -%}
        {%- when "audits" -%}{%- assign cat_line = "Know exactly what's broken, before you spend a euro on building." -%}
        {%- when "outbound" -%}{%- assign cat_line = "Cold email infrastructure that actually reaches the inbox." -%}
        {%- when "enrichment" -%}{%- assign cat_line = "Records that fill, score and clean themselves." -%}
        {%- when "integration" -%}{%- assign cat_line = "Your tools on one data spine, talking automatically." -%}
        {%- when "salesforce" -%}{%- assign cat_line = "Deep platform work on the org your revenue runs on." -%}
        {%- when "hubspot" -%}{%- assign cat_line = "Every hub configured around one clean customer record." -%}
        {%- when "connected-tools" -%}{%- assign cat_line = "The tools around your CRM, wired into the same flow." -%}
        {%- when "managed" -%}{%- assign cat_line = "We stay on, so the engine keeps running beautifully." -%}
        {%- else -%}{%- assign cat_line = "" -%}
      {%- endcase -%}
      <div class="grid lg:grid-cols-[280px_1fr] gap-8 lg:gap-16 border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-8 md:pt-10 rv">
        <div class="lg:sticky lg:top-32 lg:self-start">
          <span class="apx-label"><span class="idx">{{ idx }}</span>{{ cat.name }}</span>
          <p class="mt-3 max-w-[380px] text-[17px] leading-relaxed font-medium text-ink-soft" style="text-wrap:balance">{{ cat_line }}</p>
        </div>
        <div class="grid sm:grid-cols-2 gap-4">
          {% for s in cat.services %}
          <a href="{{ site.baseurl }}{{ s.url }}/" class="apx-card p-6 group">
            <div class="flex items-start justify-between gap-4">
              <span class="w-11 h-11 rounded-xl bg-accent-tint text-accent flex items-center justify-center shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">
                {% include ui/icon.html name=s.icon class="w-5 h-5" %}
              </span>
              <span class="text-[13px] font-semibold text-faint whitespace-nowrap pt-1.5">{{ s.price }}{{ s.price_suffix }}{% if s.duration %} &middot; {{ s.duration }}{% endif %}</span>
            </div>
            <h2 class="mt-5 text-[17px] font-bold tracking-[-0.01em] text-ink leading-snug">{{ s.title }}</h2>
            <p class="mt-1.5 text-sm leading-relaxed text-muted">{{ s.short_description }}</p>
          </a>
          {% endfor %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

{% include sections/logo-marquee.html %}
{% include sections/cta-band.html %}
