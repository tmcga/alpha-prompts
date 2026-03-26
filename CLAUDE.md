# Alpha Stack

This is **Alpha Stack** — an installable AI skill system for finance. 22 skills, 19 computational tools, and a structured workflow for investment analysis.

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

**Alternatives**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/pe` | private-capital | Private equity (buyouts, growth, credit, fund metrics) |
| `/vc` | venture-capital | Venture capital (term sheets, cap tables, dilution, rNPV, crypto) |
| `/real-estate` | real-estate | Real estate (cap rates, development, REIT, debt structuring) |
| `/wealth` | wealth-advisory | Wealth advisory (retirement, estate/tax, goals-based, insurance) |

**Quant**
| Command | Skill | What It Does |
|---------|-------|-------------|
| `/quant` | quant-signals | Strategy dev (signals, backtesting, regime detection, LLM sentiment) |

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

## Output Standards

When producing financial analysis:

- **Assumptions first.** Every number is a bet. List assumptions explicitly before presenting results.
- **Ranges over points.** Never present a single-point estimate without a sensitivity table or confidence range.
- **Show your work.** Include the tool command and its output so the user can verify and re-run with different inputs.
- **Risk caveats.** Every recommendation must include what kills the thesis — the bear case, the tail risk, the regime change.
- **No hallucinated numbers.** If the user has not provided a data point, ask for it. Never fabricate financial data.

## Cross-Desk Analysis

When analyzing a company, event, or market move, offer to show it through multiple desk perspectives. The same acquisition looks different to an M&A banker, an event-driven hedge fund, a credit analyst, and an equity research analyst. Cross-referencing is a first-class feature — it is often where the real edge is found.

## Repo Structure

```
skills/          22 skill directories, each with SKILL.md + prompts/
tools/           19 standalone Python calculators (stdlib-only, <200 lines each)
mcp_server.py    MCP server exposing all tools for Claude Desktop
docs/            Workflow documentation
ETHOS.md         Finance AI philosophy
```
