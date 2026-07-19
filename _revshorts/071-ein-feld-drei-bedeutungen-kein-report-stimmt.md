---
layout: revshort
title: "One field, three meanings, no report is right"
description: "Ask three departments what's in the 'Region' field and you get three answers. Marketing means the campaign's language region, DACH as one block...."
date: 2026-05-23
read_time: "2 min read"
category: "Data"
hero_icon: "database"
lang: en
translation: /de/revshorts/071-ein-feld-drei-bedeutungen-kein-report-stimmt/
---

Ask three departments what's in the "Region" field and you get three answers. Marketing means the campaign's language region, DACH as one block. Sales means the sales territory, the territory logic with North, South, and the odd special case of Austria, which historically sits with one particular AE. Finance means the country of the billing address, because VAT hangs on it.

One field. Three truths. And every report that groups by "Region" is wrong for two out of three departments, without anyone noticing.

The insidious part: everyone involved is acting correctly. The marketing colleague maintains the field by his definition, the sales colleague overwrites it by his, and finance pulls the data and wonders why Switzerland sometimes shows up and sometimes doesn't. There's no culprit. There's only a field that was never defined, and a data model that crams three concepts into one column because nobody asked questions when it was created five years ago.

The same game runs with "Lead Source," where campaign, channel, and first touch get mixed up. With "Customer since," where nobody knows whether the date means the first opportunity, the first contract, or the first invoice. With "MRR," which one dashboard calculates with discounts and another without. Every meeting where two teams show up with different numbers on the same topic is, in the end, a semantics meeting. You laboriously reach an agreement, and at the next quarterly review the debate starts over from the top, because the agreement isn't written down anywhere.

The solution is almost insultingly simple: a field glossary. Per critical field, one definition, one owner, the allowed values, the source of population, and who may change it. Twenty fields are enough to start, the other three hundred usually aren't worth it. The document costs two workshops and afterwards lives wherever your documentation lives. No tool to buy, no license, no migration.

And when the glossary uncovers a real collision, as with "Region," the answer isn't the better definition but separation: three fields for three concepts, cleanly named, automatically populated wherever possible. Deriving a country code from the billing address is something any CRM can do.

The ROI of this document is hard to put on a balance sheet and easy to feel. Every numbers debate that doesn't happen because you can simply look it up is time won. How many of your meetings last week were actually arguments about field definitions?
