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

## Finance Tools

Standalone Python scripts with zero external dependencies. Run from the command line or import as modules.

| Tool | What It Does | Example |
|------|-------------|---------|
| [dcf.py](tools/dcf.py) | DCF valuation with sensitivity tables | `python tools/dcf.py --fcf 100,110,121 --wacc 0.10 --terminal-growth 0.025` |
| [lbo.py](tools/lbo.py) | LBO returns (MOIC, IRR, attribution) | `python tools/lbo.py --ebitda 100 --entry-multiple 10 --leverage 5` |
| [black_scholes.py](tools/black_scholes.py) | Options pricing with full Greeks | `python tools/black_scholes.py --spot 100 --strike 105 --vol 0.2` |
| [wacc.py](tools/wacc.py) | WACC calculator with CAPM | `python tools/wacc.py --equity 1000 --debt 500 --beta 1.2` |
| [bond_yield.py](tools/bond_yield.py) | YTM, duration, convexity, DV01 | `python tools/bond_yield.py --face 1000 --coupon 0.05 --price 980` |
| [portfolio_risk.py](tools/portfolio_risk.py) | Sharpe, Sortino, max drawdown, VaR | `python tools/portfolio_risk.py --returns 0.02,-0.01,0.03,0.01` |
| [merger_arb.py](tools/merger_arb.py) | Merger arb spread and implied probability | `python tools/merger_arb.py --current 45 --offer 50 --days 90` |

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
