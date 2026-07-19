---
layout: default
title: RevShorts – Short RevOps Reads
description: "RevShorts are 400 to 500 word reads on a single RevOps idea: one pattern, one failure mode, one fix. From the APX team."
image: /assets/images/logos/APX_LOGO.png
---

<!-- REVSHORTS HERO, same pattern as the articles hub hero -->
<section class="relative overflow-hidden bg-[linear-gradient(180deg,#FFFFFF_0%,#FBF9FF_55%,#FAF8F5_100%)]">
  <div class="apx-hero-grid"></div>
  <div class="apx-hero-glow"></div>
  <div class="relative z-[4] pt-36 md:pt-44 pb-12 md:pb-16 px-4 sm:px-6">
    <div class="max-w-wide mx-auto text-center">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-accent-tint text-accent border border-accent/15 text-[12px] font-bold uppercase tracking-[0.14em] mb-6">
        RevShorts
      </div>
      <h1 class="font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.4rem,5.2vw,4.25rem)] mb-6 sm:mb-8" style="text-wrap:balance">One idea. <span class="text-gradient">Two minutes.</span></h1>
      <p class="text-[17.5px] md:text-[19px] leading-relaxed font-medium text-muted max-w-3xl mx-auto">
        Short reads on a single RevOps idea: one pattern, one failure mode, one fix. No filler, no consulting cycle. For the longer pieces, see the <a href="{{ site.baseurl }}/articles" class="font-bold text-accent hover:text-accent-strong transition-colors">articles</a>.
      </p>
    </div>
  </div>
</section>

<!-- SEARCH + CATEGORY FILTER, same feature as the articles hub -->
<section class="px-6 pb-12 bg-paper">
  <div class="max-w-2xl mx-auto">
    <div class="relative group">
      <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
        {% include ui/icon.html name="search" class="h-5 w-5 text-faint group-focus-within:text-accent transition-colors" %}
      </div>
      <input type="text"
              id="rs-search-input"
              class="block w-full pl-11 pr-4 py-4 border border-line rounded-2xl leading-5 bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent sm:text-sm shadow-sm transition-all cursor-text"
              placeholder="Search RevShorts by topic or keyword..."
      >
      <div class="absolute inset-y-0 right-0 pr-2 flex items-center">
        <button id="rs-clear-search" class="p-2 text-faint hover:text-ink cursor-pointer hidden" aria-label="Clear search">
          {% include ui/icon.html name="x" class="h-5 w-5" %}
        </button>
      </div>
    </div>
    <div id="rs-category-filters" class="flex gap-2 mt-4 justify-center overflow-x-auto no-scrollbar">
      <button data-category="all" class="rs-category-btn px-4 py-1.5 rounded-full border text-xs font-bold transition-colors whitespace-nowrap cursor-pointer bg-purple-gradient border-transparent text-white">All</button>
      {% assign rs_cats = site.revshorts | map: 'category' | compact | uniq | sort %}
      {% for cat in rs_cats %}
      <button data-category="{{ cat }}" class="rs-category-btn px-4 py-1.5 rounded-full bg-surface border border-line text-xs font-bold text-muted hover:border-accent hover:text-accent transition-colors whitespace-nowrap cursor-pointer">{{ cat }}</button>
      {% endfor %}
    </div>
  </div>
</section>

<!-- REVSHORTS GRID, restored card grid, warm surfaces -->
<section class="pb-16 md:pb-24 px-4 sm:px-6 bg-paper">
  <div class="max-w-wide mx-auto">
    {% assign shorts = site.revshorts | sort: 'date' | reverse %}
    {% if shorts.size > 0 %}
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 sm:gap-6">
      {% for item in shorts %}
      <a href="{{ site.baseurl }}{{ item.url }}" class="apx-card group p-7 revshort-card" data-title="{{ item.title | escape }}" data-category="{{ item.category | escape }}" data-excerpt="{{ item.description | default: item.excerpt | strip_html | truncatewords: 40 | escape }}">
        <div class="flex items-center justify-between mb-6">
          <div class="w-11 h-11 rounded-2xl bg-accent-tint flex items-center justify-center text-accent group-hover:bg-purple-gradient group-hover:text-white transition-all">
            {% assign _ic = item.hero_icon | default: 'zap' %}{% include ui/icon.html name=_ic class="w-5 h-5" %}
          </div>
          <span class="apx-label">{{ item.read_time | default: "2 Min" }}</span>
        </div>
        <div class="flex items-center gap-2 mb-2 text-[11px] font-bold uppercase tracking-widest text-faint">
          <span>{{ item.date | date: "%b %d, %Y" }}</span>
          {% if item.category %}<span aria-hidden="true">&bull;</span><span>{{ item.category }}</span>{% endif %}
        </div>
        <h2 class="text-xl font-bold text-ink mb-3 leading-snug group-hover:text-accent-strong transition-colors" style="text-wrap:balance">{{ item.title }}</h2>
        <p class="text-muted text-sm leading-relaxed mb-5 flex-grow">{{ item.description | default: item.excerpt | strip_html | truncatewords: 24 }}</p>
        <span class="font-mono text-sm font-bold text-ink flex items-center gap-1 group-hover:gap-2 group-hover:text-accent transition-all">read {% include ui/icon.html name="arrow-right" class="w-3.5 h-3.5" %}</span>
      </a>
      {% endfor %}
    </div>
    <div id="rs-no-results" class="hidden max-w-md mx-auto apx-card border-dashed p-10 text-center">
      <div class="w-12 h-12 rounded-2xl bg-accent-tint flex items-center justify-center text-accent mx-auto mb-4">{% include ui/icon.html name="search" class="w-6 h-6" %}</div>
      <p class="text-muted">Nothing matches that yet. Try another keyword or category.</p>
    </div>
    {% else %}
    <div class="max-w-md apx-card border-dashed p-10 text-center">
      <div class="w-12 h-12 rounded-2xl bg-accent-tint flex items-center justify-center text-accent mx-auto mb-4">{% include ui/icon.html name="zap" class="w-6 h-6" %}</div>
      <p class="text-muted">First RevShorts are on the way. In the meantime, the <a href="{{ site.baseurl }}/articles" class="font-bold text-accent hover:text-accent-strong">articles</a> have the long-form pieces.</p>
    </div>
    {% endif %}
  </div>
</section>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('rs-search-input');
    const clearBtn = document.getElementById('rs-clear-search');
    const categoryBtns = document.querySelectorAll('.rs-category-btn');
    const cards = document.querySelectorAll('.revshort-card');
    const noResults = document.getElementById('rs-no-results');
    let activeCategory = 'all';

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();
            if (clearBtn) clearBtn.classList.toggle('hidden', query.length === 0);
            filterShorts(query, activeCategory);
        });
    }

    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            searchInput.value = '';
            clearBtn.classList.add('hidden');
            filterShorts('', activeCategory);
        });
    }

    categoryBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            activeCategory = this.dataset.category;
            categoryBtns.forEach(b => {
                b.classList.remove('bg-purple-gradient', 'border-transparent', 'text-white');
                b.classList.add('bg-surface', 'border-line', 'text-muted');
            });
            this.classList.remove('bg-surface', 'border-line', 'text-muted');
            this.classList.add('bg-purple-gradient', 'border-transparent', 'text-white');
            filterShorts(searchInput ? searchInput.value.toLowerCase().trim() : '', activeCategory);
        });
    });

    function filterShorts(query, category) {
        let visible = 0;
        cards.forEach(card => {
            const title = (card.dataset.title || '').toLowerCase();
            const cardCategory = card.dataset.category || '';
            const excerpt = (card.dataset.excerpt || '').toLowerCase();
            const matchesSearch = query === '' || title.includes(query) || excerpt.includes(query);
            const matchesCategory = category === 'all' || cardCategory === category;
            const show = matchesSearch && matchesCategory;
            card.style.display = show ? '' : 'none';
            if (show) visible++;
        });
        if (noResults) noResults.classList.toggle('hidden', visible > 0);
    }
});
</script>

{% include blog/home/blog_subscribe.html %}
{% include sections/cta-band.html %}
