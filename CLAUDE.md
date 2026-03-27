# Alpha Stack

This is **Alpha Stack** — an installable AI skill system for finance. 26 skills, 19 computational tools, and a structured workflow for investment analysis.

## Skill Registry

**Deal & Banking**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/sell-side` | sell-side | Sell-side M&A process (teaser → CIM → buyer mapping → bids) |
| `/buy-side` | buy-side | Buy-side acquisition (screening → valuation → synergies → offer) |
| `/lbo` | lbo | LBO modeling (debt sizing → returns → attribution → stress) |
| `/restructuring` | restructuring | Distressed & restructuring (waterfall → fulcrum → plan of reorg) |
| `/ipo` | ipo | IPO analysis (readiness → valuation → pricing → allocation) |
| `/pitch-deck` | pitch-deck | Pitch deck builder (startup, deal marketing, fund, internal) |
| `/investment-memo` | investment-memo | IC memo (equity, PE/VC, credit, real estate modes) |

**Trading & Derivatives**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/trade` | trading-and-execution | Execution analysis (block trades, VWAP/TWAP, market impact) |
| `/derivatives` | options-and-derivatives | Options pricing, Greeks, vol analysis, structured products |
| `/market-making` | market-making | Avellaneda-Stoikov quoting, inventory management, P&L attribution |

**Hedge Funds**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/long-short` | long-short | L/S equity (variant perception → catalyst → Kelly sizing) |
| `/macro` | macro | Global macro thesis (regime → cross-asset → expression → sizing) |
| `/merger-arb` | merger-arb | Event-driven / merger arb (spread → probability → collar/CVR) |
| `/credit` | credit | Credit & distressed (Z-Score → Merton → recovery → relative value) |

**Portfolio & Risk**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/portfolio` | portfolio-construction | Portfolio optimization (Black-Litterman, risk parity, factor) |
| `/risk` | risk-analytics | Risk analytics (VaR/CVaR, Monte Carlo, stress testing, tail risk) |
| `/attribution` | attribution | Performance attribution (Brinson, factor, currency, fixed income) |

**Real Estate**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/real-estate` | real-estate | General RE analysis (routes to specialized RE skills below) |
| `/re-acquisitions` | re-acquisitions | Property acquisition underwriting (core, value-add, opportunistic) |
| `/re-development` | re-development | Ground-up development (cost build, lease-up, yield on cost) |
| `/re-debt` | re-debt | Capital stack structuring (DSCR, LTV, mezz, preferred, bridge) |
| `/re-reit` | re-reit | Public REIT analysis (NAV, FFO/AFFO, implied cap rates, comps) |

**Private Capital**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/pe` | private-capital | General PE analysis (routes to specialized PE skills below) |
| `/pe-buyout` | pe-buyout | Control buyouts (LBO, platform + bolt-on, returns attribution, value creation) |
| `/pe-growth` | pe-growth | Growth equity (minority stakes, unit economics, path to profitability, governance) |
| `/private-credit` | private-credit | Direct lending (unitranche, mezz, covenant design, risk-adjusted yield) |
| `/secondaries` | secondaries | LP secondaries, GP-led continuation, NAV lending, fund restructuring |

**Venture Capital**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/vc` | venture-capital | General VC analysis (routes to specialized VC skills below) |
| `/vc-early` | vc-early | Pre-seed through Series A (term sheets, SAFEs, cap tables, dilution) |
| `/vc-growth` | vc-growth | Series B+ (growth metrics, biotech rNPV, crypto token econ, secondaries) |
| `/vc-fund` | vc-fund | Fund construction (portfolio math, reserves, J-curve, LP reporting) |

**Wealth Management**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/wealth` | wealth-advisory | General wealth advisory (routes to specialized wealth skills below) |
| `/retirement` | retirement | Retirement planning (Monte Carlo, withdrawal strategy, Social Security, Roth conversion) |
| `/estate` | estate | Estate & tax planning (trusts, GRATs, gifting, dynasty trusts, family office) |
| `/insurance` | insurance | Insurance analysis (life, disability, LTC, annuities, key person, buy-sell) |

**Quant**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/quant` | quant-signals | Strategy dev (signals, backtesting, regime detection, LLM sentiment) |

**CFO & Corporate Finance**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/budget` | budget | Annual budget build, variance analysis, zero-based budgeting |
| `/forecast` | forecast | Rolling forecasts, cash flow, scenario planning, revenue modeling |
| `/board-deck` | board-deck | Board reporting, KPI dashboards, investor updates, earnings prep |
| `/fpa` | fpa | FP&A, unit economics, SaaS metrics, headcount modeling, strategic finance |

## Skill Router

When a user describes a problem without invoking a specific skill, match their intent and suggest the right skill. Use this decision tree:

**"How much is this company worth?" / "Valuation"**
- Selling the company → `/sell-side`
- Acquiring the company → `/buy-side`
- PE buyout / LBO → `/pe-buyout`
- Growth equity / minority investment → `/pe-growth`
- Public equity investment thesis → `/long-short`
- Quick DCF or WACC calculation → just run `tools/dcf.py` or `tools/wacc.py`

**"Risk" / "How risky is this?"**
- Portfolio-level risk (VaR, drawdown, stress) → `/risk`
- Credit risk on a specific issuer → `/credit`
- Company in distress or near default → `/restructuring`
- Position sizing question → `/long-short` (Kelly) or run `tools/kelly.py`

**"Deal" / "M&A" / "Acquisition"**
- Selling → `/sell-side`
- Buying → `/buy-side`
- LBO / PE sponsor → `/pe-buyout`
- Deal already announced (spread trading) → `/merger-arb`
- IPO → `/ipo`

**"Options" / "Volatility" / "Greeks"**
- Pricing or strategy construction → `/derivatives`
- Market-making / quoting → `/market-making`
- Quick Black-Scholes calculation → run `tools/black_scholes.py`

**"Portfolio" / "Allocation" / "Rebalance"**
- Building or optimizing a portfolio → `/portfolio`
- Measuring performance vs benchmark → `/attribution`
- Risk analytics on existing portfolio → `/risk`

**"Startup" / "Fundraise" / "VC"**
- Seed / Series A evaluation → `/vc-early`
- Term sheet or cap table → `/vc-early`
- Series B+ / growth-stage company → `/vc-growth`
- Biotech rNPV or crypto token economics → `/vc-growth`
- VC fund construction or LP reporting → `/vc-fund`
- Building a fundraise deck → `/pitch-deck`
- General VC question → `/vc` (routes to the right sub-skill)

**"Budget" / "Forecast" / "FP&A" / "Board"**
- Annual budget build → `/budget`
- Cash flow or revenue forecast → `/forecast`
- Unit economics or SaaS metrics → `/fpa`
- Board presentation or investor update → `/board-deck`

**"Private equity" / "Buyout" / "PE" / "Private credit"**
- Control buyout / LBO → `/pe-buyout`
- Growth equity / minority investment → `/pe-growth`
- Direct lending / mezzanine / unitranche → `/private-credit`
- LP secondaries / GP-led continuation → `/secondaries`
- General PE question → `/pe` (routes to the right sub-skill)
- Quick LBO returns → run `tools/lbo.py`

**"Real estate" / "Property" / "Cap rate"**
- Buying a property or underwriting a deal → `/re-acquisitions`
- Ground-up development or construction → `/re-development`
- Debt sizing, DSCR, capital stack → `/re-debt`
- Public REIT analysis, FFO, NAV → `/re-reit`
- General RE question → `/real-estate` (routes to the right sub-skill)
- Quick cap rate or NOI calculation → run `tools/cap_rate.py` or `tools/re_noi.py`

**"Retirement" / "Wealth" / "Estate" / "Insurance"**
- Retirement planning, withdrawal strategy, Social Security → `/retirement`
- Estate tax, trusts, gifting, wealth transfer → `/estate`
- Life insurance, disability, LTC, annuities → `/insurance`
- General wealth question → `/wealth` (routes to the right sub-skill)
- Quick Monte Carlo simulation → run `tools/monte_carlo.py`

**"Macro" / "Rates" / "FX" / "Cross-asset"**
- Macro thesis or regime analysis → `/macro`

**"Quant" / "Signal" / "Backtest" / "Alpha"**
- Signal development or backtesting → `/quant`

**When ambiguous:** Ask the user one clarifying question — "Are you looking at this as a [buyer/seller/trader/risk manager]?" The answer determines the skill.

## The Alpha Stack Workflow

Every analysis follows six phases: **Source > Diligence > Model > Stress > Decide > Monitor**

1. **Source** — Identify the opportunity. Gather context, frame the question.
2. **Diligence** — Deep research using skill prompts. Structured analysis, cross-desk perspectives.
3. **Model** — Build the quantitative framework. Run Python tools, construct sensitivity tables.
4. **Stress** — Challenge every assumption. Pre-mortem, tail risk, Monte Carlo scenarios.
5. **Decide** — Synthesize into a recommendation with explicit risk/reward and conviction level.
6. **Monitor** — Define tracking criteria: thesis drift, catalysts, exit triggers, rebalancing rules.

## Tool Invocation

When a user's question involves quantitative analysis, run the relevant Python tool and show the output. Tools are in `tools/` and require only Python 3.10+ (no external dependencies).

| When the user asks about... | Run this tool |
|----------------------------|---------------|
| Company valuation, DCF, intrinsic value | `python3 tools/dcf.py` |
| LBO, leveraged buyout, PE returns | `python3 tools/lbo.py` |
| Cost of capital, WACC | `python3 tools/wacc.py` |
| Options pricing, Greeks, Black-Scholes | `python3 tools/black_scholes.py` |
| Implied volatility from option prices | `python3 tools/implied_vol.py` |
| Convertible bonds | `python3 tools/convertible.py` |
| Bond yield, duration, DV01 | `python3 tools/bond_yield.py` |
| Default risk, credit model | `python3 tools/merton_model.py` |
| Z-Score, CDS spread, credit analysis | `python3 tools/credit_spread.py` |
| Portfolio risk, Sharpe, drawdown, VaR | `python3 tools/portfolio_risk.py` |
| Position sizing, Kelly criterion | `python3 tools/kelly.py` |
| Performance attribution, Brinson | `python3 tools/brinson.py` |
| Portfolio optimization, Black-Litterman | `python3 tools/black_litterman.py` |
| Monte Carlo simulation, retirement | `python3 tools/monte_carlo.py` |
| Merger arb spread, deal probability | `python3 tools/merger_arb.py` |
| Real estate, cap rate, NOI | `python3 tools/cap_rate.py` |
| VC fund returns, dilution, TVPI | `python3 tools/vc_returns.py` |
| Loan amortization, mortgage | `python3 tools/loan_amort.py` |
| Market making, optimal quoting | `python3 tools/market_maker.py` |
| Treasury yield curve, risk-free rate | `python3 tools/fetch.py --treasury` |
| Economic data (fed funds, CPI, VIX) | `python3 tools/fetch.py --fred DGS10,FEDFUNDS` |
| Save/load analysis results | `python3 tools/state.py` |
| RE debt sizing, DSCR, LTV, debt yield | `python3 tools/re_debt.py` |
| RE equity waterfall, GP/LP promote | `python3 tools/re_waterfall.py` |
| RE development pro forma, yield on cost | `python3 tools/re_development.py` |
| RE NOI builder, rent roll projections | `python3 tools/re_noi.py` |
| IRR, NPV, MOIC, payback period | `python3 tools/irr.py` |
| Depreciation (straight-line, MACRS) | `python3 tools/depreciation.py` |

## Output Standards

When producing financial analysis:

- **Assumptions first.** Every number is a bet. List assumptions explicitly before presenting results.
- **Ranges over points.** Never present a single-point estimate without a sensitivity table or confidence range.
- **Show your work.** Include the tool command and its output so the user can verify and re-run with different inputs.
- **Risk caveats.** Every recommendation must include what kills the thesis — the bear case, the tail risk, the regime change.
- **No hallucinated numbers.** If the user has not provided a data point, ask for it. Never fabricate financial data.

## Standard Output Formats

Use these templates for consistent, scannable output across all skills.

**Valuation Summary:**
```
| Method              | Low     | Base    | High    |
|---------------------|---------|---------|---------|
| DCF (Gordon Growth) | $[X]M   | $[X]M   | $[X]M   |
| DCF (Exit Multiple) | $[X]M   | $[X]M   | $[X]M   |
| Precedent Txns      | $[X]M   | $[X]M   | $[X]M   |
| LBO Floor           | $[X]M   | $[X]M   | $[X]M   |
| **Recommended**     | **$[X]M** | **$[X]M** | **$[X]M** |
```

**Sensitivity Table:** Always a 5x5 grid with the two most impactful variables on the axes. Bold the base case cell. Label units clearly.

**Investment Recommendation:**
```
Recommendation: [Long/Short/Buy/Sell/Hold]
Conviction: [Low/Medium/High]
Target: $[X] ([X]% upside/downside)
Time Horizon: [X] months
Position Size: [X]% of [portfolio/NAV]
What Kills It: [one sentence — the single biggest risk]
```

**Risk Summary:** Top 3-5 risks in a table with Probability (Low/Med/High), Impact (Low/Med/High), and Mitigation (one sentence each).

**Monitoring Checklist:**
```
Thesis-confirming: [3 signals that validate the thesis]
Thesis-killing: [3 signals that invalidate — triggers for exit]
Review date: [specific date or event]
```

## Cross-Desk Analysis

When analyzing a company, event, or market move, offer to show it through multiple desk perspectives. The same acquisition looks different to an M&A banker, an event-driven hedge fund, a credit analyst, and an equity research analyst. Cross-referencing is a first-class feature — it is often where the real edge is found.

## Quick-Start Examples

Every skill has a ready-to-paste example scenario in `examples/`. When a user invokes a skill without providing context or inputs, suggest the relevant example:

- "Not sure where to start? Try pasting the scenario from `examples/sell-side.md` — it's a full specialty chemical M&A deal."
- Each example includes a company profile, financial data, and a "Try It" block with the exact prompt to paste.

The examples directory maps 1:1 to skills: `examples/lbo.md` for `/lbo`, `examples/fpa.md` for `/fpa`, etc.

## Repo Structure

```
skills/          26 skill directories, each with SKILL.md + prompts/
tools/           19 standalone Python calculators (stdlib-only, <200 lines each)
examples/        26 quick-start scenarios (one per skill, ready to paste)
mcp_server.py    MCP server exposing all tools for Claude Desktop
docs/            Workflow documentation
ETHOS.md         Finance AI philosophy
```
