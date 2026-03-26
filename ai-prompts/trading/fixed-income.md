# Fixed Income Trading -- Rates & Credit

```
You are a senior fixed income trader covering both rates and credit markets at a
major dealer. You have deep expertise in government bonds, investment-grade and
high-yield corporate bonds, interest rate swaps, and credit default swaps. You think
in terms of spreads (Z-spread, OAS, ASW, CDS basis), carry and roll-down, relative
value across the curve, and convexity. You understand repo markets, financing costs,
and how central bank policy transmits through the rates complex. When asked to
analyze a trade, you provide specific spread levels, DV01 calculations, breakeven
analysis, and scenario P&L. You reference real market conventions (30/360, ACT/360,
semi-annual vs annual coupons, T+1 settlement).
```

## What This Desk Does

The fixed income desk trades government bonds, corporate bonds, and related derivatives across the maturity spectrum. Rates traders manage yield curve exposure, construct relative value trades, and position for central bank policy shifts. Credit traders focus on corporate bond spreads, CDS, and crossover opportunities between investment grade and high yield. The desk provides liquidity to institutional investors, manages inventory risk, and generates alpha through carry, roll-down, and mean-reversion strategies. Financing via the repo market is integral to every position.

---

## 1. Bond Relative Value

Relative value analysis identifies bonds that are cheap or rich versus a fitted curve or comparable securities. The primary spread measures are:

- **G-spread:** yield minus interpolated government bond yield
- **Z-spread:** constant spread added to the spot Treasury curve to match bond price
- **OAS (Option-Adjusted Spread):** Z-spread adjusted for embedded optionality (calls, puts, sinking funds)
- **ASW (Asset Swap Spread):** spread to LIBOR/SOFR on an asset-swapped basis

**Z-spread formula:**
Price = sum_t=1..n [ CF_t / (1 + r_t + Z)^t ], where r_t = spot rate at time t, Z = Z-spread, CF_t = cash flow at time t.

```
Perform a relative value analysis on these bonds:

Bond A: [ISSUER_A] [COUPON_A]% [MATURITY_A], Price: [PRICE_A], Yield: [YIELD_A]%
Bond B: [ISSUER_B] [COUPON_B]% [MATURITY_B], Price: [PRICE_B], Yield: [YIELD_B]%

- Both rated [RATING]
- Sector: [SECTOR]
- Benchmark Treasury: [UST_COUPON]% [UST_MATURITY], Yield: [UST_YIELD]%
- SOFR swap rate ([TENOR]): [SWAP_RATE]%

Calculate and compare:
1. G-spread, Z-spread, OAS, and ASW spread for each bond
2. Carry (coupon income minus financing cost) over 3-month horizon
3. Roll-down return assuming unchanged spread curve
4. Total expected return = carry + roll-down +/- spread change scenarios
5. Liquidity assessment (bid-ask spread, issue size, age, benchmark status)
6. Recommendation: which bond is cheaper and what trade expresses the view?
```

```
Build a rich/cheap analysis for the [ISSUER] credit curve:

Outstanding bonds:
| Bond     | Coupon | Maturity   | Price   | Yield  | Z-spread | OAS  |
|----------|--------|------------|---------|--------|----------|------|
| [BOND_1] | [C1]%  | [MAT_1]   | [P1]    | [Y1]%  | [Z1]     | [O1] |
| [BOND_2] | [C2]%  | [MAT_2]   | [P2]    | [Y2]%  | [Z2]     | [O2] |
| [BOND_3] | [C3]%  | [MAT_3]   | [P3]    | [Y3]%  | [Z3]     | [O3] |
| [BOND_4] | [C4]%  | [MAT_4]   | [P4]    | [Y4]%  | [Z4]     | [O4] |

1. Fit a credit curve through these points (linear, Nelson-Siegel, or polynomial)
2. Identify residuals: which bonds are rich (above curve) or cheap (below curve)?
3. Suggest curve trades: buy cheap, sell rich, DV01-neutral
4. Account for differences in coupon, liquidity, and covenants
```

---

## 2. Yield Curve Trading

Yield curve trades express views on how the shape of the curve will change, independent of the overall level.

**Common curve trades:**
- **Flattener:** short the short end, long the long end (profits if curve flattens)
- **Steepener:** long the short end, short the long end (profits if curve steepens)
- **Butterfly:** long the wings, short the belly (or vice versa)

**Butterfly spread:**
Butterfly = 2 * yield_belly - yield_short - yield_long

**DV01 weighting for curve-neutral trades:**
Weight ratio = DV01_A / DV01_B (to be duration-neutral across the legs)

```
Design a yield curve trade based on the following view:

- View: [FLATTENING / STEEPENING / BUTTERFLY_WIDENING / BUTTERFLY_NARROWING]
- Curve: [UST / BUND / GILT / SOFR_SWAP]
- Tenors: [SHORT_TENOR] vs [LONG_TENOR] (or [SHORT] / [BELLY] / [LONG] for butterfly)
- Current levels:
  - [SHORT_TENOR] yield: [Y_SHORT]%
  - [BELLY_TENOR] yield: [Y_BELLY]% (if butterfly)
  - [LONG_TENOR] yield: [Y_LONG]%
- Spread (current): [SPREAD] bps
- Spread (3M average): [AVG_SPREAD] bps
- Catalyst: [FED_MEETING / SUPPLY / DATA_RELEASE / POSITIONING]

Provide:
1. Exact position sizing (DV01-neutral across legs)
2. Carry and roll-down for each leg and net
3. Breakeven: how many bps of adverse curve move before carry is consumed
4. Scenario analysis: +/- 25bps parallel shift, +/- 15bps curve move
5. Historical percentile of current curve spread
6. Risk factors: supply calendar, central bank, flight-to-quality
```

---

## 3. Credit Trading

Credit trading spans investment-grade (IG) and high-yield (HY) corporate bonds and credit default swaps (CDS).

**CDS basis:**
Basis = CDS spread - bond Z-spread (or ASW). Positive basis = CDS wider than bonds; negative basis = CDS tighter.

**CDS pricing (simplified):**
CDS_spread approx= (1 - Recovery) * hazard_rate, where hazard rate is the annualized probability of default.

```
Analyze this credit trading opportunity:

- Issuer: [ISSUER]
- Rating: [RATING] (Moody's/S&P/Fitch)
- Sector: [SECTOR]
- 5Y CDS: [CDS_SPREAD] bps
- 5Y bond Z-spread: [Z_SPREAD] bps
- CDS basis: [BASIS] bps
- Recovery assumption: [RECOVERY]%
- Recent catalyst: [DOWNGRADE / EARNINGS / M&A / RESTRUCTURING / SECTOR_STRESS]

Evaluate:
1. Is the CDS basis justified? What drives it (funding, delivery option, restructuring clause)?
2. Implied default probability from CDS spread vs historical default rate for this rating
3. Relative value: bonds vs CDS — which offers better risk-adjusted carry?
4. Basis trade construction: buy bond + buy CDS protection (negative basis trade)
5. Funding cost assumption and breakeven holding period
6. Jump-to-default risk: P&L on each leg if sudden credit event occurs
```

```
Screen for crossover credit opportunities:

- Universe: [IG_INDEX / HY_INDEX / SPECIFIC_SECTOR]
- Focus: [FALLEN_ANGELS / RISING_STARS / CROSSOVER (BBB-/BB+)]
- Time horizon: [3M / 6M / 12M]
- Macro backdrop: [TIGHTENING / EASING / NEUTRAL]

Identify candidates where:
1. Rating trajectory diverges from spread pricing (spread implies downgrade but fundamentals improving, or vice versa)
2. Index inclusion/exclusion mechanics create forced buying or selling
3. Fallen angel candidates: IG names at risk of downgrade to HY — quantify the spread widening on index exit
4. Rising star candidates: HY names likely to be upgraded to IG — quantify the spread compression on index entry
5. For each candidate, provide: current spread, rating, leverage, interest coverage, free cash flow trend
```

---

## 4. Repo and Financing

The repo market is the plumbing of fixed income trading. Every position has an associated financing cost or benefit.

**Key concepts:**
- **GC (General Collateral):** standard repo rate for generic Treasury collateral
- **Special:** repo rate below GC for bonds in high demand (short squeeze, settlement fails)
- **Implied repo rate:** IRR = [(Futures_price + accrued_at_delivery) / (Bond_price + accrued_today) - 1] * (360 / days)
- **Term repo:** locked-in financing rate for a defined period (vs overnight roll risk)

```
Analyze the repo and financing dynamics for this position:

- Bond: [ISSUER] [COUPON]% [MATURITY]
- Position: [LONG/SHORT] $[NOTIONAL] face value
- Overnight GC rate: [GC_RATE]%
- Overnight special rate (if applicable): [SPECIAL_RATE]%
- Term repo rate ([TENOR]): [TERM_RATE]%
- Bond coupon frequency: [SEMI / ANNUAL / QUARTERLY]
- Next coupon date: [DATE]

Calculate:
1. Daily and monthly carry cost (or benefit) of financing this position
2. Advantage of term repo vs overnight roll (rate lock vs flexibility)
3. If the bond is on special: implied demand, fails rate, squeeze probability
4. Net carry = coupon accrual - repo cost (positive carry or negative carry)
5. Impact of a [X]bps move in repo rates on the position's P&L
```

---

## 5. Duration and Convexity Management

Duration and convexity are the primary risk measures for fixed income portfolios.

**Key formulas:**
- **Modified duration:** ModDur = -1/P * dP/dy
- **DV01 (Dollar Value of 1bp):** DV01 = ModDur * Price * Notional / 10,000
- **Convexity:** C = 1/P * d^2P/dy^2
- **Price change (second-order):** dP/P approx= -ModDur * dy + 0.5 * Convexity * (dy)^2
- **Key Rate Duration (KRD):** sensitivity to a shift at a specific point on the curve

```
Manage the duration and convexity profile of this portfolio:

Portfolio:
| Bond       | Notional ($M) | ModDur | Convexity | DV01 ($) | KRD_2Y | KRD_5Y | KRD_10Y | KRD_30Y |
|------------|---------------|--------|-----------|----------|--------|--------|---------|---------|
| [BOND_1]   | [N1]          | [D1]   | [C1]      | [DV1]    | [K1_2] | [K1_5] | [K1_10] | [K1_30] |
| [BOND_2]   | [N2]          | [D2]   | [C2]      | [DV2]    | [K2_2] | [K2_5] | [K2_10] | [K2_30] |
| [BOND_3]   | [N3]          | [D3]   | [C3]      | [DV3]    | [K3_2] | [K3_5] | [K3_10] | [K3_30] |
| Total      | [N_TOT]       | [D_T]  | [C_T]     | [DV_T]   | [KT_2] | [KT_5] | [KT_10] | [KT_30] |

- Target duration: [TARGET_DUR]
- Target DV01: $[TARGET_DV01]
- Benchmark: [BENCHMARK_INDEX]
- Benchmark duration: [BENCH_DUR]

Provide:
1. Current duration mismatch vs benchmark (over/underweight in duration)
2. Key rate duration profile vs benchmark — identify curve exposure
3. Convexity position: are we long or short convexity relative to benchmark?
4. Hedging recommendations using futures (contracts, notional, DV01 match)
5. Scenario P&L: parallel shift +/- 50bps, 100bps; bull/bear flattener/steepener
6. Convexity hedging: when to use options (swaptions, bond options) vs cash bonds
```

```
A portfolio needs to add $[NOTIONAL]M of convexity. Current portfolio convexity
is [CURRENT_CONV] and target is [TARGET_CONV].

Compare these approaches:
1. Buy long-dated Treasuries (30Y) — convexity per unit of duration
2. Buy receiver swaptions ([STRIKE], [EXPIRY]x[TENOR]) — gamma and vega exposure
3. Buy Treasury bond options (calls on TLT or bond futures options)
4. Sell MBS (which are short convexity due to prepayment risk)

For each, calculate: cost, DV01 impact, convexity added, carry implications, and
liquidity of the hedge.
```

---

## See Also

- [derivatives.md](derivatives.md) -- for interest rate options and swaption strategies
- [structured-products.md](structured-products.md) -- for MBS, ABS, CLO analysis
- [fx-and-rates.md](fx-and-rates.md) -- for cross-currency rates and swap pricing
- [market-making.md](market-making.md) -- for bond market-making dynamics
