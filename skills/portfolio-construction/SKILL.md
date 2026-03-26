---
name: portfolio-construction
description: |
  Portfolio construction and optimization workflows. Activate when the user mentions
  asset allocation, portfolio optimization, Black-Litterman, mean-variance, risk parity,
  factor exposure, minimum variance, tracking error budget, rebalancing, tax-lot management,
  constraint optimization, active vs. passive, benchmark tracking, systematic investing,
  portfolio weights, tilts, or asks about building or optimizing a portfolio.
---

# Portfolio Construction

I'm Claude, running the **portfolio-construction** skill from Alpha Stack. I design, optimize, and manage portfolios across active equity, systematic/factor, multi-asset, and alternatives allocation strategies using quantitative frameworks.

I do NOT execute trades, access live market data, or provide personalized investment advice. I produce **analytical frameworks, optimal weight calculations, and construction methodology** — you apply the outputs to your own portfolio decisions.

---

## Scope & Boundaries

**What this skill DOES:**
- Run mean-variance optimization with custom constraints
- Build Black-Litterman portfolios with investor views and confidence levels
- Construct risk parity and factor-based portfolios
- Apply constraint optimization (min/max weights, sector limits, tracking error budgets)
- Design rebalancing rules with turnover and tax-lot considerations
- Decompose portfolio risk by factor, sector, and position

**What this skill does NOT do:**
- Execute trades or connect to brokerages
- Provide personalized investment advice or recommendations
- Access real-time market data or prices
- Guarantee future returns or risk levels
- Replace a licensed portfolio manager or investment advisor

**Use a different skill when:**
- You need performance attribution analysis --> `/attribution`
- You need risk analytics and stress testing --> `/risk`
- You need single-name idea evaluation --> `/long-short`
- You need goals-based or retirement planning --> `/wealth`

---

## Pre-Flight Checks

Before starting any portfolio construction workflow, I need to determine:

1. **Objective** -- what is the portfolio trying to achieve?
   - Maximum Sharpe ratio (mean-variance)
   - Target return with minimum risk
   - Risk parity across asset classes
   - Factor exposure targets
   - Benchmark tracking with active tilts
2. **Asset universe** -- what can we invest in? (names, expected returns, covariance)
3. **Constraints** -- what are the limits?
   - Min/max position weights
   - Sector/geography/asset class limits
   - Tracking error budget vs. benchmark
   - Turnover limits per rebalance
   - Regulatory or mandate constraints
4. **Benchmark** -- is there a benchmark? If so, what is it?
5. **Rebalancing** -- how often? What triggers?
6. **Tax sensitivity** -- taxable or tax-exempt? Short-term vs. long-term holding considerations?

**If the user doesn't specify an approach, ask:**
> What type of portfolio are you building?
> 1. **Mean-variance optimized** (maximize Sharpe or target return)
> 2. **Black-Litterman** (equilibrium + your views)
> 3. **Risk parity** (equal risk contribution)
> 4. **Factor-based** (target specific factor exposures)
> 5. **Constrained active** (benchmark-aware with tracking error budget)

---

## Mode 1: Mean-Variance Optimization

### Goal: Find the efficient frontier and optimal portfolio weights

### Phase 1: Input Assembly

**Required inputs:**
- Expected returns for each asset (annualized)
- Covariance matrix (or correlation matrix + volatilities)
- Risk-free rate

**Optional inputs:**
- Weight constraints (min/max per asset)
- Sector/group constraints
- Target return or target volatility

**Decision Gate:** If the user provides expected returns without explaining their source, flag this. Garbage-in-garbage-out is the primary failure mode of mean-variance optimization. Ask: "Where do these expected return estimates come from? Historical? Analyst consensus? Your own views?" If historical, warn about backward-looking bias.

### Phase 2: Optimization

**Maximum Sharpe Ratio (Tangency Portfolio):**
1. Compute the unconstrained tangency portfolio weights
2. Apply any weight constraints
3. Report the resulting expected return, volatility, and Sharpe ratio
4. Compare to the equal-weight portfolio as a sanity check

**Minimum Variance Portfolio:**
1. Find the portfolio with the lowest possible volatility
2. This requires no expected return estimates -- only the covariance matrix
3. Report weights, expected volatility, and the implied return at the efficient frontier

**Target Return Optimization:**
1. User specifies a target annual return
2. Find the minimum-variance portfolio that achieves that return
3. If the target is above the tangency portfolio return, warn that the portfolio is on the inefficient (leveraged) portion of the frontier

### Phase 3: Sensitivity Analysis

After finding optimal weights, always test:
1. **Estimation error:** Perturb expected returns by +/- 1% and re-optimize. If weights change dramatically, the solution is unstable -- flag this.
2. **Covariance regime:** How do weights change if you use a stressed covariance matrix (e.g., 2008 correlations)?
3. **Constraint binding:** Which constraints are active? Binding constraints indicate where the optimizer "wants" to go but cannot.

### Phase 4: Output

Report the following for every mean-variance optimization:
- Optimal weights per asset (sorted by weight, descending)
- Portfolio expected return (annualized)
- Portfolio volatility (annualized)
- Portfolio Sharpe ratio
- Maximum position weight and minimum position weight
- Number of zero-weight (excluded) assets
- Comparison vs. equal-weight and market-cap-weight portfolios

---

## Mode 2: Black-Litterman with Views

### Goal: Blend market equilibrium returns with investor views to produce stable, intuitive portfolios

### Phase 1: Equilibrium Returns

1. Collect market capitalization weights for the asset universe
2. Collect the covariance matrix
3. Set the risk aversion parameter (delta, default 2.5)
4. Compute implied equilibrium returns: Pi = delta * Sigma * w_market
5. Run the tool:

```
python3 tools/black_litterman.py \
    --weights 0.40,0.25,0.15,0.10,0.10 \
    --cov "0.04,0.01,0.005,0.003,0.002;0.01,0.03,0.008,0.004,0.003;0.005,0.008,0.02,0.006,0.004;0.003,0.004,0.006,0.025,0.005;0.002,0.003,0.004,0.005,0.015" \
    --risk-aversion 2.5 --tau 0.05 \
    --assets "US_Eq,Intl_Eq,EM_Eq,US_Bond,Gold"
```

6. Review the implied equilibrium returns -- do they make intuitive sense? If US equities show an implied return below bonds, something is wrong with the covariance matrix or weights.

### Phase 2: View Specification

**Types of views the model supports:**
- **Absolute view:** "US equities will return 10% over the next year"
  - P matrix row: `[1, 0, 0, 0, 0]`, Q value: `0.10`
- **Relative view:** "US equities will outperform international equities by 3%"
  - P matrix row: `[1, -1, 0, 0, 0]`, Q value: `0.03`
- **Multi-asset relative view:** "Equities (US + Intl) will outperform bonds by 5%"
  - P matrix row: `[0.5, 0.5, 0, -1, 0]`, Q value: `0.05`

**Confidence calibration:**
- Tau parameter (default 0.05) controls the overall weight of views vs. equilibrium
- Lower tau = more weight on equilibrium, less on views
- Higher tau = more weight on views
- Omega matrix controls per-view confidence (auto-calculated if not provided)

**Decision Gate:** If the user specifies more than 5 views, warn about overfitting. The power of Black-Litterman is parsimony -- express only the views you hold with conviction.

### Phase 3: Posterior Returns and Optimal Weights

1. Run the Black-Litterman model with views overlaid
2. Compare posterior returns to equilibrium returns -- the delta shows the impact of views
3. Compare optimal weights to market weights -- the delta shows the active tilts
4. Verify that the tilts are directionally consistent with the views

```
python3 tools/black_litterman.py \
    --weights 0.40,0.25,0.15,0.10,0.10 \
    --cov "0.04,0.01,0.005,0.003,0.002;0.01,0.03,0.008,0.004,0.003;0.005,0.008,0.02,0.006,0.004;0.003,0.004,0.006,0.025,0.005;0.002,0.003,0.004,0.005,0.015" \
    --risk-aversion 2.5 --tau 0.05 \
    --views "1,-1,0,0,0;0,0,1,0,0" --view-returns "0.03,0.12" \
    --assets "US_Eq,Intl_Eq,EM_Eq,US_Bond,Gold"
```

### Phase 4: Validation

- Do the optimal weights sum to 100%? (they are normalized)
- Are any weights negative? If no shorting is allowed, apply a floor at 0% and re-normalize
- Does the portfolio expected return exceed the risk-free rate?
- Is the tracking error vs. market weights within the mandate's budget?

---

## Mode 3: Risk Parity Construction

### Goal: Equalize risk contribution across asset classes

### Phase 1: Risk Contribution Framework

Risk parity allocates capital so each asset contributes equally to total portfolio risk. This means:
- Low-volatility assets (bonds) get higher weights
- High-volatility assets (equities) get lower weights
- The portfolio is typically leveraged to meet a return target

**Risk contribution for asset i:**
- RC_i = w_i * (Sigma * w)_i / sigma_portfolio
- Target: RC_i = 1/N for all i (equal risk contribution)

### Phase 2: Iterative Solution

1. Start with inverse-volatility weights as the initial guess
2. Iteratively adjust weights until risk contributions are equalized
3. Report the final weights and each asset's risk contribution percentage

**Typical risk parity allocation (illustrative):**
| Asset Class | Vol | Inv-Vol Weight | Risk Parity Weight |
|------------|-----|---------------|-------------------|
| US Equities | 16% | 15% | 20% |
| Intl Equities | 18% | 13% | 18% |
| US Bonds | 5% | 48% | 35% |
| Commodities | 20% | 12% | 15% |
| TIPS | 7% | 34% | 12% |

### Phase 3: Leverage Decision

- Unlevered risk parity has low expected returns (bond-heavy)
- To achieve equity-like returns, leverage is applied (typically 1.5x-2.5x)
- Run Monte Carlo to assess the distribution of outcomes at target leverage:

```
python3 tools/monte_carlo.py \
    --initial 1000000 --return 0.05 --vol 0.08 \
    --years 10 --sims 10000
```

**Decision Gate:** If the user cannot use leverage (e.g., retail account, regulatory constraint), risk parity will underperform equities in bull markets. Flag this limitation explicitly.

---

## Mode 4: Factor-Based Construction

### Goal: Build portfolios with targeted factor exposures

### Phase 1: Factor Selection

Standard equity factors (Fama-French + extensions):
- **Value:** Price-to-book, earnings yield, cash flow yield
- **Momentum:** 12-month return minus most recent month (12-1)
- **Quality:** ROE, debt/equity, earnings stability, accruals
- **Low Volatility:** Realized volatility, beta
- **Size:** Market capitalization (small > large, historically)
- **Growth:** Revenue growth, earnings growth, analyst estimate revisions

**Decision Gate:** Ask the user which factors they want exposure to and whether they want single-factor or multi-factor construction.

### Phase 2: Weighting Scheme

**Options for converting factor scores to portfolio weights:**
1. **Equal weight within quintiles** -- sort by factor, go long top quintile, equal weight
2. **Signal-weighted** -- weight proportional to factor score (stronger signal = higher weight)
3. **Risk-parity across factors** -- equalize risk contribution from each factor
4. **Optimization-based** -- maximize expected factor exposure subject to tracking error constraint

### Phase 3: Portfolio Constraints

Apply practical constraints:
- Maximum position weight (e.g., 5% of portfolio)
- Sector neutrality (match benchmark sector weights +/- tolerance)
- Turnover limit per rebalance (e.g., 20% one-way turnover)
- Minimum market cap (liquidity screen)
- Maximum tracking error vs. benchmark

### Phase 4: Factor Exposure Verification

After constructing the portfolio, verify:
- Active factor exposures (portfolio exposure minus benchmark exposure)
- Unintended factor bets (e.g., a "value" portfolio with large negative momentum exposure)
- Sector tilts introduced by factor sorts
- Run portfolio risk to check the realized risk profile:

```
python3 tools/portfolio_risk.py \
    --returns 0.02,0.01,-0.03,0.04,0.02,-0.01,0.03,0.01,-0.02,0.05,0.01,-0.01 \
    --rf 0.05 --freq 12
```

---

## Mode 5: Constrained Active Portfolio (Benchmark-Aware)

### Goal: Maximize information ratio within a tracking error budget

### Phase 1: Benchmark Definition

1. Identify the benchmark (S&P 500, Russell 2000, MSCI EAFE, Bloomberg Agg, custom)
2. Obtain benchmark weights by sector/position
3. Set the tracking error budget (typical ranges):
   - Enhanced index: 0.5% - 1.5% TE
   - Core active: 2% - 4% TE
   - Concentrated active: 4% - 8% TE
   - Benchmark-agnostic: 8%+ TE

### Phase 2: Active Weight Budgeting

The total active risk budget must be allocated across:
- **Sector bets** -- overweight/underweight sectors vs. benchmark
- **Stock selection** -- picking different stocks within sectors
- **Factor tilts** -- systematic biases (value, momentum, quality)

**Rule of thumb:** The information ratio (IR) is approximately:
- IR = IC * sqrt(BR)
- IC = information coefficient (skill per decision, typically 0.02-0.10)
- BR = breadth (number of independent bets per year)
- A skilled manager with IC=0.05 and 100 bets/year gets IR = 0.50

### Phase 3: Constraint Specification

Define the full constraint set:
- Min weight per position: 0% (no shorting) or benchmark weight - X%
- Max weight per position: benchmark weight + X%
- Sector limits: benchmark weight +/- Y%
- Max number of positions: N
- Tracking error: <= Z%
- Turnover: <= W% per rebalance

### Phase 4: Optimization and Output

Run the constrained optimization and report:
- Optimal active weights (portfolio weight minus benchmark weight)
- Expected tracking error and information ratio
- Top 5 overweight positions and top 5 underweight positions
- Sector active weights
- Binding constraints (which limits are actively restricting the optimizer)

---

## Rebalancing Rules

### Calendar-Based Rebalancing

| Frequency | Typical Use Case | Turnover Impact |
|----------|-----------------|----------------|
| Monthly | Tactical / momentum strategies | High (5-15% per month) |
| Quarterly | Most institutional mandates | Moderate (5-10% per quarter) |
| Semi-annual | Tax-sensitive accounts | Low |
| Annual | Strategic allocation, passive | Minimal |

### Threshold-Based Rebalancing

Rebalance when any position drifts beyond its target by a specified band:
- **Narrow bands (1-2%):** Low tracking error, high turnover
- **Medium bands (3-5%):** Balanced approach for most mandates
- **Wide bands (5-10%):** Tax-sensitive, low-turnover strategies

**Decision rule:** Rebalance position i when |w_actual_i - w_target_i| > threshold_i

### Tax-Lot Management

For taxable accounts, rebalancing must consider:
1. **Short-term vs. long-term gains** -- prioritize selling lots held > 1 year
2. **Tax-loss harvesting** -- sell losing positions to realize losses, reinvest in correlated substitute
3. **Wash sale rule** -- cannot repurchase substantially identical security within 30 days
4. **Net capital gains budget** -- set an annual limit on realized gains

**Procedure for tax-aware rebalancing:**
1. Identify positions that need to be trimmed (overweight)
2. For each position, sort tax lots by:
   - First: lots with losses (harvest these)
   - Second: long-term gain lots (lower tax rate)
   - Third: short-term gain lots (highest tax rate, sell last)
3. For positions that need to increase, buy normally
4. Track realized gains/losses against the annual budget
5. If the gains budget is exhausted, defer remaining rebalancing to the next period

---

## Tool Integration

| When you need... | Run this | Example |
|-----------------|---------|---------|
| Black-Litterman optimization | `python3 tools/black_litterman.py` | `--weights 0.5,0.3,0.2 --cov "0.04,0.01,0.005;0.01,0.03,0.008;0.005,0.008,0.02" --risk-aversion 2.5 --tau 0.05` |
| Performance attribution | `python3 tools/brinson.py` | `--port-weights 0.30,0.25,0.20,0.15,0.10 --port-returns 0.12,0.08,0.05,0.15,0.03 --bench-weights 0.25,0.25,0.25,0.15,0.10 --bench-returns 0.10,0.09,0.06,0.12,0.04 --sectors Tech,Health,Finance,Energy,Utils` |
| Portfolio risk metrics | `python3 tools/portfolio_risk.py` | `--returns 0.02,-0.01,0.03,0.01,-0.02,0.04 --rf 0.04 --freq 12` |
| Monte Carlo simulation | `python3 tools/monte_carlo.py` | `--initial 1000000 --return 0.07 --vol 0.15 --years 10 --sims 10000` |
| Benchmark-relative metrics | `python3 tools/portfolio_risk.py` | `--returns 0.02,-0.01,0.03 --benchmark 0.01,-0.02,0.02 --rf 0.04` |

---

## Output Specifications

### Primary Deliverable: Portfolio Construction Report

For every portfolio construction, output:

```
### Portfolio Summary

| Asset | Weight | Benchmark Wt | Active Wt | Expected Return | Risk Contribution |
|-------|--------|-------------|-----------|----------------|------------------|
| ...   | ...    | ...         | ...       | ...            | ...              |

**Portfolio Metrics:**
- Expected Return: X.XX%
- Expected Volatility: X.XX%
- Sharpe Ratio: X.XX
- Tracking Error vs. Benchmark: X.XX%
- Information Ratio: X.XX

**Constraints Status:**
- [Binding / Not binding] for each constraint
```

### Supporting Artifacts:
- **Efficient frontier chart data** -- return/risk pairs for 20 portfolios along the frontier
- **Weight sensitivity table** -- how weights change as target return varies
- **Risk decomposition** -- contribution of each position to total portfolio risk
- **Rebalancing schedule** -- next rebalancing date and expected turnover

---

## Quality Gates & Completion Criteria

- [ ] All input assumptions are documented (source of expected returns, covariance estimation method)
- [ ] Weights sum to 100% (or intended leverage ratio)
- [ ] No position exceeds stated max weight constraint
- [ ] Tracking error is within the stated budget
- [ ] Risk contributions are reported for each position
- [ ] Sensitivity analysis has been run (return perturbation, covariance stress)
- [ ] Rebalancing rules are specified (frequency, threshold, tax treatment)
- [ ] Output includes comparison to at least one alternative (equal-weight, market-cap, or prior portfolio)

**Success metric:** A portfolio manager reading the output should have all the information needed to implement the portfolio, including weights, constraints, rebalancing rules, and risk expectations.

**Escalation triggers:**
- Covariance matrix is not positive semi-definite --> flag and offer nearest PSD approximation
- Optimizer produces extreme weights (>50% in one asset) --> add constraints and re-run
- Expected returns are implausible (>30% annualized for any asset) --> challenge the assumption
- Tracking error exceeds mandate limit --> tighten constraints or reduce active bets

---

## Hard Constraints

- **NEVER** fabricate expected returns, volatilities, or correlations
- **NEVER** present optimization output without documenting input assumptions
- **NEVER** recommend leverage without explicitly flagging the additional risk
- **ALWAYS** report tracking error when a benchmark is specified
- **ALWAYS** run sensitivity analysis on mean-variance outputs (they are notoriously unstable)
- **ALWAYS** flag when constraints are binding -- this tells the user where the optimizer is being limited
- If the user provides returns without a covariance matrix, **require** the covariance matrix before optimizing

---

## Common Pitfalls

1. **Trusting mean-variance outputs blindly:** MVO is extremely sensitive to expected return inputs. A 0.5% change in expected return for one asset can flip the entire portfolio. --> Always run sensitivity analysis and consider Black-Litterman as a more stable alternative.

2. **Ignoring estimation error:** Sample covariance matrices estimated from short histories are noisy. --> Use shrinkage estimators (Ledoit-Wolf) or factor-based covariance models for more than 20 assets.

3. **Overfitting to historical data:** A portfolio optimized on the last 5 years of data may perform poorly in the next 5. --> Out-of-sample testing, regime-aware construction, and robust optimization help mitigate this.

4. **Neglecting transaction costs:** The optimal portfolio on paper requires 40% turnover per quarter, eating the alpha. --> Always include turnover constraints and estimate the break-even alpha after costs.

5. **Risk parity without understanding leverage:** Unlevered risk parity dramatically underperforms equities in bull markets. The strategy only works at target volatility with leverage. --> Always discuss the leverage decision explicitly.

6. **Factor construction with unintended bets:** A "value" sort may inadvertently load on small-cap, low-momentum, or sector concentration. --> Always check multi-factor exposures after construction.

7. **Tax-lot ignorance in taxable accounts:** Rebalancing without considering tax lots can trigger unnecessary short-term capital gains. --> Implement the tax-lot hierarchy (losses first, then long-term gains, then short-term gains).

---

## Related Skills

- After constructing the portfolio, use **`/attribution`** to decompose performance
- For risk analytics and stress testing, use **`/risk`**
- For single-name idea evaluation within the portfolio, use **`/long-short`**
- For goals-based portfolio construction, use **`/wealth`**
- For factor signal research, use **`/quant`**
