---
layout: revshort
title: "Real-time is a wish, not a requirement"
description: "'This obviously has to run in real time.' The sentence comes up in almost every integration workshop, usually within the first ten minutes, and it almost never gets..."
date: 2026-06-04
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/083-echtzeit-ist-ein-wunsch-keine-anforderung/
---

"This obviously has to run in real time." The sentence comes up in almost every integration workshop, usually within the first ten minutes, and it almost never gets questioned. It sounds reasonable, after all. Who wants stale data?

Then we ask the counter-question: which decision is waiting on this data point, and how long can it afford to wait? That's when the room goes quiet. The payment status flowing back from billing into the CRM gets looked at once a day by someone in sales support. The management dashboard gets opened on Mondays. Enrichment of new accounts with company data needs to be done before a human touches the account, and that happens hours later at the earliest. For a good 95 percent of all data flows, a sync every 15 minutes is not a compromise. It's simply invisible.

The difference in effort, on the other hand, is very visible. Real-time means event-driven: webhooks that have to arrive reliably, retry logic for when the other side isn't responding, race conditions when two events overtake each other, API limits that snap under load spikes. All solvable. All expensive. A 15-minute batch, by contrast, is boring, robust engineering: fetch all records since the last run, process, write, and whatever fails simply gets picked up by the next run. Testable, traceable, a tenth of the complexity. And in integrations, complexity is not an abstract quantity. It's pretty much exactly the number of places where things can break at three in the morning.

The exceptions exist, and you should take them seriously. Speed-to-lead is real: if a demo request sits untouched for five minutes, connect rates measurably drop, so that one flow deserves to be built event-driven. The rep sitting in a customer meeting who needs the current contract status counts too. But that's two, maybe three flows per company. Not twenty.

So here's a simple proposal: write down an honest latency requirement for every data flow. Not a reflex answer, but a number with a reason. "15 minutes, because the report gets pulled at eight in the morning." "30 seconds, because an SDR should call while the lead is still on the website." Anyone who runs this exercise once discovers that the list consists almost entirely of quarter hours, and suddenly the integration project shrinks from six months of event architecture to three weeks of solid batch jobs.

"Instantly" is not a requirement. It's the absence of one, and you're paying five figures for it.
