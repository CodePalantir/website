---
# TODO: replace with the real engagement + numbers.
# Everything below is a clearly-marked PLACEHOLDER: the client is anonymised
# and the metrics are illustrative, pending the real client's approval.
layout: case
title: "Re-architecting a CRM the sales team had quietly stopped using"
client: "Confidential · Industrial group"
category: "Salesforce"
order: 3
placeholder: true
services:
  - technical-health-audit
  - sales-cloud-setup
  - service-cloud-console
summary: "An industrial group's Salesforce had grown into 40+ required fields and a process nobody followed, so the real pipeline lived in spreadsheets. We rebuilt the org around how the business actually sells, and the team came back."
metrics:
  - label: "Weekly active CRM users"
    before: "31%"
    after: "87%"
  - label: "Quote turnaround"
    before: "9 days"
    after: "2 days"
  - label: "Deals tracked outside the CRM"
    before: "~40%"
    after: "0"
---

<!-- TODO: replace with the real engagement + numbers, placeholder narrative below. -->

## The situation

On paper, this industrial group had a mature Salesforce implementation. In practice, the sales team had quietly stopped using it. Opportunity screens carried more than forty required fields, many added for a report someone ran once, and the sales process modelled in the org described how a consultant imagined machinery sales working, not how a nine-month, multi-stakeholder industrial deal actually moves.

So the real pipeline lived in spreadsheets and inboxes. Forecast meetings started with "let me check my file", and service had no view of what sales had promised.

## The diagnosis

The audit spent as much time with the sales team as with the metadata. The finding was blunt: the org wasn't broken, it was wrong. Adoption wasn't a training problem, the system genuinely made every deal slower to record than to close. Usage data confirmed it: under a third of the team touched the CRM in a given week, and the fields leadership relied on for forecasting were empty or stale in most open deals.

The recommendation was a re-architecture, not a re-training: model the actual sales motion, cut every field that no decision depends on, and give service the same customer record sales uses.

## What we shipped

- A rebuilt opportunity model matching the real sales motion, long-cycle, multi-site, distributor-involved, with stages the team recognised from their own deals.
- Required fields cut to the handful that drive forecasting and hand-offs; everything else became optional or was removed with its dead reports.
- Guided quoting that pulls specs and pricing instead of asking reps to retype them, the single biggest drag on quote turnaround.
- A Service Cloud console on the same customer record, so service sees commitments the moment a deal closes.
- Migration of the spreadsheet pipeline into the new model, done with the team deal by deal, which doubled as the only training anyone needed.

## The outcome

Adoption recovered without a mandate, because the CRM became the easiest place to run a deal rather than an extra chore after it. Quotes that took most of two weeks now go out in days, forecast meetings read from live pipeline instead of personal files, and service stopped being surprised by what sales had sold. The org is smaller than the one it replaced, which is usually what "fixed" looks like.
