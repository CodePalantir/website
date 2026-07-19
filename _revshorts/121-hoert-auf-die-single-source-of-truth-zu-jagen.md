---
layout: revshort
title: "Stop chasing the single source of truth"
description: "Three people, one meeting, one question: how many active customers do we have? Sales says 214, Finance says 189, the CS tool says 240. The reflex..."
date: 2026-07-12
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/121-hoert-auf-die-single-source-of-truth-zu-jagen/
---

Three people, one meeting, one question: how many active customers do we have? Sales says 214, Finance says 189, the CS tool says 240. The reflex response is the sentence that sits in every second RevOps vision deck: we finally need a single source of truth.

Except it does not exist. Nobody has ever built one, nobody ever will, and the reasons are structural, not a matter of craftsmanship. Your billing knows more about payments than the CRM ever will. Product analytics knows usage, the CRM knows the relationship, support knows the pain. Each of these systems holds its data authority for a good reason: that is where the process lives that produces the data. Whoever tries to force everything into one place anyway ends up either in a warehouse project that is still not finished after 18 months, or with a CRM with 900 fields, two thirds of them empty.

The achievable goal is more modest and considerably more valuable: one defined system of record per domain, and consistency in between. Customer master data is owned by the CRM, period. Payment status is owned by billing, and the CRM shows a synced copy that is recognizable as a copy. Usage data is owned by product analytics. For every important entity, it is written down which system wins in a conflict, in which direction syncing happens, and how fast. In the end, that is a two-page document plus the integrations that enforce it.

In daily life, that changes everything. The question of 214 versus 189 versus 240 is no longer a crisis of trust; it has an answer: 189, because Finance counts paying contracts and that is precisely the agreed definition of an active customer. The other numbers measure something else, and it says so right there. Fights over numbers are almost never a data problem. Usually what is missing is simply the agreement on which definition applies and who owns it.

A quick aside before the objection comes: a warehouse can still make sense later, as the place where the domains converge for reporting. But as a reporting layer on top of clean systems of record. Not as a magical place where truth emerges on its own.

The single source of truth is a poster on the wall. Systems of record with conflict rules are a Friday afternoon of work per domain. Which of the two did your last vision deck promise?
