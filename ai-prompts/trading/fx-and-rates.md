# FX & Interest Rate Markets

```
You are a senior FX and rates trader at a global macro hedge fund with prior
experience at a G-SIB dealer. You have deep expertise in spot FX, forwards, FX
options, interest rate swaps, cross-currency basis swaps, and central bank policy
analysis. You understand covered and uncovered interest rate parity, carry trade
mechanics, real effective exchange rate models, and the plumbing of global funding
markets. You think in terms of forward points, swap spreads, basis, and the
interplay between monetary policy divergence, capital flows, and risk sentiment.
When analyzing trades, you provide specific levels, carry calculations, breakeven
analysis, and risk scenarios grounded in actual market conventions (ACT/360, T+2
settlement, ISDA fixings).
```

## What This Desk Does

The FX and rates desk trades currencies and interest rate instruments across developed and emerging markets. FX traders manage spot, forward, and options books, expressing views on monetary policy divergence, trade flows, and risk appetite. Rates traders construct swap and basis swap positions to capture yield curve views and funding dislocations. The desk sits at the intersection of macro analysis and market microstructure, requiring fluency in central bank communication, balance of payments data, and the mechanics of global dollar funding. Positions often span multiple instruments: a single trade idea might involve spot FX, an interest rate swap, and an FX option simultaneously.

---

## 1. FX Spot and Forward Analysis

**Covered interest rate parity (CIP):**
F/S = (1 + r_d * T) / (1 + r_f * T), where F = forward rate, S = spot rate, r_d = domestic rate, r_f = foreign rate, T = time in years.

Forward points = F - S. Positive forward points mean domestic currency trades at a premium (lower domestic rate).

**Uncovered interest rate parity (UIP):**
E[S_T]/S = (1 + r_d) / (1 + r_f). UIP predicts high-yield currencies depreciate. Empirically, UIP fails over short horizons (the "forward premium puzzle"), which is why carry trades work.

**Real Effective Exchange Rate (REER):**
REER = trade-weighted nominal exchange rate adjusted for relative CPI differentials. Deviation from long-run average signals over/undervaluation.

```
Analyze this FX pair for a directional trade:

- Currency pair: [CCY1/CCY2]
- Spot rate: [SPOT]
- 3M forward: [FWD_3M] (forward points: [FWD_PTS])
- 1Y forward: [FWD_1Y]
- [CCY1] policy rate: [RATE_1]%
- [CCY2] policy rate: [RATE_2]%
- Rate differential: [DIFF] bps
- REER percentile (10Y): [REER_PCTL]%
- Current account balance ([CCY1] country): [CA]% of GDP
- Positioning (IMM/CFTC): [NET_LONG/NET_SHORT] [SIZE] contracts

Provide:
1. Carry analysis: annualized carry in bps from going [LONG/SHORT] [CCY1/CCY2]
2. Forward rate vs spot: is the forward pricing in enough depreciation?
3. REER valuation: how far from fair value? Mean-reversion signal?
4. Flow analysis: current account, capital account, FDI, portfolio flows
5. Central bank divergence trajectory over next 6-12 months
6. Technical levels: key support/resistance, recent range, breakout risk
7. Risk scenarios: risk-on vs risk-off, commodity shock, EM contagion
```

```
Construct a carry trade portfolio:

Target currencies (long, high yield): [CCY_1], [CCY_2], [CCY_3]
Funding currencies (short, low yield): [CCY_A], [CCY_B]

For each pair:
- Spot rate, 3M forward points, annualized carry (bps)
- Sharpe ratio of carry strategy (historical 3Y)
- Drawdown in last 3 major risk-off episodes
- Vol-adjusted position sizing to equalize risk across pairs

Portfolio-level:
1. Total expected carry (annualized)
2. Correlation matrix of carry pairs
3. Maximum historical portfolio drawdown
4. Suggested hedges: long vol overlay, risk-off trigger for position reduction
5. Breakeven exchange rate move that eliminates carry over 3M horizon
```

---

## 2. Interest Rate Swap Pricing

**Plain vanilla IRS:** Exchange fixed rate for floating rate (SOFR, EURIBOR, etc.) on a notional amount.

**Swap rate determination:**
Fixed rate is set so that PV(fixed leg) = PV(floating leg) at inception.
PV(fixed) = C * sum_t [ delta_t * DF_t ], where C = fixed coupon, delta_t = day count fraction, DF_t = discount factor.
PV(float) = sum_t [ f_t * delta_t * DF_t ], where f_t = forward rate for period t.

**DV01 of a swap:** DV01 approx= Notional * ModDur_annuity / 10,000. For a par swap, DV01 per $1M notional is approximately equal to the sum of discount factors divided by 10,000.

**Swap spread:** Swap_rate - Treasury_yield of same maturity. Reflects bank credit risk, supply/demand for fixed-rate paying, and balance sheet constraints.

**CVA/DVA:**
CVA = Expected loss from counterparty default. CVA = LGD * integral_0^T EE(t) * dPD(t), where EE = expected exposure, PD = probability of default. DVA is the mirror image (own default).

```
Price and analyze this interest rate swap:

- Notional: $[NOTIONAL]M
- Tenor: [TENOR] years
- Fixed rate (mid): [FIXED_RATE]%
- Floating index: [SOFR / EURIBOR / SONIA / TONAR]
- Current floating rate: [FLOAT_RATE]%
- Pay frequency (fixed): [SEMI / ANNUAL / QUARTERLY]
- Pay frequency (float): [QUARTERLY / SEMI / ANNUAL]
- Day count (fixed): [30_360 / ACT_360 / ACT_365]
- Day count (float): [ACT_360 / ACT_365]
- Direction: [PAY_FIXED / RECEIVE_FIXED]

Calculate:
1. DV01 of each leg and net DV01
2. Current mark-to-market (if off-market, at rate [OFF_MARKET_RATE]%)
3. Carry: what do you earn/pay over the next quarter assuming rates unchanged?
4. Roll-down: value change from the passage of time (moving down the forward curve)
5. Breakeven rate: where does the floating rate need to average for the swap to break even?
6. Swap spread vs Treasury: current level, historical percentile, and drivers
7. CVA charge estimate given counterparty rating [RATING] and netting set exposure
```

---

## 3. FX Options

**Garman-Kohlhagen model (Black-Scholes for FX):**
C = S * e^(-r_f * T) * N(d1) - K * e^(-r_d * T) * N(d2)

d1 = [ln(S/K) + (r_d - r_f + sigma^2/2) * T] / (sigma * sqrt(T))
d2 = d1 - sigma * sqrt(T)

**FX vol surface conventions:**
- Quoted in delta space: 10-delta put, 25-delta put, ATM (delta-neutral straddle), 25-delta call, 10-delta call
- **Risk reversal (RR):** 25d call vol - 25d put vol. Positive RR = calls bid over puts (bullish skew).
- **Butterfly (BF):** 0.5 * (25d call vol + 25d put vol) - ATM vol. Positive BF = wings bid over ATM (fat tails).
- **ATM convention:** usually delta-neutral straddle (DNS), where the straddle delta = 0.

```
Analyze the FX options surface for [CCY1/CCY2]:

Spot: [SPOT], Forward ([TENOR]): [FWD]

Volatility surface:
| Tenor | ATM  | 25d RR | 25d BF | 10d RR | 10d BF |
|-------|------|--------|--------|--------|--------|
| 1W    | [V1] | [RR1]  | [BF1]  | [RR1b] | [BF1b] |
| 1M    | [V2] | [RR2]  | [BF2]  | [RR2b] | [BF2b] |
| 3M    | [V3] | [RR3]  | [BF3]  | [RR3b] | [BF3b] |
| 6M    | [V4] | [RR4]  | [BF4]  | [RR4b] | [BF4b] |
| 1Y    | [V5] | [RR5]  | [BF5]  | [RR5b] | [BF5b] |

Provide:
1. Vol term structure: contango/backwardation? Event-driven kinks?
2. Skew interpretation: what does the risk reversal tell us about market positioning?
3. Butterfly interpretation: are tails priced richly? Is jump risk elevated?
4. Historical comparison: current ATM vol vs realized vol (1M, 3M, 1Y)
5. Strategy recommendations:
   a. If view is [CCY1] appreciates: buy risk reversal? Buy call spread?
   b. If view is range-bound: sell straddle? Sell strangle? Iron condor?
   c. If hedging: optimal strike and tenor for a corporate hedger
6. Vega and gamma exposure for each strategy
```

```
Price a structured FX hedge for a corporate client:

- Exposure: [CCY1] [RECEIVABLE/PAYABLE] of [AMOUNT] in [MONTHS] months
- Current spot: [SPOT]
- Forward rate: [FWD]
- Budget rate: [BUDGET_RATE]
- Hedge ratio desired: [PCT]%

Compare these structures:
1. Forward contract: lock in [FWD], no optionality, no premium
2. Vanilla put (or call): strike [STRIKE], premium [PREMIUM_PCT]% of notional
3. Zero-cost collar: buy [PUT/CALL] at [K1], sell [CALL/PUT] at [K2]
4. Participating forward: 50/100 or other ratio, zero premium
5. Knock-in/knock-out structure: barrier at [BARRIER], reduced premium

For each, show: all-in worst-case rate, best-case rate, premium cost, accounting
treatment (hedge effectiveness under IFRS 9 / ASC 815), and breakeven vs forward.
```

---

## 4. Cross-Currency Basis

**Cross-currency basis swap:** Exchange floating rates in two currencies, with exchange of notional at inception and maturity. The basis (quoted in bps) is added to the non-USD leg.

A negative XCCY basis for EUR/USD means that EUR EURIBOR payers receive less than fair value, implying USD funding is scarce (or EUR is being dumped to borrow USD).

**Drivers of basis:** USD funding demand from non-US banks, central bank swap lines, quarter/year-end balance sheet constraints, hedging demand from real money (Japanese lifers, European insurers).

```
Analyze cross-currency basis dynamics for [CCY1/CCY2]:

Current basis term structure:
| Tenor | Basis (bps) | 3M ago | 1Y ago | 5Y avg |
|-------|-------------|--------|--------|--------|
| 3M    | [B_3M]      | [H3_3] | [H3_1Y]| [H3_5Y]|
| 1Y    | [B_1Y]      | [H1_3] | [H1_1Y]| [H1_5Y]|
| 5Y    | [B_5Y]      | [H5_3] | [H5_1Y]| [H5_5Y]|
| 10Y   | [B_10Y]     | [H10_3]| [H10_1]| [H10_5]|

Assess:
1. Current level vs historical: is basis wide (USD shortage) or tight?
2. Key drivers: bank balance sheet, central bank swap line usage, hedging flows
3. Quarter-end/year-end seasonality patterns
4. Impact on foreign investors hedging US asset purchases (all-in hedged yield)
5. Trading opportunity: is basis mean-reverting? Entry/exit levels.
6. Position construction: receive [CCY1] + pay [CCY2] via XCCY basis swap
```

---

## 5. Central Bank Analysis

```
Analyze central bank policy expectations for [CENTRAL_BANK]:

Current policy rate: [RATE]%
Market-implied path (from OIS/Fed Funds futures):
| Meeting date | Implied rate | Change from prior | Probability of hike/cut |
|--------------|-------------|-------------------|------------------------|
| [DATE_1]     | [R1]%       | [CHG_1] bps       | [PROB_1]%              |
| [DATE_2]     | [R2]%       | [CHG_2] bps       | [PROB_2]%              |
| [DATE_3]     | [R3]%       | [CHG_3] bps       | [PROB_3]%              |
| [DATE_4]     | [R4]%       | [CHG_4] bps       | [PROB_4]%              |

Recent communication:
- Last statement key language: [SUMMARY]
- Dot plot median (if Fed): [DOT_MEDIAN]% for [YEAR]
- Key data since last meeting: [CPI / NFP / GDP / PMI]

Provide:
1. Is the market pricing too many or too few cuts/hikes relative to the macro data?
2. Reaction function: what data would cause the central bank to deviate from guidance?
3. Trade expression: how to position for your view on rates
   a. Front-end: SOFR futures, Fed Funds futures, or Euribor futures
   b. Curve: steepener or flattener to express earlier/later cycle view
   c. FX: which currency pairs are most sensitive to this central bank?
4. Historical precedents: similar macro setups and how the central bank responded
5. QE/QT considerations: impact on term premium and curve shape
6. Risk scenarios: hawkish surprise, dovish surprise, emergency action
```

```
Evaluate the impact of [CENTRAL_BANK] balance sheet policy:

- Current balance sheet size: $[SIZE]T
- Monthly pace of QE/QT: $[PACE]B
- Composition: [GOVT_BONDS]% government bonds, [MBS]% MBS, [OTHER]% other
- Estimated neutral balance sheet: $[NEUTRAL]T
- Reserves: $[RESERVES]T (ample / adequate / scarce threshold: $[THRESHOLD]T)

Analyze:
1. Term premium impact: how many bps has QE/QT added/removed from 10Y yields?
2. Liquidity conditions: is reserve scarcity emerging? Money market stress signals?
3. When will the central bank need to slow/stop QT? (repo facility usage, T-bill issuance)
4. Impact on swap spreads: how does balance sheet shrinkage affect supply/demand
5. Portfolio rebalancing channel: flow from government bonds into credit, equities
```

---

## See Also

- [fixed-income.md](fixed-income.md) -- for bond trading and yield curve strategies
- [derivatives.md](derivatives.md) -- for options pricing framework (adapted via Garman-Kohlhagen for FX)
- [commodities.md](commodities.md) -- for commodity currencies and macro linkages
- [equities.md](equities.md) -- for equity impact of rate/FX moves
