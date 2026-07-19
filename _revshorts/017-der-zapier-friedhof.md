---
layout: revshort
title: "The Zapier graveyard"
description: "Stack inventory at a client, 60 people, solid growth: 47 zaps. Built over four years by four different people, two of whom no longer work there...."
date: 2026-03-30
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/017-der-zapier-friedhof/
---

Stack inventory at a client, 60 people, solid growth: 47 zaps. Built over four years by four different people, two of whom no longer work there. Documentation doesn't exist, naming conventions don't either, one zap is called "Test Copy 2 FINAL". And one of them, the one that hands deals to the invoicing tool, has been silently failing for three weeks because somebody renamed a field in the CRM. Nobody noticed. It only surfaced when a customer called to ask where his invoice was.

That's not a Zapier problem. Zapier and Make are perfectly legitimate tools, for prototypes even the best: in an hour you have a workflow you can observe for a while before building it properly. For low-volume stuff that hurts nobody when it fails, the Slack message on new deals, the export into a sheet, there's nothing wrong with them long term either.

The problem starts at a clearly nameable line, and that line is called business-critical. The moment a workflow touches revenue, routes leads, triggers invoices, kicks off contracts, the requirement changes fundamentally. Not the function. The error handling.

That's exactly where the difference between automation glue and integration architecture lives. Glue executes as long as everything goes well. Architecture assumes things will go wrong, because they do. APIs have timeouts, systems have maintenance windows, coworkers rename fields. An integration that ignores this isn't a smaller version of a real integration. It's a ticking one, except nobody knows how loud the bang will be or when.

Concretely, architecture means three things. Monitoring: when something fails, an alert reaches a human within minutes, not a log nobody reads. Retry logic: a timeout at 3 a.m. gets retried automatically instead of silently discarded, and whatever still fails after three attempts lands in a queue for manual review, so no record simply vanishes. And ownership: a person with a name is responsible, knows the routes, gets informed before anyone touches a field. Whether Make runs underneath, or n8n, Workato, or custom code, is honestly secondary.

So the question for your stack isn't which automation tool you use. The question is: if your most important route breaks tonight, who notices, and when? If the answer is "the customer, next week," you know what to do.
