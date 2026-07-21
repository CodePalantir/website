---
layout: default
title: Contact – Talk to APX
description: "Tell us what your revenue systems should be doing and where they fall short. We reply within one working day."
permalink: /contact/
lang: en
translation: /de/kontakt/
---

<!-- 1. HERO + FORM -->
<section class="px-6 bg-paper pt-[clamp(7rem,15vh,10rem)] pb-[clamp(4rem,8vh,7rem)]">
  <div class="max-w-wide mx-auto">
    <div class="grid lg:grid-cols-[0.9fr_1.1fr] gap-12 lg:gap-20 items-start">

      <!-- Left: talk to us -->
      <div class="rv">
        <span class="apx-eyebrow">Contact</span>
        <h1 class="mt-4 font-bold text-ink tracking-[-0.03em] leading-[1.03] text-[clamp(2.5rem,5.2vw,4.25rem)]" style="text-wrap:balance">Let&#8217;s <span class="text-gradient">talk.</span></h1>
        <p class="mt-5 max-w-[46ch] text-[clamp(1.05rem,1.4vw,1.3rem)] leading-relaxed text-muted">Tell us what your revenue systems should be doing and where they fall short. We reply within one working day.</p>

        <div class="mt-10 space-y-5">
          <a href="mailto:{{ site.contact.email }}" class="flex items-center gap-4 group">
            <span class="inline-grid place-items-center w-11 h-11 rounded-xl bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="mail" class="w-5 h-5" %}</span>
            <span class="text-[17px] font-semibold text-ink group-hover:text-accent transition-colors">{{ site.contact.email }}</span>
          </a>
          <a href="{{ site.contact.phone_href }}" data-ap-track="call" data-ap-category="contact" class="flex items-center gap-4 group">
            <span class="inline-grid place-items-center w-11 h-11 rounded-xl bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="phone-call" class="w-5 h-5" %}</span>
            <span class="text-[17px] font-semibold text-ink group-hover:text-accent transition-colors">{{ site.contact.phone_display }}</span>
          </a>
          <a href="{{ site.contact.linkedin }}" target="_blank" rel="noopener noreferrer" class="flex items-center gap-4 group">
            <span class="inline-grid place-items-center w-11 h-11 rounded-xl bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="linkedin" class="w-5 h-5" %}</span>
            <span class="text-[17px] font-semibold text-ink group-hover:text-accent transition-colors">APX on LinkedIn</span>
          </a>
          <div class="flex items-center gap-4">
            <span class="inline-grid place-items-center w-11 h-11 rounded-xl bg-accent-tint text-accent shrink-0">{% include ui/icon.html name="map-pin" class="w-5 h-5" %}</span>
            <span class="text-[17px] font-medium text-muted">Gladstonos 16, 8046 Paphos, Cyprus</span>
          </div>
        </div>

        <div class="mt-10 apx-card p-6">
          <p class="text-[15px] font-bold text-ink">Rather talk it through live?</p>
          <p class="mt-1.5 text-[14.5px] leading-relaxed text-muted">Skip the form and grab a slot straight in the calendar.</p>
          <div class="mt-5 space-y-3">
            <a href="https://calendly.com/apx-revops/intro-call?utm_source=website&utm_content=contact-page" target="_blank" rel="noopener noreferrer" data-ap-track="book-call" data-ap-category="contact-page" data-ap-value="intro" class="flex items-center gap-3.5 p-3.5 rounded-xl border border-line bg-surface hover:border-accent/40 hover:shadow-md transition-all group">
              <span class="inline-grid place-items-center w-10 h-10 rounded-lg bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="message-circle" class="w-5 h-5" %}</span>
              <span class="flex-1">
                <span class="block text-[15px] font-bold text-ink group-hover:text-accent transition-colors">Intro call</span>
                <span class="block text-[13px] text-faint">30 min, no prep needed</span>
              </span>
              {% include ui/icon.html name="arrow-right" class="w-4 h-4 text-faint group-hover:text-accent group-hover:translate-x-1 transition-all" %}
            </a>
            <a href="https://calendly.com/apx-revops/audit-scoping?utm_source=website&utm_content=contact-page" target="_blank" rel="noopener noreferrer" data-ap-track="book-call" data-ap-category="contact-page" data-ap-value="audit" class="flex items-center gap-3.5 p-3.5 rounded-xl border border-line bg-surface hover:border-accent/40 hover:shadow-md transition-all group">
              <span class="inline-grid place-items-center w-10 h-10 rounded-lg bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="heart-pulse" class="w-5 h-5" %}</span>
              <span class="flex-1">
                <span class="block text-[15px] font-bold text-ink group-hover:text-accent transition-colors">Audit scoping call</span>
                <span class="block text-[13px] text-faint">30 min, start the €2,450 audit</span>
              </span>
              {% include ui/icon.html name="arrow-right" class="w-4 h-4 text-faint group-hover:text-accent group-hover:translate-x-1 transition-all" %}
            </a>
            <a href="https://calendly.com/apx-revops/managed-partnership-interview?utm_source=website&utm_content=contact-page" target="_blank" rel="noopener noreferrer" data-ap-track="book-call" data-ap-category="contact-page" data-ap-value="partner" class="flex items-center gap-3.5 p-3.5 rounded-xl border border-line bg-surface hover:border-accent/40 hover:shadow-md transition-all group">
              <span class="inline-grid place-items-center w-10 h-10 rounded-lg bg-accent-tint text-accent shrink-0 transition-colors group-hover:bg-purple-gradient group-hover:text-white">{% include ui/icon.html name="crown" class="w-5 h-5" %}</span>
              <span class="flex-1">
                <span class="block text-[15px] font-bold text-ink group-hover:text-accent transition-colors">Managed partnership interview</span>
                <span class="block text-[13px] text-faint">45 min, for retainer engagements</span>
              </span>
              {% include ui/icon.html name="arrow-right" class="w-4 h-4 text-faint group-hover:text-accent group-hover:translate-x-1 transition-all" %}
            </a>
          </div>
        </div>
      </div>

      <!-- Right: the request form (Netlify Forms) -->
      <div class="apx-card p-7 md:p-10 rv">
        <form name="contact" method="POST" action="/contact/thanks/" data-netlify="true" netlify-honeypot="bot-field" class="space-y-6">
          <input type="hidden" name="form-name" value="contact">
          <p class="hidden"><label>Don&#8217;t fill this out if you&#8217;re human: <input name="bot-field"></label></p>

          <div class="grid sm:grid-cols-2 gap-6">
            <div>
              <label for="c-name" class="block text-sm font-semibold text-ink mb-2">Name <span class="text-accent">*</span></label>
              <input type="text" id="c-name" name="name" required autocomplete="name" placeholder="Your name"
                     class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all">
            </div>
            <div>
              <label for="c-email" class="block text-sm font-semibold text-ink mb-2">Work email <span class="text-accent">*</span></label>
              <input type="email" id="c-email" name="email" required autocomplete="email" placeholder="you@company.com"
                     class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all">
            </div>
          </div>

          <div class="grid sm:grid-cols-2 gap-6">
            <div>
              <label for="c-company" class="block text-sm font-semibold text-ink mb-2">Company</label>
              <input type="text" id="c-company" name="company" autocomplete="organization" placeholder="Company name"
                     class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all">
            </div>
            <div>
              <label for="c-phone" class="block text-sm font-semibold text-ink mb-2">Phone</label>
              <input type="tel" id="c-phone" name="phone" autocomplete="tel" placeholder="Optional"
                     class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all">
            </div>
          </div>

          <div>
            <label for="c-topic" class="block text-sm font-semibold text-ink mb-2">What is this about?</label>
            <select id="c-topic" name="topic"
                    class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all cursor-pointer">
              <option>Technical Health Audit</option>
              <option>Salesforce or HubSpot work</option>
              <option>Integration or data project</option>
              <option>Managed support</option>
              <option>Something else</option>
            </select>
          </div>

          <div>
            <label for="c-message" class="block text-sm font-semibold text-ink mb-2">How can we help? <span class="text-accent">*</span></label>
            <textarea id="c-message" name="message" required rows="5" placeholder="A few lines about your stack and what is not working the way it should."
                      class="block w-full px-4 py-3.5 border border-line rounded-xl bg-surface text-ink placeholder-faint focus:outline-none focus:ring-2 focus:ring-accent focus:border-transparent transition-all resize-y"></textarea>
          </div>

          <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 pt-1">
            <button type="submit" data-ap-track="contact-submit" class="apx-btn apx-btn-accent">
              Send my request
              {% include ui/icon.html name="arrow-right" class="w-[18px] h-[18px]" %}
            </button>
            <p class="text-[13px] text-faint">No newsletters, no drip sequence. Just an answer.</p>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>
