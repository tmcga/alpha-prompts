# Alpha Stack

> What if every analyst had a senior MD's frameworks, a quant's toolkit, and a risk officer's discipline — loaded into their terminal?

**Alpha Stack** is an installable AI skill system for finance. 12 skills covering every major Wall Street desk, 19 computational tools with zero dependencies, and a structured workflow for investment analysis — from sourcing ideas to monitoring positions.

It turns Claude Code into a **virtual finance team**: an M&A banker who builds merger models, a derivatives trader who thinks in Greeks, a portfolio manager who optimizes with Black-Litterman, and a risk officer who stress-tests everything with Monte Carlo.

---

## Install (30 seconds)

```bash
git clone https://github.com/tmcga/alpha-prompts.git ~/alpha-stack
cd ~/alpha-stack && ./setup.sh
```

Open Claude Code. Type `/deal`. You're running.

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

## 12 Skills

| Command | Skill | What It Does |
|---------|-------|-------------|
| `/deal` | Deal Execution | M&A advisory, leveraged finance, restructuring, fairness opinions |
| `/markets` | Capital Markets | ECM, DCM, equity research, IPO analysis |
| `/derivatives` | Options & Derivatives | Black-Scholes, Greeks, implied vol, convertible bonds |
| `/trade` | Trading & Execution | Equities, FI, FX, commodities, Avellaneda-Stoikov market making |
| `/hedge` | Hedge Fund Strategies | L/S equity, macro, quant, event-driven, credit/distressed |
| `/pe` | Private Capital | Buyouts, growth equity, special sits, private credit |
| `/real-assets` | Real Assets | Real estate (cap rates, development), infrastructure |
| `/portfolio` | Portfolio Construction | Black-Litterman, Brinson attribution, factor investing |
| `/risk` | Risk Analytics | VaR/CVaR, Monte Carlo, stress testing, tail risk |
| `/vc` | Venture Capital | Seed through growth, dilution modeling, fund metrics (TVPI/IRR) |
| `/wealth` | Wealth Advisory | Retirement planning, estate/tax, goals-based allocation |
| `/quant` | Quant Signals | Strategy development, LLM sentiment, cross-desk analysis |

Each skill includes role-specific AI personas, structured workflows, mathematical frameworks, and automatic tool invocation.

---

## 19 Computational Tools

Standalone Python calculators. Zero dependencies — just Python 3.10+. Run from CLI or import as modules.

| Domain | Tools |
|--------|-------|
| **Valuation** | `dcf.py` `lbo.py` `wacc.py` |
| **Options** | `black_scholes.py` `implied_vol.py` `convertible.py` |
| **Fixed Income & Credit** | `bond_yield.py` `merton_model.py` `credit_spread.py` |
| **Portfolio & Risk** | `portfolio_risk.py` `kelly.py` `brinson.py` `black_litterman.py` `monte_carlo.py` |
| **M&A** | `merger_arb.py` |
| **RE / VC / Lending** | `cap_rate.py` `vc_returns.py` `loan_amort.py` |
| **Quant Trading** | `market_maker.py` |

```bash
# Run any tool directly
python3 tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --shares 100
python3 tools/kelly.py --win-prob 0.55 --win-loss-ratio 1.5 --fraction 0.5
python3 tools/monte_carlo.py --initial 1000000 --return 0.07 --vol 0.15 --years 30 --withdrawal 0.04
```

Full tool documentation at [tools/README.md](tools/README.md).

---

## Claude Desktop (MCP Server)

Alpha Stack is also a **finance MCP server** — 23 tools that Claude Desktop can call natively. No terminal, no Python knowledge. Just ask a question and Claude runs the math.

### Setup

```bash
git clone https://github.com/tmcga/alpha-prompts.git ~/alpha-stack
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

### 23 MCP Tools

| Category | Tools Available |
|----------|---------------|
| **Valuation** | `dcf_valuation` `lbo_returns` `wacc` |
| **Options & Derivatives** | `black_scholes` `implied_volatility` `convertible_bond` |
| **Fixed Income & Credit** | `bond_analytics` `merton_model` `altman_zscore` `credit_from_spread` |
| **Portfolio & Risk** | `portfolio_metrics` `benchmark_relative` `kelly_criterion` `multi_outcome_kelly` `brinson_attribution` `black_litterman` `monte_carlo_sim` |
| **M&A** | `merger_arb` |
| **RE / VC / Lending** | `real_estate_valuation` `fund_metrics` `dilution_waterfall` `loan_amortization` |
| **Quant Trading** | `optimal_quotes` |

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

        The majority of returns come from deleveraging — the debt paydown
        from $500M to $120M drives 71.5% of the return. Multiple expansion
        from 10x to 11x adds another 27.6%...
```

```
You:    Size my position. Win probability 55%, win/loss ratio 1.5.

Claude: [calls kelly_criterion tool]

        Full Kelly: 25.0% of capital
        Half Kelly: 12.5% (recommended)
        Edge: +37.5%
        P(50% drawdown) at full Kelly: 12.5%

        I'd recommend half Kelly here. The edge is real but the
        drawdown risk at full Kelly is meaningful...
```

---

## Example Session

```
You:     /deal
Claude:  Deal Execution skill activated. What deal are you working on?

You:     Sell-side M&A for a $200M revenue specialty chemical company.
         EBITDA: $60M, growing 8%. Net debt: $150M. 100M shares out.

Claude:  Let me build the valuation framework.
         [Runs DCF, LBO, and WACC tools]
         [Produces sensitivity tables]
         [Generates buyer universe with strategic rationale]
         [Stress-tests the downside: margin compression, cyclical risk]
         [Delivers valuation range: $850M-$1.1B enterprise value]
```

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
├── mcp_server.py          MCP server (23 tools for Claude Desktop)
├── pyproject.toml         Python dependencies (mcp SDK)
├── skills/                12 skill directories (SKILL.md + prompts/)
│   ├── deal-execution/
│   ├── hedge-fund-strategies/
│   ├── portfolio-construction/
│   └── ...
├── tools/                 19 Python calculators (stdlib-only)
├── tests/                 53 pytest tests
└── docs/                  Workflow documentation
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new skills, prompts, or tools.

## License

[MIT](LICENSE)
