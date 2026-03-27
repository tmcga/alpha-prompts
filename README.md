# Alpha Stack

[![CI](https://github.com/tmcga/alpha-stack/actions/workflows/ci.yml/badge.svg)](https://github.com/tmcga/alpha-stack/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-44-orange)
![Tools](https://img.shields.io/badge/tools-25-purple)

> What if every analyst had a senior MD's frameworks, a quant's toolkit, and a risk officer's discipline — loaded into their terminal?

**Alpha Stack** is an installable AI skill system for finance. 44 skills covering every major Wall Street desk, corporate finance function, and back-office operation, 25 computational tools with zero dependencies, and a structured workflow for investment analysis — from sourcing ideas to monitoring positions.

### Why Alpha Stack?

- **Not prompts — pipelines.** Each skill is a 200-870 line execution pipeline with phased workflows, decision gates, and quality checks. Not a list of questions to ask.
- **Real math, not vibes.** 25 Python tools that run DCF, Black-Scholes, Monte Carlo, Black-Litterman, LBO, DSCR sizing, equity waterfalls, and more. Every recommendation is backed by a calculation you can verify.
- **Adversarial by default.** Every thesis gets a pre-mortem. Every valuation gets a sensitivity table. Every recommendation includes what kills it.
- **Zero dependencies.** All tools are stdlib-only Python. Install in 30 seconds. No API keys, no accounts, no subscriptions.

---

## Install (30 seconds)

```bash
git clone https://github.com/tmcga/alpha-stack.git ~/alpha-stack
cd ~/alpha-stack && ./setup.sh
```

Open Claude Code. Type `/sell-side`. You're running.

**For Claude Desktop** (no terminal needed): run `./setup-mcp.sh` instead. See [MCP Server](#claude-desktop-mcp-server) below.

---

## The Workflow

Every analysis follows six phases:

```
  Source ──> Diligence ──> Model ──> Stress ──> Decide ──> Monitor
    │           │            │          │          │          │
  Frame the   Research    Run the    Break the   Ship the   Track the
  question    deeply      numbers    thesis      memo       position
```

**Source** — Identify the opportunity. Frame the analytical question.
**Diligence** — Deep research using desk-specific prompt frameworks.
**Model** — Build the quantitative case. Run Python tools, sensitivity tables.
**Stress** — Pre-mortem. What kills this thesis? Who is on the other side?
**Decide** — Recommendation with conviction level, sizing, and risk/reward.
**Monitor** — Catalyst calendar, thesis-drift triggers, exit criteria.

---

## 44 Skills

**Deal & Banking**
| Command | What It Does |
|---------|-------------|
| `/sell-side` | Sell-side M&A — teaser, CIM, buyer mapping, bid evaluation, fairness opinion |
| `/buy-side` | Buy-side acquisition — target screening, valuation, synergies, offer structuring |
| `/lbo` | LBO modeling — debt sizing, returns attribution, sensitivity, exit analysis |
| `/restructuring` | Distressed — liquidity triage, waterfall, fulcrum security, plan of reorg |
| `/ipo` | IPO analysis — readiness, valuation, bookbuilding, pricing, stabilization |
| `/pitch-deck` | Pitch deck builder — startup fundraise, deal marketing, fund pitch, internal |
| `/investment-memo` | IC memo — equity L/S, PE/VC, credit, and real estate modes |

**Trading & Derivatives**
| Command | What It Does |
|---------|-------------|
| `/trade` | Execution analysis — block trades, VWAP/TWAP, market impact, TCA |
| `/derivatives` | Options pricing — Greeks, implied vol, strategy construction, convertibles |
| `/market-making` | Avellaneda-Stoikov — optimal quoting, inventory management, regime adaptation |

**Hedge Funds**
| Command | What It Does |
|---------|-------------|
| `/long-short` | L/S equity — variant perception, catalyst mapping, Kelly sizing, monitoring |
| `/macro` | Global macro — regime identification, cross-asset expression, geopolitical risk |
| `/merger-arb` | Event-driven — deal spread, implied probability, collar/CVR, portfolio exposure |
| `/credit` | Credit analysis — Z-Score, Merton model, recovery, relative value, IG/HY/distressed |

**Portfolio & Risk**
| Command | What It Does |
|---------|-------------|
| `/portfolio` | Portfolio construction — Black-Litterman, risk parity, factor, constrained optimization |
| `/risk` | Risk analytics — VaR/CVaR, Monte Carlo stress testing, factor decomposition, tail risk |
| `/attribution` | Performance attribution — Brinson-Fachler, factor, currency, fixed income, multi-period |

**Real Estate**
| Command | What It Does |
|---------|-------------|
| `/re-acquisitions` | Property acquisition underwriting — core, value-add, opportunistic strategies |
| `/re-development` | Ground-up development — cost build, lease-up, yield on cost, construction financing |
| `/re-debt` | Capital stack structuring — DSCR/LTV/debt yield sizing, mezzanine, preferred, bridge |
| `/re-reit` | Public REIT analysis — NAV, FFO/AFFO, implied cap rates, sector comps |

**Private Capital**
| Command | What It Does |
|---------|-------------|
| `/pe-buyout` | Control buyouts — LBO, platform + bolt-on, returns attribution, value creation |
| `/pe-growth` | Growth equity — minority stakes, unit economics, path to profitability, governance |
| `/private-credit` | Direct lending — unitranche, mezzanine, covenant design, risk-adjusted yield |
| `/secondaries` | LP secondaries — GP-led continuation, NAV lending, fund restructuring |

**Venture Capital**
| Command | What It Does |
|---------|-------------|
| `/vc-early` | Pre-seed through Series A — term sheets, SAFEs, cap tables, dilution modeling |
| `/vc-growth` | Series B+ — growth metrics, biotech rNPV, crypto token economics, secondary shares |
| `/vc-fund` | Fund construction — portfolio math, reserves, power law, J-curve, LP reporting |

**Wealth Management**
| Command | What It Does |
|---------|-------------|
| `/retirement` | Retirement planning — Monte Carlo, withdrawal strategy, Social Security, Roth conversion |
| `/estate` | Estate & tax planning — trusts, GRATs, gifting, dynasty trusts, family office |
| `/insurance` | Insurance analysis — life, disability, LTC, annuities, key person, buy-sell |

**Quant**
| Command | What It Does |
|---------|-------------|
| `/quant` | Strategy development — signals, backtesting, overfitting detection, LLM sentiment, regime |

**CFO & Corporate Finance**
| Command | What It Does |
|---------|-------------|
| `/budget` | Annual budget build, variance analysis, zero-based budgeting, departmental review |
| `/forecast` | Rolling forecasts, 13-week cash flow, scenario planning, revenue modeling |
| `/board-deck` | Board reporting, KPI dashboards, investor updates, earnings prep |
| `/fpa` | FP&A — unit economics, SaaS metrics, headcount modeling, strategic finance |

**Accounting & Data**
| Command | What It Does |
|---------|-------------|
| `/accounting` | Journal entries, accruals, closing process, chart of accounts, ASC 606/842 |
| `/financial-statements` | P&L, balance sheet, cash flow (indirect method), ratio analysis, DuPont |
| `/audit` | Audit planning, risk assessment, substantive testing, controls, sampling |
| `/data-entry` | Financial data extraction, cleaning, normalization, validation |

Each skill is an execution pipeline with phased workflows, decision gates, tool integration, quality gates, hard constraints, and common pitfalls.

Every skill has a **ready-to-paste example** in [`examples/`](examples/) — realistic scenarios with all inputs pre-filled so you can try any skill immediately without inventing data.

---

## 25 Computational Tools

Standalone Python calculators. Zero dependencies — just Python 3.10+. Run from CLI or import as modules.

| Domain | Tools |
|--------|-------|
| **Valuation** | `dcf.py` `lbo.py` `wacc.py` `irr.py` |
| **Options** | `black_scholes.py` `implied_vol.py` `convertible.py` |
| **Fixed Income & Credit** | `bond_yield.py` `merton_model.py` `credit_spread.py` |
| **Portfolio & Risk** | `portfolio_risk.py` `kelly.py` `brinson.py` `black_litterman.py` `monte_carlo.py` |
| **M&A** | `merger_arb.py` |
| **Real Estate** | `cap_rate.py` `re_debt.py` `re_waterfall.py` `re_development.py` `re_noi.py` |
| **VC / Lending** | `vc_returns.py` `loan_amort.py` |
| **Tax & Depreciation** | `depreciation.py` |
| **Quant Trading** | `market_maker.py` |

```bash
# Run any tool directly
python3 tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --shares 100
python3 tools/re_debt.py --noi 1800000 --value 28000000 --rate 0.0625 --min-dscr 1.25 --max-ltv 0.65
python3 tools/re_waterfall.py --equity 10000000 --cfs 800000,900000,1000000,1100000,15000000
python3 tools/irr.py --cfs="-1000000,200000,300000,400000,500000"
```

Full tool documentation at [tools/README.md](tools/README.md).

---

## Claude Desktop (MCP Server)

Alpha Stack is also a **finance MCP server** — 37 tools that Claude Desktop can call natively. No terminal, no Python knowledge. Just ask a question and Claude runs the math.

### Setup

```bash
git clone https://github.com/tmcga/alpha-stack.git ~/alpha-stack
cd ~/alpha-stack && ./setup-mcp.sh
```

Restart Claude Desktop. Look for the hammer icon — that means the tools are live.

<details>
<summary>Manual setup (without installer)</summary>

1. Install [uv](https://docs.astral.sh/uv/): `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Install dependencies: `cd ~/alpha-stack && uv sync`
3. Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "alpha-stack": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/alpha-stack", "python", "mcp_server.py"]
    }
  }
}
```
4. Restart Claude Desktop.
</details>

### What It Looks Like

```
You:    I'm looking at a company with EBITDA of $100M. Entry at 10x, exit at 11x,
        5x leverage, 6% rate, 8% EBITDA growth, 5 year hold. What are sponsor returns?

Claude: [calls lbo_returns tool]

        MOIC: 2.99x
        IRR: 24.5%

        Returns Attribution:
          EBITDA Growth:    0.9%
          Multiple Change: 27.6%
          Deleveraging:    71.5%
```

```
You:    Size a senior loan on a $28M property with $1.8M NOI at 6.25%.

Claude: [calls re_debt_sizing tool]

        Binding Constraint: LTV
        Max Loan:     $18,200,000
        Actual DSCR:  1.34x
        Debt Yield:   9.89%
        Positive Leverage: YES
```

---

## See It In Action

Full annotated example outputs with real tool results:

- **[Sell-Side M&A](examples/outputs/sell-side-chemicals.md)** — DCF valuation, LBO floor, buyer universe, risk matrix for a specialty chemical company
- **[LBO Analysis](examples/outputs/lbo-software-buyout.md)** — Returns attribution, sensitivity tables, debt schedule for a cloud security buyout
- **[Long/Short Equity](examples/outputs/long-short-semis.md)** — Variant perception thesis, Kelly sizing, catalyst calendar for semi equipment
- **[Retirement Planning](examples/outputs/retirement-monte-carlo.md)** — Monte Carlo simulation, ruin probability, portfolio recommendations
- **[Performance Attribution](examples/outputs/quarterly-attribution.md)** — Brinson-Fachler decomposition, CIO commentary

Every skill also has a **ready-to-paste example scenario** in [`examples/`](examples/) — try any skill immediately without inventing data.

---

## Philosophy

Alpha Stack is built on seven principles documented in [ETHOS.md](ETHOS.md):

1. **Assumptions are the model** — every number is a bet; make the bets explicit
2. **Second-order thinking** — "and then what?" is the most important question
3. **Adversarial by default** — pre-mortem every thesis before it gets capital
4. **Precision over confidence** — ranges over point estimates, distributions over averages
5. **Tools verify intuition** — run the math, then interpret
6. **Cross-desk fluency** — seeing all perspectives is the edge
7. **No hallucinated numbers** — if the data doesn't exist, ask for it

---

## Project Structure

```
alpha-stack/
├── CLAUDE.md              AI-native instructions for Claude Code
├── ETHOS.md               The Alpha Edge — finance AI philosophy
├── setup.sh               Claude Code skill installer
├── setup-mcp.sh           Claude Desktop MCP installer
├── mcp_server.py          MCP server (37 tools for Claude Desktop)
├── pyproject.toml         Python dependencies (mcp SDK)
├── examples/              26 ready-to-paste scenarios + 5 annotated outputs
├── scripts/               Contributor scaffolding (new-skill.sh, new-tool.sh)
├── skills/                44 skill directories (SKILL.md + prompts/)
│   ├── sell-side/         782 lines — full M&A process
│   ├── re-acquisitions/   240 lines — property acquisition underwriting
│   ├── pe-buyout/         257 lines — control buyout analysis
│   ├── vc-early/          252 lines — early-stage VC evaluation
│   ├── retirement/        282 lines — Monte Carlo retirement planning
│   └── ... (35 more)
├── tools/                 25 Python calculators (stdlib-only, <200 lines each)
├── tests/                 98 pytest tests
└── docs/                  Workflow documentation
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new skills, prompts, or tools. Scaffolding scripts in [`scripts/`](scripts/) create properly structured files from templates. All contributions welcome.

## License

[MIT](LICENSE) — use it however you want.
