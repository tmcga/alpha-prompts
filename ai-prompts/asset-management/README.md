# Asset Management — Prompt Library

Prompt templates for institutional asset management covering the full spectrum from active equity to multi-asset allocation. Each file targets a specific function with role-appropriate personas, real analytical frameworks, and structured prompt templates designed for benchmark-relative, fiduciary-duty-aware investing at scale.

## How Asset Management Differs from Hedge Funds

| Dimension | Asset Management | Hedge Funds |
|-----------|-----------------|-------------|
| **Objective** | Beat a benchmark (relative return) | Absolute return, uncorrelated alpha |
| **Constraints** | Tracking error budget, sector limits, ESG mandates | Fewer constraints, wider toolkit |
| **Fee structure** | 30-80 bps management fee, fee compression pressure | 1-2% mgmt + 15-20% performance fee |
| **Scale** | $100B+ AUM common; capacity is a feature | $1-50B typical; capacity is a constraint |
| **Fiduciary duty** | ERISA, prudent investor rule, client suitability | Sophisticated investor base, fewer fiduciary rules |
| **Liquidity** | Daily/weekly liquidity, cash drag management | Lock-ups, gates, side pockets permitted |
| **Risk lens** | Tracking error, active share, information ratio | Volatility, drawdown, tail risk, Sharpe ratio |
| **Transparency** | Full holdings disclosure (mutual funds), regulatory reporting | Limited transparency, investor letters |

## Division Map

| File | Function | Focus Area |
|------|----------|------------|
| [active-equity.md](active-equity.md) | Active Equity | Fundamental stock selection, alpha generation, Brinson attribution, ESG integration |
| [systematic-factor.md](systematic-factor.md) | Systematic & Factor Investing | Factor portfolios, smart beta design, factor timing, crowding analysis |
| [fixed-income-am.md](fixed-income-am.md) | Fixed Income | Duration management, credit allocation, MBS, LDI, yield curve strategies |
| [multi-asset.md](multi-asset.md) | Multi-Asset Allocation | SAA, TAA, target-date funds, capital market assumptions, model portfolios |
| [alternatives-allocation.md](alternatives-allocation.md) | Alternatives Allocation | PE pacing, hedge fund DD, real assets, secondaries, portfolio impact analysis |
| [risk-analytics.md](risk-analytics.md) | Risk & Performance Analytics | Factor risk decomposition, VaR/CVaR, scenario analysis, liquidity risk |

## How to Use

1. **Set the persona.** Each file begins with a role context block. Paste it at the start of your conversation to calibrate the AI's analytical lens and vocabulary.
2. **Fill the brackets.** Prompts use `[bracket placeholders]` for portfolio-specific data. Replace them with your actual figures.
3. **Combine across files.** A CIO building a total portfolio will pull from multi-asset (SAA), active-equity (mandate design), fixed-income (duration), and risk-analytics (total portfolio risk). Use prompts from multiple files as needed.
4. **Reference the foundations.** Quantitative frameworks build on [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) — factor models, mean-variance optimization, risk parity, and statistical testing fundamentals live there. The asset management files extend these with benchmark-relative thinking, fiduciary context, and institutional scale.

## Related

- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — foundational quant frameworks, alpha research, factor decomposition
- [Trading Prompts](../trading/) — execution, microstructure, and flow analysis
- [Banking Prompts](../banking/) — capital markets, underwriting, and deal structuring
