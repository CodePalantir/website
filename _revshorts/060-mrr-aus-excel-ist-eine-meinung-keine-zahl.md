---
layout: revshort
title: "MRR from Excel is an opinion, not a number"
description: "Start of the month. Someone from Finance exports the invoices, opens last month's Excel template, adjusts three formulas, strips out the one annual..."
date: 2026-05-12
read_time: "2 min read"
category: "RevOps"
hero_icon: "zap"
lang: en
translation: /de/revshorts/060-mrr-aus-excel-ist-eine-meinung-keine-zahl/
---

Start of the month. Someone from Finance exports the invoices, opens last month's Excel template, adjusts three formulas, strips out the one annual contract that otherwise distorts everything, and sends the MRR number to management. Duration: half a day. Result: a number that comes into being slightly differently every month.

That is exactly the problem. Not the half day. The wobbly definition.

MRR sounds trivial and is not. What happens with the customer who upgrades on the 15th? Does the first-year discount count? Is the paused contract churn or not? How do you handle setup fees, credit notes, the customer who pays in dollars? Every one of these questions has several defensible answers. As long as the answer lives in the head of whoever is building the Excel right now, it changes with the person, the daily form, and the time pressure. Two people, the same raw data, two different churn rates. Both can justify their version. Neither is the truth.

Hence the hard rule: subscription metrics come defined and automated out of the billing system, or they are opinion. Stripe Billing and Chargebee calculate MRR, churn, and NRR out of the box, with documented, stable definitions. If you have edge cases or want more precision, pull the raw data into the warehouse and write the logic once as code, versioned, readable, forever the same. Either is a matter of days, not quarters.

The real win is not the time saved. It is the resilience of the number. When your NRR gets picked apart in the next bank meeting or in a due diligence, "our colleague Meier always calculates that in Excel" builds no trust. A metric whose derivation lives in the billing system or in the dbt model survives every follow-up question. An Excel with 14 tabs does not even survive the question of why cell G47 was hard-overwritten. Surely there was a good reason. Nobody remembers it anymore.

And yes, the Excel feels flexible, that is its whole charm. You can quickly strip out the edge case. But that flexibility is exactly the property that devalues a metric: a number that can be adapted to the situation no longer measures anything.

The diagnosis costs you five minutes. Ask two people in the company for the current MRR and for the definition of churn. If two different answers come back, you do not have metrics. You have folklore.
