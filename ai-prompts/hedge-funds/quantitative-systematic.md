# Quantitative / Systematic Strategies

## Role Context

```
You are a senior quantitative researcher at a systematic trading firm managing $20B across
equity stat-arb, futures momentum, and multi-asset factor strategies. You think in terms of
information coefficients, signal decay, and the Fundamental Law of Active Management. Every
signal must survive rigorous out-of-sample testing, multiple testing correction, and realistic
transaction cost modeling before it earns a dollar of capital. You are deeply aware that most
backtested alpha is illusory -- the product of overfitting, survivorship bias, or ignoring
market impact. You demand t-statistics above 3.0 for new signals, use combinatorial purged
cross-validation, and size strategies using the Kelly criterion adjusted for parameter
uncertainty. You never confuse in-sample performance with out-of-sample expectation.
```

---

## What This Desk Does

Quantitative systematic strategies use statistical models to identify, size, and execute trading signals across large instrument universes with minimal human intervention. The edge comes from breadth -- trading hundreds or thousands of instruments with small, repeatable edges -- rather than from deep conviction on any single name. Strategies include cross-sectional equity factors (value, momentum, quality), time-series momentum in futures, statistical arbitrage (mean reversion of cointegrated pairs), and machine-learning-driven signals. The research process is hypothesis-driven: define a signal, test it rigorously for statistical significance, model transaction costs, estimate capacity, and deploy with strict risk limits. Portfolio construction uses optimization frameworks that maximize expected return per unit of risk subject to turnover, factor exposure, and concentration constraints.

---

## 1. Alpha Signal Research

### Design and Test a New Alpha Signal

```
I'm researching a new alpha signal for [asset class / universe]:

Signal hypothesis: [describe the economic intuition, e.g., "stocks with improving cash
conversion cycles outperform because the market underweights balance sheet quality changes"]

Raw data source: [describe data: fundamental, alternative, technical, sentiment]
Signal transformation: [how raw data becomes a z-scored signal, e.g., cross-sectional rank,
time-series z-score, percentile, composite]

Help me construct and validate this signal:

1. **Feature engineering**:
   - Raw feature: [describe]
   - Transformations to test: rank, z-score, winsorize (at [X] sigma), normalize by sector
   - Lag structure: Test signal at t-1, t-5, t-21 (avoid look-ahead bias)
   - Composite construction: If combining sub-signals, use [equal weight / IC-weight / PCA]

2. **Signal quality metrics**:
   - Information Coefficient: IC = corr(signal_t, return_t+1)
     Target: IC > 0.02 for daily, > 0.05 for monthly
   - IC Information Ratio: IC_IR = mean(IC) / std(IC)
     Target: IC_IR > 0.5
   - IC autocorrelation: High autocorrelation = slow-decaying signal (good for low turnover)
   - Quantile spread: Long top quintile, short bottom quintile. Monotonic spread across quintiles?

3. **Decay analysis**:
   - Measure IC at horizons: 1d, 5d, 21d, 63d
   - Half-life of signal: At what horizon does IC drop to 50% of peak?
   - Turnover implied by decay: Faster decay = higher turnover = more transaction cost drag
   - Optimal holding period: Maximize IC(h) - cost(h) where cost increases with turnover

4. **Orthogonality to known factors**:
   - Regress signal returns on Fama-French 5 factors + Momentum:
     r_signal = alpha + b1*MKT + b2*SMB + b3*HML + b4*RMW + b5*CMA + b6*UMD + epsilon
   - Is alpha statistically significant after controlling for known factors? (t-stat > 2.0)
   - If not, this signal is a repackaged known factor, not new alpha

5. **Capacity estimation**:
   - At what AUM does market impact consume the alpha?
   - Sharpe decay with AUM: SR(AUM) = SR_0 x (1 - AUM / Capacity)
   - Capacity = (Alpha x ADV_universe) / (Impact_coefficient x Turnover)
   - Rule of thumb: If you trade X% of ADV, expect 0.5*X% market impact per side
```

### Signal Combination and Portfolio Alpha

```
I have [N] alpha signals for [universe] that I want to combine into a composite signal:

Signal characteristics:
| Signal | IC | IC_IR | Turnover | Correlation to Signal 1 | Decay (half-life) |
|--------|-----|-------|----------|------------------------|-------------------|
| Signal 1 | [X] | [X] | [X]% | 1.00 | [X] days |
| Signal 2 | [X] | [X] | [X]% | [X] | [X] days |
| Signal N | [X] | [X] | [X]% | [X] | [X] days |

Fundamental Law of Active Management:
  IR = IC x sqrt(BR)
  where BR = number of independent bets per year

For a composite signal:
  IC_composite = w' x IC_vector (weighted average IC)
  BR_composite accounts for correlation between signals reducing effective breadth

Help me:
1. Optimal signal weights: Maximize composite IC_IR, not just IC
2. Account for signal correlation: Diversification benefit from combining low-correlated signals
3. Turnover budget: Composite turnover must stay below [X]% monthly to keep costs manageable
4. Rebalance frequency: Align with slowest-decaying signal or use staggered rebalance
5. Expected portfolio IR after costs:
   IR_net = IC_composite x sqrt(BR_effective) - Turnover x Cost_per_turn
```

---

## 2. Backtesting Rigor

### Validate a Backtest with Proper Statistical Methods

```
I've backtested a strategy with these results:

Backtest period: [start] to [end] ([X] years)
Sharpe ratio (gross): [X]
Sharpe ratio (net of estimated costs): [X]
Number of trades: [X]
Win rate: [X]%
Average holding period: [X] days
Number of parameters optimized: [P]
Number of strategy variants tested: [N]
Skewness of returns: [X]
Kurtosis of returns: [X]

Apply rigorous statistical validation:

1. **Minimum required Sharpe for significance**:
   t-stat = SR x sqrt(T) where T = years of data
   Require t-stat > 3.0 (not 2.0) because:
   - Multiple testing: We tested [N] variants, so the effective bar is higher
   - Non-normal returns: Fat tails inflate apparent Sharpe
   - Regime specificity: The backtest period may not represent future regimes

2. **Deflated Sharpe Ratio** (Bailey & Lopez de Prado):
   SR* = (SR_observed - SR_0) / sqrt(V[SR])
   where:
   - SR_0 = expected max Sharpe from [N] independent trials of zero-alpha strategies
     SR_0 ~ sqrt(2 x ln(N)) x (1 - gamma) + gamma x sqrt(2 x ln(N))  (approx)
   - V[SR] = (1 - skew*SR + ((kurt-1)/4)*SR^2) / T
   - If SR* < critical value, the observed Sharpe is likely noise

3. **Multiple testing correction**:
   - Bonferroni: p_adjusted = p x N (conservative, controls family-wise error rate)
   - Holm-Bonferroni: Step-down procedure, less conservative than Bonferroni
   - Benjamini-Hochberg: Controls false discovery rate -- appropriate when testing many signals
   - Practical rule: If you tested 100 variants, a Sharpe of 2.0 is NOT impressive

4. **Walk-forward validation**:
   - Split data: [60%] in-sample, [20%] validation, [20%] out-of-sample
   - In-sample: Fit parameters
   - Validation: Select best model (this consumes some out-of-sample validity)
   - Out-of-sample: Final unbiased performance estimate (NEVER re-optimize on this set)
   - Rolling walk-forward: Retrain every [X] months on expanding or rolling window

5. **Combinatorial Purged Cross-Validation (CPCV)**:
   - Split time series into [K] non-overlapping blocks
   - For each combination of training/test blocks, purge observations near boundaries
   - Embargo period: [X] days after each training block to prevent leakage
   - This generates multiple out-of-sample paths, giving a distribution of performance
   - Use the DISTRIBUTION of OOS Sharpe ratios, not the single best path

6. **Minimum backtest length**:
   T_min = (1 + (1 - skew*SR + ((kurt-1)/4)*SR^2)) x (z_alpha / SR)^2
   For SR = 1.0, normal returns: T_min ~ 16 years for 95% confidence
   For SR = 2.0, normal returns: T_min ~ 4 years for 95% confidence
```

---

## 3. Factor Model Construction

### Build and Validate a Custom Factor Model

```
I'm constructing a factor model for [equity universe / asset class] to use for:
- [ ] Risk decomposition
- [ ] Alpha signal orthogonalization
- [ ] Portfolio optimization constraints
- [ ] Performance attribution

Factor candidates:
- Standard: Market, Size, Value, Momentum, Quality, Low Vol
- Custom: [describe proprietary factors, e.g., "earnings revision breadth", "supply chain disruption score"]

Help me build the model:

1. **Factor construction methodology**:
   - Long/short portfolio for each factor (quintile or decile sorts)
   - Sector neutralization: Construct factors within sectors to avoid sector bets
   - Rebalance frequency: [monthly / quarterly]
   - Weighting: [equal-weight / cap-weight / signal-weight] within quintiles

2. **Factor orthogonalization**:
   - Test pairwise correlation of factor returns
   - If two factors are > 0.5 correlated, consider:
     a) Dropping the weaker factor
     b) Gram-Schmidt orthogonalization: Regress Factor B on Factor A, use residual as "pure" Factor B
     c) PCA: Extract orthogonal principal components from factor set
   - Goal: Each factor captures an independent source of return variation

3. **Factor crowding detection**:
   - Measure: How many investors are exposed to this factor?
   - Indicators: Factor valuation spread (compressed = crowded), short interest in factor shorts,
     factor flow data, correlation of factor with broad market drawdowns
   - Risk: Crowded factors exhibit "factor crashes" -- rapid reversal when positions unwind
   - Crowding adjustment: Reduce allocation to factors with elevated crowding scores

4. **Factor model regression**:
   r_i,t = alpha_i + Sum_k(beta_i,k x F_k,t) + epsilon_i,t
   - Estimate betas using rolling [36 / 60]-month OLS or Bayesian shrinkage
   - Test for beta stability: Are betas constant or time-varying?
   - Model fit: R-squared should explain [40-70]% of cross-sectional return variation
   - Residual analysis: epsilon should be uncorrelated across assets (if not, missing factor)

5. **Fama-MacBeth cross-sectional test**:
   For each month t: r_i,t = gamma_0,t + Sum_k(gamma_k,t x beta_i,k) + u_i,t
   Factor risk premium = time-series average of gamma_k,t
   t-stat for risk premium: Use Newey-West standard errors for autocorrelation robustness
```

---

## 4. Machine Learning in Trading Signals

### Apply ML to Signal Generation with Overfitting Prevention

```
I want to apply machine learning to [signal generation / regime detection / return prediction]
for [asset class / universe].

Features: [list features, e.g., "momentum, value, sentiment, volatility, macro indicators"]
Target: [forward return, binary classification (up/down), regime label]
Training data: [X] years, [X] observations, [X] features

Help me design an ML pipeline that avoids the most common quant ML pitfalls:

1. **Feature importance and selection**:
   - Start with [X] candidate features
   - Remove features with: IC < [threshold], > [X]% missing data, look-ahead bias
   - Feature importance: Use [permutation importance / SHAP values / tree-based importance]
   - Feature selection: Forward stepwise, LASSO (L1 regularization), or mRMR
   - Target: [10-30] features maximum. More features = more overfitting risk.

2. **Model selection**:
   For return prediction (regression):
   - Linear: Ridge, LASSO, Elastic Net (strong baseline, hard to overfit)
   - Tree-based: Random Forest, XGBoost, LightGBM (capture non-linearities)
   - Neural: LSTM for sequence modeling (high overfitting risk, needs lots of data)
   Rule of thumb: Start with penalized linear models. Add complexity only if OOS improves.

   For regime detection (unsupervised):
   - Hidden Markov Models (HMM): [2-4] states on [returns, volatility, correlation]
   - K-means / GMM on feature space
   - Regime features: VIX level, yield curve slope, credit spreads, cross-asset correlations

3. **Overfitting prevention** (THE critical issue in financial ML):
   - Regularization: L1 (LASSO), L2 (Ridge), dropout (neural nets)
   - Ensemble methods: Bagging reduces variance, boosting reduces bias
   - Cross-validation: Use CPCV (not random k-fold -- time series has autocorrelation!)
   - Early stopping: Monitor validation loss, stop when it starts increasing
   - Feature/target ratio: Never exceed 1 feature per 20 observations (absolute minimum)
   - Complexity budget: Information criterion (AIC/BIC) penalizes parameter count

4. **Non-linear signal detection**:
   - Interaction effects: Does momentum work differently in high-vol vs. low-vol regimes?
   - Threshold effects: Does value only work when spread exceeds [X] sigma?
   - Tree-based models naturally capture these; test with partial dependence plots
   - If non-linearity is robust OOS, it adds genuine alpha above linear factors

5. **Production deployment checks**:
   - OOS performance: Must be > [50]% of in-sample Sharpe (typical Sharpe decay: 40-60%)
   - Turnover: ML signals often have high, unstable turnover. Constrain rebalance frequency.
   - Regime robustness: Test performance in each detected regime separately
   - Feature drift: Monitor feature distributions in production vs. training data
   - Model staleness: Retrain every [X] months on expanding window
```

---

## 5. Execution Optimization

### Model Market Impact and Optimize Execution

```
My strategy trades [asset class] with the following characteristics:
- Universe size: [X] instruments
- Average daily volume of typical instrument: $[X]M
- Average trade size: [X]% of ADV
- Rebalance frequency: [daily / weekly / monthly]
- Monthly one-way turnover: [X]%
- Urgency: [high (alpha decays fast) / low (alpha is slow)]

Model execution costs and optimize trading:

1. **Market impact model (Almgren-Chriss framework)**:
   Total cost = Permanent impact + Temporary impact + Timing risk

   Permanent impact (information leakage):
   g(v) = gamma x sigma x (v/V)^delta
   where v = trade rate (shares/time), V = market volume, sigma = volatility
   Typical: gamma ~ 0.1, delta ~ 0.5

   Temporary impact (liquidity consumption):
   h(v) = eta x sigma x (v/V)^beta + epsilon x (spread/2)
   Typical: eta ~ 0.1, beta ~ 0.6

2. **Optimal execution speed**:
   Trade-off: Execute faster = more market impact but less timing risk (alpha decay)
   Optimal trajectory minimizes:
     E[Cost] + lambda x Var[Cost]
   where lambda = risk aversion parameter

   If alpha half-life = [X] hours/days:
   - Fast-decaying alpha (< 1 day): Execute immediately, accept market impact
   - Medium-decaying (1-5 days): TWAP/VWAP over [X] hours
   - Slow-decaying (> 5 days): Spread execution over multiple days, use limit orders

3. **Implementation shortfall decomposition**:
   IS = Decision price - Execution price
   Components:
   - Delay cost: Price move from decision to order submission
   - Market impact: Price move caused by our execution
   - Timing cost: Difference between TWAP benchmark and actual fills
   - Opportunity cost: Portion of order not filled (unfilled alpha)

4. **Execution algorithm selection**:
   | Algorithm | Best for | Participation rate | Alpha decay tolerance |
   |-----------|----------|-------------------|----------------------|
   | TWAP | Even execution | Fixed % | Medium |
   | VWAP | Match market volume profile | Variable | Medium |
   | IS (Shortfall) | Minimize total cost | Front-loaded | Low |
   | POV | Adaptive to volume | Target % | Medium |
   | Limit/passive | Minimize impact | Opportunistic | High |

5. **AUM capacity estimation**:
   At AUM level A, total annual cost = Turnover x 2 x Impact(A)
   Net Sharpe(A) = Gross Sharpe - (Annual cost / Annual volatility)
   Capacity = AUM where Net Sharpe = [minimum acceptable, e.g., 0.5]
   Sharpe decay curve: Plot Net Sharpe vs. AUM to find optimal fund size
```

---

## Mathematical Frameworks Reference

**Fundamental Law of Active Management**:
IR = IC x sqrt(BR). Information Ratio equals Information Coefficient times square root of Breadth (independent bets per year). This is the central equation of quantitative investing.

**Information Coefficient (IC)**:
IC = corr(signal, forward_return). Cross-sectional rank correlation, measured per period. IC > 0.05 monthly is a strong signal. IC_IR = mean(IC)/std(IC) > 0.5 is investable.

**Deflated Sharpe Ratio**:
Adjusts observed Sharpe for multiple testing, non-normal returns, and backtest length. A Sharpe of 1.5 from testing 1,000 strategies is less impressive than a Sharpe of 0.8 from a single hypothesis.

**Kelly Criterion with Parameter Uncertainty**:
f* = mu/sigma^2 (continuous case). With estimation error: f_adjusted = f* / (1 + sigma_mu^2/sigma^2) where sigma_mu is the standard error of the mean return estimate. This naturally reduces sizing when the edge is uncertain.

**Sharpe Decay with AUM**:
SR(AUM) ~ SR(0) - k x AUM x Turnover / ADV_universe, where k is a market impact constant. Every strategy has a capacity ceiling.

**t-stat Requirements**:
For a single test: t > 2.0 (p < 0.05). For 10 tests: t > 2.8 (Bonferroni). For 100 tests: t > 3.4. For 1,000 tests: t > 3.8. Harvey, Liu, and Zhu (2016) recommend t > 3.0 as a minimum for any factor.

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- Signal generation, portfolio construction, statistical testing
- [`fundamental-long-short.md`](fundamental-long-short.md) -- Fundamental signals to combine with quant factors
- [`global-macro.md`](global-macro.md) -- Macro factor models for systematic macro
- [`event-driven.md`](event-driven.md) -- Event-driven signals (earnings, M&A) for systematic event strategies
