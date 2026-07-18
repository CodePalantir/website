---
layout: default
title: RevShorts – Short RevOps Reads
description: "RevShorts are 400 to 500 word reads on a single RevOps idea: one pattern, one failure mode, one fix. From the APX team."
image: /assets/images/logos/APX_LOGO.png
---

<!-- ── 1 · Hero — same grid+glow ground as the homepage ─────────── -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow"></div>

  <div class="relative z-[4] px-6 pt-40 pb-16 md:pt-48 md:pb-20 text-center">
    <div class="w-full max-w-[880px] mx-auto">
      <span class="apx-eyebrow">RevShorts</span>
      <h1 class="mt-5 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.4rem,5vw,4rem)]" style="text-wrap:balance">
        One idea. <span class="text-gradient">Two minutes.</span>
      </h1>
      <p class="mt-6 mx-auto max-w-[600px] text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted">
        Short reads on a single RevOps idea: one pattern, one failure mode, one fix. No filler, no consulting cycle.
      </p>
      <p class="mt-4 text-[15.5px] font-medium text-faint">
        For the longer pieces, see the <a href="{{ site.baseurl }}/blog/" class="font-semibold text-accent hover:text-accent-strong transition-colors">blog</a>.
      </p>
    </div>
  </div>
</section>

<!-- ── 2 · All shorts ───────────────────────────────────────────── -->
<section class="px-6 pb-16 md:pb-24 bg-paper">
  <div class="max-w-wide mx-auto">
    {% assign shorts = site.revshorts | sort: 'date' | reverse %}
    {% if shorts.size > 0 %}
    <div class="rv">
      <span class="apx-label"><span class="idx">{{ shorts.size }}</span>Shorts — newest first</span>
      <hr class="apx-rule mt-4">
    </div>
    <div class="mt-10 grid sm:grid-cols-2 lg:grid-cols-3 gap-5 md:gap-6">
      {% for item in shorts %}
      <a href="{{ site.baseurl }}{{ item.url }}" class="apx-card group p-6 md:p-7">
        <div class="flex items-center justify-between gap-3">
          <div class="w-10 h-10 rounded-xl bg-accent-tint flex items-center justify-center text-accent">
            {% assign _ic = item.hero_icon | default: 'zap' %}{% include ui/icon.html name=_ic class="w-[18px] h-[18px]" %}
          </div>
          <span class="apx-label">{{ item.read_time | default: "2 Min Read" }}</span>
        </div>
        <h2 class="mt-5 text-[1.15rem] font-bold text-ink tracking-[-0.01em] leading-snug group-hover:text-accent-strong transition-colors" style="text-wrap:balance">{{ item.title }}</h2>
        <div class="mt-auto pt-5 flex items-center gap-2 text-[12.5px] font-medium text-faint">
          {% if item.category %}<span class="font-semibold text-accent">{{ item.category }}</span><span aria-hidden="true">&middot;</span>{% endif %}
          <span>{{ item.date | date: "%b %-d, %Y" }}</span>
          <span class="ml-auto inline-flex items-center gap-1 text-[13px] font-semibold text-ink group-hover:text-accent transition-colors">
            Read {% include ui/icon.html name="arrow-right" class="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" %}
          </span>
        </div>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="max-w-md mx-auto apx-card p-10 text-center border-dashed">
      <div class="w-12 h-12 rounded-2xl bg-accent-tint flex items-center justify-center text-accent mx-auto mb-4">{% include ui/icon.html name="zap" class="w-6 h-6" %}</div>
      <p class="text-muted">First RevShorts are on the way. In the meantime, the <a href="{{ site.baseurl }}/blog/" class="font-semibold text-accent hover:text-accent-strong">blog</a> has the long-form pieces.</p>
    </div>
    {% endif %}
  </div>
</section>

{% include sections/cta-band.html %}
