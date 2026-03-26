# Sales & Trading -- AI Prompt Library

## Overview

This section contains prompt templates for sell-side and buy-side trading desks across all major asset classes. Each file provides role-specific persona blocks, analytical frameworks, mathematical models, and ready-to-use prompt templates with bracket placeholders you can fill in for your specific use case.

## How to Use

1. **Pick your desk.** Navigate to the file matching your asset class or function.
2. **Copy the persona block** at the top of the file into your system prompt to ground the AI in the correct role context.
3. **Select a prompt template** from the categorized sections. Replace `[bracket placeholders]` with your specific parameters.
4. **Chain prompts** across files when your analysis spans asset classes (e.g., equity derivatives work uses both `equities.md` and `derivatives.md`).

## Division Files

| File | Desk / Function | Key Topics |
|------|----------------|------------|
| [equities.md](equities.md) | Cash Equities Trading | Block trades, program trading, sector rotation, short selling, algorithmic execution |
| [fixed-income.md](fixed-income.md) | Fixed Income (Rates & Credit) | Bond relative value, yield curve, credit trading, repo, duration management |
| [derivatives.md](derivatives.md) | Options & Derivatives | Pricing/Greeks, volatility analysis, strategy construction, exotics, hedging |
| [structured-products.md](structured-products.md) | Structured Products | MBS, CLOs, ABS, tranche analysis, securitization structuring |
| [fx-and-rates.md](fx-and-rates.md) | FX & Interest Rates | Spot/forward FX, IRS pricing, FX options, cross-currency basis, central banks |
| [commodities.md](commodities.md) | Commodities | Futures curves, energy, metals, agriculture, physical vs derivatives |
| [market-making.md](market-making.md) | Market Making & Electronic Trading | Spreads, inventory, order flow, microstructure, quoting algorithms |

## Cross-References

- For risk management frameworks that apply across desks, see `../risk-management/` (if available).
- For macro and research overlays, see `../research/` (if available).
- For compliance and regulatory considerations, consult your firm's internal policies.

## Conventions

- All prompt templates use `[BRACKET_PLACEHOLDERS]` for user-supplied values.
- Mathematical formulas are written inline using standard notation.
- "See also" links at the bottom of each file point to related division files.
