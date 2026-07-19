---
layout: revshort
title: "Docs nobody reads are not docs"
description: "In your Confluence sits a page called 'Lead Process v3 final'. Last edited 14 months ago, by a colleague who's no longer there. It describes three fields..."
date: 2026-06-21
read_time: "2 min read"
category: "AI"
hero_icon: "sparkles"
lang: en
translation: /de/revshorts/100-doku-die-niemand-liest-ist-keine-doku/
---

In your Confluence sits a page called "Lead Process v3 final". Last edited 14 months ago, by a colleague who's no longer there. It describes three fields that no longer exist and a status value that's since been renamed. Views last quarter: four. Two of those were you, looking for something else.

That's not a maintenance problem, that's a design flaw. Process documentation in a wiki doesn't go stale eventually, it goes stale while being written, because the system keeps turning while the document stands still. And even if it were current: the rep who right now doesn't know what belongs in "Qualification Reason" doesn't switch to the wiki, doesn't search, doesn't read. He guesses. Or leaves the field empty, and your report later counts guesses.

Documentation belongs where the work happens. In the system itself.

That starts with field descriptions worthy of the name. "Expected Revenue" needs the help text: net, in euros, annual value, excluding options. One sentence, right on the field, visible at the moment of entry. Costs two minutes per field and saves a thousand wrong values. Then, names that speak. An automation called "Flow 27 Copy Copy" documents nothing, "Lead Routing DACH New Business" explains itself on reading. Same goes for fields, reports, stages. Whoever has to think while naming is already documenting.

And error messages. A validation rule that spits out "ERROR: condition not met" produces a support ticket. One that says "From stage Proposal onward we need the decision date, enter it in the Close Plan field" trains the whole sales team on the side. Every error message is a documentation page that's guaranteed to be read, namely at the exact moment of the error.

A remainder stays with the wiki, granted. Architecture decisions, the why behind the data model, integration overviews: that lives poorly anywhere else and doesn't need to be accurate daily. But everything a user needs to know while working has no business being in the wiki.

The test is simple. Take your newest sales hire and watch them work in the CRM for an hour, without helping. Every place they stall and have to ask someone, documentation is missing in the system. The Confluence page helped them exactly zero times in that hour. So why are you maintaining it?
