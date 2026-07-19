---
layout: revshort
title: "Payment status belongs in the CRM"
description: "Scene from an ordinary Tuesday: the account executive calls the customer, in a good mood, the renewal is coming up. What he does not know: accounting..."
date: 2026-05-10
read_time: "2 min read"
category: "Integration"
hero_icon: "git-branch"
lang: en
translation: /de/revshorts/058-der-zahlungsstatus-gehoert-ins-crm/
---

Scene from an ordinary Tuesday: the account executive calls the customer, in a good mood, the renewal is coming up. What he does not know: accounting sent that same company its second dunning notice yesterday. Two departments, one customer, zero shared information.

This is not a communication problem you solve with a weekly sync. It is a data problem. The payment status lives in the billing system or the ERP, the CRM knows nothing about it, and the person calling the customer happens to work in the CRM. Two systems that do not talk to each other, and so the people behind them do not either.

Yet the integration that fixes exactly this is maybe the most rewarding one in all of RevOps. Invoice created, invoice paid, invoice overdue: three status values, one field on the account, one sync per night is plenty in most cases. No real-time streaming, no middleware cathedral. Stripe, Chargebee, billwerk, even a boarded-up old ERP will surrender this information somehow, worst case as an export a script picks up.

So why does hardly anyone have it? Because it falls between two responsibilities. Accounting thinks in its own system and considers the CRM a sales toy. Sales wants nothing to do with invoices as long as the commission is right. And for IT the thing is too small to open a project for. So it stays unbuilt. For years.

The counter-math is quick. An AE who sees before the call that the customer is overdue has a different conversation. A CSM who knows about the open balance escalates internally before the third notice goes out and ruins the relationship. And whoever sees in the dashboard which accounts have open pipeline and open balances at the same time prioritizes differently. These are not nice-to-haves. This is the difference between a company that talks to its customer and three departments that do so independently of each other.

By the way: this is exactly where a line runs that we draw deliberately. Journal entries, chart of accounts, tax logic, everything from the ERP onward belongs to the tax people and stays there. But order won, billing triggered, payment status back into the CRM: that is revenue process, not accounting.

If you build only one integration this year, build this one. It is small, it is cheap, and it prevents your sales team's most expensive phone calls. What other integration can claim that?
