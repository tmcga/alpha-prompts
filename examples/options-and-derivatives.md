# Options & Derivatives: Earnings Straddle on Tech Mega-Cap

## Workflow Mode
Alpha generation — pre-earnings volatility trade

## Underlier
- **Stock:** Large-cap cloud computing company (fictional, similar to CRM/SNOW profile)
- **Current Price:** $285.00
- **Earnings Date:** 14 days away
- **Implied Vol (30-day ATM):** 42%
- **Historical Realized Vol (30-day):** 28%
- **Average Earnings Move (last 8 quarters):** +/- 8.2%
- **Implied Earnings Move (from weekly options):** +/- 11.5%
- **Dividend Yield:** 0%
- **Borrow Cost:** 0.3%

## Trade Idea
Sell the earnings straddle — implied move (11.5%) is significantly higher than average historical move (8.2%). Vol is rich at 42% vs 28% realized.

## Options Data
- **ATM Call (14-day, $285 strike):** $12.80, delta 0.52, IV 42.5%
- **ATM Put (14-day, $285 strike):** $12.20, delta -0.48, IV 41.8%
- **Risk-Free Rate:** 4.8%

## Risk Parameters
- **Max Vega Exposure:** $50K per vol point
- **Max Gamma Exposure:** Keep delta within +/- $500K notional overnight
- **Theta Target:** Collect $15K/day minimum
- **Position Size:** $2M notional max

## Try It
```
/derivatives

Evaluating a short straddle ahead of earnings on a $285 cloud computing stock.
Earnings in 14 days. Implied vol 42% vs 28% realized. Implied earnings move
11.5% vs 8.2% historical average. ATM call $12.80 (42.5% IV), ATM put $12.20
(41.8% IV). Risk-free rate 4.8%. Want to sell vol but need to size it right —
max vega $50K per vol point, keep delta under $500K notional overnight. Price
the straddle and show me the Greeks and breakevens.
```
