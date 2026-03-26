# Fixed Income Asset Management

```
You are a senior fixed income portfolio manager at a large asset manager running $20-100B
across investment grade, high yield, emerging markets, and securitized mandates. You think
in terms of duration, convexity, spread duration, key rate exposures, and carry/roll-down
optimization. Every position must have a clearly defined yield advantage, spread compression
thesis, or curve positioning rationale. You understand that fixed income alpha at scale comes
from duration management, sector rotation, security selection, and yield curve positioning —
not from concentrated bets. You are deeply aware of benchmark construction, index rebalancing
flows, new issue concessions, and the liquidity premium embedded in off-the-run securities.
Your clients include pension funds with liability-matching needs, insurance companies with
regulatory capital constraints, and total return investors seeking income with controlled drawdown.
```

## What This Desk Does

The fixed income asset management team constructs and manages bond portfolios that target either benchmark-relative outperformance (active total return) or liability-matching objectives (LDI). Alpha sources in fixed income are more diverse than in equity — duration positioning, yield curve trades (flattener/steepener, butterfly), sector allocation (IG/HY/EM/securitized), issuer selection, and new issue arbitrage all contribute. The desk must manage interest rate risk (DV01, key rate durations), credit risk (spread duration, default probability), prepayment risk (MBS), and liquidity risk (bid-ask spreads widen dramatically in stress). Fixed income benchmarks like the Bloomberg Aggregate contain thousands of securities, many of which are illiquid, creating opportunities for active managers to outperform through stratified sampling and liquidity management.

---

## 1. Duration Management

Positioning portfolio interest rate sensitivity relative to the benchmark to express views on the level and shape of the yield curve.

**Modified Duration:** D_mod = -(1/P) x (dP/dy) — percentage price change per 1% yield change.

**Convexity:** C = (1/P) x (d2P/dy2) — measures curvature; positive convexity benefits the holder.

**DV01:** Dollar value of a 01 = D_mod x P x 0.0001 — dollar P&L per 1bp yield move.

**Key Rate Duration (KRD):** Sensitivity to yield changes at specific maturity points (2y, 5y, 10y, 30y), holding other points constant.

### Duration Positioning and Curve Trades

```
I manage a [benchmark: Bloomberg Aggregate / Bloomberg IG / Bloomberg HY / custom]-benchmarked
fixed income portfolio:

Portfolio characteristics:
- AUM: $[X]B
- Portfolio duration: [X] years (benchmark: [X] years)
- Duration deviation: [X] years (budget: +/- [X] years)
- Key rate duration profile: 2y=[X], 5y=[X], 10y=[X], 30y=[X]
- Benchmark KRD profile: 2y=[X], 5y=[X], 10y=[X], 30y=[X]

Current yield curve:
- 2y Treasury: [X]%, 5y: [X]%, 10y: [X]%, 30y: [X]%
- 2s10s spread: [X] bps, 5s30s spread: [X] bps
- Term premium estimate (ACM model): [X] bps at 10y

My rate view: [describe — e.g., "rates decline 50bps led by the front end as Fed cuts"]

Help me:
1. **Duration bet sizing**: If I extend duration by [X] years vs benchmark, what is my expected
   active return if rates move as expected? Active return from duration = -(D_p - D_b) x delta_y
2. **Curve trade construction**: Design a barbell vs bullet vs ladder trade
   - Barbell: Overweight 2y + 30y, underweight 10y (benefits from flattening + positive convexity)
   - Bullet: Concentrate in 5-10y (benefits from parallel shift down, lower convexity)
   - Butterfly: 2s/5s/10s or 5s/10s/30s, duration-neutral but curve-shape dependent
3. **Key rate duration positioning**: Which part of the curve to overweight/underweight?
   - KRD active bets: sum(KRD_active_k x delta_y_k) = expected active return from curve positioning
4. **Convexity management**: Portfolio convexity vs benchmark, cost of convexity (negative carry)
   - MBS: negative convexity at low rates (prepayment risk)
   - Callable bonds: negative convexity near call price
   - Long-dated zeros: maximum positive convexity
5. **Roll-down return**: Estimate carry + roll-down for each maturity bucket
   - Roll-down = yield at current maturity - yield at (current maturity - holding period) x duration

Duration risk budget: +/- [X] year deviation = approximately [X] bps tracking error per [X] bps
rate volatility. Size duration bets relative to conviction and tracking error budget.
```

---

## 2. Credit Allocation

Allocating across credit sectors (investment grade, high yield, emerging markets) and selecting issuers to generate spread-based alpha.

**Spread Duration:** Sensitivity of bond price to a 1bp change in credit spread (distinct from rate duration for spread product).

**Option-Adjusted Spread (OAS):** Spread over the Treasury curve after adjusting for embedded options (calls, puts, prepayment).

### Credit Sector Allocation

```
I need to set my credit sector allocation across:
- Investment grade corporates: [current weight X% vs benchmark X%]
- High yield: [current weight X% vs benchmark X%]
- EM hard currency: [current weight X% vs benchmark X%]
- EM local currency: [current weight X% vs benchmark X%]
- Securitized (ABS/CMBS): [current weight X% vs benchmark X%]

Current spread levels:
- IG OAS: [X] bps (percentile vs 20-year history: [X]th)
- HY OAS: [X] bps (percentile: [X]th)
- EM sovereign spread: [X] bps (percentile: [X]th)
- CMBS AAA spread: [X] bps

Credit cycle indicators:
- Default rate (trailing 12m): IG [X]%, HY [X]%
- Earnings growth: [X]%
- Net leverage: IG [X]x, HY [X]x
- Interest coverage: IG [X]x, HY [X]x
- Issuance pace: [above / below] trend

Help me:
1. **Spread compensation analysis**: Are spreads wide enough to compensate for expected defaults?
   - Breakeven default rate = OAS / (1 - recovery_rate) for each sector
   - Compare breakeven vs actual expected default rate
2. **Relative value across sectors**: Spread per unit of spread duration, spread per unit of default risk
3. **Credit cycle positioning**: Where are we in the cycle? (expansion, downturn, repair, recovery)
   - Expansion: Add HY beta, compress spread overweight
   - Downturn: Upgrade quality, reduce HY, increase IG
4. **Issuer selection within sectors**: Identify fallen angel candidates, rising stars, and curve trades
5. **Spread duration management**: Portfolio spread duration vs benchmark — how much spread risk?
   - Spread duration x spread change = approximate price impact from spread moves
6. **Tail risk**: Estimate portfolio loss in a 2008-style credit event (spreads +300-500bps in IG,
   +800-1200bps in HY) vs a mild recession (spreads +50-100bps IG, +150-300bps HY)
```

### Issuer Selection and Credit Research

```
Evaluate [ISSUER] bonds for inclusion in my credit portfolio:

Issuer: [name], Sector: [sector], Rating: [Moody's/S&P/Fitch]
Bond: [coupon]% [maturity date], Price: $[X], YTW: [X]%, OAS: [X] bps
Benchmark-comparable spread: [X] bps (sector average OAS for same rating/maturity)

Credit fundamentals:
- Revenue: $[X]B, EBITDA: $[X]B, Net income: $[X]B
- Total debt: $[X]B, Net debt/EBITDA: [X]x, Interest coverage: [X]x
- FCF: $[X]B, FCF/debt: [X]%
- Upcoming maturities: $[X]B in [time period]

Help me assess:
1. **Credit quality trajectory**: Is the credit improving or deteriorating? Rating migration probability?
2. **Spread adequacy**: Is the OAS sufficient compensation for the credit risk?
   - Compare: OAS vs sector peers, OAS vs historical range, OAS vs CDS spread
3. **Relative value on the curve**: Is the 5y or 10y bond cheaper? (Z-spread curve analysis)
4. **Event risk**: M&A, LBO, shareholder-friendly actions, litigation, regulatory
5. **Recovery analysis**: If default occurs, estimated recovery rate based on capital structure position
6. **Active spread duration contribution**: How does adding this bond affect portfolio spread duration?
```

---

## 3. Mortgage-Backed Securities

Managing prepayment risk and extracting value from the agency MBS market through OAS analysis, specified pool selection, and TBA trading.

**Effective Duration:** Accounts for prepayment changes when rates shift (unlike modified duration). Calculated by shocking rates +/- and averaging price changes.

**OAS (for MBS):** Spread over the Treasury curve that equates the present value of projected (prepayment-model-adjusted) cash flows to the market price, using Monte Carlo simulation of rate paths.

### MBS Portfolio Analysis

```
I manage an MBS allocation within a core fixed income portfolio:

MBS portfolio:
- Allocation: [X]% of portfolio ($[X]B) vs benchmark weight [X]%
- Coupon distribution: [X]% in 2.0s, [X]% in 2.5s, [X]% in 3.0s, [X]% in 3.5s+
- WAC: [X]%, WAM: [X] months, WALA: [X] months
- Effective duration: [X] years, Convexity: [X]
- Current coupon MBS spread to Treasuries: [X] bps

Prepayment environment:
- Current 30y mortgage rate: [X]%
- Primary-secondary spread: [X] bps
- Refi index: [X] (vs historical range [X]-[X])
- Prepayment speeds (CPR): [coupon 1] at [X] CPR, [coupon 2] at [X] CPR

Help me:
1. **OAS analysis**: Calculate OAS for each coupon stack using a prepayment model
   - OAS = total spread - prepayment option cost
   - Compare OAS across coupons to find cheapest MBS
2. **Convexity management**: MBS has negative convexity — when rates fall, prepayments increase
   (duration shortens when you want it longer) and vice versa
   - Hedge negative convexity with: long swaptions, Treasury options, or IO strips
3. **Specified pool selection**: Pay-up analysis for pools with prepayment protection
   - Low loan balance pools, high LTV pools, geographic concentrations
   - Pay-up = premium for specified pool vs TBA; is the pay-up justified by slower prepayments?
4. **TBA dollar roll analysis**: Calculate the roll (drop) for [month] settlement
   - Roll income = (front price - back price) - (accrued interest difference) + (reinvestment on principal)
   - Roll is "special" if roll income > financing cost — implies strong demand for TBA collateral
5. **Duration drift management**: MBS duration changes nonlinearly with rates
   - +100bps rate shock: portfolio duration extends to ~[X] years (extension risk)
   - -100bps rate shock: portfolio duration contracts to ~[X] years (contraction risk)
```

---

## 4. Liability-Driven Investing

Managing fixed income assets to match pension or insurance liabilities, focusing on funded status volatility reduction and glide path execution.

### LDI Portfolio Construction

```
I'm constructing an LDI portfolio for a corporate pension plan:

Liability characteristics:
- PBO (Projected Benefit Obligation): $[X]B
- Discount rate: [X]% (AA corporate curve)
- Liability duration: [X] years
- Liability key rate profile: 10y=[X]%, 20y=[X]%, 30y=[X]%
- Plan funded status: [X]% (assets / PBO)
- Annual benefit payments: $[X]M
- Active participants: [X]%, deferred vested: [X]%, retirees: [X]%

Current asset allocation:
- Return-seeking: [X]% (equities, alternatives)
- Liability-hedging: [X]% (long duration bonds, LDI strategies)

Help me:
1. **Hedge ratio calculation**: What percentage of liability interest rate risk is hedged?
   - Hedge ratio = (asset duration x asset value) / (liability duration x liability value)
   - Target: [X]% hedge ratio, increasing as funded status improves
2. **Key rate duration matching**: Match asset KRD profile to liability KRD profile
   - Liability cash flows are concentrated in 10-30y — need long-duration assets
   - Long corporate bonds (20-30y), STRIPS, Treasury futures overlay
3. **Glide path design**: As funded status improves from [X]% to 100%+:
   - Increase LDI allocation by [X]% for each [X]% improvement in funded status
   - Trigger points: 85% funded -> 50% LDI, 95% funded -> 70% LDI, 105% -> 90% LDI
4. **Credit spread hedging**: Liability discount rate = Treasuries + AA credit spread
   - Should I hedge the credit spread component? (Requires long credit, not just Treasuries)
   - Credit spread risk: PBO changes by ~[X]% per 10bps credit spread move
5. **Completion portfolio**: What derivatives overlay (Treasury futures, interest rate swaps)
   is needed to fill the duration gap between physical bonds and liability target?
   - Notional = (target_duration - physical_duration) x asset_value / futures_DV01
6. **Cash flow matching for retiree liabilities**: Dedicated bond portfolio for near-term payments
   - Match first [X] years of benefit payments with individual bonds (defeasance)
```

---

## 5. Total Return and Yield Curve Strategies

Generating alpha through carry optimization, roll-down capture, and relative value positioning along the yield curve.

### Carry and Roll-Down Optimization

```
I want to maximize carry + roll-down in my fixed income portfolio:

Current yield curve: [provide key points or describe shape]
Portfolio duration target: [X] years (vs benchmark [X] years)
Duration tolerance: +/- [X] years

Help me:
1. **Carry calculation by maturity bucket**:
   - Carry = yield - financing rate (repo rate or portfolio funding cost)
   - 2y carry: [X] bps, 5y: [X] bps, 10y: [X] bps, 30y: [X] bps
2. **Roll-down return by maturity**:
   - Roll-down = change in price as bond ages along a static yield curve
   - Approximate: roll-down = (yield_current_maturity - yield_shorter_maturity) x duration
   - Best roll-down typically in the 3-7y part of the curve (steepest part)
3. **Total carry + roll-down optimization**: Which maturity buckets maximize total return in a
   static curve environment?
   - Total expected return = carry + roll-down + expected capital gain from rate view
4. **Barbell vs bullet**: Compare carry/roll profiles
   - Bullet (5y concentrated): Maximum roll-down capture in steep curve
   - Barbell (2y + 10y): Higher carry at short end, convexity benefit at long end
5. **Spread carry**: For credit bonds, include spread carry (OAS x spread duration)
   - Total carry = Treasury carry + spread carry
   - Risk-adjusted carry = carry / spread_duration (carry per unit of spread risk)
6. **Breakeven analysis**: How much can yields rise before total return turns negative?
   - Breakeven yield change = (carry + roll-down) / duration
   - Example: 200bps carry + 40bps roll-down, 6y duration -> breakeven = 40bps yield rise
```

---

## Mathematical Reference

**Modified Duration:** D_mod = D_mac / (1 + y/k) where k = compounding frequency

**Effective Duration:** D_eff = (P_down - P_up) / (2 x P_0 x delta_y) — used for bonds with embedded options

**Convexity:** C = (P_down + P_up - 2*P_0) / (P_0 x delta_y^2)

**Price Change (2nd order):** delta_P/P = -D_mod x delta_y + (1/2) x C x (delta_y)^2

**DV01:** DV01 = D_mod x P x 0.0001

**Key Rate Duration:** KRD_k = -(1/P) x (dP/dy_k) holding all other key rates constant. Sum of KRDs = effective duration.

**Spread Duration:** SD = -(1/P) x (dP/ds) where s = credit spread. For fixed-rate bullet bonds, spread duration approximately equals modified duration.

**OAS (MBS):** The constant spread added to each simulated short rate path such that the average present value of cash flows across all Monte Carlo paths equals the market price.

**Roll-Down Return:** R_roll = (yield_T - yield_{T-dt}) x D_mod x dt (approximately)

**Breakeven Yield Change:** delta_y_BE = (carry + roll) / D_mod — yield must rise by this amount to offset carry and roll-down income.

---

## See Also

- [Multi-Asset Allocation](multi-asset.md) — fixed income's role in strategic and tactical asset allocation
- [Risk & Performance Analytics](risk-analytics.md) — VaR, duration contribution, and scenario analysis for bond portfolios
- [Active Equity](active-equity.md) — equity counterpart for total portfolio construction
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — factor models and risk parity frameworks applicable to fixed income factors
