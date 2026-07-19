---
layout: revshort
title: "Required fields produce the garbage they're supposed to prevent"
description: "There's a law of nature in every CRM, and it goes: every required field gets filled. Just not necessarily with the truth."
date: 2026-05-24
read_time: "2 min read"
category: "Outbound"
hero_icon: "send"
lang: en
translation: /de/revshorts/072-pflichtfelder-produzieren-den-muell-den-sie-verhindern-s/
---

There's a law of nature in every CRM, and it goes: every required field gets filled. Just not necessarily with the truth.

The story always begins the same way. A report is full of holes, industry is missing on half the accounts, so someone makes the field required. Sounds logical. Three months later, 200 accounts say "Other," 80 say "test," and a few contain a single period, because the rep figured out the system accepts a period. The report is no longer full of holes. It's wrong. And wrong is worse than empty, because an empty field honestly says "I don't know," while a wrong field pretends to know something.

The rep is acting entirely rationally. He wants to create an opportunity, the call is still running, the customer is waiting, and the system now demands the employee count, the industry, and the lead channel on the spot. So he types whatever. The save button is his goal, not your data quality. Answer that with even more requirements, with validation rules on top of the validation rules, and all you breed is more creative placeholders. I've seen orgs where "tbd" was the most common industry value. In second place: "TBD."

The real question is never "how do I force the rep," but "why does a human have to type this at all." Employee count, industry, revenue band, country: all data an enrichment service delivers more reliably than any salesperson, automatically, at account creation. Lead source belongs set technically, from the form, from the campaign, from the UTM parameter, and never in a human's hands. What remains as genuine human input is short: the things only the rep can know, because they were said in the conversation. Next step, decision process, pain point. And even those are better asked at the stage change than at creation, at the moment the information actually exists.

A usable rule of thumb: more than five manual required fields per object is a design flaw. Not because five is a magic number, but because beyond it, the placeholder rate grows faster than the information gain.

Run the test. Pull the value distribution of your three oldest required fields and count how often "Other," "test," and their relatives show up. If it's more than ten percent, you don't have a discipline problem in sales. You have a form that forces lies.
