---
layout: revshort
title: "Agency or in-house admin is the wrong question"
description: "The question comes up in almost every first call: should we hand the CRM to an agency or hire someone? As if it were an either-or. Both answers are..."
date: 2026-06-23
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/102-agentur-oder-eigener-admin-ist-die-falsche-frage/
---

The question comes up in almost every first call: should we hand the CRM to an agency or hire someone? As if it were an either-or. Both answers are wrong when taken pure.

Everything to the agency: then every new field becomes a ticket, every ticket a three-day round trip, and the head of sales who just wants one status value renamed pays a prorated day rate for it. After a year, nobody in the house knows their own system, and the agency goes from service provider to hostage situation with invoicing. Everything in-house: then the one admin does it all, from password resets to the billing integration, and for the integration he lacks the experience, which only becomes apparent when it breaks in production. Seen both many times. Both expensive.

The sustainable answer is a division of labor along a clear line. In-house belongs everything that occurs daily and needs closeness to the business: user management, reports, field adjustments, training, an ear to the reps. External belongs everything that is rare, hard, and consequential: data model changes, integrations, migrations, larger automation logic, everything you need three times in five years and where building internal experience simply doesn't pay off.

So far, so sensible. The part that's missing in practice is a different one: the line has to be in the contract, not just in people's heads. Who is allowed to deploy to production? Who owns the data model, who approves changes to it? What happens when the internal admin touches an automation the agency built on a Friday, and the invoice handoff is due Monday? Without written answers to these questions, you get the usual theater when things break: the agency points at the admin, the admin points at the agency, and you pay for the troubleshooting while both get to be right.

Three sentences are often enough. Data model and integrations are changed only by the external partner, documented in the system. Everything on the configuration layer above belongs to the internal admin, no sign-off needed. Handovers happen in writing with a sandbox test, otherwise the change counts as not accepted.

Sounds like contract prose for something you could surely settle collegially? Collegial works right up until the first broken quarter close.

Don't ask yourselves agency or admin. Ask where the line runs at your company today, and who signed it. If the answer is "nowhere", you don't have a division of labor. You've had luck, so far.
