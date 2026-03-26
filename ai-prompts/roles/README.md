# Finance Role Prompt Libraries

Role-specific prompt templates with domain frameworks, mathematical models, and analytical patterns for different finance professionals.

## Roles

| Role | Focus | Key Frameworks |
|------|-------|----------------|
| [Hedge Fund Analyst](hedge-fund-analyst.md) | Alpha research, portfolio construction, risk management | IC/IR, Black-Litterman, Kelly criterion, factor models, Deflated Sharpe Ratio |
| [Investment Banker](investment-banker.md) | Valuation, M&A, capital structure, financial modeling | DCF/WACC, comps, precedents, accretion/dilution, LBO returns |
| [PE Analyst](pe-analyst.md) | Deal screening, LBO modeling, due diligence, value creation | LBO math (MOIC/IRR), returns bridge, 100-day plans, buy-and-build |

## How to Use

Each role file contains:
1. **Role context prompt** — sets the AI's persona and analytical lens
2. **Categorized prompt templates** — copy, fill in your data, and use with Claude or any LLM
3. **Mathematical frameworks** — key formulas and models referenced inline

Start with the role context prompt, then use the specific template that matches your task. The role context helps the AI calibrate its level of detail, terminology, and analytical rigor.

## Combining Roles

Many real-world analyses cross role boundaries:
- **PE analyst doing IB-style valuation**: Use the IB valuation prompts but frame the output through the PE lens (IRR/MOIC sensitivity, downside protection)
- **HF analyst evaluating an event**: Use the IB M&A frameworks for deal analysis, then the HF risk/sizing frameworks for position construction
- **IB analyst building a pitch**: Use PE screening criteria to understand what financial buyers will pay, and HF frameworks to understand public market reception
