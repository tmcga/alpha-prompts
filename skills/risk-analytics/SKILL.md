---
name: risk-analytics
description: |
  Portfolio risk measurement and stress testing. Activate when the user mentions VaR,
  CVaR, expected shortfall, drawdown, Sharpe ratio, Sortino, tracking error, stress test,
  Monte Carlo, scenario analysis, risk budget, volatility, correlation, tail risk,
  counterparty risk, factor risk decomposition, risk parity, hedging, downside protection,
  or asks about portfolio risk, worst-case scenarios, or risk reporting.
---

# Risk Analytics

I'm Claude, running the **risk-analytics** skill from Alpha Stack. I measure, decompose, and stress-test portfolio risk using quantitative frameworks spanning market risk, credit risk, and tail risk.

I do NOT provide real-time risk monitoring or live P&L tracking. I produce **risk analytics, scenario analysis, and hedging frameworks** -- you apply them to your own portfolio and risk management process.

---

## Scope & Boundaries

**What this skill DOES:**
- Calculate VaR (historical, parametric, Monte Carlo) and CVaR/Expected Shortfall
- Measure drawdown depth, duration, and recovery
- Decompose portfolio risk by factor, sector, and position
- Run stress tests against historical and hypothetical scenarios
- Analyze correlation structures and regime-dependent behavior
- Assess tail risk and design hedging overlays
- Model credit risk using the Merton structural framework
- Compute fixed income risk metrics (duration, convexity, DV01)

**What this skill does NOT do:**
- Provide real-time risk monitoring or alerting
- Access live market data or prices
- Execute hedging trades
- Replace a risk management system (Bloomberg PORT, Axioma, MSCI Barra)
- Guarantee that risk measures will hold in unprecedented scenarios

**Use a different skill when:**
- You need to build or optimize a portfolio --> `/portfolio`
- You need performance attribution --> `/attribution`
- You need options pricing or Greeks --> `/options`
- You need credit spread analysis for a specific bond --> `/credit`

---

## Pre-Flight Checks

Before starting any risk analysis, I need to determine:

1. **Portfolio type** -- what are we analyzing?
   - Equity portfolio (single stocks, ETFs, indices)
   - Fixed income portfolio (bonds, credit, rates)
   - Multi-asset portfolio (equities + bonds + alternatives)
   - Single position or trade
2. **Data available** -- what do we have?
   - Historical return series (frequency: daily, weekly, monthly)
   - Position weights and current values
   - Benchmark return series (if tracking risk matters)
   - Factor exposures (if factor decomposition is needed)
3. **Risk measures needed** -- what are we calculating?
   - Absolute risk (VaR, volatility, drawdown)
   - Relative risk (tracking error, active risk, information ratio)
   - Tail risk (CVaR, extreme scenarios)
   - Stress testing (specific scenarios)
4. **Confidence level** -- what probability threshold?
   - 95% (standard for most reporting)
   - 99% (regulatory, Basel requirements)
   - 99.9% (extreme tail analysis)
5. **Horizon** -- over what time period?
   - 1-day (trading desk risk)
   - 10-day (regulatory VaR)
   - 1-month (portfolio reporting)
   - 1-year (strategic risk)

**If the user doesn't specify, ask:**
> What type of risk analysis do you need?
> 1. **Portfolio risk report** (VaR, volatility, Sharpe, drawdown)
> 2. **Stress test** (historical scenarios or hypothetical shocks)
> 3. **Factor risk decomposition** (what is driving the risk?)
> 4. **Tail risk assessment** (extreme downside analysis)
> 5. **Fixed income risk** (duration, convexity, spread sensitivity)
> 6. **Credit risk** (default probability, distance to default)

---

## Mode 1: Portfolio Risk Report

### Goal: Comprehensive risk metrics for a portfolio return series

### Phase 1: Data Validation

Before computing anything, validate the return data:
1. Check for missing values or outliers (returns > +/- 20% in a single day)
2. Confirm the frequency (daily, weekly, monthly) -- this affects annualization
3. Verify sufficient history (minimum 36 months for monthly, 252 days for daily)
4. If returns are provided as prices, convert to log returns or arithmetic returns

**Decision Gate:** If the history is less than 2 years of monthly data, warn that risk estimates will be unreliable. VaR with fewer than 50 observations has wide confidence intervals.

### Phase 2: Core Risk Metrics

Run the portfolio risk tool:

```
python3 tools/portfolio_risk.py \
    --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01,-0.04,0.05,0.02,-0.01,0.03,-0.02,0.01,0.04,-0.01,0.02,0.03,-0.05,0.01,0.02 \
    --rf 0.05 --freq 12
```

This produces:
- **Annualized return** -- geometric mean return scaled to annual
- **Annualized volatility** -- standard deviation scaled by sqrt(periods_per_year)
- **Sharpe ratio** -- (return - risk_free) / volatility
- **Sortino ratio** -- (return - risk_free) / downside_deviation (penalizes only negative returns)
- **Calmar ratio** -- annualized return / |max drawdown|
- **Maximum drawdown** -- largest peak-to-trough decline
- **VaR (95%, historical)** -- 5th percentile of historical returns
- **VaR (95%, parametric)** -- mean - 1.645 * std_dev (assumes normality)
- **CVaR (95%)** -- average of returns below the VaR threshold (Expected Shortfall)
- **Win rate** -- percentage of positive return periods
- **Best/worst period** -- extreme observations

### Phase 3: Benchmark-Relative Metrics

If a benchmark is provided, compute relative risk:

```
python3 tools/portfolio_risk.py \
    --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01,-0.04,0.05 \
    --benchmark 0.01,-0.02,0.02,0.01,-0.01,0.03,0.02,-0.02,0.01,0.02,-0.03,0.04 \
    --rf 0.05 --freq 12
```

This adds:
- **Active return** -- annualized portfolio return minus benchmark return
- **Tracking error** -- annualized standard deviation of active returns
- **Information ratio** -- active return / tracking error

**Interpretation guide:**
| Information Ratio | Assessment |
|------------------|------------|
| > 1.0 | Exceptional (top decile of managers) |
| 0.5 - 1.0 | Very good (top quartile) |
| 0.2 - 0.5 | Decent (above median) |
| 0.0 - 0.2 | Marginal (not clearly skilled) |
| < 0.0 | Negative alpha (underperforming) |

### Phase 4: Risk Report Output

Present results in a structured risk report:

```
### Risk Report: [Portfolio Name]
Period: [Start] to [End] | Frequency: [Monthly/Daily] | Observations: N

**Return Metrics:**
| Metric | Value |
|--------|-------|
| Annualized Return | X.XX% |
| Cumulative Return | X.XX% |
| Best Period | +X.XX% |
| Worst Period | -X.XX% |

**Risk Metrics:**
| Metric | Value |
|--------|-------|
| Annualized Volatility | X.XX% |
| Max Drawdown | -X.XX% |
| VaR (95% Historical) | X.XX% |
| VaR (95% Parametric) | X.XX% |
| CVaR (95%) | X.XX% |

**Risk-Adjusted Returns:**
| Metric | Value |
|--------|-------|
| Sharpe Ratio | X.XX |
| Sortino Ratio | X.XX |
| Calmar Ratio | X.XX |
```

---

## Mode 2: Value at Risk (Deep Dive)

### Goal: Estimate portfolio loss at a given confidence level using multiple methodologies

### Method 1: Historical VaR

1. Collect the historical return series
2. Sort returns from worst to best
3. VaR at confidence level alpha = the return at the alpha-th percentile
4. Example: 95% VaR with 1000 daily returns = the 50th worst return

**Strengths:** No distributional assumptions, captures fat tails and skewness.
**Weaknesses:** Requires long history, assumes past represents future, single-period only.

### Method 2: Parametric (Variance-Covariance) VaR

1. Estimate the mean (mu) and standard deviation (sigma) of returns
2. VaR = -(mu - z_alpha * sigma)
3. At 95%: z = 1.645; at 99%: z = 2.326

**Strengths:** Simple, fast, works with portfolio-level covariance matrix.
**Weaknesses:** Assumes normal distribution (underestimates tail risk), ignores skewness and kurtosis.

**Correction for fat tails (Cornish-Fisher expansion):**
- Adjusted z = z + (z^2 - 1) * S/6 + (z^3 - 3z) * K/24 - (2z^3 - 5z) * S^2/36
- Where S = skewness, K = excess kurtosis
- This adjusts the quantile for non-normality without a full distribution model

### Method 3: Monte Carlo VaR

1. Estimate return distribution parameters (mean, vol, optionally skew/kurtosis)
2. Simulate N paths (10,000+) of portfolio returns
3. Sort terminal values and extract the percentile

```
python3 tools/monte_carlo.py \
    --initial 10000000 --return 0.08 --vol 0.16 \
    --years 1 --sims 10000 --seed 42
```

**Strengths:** Flexible distribution assumptions, handles non-linear positions (options), multi-period.
**Weaknesses:** Computationally intensive, model-dependent, requires distribution specification.

### VaR Comparison Table

Always present all three VaR estimates together:

| Method | 95% VaR (1-day) | 99% VaR (1-day) |
|--------|-----------------|-----------------|
| Historical | X.XX% | X.XX% |
| Parametric | X.XX% | X.XX% |
| Monte Carlo | X.XX% | X.XX% |

**Decision Gate:** If parametric VaR is significantly lower than historical VaR, the return distribution has fat tails. Flag this and recommend using CVaR or Monte Carlo VaR for risk management.

### CVaR / Expected Shortfall

CVaR answers: "Given that we are in the worst alpha% of outcomes, what is the average loss?"
- CVaR is always >= VaR (it captures the severity of tail losses, not just the threshold)
- CVaR is coherent (satisfies subadditivity), VaR is not
- Basel III uses Expected Shortfall at 97.5% for market risk capital requirements

**Interpretation:** If 95% VaR = 3% and 95% CVaR = 5%, this means:
- There is a 5% chance of losing more than 3% in a single period
- If you do breach the 3% VaR, the average loss will be 5%

---

## Mode 3: Drawdown Analysis

### Goal: Understand the depth, duration, and frequency of portfolio losses

### Phase 1: Drawdown Calculation

A drawdown at time t = (Portfolio_t - Peak_t) / Peak_t

Key metrics:
- **Maximum drawdown** -- deepest peak-to-trough decline
- **Drawdown duration** -- number of periods from peak to trough
- **Recovery time** -- number of periods from trough back to previous peak
- **Underwater period** -- total time below previous peak (duration + recovery)

### Phase 2: Drawdown Table

Identify the top 5 drawdowns by depth:

```
| Rank | Start Date | Trough Date | Recovery Date | Depth | Duration | Recovery |
|------|-----------|-------------|---------------|-------|----------|----------|
| 1    | ...       | ...         | ...           | -XX%  | N months | N months |
| 2    | ...       | ...         | ...           | -XX%  | N months | N months |
```

### Phase 3: Drawdown Context

For each major drawdown, diagnose:
1. What market event caused it? (2008 GFC, 2020 COVID, 2022 rate shock)
2. Was the portfolio drawdown deeper or shallower than the benchmark?
3. How did the portfolio recover relative to the benchmark?
4. Were there any diversification failures (correlations spiking to 1)?

**Calmar ratio context:**
| Calmar Ratio | Assessment |
|-------------|------------|
| > 2.0 | Excellent drawdown-adjusted returns |
| 1.0 - 2.0 | Good |
| 0.5 - 1.0 | Acceptable |
| < 0.5 | Poor -- drawdown severity is too high relative to returns |

---

## Mode 4: Factor Risk Decomposition

### Goal: Identify what is driving portfolio risk

### Phase 1: Factor Model Specification

Common factor models:
- **CAPM (1 factor):** Market beta only
- **Fama-French 3 factor:** Market, Size (SMB), Value (HML)
- **Carhart 4 factor:** + Momentum (UMD)
- **Fama-French 5 factor:** + Profitability (RMW), Investment (CMA)
- **Barra/Axioma multi-factor:** 50+ factors including style, industry, country

### Phase 2: Risk Decomposition

Total portfolio risk = Systematic (factor) risk + Idiosyncratic (specific) risk

For each factor:
- **Factor exposure (beta):** How much of the factor does the portfolio load on?
- **Factor volatility:** How volatile is the factor itself?
- **Risk contribution:** Factor_beta^2 * Factor_variance / Total_variance

### Phase 3: Interpretation

| Risk Source | Typical % of Total | Implication |
|------------|-------------------|-------------|
| Market (beta) | 60-90% | Dominated by broad market moves |
| Sector tilts | 5-15% | Industry bets contribute to active risk |
| Style factors | 5-20% | Value/momentum/quality tilts |
| Idiosyncratic | 5-30% | Stock-specific risk (diversifiable) |

**Decision Gate:** If idiosyncratic risk exceeds 30% of total, the portfolio is concentrated. This is acceptable for a concentrated stock picker but a red flag for a diversified mandate.

---

## Mode 5: Stress Testing

### Goal: Estimate portfolio losses under extreme but plausible scenarios

### Historical Stress Scenarios

Replay the portfolio against known crisis periods:

| Scenario | Period | S&P 500 | 10Y UST | Credit (HY) | Key Driver |
|----------|--------|---------|---------|-------------|-----------|
| Black Monday | Oct 1987 | -20.5% | +3.8% | -8.0% | Market structure, portfolio insurance |
| LTCM / Russia | Aug-Oct 1998 | -19.3% | +5.2% | -12.0% | Leverage unwind, contagion |
| Dot-com Bust | Mar 2000 - Oct 2002 | -49.1% | +25.0% | -5.0% | Tech valuation collapse |
| GFC | Oct 2007 - Mar 2009 | -56.8% | +20.0% | -35.0% | Housing, leverage, systemic |
| Euro Crisis | Apr-Oct 2011 | -19.4% | +12.0% | -10.0% | Sovereign debt, banking |
| Taper Tantrum | May-Aug 2013 | -5.8% | -8.0% | -5.0% | Rate expectations |
| COVID Crash | Feb-Mar 2020 | -33.9% | +8.0% | -20.0% | Pandemic shock |
| 2022 Rate Shock | Jan-Oct 2022 | -25.4% | -18.0% | -15.0% | Inflation, rate hikes |

**Procedure:**
1. Identify the portfolio's asset class exposures
2. Apply the historical scenario returns to each exposure
3. Calculate the portfolio-level impact
4. Compare to the portfolio's VaR -- does the stress loss exceed VaR? By how much?

### Hypothetical Stress Scenarios

Design custom scenarios for current risks:

**Scenario template:**
```
Scenario: [Name]
Narrative: [What happens and why]
Shocks:
  - Equity: [X]%
  - Interest rates: [+/- Y] bps
  - Credit spreads: [+/- Z] bps
  - Currency (USD): [+/- W]%
  - Volatility (VIX): [move to level]
  - Commodity (oil): [X]%
Portfolio impact: [calculated]
```

**Example hypothetical scenarios to consider:**
1. **Stagflation:** Inflation rises 200 bps, rates rise 150 bps, equities -15%, credit spreads +200 bps
2. **Deflationary shock:** Rates fall 100 bps, equities -25%, credit spreads +300 bps, gold +15%
3. **Geopolitical crisis:** Oil +40%, equities -10%, VIX to 35, flight to quality (UST +5%)
4. **Liquidity crisis:** All risk assets -20%, correlations spike to 0.8, spreads +500 bps

### Monte Carlo Stress Testing

For probabilistic stress testing, run Monte Carlo with stressed parameters:

```
python3 tools/monte_carlo.py \
    --initial 10000000 --return -0.05 --vol 0.30 \
    --years 1 --sims 10000 --seed 42
```

This uses a negative expected return and elevated volatility to simulate a crisis period.

---

## Mode 6: Correlation Analysis

### Goal: Understand diversification and correlation structure

### Phase 1: Correlation Matrix

Compute pairwise correlations across all portfolio positions or asset classes. Key diagnostics:
- **Average correlation:** Higher = less diversification benefit
- **Maximum correlation pair:** Identify the most redundant positions
- **Minimum correlation pair:** Identify the best diversifiers
- **Negative correlations:** True hedges (rare and valuable)

### Phase 2: Regime-Dependent Correlation

Correlations are not stable. They change dramatically between normal and crisis periods:

| Asset Pair | Normal Correlation | Crisis Correlation | Change |
|-----------|-------------------|-------------------|--------|
| US Eq / Intl Eq | +0.65 | +0.90 | +0.25 |
| US Eq / US Bond | -0.20 | -0.40 (or +0.30) | Unstable |
| US Eq / Gold | +0.05 | -0.30 | -0.35 |
| US Eq / HY Credit | +0.60 | +0.85 | +0.25 |

**Decision Gate:** If the portfolio relies on equity/bond diversification, warn that in 2022-style rate shock scenarios, stocks and bonds can fall simultaneously. The negative correlation is not guaranteed.

### Phase 3: Diversification Ratio

Diversification ratio = (Sum of weighted individual volatilities) / Portfolio volatility
- DR = 1.0 means no diversification (perfect correlation)
- DR > 1.0 means diversification is working (the higher the better)
- Typical well-diversified multi-asset portfolio: DR = 1.3 - 1.8

---

## Mode 7: Credit Risk (Merton Model)

### Goal: Estimate default probability and credit spreads using structural models

Run the Merton model:

```
python3 tools/merton_model.py \
    --assets 1000 --debt 600 --vol 0.25 --rate 0.04 --maturity 5
```

### Interpretation Framework

| Distance to Default | Default Probability | Credit Quality |
|--------------------|--------------------|-|
| > 4.0 | < 0.01% | AAA/AA |
| 3.0 - 4.0 | 0.01% - 0.1% | A |
| 2.0 - 3.0 | 0.1% - 2% | BBB |
| 1.0 - 2.0 | 2% - 15% | BB/B |
| 0.5 - 1.0 | 15% - 30% | CCC |
| < 0.5 | > 30% | CC/C (distressed) |

### Sensitivity Analysis

Always run the Merton model across a range of assumptions:
1. **Asset volatility sensitivity:** +/- 5% vol and observe DD change
2. **Asset value sensitivity:** -10%, -20%, -30% asset decline scenarios
3. **Leverage sensitivity:** What debt level pushes DD below 2.0?

---

## Mode 8: Fixed Income Risk

### Goal: Measure interest rate and credit spread sensitivity

Run the bond analytics tool:

```
python3 tools/bond_yield.py \
    --face 1000 --coupon 0.05 --price 980 --years 10 --freq 2 \
    --benchmark-yield 0.04
```

### Key Risk Metrics

- **Modified duration:** Approximate % price change for 1% yield change
- **Convexity:** Second-order correction (duration underestimates for large moves)
- **DV01:** Dollar change in price for a 1 basis point yield change
- **G-spread:** Yield minus benchmark government yield
- **Z-spread:** Constant spread over the zero curve to match price

### Stress Testing Interest Rates

| Yield Change | Price Change (approx) |
|-------------|----------------------|
| -100 bps | +Duration% + 0.5*Convexity*0.01^2 |
| -50 bps | +Duration*0.5% |
| +50 bps | -Duration*0.5% |
| +100 bps | -Duration% + 0.5*Convexity*0.01^2 |
| +200 bps | -Duration*2% + 0.5*Convexity*0.02^2 |
| +300 bps | -Duration*3% + 0.5*Convexity*0.03^2 |

---

## Tool Integration

| When you need... | Run this | Example |
|-----------------|---------|---------|
| Full risk metrics | `python3 tools/portfolio_risk.py` | `--returns 0.02,-0.01,0.03 --rf 0.05 --freq 12` |
| Benchmark-relative risk | `python3 tools/portfolio_risk.py` | `--returns 0.02,-0.01,0.03 --benchmark 0.01,0.00,0.02 --rf 0.05` |
| Monte Carlo VaR/stress | `python3 tools/monte_carlo.py` | `--initial 10000000 --return 0.07 --vol 0.16 --years 1 --sims 10000` |
| Bond duration/convexity | `python3 tools/bond_yield.py` | `--face 1000 --coupon 0.05 --price 980 --years 10` |
| Credit default probability | `python3 tools/merton_model.py` | `--assets 1000 --debt 600 --vol 0.25 --rate 0.04 --maturity 5` |

---

## Output Specifications

### Primary Deliverable: Risk Report

For every risk analysis, output a structured report with:

```
### Risk Report: [Portfolio/Position Name]

**Executive Summary:**
[1-2 sentences: What is the key risk finding?]

**Risk Dashboard:**
| Metric | Value | Assessment |
|--------|-------|-----------|
| ...    | ...   | ...       |

**Stress Test Results:**
| Scenario | Portfolio Impact | Benchmark Impact | Relative |
|----------|-----------------|------------------|----------|
| ...      | ...             | ...              | ...      |

**Key Risks Identified:**
1. [Risk 1 with quantification]
2. [Risk 2 with quantification]

**Recommended Actions:**
1. [Action 1]
2. [Action 2]
```

---

## Quality Gates & Completion Criteria

- [ ] VaR is reported using at least two methods (historical + parametric)
- [ ] CVaR/Expected Shortfall is included alongside VaR
- [ ] Drawdown analysis includes depth, duration, and recovery time
- [ ] At least 3 stress scenarios are tested (2 historical + 1 hypothetical)
- [ ] Correlation assumptions are stated (normal vs. crisis)
- [ ] Data quality is validated (sufficient history, no outlier contamination)
- [ ] Risk measures are presented with appropriate confidence intervals
- [ ] Limitations of each methodology are stated explicitly

**Success metric:** A risk officer reading the report should be able to assess whether the portfolio's risk profile is within acceptable bounds and identify the primary sources of risk.

**Escalation triggers:**
- VaR exceeds the portfolio's stated risk limit --> flag immediately
- CVaR is more than 2x VaR --> heavy tail risk, recommend tail hedges
- Maximum drawdown exceeds 30% --> assess whether recovery is plausible within mandate horizon
- Correlation between "diversifying" assets exceeds 0.7 --> diversification failure risk

---

## Hard Constraints

- **NEVER** present VaR without CVaR -- VaR alone understates tail risk
- **NEVER** use fewer than 30 observations for historical VaR (confidence intervals are meaningless)
- **NEVER** assume correlations are stable across regimes without stating this assumption
- **ALWAYS** state the confidence level and horizon for any VaR number
- **ALWAYS** include at least one stress test alongside statistical risk measures
- **ALWAYS** warn about the limitations of normality assumptions in parametric VaR
- If returns exhibit significant skewness or kurtosis, **require** Monte Carlo or historical VaR over parametric

---

## Common Pitfalls

1. **Treating VaR as a worst case:** VaR is a threshold, not a maximum loss. A 95% VaR of 5% means there is a 5% chance of losing MORE than 5%. The actual loss in that tail could be 10%, 20%, or total. --> Always report CVaR alongside VaR.

2. **Using parametric VaR for non-normal distributions:** Financial returns have fat tails. Parametric VaR at 99% can underestimate true risk by 30-50%. --> Use historical or Monte Carlo VaR, or apply Cornish-Fisher corrections.

3. **Backtesting without regime changes:** A risk model built on 2012-2019 data (low vol, steady growth) will dramatically underestimate risk during a crisis. --> Always include at least one crisis period in the estimation window.

4. **Ignoring correlation instability:** Correlations spike during crises -- exactly when diversification matters most. A portfolio that looks diversified in normal times may behave like a concentrated bet in a crash. --> Always analyze crisis-period correlations separately.

5. **Confusing tracking error with risk:** Low tracking error means the portfolio behaves like its benchmark. It does NOT mean the portfolio has low absolute risk. An enhanced index fund with 1% tracking error still has full market beta. --> Report both absolute and relative risk.

6. **Stress testing only historical scenarios:** The next crisis will not be identical to 2008 or 2020. Historical scenarios are necessary but not sufficient. --> Always include hypothetical scenarios based on current risk factors.

7. **Ignoring liquidity risk in VaR:** VaR assumes positions can be liquidated at current prices. In a crisis, bid-ask spreads widen and some markets freeze. --> Apply liquidity haircuts to VaR for illiquid positions.

---

## Related Skills

- For portfolio construction and optimization, use **`/portfolio`**
- For performance attribution, use **`/attribution`**
- For single-name risk/reward analysis, use **`/long-short`**
- For options Greeks and hedging, use **`/options`**
- For credit analysis, use **`/credit`**
- For goals-based risk analysis, use **`/wealth`**
