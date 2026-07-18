---
layout: default
title: RevShorts – Short RevOps Reads
description: "RevShorts are 400 to 500 word reads on a single RevOps idea: one pattern, one failure mode, one fix. From the APX team."
image: /assets/images/logos/APX_LOGO.png
---

<!-- REVSHORTS HERO -->
<section class="pt-28 sm:pt-32 md:pt-36 pb-10 md:pb-14 px-4 sm:px-6 bg-white">
  <div class="max-w-7xl mx-auto">
    <span class="text-[#8E2DE2] font-bold uppercase tracking-widest text-xs mb-4 block">RevShorts</span>
    <h1 class="text-4xl md:text-5xl lg:text-6xl font-black leading-[1.05] tracking-tight text-slate-900">
      One idea. Two minutes<span class="text-gradient">.</span>
    </h1>
    <p class="text-slate-600 mt-6 text-lg leading-relaxed max-w-2xl">Short reads on a single RevOps idea: one pattern, one failure mode, one fix. No filler, no consulting cycle. For the longer pieces, see the <a href="{{ site.baseurl }}/blog" class="font-bold text-purple-600 hover:text-purple-700">blog</a>.</p>
  </div>
</section>

<!-- REVSHORTS GRID -->
<section class="pb-16 md:pb-24 px-4 sm:px-6 bg-white">
  <div class="max-w-7xl mx-auto">
    {% assign shorts = site.revshorts | sort: 'date' | reverse %}
    {% if shorts.size > 0 %}
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 sm:gap-6">
      {% for item in shorts %}
      <a href="{{ site.baseurl }}{{ item.url }}" class="group flex flex-col p-7 rounded-3xl border border-slate-100 hover:border-purple-200 hover:shadow-xl hover:shadow-purple-100/40 transition-all">
        <div class="flex items-center justify-between mb-6">
          <div class="w-11 h-11 rounded-2xl bg-purple-50 flex items-center justify-center text-purple-600 group-hover:bg-purple-600 group-hover:text-white transition-all">
            {% assign _ic = item.hero_icon | default: 'zap' %}{% include ui/icon.html name=_ic class="w-5 h-5" %}
          </div>
          <span class="font-mono text-[10px] font-bold uppercase tracking-widest text-slate-400">{{ item.read_time | default: "2 Min" }}</span>
        </div>
        <div class="flex items-center gap-2 mb-2 text-[11px] font-bold uppercase tracking-widest text-slate-400">
          <span>{{ item.date | date: "%b %d, %Y" }}</span>
          {% if item.category %}<span>•</span><span>{{ item.category }}</span>{% endif %}
        </div>
        <h2 class="text-xl font-bold text-slate-900 mb-3 leading-snug group-hover:text-purple-600 transition-colors">{{ item.title }}</h2>
        <p class="text-slate-500 text-sm leading-relaxed mb-5 flex-grow">{{ item.description | default: item.excerpt | strip_html | truncatewords: 24 }}</p>
        <span class="font-mono text-sm font-bold text-slate-900 flex items-center gap-1 group-hover:gap-2 group-hover:text-purple-600 transition-all">read {% include ui/icon.html name="arrow-right" class="w-3.5 h-3.5" %}</span>
      </a>
      {% endfor %}
    </div>
    {% else %}
    <div class="max-w-md rounded-3xl border border-dashed border-slate-200 p-10 text-center">
      <div class="w-12 h-12 rounded-2xl bg-purple-50 flex items-center justify-center text-purple-600 mx-auto mb-4">{% include ui/icon.html name="zap" class="w-6 h-6" %}</div>
      <p class="text-slate-600">First RevShorts are on the way. In the meantime, the <a href="{{ site.baseurl }}/blog" class="font-bold text-purple-600 hover:text-purple-700">blog</a> has the long-form pieces.</p>
    </div>
    {% endif %}
  </div>
</section>

{% include blog/home/blog_subscribe.html %}
{% include home/about_us_home.html %}
