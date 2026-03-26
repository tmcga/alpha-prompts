# Multi-Asset Strategies & Allocation

```
You are a senior multi-asset portfolio strategist at a large institutional asset manager
overseeing $50-500B in diversified portfolios. You are responsible for strategic asset
allocation, tactical tilts, model portfolio design, and capital market assumptions. You
think in terms of long-term expected returns, risk budgets, correlation regimes, and the
full opportunity set across equities, fixed income, real assets, and alternatives. You
use mean-variance optimization, Black-Litterman, and risk parity as complementary tools,
understanding the strengths and limitations of each. Your clients range from sovereign
wealth funds with 30-year horizons to retirement savers needing a glide path. You are
intensely focused on implementation costs, tax efficiency, rebalancing discipline, and
translating complex optimization outputs into investable portfolios.
```

## What This Desk Does

The multi-asset team sets the top-level allocation framework that determines how capital is divided across asset classes, geographies, styles, and implementation vehicles. This is the highest-leverage decision in investment management — academic research consistently shows that asset allocation explains 85-95% of portfolio return variation over time. The team builds capital market assumptions (10-year return, risk, and correlation forecasts), runs optimization models to derive strategic allocations, overlays tactical tilts based on shorter-term signals, and constructs model portfolios that translate these views into specific fund and ETF selections. Multi-asset portfolios serve as the default option for most investors, including target-date funds (the largest single category in US retirement), balanced funds, and outsourced CIO (OCIO) mandates.

---

## 1. Strategic Asset Allocation

Determining the long-term policy portfolio based on capital market assumptions, risk tolerance, and investment horizon.

**Mean-Variance Optimization (Markowitz):**
Minimize: (1/2) x w' x Sigma x w - lambda x w' x mu
Subject to: w' x 1 = 1, w >= 0 (if long-only)
Solution (unconstrained): w* = (1/lambda) x Sigma_inv x mu

**Black-Litterman Equilibrium Returns:**
pi = lambda x Sigma x w_mkt (implied returns from market cap weights)
mu_BL = [(tau*Sigma)^-1 + P'*Omega^-1*P]^-1 x [(tau*Sigma)^-1*pi + P'*Omega^-1*Q]

Where: P = view pick matrix, Q = view returns, Omega = view uncertainty, tau = scalar (~0.05).

### Strategic Allocation Optimization

```
I need to build a strategic asset allocation for a [client type: pension / endowment / SWF / individual]:

Investment horizon: [X] years
Return objective: [X]% nominal / [X]% real (above inflation)
Risk tolerance: [X]% maximum drawdown, [X]% annualized volatility target
Liability stream: [describe if applicable — pension payments, endowment spending rule]
Liquidity requirements: [X]% available within 30 days, [X]% within 1 year
Regulatory/policy constraints: [describe — e.g., max 60% equity, min 20% IG bonds, max 15% alternatives]

Asset class menu:
- US Large Cap Equity: Expected return [X]%, volatility [X]%
- US Small Cap Equity: Expected return [X]%, volatility [X]%
- International Developed Equity: Expected return [X]%, volatility [X]%
- Emerging Markets Equity: Expected return [X]%, volatility [X]%
- US Aggregate Bonds: Expected return [X]%, volatility [X]%
- US Long Government/Credit: Expected return [X]%, volatility [X]%
- US High Yield: Expected return [X]%, volatility [X]%
- EM Debt: Expected return [X]%, volatility [X]%
- Real Estate (REITs): Expected return [X]%, volatility [X]%
- Private Equity: Expected return [X]%, volatility [X]%
- Hedge Funds: Expected return [X]%, volatility [X]%
- Commodities: Expected return [X]%, volatility [X]%
- TIPS: Expected return [X]%, volatility [X]%

Correlation matrix: [provide or use standard assumptions]

Help me:
1. **Mean-variance efficient frontier**: Calculate and plot the efficient frontier
   - Identify minimum variance portfolio, maximum Sharpe portfolio, and target-return portfolio
2. **Black-Litterman adjustment**: Start with market-cap equilibrium returns, overlay my views
   - View 1: [asset class] will outperform by [X]% with [X]% confidence
   - View 2: [describe relative or absolute view]
3. **Robust optimization**: Apply resampling or worst-case optimization to handle estimation error
   - Resampled efficient frontier (Michaud): average weights across bootstrapped efficient frontiers
4. **Risk budgeting**: Allocate risk (not capital) across asset classes
   - Risk contribution: RC_i = w_i x (Sigma x w)_i / sqrt(w' x Sigma x w)
   - Ensure no single asset class dominates total risk
5. **Implementation overlay**: How to access each asset class (active vs passive, commingled vs SMA)
6. **Rebalancing policy**: Calendar vs threshold-based, tax implications, transaction costs

Output: Recommended strategic allocation with expected return, volatility, Sharpe ratio,
max drawdown estimate, and 95% VaR.
```

---

## 2. Tactical Asset Allocation

Short- to medium-term deviations from strategic weights based on valuation, macro, sentiment, and momentum signals.

### Tactical Overlay Framework

```
I want to implement tactical tilts on top of my strategic allocation:

Strategic weights: [list asset class weights]
Tactical deviation budget: +/- [X]% per asset class, total absolute deviation <= [X]%
Rebalancing frequency: [monthly / quarterly]
Tracking error budget for tactical overlay: [X] bps

Tactical signals I'm evaluating:

1. **Valuation signals** (12-36 month horizon):
   - Equity CAPE (Shiller P/E): US = [X]x (percentile: [X]th), EAFE = [X]x, EM = [X]x
   - Credit spreads vs fair value: IG at [X] bps ([X]th percentile), HY at [X] bps
   - Yield vs expected inflation: Real yields at [X]% (percentile: [X]th)

2. **Macro signals** (3-12 month horizon):
   - PMI / ISM: [X] (above/below 50), direction: [improving/deteriorating]
   - Yield curve slope: 2s10s at [X] bps, 3m10y at [X] bps
   - Credit impulse: [positive/negative], magnitude: [X]% of GDP
   - Earnings revision ratio: [X]% (above/below 1.0)

3. **Momentum signals** (1-12 month horizon):
   - 12-month asset class returns: equities [X]%, bonds [X]%, commodities [X]%
   - Cross-asset time-series momentum: long above-trend, short below-trend

4. **Sentiment/positioning** (1-3 month horizon, contrarian):
   - Fund flows: equity funds [inflows/outflows], bond funds [inflows/outflows]
   - VIX level: [X] (percentile: [X]th), MOVE index: [X]
   - AAII bull/bear ratio: [X]

Help me:
1. Score each signal (z-score or percentile) and combine into a composite tactical signal per asset class
2. Translate signals into position sizes: delta_w = signal_strength x max_deviation x conviction
3. Estimate expected alpha from tactical overlay (historically ~0-50 bps/year from TAA)
4. Assess signal interaction: Are valuation and momentum aligned or conflicting?
5. Risk check: Does the tactical overlay create unintended factor exposures?
6. Transaction cost drag: Is the expected tactical alpha > rebalancing costs?
```

---

## 3. Target-Date Fund Design

Constructing age-based glide paths that evolve from growth-oriented to income-oriented as participants approach and enter retirement.

### Glide Path Construction

```
I'm designing a target-date fund suite for a [401k / IRA / DC pension] platform:

Product lineup: Target dates from [2030] to [2065] in 5-year increments
Total AUM: $[X]B across all vintages
Fee target: [X] bps (all-in)

Design parameters:
- Starting equity allocation (40 years to retirement): [X]%
- Equity allocation at retirement (age 65): [X]%
- Terminal equity allocation (age 85+): [X]%
- "To" vs "Through" retirement: [to = most derisking by retirement / through = continues after]
- Maximum drawdown tolerance at retirement: [X]%

Help me design:
1. **Glide path shape**: Linear, convex, or concave derisking?
   - Human capital argument: Young workers have bond-like human capital -> high equity appropriate
   - Sequence-of-returns risk: Largest risk at retirement -> rapid derisking in final 10 years
   - Convex path: Slow reduction early (40-55), rapid reduction late (55-70), flat in retirement
2. **Equity sub-allocation along the path**:
   - Young: Higher international, EM, small cap (growth-oriented, long horizon)
   - Near retirement: More US large cap, dividend, low vol (stability-oriented)
3. **Fixed income evolution**:
   - Young: TIPS, short-duration (inflation protection, low interest rate risk)
   - Mid-career: Core aggregate (diversification)
   - Retirement: Long-duration, income-oriented, TIPS ladder for real income
4. **Alternatives inclusion**: Real assets (REITs, commodities) for inflation protection
   - Allocate [X]% to real assets for participants > 20 years from retirement
5. **Risk analysis at each point on the glide path**:
   - Expected return, volatility, max drawdown (95th percentile), probability of shortfall
   - Monte Carlo simulation: % of scenarios meeting [X]% replacement rate at retirement
6. **Implementation**: Passive core with active satellite? All-passive? Index fund selection.

Key metric: Funded ratio at retirement = portfolio value / PV(retirement spending needs).
Target: > 80% probability of funding 30 years of retirement spending at 4% withdrawal rate.
```

---

## 4. Model Portfolio Construction

Building implementable model portfolios for wealth management platforms with specific fund/ETF selections.

### Core-Satellite Model Portfolio

```
Build a model portfolio for a [risk profile: conservative / moderate / growth / aggressive] investor:

Risk profile parameters:
- Target return: [X]% nominal
- Volatility tolerance: [X]%
- Maximum drawdown tolerance: [X]%
- Investment horizon: [X] years
- Tax status: [taxable / tax-deferred / tax-exempt]
- Minimum investment: $[X]

Strategic allocation (from SAA process):
- US Equity: [X]%, International Equity: [X]%, EM Equity: [X]%
- US Bonds: [X]%, International Bonds: [X]%, TIPS: [X]%
- Real Assets: [X]%, Alternatives: [X]%, Cash: [X]%

Help me construct:
1. **Core allocation (60-80% of portfolio)**: Low-cost passive index funds/ETFs
   - Selection criteria: Expense ratio < [X] bps, tracking error < [X] bps, AUM > $[X]B
   - Fund recommendations for each core asset class with ER, TE, and tax efficiency comparison
2. **Satellite allocation (20-40%)**: Active managers or thematic ETFs with alpha potential
   - Criteria: Information ratio > [X], consistent track record > [X] years, reasonable fees
   - Identify asset classes where active management adds value (EM, small cap, credit)
3. **Tax optimization** (for taxable accounts):
   - Tax-loss harvesting pairs (primary and secondary ETF for each asset class)
   - Municipal bonds vs taxable bonds: breakeven tax rate analysis
   - Asset location: Place tax-inefficient assets (HY, REITs, active strategies) in tax-deferred
4. **Rebalancing rules**:
   - Threshold: Rebalance when any asset class drifts > [X]% from target
   - Tax-aware: Rebalance using new contributions and withdrawals first (avoid realizing gains)
   - Calendar overlay: Review at least [quarterly / semi-annually]
5. **Fee budget**: Total portfolio weighted expense ratio = [X] bps
   - Core: [X] bps average, Satellite: [X] bps average, Blended: [X] bps
6. **Monitoring and governance**: Benchmark for total portfolio, trigger for fund replacement
```

---

## 5. Capital Market Assumptions

Building the long-term return, risk, and correlation forecasts that underpin all allocation decisions.

### 10-Year CMA Framework

```
I need to build 10-year capital market assumptions for our annual allocation review:

Current market data:
- US 10y Treasury yield: [X]%
- US equity earnings yield (1/CAPE): [X]%
- IG credit spread: [X] bps
- HY credit spread: [X] bps
- US inflation expectations (10y breakeven): [X]%
- Dividend yield (S&P 500): [X]%
- Buyback yield (S&P 500): [X]%

Help me build CMAs using building-block methodology:

1. **Fixed income expected returns**:
   - US Aggregate = current yield + roll-down - expected default losses +/- duration gain/loss
   - IG corporates = Treasury yield + OAS - expected default loss (IG avg default ~0.1%/yr)
   - HY = Treasury yield + OAS - expected default loss (HY avg ~3-4%/yr x (1 - recovery ~40%))
   - TIPS = real yield + inflation expectation

2. **Equity expected returns (building blocks)**:
   - E[R_equity] = dividend yield + buyback yield + earnings growth + valuation change
   - Earnings growth = real GDP growth + inflation + margin expansion/compression
   - Valuation change = (target_CAPE / current_CAPE)^(1/10) - 1
   - International: Same framework, adjust for currency and relative valuation

3. **Alternatives expected returns**:
   - Private equity = public equity + illiquidity premium (200-400bps) - fees (300-500bps)
   - Real estate = cap rate + NOI growth - capex
   - Hedge funds = risk-free + alpha expectation (reduced by fee drag)
   - Commodities = roll yield + spot return (inflation hedge, no income)

4. **Risk estimates**: Use 15-20 year realized volatility, adjust for current regime
   - Equity vol: ~15-17%, Bond vol: ~4-6%, Credit vol: ~6-10%

5. **Correlation matrix**: Estimate from 15-20 year rolling windows
   - Key: Stock-bond correlation (currently [positive/negative], historical regime shifts)
   - Stress correlation adjustment: Correlations increase in tail events

6. **Geometric vs arithmetic returns**: Geo = Arith - (vol^2 / 2) approximately
   - Use geometric returns for wealth accumulation, arithmetic for single-period optimization

Output: Full CMA table with expected return (geometric), volatility, Sharpe ratio for each
asset class, plus full correlation matrix.
```

---

## Mathematical Reference

**Mean-Variance Optimization:**
max: w'*mu - (lambda/2)*w'*Sigma*w subject to w'*1 = 1, w >= 0
Unconstrained solution: w* = (1/lambda) * Sigma^-1 * mu

**Black-Litterman:**
Equilibrium returns: pi = lambda * Sigma * w_mkt
Combined returns: mu_BL = [(tau*Sigma)^-1 + P'*Omega^-1*P]^-1 * [(tau*Sigma)^-1*pi + P'*Omega^-1*Q]
- tau ~ 0.05 (scalar, confidence in equilibrium)
- P = K x N view pick matrix (K views on N assets)
- Q = K x 1 vector of view returns
- Omega = K x K diagonal matrix of view uncertainties

**Risk Parity:**
Equal risk contribution: w_i * (Sigma*w)_i = w_j * (Sigma*w)_j for all i,j
Simplified (diagonal Sigma): w_i proportional to 1/sigma_i

**Sharpe Ratio Optimization:**
max: (w'*mu - r_f) / sqrt(w'*Sigma*w)
Equivalent to tangency portfolio on efficient frontier.

**Geometric Return Approximation:**
E[R_geometric] = E[R_arithmetic] - sigma^2 / 2
This matters: 10% arithmetic with 20% vol -> ~8% geometric.

**Rebalancing Bonus:**
Diversification return from rebalancing = (1/2) * sum(w_i * sigma_i^2) - (1/2) * sigma_portfolio^2
This is the "volatility harvesting" benefit of disciplined rebalancing (~20-50 bps/year).

---

## See Also

- [Active Equity](active-equity.md) — active equity mandates within the multi-asset structure
- [Fixed Income Asset Management](fixed-income-am.md) — fixed income allocation detail and LDI
- [Alternatives Allocation](alternatives-allocation.md) — PE, hedge funds, real assets in the total portfolio
- [Risk & Performance Analytics](risk-analytics.md) — total portfolio risk decomposition and scenario analysis
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — portfolio construction math, risk parity, and Black-Litterman detail
