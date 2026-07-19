---
layout: revshort
title: "Friday, 5 p.m., just a small thing"
description: "The message always arrives at the same time. Friday, just before five: 'Can you quickly put a validation rule on the opportunity? Just a small thing,..."
date: 2026-06-20
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/099-freitag-17-uhr-nur-eine-kleinigkeit/
---

The message always arrives at the same time. Friday, just before five: "Can you quickly put a validation rule on the opportunity? Just a small thing, Monday is pipeline review." The admin wants to start the weekend, clicks the rule together, activates it, done for the day.

What the rule does over the weekend, nobody sees. The nightly import from the webshop fails against it, silently, 600 records left stranded. The marketing automation tries to convert leads and runs into the same wall. Monday morning the pipeline is formally cleaner for the review, but it's missing two days of data, and three people spend the morning troubleshooting instead of doing the review the rule was built for.

There is no such thing as a small thing in the CRM. Every validation rule, every new required status, every changed automation intervenes in a system that integrations, imports, and other automations hang off of, and those don't keep office hours. More runs in your CRM at night than during the day. Which is exactly when nobody is around to notice.

Software teams learned this twenty years ago and turned it into rules. Deployment windows: changes go live Tuesday through Thursday mornings, when people are around who can react. Freeze periods: no deployment before weekends, none in the last week of the quarter, when the forecast is locked and every status change shifts numbers the board will discuss on Monday. And nothing goes straight to production that hasn't been tested in the sandbox against the running integrations first.

Sounds like enterprise bureaucracy for a company of 60? It's the opposite. The rules fit on half a page and cost nothing except the willingness to say no once. "Happy to, it goes live Tuesday morning" is a complete sentence. Whoever truly has an emergency can escalate, but then it's called an emergency and someone stays on it until the night runs are through.

The real win isn't the admin's rescued weekend, although that counts too. It's the data quality. Almost every dead record we find in audits has a timestamp, and a striking number of them fall between Friday evening and Monday morning.

Your head of manufacturing would never let someone rebuild a machine at five on a Friday and then lock up. Why is that allowed to happen in the system where your entire revenue is made?
