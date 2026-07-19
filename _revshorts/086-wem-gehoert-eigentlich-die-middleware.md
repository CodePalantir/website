---
layout: revshort
title: "Who actually owns the middleware?"
description: "Almost every company we audit has it: the integration a freelancer built in 2022. Runs on a server whose credentials live in an old Slack thread, or as a..."
date: 2026-06-07
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/086-wem-gehoert-eigentlich-die-middleware/
---

Almost every company we audit has it: the integration a freelancer built in 2022. Runs on a server whose credentials live in an old Slack thread, or as a Make scenario in the personal account of someone who left last year. It connects CRM and billing, or shop and CRM, or all three. It runs. Until it doesn't.

And then something interesting happens, namely a very predictable sequence. The customer notices first: the order confirmation doesn't arrive, the invoice is missing, the onboarding call never gets booked. Sales notices next, because deals are missing from the forecast or payment statuses sit on "open" that were settled long ago. You yourselves notice last, often only when the third customer calls. This sequence isn't bad luck. It's the logical consequence of an integration without monitoring only surfacing through symptoms, and symptoms happen out there, at the money and at the customer.

The ownership hole is systemic. There's an admin for the CRM. Marketing owns the website. Accounting owns billing. But the data flow in between, the exact place where revenue information travels from one system to the next, belongs to no one. "It's running fine" is not an operating model. It's the absence of one.

What a data flow needs is manageable. First, a name on the org chart, a person, not a team, because nobody calls "the team" at night. Second, monitoring that reports the failure before the customer does: an error queue that failed records fall into instead of vanishing, a heartbeat that raises an alarm when the sync goes silent, an alert into a channel someone actually reads. Third, one page of documentation. Which flows exist, where they run, where the credentials live, what to do on error X. For a typical company our size, that's one afternoon of work per integration. Not a project, an afternoon.

The test is simple and stings a little. Open your org chart and point at the person who gets called when the sync between CRM and billing stops at two in the morning tonight. If your finger points at nothing, you now know who will notice first. Not you.
