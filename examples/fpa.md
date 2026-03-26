# FP&A: SaaS Unit Economics & Cohort Analysis

## Analysis Type
Unit economics + SaaS metrics

## Company Profile
- **Name:** WorkGrid (fictional)
- **Industry:** B2B SaaS — project management for construction
- **Stage:** Series B, 3 years post-product launch
- **ARR:** $22M
- **Customers:** 680
- **ACV:** $32K average (range: $8K SMB to $120K enterprise)
- **Employees:** 110

## Business Model
- **Segments:** SMB (<$15K ACV, 420 customers), Mid-Market ($15-50K, 210 customers), Enterprise (>$50K, 50 customers)
- **Pricing:** Per-seat + platform fee, annual contracts
- **Average Seats per Customer:** SMB 8, Mid-Market 25, Enterprise 80

## Key Metrics
| Metric | SMB | Mid-Market | Enterprise | Blended |
|--------|-----|-----------|-----------|---------|
| ACV | $8K | $28K | $95K | $32K |
| Gross Margin | 82% | 80% | 75% | 80% |
| CAC | $6K | $22K | $65K | $18K |
| CAC Payback (months) | 9 | 10 | 10 | 10 |
| LTV/CAC | 3.8x | 4.2x | 5.1x | 4.2x |
| Logo Churn (annual) | 18% | 8% | 3% | 12% |
| Net Revenue Retention | 95% | 112% | 135% | 108% |
| Sales Cycle (days) | 21 | 45 | 90 | 38 |
| Payback (months) | 9 | 10 | 10 | 10 |

## Cohort Data (Annual Cohorts, Revenue Retained)
| Cohort | Year 0 | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|--------|
| 2023 | $4.2M | $3.8M | $3.5M | — |
| 2024 | $6.8M | $6.5M | — | — |
| 2025 | $11.0M | — | — | — |

## Decision Context
CFO preparing for Series C fundraise. Need to answer: "Which segment should we invest in? SMB has volume but high churn. Enterprise has great economics but slow sales cycles and lower gross margin. Mid-market is the sweet spot — but is it big enough?"

## Time Horizon
Forward projection: 3 years

## Try It
```
/fpa

Unit economics for WorkGrid — $22M ARR construction SaaS with 3 segments.
SMB: $8K ACV, 18% churn, 3.8x LTV/CAC. Mid-Market: $28K ACV, 8% churn,
4.2x LTV/CAC. Enterprise: $95K ACV, 3% churn, 5.1x LTV/CAC, but 75% gross
margin and 90-day sales cycles. Blended NRR 108%. Cohort data shows SMB
revenue decaying while Enterprise and Mid-Market expand. Preparing for
Series C — which segment should we double down on? Model the 3-year ARR
impact of shifting GTM investment between segments.
```
