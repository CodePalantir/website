---
layout: default
title: Request received
description: "Your request is in. We reply within one working day."
permalink: /contact/thanks/
sitemap: false
---

<section class="px-6 bg-paper pt-[clamp(8rem,18vh,12rem)] pb-[clamp(5rem,10vh,8rem)]">
  <div class="max-w-wide mx-auto text-center">
    <div class="max-w-[560px] mx-auto rv">
      <span class="inline-grid place-items-center w-14 h-14 rounded-2xl bg-purple-gradient text-white mx-auto">{% include ui/icon.html name="check" class="w-7 h-7" %}</span>
      <h1 class="mt-6 font-bold text-ink tracking-[-0.025em] leading-[1.06] text-[clamp(2.25rem,4.5vw,3.5rem)]" style="text-wrap:balance">Got it. <span class="text-gradient">Thank you.</span></h1>
      <p class="mt-5 text-lg leading-relaxed text-muted">Your request is in and a real person will read it. We reply within one working day, usually faster.</p>
      <div class="mt-9 flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="{{ '/' | relative_url }}" class="apx-btn apx-btn-primary">Back to home</a>
        <a href="{{ '/revshorts' | relative_url }}" class="apx-btn apx-btn-ghost">Read a RevShort meanwhile</a>
      </div>
    </div>
  </div>
</section>
