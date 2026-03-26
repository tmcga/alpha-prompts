# Hedge Fund Analyst

Prompt library for systematic and discretionary hedge fund analysts. Covers alpha research, portfolio construction, risk attribution, and the quantitative frameworks used at multi-strategy funds.

## Role Context

```
You are a senior quantitative analyst at a multi-strategy hedge fund. You think in terms of
risk-adjusted returns, factor exposures, and capacity constraints. Every trade idea must have
a clearly defined edge, a sizing framework, and a kill criterion. You are skeptical of
backtests and always ask about regime dependence, survivorship bias, and transaction costs.
```

---

## 1. Alpha Research & Signal Generation

### Generate a New Trading Signal

```
I'm researching a new alpha signal for [asset class: equities / crypto / futures / macro].

Hypothesis: [describe your edge, e.g. "post-earnings drift is under-exploited in mid-cap equities"]

For this signal, help me design:

1. **Signal construction**: What raw data do I need? How do I transform it into a standardized signal (-1 to +1)?
2. **Decay analysis**: What's the expected half-life of this signal? How quickly should I expect alpha to decay after entry?
3. **Orthogonality**: How do I test whether this signal is genuinely new vs. a repackaged momentum/value/quality factor?
4. **Universe selection**: Which instruments should this signal trade, and which should it avoid?
5. **Capacity estimate**: At what AUM does this signal's alpha degrade due to market impact?

Mathematical framework to use:
- Information coefficient (IC) and IC information ratio (IC_IR)
- Turnover-adjusted Sharpe: Sharpe_net = Sharpe_gross - (turnover × cost_per_turn)
- Factor regression: r_signal = alpha + beta_mkt × r_mkt + beta_mom × r_mom + ... + epsilon
```

### Cross-Sectional Signal Analysis

```
I have a cross-sectional signal scored across [N] instruments in [asset class].

Signal characteristics:
- Mean IC: [X]
- IC standard deviation: [X]
- Monthly turnover: [X]%
- Average holding period: [X] days

Using the Fundamental Law of Active Management:
  IR = IC × sqrt(BR)
where BR (breadth) = number of independent bets per year.

Help me:
1. Estimate the expected IR given my IC and breadth
2. Determine if the IC is statistically significant (t-stat = IC_mean / IC_std × sqrt(N_months))
3. Calculate the optimal leverage given my risk budget
4. Identify whether my signal is crowded (correlation with common factors)
5. Design a proper out-of-sample test that avoids look-ahead bias
```

---

## 2. Portfolio Construction

### Mean-Variance Optimization

```
I'm constructing a portfolio from [N] assets/strategies with the following inputs:

Expected returns (annualized): [list or describe]
Covariance matrix source: [sample, shrinkage (Ledoit-Wolf), factor model]
Constraints: [long-only / long-short, max position size, sector limits, turnover limits]

Help me:
1. Set up the optimization: minimize w'Σw subject to w'μ ≥ target_return, constraints
2. Apply Black-Litterman to blend my views with market equilibrium returns
3. Use shrinkage estimation for the covariance matrix (Ledoit-Wolf or Oracle Approximating)
4. Implement robust optimization to account for estimation error in μ and Σ
5. Calculate the efficient frontier and identify the maximum Sharpe portfolio

Key formulas:
- Optimal weights (unconstrained): w* = (1/λ) × Σ⁻¹ × μ
- Black-Litterman: μ_BL = [(τΣ)⁻¹ + P'Ω⁻¹P]⁻¹ × [(τΣ)⁻¹π + P'Ω⁻¹Q]
  where π = equilibrium returns, P = view matrix, Q = view returns, Ω = view uncertainty
- Risk contribution: RC_i = w_i × (Σw)_i / (w'Σw)
```

### Risk Parity Construction

```
I want to build a risk parity portfolio across [N] assets/strategies.

Asset classes and approximate volatilities:
- [Asset 1]: [vol]%
- [Asset 2]: [vol]%
- [Asset N]: [vol]%

Help me:
1. Calculate inverse-volatility weights as a starting point
2. Solve for true risk parity: each asset contributes equally to portfolio variance
   - Objective: minimize Σ(RC_i - RC_target)² where RC_i = w_i × (Σw)_i / σ_portfolio
3. Decide whether to lever the portfolio to a target volatility
4. Compare risk parity vs. equal weight vs. mean-variance for this asset mix
5. Address the criticism: risk parity over-allocates to bonds in low-rate environments
```

---

## 3. Risk Management & Attribution

### Factor Risk Decomposition

```
My portfolio has the following characteristics:
- Gross exposure: [X]%
- Net exposure: [X]%
- Number of positions: [N]
- Strategy type: [long-short equity / macro / stat arb / multi-strategy]

Recent performance:
- MTD return: [X]%
- YTD return: [X]%
- Current drawdown from peak: [X]%

Help me decompose risk and P&L:
1. Factor attribution: What portion of returns came from market beta, sector, size, value, momentum, volatility, and idiosyncratic alpha?
2. Marginal risk contribution: Which positions are contributing most to portfolio variance?
3. Stress testing: Model portfolio P&L under:
   - 2008 GFC scenario (equities -40%, credit spreads +500bps, vol spike to 80)
   - 2020 COVID crash (equities -35% in 3 weeks, then V-recovery)
   - Rate shock (+200bps parallel shift in yield curve)
   - Liquidity crisis (bid-ask spreads widen 5x, can only liquidate 10%/day)
4. Tail risk: Estimate portfolio VaR (95%, 99%) and CVaR using historical simulation
5. Correlation breakdown: Which position pairs become more correlated in drawdowns?
```

### Drawdown Analysis

```
My strategy is in a drawdown:
- Peak equity: [X]
- Current equity: [X]
- Drawdown: [X]%
- Duration: [X] days
- Strategy type: [describe]
- Historical max drawdown: [X]%
- Historical average recovery time: [X] days

Help me think through:
1. Is this drawdown within the expected distribution? (Compare to historical DD distribution, not just max)
2. Has the signal's IC degraded, or is this normal variance around a positive-expectancy process?
3. Should I reduce risk? Framework: Kelly criterion says optimal f* = edge/odds. If edge has decreased, optimal sizing decreases proportionally.
4. What's the probability of recovery within [X] months given historical drawdown patterns?
5. Kill criteria: At what point should I shut down the strategy vs. ride it out?
```

---

## 4. Statistical Testing

### Strategy Validation

```
I've backtested a strategy and want to validate it before allocating capital.

Backtest results:
- Period: [start] to [end]
- Sharpe ratio: [X]
- Number of trades: [X]
- Parameters optimized: [X] parameters over [X] combinations

Help me apply proper statistical rigor:
1. Multiple testing correction: With [N] strategies/parameters tested, what's the adjusted significance threshold?
   - Bonferroni: α_adj = α / N
   - Holm-Bonferroni (step-down, less conservative)
   - False Discovery Rate (Benjamini-Hochberg) for large strategy sets
2. Deflated Sharpe Ratio (Bailey & Lopez de Prado):
   SR* = (SR - SR_0) / sqrt((1 - skew×SR + ((kurtosis-1)/4)×SR²) / T)
   where SR_0 accounts for the number of trials
3. Minimum backtest length: T_min = (1 + (1-skew×SR + ((kurt-1)/4)×SR²)) × (z_α / SR)²
4. Walk-forward validation: How should I split in-sample vs. out-of-sample?
5. Combinatorial purged cross-validation (CPCV) for time series without leakage
```

---

## 5. Execution & Market Microstructure

### Transaction Cost Analysis

```
My strategy trades [asset class] with:
- Average daily volume of target instruments: [X]
- Average position size: [X]% of ADV
- Holding period: [X] days
- Monthly turnover: [X]%

Help me model realistic execution costs:
1. Spread cost: half-spread × 2 (round trip)
2. Market impact: Almgren-Chriss model
   - Temporary impact: η × (v/V)^δ where v = trade rate, V = market volume
   - Permanent impact: γ × (v/V)^β
3. Timing cost: slippage from decision price to execution price
4. Opportunity cost: alpha lost from not trading the full desired size
5. Net Sharpe after costs: How much does my Sharpe degrade at [X] AUM vs. [10X] AUM?
```
