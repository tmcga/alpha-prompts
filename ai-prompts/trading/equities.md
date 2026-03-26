# Cash Equities Trading

```
You are a senior cash equities trader at a bulge-bracket investment bank. You have
15+ years of experience executing large institutional orders across US and European
equity markets. You understand market microstructure, liquidity dynamics, and the
interplay between fundamental flows and technical positioning. You think in terms of
market impact, timing risk, and information leakage. You are fluent in algorithmic
execution strategies, program trading mechanics, and short-selling constraints. When
analyzing trades, you provide specific numbers, relevant benchmarks, and actionable
recommendations grounded in real market conventions.
```

## What This Desk Does

The cash equities desk executes buy and sell orders in listed stocks for institutional clients and the firm's proprietary accounts. The desk manages single-stock risk, handles large block trades with minimal market impact, and runs program trades involving hundreds of names simultaneously. Traders on this desk must balance speed of execution against price slippage, navigate fragmented liquidity across exchanges and dark pools, and maintain awareness of index rebalance flows, sector rotation trends, and short-interest dynamics that drive order flow and positioning.

---

## 1. Block Trade Analysis

Block trades involve large orders (typically >10,000 shares or >$200,000 notional) that require careful execution to minimize market impact and information leakage.

**Key metrics:** Discount to VWAP, market impact cost (bps), timing risk, participation rate, block liquidity score.

**Market impact model (square-root model):**
Impact (bps) = sigma * sqrt(Q / V) * eta, where sigma = daily volatility, Q = order size, V = average daily volume, eta = market impact coefficient (typically 0.5-1.5).

```
Analyze this block trade for execution feasibility:

- Stock: [TICKER]
- Order side: [BUY/SELL]
- Order size: [SHARES] shares ([X]% of ADV)
- Current price: $[PRICE]
- 20-day ADV: [ADV] shares
- 30-day realized volatility: [VOL]%
- Spread: [BID] / [ASK]
- Upcoming catalysts: [EARNINGS_DATE / INDEX_REBAL / OTHER]

Provide:
1. Estimated market impact in basis points using the square-root model
2. Optimal execution window (time of day, number of days)
3. Recommended participation rate
4. Risk of information leakage and adverse selection
5. Suggested discount/premium to VWAP for a risk bid/offer
6. Comparison: risk trade vs agency execution vs dark pool sourcing
```

```
A client wants to sell a [SHARES]-share block of [TICKER] (approximately [X]% of
ADV). The stock has declined [Y]% over the past [N] days on [CATALYST]. Short
interest is [SI]% of float, and the borrow rate is [BORROW]%.

Evaluate:
1. Is the selling pressure already reflected in current price?
2. What discount to last sale / VWAP should we bid?
3. What is our expected P&L range if we take the block as principal?
4. Hedging strategy: correlated single names, sector ETF, or index futures?
5. Unwind timeline and expected slippage
```

---

## 2. Program Trading

Program trading involves executing baskets of stocks simultaneously, often tied to index rebalances, portfolio transitions, or quantitative strategies.

**Key metrics:** Tracking error, implementation shortfall, beta exposure, sector tilt, cash residual, turnover cost.

**Tracking error formula:**
TE = sqrt(sum_i (w_i_portfolio - w_i_benchmark)^2 * sigma_i^2 + 2 * sum_i sum_j (w_i - w_i_b)(w_j - w_j_b) * rho_ij * sigma_i * sigma_j)

```
Construct a program trade for the following portfolio transition:

- Outgoing portfolio: [DESCRIPTION / TICKER LIST]
- Target portfolio: [DESCRIPTION / BENCHMARK / TICKER LIST]
- Total AUM: $[AUM]
- Maximum tracking error budget: [TE_BPS] bps annualized
- Transition timeline: [DAYS] trading days
- Constraints: [SECTOR_LIMITS / SINGLE_NAME_LIMITS / TAX_LOT_RESTRICTIONS]

Provide:
1. Optimal crossing strategy (internal cross, external cross, open market)
2. Expected transition cost breakdown (commissions, spread, impact, opportunity)
3. Sequencing: which legs to execute first to minimize interim risk
4. Cash management during the transition (temporary cash equitization via futures)
5. Tracking error profile day-by-day during the transition
```

```
The [INDEX_NAME] is rebalancing on [DATE]. The following changes are expected:

- Additions: [TICKER_LIST_ADD]
- Deletions: [TICKER_LIST_DEL]
- Weight changes: [SIGNIFICANT_REWEIGHTS]

Total estimated flow: $[FLOW]B one-way.

Analyze:
1. Historical price pattern for additions/deletions around rebalance dates
2. Expected demand/supply imbalance for each name
3. Pre-positioning strategy: when to start building/reducing positions
4. MOC (Market on Close) imbalance expectations on rebalance day
5. Risk of front-running by other participants and how to mitigate
```

---

## 3. Sector Rotation Analysis

Sector rotation tracks capital flows between equity sectors based on macroeconomic regime, relative valuation, and momentum signals.

**Key metrics:** Relative performance (sector vs index), factor attribution (value/growth/momentum/quality), fund flow data, relative P/E, earnings revision breadth.

```
Analyze the current sector rotation dynamics in [MARKET / INDEX]:

- Time period: [START_DATE] to [END_DATE]
- Macro regime: [EXPANSION / LATE_CYCLE / RECESSION / RECOVERY]
- Recent Fed/ECB action: [RATE_DECISION / GUIDANCE]
- Key data releases: [NFP / CPI / PMI / EARNINGS_SEASON]

Provide:
1. Sector relative performance rankings (1M, 3M, YTD)
2. Fund flow data: which sectors are seeing inflows/outflows
3. Factor decomposition: how much of sector moves are beta, value, growth, momentum
4. Historical sector playbook for this stage of the economic cycle
5. Contrarian opportunities: sectors with negative sentiment but improving fundamentals
6. Recommended overweight/underweight tilts with conviction levels
```

---

## 4. Short Selling

Short selling requires locating borrowable shares, managing borrow costs, and monitoring squeeze risk from rising utilization and buy-in potential.

**Key metrics:** Short interest (% of float), utilization rate, cost to borrow (CTB), days to cover, buy-in risk, fee rebate.

**Cost of carry for short position:**
Net carry = -CTB (annualized) + short rebate rate - dividend yield (if applicable)

```
Evaluate the short-selling dynamics for [TICKER]:

- Current short interest: [SI_SHARES] shares ([SI_PCT]% of float)
- Utilization: [UTIL]%
- Cost to borrow: [CTB]% (GC / warm / hot / special)
- Days to cover: [DTC]
- Recent short interest trend: [INCREASING / DECREASING / STABLE]
- Upcoming catalysts: [EARNINGS / LOCKUP_EXPIRY / SECONDARY / OTHER]
- Retail ownership concentration: [HIGH / MODERATE / LOW]

Assess:
1. Squeeze risk score (1-10) with key drivers
2. Expected borrow cost trajectory over the next 30/60/90 days
3. Recall risk and buy-in probability
4. Optimal short entry timing relative to catalysts
5. Hedging the short via puts or put spreads (cost comparison)
6. Regulatory considerations (Reg SHO threshold list, uptick rule applicability)
```

```
A client wants to initiate a [LONG_TICKER] / [SHORT_TICKER] pairs trade:

- Long leg: [SHARES_LONG] shares of [LONG_TICKER] at $[PRICE_LONG]
- Short leg: [SHARES_SHORT] shares of [SHORT_TICKER] at $[PRICE_SHORT]
- Beta-adjusted ratio: [RATIO]
- Historical spread: mean [MEAN], current [CURRENT], z-score [ZSCORE]
- Correlation (1Y): [CORR]

Provide:
1. Locate availability and borrow cost for the short leg
2. Expected carry (positive or negative) for the combined position
3. Spread convergence probability based on historical distribution
4. Maximum drawdown scenarios and suggested stop-loss levels
5. Sector/factor residual exposures after the pair is constructed
```

---

## 5. Algorithmic Execution

Algorithmic execution strategies minimize market impact by slicing large orders over time according to volume patterns, price benchmarks, or urgency parameters.

**Common algorithms:**
- **TWAP** (Time-Weighted Average Price): uniform distribution over time window
- **VWAP** (Volume-Weighted Average Price): follows historical intraday volume curve
- **IS** (Implementation Shortfall / Arrival Price): front-loads execution to minimize timing risk
- **POV** (Percentage of Volume): participates at a fixed rate of real-time volume

**Implementation shortfall decomposition:**
IS = (execution price - decision price) / decision price
IS = delay cost + market impact cost + timing cost + opportunity cost

```
Recommend an execution algorithm for the following order:

- Stock: [TICKER]
- Side: [BUY/SELL]
- Order size: [SHARES] shares ($[NOTIONAL] notional)
- % of ADV: [PCT_ADV]%
- Urgency: [LOW / MEDIUM / HIGH / URGENT]
- Benchmark: [VWAP / ARRIVAL / CLOSE / TWAP]
- Market conditions: [NORMAL / VOLATILE / EARNINGS_DAY / LOW_LIQUIDITY]
- Alpha signal decay: [FAST / MEDIUM / SLOW / NONE]
- Dark pool preference: [YES / NO / INDIFFERENT]

Provide:
1. Recommended algorithm (TWAP / VWAP / IS / POV / Iceberg / other)
2. Participation rate and expected completion time
3. Estimated market impact (bps) and total execution cost
4. Venue routing strategy (lit exchanges, dark pools, midpoint pegs)
5. Aggressive vs passive limit order mix
6. Real-time adjustment triggers (if stock moves X%, if volume spikes, etc.)
```

```
Compare execution quality for these completed algorithmic orders:

| Order | Algo | Ticker | Side | Shares | Benchmark | Result (bps) |
|-------|------|--------|------|--------|-----------|---------------|
| 1     | [A1] | [T1]   | [S1] | [SH1]  | [B1]      | [R1]          |
| 2     | [A2] | [T2]   | [S2] | [SH2]  | [B2]      | [R2]          |
| 3     | [A3] | [T3]   | [S3] | [SH3]  | [B3]      | [R3]          |

For each order, decompose the implementation shortfall into:
1. Delay cost
2. Market impact cost
3. Timing cost
4. Opportunity cost (for partially filled orders)
Identify which algo settings should be adjusted for future similar orders.
```

---

## See Also

- [derivatives.md](derivatives.md) -- for equity options and volatility strategies
- [market-making.md](market-making.md) -- for equity market-making and microstructure
- [fixed-income.md](fixed-income.md) -- for convertible bond arbitrage (equity + credit)
