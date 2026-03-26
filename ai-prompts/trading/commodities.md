# Commodity Trading

```
You are a senior commodity trader and analyst with expertise spanning energy, metals,
and agricultural markets. You have experience trading physical commodities and
financial derivatives (futures, options, swaps) across major exchanges (CME/NYMEX,
ICE, LME, CBOT). You understand the fundamental drivers of each commodity complex:
supply/demand balances, inventory dynamics, weather, geopolitics, and logistics. You
think in terms of futures curves (contango vs backwardation), roll yield, convenience
yield, storage economics, and basis between physical and derivatives. You can analyze
crack spreads, crush spreads, spark spreads, and cross-commodity relative value. You
understand the distinction between financial and physical trading, including delivery
mechanics, tank farm economics, and pipeline constraints.
```

## What This Desk Does

The commodity desk trades futures, options, swaps, and physical contracts across energy (crude oil, natural gas, refined products, power), metals (gold, silver, copper, aluminum, nickel), and agricultural products (corn, wheat, soybeans, sugar, coffee). Traders manage curve positions, express relative value views through spread trades, and serve as intermediaries between physical producers/consumers and financial markets. Fundamental analysis of supply chains, inventories, weather, and geopolitics is as important as technical and quantitative analysis. The desk requires understanding of physical delivery logistics, storage economics, and the regulatory landscape (CFTC position limits, speculative vs commercial hedger classification).

---

## 1. Futures Curve Analysis

**Key concepts:**
- **Contango:** futures price > spot price. Driven by storage costs, insurance, financing. Encourages inventory accumulation.
- **Backwardation:** spot price > futures price. Signals tight supply, strong near-term demand. Encourages inventory drawdowns.
- **Convenience yield:** non-monetary return from holding physical inventory (supply security, ability to meet unexpected demand). y = r + u - (F/S - 1)/T, where r = risk-free rate, u = storage cost.
- **Roll yield:** return from rolling a futures position forward. Positive in backwardation (selling high near-month, buying low far-month), negative in contango.
- **Calendar spread:** Long front month, short back month (or vice versa), expressing a view on curve shape.

**Cost of carry model:**
F = S * e^((r + u - y) * T), where r = risk-free rate, u = storage cost rate, y = convenience yield, T = time to maturity.

```
Analyze the futures curve for [COMMODITY]:

Spot / front month: $[SPOT]
Curve:
| Contract | Expiry     | Price  | Spread to front |
|----------|------------|--------|-----------------|
| [M1]     | [DATE_1]   | [P1]   | --              |
| [M2]     | [DATE_2]   | [P2]   | [SP_2]          |
| [M3]     | [DATE_3]   | [P3]   | [SP_3]          |
| [M6]     | [DATE_6]   | [P6]   | [SP_6]          |
| [M12]    | [DATE_12]  | [P12]  | [SP_12]         |
| [M24]    | [DATE_24]  | [P24]  | [SP_24]         |

- Current inventory: [INVENTORY] (vs 5Y avg: [INV_5Y_AVG])
- Days of supply: [DAYS_SUPPLY]
- Production: [PROD] (trend: [UP/DOWN/FLAT])
- Demand: [DEMAND] (trend: [UP/DOWN/FLAT])

Provide:
1. Curve shape characterization: contango, backwardation, or mixed
2. Implied convenience yield and storage cost decomposition
3. Roll yield: expected return from rolling a long position over 3M, 6M, 12M
4. Historical percentile of current curve shape (1Y, 3Y, 5Y)
5. Fundamental drivers: what is the curve "telling us" about supply/demand
6. Calendar spread trade: which spread offers best risk/reward? Entry, target, stop.
```

```
Evaluate a cash-and-carry arbitrage opportunity:

- Commodity: [COMMODITY]
- Spot price: $[SPOT] per [UNIT]
- 6-month futures: $[FUTURES_6M] per [UNIT]
- Annualized implied roll: [ROLL]%
- Storage cost: $[STORAGE] per [UNIT] per month
- Financing rate: [FIN_RATE]%
- Insurance/deterioration: $[INS] per [UNIT] per month
- Transport to delivery point: $[TRANSPORT] per [UNIT]

Calculate:
1. Full cost of carry: financing + storage + insurance + transport
2. Implied profit/loss: futures price - spot - full carry cost
3. Is the arbitrage executable? (storage availability, delivery specs, quality matching)
4. Breakeven: at what futures premium does cash-and-carry become profitable?
5. Risks: basis risk at delivery, quality adjustments, early delivery option value
```

---

## 2. Energy Trading

**Key spreads:**
- **Crack spread (refining margin):** Revenue from refined products minus crude cost. 3-2-1 crack = 2 * gasoline + 1 * heating oil - 3 * crude.
- **Spark spread (power generation):** Power price - (gas price * heat rate). Measures gas-fired power plant profitability.
- **Frac spread:** NGL price - natural gas price. Measures gas processing economics.
- **Brent-WTI spread:** Reflects Atlantic Basin supply/demand balance, pipeline capacity, export economics.

```
Analyze the crude oil market:

Supply/demand balance:
- Global production: [PROD] mbd (OPEC: [OPEC], Non-OPEC: [NON_OPEC])
- Global demand: [DEMAND] mbd
- Implied surplus/deficit: [BALANCE] mbd
- OECD commercial inventories: [INV] mb (vs 5Y avg: [INV_5Y])
- OPEC spare capacity: [SPARE] mbd
- US shale rig count: [RIGS] (trend: [UP/DOWN/FLAT])

Prices:
- Brent front month: $[BRENT]
- WTI front month: $[WTI]
- Brent-WTI spread: $[BW_SPREAD]
- Brent 12M calendar spread: $[BRENT_12M_CAL]

Geopolitical risk premium (qualitative): [LOW / MODERATE / ELEVATED / HIGH]

Provide:
1. Supply/demand outlook for next 2 quarters
2. Fair value estimate based on inventory levels and balances
3. OPEC behavior: compliance, production cuts/additions expected?
4. Crack spread analysis: refining margins signaling demand strength or weakness?
5. Positioning: CFTC managed money net length vs historical range
6. Trade recommendations: outright, calendar spread, or crack spread
```

```
Evaluate natural gas basis and seasonal patterns:

- Henry Hub front month: $[HH_PRICE] per MMBtu
- Regional hub: [HUB_NAME] at $[REGIONAL_PRICE]
- Basis: $[BASIS] (premium/discount to HH)
- Storage (US): [STORAGE_BCF] Bcf (vs 5Y avg: [STORAGE_5Y] Bcf)
- Winter strip (Nov-Mar): $[WINTER_STRIP]
- Summer strip (Apr-Oct): $[SUMMER_STRIP]
- Winter/summer spread: $[W_S_SPREAD]
- LNG export capacity: [LNG_CAP] Bcf/d, current flows: [LNG_FLOWS] Bcf/d

Analyze:
1. Storage trajectory: injection/withdrawal rate vs seasonal norm
2. Weather outlook: heating degree days (HDD) / cooling degree days (CDD) forecast
3. Seasonal spread trade: long winter / short summer (or vice versa)?
4. Regional basis drivers: pipeline capacity, local production, demand nodes
5. LNG export impact: how much incremental demand is LNG pulling from the market?
6. Risk scenarios: polar vortex, hurricane disruption, pipe outage
```

---

## 3. Metals Analysis

**Gold pricing framework:**
Gold = f(real yields, USD, central bank purchases, geopolitical risk, physical demand)
Strong inverse correlation with US real yields (TIPS): gold competes with yield-bearing safe assets.

**Copper-to-gold ratio:** Historically correlated with the 10Y Treasury yield and global growth expectations. Rising ratio = risk-on, falling ratio = risk-off.

**LME dynamics:** Warehouse stocks, cancelled warrants (metal earmarked for withdrawal), tom-next spread (backwardation indicator), exchange for physical (EFP) basis.

```
Analyze the metals market with macro overlay:

Gold:
- Spot: $[GOLD_SPOT] per oz
- US 10Y real yield (TIPS): [REAL_YIELD]%
- USD index (DXY): [DXY]
- Central bank net purchases (YTD): [CB_TONS] tonnes
- ETF holdings: [ETF_TONS] tonnes (change MTD: [ETF_CHG])

Copper:
- Spot (LME): $[CU_SPOT] per tonne
- LME warehouse stocks: [CU_LME] tonnes (trend: [UP/DOWN])
- Cancelled warrants: [CU_WARRANTS]%
- China import premium: $[CU_CHINA_PREM] per tonne
- Copper-to-gold ratio: [CU_AU_RATIO] (6M change: [CU_AU_CHG])

Provide:
1. Gold fair value model: based on real yields, DXY, and central bank demand
2. Gold positioning: is current price above/below model? What explains the residual?
3. Copper supply/demand: mine supply growth, smelter utilization, demand from EVs/grid
4. Copper-to-gold ratio interpretation: what is it signaling about growth vs safety?
5. Relative value: long gold / short copper as recession hedge (or reverse)
6. Trade expression: futures, options, ETF, miners equity — pros/cons of each
```

---

## 4. Agricultural Commodities

**Key drivers:** Weather (El Nino/La Nina, drought, frost), crop cycle (planting, growing, harvest), USDA reports (WASDE, crop progress, export inspections), government policy (subsidies, export bans, ethanol mandates), and logistics (river levels, port congestion, freight rates).

**Crush spread (soybeans):** Revenue from soybean meal + soybean oil - soybean cost. Measures processing margin.

**Corn-ethanol spread:** Ethanol price * 2.8 (gallons per bushel) - corn price. Measures ethanol production economics.

```
Analyze the agricultural commodity outlook for [CROP]:

Fundamental data:
- USDA ending stocks estimate: [STOCKS] (stocks-to-use ratio: [STU_RATIO]%)
- Production estimate: [PROD] (vs prior year: [PROD_PRIOR])
- Demand: domestic [DOM_DEMAND], export [EXPORT_DEMAND]
- Key growing regions: [REGIONS]
- Crop condition (% good/excellent): [CONDITION]%
- Weather outlook: [WEATHER_SUMMARY]
- Current price: $[PRICE] per [UNIT]
- Seasonal pattern: [HIGH_MONTH] highs, [LOW_MONTH] lows

Provide:
1. Supply/demand balance: surplus or deficit? Trend in stocks-to-use ratio?
2. Weather risk premium: is current price embedding a weather risk premium?
3. Seasonal trade setup: where are we in the crop cycle? Buy/sell opportunity?
4. USDA report calendar: next key report date and potential market impact
5. Global trade flows: export competition (Brazil, Argentina, Black Sea, Australia)
6. Cross-commodity: substitution effects (corn/wheat, soybean meal/DDGs)
```

```
Evaluate this spread trade in the grain complex:

- Trade: [LONG_COMMODITY] / [SHORT_COMMODITY] spread
- Current spread: $[SPREAD] per [UNIT]
- 3Y average spread: $[AVG_SPREAD]
- 3Y spread range: $[LOW] to $[HIGH]
- Fundamental thesis: [THESIS]

Examples: corn/wheat spread, soybean crush, old crop/new crop calendar spread

Analyze:
1. Historical spread distribution and current percentile
2. Fundamental drivers: why should the spread widen/narrow from here?
3. Seasonal pattern of this spread
4. Position sizing: margin requirements, vol of spread, appropriate risk per unit
5. Entry, target, and stop-loss levels
6. Risks: weather event, USDA surprise, export ban, logistics disruption
```

---

## 5. Physical vs Derivatives

**Basis:** Physical price minus futures price (or vice versa, depending on convention). Basis risk arises when the hedge instrument does not perfectly match the physical exposure.

**Delivery mechanics:** Futures contracts specify quality, location, and timing for physical delivery. The short delivers to the long. Conversion factors (for bond futures) or quality differentials (for commodities) adjust for grade differences.

**Physical arbitrage:** Buy physical in one location, sell futures (or physical) in another, profiting from geographic basis after transport costs.

```
Analyze a physical vs derivatives basis trade:

- Commodity: [COMMODITY]
- Physical grade: [GRADE] at [LOCATION]
- Physical price: $[PHYS_PRICE] per [UNIT]
- Nearest futures contract: [CONTRACT] at $[FUTURES_PRICE]
- Basis: $[BASIS] ([PREMIUM/DISCOUNT] to futures)
- Delivery point: [DELIVERY_LOCATION]
- Transport cost (physical location to delivery): $[TRANSPORT]
- Quality differential: $[QUALITY_ADJ]
- Historical basis range (1Y): $[BASIS_LOW] to $[BASIS_HIGH]

Evaluate:
1. Is the basis wide or tight vs historical? What is driving it?
2. Physical arbitrage: can we buy physical, sell futures, and deliver profitably?
3. Logistics: transport availability, lead time, counterparty reliability
4. Quality risk: does the physical grade meet delivery specs? Any adjustments?
5. Financing: cost of holding physical inventory until delivery
6. Optionality: delivery window, alternative delivery points, grade substitution
```

```
A [PRODUCER/CONSUMER] needs to hedge [VOLUME] [UNITS] of [COMMODITY] for delivery
in [MONTHS] months at [LOCATION]:

- Current spot: $[SPOT]
- Futures ([MONTH]): $[FUTURES]
- Basis at [LOCATION] (historical avg): $[HIST_BASIS]
- Current basis: $[CURR_BASIS]
- Hedge instrument options: [EXCHANGE] futures, OTC swap, physical forward

Compare:
1. Futures hedge: contract specs, margin, basis risk, roll risk
2. OTC swap: fixed-for-floating, counterparty risk, ISDA documentation
3. Physical forward: lock in delivered price, credit risk, performance risk
4. Basis hedge: separate basis swap to lock in location differential
5. Recommended approach: considering liquidity, credit, basis risk, and accounting
```

---

## See Also

- [fx-and-rates.md](fx-and-rates.md) -- for commodity currencies (AUD, CAD, BRL, ZAR) and rate impact
- [derivatives.md](derivatives.md) -- for options pricing applied to commodity markets
- [structured-products.md](structured-products.md) -- for commodity-linked structured notes
- [market-making.md](market-making.md) -- for futures market-making and spread quoting
