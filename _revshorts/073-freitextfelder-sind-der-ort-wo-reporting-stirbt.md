---
layout: revshort
title: "Free-text fields are where reporting goes to die"
description: "Open the 'Region' field in your CRM and look at what's in there. München. Muenchen. MUC. Munich, because a colleague was on the English keyboard..."
date: 2026-05-25
read_time: "2 min read"
category: "Data"
hero_icon: "database"
lang: en
translation: /de/revshorts/073-freitextfelder-sind-der-ort-wo-reporting-stirbt/
---

Open the "Region" field in your CRM and look at what's in there. München. Muenchen. MUC. Munich, because a colleague was on the English keyboard layout. Bavaria, because someone was thinking generously. South, from the era before the 2024 territory redesign. Six spellings, one city, zero analyzability.

And then someone wonders why the revenue-by-region report doesn't add up.

The pattern is always the same. A field gets created, fast, between two meetings, as free text, because free text needs no discussion. A picklist would mean someone has to decide which values are allowed. So it stays open. Three years later, the field holds 214 distinct values for 16 actual regions, and every analysis starts with an hour of Excel cleanup, done by a different person every time, slightly differently every time.

Free text feels like freedom. True, for the person typing. For the person analyzing, it's archaeology.

The solution sounds banal and isn't: picklists with ownership. Not just dropdowns, but dropdowns a human is responsible for. Who may add values? What happens to old values when territories change? How does existing data get migrated? Those aren't technical questions, they're governance questions, and that's exactly why everyone dodges them.

Of course there are fields that have to be free text. Notes. Context. What the customer literally said. Everything you'll never build a report on. The rule of thumb is simple: if a field is ever supposed to end up in a filter, a grouping, or a chart, free text is the wrong answer. And "ever" arrives faster than you think.

The real point sits one level deeper. Every analysis you want to run in two years is decided today, at field creation. The dashboard is just the end of the chain. If you're sloppy at creation, you can polish downstream all you want, the data won't support it. Reporting problems are almost never reporting problems. They're field-creation problems with a two-year delay.

So: new field, three questions. Will this ever be analyzed? Who owns the value list? What happens to the legacy data? Takes two minutes. The alternative costs, conservatively, an hour per month for everyone who has to work with the field.

How many of your free-text fields would be picklists today if someone had thought for two minutes at creation?
