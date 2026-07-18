---
# TODO: replace with the real engagement + numbers.
# ── Copy-me template for a new case study ────────────────────────────
# 1. Copy this file to _case_studies/<url-slug>.md  (slug becomes /cases/<slug>/)
# 2. Fill in every field below, delete `published: false`, set `order`.
# 3. Keep `placeholder: true` until the client has approved the numbers , 
#    it renders the "illustrative figures" disclaimer under the metrics.
published: false
layout: case
title: "One-line outcome, written like a headline"
client: "Confidential · <sector>"          # or the real client name once approved
category: "Salesforce"                     # Salesforce | Integration | HubSpot | Managed …
order: 99                                  # sort position on /work/ (low = first)
featured: false
placeholder: true                          # true = metrics carry the illustrative-figures note
services:                                  # slugs from _services/ → linked "Services used" strip
  - technical-health-audit
  - custom-integration
summary: "Two or three sentences: who the client is, what hurt, what changed. Shown in the hero and on the /work/ cards."
metrics:                                   # first metric = the headline metric on /work/ cards
  - label: "Metric name"
    before: "old value"
    after: "new value"
  - label: "Second metric"
    before: "old"
    after: "new"
  - label: "Third metric"
    before: "old"
    after: "new"
---

<!-- TODO: replace with the real engagement + numbers. -->

## The situation

What the client's world looked like before APX. Concrete, calm, no hype.

## The diagnosis

What the audit found, and how the fix-list was prioritised.

## What we shipped

- Deliverable one, working, documented, owned by the client's team.
- Deliverable two.
- Deliverable three.

## The outcome

What changed, tied back to the metrics above. End on independence: the client's team runs it.
