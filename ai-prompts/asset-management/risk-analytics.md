# Risk Management & Performance Analytics

```
You are a senior risk officer and head of portfolio analytics at a large institutional asset
manager. You oversee risk measurement, attribution, and reporting across $100B+ in equities,
fixed income, alternatives, and multi-asset portfolios. You think in terms of factor risk
decomposition, VaR and tail risk, scenario analysis, and liquidity-adjusted risk measures.
You understand that risk models are approximations — you focus on model limitations, regime
dependence, and the gap between ex-ante risk estimates and realized outcomes. You are the
second line of defense: your role is to challenge portfolio managers, identify hidden risks,
and ensure the firm's risk-taking is intentional, diversified, and within policy guidelines.
You communicate risk in terms that both quantitative PMs and non-technical board members
can understand.
```

## What This Desk Does

The risk and performance analytics team provides independent measurement, monitoring, and reporting of investment risk and return across all portfolios managed by the firm. This includes ex-ante risk estimation (what could happen), ex-post attribution (what did happen and why), stress testing (what happens under extreme scenarios), and liquidity risk assessment (can we meet redemptions without fire sales). The team maintains risk models (factor-based, statistical, and scenario-based), sets and monitors risk limits (tracking error, VaR, concentration, leverage), and produces performance attribution that decomposes returns into skill-based and risk-based components. Effective risk management is not about avoiding risk — it is about ensuring that risk-taking is intentional, compensated, and within the firm's risk appetite.

---

## 1. Factor Risk Decomposition

Breaking portfolio risk into systematic factor exposures and idiosyncratic (stock-specific) components to identify unintended bets and concentration.

**Total portfolio variance:** sigma_p^2 = w' x B x F x B' x w + w' x D x w

Where: B = factor exposure matrix (N x K), F = factor covariance matrix (K x K), D = diagonal matrix of idiosyncratic variances, w = portfolio weights.

**Marginal Contribution to Risk (MCTR):** MCTR_i = (Sigma x w)_i / sigma_p = beta_i x sigma_p

**Component Risk (CR):** CR_i = w_i x MCTR_i. Sum of all CR_i = sigma_p.

**Percent Contribution to Risk:** PCR_i = CR_i / sigma_p = w_i x beta_i.

### Factor Risk Attribution

```
Decompose the risk of my [equity / fixed income / multi-asset] portfolio:

Portfolio: [name], AUM: $[X]B, Benchmark: [index]
Number of holdings: [N]
Risk model: [Barra / Axioma / Northfield / Bloomberg / custom factor model]

Current risk metrics:
- Portfolio volatility (ex-ante): [X]%
- Benchmark volatility: [X]%
- Tracking error (ex-ante): [X] bps
- Active share: [X]%

Factor exposures (portfolio vs benchmark):
- Market beta: [X] vs [X]
- Size (SMB): [X] vs [X]
- Value (HML): [X] vs [X]
- Momentum (UMD): [X] vs [X]
- Quality (QMJ): [X] vs [X]
- Volatility (BAB): [X] vs [X]
- [Sector factors: list active weights]

Help me:
1. **Risk decomposition**: What percentage of total portfolio risk comes from:
   - Systematic factor risk: [X]% (driven by factor exposures)
   - Idiosyncratic risk: [X]% (driven by stock-specific positions)
   - For tracking error: factor active risk vs stock-specific active risk

2. **Marginal contribution to tracking error**: Which positions contribute most to active risk?
   - MCTE_i = (Sigma_active x w_active)_i / TE
   - Top 10 risk contributors: [list positions with MCTE]
   - Identify positions that are large alpha bets vs positions that are large risk contributors

3. **Unintended factor bets**: Factor exposures that are not part of the investment thesis
   - If I'm a stock picker, my alpha should come from idiosyncratic risk, not factor tilts
   - Flag: Factor active exposures > [X] standard deviations from benchmark
   - Cost of unintended bets: factor_exposure x factor_volatility = risk without conviction

4. **Risk concentration**: Herfindahl index of risk contributions
   - HHI_risk = sum(PCR_i^2) — high HHI means risk is concentrated in few positions
   - Compare HHI of weight vs HHI of risk (different if positions have different betas)

5. **Incremental VaR**: What is the change in portfolio VaR from adding position i?
   - IVaR_i = VaR(portfolio + position_i) - VaR(portfolio)
   - Use for new position sizing: How much risk does this trade add?

6. **Risk budget utilization**: What percent of the tracking error budget is consumed?
   - TE used / TE budget = [X]%. Remaining risk budget for new trades: [X] bps.
```

---

## 2. Scenario Analysis and Stress Testing

Evaluating portfolio behavior under historical crises, hypothetical shocks, and extreme-but-plausible scenarios.

### Historical and Hypothetical Stress Tests

```
Run stress tests on my portfolio for risk reporting and investment committee:

Portfolio: [name], AUM: $[X]B
Asset class composition: [equity X%, FI X%, alternatives X%, cash X%]
Gross/net exposure (if applicable): [X]% / [X]%

Historical scenarios to model:
1. **2008 GFC** (Sep 2008 - Mar 2009):
   - Equities: -40%, IG spreads: +300bps, HY spreads: +1200bps, VIX: 80
   - Treasuries: +15% (flight to quality), Dollar: +15%
2. **2020 COVID crash** (Feb-Mar 2020):
   - Equities: -34% in 23 trading days, HY spreads: +600bps, Oil: -65%
   - V-shaped recovery: +45% from March low by August
3. **2022 rate shock** (Jan-Oct 2022):
   - Equities: -25%, Aggregate bonds: -16%, 60/40: -20%
   - Rates: +300bps across the curve, no safe haven from bonds
4. **1987 crash** (Oct 1987): Equities: -22% in one day, implied vol spike
5. **Stagflation** (1973-74): Equities: -45%, inflation: 12%, bonds: negative real returns

Hypothetical scenarios:
6. **Rate shock**: Parallel +200bps shift across all maturities
7. **Credit crisis**: IG spreads +200bps, HY +600bps, EM +400bps, defaults spike
8. **Equity bear market**: -30% equities, correlation spike (all risk assets correlate to 0.8)
9. **USD collapse**: Dollar -20%, EM currencies +15%, gold +30%
10. **Liquidity crisis**: Bid-ask spreads 5x normal, can only liquidate 10% of portfolio per week

For each scenario, calculate:
1. Portfolio P&L (dollar and percentage)
2. Contribution by asset class and top positions
3. Days to recover (based on historical analog recovery time)
4. Liquidity impact: Can I meet potential redemptions during the scenario?
5. Conditional correlations: How do asset class correlations change in the scenario?

Reverse stress test: What scenario would cause a [X]% loss? What conditions would trigger it?
```

### Conditional Correlation Analysis

```
Analyze how correlations in my portfolio change under stress:

Normal correlation matrix (unconditional, trailing [X] years): [provide or describe]
Concern: Correlations spike in drawdowns, reducing diversification when most needed.

Help me:
1. **Conditional correlation estimation**: Calculate correlations for:
   - Normal regime (VIX < 20): [correlation matrix]
   - Elevated stress (VIX 20-30): [correlation matrix]
   - Crisis (VIX > 30): [correlation matrix]
2. **Stock-bond correlation regime**: Currently [positive/negative]
   - Positive stock-bond correlation = bonds don't hedge equities (2022 regime)
   - Negative correlation = bonds hedge equities (2008, 2020)
   - Impact on portfolio VaR under each correlation regime
3. **Copula analysis**: Use a t-copula or Clayton copula to model tail dependence
   - Tail dependence coefficient: probability of joint extreme moves
   - Normal distribution underestimates joint tail events (Gaussian copula problem)
4. **Diversification ratio**: DR = sum(w_i x sigma_i) / sigma_portfolio
   - DR in normal times: [X] (higher = more diversification benefit)
   - DR in crisis: [X] (collapses as correlations spike)
5. **Hedging effectiveness**: Do my hedges work when I need them?
   - Hedge ratio stability across regimes
   - Cost of hedges that work in crisis (put options, CDS, tail risk strategies)
```

---

## 3. Value-at-Risk and Tail Risk

Estimating potential losses using parametric, historical simulation, and Monte Carlo VaR approaches, with extensions for non-normal distributions.

**Parametric VaR (normal):** VaR_alpha = mu - z_alpha x sigma

Where z_alpha = 1.645 for 95%, 2.326 for 99%.

**Portfolio VaR:** VaR_p = z_alpha x sqrt(w' x Sigma x w) x Portfolio_Value

**Cornish-Fisher VaR (non-normal):** Adjusts z_alpha for skewness and kurtosis:
z_CF = z + (1/6)(z^2 - 1)S + (1/24)(z^3 - 3z)(K-3) - (1/36)(2z^3 - 5z)S^2

Where S = skewness, K = kurtosis (excess kurtosis = K-3 in some conventions).

**CVaR (Expected Shortfall):** E[Loss | Loss > VaR] — average loss in the tail beyond VaR.
For normal: CVaR_alpha = sigma x phi(z_alpha) / (1 - alpha) where phi is the standard normal PDF.

### VaR Analysis and Reporting

```
Calculate VaR and tail risk metrics for my portfolio:

Portfolio: [name], AUM: $[X]B
Asset classes: [list with weights]
Return history: [X] years of daily/monthly returns available

Current portfolio statistics:
- Annualized return: [X]%
- Annualized volatility: [X]%
- Skewness: [X]
- Excess kurtosis: [X]
- Maximum drawdown: [X]%

Help me calculate:
1. **Parametric VaR** (1-day and 10-day, 95% and 99%):
   - VaR_1d_95 = portfolio_value x sigma_daily x 1.645
   - VaR_10d_99 = VaR_1d_99 x sqrt(10) (square root of time, assumes i.i.d.)
   - Limitation: Assumes normal distribution (underestimates tail risk)

2. **Cornish-Fisher adjusted VaR**: Correct for observed skewness and kurtosis
   - z_CF = z + (1/6)(z^2-1)*skew + (1/24)(z^3-3z)*excess_kurtosis - (1/36)(2z^3-5z)*skew^2
   - VaR_CF = portfolio_value x sigma x z_CF
   - This is more accurate for portfolios with options, credit, or MBS (non-normal returns)

3. **Historical simulation VaR**: Use actual historical return distribution
   - Sort [X] years of daily returns, take the [5th / 1st] percentile
   - Advantages: No distribution assumption, captures actual tail behavior
   - Limitation: Only as good as the history; misses scenarios that haven't occurred

4. **Monte Carlo VaR**: Simulate [10,000+] return paths from fitted distribution
   - Use multivariate t-distribution or copula for fat tails and tail dependence
   - Advantages: Can model complex portfolios, path-dependent instruments, options
   - VaR = [alpha] percentile of simulated P&L distribution

5. **CVaR / Expected Shortfall**: Average loss beyond VaR
   - CVaR is a coherent risk measure (VaR is not — it can violate sub-additivity)
   - CVaR_95 typically 20-40% larger than VaR_95 for equity portfolios
   - Report both: VaR tells you the threshold, CVaR tells you how bad it gets beyond that

6. **Component VaR**: Decompose portfolio VaR into position contributions
   - CVaR_i = w_i x beta_i x VaR_portfolio
   - Sum of all component VaRs = portfolio VaR
   - Identifies which positions contribute most to tail risk

7. **VaR backtesting**: Count VaR exceptions (days where actual loss > VaR)
   - Expected exceptions at 99%: [X] per year for daily VaR
   - Too many exceptions: model underestimates risk (recalibrate)
   - Too few: model is too conservative (capital inefficiency)
   - Kupiec test, Christoffersen test for statistical evaluation
```

---

## 4. Liquidity Risk

Assessing the ability to liquidate portfolio positions without excessive market impact, and managing redemption risk.

### Liquidity Risk Assessment

```
Assess the liquidity profile of my portfolio:

Portfolio: [name], AUM: $[X]B
Largest positions: [list top 10 with weight, ADV, and bid-ask spread]
Redemption terms: [daily / weekly / monthly / quarterly] with [X]-day notice

Liquidity inputs per position:
- Average daily volume (ADV): $[X]M
- Bid-ask spread: [X] bps
- Average participation rate to avoid impact: [X]% of ADV
- Days to liquidate at [X]% participation: position_value / (ADV x participation_rate)

Help me:
1. **Liquidity scoring**: Score each position (1-5) based on:
   - Time to liquidate (days): < 1 day = 5 (very liquid), > 30 days = 1 (illiquid)
   - Bid-ask spread: < 5 bps = 5, > 100 bps = 1
   - Market impact estimate: Almgren-Chriss or square-root model
   - Composite liquidity score = weighted average across scoring dimensions

2. **Portfolio liquidity profile**:
   - Day 1 liquidity: [X]% of NAV can be liquidated in 1 day without > [X] bps impact
   - 1-week liquidity: [X]% of NAV
   - 1-month liquidity: [X]% of NAV
   - Build a cumulative liquidation schedule

3. **Liquidity-adjusted VaR (LVaR)**:
   - LVaR = VaR + Liquidity Cost
   - Liquidity Cost = sum(w_i x spread_i / 2) for immediate liquidation
   - More sophisticated: LVaR = VaR + (1/2) x sum(w_i x spread_i) + market_impact_cost
   - LVaR is typically 10-30% higher than standard VaR

4. **Redemption stress test**: Can I meet a [X]% redemption request?
   - Scenario: 10% of AUM redeemed in [X] days
   - What positions do I sell first? (most liquid, least conviction, tax-loss candidates)
   - What is the cost of forced liquidation? (spread + impact + opportunity cost)
   - Does liquidation change portfolio characteristics? (tracking error, factor tilts)

5. **Liquidity mismatch**: Compare liability (redemption) liquidity vs asset liquidity
   - Daily redemption fund with 10% in illiquid securities = mismatch risk
   - Swing pricing: Adjust NAV to pass liquidation costs to redeeming investors
   - Liquidity bucket: Maintain [X]% in cash or T-bills as liquidity buffer

6. **Market-wide liquidity risk**: In a crisis, liquidity evaporates across all assets simultaneously
   - Bid-ask spreads widen 3-10x in stress (model this scenario)
   - ADV drops 50%+ in crisis (fewer market makers, wider spreads)
   - Correlation of illiquidity across positions (crowded trades unwind simultaneously)
```

---

## 5. Performance Analytics

Measuring and reporting risk-adjusted returns, drawdowns, and skill-based metrics to evaluate portfolio managers and strategies.

### Comprehensive Performance Report

```
Generate a comprehensive performance analytics report for [portfolio]:

Portfolio: [name], Inception: [date], Benchmark: [index]
Return stream: [provide monthly/daily returns or describe period]

Core metrics to calculate:
- Annualized return: [X]% gross, [X]% net
- Benchmark return: [X]%
- Active return (alpha): [X] bps

Calculate and interpret:

1. **Risk-adjusted return ratios**:
   - Sharpe ratio: (R_p - R_f) / sigma_p
   - Sortino ratio: (R_p - R_f) / sigma_downside (only penalizes downside deviation)
   - Information ratio: alpha / tracking_error
   - Calmar ratio: annualized_return / max_drawdown
   - Treynor ratio: (R_p - R_f) / beta_p

2. **Drawdown analysis**:
   - Maximum drawdown: [X]% (peak: [date], trough: [date], recovery: [date])
   - Average drawdown: [X]%
   - Maximum drawdown duration: [X] months
   - Drawdown distribution: histogram of all drawdowns
   - Ulcer index: sqrt(mean(drawdown_i^2)) — penalizes deep and prolonged drawdowns

3. **Skill assessment metrics**:
   - Hit rate: % of months with positive active return ([X]%)
   - Win/loss ratio: average positive active return / |average negative active return|
   - Batting average x win/loss = information ratio proxy
   - Up capture: portfolio return in up-benchmark months / benchmark return
   - Down capture: portfolio return in down-benchmark months / benchmark return
   - Capture ratio: up_capture / down_capture (> 1.0 = skill)

4. **Statistical significance**:
   - t-stat of alpha = alpha / SE(alpha) = IR x sqrt(T_years)
   - Years needed for significance at 95%: T = (1.96 / IR)^2
   - At IR = 0.5, need ~15 years for statistical significance (sobering reality)
   - Bootstrap confidence interval for Sharpe ratio

5. **Peer ranking**:
   - Percentile rank vs [peer universe] over 1Y, 3Y, 5Y, 10Y, since inception
   - Consistency: % of rolling 3-year periods in top half
   - Style-adjusted rank: Rank after controlling for factor exposures

6. **Return decomposition**:
   - Brinson attribution summary: allocation [X] bps, selection [X] bps, interaction [X] bps
   - Factor attribution: factor timing [X] bps, factor exposure [X] bps, residual alpha [X] bps
   - Fee impact: gross-to-net bridge ([X] bps management fee, [X] bps trading costs)
```

### Manager Comparison and Selection Analytics

```
Compare [N] managers for a [mandate type] allocation:

Managers:
- Manager A: [strategy], [X]-year track record, IR = [X], TE = [X]%
- Manager B: [strategy], [X]-year track record, IR = [X], TE = [X]%
- Manager C: [strategy], [X]-year track record, IR = [X], TE = [X]%

Help me evaluate:
1. **Return comparison**: Annualized alpha, risk, IR for each (apples-to-apples time period)
2. **Risk-adjusted comparison**: Sharpe, Sortino, information ratio ranking
3. **Style analysis** (Sharpe returns-based style analysis):
   - Regress each manager's returns on style indices to identify actual (not stated) style
   - Identify style drift: Has the manager's style changed over time?
4. **Drawdown comparison**: Maximum drawdown, recovery time, drawdown frequency
5. **Correlation analysis**: Correlation between managers (low correlation = blend both for better IR)
   - Blended IR = IR_A_alone < IR_A+B_together if correlation < 1.0
   - Optimal manager blend: allocate to minimize total tracking error for given alpha
6. **Fee-adjusted comparison**: Net-of-fee returns and IR
   - Manager with higher gross IR but higher fees may be worse net
7. **Qualitative assessment**: Team stability, organizational risk, capacity, alignment
```

---

## Mathematical Reference

**VaR Formulas:**
- Parametric (normal): VaR_alpha = -mu_p + z_alpha x sigma_p (loss expressed as positive number)
- 95% VaR: z = 1.645; 99% VaR: z = 2.326
- Cornish-Fisher: z_CF = z + (1/6)(z^2-1)S + (1/24)(z^3-3z)(K-3) - (1/36)(2z^3-5z)S^2
- Historical: VaR = -Percentile(returns, alpha)
- CVaR_alpha = E[Loss | Loss > VaR_alpha] (expected shortfall, coherent risk measure)

**Component VaR:** CVaR_i = w_i x (Sigma x w)_i / sigma_p x VaR_p = w_i x beta_i x VaR_p. Sum of component VaRs = portfolio VaR.

**Marginal VaR:** MVaR_i = dVaR/dw_i = beta_i x VaR_p / Portfolio_Value. Tells you how much VaR changes per dollar added to position i.

**Incremental VaR:** IVaR = VaR(portfolio + new_position) - VaR(portfolio). For small positions, IVaR approximately equals MVaR_i x position_size.

**Risk-Adjusted Return Metrics:**
- Sharpe = (R_p - R_f) / sigma_p
- Sortino = (R_p - R_f) / sigma_downside where sigma_downside = sqrt(mean(min(R_t - R_f, 0)^2))
- Information Ratio = (R_p - R_b) / TE
- Calmar = annualized_return / |max_drawdown|
- Treynor = (R_p - R_f) / beta_p

**Statistical Significance of Alpha:**
- t_stat = alpha / SE(alpha) = IR x sqrt(T)
- Minimum track record length (MTL): T_min = (z_alpha / IR)^2 years
- At IR = 0.5: MTL = (1.96/0.5)^2 = 15.4 years for 95% confidence

**Liquidity-Adjusted VaR:**
LVaR = VaR + (1/2) x sum(w_i x spread_i) + sum(impact_cost_i)
Where impact_cost_i = sigma_i x sqrt(w_i x Portfolio_Value / ADV_i) x eta (Almgren-Chriss)

---

## See Also

- [Active Equity](active-equity.md) — Brinson attribution and information ratio analysis for equity portfolios
- [Systematic & Factor Investing](systematic-factor.md) — factor models and factor risk decomposition
- [Fixed Income Asset Management](fixed-income-am.md) — duration risk, spread risk, and key rate duration analysis
- [Multi-Asset Allocation](multi-asset.md) — total portfolio risk budgeting and SAA optimization
- [Alternatives Allocation](alternatives-allocation.md) — risk measurement challenges for illiquid alternatives
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — factor risk decomposition, drawdown analysis, and statistical testing
