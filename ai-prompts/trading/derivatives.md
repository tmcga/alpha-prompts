# Options & Derivatives Trading

```
You are a senior derivatives trader and structurer with deep expertise in options
pricing, volatility analysis, and complex payoff construction. You are fluent in
Black-Scholes-Merton, local volatility, stochastic volatility (Heston, SABR), and
Monte Carlo methods. You think in Greeks — delta, gamma, vega, theta, rho, vanna,
volga, charm — and manage multi-dimensional risk books. You understand volatility
surfaces, skew dynamics, term structure, and the relationship between implied and
realized volatility. You can construct, price, and risk-manage strategies ranging
from vanilla spreads to exotic path-dependent derivatives. When analyzing trades,
you provide exact Greeks, breakeven levels, max profit/loss, and scenario analysis
across spot and vol dimensions.
```

## What This Desk Does

The derivatives desk trades listed and OTC options across equities, indices, and other asset classes. Traders manage complex volatility books, pricing new structures for institutional clients while hedging Greeks in real time. The desk captures edge through volatility mispricing, skew trading, and time decay. Structurers design custom payoffs for hedging and yield enhancement. Risk management involves continuous delta-hedging, gamma and vega exposure monitoring, and stress testing across spot, vol, and correlation dimensions.

---

## 1. Options Pricing and Greeks

**Black-Scholes-Merton formula (European call):**
C = S * N(d1) - K * e^(-rT) * N(d2)

where d1 = [ln(S/K) + (r + sigma^2/2) * T] / (sigma * sqrt(T)),
d2 = d1 - sigma * sqrt(T), and N() is the standard normal CDF.

**Put-call parity:** C - P = S - K * e^(-rT)

**The Greeks:**
- Delta: dV/dS (directional exposure)
- Gamma: d^2V/dS^2 (convexity of delta, acceleration)
- Vega: dV/d(sigma) (sensitivity to implied vol)
- Theta: dV/dT (time decay, typically negative for long options)
- Rho: dV/dr (interest rate sensitivity)
- Vanna: d^2V/(dS * d(sigma)) (delta sensitivity to vol changes)
- Volga (Vomma): d^2V/d(sigma)^2 (vega convexity)
- Charm: d(delta)/dT (delta decay)

```
Price and risk-analyze this option position:

- Underlying: [TICKER], Current price: $[SPOT]
- Option type: [CALL/PUT]
- Strike: $[STRIKE] ([MONEYNESS]% moneyness)
- Expiration: [DATE] ([DTE] days to expiry)
- Implied volatility: [IV]%
- Risk-free rate: [RATE]%
- Dividend yield: [DIV_YIELD]%
- Position size: [CONTRACTS] contracts

Calculate:
1. Theoretical price (Black-Scholes) and comparison to market price $[MARKET_PRICE]
2. Full Greeks: delta, gamma, vega, theta (daily), rho
3. Higher-order Greeks: vanna, volga, charm
4. Put-call parity check (if both put and call are available)
5. Breakeven at expiration and current breakeven (including theta decay)
6. P&L scenarios: spot +/- 5%, 10%; vol +/- 5 vols; time decay over 1 week
```

```
Decompose the P&L attribution for this options book over [PERIOD]:

- Starting portfolio Greeks: Delta [D0], Gamma [G0], Vega [V0], Theta [T0]
- Ending portfolio Greeks: Delta [D1], Gamma [G1], Vega [V1], Theta [T1]
- Spot move: $[S0] to $[S1] (dS = [DS], [DS_PCT]%)
- IV change: [IV0]% to [IV1]% (d_sigma = [DIVOL] vols)
- Time elapsed: [DAYS] calendar days

Attribute P&L to:
1. Delta P&L = delta * dS
2. Gamma P&L = 0.5 * gamma * dS^2
3. Vega P&L = vega * d_sigma
4. Theta P&L = theta * days
5. Residual (higher-order, cross-Greeks, unexplained)
6. Total P&L and reconciliation to actual book P&L of $[ACTUAL_PL]
```

---

## 2. Volatility Analysis

**Implied vs realized volatility:**
- Implied vol (IV): market's expectation of future volatility, extracted from option prices
- Realized vol (RV): historical volatility computed from actual returns
- Vol risk premium: IV - RV (typically positive — sellers earn a premium)

**Realized volatility calculation:**
RV = sqrt(252 / n * sum_i=1..n (ln(S_i / S_{i-1}))^2) (close-to-close)
Yang-Zhang estimator incorporates open, high, low, close for better efficiency.

**Vol surface dimensions:** Strike (moneyness), Expiry (term structure), and the interaction (skew dynamics).

```
Analyze the volatility surface for [TICKER / INDEX]:

Current spot: $[SPOT]
Term structure of ATM IV:
| Expiry   | DTE  | ATM IV | RV (same window) | IV - RV |
|----------|------|--------|-------------------|---------|
| [EXP_1]  | [D1] | [IV1]% | [RV1]%           | [DIFF1] |
| [EXP_2]  | [D2] | [IV2]% | [RV2]%           | [DIFF2] |
| [EXP_3]  | [D3] | [IV3]% | [RV3]%           | [DIFF3] |
| [EXP_4]  | [D4] | [IV4]% | [RV4]%           | [DIFF4] |

Skew (for [TARGET_EXPIRY]):
| Strike (% spot) | IV    |
|------------------|-------|
| 80%              | [S80] |
| 90%              | [S90] |
| 95%              | [S95] |
| 100% (ATM)       | [S100]|
| 105%             | [S105]|
| 110%             | [S110]|

Provide:
1. Term structure shape: contango, backwardation, or humped? What drives it?
2. Skew analysis: 25-delta put/call skew, skew richness vs historical
3. Vol-of-vol: is realized vol of IV elevated? (signal for gamma scalping)
4. Implied vol surface: any arbitrage violations (calendar spread, butterfly)?
5. Relative value: which expiry/strike offers the best long vol or short vol entry?
6. Upcoming catalysts that could cause vol repricing (earnings, events, data)
```

```
Evaluate a volatility trade on [TICKER]:

- Current ATM IV ([DTE]-day): [IV_CURRENT]%
- 20-day realized vol: [RV_20]%
- 60-day realized vol: [RV_60]%
- IV percentile rank (1Y): [IV_RANK]%
- Thesis: [LONG_VOL / SHORT_VOL] because [RATIONALE]

Structure the trade as:
1. Straddle (ATM): cost, breakeven, Greeks, max loss
2. Strangle (25-delta): cost, breakeven, Greeks, max loss
3. Calendar spread (sell front, buy back): cost, vega exposure, theta
4. Comparison: which structure best expresses the view with optimal risk/reward?
```

---

## 3. Options Strategy Construction

```
Construct an options strategy for the following view:

- Underlying: [TICKER] at $[SPOT]
- Directional view: [BULLISH / BEARISH / NEUTRAL]
- Volatility view: [LONG_VOL / SHORT_VOL / NEUTRAL]
- Conviction: [HIGH / MODERATE / LOW]
- Time horizon: [DAYS / WEEKS / MONTHS]
- Max capital at risk: $[MAX_LOSS]
- Target return: [X]x risk

Consider these structures (as appropriate to the view):
1. Vertical spread (bull call, bear put, bull put, bear call)
2. Straddle or strangle
3. Risk reversal (sell put, buy call or vice versa)
4. Ratio spread (1x2, 1x3)
5. Butterfly or condor
6. Collar (long stock + protective put + covered call)
7. Calendar or diagonal spread

For the recommended strategy, provide:
- Exact strikes and expirations
- Net debit or credit
- Max profit, max loss, breakeven point(s)
- Greeks at inception
- P&L diagram across spot prices at expiration
- Scenario: what happens if vol rises/falls 5 vols, spot moves +/- 10%
```

```
Design a yield enhancement overlay for a [LONG/SHORT] position in [TICKER]:

- Position: [SHARES] shares at $[ENTRY_PRICE]
- Current price: $[SPOT]
- Target exit: $[TARGET] ([X]% above/below current)
- Downside tolerance: $[FLOOR] ([Y]% below current)
- Holding period: [MONTHS] months
- Current ATM IV: [IV]%

Compare:
1. Covered call: strike selection, premium income, cap on upside
2. Collar: put strike + call strike, net cost, defined range
3. Put spread collar: sell put spread (reduce cost) + sell call
4. Cash-secured put writing at [STRIKE] if willing to add to position
For each, provide annualized yield enhancement, breakeven, and probability analysis.
```

---

## 4. Exotic Derivatives

Exotic derivatives have path-dependent or non-standard payoffs that require specialized pricing models.

**Barrier options:** knock-in or knock-out when spot crosses a barrier level.
**Digital (binary) options:** pay fixed amount if condition is met at expiry.
**Variance swaps:** Payoff = Notional * (RV^2 - K_var), where K_var = variance strike.
**Vol swaps:** Payoff = Notional * (RV - K_vol), where K_vol = vol strike.
Note: K_var > K_vol^2 due to convexity adjustment: K_var approx= K_vol^2 + vol_of_vol^2 * T.

**Autocallable:** periodic observation dates; if spot > autocall barrier, early redemption at coupon; if spot < knock-in barrier at maturity, investor bears downside.

```
Price and risk-assess this exotic derivative:

Type: [BARRIER_OPTION / DIGITAL / VARIANCE_SWAP / AUTOCALLABLE / OTHER]
Underlying: [TICKER / INDEX] at $[SPOT]

For barrier option:
- Option type: [CALL/PUT]
- Barrier type: [UP-AND-OUT / UP-AND-IN / DOWN-AND-OUT / DOWN-AND-IN]
- Strike: $[STRIKE], Barrier: $[BARRIER]
- Expiry: [DATE], Rebate: $[REBATE] (if any)

For variance/vol swap:
- Variance strike: [K_VAR] (or vol strike: [K_VOL]%)
- Vega notional: $[VEGA_NOTIONAL]
- Observation period: [START] to [END]
- Realized vol so far (if mid-period): [RV_SOFAR]%

Provide:
1. Theoretical price using appropriate model (local vol, Monte Carlo, closed-form)
2. Greeks and sensitivities (delta, vega, barrier delta, gap risk)
3. Scenario analysis: P&L at various spot levels and vol levels
4. Key risks: barrier proximity, gap risk, pin risk, correlation
5. Hedging approach: static replication vs dynamic hedging, costs and residual risks
```

---

## 5. Hedging Portfolio Risk

```
Design a hedging program for this portfolio:

Portfolio characteristics:
- AUM: $[AUM]
- Beta to [INDEX]: [BETA]
- Portfolio delta: [DELTA] (in $ terms)
- Top 5 positions: [POS_1], [POS_2], [POS_3], [POS_4], [POS_5]
- Current hedge ratio: [HEDGE_PCT]%
- Max annual hedging budget: [BUDGET]% of AUM

Risk to hedge: [DIRECTIONAL / TAIL / VOLATILITY / SPECIFIC_EVENT]

Evaluate these hedging approaches:
1. Index put options: strike selection, term, cost as % of AUM, protection level
2. Put spread: reduce cost by selling lower strike put, protection range
3. Collar on portfolio: sell upside call to fund downside put, net cost
4. VIX calls: convexity benefit in a crash, basis risk to portfolio
5. Tail risk hedge: deep OTM puts (5-10 delta), rolling program cost and payoff
6. Cross-asset hedge: short credit (HYG puts), long bonds, long gold

For the recommended approach:
- Exact instruments and sizing
- Cost per quarter, annualized drag on returns
- Protection: portfolio drawdown with and without hedge for -10%, -20%, -30% scenarios
- Greeks of the hedge overlay
- Rebalancing frequency and rules (delta-hedge the hedge? roll schedule?)
```

```
Evaluate this delta-hedging and gamma scalping strategy:

- Position: [LONG/SHORT] [CONTRACTS] ATM straddles on [TICKER]
- Implied vol at entry: [IV_ENTRY]%
- Delta-hedge frequency: [CONTINUOUS / DAILY / INTRADAY_N_TIMES]
- Current realized vol: [RV]%
- Days remaining: [DTE]
- Gamma: [GAMMA] (per 1% move)
- Theta: $[THETA] per day

Calculate:
1. Breakeven realized vol for this gamma scalping position
2. Expected P&L per day if RV = [SCENARIO_RV]%
3. Hedging P&L = 0.5 * gamma * (dS)^2 summed over rebalance intervals
4. Theta bleed per day vs expected gamma revenue
5. Impact of hedging frequency on P&L (discrete vs continuous)
6. Vol-of-vol effect: does clustering of moves help or hurt the strategy?
```

---

## See Also

- [equities.md](equities.md) -- for underlying equity execution and block trades
- [fixed-income.md](fixed-income.md) -- for bond options, swaptions, rate vol
- [fx-and-rates.md](fx-and-rates.md) -- for FX options and Garman-Kohlhagen model
- [structured-products.md](structured-products.md) -- for embedded optionality in structured notes
- [market-making.md](market-making.md) -- for options market-making dynamics
