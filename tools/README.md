# Finance Tools

Standalone Python calculators with zero external dependencies. Each tool works from the command line or as an importable module.

**Requirements:** Python 3.10+ (stdlib only — no pip install needed).

## Tools

### Valuation & Corporate Finance
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [dcf.py](dcf.py) | DCF valuation (Gordon Growth or exit multiple) | Enterprise value, equity value, price/share, sensitivity table |
| [lbo.py](lbo.py) | LBO returns calculator with detailed FCF build | MOIC, IRR, returns attribution (growth vs multiple vs leverage) |
| [wacc.py](wacc.py) | WACC calculator with CAPM build-up | Cost of equity, WACC, capital structure, unlevered beta, size/country premia |

### Options & Derivatives
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [black_scholes.py](black_scholes.py) | Options pricing with Greeks | Price, delta, gamma, vega, theta, rho, vanna, charm |
| [implied_vol.py](implied_vol.py) | Implied volatility solver | Implied vol, moneyness, intrinsic/time value decomposition |
| [convertible.py](convertible.py) | Convertible bond pricer | Bond floor, parity, embedded option value, conversion premium, breakeven |

### Fixed Income & Credit
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [bond_yield.py](bond_yield.py) | Bond analytics with spread metrics | YTM, modified/Macaulay duration, convexity, DV01, G-spread, Z-spread |
| [merton_model.py](merton_model.py) | Merton structural credit model | Distance to default, default probability, credit spread, equity value |
| [credit_spread.py](credit_spread.py) | Credit analysis (Z-Score + spread) | Altman Z-Score, hazard rate, cumulative PD, expected loss |

### Portfolio & Risk
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [portfolio_risk.py](portfolio_risk.py) | Portfolio risk metrics | Sharpe, Sortino, Calmar, max drawdown, VaR/CVaR, tracking error, info ratio |
| [kelly.py](kelly.py) | Kelly criterion position sizer | Optimal fraction, geometric growth rate, drawdown probabilities |
| [brinson.py](brinson.py) | Brinson-Fachler performance attribution | Allocation, selection, interaction effects per sector |
| [black_litterman.py](black_litterman.py) | Black-Litterman portfolio optimizer | Equilibrium returns, posterior returns, optimal weights with views |
| [monte_carlo.py](monte_carlo.py) | Monte Carlo simulation engine | Percentile distribution, success/ruin probability, retirement planning |

### M&A & Special Situations
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [merger_arb.py](merger_arb.py) | Merger arb spread analysis | Gross/annualized spread, implied probability, collar, CVR support |

### Real Estate, VC & Lending
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [cap_rate.py](cap_rate.py) | Real estate valuation | Property value, cap rate decomposition, sensitivity, development spread |
| [vc_returns.py](vc_returns.py) | VC fund returns & dilution | TVPI/DPI/RVPI, net IRR, J-curve, dilution waterfall |
| [loan_amort.py](loan_amort.py) | Loan amortization schedule | Monthly payment, interest/principal split, early payoff savings |

### Quantitative Trading
| Tool | Description | Key Outputs |
|------|-------------|-------------|
| [market_maker.py](market_maker.py) | Avellaneda-Stoikov market making | Reservation price, optimal spread, bid/ask quotes, inventory risk |

## Quick Examples

```bash
# DCF: Gordon Growth terminal value
python tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --net-debt 500 --shares 100

# DCF: Exit multiple method
python tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --exit-multiple 12 --net-debt 500 --shares 100

# LBO: Detailed FCF build with tax rate
python tools/lbo.py --ebitda 100 --entry-multiple 10 --exit-multiple 11 --leverage 5 --rate 0.06 --growth 0.08 --tax-rate 0.25

# Options: Call pricing with dividend yield
python tools/black_scholes.py --spot 100 --strike 105 --time 0.5 --rate 0.05 --vol 0.2 --div 0.02 --type call

# Implied vol from market price
python tools/implied_vol.py --price 5.50 --spot 100 --strike 105 --time 0.5 --rate 0.05 --type call

# Kelly criterion: Half Kelly sizing
python tools/kelly.py --win-prob 0.55 --win-loss-ratio 1.5 --fraction 0.5

# Merton credit model
python tools/merton_model.py --assets 1000 --debt 600 --vol 0.25 --rate 0.04 --maturity 5

# Monte Carlo retirement simulation
python tools/monte_carlo.py --initial 1000000 --return 0.07 --vol 0.15 --years 30 --withdrawal 0.04 --goal 500000

# Brinson attribution
python tools/brinson.py --port-weights 0.30,0.25,0.20 --port-returns 0.12,0.08,0.05 --bench-weights 0.25,0.25,0.25 --bench-returns 0.10,0.09,0.06 --sectors Tech,Health,Finance

# Black-Litterman with views
python tools/black_litterman.py --weights 0.5,0.3,0.2 --cov "0.04,0.01,0.005;0.01,0.03,0.008;0.005,0.008,0.02" --views "1,0,-1" --view-returns 0.02 --assets Stocks,Bonds,Alts

# Credit: Altman Z-Score
python tools/credit_spread.py --zscore --wc-ta 0.1 --re-ta 0.2 --ebit-ta 0.15 --eq-debt 0.8 --sales-ta 1.5

# Credit: Default probability from CDS spread
python tools/credit_spread.py --spread 0.03 --recovery 0.40 --maturity 5

# Real estate cap rate
python tools/cap_rate.py --noi 5000000 --cap-rate 0.055 --rf 0.04 --growth 0.02

# VC fund performance
python tools/vc_returns.py --fund --contributions 10,10,10,5,5 --distributions 0,0,0,5,15 --nav 60 --years 5

# VC dilution waterfall
python tools/vc_returns.py --dilution --rounds "5M@20M,10M@80M,25M@300M" --founder-shares 8000000

# Loan amortization with extra payments
python tools/loan_amort.py --principal 500000 --rate 0.065 --years 30 --extra 500

# Convertible bond
python tools/convertible.py --face 1000 --coupon 0.02 --maturity 5 --spread 0.03 --stock 50 --ratio 15 --vol 0.30

# Avellaneda-Stoikov market maker
python tools/market_maker.py --mid 100 --inventory 50 --gamma 0.01 --vol 0.02 --time 0.5 --intensity 1.5

# Bond with spread analysis
python tools/bond_yield.py --face 1000 --coupon 0.05 --price 980 --years 10 --benchmark-yield 0.04

# WACC with size and country risk
python tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05 --size-premium 0.02 --country-risk 0.01

# Portfolio risk with benchmark
python tools/portfolio_risk.py --returns 0.02,-0.01,0.03,0.01,-0.02 --benchmark 0.01,0.00,0.02,0.01,-0.01 --rf 0.04

# Merger arb with CVR
python tools/merger_arb.py --current 45 --offer 50 --days 90 --type cash --cvr 5 --cvr-prob 0.6
```

## Using as Modules

```python
from tools.dcf import dcf_valuation
from tools.black_scholes import black_scholes
from tools.kelly import kelly_criterion
from tools.merton_model import merton_model
from tools.monte_carlo import monte_carlo_sim
from tools.brinson import brinson_attribution
from tools.black_litterman import black_litterman

result = dcf_valuation(fcfs=[100, 110, 121], wacc=0.10, terminal_growth=0.025)
print(f"Enterprise Value: ${result['enterprise_value']:,.0f}")

greeks = black_scholes(spot=100, strike=105, time=0.5, rate=0.05, vol=0.2)
print(f"Delta: {greeks['delta']:.4f}")

sizing = kelly_criterion(win_prob=0.55, win_loss_ratio=1.5, fraction=0.5)
print(f"Half Kelly: {sizing['applied_fraction']*100:.1f}%")
```
