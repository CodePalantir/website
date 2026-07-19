---
layout: revshort
title: "Even flawless automation costs money every month"
description: "The flow has been running for two years without a single error. Sounds like a finished project. It isn't."
date: 2026-07-11
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/120-auch-fehlerfreie-automatisierung-kostet-jeden-monat-geld/
---

The flow has been running for two years without a single error. Sounds like a finished project. It isn't.

Three kinds of cost keep running, invisible but real. Understanding: someone on the team has to know what the flow does, why it does it, and what happens if you touch it. When the colleague who built it left, that knowledge left with her, and since then nobody dares go near the automation that sets the opportunity status. Maintenance: the API the flow calls gets a new version, the field it listens to gets renamed, the tool on the other end changes its behavior after an update. None of that is an error in the flow, all of it creates work. And the most expensive of the three, dependencies: every new process has to be built around the existing 40 automations. The question "can we rename this field" takes five minutes in a fresh org. In a grown one, it is two days of impact analysis.

Hence the proposal: think in terms of a complexity budget. Every automation, every integration, every custom field spends some of it, entirely regardless of whether it works. The budget is finite, it depends on the size and seniority of your team, and when it is overdrawn, you notice through one clear symptom: simple changes suddenly take weeks, and nobody holds the whole system in their head anymore.

Through that lens, decisions come out differently. The report that is needed once a quarter? Build it by hand, twenty minutes, four times a year. The data handoff to a tool that might get kicked out next year? A CSV export is plenty. The approval step where a human is supposed to look anyway? Then let the human look, instead of building logic that simulates human judgment and produces edge cases someone has to maintain in return.

Sometimes the manual step is the right architecture. Coming from an engineering firm that may sound strange, but it is exactly the experience from the orgs we clean up: the worst ones are never the ones with too little automation. They are the ones with 200 flows, 60 of which nobody can explain anymore.

You automate what happens frequently, is stably defined, and demonstrably eats time. The rest stays manual, deliberately and documented. How much of your complexity budget is already spent, and on what?
