# Alpha Prompts

The open-source Wall Street AI toolkit. 50+ prompt libraries covering every major desk across finance, plus lightweight tools for valuation, options pricing, and portfolio analysis.

**Every prompt includes:** role-specific AI personas, mathematical frameworks, and fill-in-the-blank templates ready for Claude, ChatGPT, or any LLM.

## Quick Start

Pick your desk and start prompting:

| Category | Desks | Highlights |
|----------|-------|------------|
| [Banking](ai-prompts/banking/) | M&A, LevFin, ECM, DCM, Restructuring, Research | Merger models, covenant analysis, IPO pricing, waterfall analysis |
| [Trading](ai-prompts/trading/) | Equities, Fixed Income, Derivatives, Structured Products, FX, Commodities, Market Making | Black-Scholes Greeks, CLO waterfalls, Avellaneda-Stoikov |
| [Hedge Funds](ai-prompts/hedge-funds/) | Fundamental L/S, Global Macro, Quant/Systematic, Event-Driven, Credit | Kelly criterion, merger arb, factor models, Merton model |
| [Private Capital](ai-prompts/private-capital/) | Buyouts, Growth Equity, Real Estate, Private Credit, Infrastructure, Special Situations | LBO modeling, cap rates, covenant design, concession analysis |
| [Asset Management](ai-prompts/asset-management/) | Active Equity, Factor/Systematic, Fixed Income, Multi-Asset, Alternatives, Risk | Black-Litterman, Brinson attribution, VaR/CVaR, factor decomposition |
| [Venture Capital](ai-prompts/venture/) | Early Stage, Growth, Crypto/Web3, Biotech, Platform Ops | Token economics, rNPV, term sheets, founder evaluation |
| [Wealth Management](ai-prompts/wealth-management/) | Private Banking, Financial Planning, Estate/Tax, Alternatives, Portfolio Construction | GRAT modeling, Monte Carlo, goals-based allocation, tax-loss harvesting |

**Start here:** The [Cross-Reference Guide](ai-prompts/cross-reference-guide.md) shows how the same event looks through 5 different desk lenses — 24 perspectives total.

## Finance Tools (19)

Standalone Python calculators with zero external dependencies. Run from the command line or import as modules.

**Valuation & Corporate Finance**
| Tool | What It Does |
|------|-------------|
| [dcf.py](tools/dcf.py) | DCF valuation — Gordon Growth or exit multiple, with sensitivity tables |
| [lbo.py](tools/lbo.py) | LBO returns — MOIC, IRR, attribution, detailed FCF build |
| [wacc.py](tools/wacc.py) | WACC — CAPM build-up with size premium, country risk |

**Options & Derivatives**
| Tool | What It Does |
|------|-------------|
| [black_scholes.py](tools/black_scholes.py) | Options pricing — Greeks, vanna, charm, dividend yield |
| [implied_vol.py](tools/implied_vol.py) | Implied volatility solver from market prices |
| [convertible.py](tools/convertible.py) | Convertible bond pricer — bond floor, parity, embedded option |

**Fixed Income & Credit**
| Tool | What It Does |
|------|-------------|
| [bond_yield.py](tools/bond_yield.py) | Bond analytics — YTM, duration, convexity, DV01, G/Z-spread |
| [merton_model.py](tools/merton_model.py) | Structural credit model — distance to default, credit spreads |
| [credit_spread.py](tools/credit_spread.py) | Credit analysis — Altman Z-Score, hazard rates, default probabilities |

**Portfolio & Risk**
| Tool | What It Does |
|------|-------------|
| [portfolio_risk.py](tools/portfolio_risk.py) | Risk metrics — Sharpe, Sortino, VaR, CVaR, benchmark-relative |
| [kelly.py](tools/kelly.py) | Kelly criterion — optimal position sizing, drawdown risk |
| [brinson.py](tools/brinson.py) | Brinson-Fachler performance attribution |
| [black_litterman.py](tools/black_litterman.py) | Black-Litterman portfolio optimizer with investor views |
| [monte_carlo.py](tools/monte_carlo.py) | Monte Carlo simulation — portfolio growth, retirement planning |

**M&A & Special Situations**
| Tool | What It Does |
|------|-------------|
| [merger_arb.py](tools/merger_arb.py) | Merger arb — spreads, implied probability, collar, CVR |

**Real Estate, VC & Lending**
| Tool | What It Does |
|------|-------------|
| [cap_rate.py](tools/cap_rate.py) | Real estate valuation — cap rate, NOI, development spread |
| [vc_returns.py](tools/vc_returns.py) | VC fund returns (TVPI/DPI/RVPI/IRR) and dilution waterfall |
| [loan_amort.py](tools/loan_amort.py) | Loan amortization — payment schedule, early payoff savings |

**Quantitative Trading**
| Tool | What It Does |
|------|-------------|
| [market_maker.py](tools/market_maker.py) | Avellaneda-Stoikov optimal quoting — reservation price, spread |

No dependencies required — just Python 3.10+.

## How to Use the Prompts

1. **Pick your desk** from the table above
2. **Copy the role context prompt** at the top of each file — it calibrates the AI
3. **Fill in the brackets** `[like this]` with your specific data
4. **Paste into Claude, ChatGPT, or any LLM**

Each file includes 4-6 prompt templates organized by workflow, with mathematical frameworks inline.

## Full Prompt Library

```
ai-prompts/
├── cross-reference-guide.md           # Same scenario, 5 desk perspectives, 24 prompts
├── banking/                           # M&A, LevFin, ECM, DCM, Restructuring, Research
├── trading/                           # Equities, FI, Derivatives, Structured, FX, Commodities, MM
├── hedge-funds/                       # L/S, Macro, Quant, Event-Driven, Credit
├── private-capital/                   # Buyouts, Growth, RE, Credit, Infra, Special Sits
├── asset-management/                  # Active, Factor, FI, Multi-Asset, Alts, Risk
├── venture/                           # Early, Growth, Crypto, Biotech, Platform Ops
├── wealth-management/                 # Private Banking, Planning, Estate, Alts, Portfolio
├── roles/                             # Foundation libraries (HF, IB, PE)
├── strategy-development.md            # Quant trading strategy design
└── llm-sentiment-prompts.md           # LLM-powered sentiment classification
```

Browse the full index at [ai-prompts/README.md](ai-prompts/README.md).

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

To add a new desk or tool:
1. Follow the existing template (role context + categorized prompts + math frameworks)
2. Open a PR

## License

[MIT](LICENSE)
