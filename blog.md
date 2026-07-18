---
layout: default
title: Insights – RevOps Engineering Notes from APX
description: "Long-form notes on revenue operations engineering: data quality, architecture, forecasting and deployment — written by the APX team, from real systems."
image: /assets/images/logos/APX_LOGO.png
---

<!-- ── 1 · Hero — same grid+glow ground as the homepage ─────────── -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow"></div>

  <div class="relative z-[4] px-6 pt-40 pb-16 md:pt-48 md:pb-20 text-center">
    <div class="w-full max-w-[880px] mx-auto">
      <span class="apx-eyebrow">Insights</span>
      <h1 class="mt-5 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.4rem,5vw,4rem)]" style="text-wrap:balance">
        Notes from the <span class="text-gradient">revenue engine room.</span>
      </h1>
      <p class="mt-6 mx-auto max-w-[600px] text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted">
        Long-form pieces on data, architecture and the operations behind numbers you can trust — written by the people who build the systems.
      </p>
      <p class="mt-4 text-[15.5px] font-medium text-faint">
        Short on time? Try <a href="{{ site.baseurl }}/revshorts/" class="font-semibold text-accent hover:text-accent-strong transition-colors">RevShorts</a> — one idea, two minutes.
      </p>
    </div>
  </div>
</section>

<!-- ── 2 · Featured latest post ─────────────────────────────────── -->
{% assign featured = site.posts.first %}
<section class="px-6 pb-14 md:pb-20 bg-paper">
  <div class="max-w-wide mx-auto rv">
    <a href="{{ site.baseurl }}{{ featured.url }}" class="apx-card group p-0 overflow-hidden grid md:grid-cols-2">
      <!-- Visual tile -->
      <div class="relative min-h-[240px] md:min-h-[420px] bg-accent-tint overflow-hidden">
        <div class="absolute inset-0 opacity-70" style="background-image:linear-gradient(rgba(74,0,224,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(74,0,224,.08) 1px,transparent 1px);background-size:44px 44px"></div>
        <div class="absolute inset-0" style="background:radial-gradient(60% 55% at 50% 50%, rgba(142,45,226,.16) 0%, transparent 72%)"></div>
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="w-24 h-24 rounded-[1.35rem] bg-white shadow-[0_18px_44px_rgba(74,0,224,.18)] flex items-center justify-center transition-transform duration-500 group-hover:scale-105">
            {% include ui/icon.html name=featured.hero_icon class="w-10 h-10 text-accent" %}
          </div>
        </div>
      </div>
      <!-- Copy -->
      <div class="flex flex-col p-8 md:p-12 lg:p-14">
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center px-3 py-1 rounded-full bg-purple-gradient text-white text-[11px] font-bold uppercase tracking-[0.14em]">Latest</span>
          <span class="inline-flex items-center px-3 py-1 rounded-full bg-accent-tint text-accent text-[11px] font-bold uppercase tracking-[0.14em]">{{ featured.category }}</span>
        </div>
        <h2 class="mt-6 font-bold text-ink tracking-[-0.02em] leading-[1.12] text-[clamp(1.6rem,2.6vw,2.25rem)] group-hover:text-accent-strong transition-colors" style="text-wrap:balance">{{ featured.title }}</h2>
        <p class="mt-4 text-[16.5px] leading-relaxed text-muted max-w-[480px]">{{ featured.description | truncatewords: 30 }}</p>
        <div class="mt-auto pt-8 flex items-center gap-4">
          <img src="{{ site.baseurl }}{{ featured.author_image }}" alt="{{ featured.author }}" class="w-11 h-11 rounded-full object-cover border border-line" loading="lazy">
          <div class="min-w-0">
            <p class="text-[15px] font-semibold text-ink leading-tight">{{ featured.author }}</p>
            <p class="mt-0.5 text-[13.5px] font-medium text-faint">{{ featured.date | date: "%b %-d, %Y" }} &middot; {{ featured.read_time }}</p>
          </div>
          <span class="ml-auto hidden sm:inline-flex items-center gap-2 text-[15px] font-semibold text-accent">
            Read {% include ui/icon.html name="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1" %}
          </span>
        </div>
      </div>
    </a>
  </div>
</section>

<!-- ── 3 · All articles ─────────────────────────────────────────── -->
<section class="px-6 pb-14 md:pb-20 bg-paper">
  <div class="max-w-wide mx-auto">
    <div class="rv">
      {% include ui/eyebrow.html text="All articles" %}
      <hr class="apx-rule mt-4">
    </div>
    <div class="mt-10 grid sm:grid-cols-2 lg:grid-cols-3 gap-5 md:gap-6">
      {% for post in site.posts offset:1 %}
      <a href="{{ site.baseurl }}{{ post.url }}" class="apx-card group rv">
        <div class="flex items-center justify-between gap-3">
          <span class="inline-flex items-center px-3 py-1 rounded-full bg-accent-tint text-accent text-[11px] font-bold uppercase tracking-[0.14em]">{{ post.category }}</span>
          <span class="apx-label">{{ post.read_time }}</span>
        </div>
        <h2 class="mt-5 text-[1.3rem] font-bold text-ink tracking-[-0.015em] leading-snug group-hover:text-accent-strong transition-colors" style="text-wrap:balance">{{ post.title }}</h2>
        <p class="mt-3 text-[15px] leading-relaxed text-muted">{{ post.description | truncatewords: 20 }}</p>
        <div class="mt-auto pt-6 border-t border-line flex items-center gap-3">
          <img src="{{ site.baseurl }}{{ post.author_image }}" alt="{{ post.author }}" class="w-9 h-9 rounded-full object-cover border border-line" loading="lazy">
          <div class="min-w-0">
            <p class="text-[14px] font-semibold text-ink leading-tight">{{ post.author }}</p>
            <p class="mt-0.5 text-[12.5px] font-medium text-faint">{{ post.date | date: "%b %-d, %Y" }}</p>
          </div>
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<!-- ── 4 · RevShorts cross-link ─────────────────────────────────── -->
<section class="px-6 pb-16 md:pb-24 bg-paper">
  <div class="max-w-wide mx-auto rv">
    <a href="{{ site.baseurl }}/revshorts/" class="apx-card group sm:flex-row sm:items-center gap-6 p-7 md:p-9">
      <div class="w-12 h-12 shrink-0 rounded-2xl bg-accent-tint flex items-center justify-center text-accent">
        {% include ui/icon.html name="zap" class="w-5 h-5" %}
      </div>
      <div class="min-w-0">
        <h2 class="text-[1.2rem] font-bold text-ink tracking-[-0.01em] group-hover:text-accent-strong transition-colors">RevShorts — one idea, two minutes.</h2>
        <p class="mt-1.5 text-[15px] leading-relaxed text-muted">{{ site.revshorts | size }} short reads on a single RevOps pattern, failure mode or fix. No filler.</p>
      </div>
      <span class="sm:ml-auto inline-flex items-center gap-2 text-[15px] font-semibold text-accent shrink-0">
        Browse all {% include ui/icon.html name="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1" %}
      </span>
    </a>
  </div>
</section>

{% include sections/cta-band.html %}
