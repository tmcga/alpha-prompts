# Banking & Capital Markets — Prompt Library

Prompt templates for investment banking divisions covering the full deal lifecycle: origination, execution, and distribution. Each file targets a specific desk with role-appropriate personas, real analytical frameworks, and structured prompt templates.

## Division Map

| File | Desk | Focus Area |
|------|------|------------|
| [mergers-and-acquisitions.md](mergers-and-acquisitions.md) | M&A Advisory | Sell-side processes, buy-side diligence, merger models, fairness opinions, cross-border deals |
| [leveraged-finance.md](leveraged-finance.md) | Leveraged Finance | Credit agreements, leveraged loans, high yield bonds, debt capacity, covenant modeling |
| [equity-capital-markets.md](equity-capital-markets.md) | ECM | IPO pricing, bookbuilding, follow-ons, convertible bonds, comparable IPO analysis |
| [debt-capital-markets.md](debt-capital-markets.md) | DCM | IG new issuance, credit ratings, liability management, ESG bonds, sovereign issuance |
| [restructuring.md](restructuring.md) | Restructuring | 13-week cash flow, plan of reorg, distressed valuation, creditor negotiations, out-of-court workouts |
| [equity-research.md](equity-research.md) | Equity Research | Coverage initiation, earnings analysis, SOTP valuation, thematic research, quant screens |

## How to Use

1. **Set the persona.** Each file begins with a role context block. Paste it at the start of your conversation to calibrate the AI's analytical lens and vocabulary.
2. **Fill the brackets.** Prompts use `[bracket placeholders]` for company-specific data. Replace them with your actual figures.
3. **Combine across files.** A sell-side M&A process touches M&A (CIM, valuation), LevFin (stapled financing), and DCM (refinancing). Pull prompts from multiple files as needed.
4. **Reference the foundations.** Mathematical frameworks build on [`../roles/investment-banker.md`](../roles/investment-banker.md) — DCF, comps, accretion/dilution, LBO, and capital structure fundamentals live there.

## Related

- [Investment Banker Role](../roles/investment-banker.md) — foundational valuation and deal math
- [PE Analyst Role](../roles/pe-analyst.md) — buy-side perspective, LBO modeling, portfolio operations
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — public markets, factor models, portfolio construction
