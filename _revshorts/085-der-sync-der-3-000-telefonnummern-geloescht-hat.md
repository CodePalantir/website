---
layout: revshort
title: "The sync that deleted 3,000 phone numbers"
description: "Monday morning, 8:30. The SDR team opens the call lists and the phone number field is empty. Not on one contact. On 3,000."
date: 2026-06-06
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/085-der-sync-der-3-000-telefonnummern-geloescht-hat/
---

Monday morning, 8:30. The SDR team opens the call lists and the phone number field is empty. Not on one contact. On 3,000.

What happened? Friday evening the new sync went live, marketing tool and CRM, bidirectional, cleanly mapped, all fields connected. In the marketing tool, the phone field was empty on almost every contact, because it was never maintained there. The sync was set to "source system wins". So overnight it did exactly what it was told: it overwrote 3,000 painstakingly researched, verified numbers, maintained over years, with nothing. Three years of data work, synced away in 40 minutes.

The mistake isn't exotic. It's the most common integration mistake there is, and it happens because bidirectional syncs get treated as a mapping exercise. Field A to field B, check the box, next field. Nobody asks the actual question: who owns this field? Field-level ownership means naming a master system for every synced field. The phone number belongs to the CRM, that's where it's maintained, the marketing tool may read, never write. Email opt-in belongs to the marketing tool, for legal reasons it actually must. Company name maybe belongs to the enrichment tool. That's one row in a table per field and a decision that takes ten seconds. With 60 fields, one morning.

Add conflict rules for the cases where both sides are allowed to write. The most important one is trivial and still gets violated constantly: empty never overwrites filled. A missing value is not information, it's the absence of information, and absence must never kill data. Second rule: newer only wins with a real timestamp comparison at the field level, not the record level, otherwise a changed salutation field drags the old address along with it.

And before go-live, the sync belongs in a run against a sandbox copy, with a diff report: these 4,200 field values would change, here's the sample. Whoever reads that report sees the 3,000 empty phone numbers before they happen. Plus a full export as a backup, right before flipping the switch. Total effort for all of this: one to two days. The damage in the real case: three weeks of reconstruction from phone system logs and old CSV exports, plus an SDR team that couldn't dial for a week.

When two of your systems contradict each other, who wins? If you don't know the answer: your sync doesn't know it either. It decides anyway. Every night.
