# Market Making: Mid-Cap ETF Quoting

## Instrument
- **Product:** Sector ETF tracking semiconductor equipment (fictional)
- **Current Mid Price:** $142.50
- **Daily Volume:** 2.4M shares
- **Tick Size:** $0.01
- **Typical Spread:** $0.04 (2.8bps)

## Model Parameters
- **Estimated Volatility (annualized):** 32%
- **Drift:** 0 (assume mean-reverting intraday)
- **Mean-Reversion Speed (kappa):** 1.5
- **Order Arrival Intensity (lambda):** 120 orders/minute per side
- **Risk Aversion (gamma):** 0.01

## Current State
- **Current Inventory:** +350 shares (slightly long)
- **Inventory Limits:** +/- 5,000 shares hard cap
- **Session Time Remaining:** 4.5 hours (270 minutes)

## Objectives
- Maximize expected P&L while keeping inventory bounded
- Target spread capture of $0.03-0.05 per round trip
- End-of-day inventory target: flat (+/- 500 shares)

## Try It
```
/market-making

Making markets in a semiconductor equipment ETF. Mid price $142.50, 2.4M
shares daily volume, $0.04 typical spread. Vol is 32% annualized, order
arrival 120/min per side. Currently +350 shares inventory, hard limit +/-5K.
Risk aversion gamma 0.01. 4.5 hours left in session. What are my optimal
bid/ask quotes? How should I adjust as inventory builds?
```
