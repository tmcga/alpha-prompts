# Hedge Fund Strategy Prompt Library

Prompt templates organized by hedge fund strategy type. Each file contains role-specific personas, categorized prompts with bracket placeholders, and the mathematical frameworks that underpin real portfolio decisions.

For foundational quant frameworks (IC/IR, Black-Litterman, Deflated Sharpe Ratio, Almgren-Chriss), see [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md). The files below extend those foundations with strategy-specific content.

---

## Strategy Files

| File | Strategy | Core Edge | Typical Holding Period |
|------|----------|-----------|----------------------|
| [fundamental-long-short.md](fundamental-long-short.md) | Fundamental L/S Equity | Variant perception, catalyst timing | Weeks to months |
| [global-macro.md](global-macro.md) | Global Macro | Macro regime identification, cross-asset expression | Weeks to quarters |
| [quantitative-systematic.md](quantitative-systematic.md) | Quantitative / Systematic | Statistical alpha signals, factor harvesting | Intraday to weeks |
| [event-driven.md](event-driven.md) | Event-Driven | Deal spreads, corporate actions, activism | Days to months |
| [credit-distressed.md](credit-distressed.md) | Credit & Distressed | Credit mispricing, recovery analysis, capital structure | Months to years |

---

## Key Differences Between Strategy Types

**Information source**: Fundamental L/S and event-driven rely on deep single-name research. Global macro relies on top-down economic analysis. Quant/systematic relies on statistical patterns across broad universes. Credit/distressed relies on legal and structural analysis of capital structures.

**Capacity profile**: Quant strategies face capacity decay as AUM grows (market impact erodes alpha). Macro strategies scale well because they trade liquid instruments. Distressed strategies are capacity-constrained by illiquidity and deal flow.

**Risk character**: L/S equity and quant strategies target low net exposure and idiosyncratic alpha. Macro strategies accept directional risk when conviction is high. Event-driven carries deal-break tail risk. Distressed carries illiquidity and binary restructuring risk.

**Correlation to markets**: L/S equity typically runs 20-50% net long. Macro can be long, short, or flat. Quant market-neutral targets near-zero beta. Event-driven has episodic correlation spikes. Distressed is correlated to credit cycles.

---

## Pod vs. Standalone Structure

**Pod model** (Citadel, Millennium, Balyasny): Each PM runs a sleeve with strict risk limits (drawdown stops, factor exposure caps, gross/net bands). Central risk team enforces constraints. PMs share infrastructure but not ideas. Capital is reallocated dynamically based on performance.

**Standalone model** (Tiger Cubs, Lone Pine, Pershing Square): Single CIO or small team runs concentrated book. Wider drawdown tolerance. Deeper conviction per position. Less diversification, more idiosyncratic risk.

**Multi-strategy model** (Bridgewater, AQR, D.E. Shaw): Blends multiple strategy types within one fund. Diversification benefit across uncorrelated return streams. Central allocation uses risk parity or Kelly-based sizing across sleeves.

---

## How to Use These Prompts

1. Start with the **role context block** at the top of each file to set the AI persona
2. Select the **prompt template** that matches your task
3. Fill in the **[bracket placeholders]** with your specific data
4. Combine prompts across files when your analysis spans strategy types (e.g., a macro-driven credit trade uses prompts from both `global-macro.md` and `credit-distressed.md`)

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- Foundational quant frameworks
- [`../trading/`](../trading/) -- Execution and market microstructure
- [`../banking/`](../banking/) -- Investment banking and deal analysis
