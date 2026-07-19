---
layout: revshort
title: "You're operating on a beating heart"
description: "Friday, 4:40 p.m. The admin quickly builds one more validation rule in the production system, because sales leadership wanted it by Monday. No test,..."
date: 2026-05-31
read_time: "2 min read"
category: "Data"
hero_icon: "database"
lang: en
translation: /de/revshorts/079-ihr-aendert-am-offenen-herzen/
---

Friday, 4:40 p.m. The admin quickly builds one more validation rule in the production system, because sales leadership wanted it by Monday. No test, no sandbox, no second pair of eyes. Save, weekend.

Monday at 9, no field rep can close opportunities anymore, because the rule demands a field half the records never had. Two hours of sales standstill for 15 people, convert that into pipeline. And the absurd part: in the IT department next door, nobody would dream of pushing untested code straight to the production server on a Friday. There they have staging, reviews, deployment windows. Three rooms over, in the CRM, suddenly none of that applies.

Why, actually? Because clicking feels more harmless than coding. A validation rule, a flow, a new required field, that's just configuration, right? It is not. A flow that fires on every lead update is software. It has dependencies, side effects, edge cases. The fact that you click it together instead of typing it changes exactly nothing about that. The CRM is the system your revenue is managed in, and you treat it with less care than the company website.

The objection always comes immediately: sandbox processes slow us down, we're not an enterprise. Not quite. The process for a 50-person company isn't a deployment pipeline with four approval stages. It's three habits. First: changes to logic that touches other records get built in the sandbox and played through with real cases, including the ugly ones, the records from 2021 with half-empty fields. Second: deployments have a time window, and Friday afternoon isn't in it, because by then nobody's left to notice the error before it bends data for an entire weekend. Third: every change gets noted somewhere, one sentence is enough. What, why, who.

That costs maybe 20 extra minutes per change. A single prevented Monday-morning outage pays that back for a year, to say nothing of the silent damage, the automations that quietly write wrong data for weeks until someone notices it in the forecast.

Deployment discipline isn't a question of company size, it's a question of how much you care about the system that manages your deals. When was your last change made straight in production, and who tested it besides luck?
