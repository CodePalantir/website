---
layout: revshort
title: "Bidirectional means two truths"
description: "'The sync should be bidirectional, all fields, both directions.' This sentence comes up in almost every integration project, usually early, usually..."
date: 2026-06-02
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/081-bidirektional-heisst-doppelte-wahrheit/
---

"The sync should be bidirectional, all fields, both directions." This sentence comes up in almost every integration project, usually early, usually in passing. It sounds like completeness. What it actually orders is data chaos with a delivery date.

Because bidirectional across all fields means: there is no leading source anymore. Two systems may change the same information, and some mechanism has to decide who wins. Usually the last write wins. Sounds fair, is roulette. Marketing corrects the industry in the MAP, three minutes later a CRM workflow overwrites it with the old value, because it touched the record for an entirely different reason. Nobody sees it. There's no error, no alert, just two systems quietly writing each other's data to pieces. The classic is the sync loop: system A updates, B syncs back, A registers that as a change, syncs again, and suddenly you're wondering why the API quota is empty at 3 a.m.

The pain is double because the truth is double too. If the CRM shows a different phone number than the support tool, which one is right? Without defined leadership, the answer is: no idea, depends on who saved last. That's the moment sales stops trusting the data and starts maintaining Excel lists again. Then you have three truths.

The solution is unspectacular and has worked for decades: one system leads, the other follows, decided per field, not blanket per object. Company name and industry are led by the CRM, because that's where enrichment and verification happen. Consent status is led by the marketing tool, because that's where the opt-ins originate. Ticket volume is led by the support system, the CRM only displays it. That yields a table, maybe 40 rows: field, owner, direction, conflict rule. A boring table, admittedly. It's the most valuable document of the entire integration, and producing it takes one afternoon with the right people at the table.

Genuine two-way cases remain, sure, an opportunity status both sides have to keep advancing. You handle those individually, with timestamps and explicit conflict logic, and you keep the list as short as humanly possible.

Whoever sells you "both directions, all fields" as a feature has either never thought through the conflict cases or is firmly counting on you booking them again for the cleanup. Which of your fields actually has an owner today?
