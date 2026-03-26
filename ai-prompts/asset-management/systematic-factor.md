# Systematic & Factor Investing

```
You are a senior portfolio manager and researcher at a large systematic asset manager
running $50-200B in factor-based strategies. You design and manage smart beta products,
factor-tilted indices, and multi-factor portfolios for institutional and retail clients.
You think in terms of factor premia persistence, capacity, turnover, and implementation
costs. You are skeptical of data-mined factors and require economic intuition, out-of-sample
evidence, and cross-geography robustness for any factor you harvest. You understand that
your clients pay 10-30 bps for smart beta, so every basis point of turnover cost and
tracking error matters. You bridge academic factor research with practical portfolio
construction at scale.
```

## What This Desk Does

The systematic factor investing team designs, constructs, and manages portfolios that systematically harvest well-documented risk premia across equity and multi-asset universes. Unlike discretionary active managers who select individual stocks based on fundamental judgment, this team builds rules-based portfolios that target persistent factor exposures — value, momentum, quality, low volatility, and size — using transparent, repeatable methodologies. The key challenges are distinguishing genuine risk premia from data-mined artifacts, managing capacity and turnover at scale, timing factor exposures when valuation spreads are extreme, and monitoring for crowding that can amplify drawdowns. Products range from single-factor ETFs at 5 bps to multi-factor institutional mandates at 30 bps, all under intense fee pressure from passive indexing.

---

## 1. Factor Portfolio Construction

Designing and implementing portfolios that isolate specific factor exposures with controlled turnover and capacity.

**Fama-French 5-Factor Model:**
R_i - R_f = alpha_i + b1*MktRf + b2*SMB + b3*HML + b4*RMW + b5*CMA + epsilon_i

Where: MktRf = market excess return, SMB = small minus big (size), HML = high minus low (value), RMW = robust minus weak (profitability), CMA = conservative minus aggressive (investment).

**Carhart 4-Factor Model (adds momentum):**
R_i - R_f = alpha_i + b1*MktRf + b2*SMB + b3*HML + b4*UMD + epsilon_i

Where UMD = up minus down (12-1 month momentum).

### Single-Factor Portfolio Design

```
I'm designing a [factor: value / momentum / quality / low volatility / size] portfolio:

Universe: [e.g., Russell 1000, MSCI World, S&P 500]
Target AUM: $[X]B
Fee budget: [X] bps
Rebalancing frequency: [monthly / quarterly / semi-annually]

Factor definition and signal construction:
- Value: [book-to-market / earnings yield / FCF yield / composite]
- Momentum: [12-1 month return / earnings momentum / composite]
- Quality: [ROE / accruals / leverage / earnings stability / composite]
- Low vol: [realized vol / beta / idiosyncratic vol / downside vol]
- Size: [market cap / free-float market cap]

Help me design the portfolio:
1. **Signal construction**: How to combine multiple metrics into a composite factor score
   - Z-score standardization, winsorize at +/- 3 sigma, equal-weight or regression-weight sub-signals
2. **Portfolio formation**: Long-only tilt vs long/short factor portfolio
   - Long-only: Overweight top quintile, underweight bottom quintile, relative to cap-weight benchmark
   - Long/short: Long top decile, short bottom decile (for factor research, not product)
3. **Turnover management**: Buffer rules, partial rebalancing, turnover penalty in optimization
   - Expected annual one-way turnover: [X]% (target < [X]%)
   - Turnover cost = turnover x avg_spread/2 x market_impact_multiplier
4. **Capacity analysis**: At what AUM does market impact erode the factor premium?
   - Capacity = factor_premium / (turnover x impact_per_dollar x 2)
5. **Sector neutrality**: Should the factor portfolio be sector-neutral to avoid unintended sector bets?
6. **Factor exposure regression**: Verify the portfolio loads on the target factor and not others
   - Run: R_portfolio = alpha + b_target*F_target + b_other*F_other + epsilon
   - Want: high b_target, low b_other, significant alpha vs cap-weight

Factor portfolio Sharpe (long/short, gross of costs):
Value ~0.3, Momentum ~0.5, Quality ~0.4, Low Vol ~0.3, Size ~0.2
Net of turnover and implementation: subtract 0.05-0.15 from each.
```

### Multi-Factor Portfolio Integration

```
I want to build a multi-factor portfolio combining [list factors] in a single portfolio:

Approach options:
A) **Factor mixing**: Blend single-factor portfolio returns (portfolio of portfolios)
B) **Signal mixing**: Combine factor scores at the stock level, then build one portfolio (integrated)
C) **Sequential sorting**: Sort on factor 1, then within each group sort on factor 2

Help me evaluate:
1. **Mixing vs integration**: Signal mixing generally produces higher Sharpe (lower turnover,
   avoids holding a stock long in one factor and short in another), but is less transparent
2. **Factor correlations**: What is the correlation structure between my chosen factors?
   - Value and momentum: typically -0.3 to -0.5 (diversification benefit)
   - Quality and low vol: typically +0.3 to +0.5 (overlap risk)
   - Use: Sigma_portfolio = w' x Sigma_factor x w for factor allocation
3. **Factor weighting**: Equal risk contribution (risk parity across factors) vs equal weight vs
   optimized (maximize expected factor Sharpe)?
   - Risk parity: w_i proportional to 1/sigma_i (adjust for correlations)
4. **Interaction effects**: Do factor combinations create emergent exposures?
   - e.g., value + momentum = "cheap with improving sentiment" (powerful combo)
   - e.g., value + low vol may tilt heavily to utilities/REITs (sector concentration)
5. **Rebalancing coordination**: Stagger factor rebalancing dates to smooth turnover
6. **Performance expectation**: Multi-factor Sharpe ~0.5-0.8 (long-only tilt), ~0.8-1.2 (long/short)
```

---

## 2. Smart Beta Product Design

Creating investable index products that deliver factor exposure in a transparent, low-cost, and scalable format.

### Index Construction Rules

```
I'm designing a smart beta index product for [factor/strategy]:

Product structure: [ETF / index fund / separate account]
Target index: [name]
Benchmark: [parent index, e.g., S&P 500]
Fee: [X] bps
Expected tracking error vs parent index: [X]%

Help me define the complete index methodology:

1. **Eligible universe**: [parent index] constituents, minimum market cap $[X]B, minimum ADV $[X]M
2. **Factor scoring**: Precise definition of each signal, data sources, calculation frequency
3. **Weighting scheme**: [factor-score-weighted / equal-weight / capped-factor-weight / risk-weighted]
   - Cap maximum stock weight at [X]% to limit concentration
4. **Rebalancing rules**: Frequency, buffer zones (e.g., stock stays in if rank < [X]+20%),
   reconstitution vs weight adjustment events
5. **Turnover budget**: Target one-way turnover < [X]% per rebalance
   - Buffer rule: Only trade if new score crosses threshold by > [X] standard deviations
6. **Index governance**: Methodology committee, discretionary overrides (avoid or allow?),
   corporate action treatment (M&A, spin-offs, delistings)
7. **Backtested performance**: 20-year backtest with [live/simulated] data
   - Annualized return: [X]%, volatility: [X]%, Sharpe: [X]
   - Maximum drawdown: [X]%, turnover: [X]%
   - Factor exposure (regression): target factor loading = [X], t-stat = [X]
8. **Capacity estimate**: At $[X]B AUM, what is the expected implementation shortfall vs index?

Key design tradeoff: Tighter factor exposure = higher turnover = higher costs.
Looser factor exposure = lower turnover = diluted factor premium.
```

---

## 3. Factor Timing and Regime Analysis

Dynamically adjusting factor allocations based on macroeconomic regimes, valuation spreads, and crowding signals.

### Factor Timing Framework

```
I want to evaluate whether to tactically tilt my factor allocations:

Current factor allocation: [value X%, momentum X%, quality X%, low vol X%, size X%]
Current market regime: [expansion / late cycle / recession / recovery]

Factor timing signals to evaluate:

1. **Valuation spreads**: Is the value factor "cheap" or "expensive"?
   - Long-short value spread: Top quintile B/M = [X]x, Bottom quintile B/M = [X]x
   - Current spread percentile vs 30-year history: [X]th percentile
   - Wide spreads historically predict stronger value factor returns over 1-3 years
2. **Macro regime**: Map business cycle to factor performance
   - Early recovery: Value, size outperform (mean-reversion after distress)
   - Mid-cycle expansion: Momentum outperforms (trends persist)
   - Late cycle: Quality, low vol outperform (defensive positioning)
   - Recession: Low vol, quality outperform; value, momentum underperform
3. **Factor momentum**: 12-month trailing factor return as a timing signal
   - Factor momentum Sharpe ~0.3-0.5 (Gupta & Kelly, 2019)
4. **Crowding metrics**: Are factors over-owned?
   - Pairwise correlation of factor portfolio holdings (high = crowded)
   - Short interest concentration in factor shorts
   - Factor ETF flow data (extreme inflows = potential crowding)
5. **Sentiment and positioning**: CFTC positioning, fund flow data, options skew

Timing budget: Constrain tactical tilts to +/- [X]% from strategic weights.
Timing adds ~0.1-0.3 Sharpe if done well, but subtracts if done poorly.
Transaction cost of rebalancing must be lower than expected timing alpha.
```

---

## 4. Risk Premia Harvesting

Capturing factor premia across asset classes beyond equities — carry, momentum, value, and volatility across fixed income, FX, commodities, and rates.

### Cross-Asset Risk Premia Portfolio

```
I want to build a cross-asset risk premia portfolio harvesting systematic premia:

Asset classes: [equities, fixed income, FX, commodities, rates, credit]
Target volatility: [X]%
Leverage constraints: [notional cap, margin requirements]

Risk premia to harvest:

1. **Carry**: Long high-yield, short low-yield assets
   - FX carry: Long high-rate currencies, short low-rate (Sharpe ~0.3-0.5 pre-2008, ~0.2 post)
   - Fixed income carry: Roll-down + coupon, optimized across the curve
   - Commodity carry: Long backwardated, short contango (roll yield)
2. **Momentum**: Long recent winners, short recent losers (time-series or cross-sectional)
   - Equity index momentum: 12-1 month returns (Sharpe ~0.4)
   - Commodity momentum: 12-month trend (Sharpe ~0.4-0.6)
   - FX momentum: 3-12 month trends (Sharpe ~0.2-0.4)
3. **Value**: Long cheap, short expensive relative to fundamentals
   - FX value: PPP-based valuation (Sharpe ~0.2, very slow convergence)
   - Equity value: Cross-country CAPE-based allocation
   - Commodity value: 5-year z-score of real price
4. **Volatility risk premium**: Sell options/variance, earn the vol risk premium
   - Equity vol selling: Put writing, short variance swaps (Sharpe ~0.4-0.6 but fat left tail)

Help me:
1. Estimate expected Sharpe of each premia in the current environment
2. Build the correlation matrix across premia (low correlation = high diversification)
3. Allocate using risk parity: equal risk contribution from each premium
4. Size the total portfolio to target vol, accounting for leverage constraints
5. Design a crash protection overlay: when do these premia fail simultaneously?
   - Carry + vol selling = correlated drawdown in risk-off events
   - Momentum = standalone, but can fail in V-shaped reversals
```

---

## 5. Factor Crowding Analysis

Monitoring concentration of capital in factor strategies and assessing the risk of crowding-driven drawdowns.

### Crowding Detection Framework

```
I need to assess whether the [factor] factor is crowded in [universe]:

Crowding indicators to evaluate:

1. **Pairwise correlation of factor portfolios**: If many managers hold similar factor portfolios,
   pairwise correlations of top-quintile stocks increase
   - Measure: Average pairwise return correlation of top-quintile stocks (current vs historical)
   - Threshold: > 0.5 average pairwise correlation = elevated crowding risk

2. **Short interest concentration**: Factor short legs accumulate short interest
   - Short interest as % of float for bottom-quintile value/momentum stocks
   - Cost to borrow for factor short portfolios (rising borrow cost = crowding)

3. **Valuation of factor portfolios**: Has capital inflow compressed the factor premium?
   - Long leg P/E, P/B, FCF yield vs history — are factor longs getting expensive?
   - Factor valuation spread: current premium vs 10-year average

4. **ETF flow analysis**: Are factor ETF inflows at extreme levels?
   - 3-month cumulative flows as % of AUM for [value / momentum / quality / low vol] ETFs
   - Extreme inflows = future underperformance (Arnott et al., 2016)

5. **Factor return autocorrelation**: Crowded factors show negative return autocorrelation
   at short horizons (momentum crashes, value traps)
   - Lag-1 monthly autocorrelation of factor returns: current vs historical

Help me:
1. Score each crowding indicator (1-5 scale) and compute composite crowding score
2. Estimate the conditional drawdown risk if the factor unwinds (historical analogs)
3. Recommend hedging strategies: options on factor ETFs, cross-factor diversification, dynamic sizing
4. Identify early warning signals for factor unwinds (quant quake indicators)

Historical crowding events to reference:
- August 2007 quant quake (factor momentum reversal, unwinding of stat arb)
- March 2020 momentum crash (fastest-ever factor rotation)
- Late 2020 value rotation (vaccine announcement triggered massive value rally)
```

---

## Mathematical Reference

**Fama-French 5-Factor Model:**
R_i - R_f = a_i + b1*MktRf + b2*SMB + b3*HML + b4*RMW + b5*CMA + e_i

**Carhart 4-Factor (adds momentum to FF3):**
R_i - R_f = a_i + b1*MktRf + b2*SMB + b3*HML + b4*UMD + e_i

**Factor Exposure Regression (time-series):**
R_portfolio_t = alpha + sum_k(beta_k * F_k_t) + epsilon_t
- alpha = unexplained return (skill or missing factor)
- beta_k = portfolio's exposure to factor k
- R-squared = fraction of return variance explained by factors

**Factor Attribution (holdings-based):**
Factor_exposure_k = sum_i(w_i * z_ik) where z_ik = stock i's standardized score on factor k
Active_factor_exposure_k = sum_i((w_pi - w_bi) * z_ik)

**Factor Portfolio Turnover Cost:**
Net_premium = gross_premium - (annual_turnover x avg_one_way_cost)
Capacity = gross_premium / (2 x turnover x marginal_impact_per_dollar)

**Information Ratio of Factor Strategy:**
IR_factor = mean(factor_return) / std(factor_return)
Annualized: IR_annual = IR_monthly x sqrt(12)

---

## See Also

- [Active Equity](active-equity.md) — fundamental stock selection that often carries implicit factor bets
- [Risk & Performance Analytics](risk-analytics.md) — factor risk decomposition and attribution frameworks
- [Multi-Asset Allocation](multi-asset.md) — factor premia as building blocks for strategic allocation
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — alpha research, signal generation, and statistical testing
