# Global Macro

## Role Context

```
You are a senior global macro portfolio manager at a $10B macro fund. You build top-down
views on economies, rates, currencies, and commodities, then express those views through the
most efficient instrument and structure. You think in terms of regime identification, policy
divergence, and cross-asset consistency. Every trade must answer three questions: What is my
macro thesis? What is the best expression? What will prove me wrong? You respect that macro
is a game of incomplete information and emphasize scenario-weighted expected value over
point forecasts. You are fluent in central bank communication, balance of payments dynamics,
and the plumbing of global capital flows.
```

---

## What This Desk Does

Global macro funds trade liquid instruments across asset classes -- government bonds, interest rate swaps, FX, equity indices, and commodities -- to express views on macroeconomic trends and policy shifts. The edge comes from synthesizing disparate macro data into a coherent regime view before the market reprices: identifying inflection points in growth, inflation, or policy where current pricing embeds the wrong probability distribution. Unlike fundamental equity, macro trades are directional and levered, with typical portfolio volatility of 10-15% targeting a Sharpe ratio of 0.7-1.2. Position sizing is driven by conviction, volatility normalization, and correlation to existing book. The best macro trades have asymmetric payoff: limited downside with convex upside when a regime shift occurs.

---

## 1. Macro Thesis Construction

### Build a Top-Down Macro View

```
I'm constructing a macro view for [country / region] over the next [6 / 12 / 18] months.

Current macro backdrop:
- GDP growth (current, trend): [X]%, [X]%
- Inflation (headline, core): [X]%, [X]%
- Policy rate (current, market-implied terminal): [X]%, [X]%
- Fiscal stance: [expansionary / neutral / contractionary]
- Credit conditions: [easing / tightening / neutral]
- Current account: [surplus / deficit] of [X]% of GDP
- Currency: [appreciating / stable / depreciating] in real effective terms

Help me build a structured macro thesis:

1. **Regime identification**: Which macro regime are we in?
   - Goldilocks (above-trend growth, low inflation)
   - Reflation (accelerating growth, rising inflation)
   - Stagflation (slowing growth, persistent inflation)
   - Deflation/recession (contracting growth, falling inflation)
   Use: Growth surprise index, inflation surprise index, PMI trajectory, yield curve shape

2. **Regime transition probability**: What is changing?
   - Leading indicators pointing to regime shift: [list LEIs and their signals]
   - Policy pivot likelihood: Is the central bank behind the curve?
   - Fiscal impulse direction: Is government spending accelerating or decelerating?

3. **Identify macro divergences**: Where are two economies on different paths?
   - Growth divergence: [Country A] accelerating vs. [Country B] decelerating
   - Policy divergence: [Country A] hiking vs. [Country B] easing
   - These divergences create the highest-conviction relative value trades

4. **Construct scenario tree**:
   | Scenario | Probability | Growth | Inflation | Policy Response |
   |----------|------------|--------|-----------|-----------------|
   | Base     | [X]%       | [X]%   | [X]%      | [describe]      |
   | Bull     | [X]%       | [X]%   | [X]%      | [describe]      |
   | Bear     | [X]%       | [X]%   | [X]%      | [describe]      |
   | Tail     | [X]%       | [X]%   | [X]%      | [describe]      |

5. **IS-LM consistency check**:
   - IS curve: Does my growth view align with monetary/fiscal settings and financial conditions?
   - LM curve: Is money supply growth consistent with my inflation forecast?
   - If fiscal expansion + monetary tightening -> higher rates, stronger currency, crowded out investment
   - If fiscal expansion + monetary easing -> growth acceleration, inflation risk, currency pressure
```

---

## 2. Central Bank Analysis

### Parse Central Bank Policy Trajectory

```
Analyze the current policy stance and likely trajectory for [central bank: Fed / ECB / BOJ / BOE / PBOC]:

Current policy:
- Policy rate: [X]%
- Market-implied rate path (OIS/Fed funds futures): [list next 4 meetings]
- Balance sheet: [X] trillion, [expanding / tapering / QT at $X/month]
- Forward guidance language: [quote key phrases from latest statement]

Framework -- Taylor Rule estimate:
  i* = r* + pi + 0.5(pi - pi*) + 0.5(y - y*)
  where:
  - r* = neutral real rate (estimate: [X]%)
  - pi = current inflation: [X]%
  - pi* = inflation target: [X]%
  - y - y* = output gap: [X]%
  - Taylor-implied rate: [calculate]

  Gap between Taylor rate and actual rate:
  - If actual < Taylor: Policy is too loose, tightening should continue
  - If actual > Taylor: Policy is too tight, easing likely

Analysis:
1. **Dot plot / projections vs. market pricing**: Where are the gaps?
   - Central bank median projection for year-end rate: [X]%
   - Market pricing for year-end rate: [X]%
   - This gap = the trade opportunity

2. **Reaction function mapping**:
   - What data would cause a hawkish pivot? [specific thresholds]
   - What data would cause a dovish pivot? [specific thresholds]
   - What is the pain threshold for balance sheet intervention?

3. **Communication signal extraction**:
   - Key phrase changes from prior statement: [list]
   - Press conference tone: [hawkish / neutral / dovish] relative to statement
   - Dissent pattern: [who dissented, which direction]
   - Minutes/accounts: [key debates, risk scenarios discussed]

4. **Balance sheet dynamics**:
   - QE/QT pace and composition (duration, MBS vs. Treasuries)
   - Reserve levels and money market plumbing stress indicators
   - Implied liquidity impact on risk assets
```

---

## 3. Cross-Asset Trade Expression

### Express a Macro View Through the Optimal Instrument

```
My macro thesis: [describe your macro view, e.g., "US growth is decelerating faster than
Europe, leading to Fed cuts before ECB cuts"]

Help me find the best trade expression across asset classes:

1. **Rates**:
   - Outright duration: Long [X]-year bond / Short [X]-year bond
   - Curve trades: [Steepener / Flattener] in [2s10s / 5s30s / other]
   - Cross-market: Long [Country A] bonds vs. Short [Country B] bonds
   - Swaps vs. cash: Pay/receive fixed in [tenor] IRS
   - Breakeven inflation: Long/short TIPS, inflation swaps

2. **FX**:
   - Spot: Long [CCY A] / Short [CCY B]
   - Carry-adjusted: Net carry of [X] bps/year (interest rate differential)
   - Purchasing Power Parity check:
     PPP rate = S_0 x (1 + pi_domestic) / (1 + pi_foreign)
     Current spot vs. PPP: [overvalued / undervalued] by [X]%
   - Interest Rate Parity:
     F/S = (1 + r_domestic) / (1 + r_foreign)
     Forward points imply [X] bps carry cost/benefit

3. **Equities**:
   - Country/regional index: Long [index A] vs. Short [index B]
   - Sector rotation: Which sectors benefit from this macro regime?
   - Volatility: Long/short VIX, variance swaps, put spreads

4. **Commodities**:
   - Energy: [Oil, natural gas] directional or relative value
   - Metals: [Gold, copper] -- gold for real rate view, copper for growth view
   - Agriculture: [if relevant to inflation/EM thesis]

5. **Optimal structure evaluation**:
   For each expression, compare:
   - Sharpe ratio of the trade (expected return / volatility)
   - Convexity: Does the trade have asymmetric payoff?
   - Liquidity: Can I get in and out cleanly?
   - Carry: Does the trade earn or bleed while I wait for the thesis to play out?
   - Correlation to existing book: Does this add diversification or concentration?

   Rank expressions by: Carry-adjusted Sharpe x (1 + convexity bonus) x (1 - correlation penalty)
```

---

## 4. Geopolitical Risk Assessment

### Build a Geopolitical Scenario Tree

```
Geopolitical event under analysis: [describe event, e.g., "Taiwan Strait tensions",
"Middle East supply disruption", "European energy crisis", "EM sovereign default"]

Construct a decision tree with probability-weighted outcomes:

1. **Scenario definition** (mutually exclusive, collectively exhaustive):
   | Scenario | Description | Probability | Duration |
   |----------|-------------|-------------|----------|
   | De-escalation | [describe] | [X]% | [X] months |
   | Status quo | [describe] | [X]% | Indefinite |
   | Escalation (contained) | [describe] | [X]% | [X] months |
   | Escalation (systemic) | [describe] | [X]% | [X]+ months |

2. **Asset impact matrix** (% move from current levels):
   | Scenario | Equities | Rates | USD | Oil | Gold | EM FX |
   |----------|----------|-------|-----|-----|------|-------|
   | De-escalation | +[X]% | +[X]bps | [X]% | -[X]% | -[X]% | +[X]% |
   | Status quo | [X]% | [X]bps | [X]% | [X]% | [X]% | [X]% |
   | Escalation (contained) | -[X]% | -[X]bps | +[X]% | +[X]% | +[X]% | -[X]% |
   | Escalation (systemic) | -[X]% | -[X]bps | +[X]% | +[X]% | +[X]% | -[X]% |

3. **Expected value across scenarios**:
   E[Asset move] = Sum of: P(scenario_i) x Impact(scenario_i)

4. **Tail hedge construction**:
   - Which options structures provide convex payoff in the escalation scenario?
   - Cost of hedge as % of portfolio NAV (acceptable: [X] bps/month)
   - Hedge ratio: Size to offset [X]% of portfolio loss in escalation scenario

5. **Signal monitoring**: What observable data indicates we are moving between scenarios?
   - Military/diplomatic actions: [specific indicators]
   - Market-based: CDS spreads, FX vol, commodity backwardation
   - News flow: [key sources and keywords to monitor]
```

---

## 5. Emerging Market Analysis

### Evaluate an Emerging Market Opportunity

```
I'm analyzing [EM country] for a potential [long / short] position in [local rates / FX /
sovereign credit / equity index].

Fundamental EM scorecard:
- Current account balance: [X]% of GDP (surplus > 0% = favorable)
- FX reserves: $[X]B, covering [X] months of imports (< 3 months = danger zone)
- External debt / GDP: [X]% (> 60% = elevated risk)
- Short-term external debt / FX reserves: [X]% (> 100% = Guidotti rule violation)
- Real interest rate (nominal - inflation): [X]% (positive = attracting capital)
- Fiscal deficit: [X]% of GDP
- Political risk: [election cycle, regime stability, institutional quality]
- Sovereign CDS spread: [X] bps (vs. rating-implied fair value of [X] bps)

Analysis framework:

1. **Balance of payments sustainability**:
   - Is the current account deficit funded by FDI (stable) or portfolio flows (flighty)?
   - Reserve adequacy: Reserves / (Short-term debt + current account deficit) > 1.0?
   - Terms of trade: Is the country a commodity exporter or importer? Direction of commodity cycle?

2. **Carry vs. crisis analysis**:
   - Carry: Nominal yield [X]% minus estimated depreciation [X]% = expected return [X]%
   - Covered interest parity deviation: NDF-implied yield vs. actual yield
   - Carry-to-risk ratio: Expected carry / FX volatility (target > 0.5 for attractive carry)
   - Crisis probability: Based on reserve adequacy, political risk, external debt profile
   - Expected value: P(stable) x Carry return + P(crisis) x Crisis loss

3. **Real exchange rate assessment**:
   - REER level vs. 10-year average: [overvalued / undervalued] by [X]%
   - PPP-implied exchange rate vs. spot
   - Balassa-Samuelson adjustment for productivity differentials
   - Direction of real rate adjustment needed for external balance

4. **Political risk premium**:
   - Election timeline: [X] months to next election
   - Policy continuity risk: [high / medium / low]
   - Capital control risk: History and current probability
   - Institutional quality trend: [improving / stable / deteriorating]

5. **Position sizing for EM**:
   - EM positions should be sized at [50-75]% of equivalent DM conviction
   - Use options for tail risk: Buy [X]-delta puts on FX, sized to cap loss at [X]% of NAV
   - Diversify across EM countries: Max [X]% of NAV in any single EM
```

---

## Mathematical Frameworks Reference

**Purchasing Power Parity (PPP)**:
S_t = S_0 x (P_domestic / P_foreign). Long-run anchor for FX valuation. Mean reversion horizon: 3-5 years.

**Uncovered Interest Rate Parity (UIP)**:
E[S_t+1] / S_t = (1 + r_domestic) / (1 + r_foreign). Empirically violated -- the "forward premium puzzle" -- which is why carry trades work.

**Covered Interest Rate Parity (CIP)**:
F/S = (1 + r_domestic) / (1 + r_foreign). Arbitrage condition. Deviations signal funding stress.

**Taylor Rule**:
i* = r* + pi + 0.5(pi - pi*) + 0.5(y - y*). Compare to actual rate to assess policy stance.

**IS-LM / Mundell-Fleming**:
For open economies: Fiscal expansion under floating rates appreciates the currency and crowds out net exports. Monetary expansion depreciates the currency and boosts net exports. Use to check internal consistency of macro views.

**Scenario-Weighted Expected Value**:
E[R] = Sum_i P(scenario_i) x R(scenario_i). Always construct at least 3-4 scenarios. The base case should never exceed 60% probability -- overconfidence in base case is the most common macro error.

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- Portfolio construction, risk parity
- [`fundamental-long-short.md`](fundamental-long-short.md) -- Bottom-up equity overlays on macro themes
- [`credit-distressed.md`](credit-distressed.md) -- Sovereign credit and EM distressed
- [`event-driven.md`](event-driven.md) -- Event-driven macro (elections, referendums, policy shifts)
