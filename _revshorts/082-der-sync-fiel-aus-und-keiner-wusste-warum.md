---
layout: revshort
title: "The sync failed, and nobody knew why"
description: "Tuesday morning, the dashboards are empty. The sync between shop and CRM didn't run overnight, the log says something like 'REQUEST_LIMIT_EXCEEDED,' and..."
date: 2026-06-03
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/082-der-sync-fiel-aus-und-keiner-wusste-warum/
---

Tuesday morning, the dashboards are empty. The sync between shop and CRM didn't run overnight, the log says something like "REQUEST_LIMIT_EXCEEDED," and the colleague who built the integration two years ago says the sentence that explains everything: "I didn't even know there was a limit."

Every API has limits. Salesforce counts calls per 24 hours, tiered by edition and licenses. HubSpot throttles per 10 seconds. Stripe, Shopify, every marketing tool: quotas, throttling, concurrency limits everywhere. That's not harassment, that's the physics of shared infrastructure, and it's on the first pages of every doc. Still, integrations get built by the dozen as if the API were an infinite faucet. One record, one call, in a loop, 80,000 times. Runs beautifully in the test with 50 records. Runs fine in production for three months too, until the data volume grows, a second team hangs its own automation on the same quota, and the two eat each other's budget away at night.

The annoying part: the solutions are textbook material. Batching, meaning 200 records per call instead of one, cuts consumption by a factor of 200, and most APIs offer bulk endpoints for exactly that. Backoff means that when throttled, the integration doesn't stubbornly knock again right away, but waits, at growing intervals, and then resumes cleanly instead of losing half the import. Add monitoring that shows quota consumption before it hits 100 percent. None of this is exotic. It just has to be planned in at the beginning, not at the end.

And that's exactly where the line between tinkering and engineering runs. The tinkerer asks: can I get the data from A to B? The engineer asks: what happens at 10x the data volume, what happens when the other side throttles, what happens when the job dies midway, and how will we notice? Both integrations look identical in the demo. The difference shows at three in the morning, months later, and then it's not in the old proposal, it's in today's postmortem.

Limits, batching, and backoff belong in the integration design, on page one, next to the data mapping. If you first meet them in an incident, you didn't buy an integration, you bought a prototype in permanent production. Do you actually know how much of your API quota got consumed last night, and by what?
