# Venture Capital -- AI Prompt Library

## Overview

Venture capital is the business of financing innovation under extreme uncertainty. Unlike public markets or even private equity, VC is governed by **power law dynamics**: a small number of outsized winners drive the vast majority of fund returns. This fundamentally shapes every aspect of the craft -- from deal selection to portfolio construction to exit timing.

The prompts in this section cover the full lifecycle of venture investing: sourcing and evaluating early-stage companies, scaling growth-stage portfolios, navigating specialized verticals (crypto/web3, biotech/healthcare), and operating portfolio companies through platform teams.

## Fund Economics

The standard VC fund operates on a **2/20 model**:

- **2% management fee** on committed capital (typically stepping down after the investment period)
- **20% carried interest** on profits above a preferred return (hurdle rate), subject to a GP clawback provision

Key fund-level math:

```
Fund Return Multiple = Total Distributions / Total Contributions
Net IRR = Time-weighted return after fees and carry
DPI (Distributions to Paid-In) = Cumulative distributions / Cumulative contributions
RVPI (Residual Value to Paid-In) = Remaining NAV / Cumulative contributions
TVPI = DPI + RVPI
```

## Power Law Portfolio Construction

In a typical VC fund:
- ~50% of investments return < 1x
- ~20% return 1-3x
- ~20% return 3-10x
- ~10% return > 10x (these drive the fund)

A single 50x+ return on a meaningful position can return the entire fund. This means the **cost of missing a winner far exceeds the cost of backing a loser**, and portfolio construction must be optimized accordingly.

```
Expected Fund Return = SUM( P(outcome_i) * Multiple_i * Weight_i )  for all investments i

Target ownership at exit: 10-20% (early stage) or 5-10% (growth stage)
Reserve ratio: typically 50-60% of fund for follow-on investments
```

## File Index

| File | Division | Focus |
|------|----------|-------|
| [early-stage.md](early-stage.md) | Seed / Series A | Market sizing, founder eval, term sheets, PMF, competition |
| [growth-stage.md](growth-stage.md) | Growth / Late-Stage | SaaS metrics, IPO readiness, secondaries, restructuring |
| [crypto-web3.md](crypto-web3.md) | Crypto / Web3 / DeFi | Token economics, protocols, DAOs, L1/L2 evaluation |
| [biotech-healthcare.md](biotech-healthcare.md) | Biotech / Healthcare | Clinical trials, pipeline rNPV, regulatory, licensing |
| [platform-operations.md](platform-operations.md) | Portfolio Operations | GTM, talent, board governance, financial ops, partnerships |

## Cross-References

- [Private Capital](../private-capital/) -- Buyouts, credit, and real assets
- [Banking](../banking/) -- IPO advisory and capital markets
- [Hedge Funds](../hedge-funds/) -- Public market perspectives on VC-backed companies
- [Trading](../trading/) -- Liquidity and secondary market dynamics
