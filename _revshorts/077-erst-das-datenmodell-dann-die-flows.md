---
layout: revshort
title: "Data model first, then the flows"
description: "The wish always sounds the same. Automate more, less manual work, ideally this month. Understandable, and a flow is quickly..."
date: 2026-05-29
read_time: "2 min read"
category: "Data"
hero_icon: "database"
lang: en
translation: /de/revshorts/077-erst-das-datenmodell-dann-die-flows/
---

The wish always sounds the same. Automate more, less manual work, ideally this month. Understandable, and a flow is quickly built. But you're automating on top of the data model you have. If that model is crooked, automation doesn't make the flaw fixable, it makes it permanent.

A scene from an audit last year. A software company keeps contracts as free-text fields on the account: term, volume, notice period, all in text columns, because four years ago nobody wanted to create a dedicated contract object. Worked fine at first. By now, 19 automations hang on those fields: renewal reminders, a commission logic, two board reports, an interface to billing. Now they want a clean contract object, multiple contracts per customer, history, the usual. The rebuild doesn't cost the two hours it would have back then. It costs six weeks, because every one of the 19 automations has to be touched, rebuilt, and tested. That is the compound interest on a crooked foundation.

Every flow is a bet that the structure underneath is right. Objects, fields, relationships: that's the load-bearing structure. Automation is the concrete you pour around it. Concrete around a straight foundation carries. Concrete around a crooked foundation makes sure you can never pull it straight again, at least not without a jackhammer.

The right order is unspectacular. First the objects: what are your things? Customers, locations, contracts, subscriptions, devices, whatever structures your business. Then the fields: what do you need to know about these things, and in what format? Then the relationships: does the contract hang off the account or the opportunity, can a contact belong to several companies? Only once that stands do the flows come. Sounds like a textbook, and still gets done the other way around in nine out of ten orgs, because a flow shines in a demo and a data model doesn't look good in any screenshot.

The test is simple. Draw your data model on a whiteboard, boxes and lines. If an argument breaks out over what an account is or where contracts live: not a single new flow until that's settled. Every automation that goes live before then pours the argument into concrete.

Is that slower? At the start, yes. Two weeks of modeling work feel sluggish next to a flow that ships Friday. But you build only once. The alternative builds three times and tears down twice.

What in your system would you model differently today, and how many automations are keeping you from doing exactly that?
