---
layout: default
title: Work — RevOps & Salesforce Case Studies
description: "Selected APX engagements: Salesforce technical-debt remediation, lead-to-cash integration and CRM re-architecture — anonymised where clients ask, measured everywhere."
image: /assets/images/logos/APX_LOGO.png
permalink: /work/
---

<!-- HERO — compact, same warm atmosphere as the services index -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow opacity-80"></div>
  <div class="relative z-[4] px-6 pt-36 md:pt-44 pb-16 md:pb-24 text-center">
    <div class="max-w-[860px] mx-auto">
      <span class="apx-eyebrow">Our work</span>
      <h1 class="mt-4 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.375rem,5.4vw,4.25rem)]" style="text-wrap:balance">
        Quiet engineering.<br class="hidden sm:block"> <span class="text-gradient">Numbers that hold.</span>
      </h1>
      <p class="mt-6 mx-auto max-w-[600px] text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted">
        A selection of engagements — anonymised where clients ask, measured everywhere. Before and after, in plain figures.
      </p>
    </div>
  </div>
</section>

<!-- CASE GRID -->
<section class="pt-6 md:pt-10 pb-20 md:pb-[7.5rem] px-6 bg-paper">
  <div class="max-w-wide mx-auto">
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-5 rv">
      {% assign cases = site.case_studies | where_exp: "c", "c.published != false" | sort: "order" %}
      {% for c in cases %}
      {% assign lead = c.metrics | first %}
      <a href="{{ site.baseurl }}{{ c.url }}" class="apx-card p-7 group">
        <div class="flex items-start justify-between gap-4">
          <span class="inline-flex items-center rounded-full bg-accent-tint text-accent px-3.5 py-1.5 text-[12px] font-bold uppercase tracking-[0.1em]">{{ c.category }}</span>
          <span class="w-9 h-9 rounded-full border border-line text-faint flex items-center justify-center shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white group-hover:border-transparent">
            {% include ui/icon.html name="arrow-up-right" class="w-4 h-4" %}
          </span>
        </div>
        <h2 class="mt-6 text-[1.35rem] font-bold tracking-[-0.015em] leading-snug text-ink" style="text-wrap:balance">{{ c.title }}</h2>
        <p class="mt-3 apx-label">{{ c.client }}</p>
        <p class="mt-4 text-sm leading-relaxed text-muted">{{ c.summary | truncatewords: 22 }}</p>
        <div class="mt-auto pt-7">
          <hr class="apx-rule">
          {% if lead %}
          <div class="mt-5 flex items-baseline gap-2.5">
            <span class="text-[1.9rem] leading-none font-bold tracking-[-0.02em] text-ink">{{ lead.after }}</span>
            <span class="text-[13px] font-semibold text-faint leading-snug">{{ lead.label }} — from {{ lead.before }}</span>
          </div>
          {% endif %}
          <p class="mt-5 inline-flex items-center gap-1.5 text-sm font-semibold text-accent">
            Read the case {% include ui/icon.html name="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-0.5" %}
          </p>
        </div>
      </a>
      {% endfor %}
    </div>
    <p class="mt-6 text-[13px] font-medium text-faint flex items-center justify-center gap-2 rv">
      {% include ui/icon.html name="info" class="w-3.5 h-3.5 shrink-0" %}
      Representative engagements — placeholder figures shown while clients&#8217; final numbers are approved for publication.
    </p>
  </div>
</section>

{% include sections/logos.html %}
{% include sections/cta-band.html track="work-cta" %}
