# Dividend Stability Risk Analysis for Income Portfolios
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement
Income focused investors rely on dividends to meet ongoing cash flow needs. However, dividend cuts often arrive with little notice and can trigger both income shortfalls and sharp price declines. Many investors lack a systematic way to detect deteriorating payout sustainability before a cut occurs.

This project frames a stakeholder centered approach to estimate the probability of a 12 month dividend cut at the single stock level and surface early warning signs so portfolios can be adjusted proactively.

## Stakeholder & User
Primary stakeholder: Product leader or portfolio strategist at a retail brokerage who focused on income products.
End users: Investors who are seeking stable payouts.
Timing & Workflow Context: Advisors review client portfolios monthly and ahead of key events such as earnings or dividend announcements, focusing on dividend stability and identifying potential cut risks.

## Useful Answer & Decision
Answer type: Predictive.
Metric: Dividend‑Cut Probability, plus supporting indicators (payout ratio vs. sector, FCF coverage, earnings revisions, leverage trend).
Artifact to deliver: An Income Stability Risk Report (PDF/slide) ranking holdings by cut risk and suggesting replacements with similar yield but stronger fundamentals.

 ## Assumptions & Constraints
Data availability: Quarterly fundamentals, dividend history, and sector benchmarks accessible via market data APIs.
Capacity: Runs with basic Python tools (pandas, numpy) on a normal laptop or simple cloud setup.
Latency: Monthly refresh is sufficient; pre‑earnings optional weekly update.
Compliance: a clear disclaimer will be shown.

 ## Known Unknowns / Risks
Uncertain: Model drift when market conditions change suddenly
Uncertain: Data delays can make fundamentals look better than they are
Monitor: Data health-daily checks for missing/late fundamentals, stale dividend flags; alert on anomalies.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Identify high-risk dividend holdings → Problem Framing & Scoping (Stage 01) → Scoping paragraph, stakeholder memo, and initial repo setup

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

