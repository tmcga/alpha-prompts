# Active Equity Management

```
You are a senior portfolio manager running a $5-20B active equity strategy benchmarked
to a major index. You have 15+ years of experience in fundamental stock selection,
portfolio construction, and performance attribution. You think in terms of alpha
generation within a tracking error budget, active share, and information ratio
optimization. Every position must have a variant view relative to consensus, a clear
catalyst timeline, and an explicit sizing rationale based on conviction and benchmark
weight. You are deeply aware of fee pressure, capacity constraints at scale, and
fiduciary obligations to pension funds, endowments, and retail investors. You integrate
ESG considerations as material risk factors rather than exclusionary screens.
```

## What This Desk Does

The active equity team selects individual stocks to generate alpha relative to a benchmark index (e.g., S&P 500, MSCI EAFE, Russell 2000) within a defined risk budget. Unlike hedge funds, positions are primarily long-only and sized relative to benchmark weight — an overweight is a bet, an underweight is a bet, and a zero-weight is the largest possible underweight bet. The team must balance conviction-weighted stock selection against tracking error constraints, sector exposure limits, and factor tilt guidelines set by the investment policy. Performance is measured by information ratio and Brinson attribution over rolling 3- and 5-year periods, with fee-adjusted returns increasingly under scrutiny from consultants and allocators.

---

## 1. Stock Selection Within a Risk Framework

Generating alpha while respecting the tracking error budget and benchmark-relative constraints that define institutional equity mandates.

**Core relationship:** Information Ratio = Alpha / Tracking Error

**Fundamental Law of Active Management:** IR = IC x sqrt(BR) x TC

Where IC = information coefficient (skill), BR = breadth (independent bets per year), TC = transfer coefficient (how much of the signal survives constraints).

**Active share:** AS = (1/2) x sum(|w_portfolio_i - w_benchmark_i|) for all holdings i

### Alpha-Aware Position Sizing

```
I manage a [benchmark]-benchmarked equity portfolio with:
- AUM: $[X]B
- Tracking error budget: [X] bps annualized
- Active share target: [X]%
- Maximum single-name active weight: [X] bps
- Current number of holdings: [N] (benchmark has [M] names)

I want to add or resize a position in [TICKER]:
- Benchmark weight: [X]%
- Current portfolio weight: [X]%
- My conviction level: [high / medium / low]
- Alpha estimate (annualized): [X] bps
- Idiosyncratic volatility: [X]%
- Beta to benchmark: [X]

Help me determine:
1. Optimal active weight given my alpha estimate and the stock's idiosyncratic risk
   - Use: optimal_active_weight = (alpha_i / (lambda * sigma_idio_i^2)) where lambda = risk aversion
2. Impact on portfolio tracking error (marginal contribution to tracking error)
3. Whether this position crowds existing factor exposures (momentum, value, quality, size)
4. How the position interacts with my existing sector overweight/underweight in [sector]
5. Kill criteria: at what loss level or thesis invalidation should I cut to benchmark weight?

Framework: Position size should reflect alpha / (risk aversion x residual variance).
A 100bp active overweight in a 3% benchmark name is very different from 100bp in a 20bp name.
```

### Variant View Documentation

```
I'm building a research case for [TICKER] as an active overweight of [X] bps vs benchmark.

Company: [name], Market cap: $[X]B, Sector: [sector]
Benchmark weight: [X]%, Current portfolio weight: [X]%

Help me structure a variant view analysis:

1. **Consensus view**: What does the street expect? (EPS, revenue growth, margins, multiples)
   - Consensus EPS: $[X], Revenue growth: [X]%, Forward P/E: [X]x
2. **My variant view**: Where do I disagree and why?
   - [describe the specific disagreement — new product cycle, margin inflection, balance sheet optionality, etc.]
3. **Catalyst timeline**: What events will prove or disprove my thesis?
   - [earnings date, product launch, regulatory decision, capital return announcement]
4. **Competitive dynamics**: Porter's five forces assessment, market share trajectory, pricing power
5. **Management assessment**: Capital allocation track record, insider ownership, compensation alignment
6. **Valuation bridge**: If my thesis is correct, what is the stock worth?
   - Bull case: $[X] ([X]x target multiple on my EPS of $[X])
   - Base case: $[X]
   - Bear case: $[X]
7. **Risk/reward asymmetry**: Upside to bull / downside to bear = [X]:1

Position sizing rule: Active weight proportional to (conviction x risk-reward asymmetry) / idiosyncratic_vol
```

---

## 2. Fundamental Research Process

The analytical workflow from initial screen to investment thesis, including earnings modeling and competitive analysis.

### Earnings Model and Estimate Revision Analysis

```
I'm building a detailed earnings model for [TICKER] to identify where consensus may be wrong.

Current consensus:
- Revenue: $[X]B (growth [X]%)
- Gross margin: [X]%
- Operating margin: [X]%
- EPS: $[X]
- FCF: $[X]B

Help me build a bottom-up revenue model and margin framework:

1. **Revenue decomposition**: Break revenue into segments/geographies/products
   - Segment 1: [name] — volume x price x mix analysis
   - Segment 2: [name] — recurring vs transactional, contract backlog
2. **Margin drivers**: Input costs, operating leverage, mix shift, pricing power
   - Gross margin sensitivity: +/- [X]% commodity prices = +/- [X] bps gross margin
3. **Earnings surprise potential**: Where is consensus most likely wrong?
   - Identify line items with highest variance and lowest analyst attention
4. **Estimate revision trajectory**: Is the revision cycle inflecting up or down?
   - 3-month EPS revision: [X]%, breadth of revisions: [X]% up vs [X]% down
5. **Quality of earnings**: Cash conversion, accruals ratio, receivables/inventory trends
   - Sloan accrual ratio = (net income - CFO - CFI) / total assets (flag if > 10%)
6. **Scenario matrix**: Revenue growth x margin = EPS matrix, map to valuation

Analytical edge often comes from modeling what consensus ignores: working capital,
below-the-line items, segment mix, or FX translation effects.
```

---

## 3. Portfolio Construction for Benchmarked Mandates

Building and managing a portfolio that maximizes alpha per unit of active risk within institutional constraints.

**Tracking error:** TE = sqrt(w_active' x Sigma x w_active) where w_active = w_portfolio - w_benchmark

**Key constraint set:** Sector deviations (+/- X%), single name active weight caps, factor tilt bounds, turnover limits, cash drag minimization.

### Portfolio Construction Optimization

```
I need to construct/rebalance my active equity portfolio with these parameters:

Mandate: [benchmark] benchmarked, [long-only / 130-30 / market neutral extension]
AUM: $[X]B
Tracking error target: [X] bps
Active share target: [X]% (current: [X]%)
Turnover budget: [X]% per annum (one-way)

Current portfolio diagnostics:
- Number of holdings: [N]
- Top 10 active overweights: [list with active weights]
- Largest sector deviation: [sector] at [X]% vs benchmark [X]%
- Factor tilts: momentum [X] sigma, value [X] sigma, quality [X] sigma, size [X] sigma

Help me:
1. Identify the binding constraint — is TE, active share, turnover, or sector limits the bottleneck?
2. Optimize position sizes to maximize expected alpha subject to:
   - TE <= target, sector deviations <= limits, max active weight per name
   - Minimize unintended factor bets (neutralize factors I have no view on)
3. Calculate the transfer coefficient: TC = corr(optimal_unconstrained_weights, actual_weights)
   - IR_constrained = IC x sqrt(BR) x TC (TC < 1 due to constraints)
4. Identify "dead weight" holdings with small active weights that consume turnover but add little alpha
5. Assess cash drag: [X]% cash vs fully invested = [X] bps annual drag at [X]% benchmark return
6. Tax lot optimization: harvest losses while maintaining desired exposures

Active share decomposition:
- Stock selection component: [X]%
- Sector allocation component: [X]%
- Interaction component: [X]%
```

---

## 4. Performance Attribution

Decomposing returns to understand sources of alpha and identify persistent skill versus luck.

**Brinson-Fachler attribution model:**

- Allocation effect (sector): sum_j (w_pj - w_bj) x (R_bj - R_b)
- Selection effect (stock picking): sum_j w_bj x (R_pj - R_bj)
- Interaction effect: sum_j (w_pj - w_bj) x (R_pj - R_bj)
- Total active return = allocation + selection + interaction

**Factor attribution:** R_active = sum_k (beta_pk - beta_bk) x F_k + alpha_residual

### Brinson Attribution Analysis

```
Analyze the performance attribution for my portfolio over [period]:

Portfolio return: [X]% (gross), [X]% (net of fees)
Benchmark return: [X]%
Active return: [X] bps (gross)
Tracking error (realized): [X] bps
Information ratio: [X]

Sector-level data (portfolio weight, benchmark weight, portfolio return, benchmark return):
- Technology: [Wp]%, [Wb]%, [Rp]%, [Rb]%
- Healthcare: [Wp]%, [Wb]%, [Rp]%, [Rb]%
- Financials: [Wp]%, [Wb]%, [Rp]%, [Rb]%
- [continue for all sectors]

Help me:
1. Calculate Brinson-Fachler attribution: allocation, selection, and interaction for each sector
2. Identify whether alpha came from sector bets (top-down) or stock picking (bottom-up)
3. Run factor attribution: How much active return is explained by factor tilts vs residual alpha?
   - Regress active returns on: Mkt-Rf, SMB, HML, UMD, QMJ, BAB
   - Residual alpha (intercept) = true stock-picking skill
4. Evaluate consistency: What is my hit rate (% of months with positive active return)?
   - Hit rate > 50% with positive skew suggests skill; hit rate < 50% with a few big wins suggests luck/concentration
5. Peer comparison: Where does my IR rank vs [peer universe]? Is it statistically significant?
   - t-stat of IR = IR x sqrt(T_years). Need t > 2.0 for significance at 95% confidence.
6. Attribution of attribution: Was positive selection effect driven by 2-3 big winners (concentrated)
   or broad-based stock picking (diversified skill)?
```

### Factor Attribution Regression

```
Run a factor attribution analysis on my portfolio's active returns:

Monthly active return time series: [provide or describe period]
Benchmark: [index]
Factor model: [Fama-French 5-factor + momentum / Barra / Axioma / custom]

Regression specification:
R_active_t = alpha + b1*MktRf_t + b2*SMB_t + b3*HML_t + b4*RMW_t + b5*CMA_t + b6*UMD_t + epsilon_t

Help me interpret:
1. Which factors explain my active return? (significant betas = unintended factor bets)
2. Is the alpha (intercept) statistically significant? (t-stat > 2.0)
3. What is the R-squared? (high R2 = returns mostly from factor tilts, not stock picking)
4. Factor timing: Are my factor exposures time-varying? Run rolling 12-month regressions.
5. Appraisal ratio = alpha / sigma(epsilon) — pure stock-picking skill measure
6. Information ratio decomposition: IR_total = IR_factor_timing + IR_stock_selection

If R2 > 0.5 and alpha is insignificant, I'm running an expensive factor portfolio —
consider whether a cheaper smart beta product delivers the same exposures.
```

---

## 5. ESG Integration

Incorporating environmental, social, and governance factors as material risk and return drivers within the investment process.

### ESG Materiality Assessment

```
I need to assess ESG materiality for [TICKER] in the [sector] sector.

Current ESG data:
- MSCI ESG rating: [AAA to CCC]
- Sustainalytics risk score: [X]
- Carbon intensity: [X] tCO2e / $M revenue
- Board independence: [X]%
- Gender diversity (board/management): [X]% / [X]%
- Controversy incidents (past 3 years): [describe]

Help me build a materiality-weighted ESG assessment:

1. **Sector-specific materiality map** (SASB framework):
   - Which E, S, and G factors are financially material for [sector]?
   - Rank by impact magnitude and probability
2. **Quantitative ESG scoring**:
   - Weight each material factor by financial impact
   - Score company vs sector peers on each factor (1-5 scale)
   - Composite ESG score = sum(weight_i x score_i) for material factors only
3. **Alpha implications**:
   - ESG momentum: Is the company improving or deteriorating on key metrics?
   - Regulatory risk: Exposure to carbon pricing, supply chain regulation, disclosure mandates
   - Valuation impact: ESG leaders trade at [X]x premium — is it justified by lower risk?
4. **Engagement framework**: If we own the stock, what governance improvements should we push for?
   - Priority issues ranked by feasibility x impact
5. **Portfolio-level ESG**: How does this position affect portfolio carbon intensity, ESG score, and
   alignment with [UN SDGs / Paris alignment / net-zero commitment]?

Integration principle: ESG is a risk factor, not a values screen. Material ESG risks
that are mispriced by the market create alpha opportunities in both directions.
```

### ESG Impact Measurement

```
Measure the ESG impact and alignment of my portfolio for client reporting:

Portfolio: [name], AUM: $[X]B, Benchmark: [index]
Client mandate: [describe ESG requirements — exclusions, tilts, impact targets]

Provide:
1. **Carbon footprint**: Portfolio weighted average carbon intensity vs benchmark
   - WACI = sum(w_i x carbon_intensity_i) for portfolio vs benchmark
   - Scope 1+2 and Scope 1+2+3 if available
2. **Temperature alignment**: Implied temperature rise based on portfolio emissions trajectory
3. **SDG alignment**: Map portfolio holdings to UN Sustainable Development Goals
4. **Controversy screening**: Holdings with severe controversies (UNGC violations, environmental fines)
5. **Active ESG contribution**: How much of my active weight is in ESG improvers vs laggards?
6. **Stewardship report**: Proxy voting record, engagement activities, escalation actions

Frameworks: TCFD reporting structure, EU SFDR classification (Article 6/8/9),
PRI reporting requirements, GRESB for real assets.
```

---

## Mathematical Reference

**Information Ratio:** IR = E[R_p - R_b] / std(R_p - R_b) = alpha / tracking_error

**Fundamental Law of Active Management:** IR = IC x sqrt(BR) x TC

**Active Share:** AS = (1/2) x sum_i |w_pi - w_bi|. Active share > 60% = truly active. Active share < 20% = closet indexer.

**Brinson Attribution:**
- Allocation_j = (w_pj - w_bj) x (R_bj - R_b)
- Selection_j = w_bj x (R_pj - R_bj)
- Interaction_j = (w_pj - w_bj) x (R_pj - R_bj)

**Optimal Active Weight (mean-variance):** delta_w_i = alpha_i / (lambda x sigma_idio_i^2)

**Tracking Error (ex-ante):** TE = sqrt(w_active' x Sigma x w_active)

**Transfer Coefficient:** TC = corr(alpha_signal, actual_active_weights x sigma). Measures how much of the alpha signal survives portfolio constraints. Unconstrained TC = 1.0; typical constrained TC = 0.4-0.7.

---

## See Also

- [Systematic & Factor Investing](systematic-factor.md) — factor models that overlap with style tilts in active portfolios
- [Risk & Performance Analytics](risk-analytics.md) — deeper risk decomposition and VaR frameworks
- [Multi-Asset Allocation](multi-asset.md) — how active equity fits within a total portfolio context
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — foundational quant frameworks, alpha research, and portfolio construction
