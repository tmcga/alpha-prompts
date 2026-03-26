# Risk Analytics: Hedge Fund Portfolio Stress Test

## Portfolio Type
Multi-asset long/short equity + options overlay

## Portfolio Positions
| Position | Weight | Asset Type | Beta | Notes |
|----------|--------|-----------|------|-------|
| Tech mega-cap basket (long) | 25% | Equity | 1.2 | FAANG-type exposure |
| Healthcare (long) | 15% | Equity | 0.7 | Defensive pharma |
| Consumer discretionary (short) | -12% | Equity | 1.4 | Retail shorts |
| Energy (long) | 10% | Equity | 1.1 | Oil services |
| Put spread on S&P 500 | 3% | Options | -0.3 | Tail hedge, 5% OTM |
| IG Credit (long) | 8% | Fixed Income | 0.2 | BBB rated portfolio |
| Cash | 51% | Cash | 0.0 | Dry powder |

## Historical Return Data (Monthly, Last 24 Months)
Portfolio returns: 1.2%, -0.8%, 2.1%, 0.3%, -1.5%, 3.2%, 1.8%, -2.4%, 0.9%, 1.1%, -0.6%, 2.8%, 0.5%, -1.2%, 1.7%, -3.1%, 2.4%, 0.8%, -0.4%, 1.9%, -1.8%, 3.5%, 1.0%, -0.2%

Benchmark (S&P 500) returns: 1.5%, -1.2%, 2.8%, 0.1%, -2.0%, 4.1%, 2.2%, -3.5%, 1.3%, 1.8%, -0.9%, 3.5%, 0.8%, -1.8%, 2.2%, -4.0%, 3.1%, 1.0%, -0.6%, 2.5%, -2.3%, 4.2%, 1.5%, -0.3%

## Risk Measures Needed
- VaR (95% and 99%, 1-day and 10-day)
- CVaR / Expected Shortfall
- Maximum drawdown analysis
- Stress scenarios: 2008 GFC replay, 2020 COVID crash, 2022 rate shock
- Factor decomposition (market, size, value, momentum, volatility)
- Tail risk metrics (skewness, kurtosis)

## Parameters
- **Confidence Level:** 99% for regulatory, 95% for internal
- **Horizon:** 1-day VaR for daily risk, 10-day for stress
- **Risk-Free Rate:** 4.8%

## Try It
```
/risk

Hedge fund portfolio: 25% tech longs, 15% healthcare longs, -12% consumer
discretionary shorts, 10% energy longs, 3% put spread tail hedge, 8% IG credit,
51% cash. Monthly returns for 24 months provided. Need VaR at 95% and 99%,
CVaR, max drawdown, and stress tests (2008 GFC, 2020 COVID, 2022 rate shock).
Also want factor decomposition. Risk-free rate 4.8%.
```
