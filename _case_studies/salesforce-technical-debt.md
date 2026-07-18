---
# TODO: replace with the real engagement + numbers.
# Everything below is a clearly-marked PLACEHOLDER: the client is anonymised
# and the metrics are illustrative, pending the real client's approval.
layout: case
title: "Four years of Salesforce technical debt, paid down in one quarter"
client: "Confidential · Series-B SaaS"
category: "Salesforce"
order: 1
featured: true
placeholder: true
services:
  - technical-health-audit
  - custom-development
  - managed-support
summary: "A Series-B SaaS company inherited an org built by three agencies in four years. Deploys took an afternoon, scheduled jobs failed silently, and nobody dared touch the Apex. We audited, stabilised, and put the platform back under engineering discipline."
metrics:
  - label: "Deploy time"
    before: "3.5 hrs"
    after: "22 min"
  - label: "Failed scheduled jobs / week"
    before: "14"
    after: "0"
  - label: "Apex without test coverage"
    before: "38%"
    after: "4%"
---

<!-- TODO: replace with the real engagement + numbers — placeholder narrative below. -->

## The situation

By the time this team reached Series B, their Salesforce org had passed through three different agencies. Each one had built on top of the last without removing anything: duplicate automation on the same objects, triggers with no shared framework, and a metadata surface nobody could fully describe. Deploys were scheduled for Friday afternoons because they routinely took the rest of the day — and sometimes the weekend.

The symptom that finally forced the issue wasn't dramatic. A scheduled job that synced billing status had been failing silently for weeks, and finance noticed the numbers drifting before anyone in RevOps did.

## The diagnosis

We started with the technical health audit: five days, the whole org, in writing. The picture it produced was uncomfortable but precise — a large share of the Apex codebase had no meaningful test coverage, more than a dozen scheduled jobs were in a failing or degraded state each week, and the deployment pipeline had no source control behind it at all. Changes went straight to production through change sets, which is why every deploy was an event.

The audit's fix-list was prioritised by risk, not by effort: stop the silent failures first, get the org into version control second, and only then start paying down the code itself.

## What we shipped

- A monitored job framework — every scheduled and queueable job now reports failures to a channel a human actually reads, instead of an unread system inbox.
- The full org under Git with a CI pipeline — validated deploys on every pull request, so "deploy day" stopped being a thing.
- A trigger framework consolidating overlapping automation per object, removing the recursion that had made behaviour unpredictable.
- Test coverage rebuilt around the code paths that carry revenue: quoting, billing sync and renewal automation first, cosmetic code last.
- A documented runbook, handed to the client's own engineers — the goal was never to make them dependent on us.

## The outcome

Deploys that took an afternoon now take the length of a coffee. Scheduled jobs either succeed or page someone — they no longer fail in silence. And because the org is in source control with tests around the revenue-critical paths, the client's team ships their own changes weekly, with us on managed support for the questions before they become big ones.
