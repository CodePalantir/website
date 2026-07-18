---
# TODO: replace with the real engagement + numbers.
# Everything below is a clearly-marked PLACEHOLDER: the client is anonymised
# and the metrics are illustrative, pending the real client's approval.
layout: case
title: "One lead-to-cash spine for a fintech running five disconnected tools"
client: "Confidential · Fintech"
category: "Integration"
order: 2
placeholder: true
services:
  - technical-health-audit
  - custom-integration
  - mulesoft-architecture
summary: "Marketing, sales, underwriting and billing each ran their own system — and each reported different numbers. We built one integration spine from first touch to invoice, so the pipeline the board sees is the pipeline that exists."
metrics:
  - label: "Systems reconciled by hand"
    before: "5"
    after: "0"
  - label: "Lead-to-CRM sync time"
    before: "24 hrs"
    after: "< 2 min"
  - label: "Records failing validation"
    before: "23%"
    after: "1.5%"
---

<!-- TODO: replace with the real engagement + numbers — placeholder narrative below. -->

## The situation

This fintech's revenue path crossed five systems: a marketing automation platform, the CRM, an in-house underwriting tool, a billing provider and a data warehouse. Each was fine on its own. Together, they disagreed — a "customer" meant something slightly different in each one, and a nightly CSV job was the closest thing to an integration layer.

The practical cost was a weekly ritual: two RevOps analysts spent most of Monday reconciling pipeline numbers by hand before the leadership meeting, and the board still asked why the figures moved between decks.

## The diagnosis

The audit traced one real lead through the whole stack, end to end. It took the lead over a day to reach the CRM, and by the time it hit billing, a fifth of the fields had been dropped, retyped or overwritten along the way. The root cause wasn't any single tool — it was that no system owned the customer record, so every hand-off was a translation, and every translation lost something.

The fix-list was an architecture, not a patch: define one canonical data spine, decide which system is the source of truth for each field, and replace the nightly CSVs with event-driven sync.

## What we shipped

- A canonical field map — one written definition of the customer and deal record, with a single source of truth declared per field.
- An event-driven integration layer replacing the nightly batch jobs, so records move between systems in minutes, not days.
- Validation at the boundary — records that fail the contract are quarantined with a reason, not silently loaded and discovered at quarter end.
- Alerting and replay — failed syncs surface in the team's channel and can be re-run without engineering time.
- Full documentation of the spine, so the client's engineers extend it instead of routing around it.

## The outcome

The Monday reconciliation ritual is gone — every dashboard reads from the same spine, so there is one pipeline number, not five. New leads reach sales while they're still warm, and data quality is enforced at the door instead of repaired at the end of the quarter. When the client added a new product line, their own team wired it into the spine using the documentation — which is exactly how we measure whether an integration engagement worked.
