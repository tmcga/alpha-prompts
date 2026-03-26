# Trading & Execution: Block Trade in Mid-Cap Pharma

## Order Details
- **Asset Class:** US equities
- **Stock:** MedGenix Corp (fictional), mid-cap pharma
- **Side:** Sell
- **Shares:** 2.5M shares
- **Current Price:** $38.40
- **Notional:** ~$96M
- **ADV (20-day):** 1.8M shares/day
- **Order Size:** 1.4x ADV (large block)

## Market Context
- **Volatility:** Stock has 45% annualized vol (recent FDA catalyst)
- **Spread:** $0.08 typical (21bps)
- **Urgency:** Moderate — fund rebalancing, not information-driven
- **Time Constraint:** Complete within 2 trading days

## Execution Parameters
- **Benchmark:** VWAP over execution window
- **Market Impact Limit:** 50bps max
- **Strategy Preference:** Algorithmic — minimize information leakage
- **Constraints:** No crossing in dark pools (compliance restriction), no more than 15% of volume in any 30-minute bucket
- **Broker:** Goldman Sachs electronic trading desk

## Try It
```
/trade

Need to sell 2.5M shares of MedGenix ($38.40, mid-cap pharma). That's 1.4x
ADV. Stock has 45% annualized vol. Moderate urgency — fund rebalancing, not
information-driven. Need to complete in 2 days. Benchmark is VWAP. Max market
impact 50bps. No dark pools (compliance). What's the optimal execution strategy?
```
