---
layout: default
title: Leistungen – Audits, Integration, Salesforce, HubSpot & Managed RevOps
description: "Jedes APX-Projekt, schriftlich gescoped und in Euro beziffert: technische Audits, Outbound- und Enrichment-Infrastruktur, Integrationen, Salesforce- und HubSpot-Builds und Managed Operations."
image: /assets/images/logos/APX_LOGO.png
permalink: /de/leistungen/
lang: de
translation: /services/
---

<!-- HERO -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow opacity-80"></div>
  <div class="relative z-[4] px-6 pt-36 md:pt-44 pb-16 md:pb-24 text-center">
    <div class="max-w-[860px] mx-auto">
      <span class="apx-eyebrow">Leistungen</span>
      <h1 class="mt-4 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.375rem,5.4vw,4.25rem)]" style="text-wrap:balance">
        Wählt die Arbeit.<br class="hidden sm:block"> <span class="text-gradient">Wir machen sie haltbar.</span>
      </h1>
      <p class="mt-6 mx-auto max-w-[600px] text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted">
        Audits, Integrationen, Plattform-Builds und Managed Operations. Jedes Projekt schriftlich gescoped, in Euro beziffert und dokumentiert übergeben.
      </p>
      <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
        {% include ui/cta.html label="Audit buchen, 2.450 €" track="leistungen-hero" no_icon=true class="w-full max-w-[340px] sm:w-auto" %}
        <a href="{{ site.cta.secondary_url }}" target="_blank" rel="noopener noreferrer" data-ap-track="book-call" data-ap-category="leistungen-hero" class="apx-btn apx-btn-ghost w-full max-w-[340px] sm:w-auto">Gespräch buchen</a>
      </div>
    </div>
  </div>
</section>

<!-- WIE WIR ARBEITEN, die vier Regeln -->
<section class="px-6 pt-12 md:pt-16 bg-paper">
  <div class="max-w-wide mx-auto grid sm:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-10 rv">
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Nur Senior</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">Die Person, die ihr kennenlernt, ist die Person, die baut.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Befunde vor Meinung</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">Wir lesen eure Systeme, bevor wir etwas empfehlen.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Fester Scope, fester Preis</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">In Euro beziffert, bevor wir starten. Nie über die Rechnung.</p>
    </div>
    <div class="border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-5">
      <h2 class="text-[16px] font-bold tracking-[-0.01em] text-ink">Code zum Erben</h2>
      <p class="mt-1.5 text-[14px] leading-relaxed text-muted">Versioniert, getestet, dokumentiert für den nächsten Engineer.</p>
    </div>
  </div>
</section>

<!-- LEISTUNGSVERZEICHNIS -->
<section class="pt-10 md:pt-14 pb-20 md:pb-[7.5rem] px-6 bg-paper">
  <div class="max-w-wide mx-auto">
    <div class="space-y-16 md:space-y-20">
      {% for cat in site.data.services.categories %}
      {%- assign idx = forloop.index | prepend: "00" | slice: -2, 2 -%}
      {%- case cat.id -%}
        {%- when "audits" -%}{%- assign cat_line = "Wisst genau, was kaputt ist, bevor ihr einen Euro ins Bauen steckt." -%}{%- assign cat_name = "Audits" -%}
        {%- when "outbound" -%}{%- assign cat_line = "Outbound, das ankommt: Zustellbarkeit, Sequenzen, Systeme." -%}{%- assign cat_name = "Outbound" -%}
        {%- when "enrichment" -%}{%- assign cat_line = "Datensätze, die sich selbst füllen, scoren und sauber halten." -%}{%- assign cat_name = "Enrichment" -%}
        {%- when "integration" -%}{%- assign cat_line = "Eure Tools auf einer Datenachse, im automatischen Austausch." -%}{%- assign cat_name = "Integration" -%}
        {%- when "salesforce" -%}{%- assign cat_line = "Tiefe Plattformarbeit an dem System, auf dem euer Umsatz läuft." -%}{%- assign cat_name = "Salesforce" -%}
        {%- when "hubspot" -%}{%- assign cat_line = "Jeder Hub konfiguriert um einen sauberen Kundendatensatz." -%}{%- assign cat_name = "HubSpot" -%}
        {%- when "connected-tools" -%}{%- assign cat_line = "Die Tools rund um euer CRM, in denselben Fluss verdrahtet." -%}{%- assign cat_name = "Verbundene Tools" -%}
        {%- when "managed" -%}{%- assign cat_line = "Wir bleiben dran, damit die Engine sauber weiterläuft." -%}{%- assign cat_name = "Managed" -%}
        {%- else -%}{%- assign cat_line = "" -%}{%- assign cat_name = cat.name -%}
      {%- endcase -%}
      <div class="grid lg:grid-cols-[280px_1fr] gap-8 lg:gap-16 border-t-[1.5px] border-[rgba(36,28,51,.14)] pt-8 md:pt-10 rv">
        <div class="lg:sticky lg:top-32 lg:self-start">
          <span class="apx-label"><span class="idx">{{ idx }}</span>{{ cat_name }}</span>
          <p class="mt-3 max-w-[380px] text-[17px] leading-relaxed font-medium text-ink-soft" style="text-wrap:balance">{{ cat_line }}</p>
        </div>
        <div class="grid sm:grid-cols-2 gap-4">
          {% for s in cat.services %}
          <a href="{{ site.baseurl }}{{ s.url }}/" class="apx-card p-6 group">
            <div class="flex items-start justify-between gap-4">
              <span class="w-11 h-11 rounded-xl bg-accent-tint text-accent flex items-center justify-center shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">
                {% include ui/icon.html name=s.icon class="w-5 h-5" %}
              </span>
              <span class="text-[13px] font-semibold text-faint whitespace-nowrap pt-1.5">{{ s.price }}{{ s.price_suffix }}{% if s.duration %} &middot; {{ s.duration | replace: "days", "Tage" }}{% endif %}</span>
            </div>
            <h2 class="mt-5 text-[17px] font-bold tracking-[-0.01em] text-ink leading-snug">{{ s.title }}</h2>
            <p class="mt-1.5 text-sm leading-relaxed text-muted">{{ s.short_description_de | default: s.short_description }}</p>
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
