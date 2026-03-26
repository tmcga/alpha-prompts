# Private Capital Prompt Library

Prompt templates for private capital investing across strategies. Each file covers a distinct asset class with role-specific persona blocks, analytical frameworks, and reusable prompt templates.

## File Index

| File | Strategy | Key Concepts |
|------|----------|--------------|
| [buyouts.md](buyouts.md) | Large/mid-cap leveraged buyouts | Operational improvement, buy-and-build, management equity, exit prep |
| [growth-equity.md](growth-equity.md) | Growth-stage investing | Unit economics, revenue quality, minority protections, path to profitability |
| [real-estate.md](real-estate.md) | Real estate private equity | Cap rates, development, REIT analysis, debt structuring |
| [private-credit.md](private-credit.md) | Direct lending and private credit | Credit underwriting, loan structuring, covenants, yield analysis |
| [infrastructure.md](infrastructure.md) | Infrastructure investing | Concessions, regulated utilities, greenfield/brownfield, energy transition |
| [special-situations.md](special-situations.md) | Special situations and tactical | Rescue financing, distressed-for-control, structured equity, cross-asset |

## Key Differences Across Private Capital Strategies

**PE Buyouts vs. Growth Equity**: Buyouts use leverage and control to drive returns through operational improvement and multiple arbitrage. Growth equity takes minority or light-majority positions in high-growth companies, relying on revenue compounding rather than financial engineering. Buyouts target 2.0-3.0x MOIC over 4-6 years; growth equity targets 3.0-5.0x+ over 3-5 years with higher variance.

**Private Credit vs. Public Fixed Income**: Private credit earns an illiquidity premium (150-400bps) over broadly syndicated loans. Lenders negotiate bespoke covenants, have direct access to borrower financials, and can amend terms bilaterally. The tradeoff is mark-to-market opacity, limited liquidity, and concentration risk.

**Real Estate vs. Infrastructure**: Both are real-asset strategies with inflation linkage, but real estate returns depend on property-level supply/demand and lease economics, while infrastructure returns are driven by concession terms, regulatory frameworks, and long-duration contracted cash flows. Infrastructure assets typically have longer hold periods (10-30 years) and lower return targets (8-12% net IRR) than opportunistic real estate (15-20%+).

## Core Private Capital Concepts

**J-Curve**: Private capital funds draw capital over 3-5 years while paying management fees from day one, producing negative returns early in fund life. Returns inflect as portfolio companies mature and exits begin. The J-curve effect is most pronounced in buyouts and real estate development, and least in private credit (which generates current income).

**Vintage Year**: The year a fund begins investing. Vintage diversification matters because entry valuations, credit conditions, and exit environments vary by cycle. A fund entering at cycle-peak multiples faces structural headwinds regardless of operational execution.

**Illiquidity Premium**: The excess return investors demand for locking up capital in illiquid structures. Academic estimates range from 100-300bps annualized. This premium is the foundational justification for private capital allocations, but it only materializes if the GP generates alpha above public-market equivalents (PME benchmarking).

**Public Market Equivalent (PME)**: Kaplan-Schoar PME compares private fund cash flows to a public index. PME > 1.0 means the fund outperformed the index. Direct Alpha methodology converts PME into an annualized spread.

## Foundational Reference

For core PE frameworks (LBO math, returns bridge, due diligence checklists, 100-day plans), see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The files in this directory extend those foundations with strategy-specific depth.
