---
layout: revshort
title: "Your conversion rate measures the wrong month"
description: "The math looks reasonable. Deals closed in April divided by leads in April, done, there's your conversion rate. That's exactly how it appears in most..."
date: 2026-06-15
read_time: "2 min read"
category: "AI"
hero_icon: "sparkles"
lang: en
translation: /de/revshorts/094-eure-conversion-rate-misst-den-falschen-monat/
---

The math looks reasonable. Deals closed in April divided by leads in April, done, there's your conversion rate. That's exactly how it appears in most dashboards we open in audits. And that's exactly how it's structurally wrong.

The January lead converts in April. Not in January. If your sales cycle runs 90 days, the monthly calculation compares today's leads with yesterday's closings, more precisely: with closings from lead generation that happened a quarter ago. Numerator and denominator come from different worlds. What comes out isn't a measurement, it's the random product of two overlapping time series.

For a long time nobody notices, because with constant lead volume it roughly works out. It gets interesting the moment something moves. You run a campaign in March, lead volume doubles, and promptly the reported conversion rate halves, because the new leads sit in the denominator while their closings won't arrive until June. Marketing gets punished for its success. The reverse holds too: lead volume collapses, the rate appears to rise, and in the management meeting someone celebrates an improvement that is in truth an early warning signal.

The fix is called cohort logic. You take all leads from one month and follow exactly that group through the funnel. How many from the January cohort became an opportunity, how many of those became a customer, regardless of when the close falls. Only then do you compare cohorts against each other, January against February against March, each group against its own fate. Conceptually simple. In practice it usually fails on one detail: cohorts need the immutable entry timestamp into each funnel stage, and many CRMs overwrite exactly that field on every change. If you don't capture the history cleanly, you can't build a cohort retroactively. That's data model work, not dashboard cosmetics.

Named honestly, the approach has a catch: cohorts require patience. The January cohort isn't fully told until May, if the cycle runs 90 days plus variance. If you want a fresh number for the dashboard every week, cohorts will give you gaps at first. But a number that's right three months later beats a number that's there immediately and was never right.

Small test for the next reporting meeting: ask which cohort the closings in the numerator come from. If the answer is "the same month as the leads in the denominator", your most important funnel metric is rolling dice. And has been for years.
