# Market Making & Electronic Trading

```
You are a senior electronic market maker and quantitative trader with deep expertise
in market microstructure, order book dynamics, and high-frequency quoting strategies.
You have built and managed market-making systems across equities, options, futures,
and fixed income. You understand adverse selection, inventory risk, information
asymmetry, and the economics of providing liquidity. You are fluent in the academic
frameworks — Glosten-Milgrom, Kyle (1985), Avellaneda-Stoikov (2008) — and their
practical implementation. You think in terms of bid-ask spreads, fill rates, queue
priority, toxicity metrics, and inventory penalty functions. When analyzing a market-
making strategy, you provide specific quantitative metrics: expected P&L per trade,
Sharpe ratio, inventory half-life, adverse selection cost, and flow toxicity scores.
```

## What This Desk Does

The market-making desk provides continuous two-sided quotes (bids and offers) in financial instruments, earning the bid-ask spread while managing inventory risk. Market makers are essential to functioning markets: they absorb order flow imbalances, reduce transaction costs for end investors, and facilitate price discovery. Modern market making is almost entirely electronic, requiring sophisticated algorithms that adjust quotes in real time based on inventory position, volatility, order flow toxicity, and competitive dynamics. The desk's profitability depends on capturing spread more often than losing to informed flow, and on managing inventory efficiently to avoid large directional losses.

---

## 1. Bid-Ask Spread Analysis

**Components of the bid-ask spread (Roll decomposition):**
Spread = Order processing cost + Adverse selection cost + Inventory holding cost

**Glosten-Milgrom model (1985):**
The bid-ask spread arises from adverse selection. The market maker sets:
- Ask = E[V | buyer arrives] = V + (mu / (mu + epsilon)) * (V_H - V), where mu = probability of informed trader, epsilon = probability of uninformed, V_H = high value, V = expected value.
- Bid = E[V | seller arrives] = V - (mu / (mu + epsilon)) * (V - V_L)

The spread widens when: (1) the fraction of informed traders increases, (2) the information advantage is larger, (3) volatility is higher.

**Effective spread:**
Effective_spread = 2 * |trade_price - midpoint| * direction, where direction = +1 for buys, -1 for sells.

**Realized spread (measures adverse selection):**
Realized_spread = 2 * direction * (trade_price - midpoint_{t+delta}), evaluated at some horizon delta (e.g., 5 minutes). If realized spread < effective spread, the difference is adverse selection cost.

```
Analyze bid-ask spread dynamics for [INSTRUMENT]:

Market data:
- Instrument: [TICKER / CONTRACT]
- Current bid: [BID], ask: [ASK], mid: [MID]
- Quoted spread: [SPREAD] ([SPREAD_BPS] bps)
- Tick size: [TICK]
- Average daily volume: [ADV]
- Average trade size: [AVG_TRADE]
- Volatility (intraday, annualized): [VOL]%
- Number of market makers quoting: [NUM_MMs]
- Exchange fee structure: maker [MAKER_FEE], taker [TAKER_FEE]

Provide:
1. Spread decomposition: order processing, adverse selection, inventory components
2. Effective spread vs quoted spread (is liquidity better or worse than displayed?)
3. Realized spread at 1-min, 5-min, 30-min horizons (adverse selection measurement)
4. How does spread vary intraday? (wider at open, tighter midday, wider at close?)
5. Spread vs volatility relationship: what is the elasticity?
6. Competitive analysis: is there room for an additional market maker?
7. Optimal spread to quote given these market conditions (see Avellaneda-Stoikov below)
```

```
Evaluate the economics of making a market in [INSTRUMENT]:

- Expected trades per day: [TRADES]
- Average spread captured: [SPREAD_CAPTURED] bps
- Average adverse selection cost: [AS_COST] bps per trade
- Net edge per trade: [NET_EDGE] bps
- Average notional per trade: $[NOTIONAL]
- Inventory turnover: [TURNOVER]x per day
- Max inventory: [MAX_INV] units ($[MAX_INV_NOTIONAL])
- Capital allocated: $[CAPITAL]

Calculate:
1. Expected gross P&L per day: trades * notional * net edge
2. Inventory risk: VaR of max inventory position (1-day, 99%)
3. Sharpe ratio (annualized) of the market-making strategy
4. Return on capital (annualized)
5. Breakeven: minimum spread to cover costs (technology, exchange fees, risk capital)
6. Sensitivity: how does P&L change with +/- 20% in volume, +/- 2 vol points?
```

---

## 2. Inventory Management

**Avellaneda-Stoikov framework (2008):**
The market maker's reservation price shifts with inventory:
r(s, q, t) = s - q * gamma * sigma^2 * (T - t)

where s = mid price, q = inventory (positive = long), gamma = risk aversion, sigma = volatility, T = terminal time.

Optimal spread around the reservation price:
delta = gamma * sigma^2 * (T - t) + (2/gamma) * ln(1 + gamma/k)

where k = order arrival intensity parameter. The market maker quotes:
- bid = r - delta/2
- ask = r + delta/2

As inventory grows long, the reservation price drops (maker lowers bid and ask to attract selling), and vice versa. This is the **inventory skew**.

**Inventory half-life:** The expected time for inventory to mean-revert to zero through the market maker's quoting adjustments and hedging activity.

```
Design an inventory management framework for a market-making book:

Parameters:
- Instrument: [INSTRUMENT]
- Max inventory: +/- [MAX_Q] units
- Risk aversion (gamma): [GAMMA]
- Intraday volatility (sigma): [SIGMA]% annualized
- Order arrival rate: [LAMBDA] orders per second
- Average fill size: [FILL_SIZE] units
- Trading session length: [HOURS] hours
- End-of-day inventory target: [EOD_TARGET] units (usually 0)

Using the Avellaneda-Stoikov framework:
1. Calculate reservation price adjustment for inventory levels of -[MAX_Q], -[MAX_Q/2], 0, +[MAX_Q/2], +[MAX_Q]
2. Optimal spread width at each inventory level
3. Inventory penalty function: quadratic vs linear vs exponential — which fits best?
4. Expected inventory distribution throughout the trading day
5. Hedging rules: when to hedge via correlated instrument vs wait for mean reversion
6. End-of-day flattening strategy: ramp up skew in final [MINUTES] minutes
7. Circuit breakers: at what inventory level do we stop quoting one side entirely?
```

```
Analyze inventory risk for this market-making portfolio:

Current positions:
| Instrument  | Position (units) | Notional ($) | Avg cost | Mid price | P&L ($) |
|-------------|------------------|-------------|----------|-----------|---------|
| [INST_1]    | [Q1]             | [N1]        | [AC1]    | [MP1]     | [PL1]   |
| [INST_2]    | [Q2]             | [N2]        | [AC2]    | [MP2]     | [PL2]   |
| [INST_3]    | [Q3]             | [N3]        | [AC3]    | [MP3]     | [PL3]   |

Correlation matrix: [PROVIDE OR ESTIMATE]

Assess:
1. Portfolio VaR (1-day, 95% and 99%)
2. Gross and net inventory exposure (are positions offsetting?)
3. Concentration risk: is one instrument dominating the risk?
4. Inventory age: how long have positions been held? (aging inventory = stale risk)
5. Hedging recommendations: reduce which positions first? Use what instruments?
6. Inventory score: rate the portfolio's risk on a 1-10 scale with justification
```

---

## 3. Order Flow Analysis

**Kyle lambda (1985):**
Kyle's model shows that price impact is linear in order flow:
dp = lambda * dQ, where lambda = sigma_v / sigma_u

sigma_v = volatility of fundamental value, sigma_u = volatility of uninformed order flow.
Higher lambda = more price impact per unit of flow = less liquidity.

**VPIN (Volume-Synchronized Probability of Informed Trading):**
VPIN = |V_buy - V_sell| / (V_buy + V_sell), calculated over volume buckets.
High VPIN indicates elevated probability of informed trading (flow toxicity).

**Flow toxicity metrics:**
- Order flow imbalance (OFI): net signed volume over a window
- Trade arrival rate asymmetry: bursts of one-sided trades
- Large trade frequency: proportion of trades > X * average size
- Cancel-to-fill ratio: high ratio signals algorithmic probing or spoofing

```
Analyze order flow for [INSTRUMENT] over [PERIOD]:

Order flow data:
- Total volume: [TOTAL_VOL]
- Buy-initiated volume: [BUY_VOL] ([BUY_PCT]%)
- Sell-initiated volume: [SELL_VOL] ([SELL_PCT]%)
- Order flow imbalance (OFI): [OFI]
- Number of trades: [NUM_TRADES]
- Average trade size: [AVG_SIZE]
- Large trade (>[THRESHOLD]) count: [LARGE_TRADES] ([LARGE_PCT]%)
- VPIN estimate: [VPIN]
- Cancel-to-fill ratio: [CTF]
- Price change over period: [PRICE_CHANGE]

Evaluate:
1. Kyle lambda estimate: price impact per unit of net flow
2. Flow toxicity assessment: is flow predominantly informed or uninformed?
3. VPIN interpretation: is informed trading probability elevated vs baseline?
4. Toxic flow identification: time windows with anomalous flow patterns
5. Internalization opportunity: which flow is safe to internalize vs externalize?
6. Price improvement analysis: should we offer price improvement to attract uninformed flow?
7. Signal: does the order flow predict near-term price direction?
```

```
Build a flow segmentation model for a market-making desk:

Flow types to classify:
1. Institutional (large, low frequency, often informed)
2. Retail (small, high frequency, usually uninformed, PFOF eligible)
3. Algorithmic/HFT (medium, very high frequency, mixed information content)
4. Index/ETF rebalance (predictable, concentrated, deadline-driven)
5. Market maker hedging (correlated with derivatives activity)

For each flow type, determine:
- Expected adverse selection cost (bps)
- Optimal spread to quote
- Internalization attractiveness (profit from internalizing vs routing to exchange)
- Price improvement to offer (bps) to attract flow
- Position in queue priority: does this flow type benefit from maker-taker vs inverted venue?
```

---

## 4. Market Microstructure

**Order book dynamics:**
- **Queue priority:** Price-time priority is standard (best price first, then earliest order at that price). Some venues use size-time or pro-rata.
- **Depth:** Sum of resting limit orders at each price level. Shallow depth = higher price impact.
- **Order book imbalance (OBI):** (Bid_depth - Ask_depth) / (Bid_depth + Ask_depth). Positive OBI predicts short-term price increase.

**Latency arbitrage:**
Faster participants observe price changes on one venue and trade on stale quotes at another venue before the market maker can update. This is a significant source of adverse selection for market makers.

Cost of latency = Probability(stale quote) * Expected_loss_per_stale_fill.

**Maker-taker vs inverted fee models:**
- Maker-taker: exchange pays rebate to liquidity providers, charges fee to takers. Encourages resting orders.
- Inverted: exchange pays takers, charges makers. Encourages aggressive orders, attracts retail flow.

```
Analyze market microstructure for [INSTRUMENT] across venues:

Venue data:
| Venue      | Market share | Avg spread | Depth at BBO | Maker fee | Taker fee | Latency (us) |
|------------|-------------|------------|--------------|-----------|-----------|--------------|
| [VENUE_1]  | [MS1]%      | [SP1]      | [DEP1]       | [MF1]     | [TF1]     | [LAT1]       |
| [VENUE_2]  | [MS2]%      | [SP2]      | [DEP2]       | [MF2]     | [TF2]     | [LAT2]       |
| [VENUE_3]  | [MS3]%      | [SP3]      | [DEP3]       | [MF3]     | [TF3]     | [LAT3]       |
| Dark pool  | [MS4]%      | midpoint   | hidden       | [MF4]     | [TF4]     | n/a          |

Evaluate:
1. Optimal venue routing: where to post resting orders vs where to take liquidity
2. Queue position analysis: expected time to fill at each venue given depth
3. Latency arbitrage risk: which venues are most susceptible to stale-quote picking?
4. Dark pool usage: when is midpoint execution valuable vs risky?
5. Fee optimization: net cost of execution across maker-taker and inverted venues
6. Fragmentation impact: is the multi-venue landscape helping or hurting liquidity?
```

---

## 5. Electronic Market Making

**Quoting algorithm design:**
The quoting engine must continuously decide: (1) at what prices to quote, (2) how much size, and (3) on which venues.

**Key parameters:**
- **Skew:** Shift quotes in the direction that reduces inventory. Long inventory -> lower bid and ask relative to mid.
- **Width:** Spread between bid and ask. Wider in volatile or toxic-flow conditions.
- **Size:** Quantity displayed. Reduce in volatile markets or when inventory is elevated.
- **Layering:** Quotes at multiple price levels for partial fills and depth.

**Fill rate vs adverse selection tradeoff:**
Tighter spreads -> higher fill rate -> more adverse selection exposure.
Wider spreads -> lower fill rate -> less adverse selection but lower gross revenue.

**Inventory penalty function (from Avellaneda-Stoikov):**
Penalty = gamma * q^2 * sigma^2 * (T - t) / 2. This term enters the market maker's value function and drives the inventory skew.

```
Design a quoting algorithm for [INSTRUMENT]:

Market parameters:
- Tick size: [TICK]
- Average spread: [AVG_SPREAD] ticks
- Intraday volatility: [VOL]%
- Average daily volume: [ADV]
- Order arrival rate: [LAMBDA] per second (per side)
- Fill probability at 1 tick wide: [FILL_1]%
- Fill probability at 2 ticks wide: [FILL_2]%
- Adverse selection at 1 tick: [AS_1] bps
- Adverse selection at 2 ticks: [AS_2] bps

Design the algorithm to specify:
1. Base spread as a function of volatility regime (low/normal/high vol)
2. Inventory skew function: how much to shift quotes per unit of inventory
3. Size management: displayed quantity vs total quantity, iceberg logic
4. Venue allocation: which venues get quotes, priority order
5. Speed bump response: how to handle fill notification latency
6. Regime detection: triggers to widen spread (news, volume spike, correlation break)
7. End-of-day protocol: flattening ramp, spread widening schedule
```

```
Backtest and optimize a market-making strategy:

Strategy parameters to test:
- Spread: [SPREAD_MIN] to [SPREAD_MAX] ticks (step [STEP])
- Inventory limit: [INV_MIN] to [INV_MAX] units
- Skew coefficient: [SKEW_MIN] to [SKEW_MAX]
- Hedge ratio: [0% / 25% / 50% / 75% / 100%] of inventory via [HEDGE_INSTRUMENT]

Historical data:
- Period: [START_DATE] to [END_DATE]
- Instrument: [INSTRUMENT]
- Data granularity: [TICK / 1SEC / 1MIN]

For each parameter combination, calculate:
1. Total P&L (gross and net of fees)
2. Sharpe ratio (annualized)
3. Maximum drawdown
4. Average inventory level and max inventory
5. Fill rate (% of quotes that resulted in trades)
6. Adverse selection per fill (realized spread at 1-min, 5-min)
7. P&L per trade and P&L per unit of risk

Identify the Pareto-optimal parameter sets (best P&L for given max drawdown).
Highlight sensitivity: which parameter has the largest impact on P&L?
```

---

## Mathematical Framework Summary

**Glosten-Milgrom (1985):** Explains the bid-ask spread as compensation for adverse selection. The spread is proportional to the probability of facing an informed trader and the magnitude of the information advantage.

**Kyle (1985):** Models strategic informed trading. Price impact (lambda) is determined by the ratio of information volatility to noise trading volatility. A single informed trader submits orders gradually to camouflage among noise traders.

**Avellaneda-Stoikov (2008):** Provides an optimal market-making framework under inventory risk. The reservation price adjusts linearly with inventory, and the optimal spread depends on risk aversion, volatility, and time horizon. This is the workhorse model for practical market-making algorithm design.

**Key relationships:**
- Glosten-Milgrom: spread = f(informed trader probability, information size)
- Kyle: lambda = sigma_v / sigma_u (price impact coefficient)
- Avellaneda-Stoikov: ask - bid = gamma * sigma^2 * (T-t) + (2/gamma) * ln(1 + gamma/k)

---

## See Also

- [equities.md](equities.md) -- for equity execution and algorithmic trading
- [derivatives.md](derivatives.md) -- for options market-making specifics (delta hedging, vol quoting)
- [fixed-income.md](fixed-income.md) -- for bond market-making (dealer inventory, run-the-book)
- [commodities.md](commodities.md) -- for futures market-making and spread quoting
