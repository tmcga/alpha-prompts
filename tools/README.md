# Finance Tools

Standalone Python calculators with zero external dependencies. Each tool works from the command line or as an importable module.

**Requirements:** Python 3.10+ (stdlib only — no pip install needed).

## Tools

| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [dcf.py](dcf.py) | Discounted Cash Flow valuation | Enterprise value, equity value, price/share, sensitivity table |
| [lbo.py](lbo.py) | LBO returns calculator | MOIC, IRR, returns attribution (growth vs multiple vs leverage) |
| [black_scholes.py](black_scholes.py) | Options pricing with Greeks | Price, delta, gamma, vega, theta, rho, put-call parity |
| [wacc.py](wacc.py) | WACC calculator with CAPM | Cost of equity, WACC, capital structure, unlevered beta |
| [bond_yield.py](bond_yield.py) | Bond analytics | YTM, modified duration, Macaulay duration, convexity, DV01 |
| [portfolio_risk.py](portfolio_risk.py) | Portfolio risk metrics | Sharpe, Sortino, Calmar, max drawdown, VaR, CVaR |
| [merger_arb.py](merger_arb.py) | Merger arb spread analysis | Gross/annualized spread, implied deal probability, risk/reward |

## Quick Examples

```bash
# DCF: 5-year projection, 10% WACC, 2.5% terminal growth
python tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --net-debt 500 --shares 100

# LBO: $100M EBITDA, 10x entry, 5x leverage, 5-year hold
python tools/lbo.py --ebitda 100 --entry-multiple 10 --exit-multiple 11 --leverage 5 --rate 0.06 --growth 0.08 --years 5

# Options: Call option pricing
python tools/black_scholes.py --spot 100 --strike 105 --time 0.5 --rate 0.05 --vol 0.2 --type call

# WACC: Full capital structure analysis
python tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05

# Bond: 10-year semi-annual bond
python tools/bond_yield.py --face 1000 --coupon 0.05 --price 980 --years 10 --freq 2

# Portfolio: Risk metrics from returns
python tools/portfolio_risk.py --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01 --rf 0.04

# Merger arb: Cash deal spread analysis
python tools/merger_arb.py --current 45 --offer 50 --days 90 --type cash --rf 0.05
```

## Using as Modules

```python
from tools.dcf import dcf_valuation
from tools.black_scholes import black_scholes
from tools.portfolio_risk import portfolio_metrics

result = dcf_valuation(fcfs=[100, 110, 121], wacc=0.10, terminal_growth=0.025)
print(f"Enterprise Value: ${result['enterprise_value']:,.0f}")

greeks = black_scholes(spot=100, strike=105, time=0.5, rate=0.05, vol=0.2)
print(f"Delta: {greeks['delta']:.4f}")

risk = portfolio_metrics(returns=[0.02, -0.01, 0.03, 0.01, -0.02], risk_free=0.04)
print(f"Sharpe: {risk['sharpe']:.2f}")
```
