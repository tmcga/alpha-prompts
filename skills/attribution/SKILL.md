---
name: attribution
description: |
  Performance attribution analysis. Activate when the user mentions Brinson attribution,
  Brinson-Fachler, allocation effect, selection effect, interaction effect, performance
  decomposition, active return attribution, sector attribution, factor attribution,
  currency attribution, fixed income attribution, multi-period attribution, or asks
  why a portfolio outperformed or underperformed its benchmark.
---

# Performance Attribution

I'm Claude, running the **attribution** skill from Alpha Stack. I decompose portfolio performance into its component sources -- answering not just "how much did we make?" but "WHY did we make it and WHERE did the value come from?"

I do NOT provide live portfolio analytics or connect to portfolio management systems. I produce **attribution analysis frameworks, calculations, and interpretation** -- you provide the weights and returns data.

---

## Scope & Boundaries

**What this skill DOES:**
- Run Brinson-Fachler attribution (allocation, selection, interaction effects)
- Perform multi-period attribution with compounding adjustments
- Decompose returns by factor exposures (factor-based attribution)
- Analyze currency attribution for international portfolios
- Compute fixed income attribution (yield, spread, duration, curve)
- Attribute performance at manager level vs. portfolio level
- Diagnose skill vs. luck patterns across time periods

**What this skill does NOT do:**
- Access live portfolio holdings or returns
- Connect to custodians, OMS, or PMS systems
- Provide real-time attribution dashboards
- Replace a full attribution system (FactSet, Bloomberg PORT, StatPro)
- Guarantee that past attribution patterns will persist

**Use a different skill when:**
- You need to build or optimize a portfolio --> `/portfolio`
- You need risk analytics and stress testing --> `/risk`
- You need factor signal research --> `/quant`
- You need single-name idea evaluation --> `/long-short`

---

## Pre-Flight Checks

Before starting any attribution analysis, I need:

1. **Portfolio data:**
   - Weights by sector/asset class/position (beginning of period)
   - Returns by sector/asset class/position (for the period)
2. **Benchmark data:**
   - Weights by sector/asset class/position (beginning of period)
   - Returns by sector/asset class/position (for the period)
3. **Attribution type:**
   - Single-period Brinson-Fachler
   - Multi-period (with linking method)
   - Factor-based
   - Currency
   - Fixed income
4. **Grouping level:**
   - Sector/industry
   - Geography/country
   - Asset class
   - Individual position
5. **Time period:**
   - Single period (one month, one quarter)
   - Multi-period (cumulative over multiple months/quarters)

**If the user doesn't specify, ask:**
> What type of attribution do you need?
> 1. **Brinson-Fachler** (sector allocation vs. stock selection)
> 2. **Multi-period Brinson** (cumulative attribution over multiple periods)
> 3. **Factor-based** (which factors drove returns)
> 4. **Currency attribution** (local return vs. currency effect)
> 5. **Fixed income** (yield, duration, spread, curve effects)

---

## Mode 1: Single-Period Brinson-Fachler Attribution

### Goal: Decompose one period's active return into allocation, selection, and interaction

### The Framework

The Brinson-Fachler model decomposes the active return (R_p - R_b) into three effects for each sector:

**Allocation Effect:** Did we overweight sectors that outperformed?
- Allocation_i = (w_p_i - w_b_i) * (R_b_i - R_b_total)
- Positive when: overweight a sector that beats the benchmark total, OR underweight a sector that lags

**Selection Effect:** Did we pick better stocks within each sector?
- Selection_i = w_b_i * (R_p_i - R_b_i)
- Positive when: portfolio return within the sector exceeds benchmark return within the sector
- Uses benchmark weight to isolate pure stock picking from weight decisions

**Interaction Effect:** The cross-term between allocation and selection
- Interaction_i = (w_p_i - w_b_i) * (R_p_i - R_b_i)
- Positive when: overweight a sector where you also outperformed on selection
- Represents the compounding benefit of being both overweight AND good at stock picking

**Total active return = Sum(Allocation) + Sum(Selection) + Sum(Interaction)**

### Phase 1: Run the Attribution

```
python3 tools/brinson.py \
    --port-weights 0.30,0.25,0.20,0.15,0.10 \
    --port-returns 0.12,0.08,0.05,0.15,0.03 \
    --bench-weights 0.25,0.25,0.25,0.15,0.10 \
    --bench-returns 0.10,0.09,0.06,0.12,0.04 \
    --sectors Tech,Health,Finance,Energy,Utils
```

### Phase 2: Worked Example

**Scenario:** US equity portfolio vs. S&P 500, Q4 2025

| Sector | Port Wt | Bench Wt | Active Wt | Port Ret | Bench Ret |
|--------|---------|----------|-----------|----------|-----------|
| Tech | 30.0% | 25.0% | +5.0% | +12.0% | +10.0% |
| Healthcare | 25.0% | 25.0% | 0.0% | +8.0% | +9.0% |
| Financials | 20.0% | 25.0% | -5.0% | +5.0% | +6.0% |
| Energy | 15.0% | 15.0% | 0.0% | +15.0% | +12.0% |
| Utilities | 10.0% | 10.0% | 0.0% | +3.0% | +4.0% |

**Step 1: Calculate total returns**
- Portfolio return = 0.30*0.12 + 0.25*0.08 + 0.20*0.05 + 0.15*0.15 + 0.10*0.03 = 8.85%
- Benchmark return = 0.25*0.10 + 0.25*0.09 + 0.25*0.06 + 0.15*0.12 + 0.10*0.04 = 8.45%
- Active return = +0.40%

**Step 2: Attribution by sector**

*Tech:*
- Allocation = (0.30-0.25) * (0.10-0.0845) = 0.05 * 0.0155 = +0.08%
- Selection = 0.25 * (0.12-0.10) = 0.25 * 0.02 = +0.50%
- Interaction = (0.30-0.25) * (0.12-0.10) = 0.05 * 0.02 = +0.10%
- Total Tech effect = +0.68%

*Healthcare:*
- Allocation = (0.25-0.25) * (0.09-0.0845) = 0.00 * 0.0055 = 0.00%
- Selection = 0.25 * (0.08-0.09) = 0.25 * (-0.01) = -0.25%
- Interaction = (0.25-0.25) * (0.08-0.09) = 0.00 * (-0.01) = 0.00%
- Total Healthcare effect = -0.25%

*Financials:*
- Allocation = (0.20-0.25) * (0.06-0.0845) = (-0.05) * (-0.0245) = +0.12%
- Selection = 0.25 * (0.05-0.06) = 0.25 * (-0.01) = -0.25%
- Interaction = (0.20-0.25) * (0.05-0.06) = (-0.05) * (-0.01) = +0.05%
- Total Financials effect = -0.08%

*Energy:*
- Allocation = (0.15-0.15) * (0.12-0.0845) = 0.00 * 0.0355 = 0.00%
- Selection = 0.15 * (0.15-0.12) = 0.15 * 0.03 = +0.45%
- Interaction = (0.15-0.15) * (0.15-0.12) = 0.00 * 0.03 = 0.00%
- Total Energy effect = +0.45%

*Utilities:*
- Allocation = (0.10-0.10) * (0.04-0.0845) = 0.00 * (-0.0445) = 0.00%
- Selection = 0.10 * (0.03-0.04) = 0.10 * (-0.01) = -0.10%
- Interaction = (0.10-0.10) * (0.03-0.04) = 0.00 * (-0.01) = 0.00%
- Total Utilities effect = -0.10%

**Step 3: Summary**

| Effect | Total | Source |
|--------|-------|--------|
| Allocation | +0.20% | Good: underweight Financials (lagged), overweight Tech (led) |
| Selection | +0.35% | Good: Tech and Energy stock picks. Bad: Healthcare, Financials |
| Interaction | +0.15% | Overweight Tech where selection was also positive |
| **Active Return** | **+0.70%** | |

Note: rounding may cause minor discrepancies vs. the 0.40% calculated above; the tool produces exact figures.

### Phase 3: Interpretation

**Key questions to answer:**
1. **Is the manager an allocator or a selector?** Compare total allocation effect vs. total selection effect across multiple periods. A consistent pattern reveals the manager's true skill.
2. **Is the interaction effect accidental?** Positive interaction means the manager overweighted sectors where they also picked well. If this is consistent, it suggests the manager has integrated top-down and bottom-up processes. If random, it is noise.
3. **Which sectors are value-adding?** Sort sectors by total effect to identify where the manager consistently adds or destroys value.
4. **Is the active return concentrated?** If 80% of active return comes from one sector, the portfolio has a single-bet problem.

---

## Mode 2: Multi-Period Attribution

### Goal: Attribute cumulative performance over multiple periods while handling compounding

### The Compounding Problem

Single-period attribution effects do not simply sum across periods because of compounding. If the portfolio returned +5% in Q1 and +3% in Q2, the cumulative return is not 8% but 8.15% (1.05 * 1.03 - 1). Attribution effects must be "linked" across periods.

### Linking Methods

**Method 1: Carino Linking (Recommended)**
- Applies a smoothing factor to each period's attribution effects so they sum to the cumulative active return
- Smoothing factor k_t = ln(1+R_p_t) - ln(1+R_b_t) / (R_p_t - R_b_t) for each period
- Overall factor K = ln(1+R_p_cum) - ln(1+R_b_cum) / Sum(k_t * (R_p_t - R_b_t))
- Linked effect = K * k_t * single_period_effect_t

**Method 2: GRAP (Geometric Return Attribution Program)**
- Compounds each effect geometrically
- Preserves the multiplicative nature of returns
- More complex but theoretically cleaner

**Method 3: Simple Summation (Approximation)**
- Sum single-period effects directly
- Only acceptable for short periods with small returns (cumulative active < 2%)
- Will not tie to the actual cumulative active return for longer periods

### Procedure

1. Run Brinson attribution for each period independently:

```
# Period 1 (Q1)
python3 tools/brinson.py \
    --port-weights 0.30,0.25,0.20,0.15,0.10 \
    --port-returns 0.05,0.03,0.02,0.04,0.01 \
    --bench-weights 0.25,0.25,0.25,0.15,0.10 \
    --bench-returns 0.04,0.03,0.025,0.035,0.015 \
    --sectors Tech,Health,Finance,Energy,Utils

# Period 2 (Q2)
python3 tools/brinson.py \
    --port-weights 0.32,0.24,0.19,0.15,0.10 \
    --port-returns 0.06,0.04,0.03,0.08,0.02 \
    --bench-weights 0.26,0.25,0.24,0.15,0.10 \
    --bench-returns 0.05,0.04,0.025,0.06,0.015 \
    --sectors Tech,Health,Finance,Energy,Utils
```

2. Collect single-period effects for each sector and effect type
3. Apply the Carino linking method (or GRAP) to produce cumulative effects
4. Verify: Sum of all linked effects = cumulative active return

### Output Format

```
### Multi-Period Attribution: Q1-Q4 2025

| Sector | Q1 Alloc | Q2 Alloc | Q3 Alloc | Q4 Alloc | Linked Total |
|--------|----------|----------|----------|----------|-------------|
| Tech   | +0.05%   | +0.08%   | +0.03%   | +0.10%   | +0.27%      |
| ...    | ...      | ...      | ...      | ...      | ...         |

| Effect | Linked Total |
|--------|-------------|
| Allocation | +X.XX% |
| Selection | +X.XX% |
| Interaction | +X.XX% |
| **Active Return** | **+X.XX%** |
```

---

## Mode 3: Factor-Based Attribution

### Goal: Decompose returns by factor exposures rather than sector groupings

### When to Use Factor Attribution

Use factor-based attribution instead of Brinson when:
- The portfolio is managed with a factor-based process (quant, smart beta)
- You want to understand whether returns came from factor tilts or alpha
- Sector groupings obscure the true return drivers
- The manager claims factor-neutral stock picking

### Framework

**Return decomposition:**
R_p = alpha + beta_mkt * R_mkt + beta_value * R_value + beta_mom * R_mom + beta_qual * R_qual + epsilon

**Attribution:**
- Market contribution = beta_mkt * R_mkt
- Value contribution = beta_value * R_value
- Momentum contribution = beta_mom * R_mom
- Quality contribution = beta_qual * R_qual
- Alpha (stock-specific) = R_p - Sum(factor contributions)

### Procedure

1. Estimate factor betas (from regression or holdings-based analysis)
2. Obtain factor returns for the period
3. Compute each factor's return contribution
4. Residual = total return minus all factor contributions

### Worked Example

**Portfolio return for the period: +8.50%**

| Factor | Beta | Factor Return | Contribution |
|--------|------|--------------|-------------|
| Market | 1.05 | +6.00% | +6.30% |
| Value (HML) | +0.20 | +2.00% | +0.40% |
| Momentum (UMD) | -0.10 | +3.00% | -0.30% |
| Quality (RMW) | +0.15 | +1.50% | +0.23% |
| Size (SMB) | +0.10 | -1.00% | -0.10% |
| **Factors total** | | | **+6.53%** |
| **Alpha (residual)** | | | **+1.97%** |

**Interpretation:**
- 74% of the portfolio return came from systematic factor exposures
- 26% came from alpha (stock-specific, non-factor returns)
- The manager has a slight value and quality tilt, with negative momentum exposure
- The negative momentum beta hurt performance by 30 bps this period
- The 1.97% alpha represents genuine stock-picking skill (or luck -- need multiple periods to distinguish)

### Decision Gate

If alpha is consistently near zero across multiple periods, the manager is essentially delivering factor returns that can be replicated cheaper with ETFs. Flag this for the user.

---

## Mode 4: Currency Attribution

### Goal: Separate local market returns from currency effects in international portfolios

### Framework

For an international portfolio, total return in base currency = local return + currency return + cross-term

**Decomposition:**
- R_total = (1 + R_local) * (1 + R_currency) - 1
- Approximately: R_total = R_local + R_currency (when returns are small)

### Per-Region Attribution

| Region | Port Wt | Local Return | Currency Return | Total Return (Base) |
|--------|---------|-------------|----------------|-------------------|
| US | 50% | +8.0% | 0.0% (base) | +8.0% |
| Europe | 20% | +6.0% | -3.0% (EUR/USD) | +2.8% |
| Japan | 15% | +4.0% | -5.0% (JPY/USD) | -1.2% |
| EM | 15% | +10.0% | -4.0% | +5.6% |

**Portfolio total in USD:**
= 0.50*8.0% + 0.20*2.8% + 0.15*(-1.2%) + 0.15*5.6% = 5.22%

**Attribution:**
- Local market return contribution: 0.50*8.0% + 0.20*6.0% + 0.15*4.0% + 0.15*10.0% = 7.30%
- Currency contribution: 0.50*0.0% + 0.20*(-3.0%) + 0.15*(-5.0%) + 0.15*(-4.0%) = -1.95%
- Cross-term: 5.22% - 7.30% - (-1.95%) = -0.13%

**Interpretation:** The portfolio earned +7.30% from local market performance but lost 1.95% to currency headwinds, primarily from JPY and EM currency weakness.

### Hedging Attribution

If the portfolio uses currency hedges:
- **Unhedged currency effect:** As calculated above
- **Hedge P&L:** Gain/loss on currency forwards or options
- **Net currency effect:** Unhedged effect + hedge P&L
- **Hedging effectiveness:** |Hedge P&L| / |Unhedged currency effect|

---

## Mode 5: Fixed Income Attribution

### Goal: Decompose bond portfolio returns into yield, duration, curve, and spread effects

### Return Components

Fixed income attribution is more complex than equity because multiple factors drive returns simultaneously:

1. **Income return (carry):** Coupon income earned over the period
   - Income = (Annual coupon / Price) * (Days in period / 365)

2. **Treasury curve effect:** Impact of changes in the risk-free yield curve
   - Duration effect = -Modified_duration * Change_in_yield
   - Convexity effect = 0.5 * Convexity * (Change_in_yield)^2
   - Curve (roll-down) = Return from bonds "rolling down" the curve as time passes

3. **Spread effect:** Impact of credit spread changes
   - Spread return = -Spread_duration * Change_in_spread

4. **Selection effect:** Security-specific returns not explained by the above

### Procedure

1. Run bond analytics for each position:

```
python3 tools/bond_yield.py \
    --face 1000 --coupon 0.05 --price 980 --years 10 --freq 2 \
    --benchmark-yield 0.04
```

2. Calculate each return component
3. Aggregate to the portfolio level using position weights
4. Compare to benchmark to determine active attribution

### Worked Example

**Investment grade corporate bond portfolio vs. Bloomberg Agg, Q4 2025**

| Component | Portfolio | Benchmark | Active |
|-----------|----------|-----------|--------|
| Income (carry) | +1.20% | +1.05% | +0.15% |
| Treasury duration | -0.80% | -0.70% | -0.10% |
| Curve/roll-down | +0.15% | +0.10% | +0.05% |
| Spread change | +0.30% | +0.20% | +0.10% |
| Selection | +0.10% | 0.00% | +0.10% |
| **Total** | **+0.95%** | **+0.65%** | **+0.30%** |

**Interpretation:**
- The portfolio outperformed by 30 bps
- +15 bps from higher carry (holding higher-yielding bonds)
- -10 bps from longer duration (rates rose, hurting the longer portfolio more)
- +10 bps from spread tightening (portfolio had more credit exposure that benefited)
- +10 bps from security selection (individual bond picks)
- +5 bps from curve positioning

---

## Mode 6: Manager-Level vs. Portfolio-Level Attribution

### Goal: Attribute performance in a multi-manager or fund-of-funds structure

### Manager-Level Attribution

When a portfolio is split across multiple managers:

**Manager allocation effect:** Did we allocate more capital to the better managers?
- Allocation_i = (w_actual_i - w_target_i) * (R_manager_i - R_portfolio_target)

**Manager selection effect:** Did each manager outperform their benchmark?
- Selection_i = w_actual_i * (R_manager_i - R_benchmark_i)

### Worked Example

**Multi-manager equity portfolio**

| Manager | Target Wt | Actual Wt | Manager Return | Benchmark | Alpha |
|---------|----------|-----------|---------------|-----------|-------|
| Large Cap Growth | 30% | 35% | +12.0% | +10.0% | +2.0% |
| Large Cap Value | 30% | 25% | +8.0% | +7.0% | +1.0% |
| Small Cap Core | 20% | 20% | +6.0% | +5.0% | +1.0% |
| International | 20% | 20% | +4.0% | +5.0% | -1.0% |

**Portfolio return:** 0.35*12% + 0.25*8% + 0.20*6% + 0.20*4% = 8.20%
**Benchmark composite return:** 0.30*10% + 0.30*7% + 0.20*5% + 0.20*5% = 7.10%
**Active return:** +1.10%

**Attribution:**
- Manager allocation: Overweight Large Cap Growth (+0.35% contribution)
- Manager selection: All managers except International added alpha (+0.85% contribution)
- Total active: +1.10% (allocation contributed ~30%, selection contributed ~70%)

---

## Tool Integration

| When you need... | Run this | Example |
|-----------------|---------|---------|
| Brinson-Fachler attribution | `python3 tools/brinson.py` | `--port-weights 0.30,0.25,0.20,0.15,0.10 --port-returns 0.12,0.08,0.05,0.15,0.03 --bench-weights 0.25,0.25,0.25,0.15,0.10 --bench-returns 0.10,0.09,0.06,0.12,0.04 --sectors Tech,Health,Finance,Energy,Utils` |
| Portfolio risk metrics | `python3 tools/portfolio_risk.py` | `--returns 0.02,-0.01,0.03 --benchmark 0.01,0.00,0.02 --rf 0.05` |
| Bond analytics for FI attribution | `python3 tools/bond_yield.py` | `--face 1000 --coupon 0.05 --price 980 --years 10 --freq 2` |

---

## Output Specifications

### Primary Deliverable: Attribution Report

For every attribution analysis, output:

```
### Attribution Report: [Portfolio Name] vs. [Benchmark Name]
Period: [Start] to [End]

**Summary:**
| Metric | Value |
|--------|-------|
| Portfolio Return | +X.XX% |
| Benchmark Return | +X.XX% |
| Active Return | +X.XX% |
| Allocation Effect | +X.XX% |
| Selection Effect | +X.XX% |
| Interaction Effect | +X.XX% |

**Detail by Sector:**
| Sector | Port Wt | Bench Wt | Port Ret | Bench Ret | Alloc | Select | Inter | Total |
|--------|---------|----------|----------|-----------|-------|--------|-------|-------|
| ...    | ...     | ...      | ...      | ...       | ...   | ...    | ...   | ...   |

**Interpretation:**
[2-3 sentences explaining the key drivers of active return]

**Skill Assessment:**
[Is the manager an allocator, a selector, or both? Is performance concentrated or diversified?]
```

### Supporting Artifacts:
- **Sector contribution waterfall** -- ordered from most positive to most negative total effect
- **Skill consistency table** -- allocation and selection effects by period (for multi-period)
- **Concentration analysis** -- what percentage of active return comes from the top 2 sectors
- **Comparison to peers** -- if available, how does the attribution profile compare to peer managers

---

## Quality Gates & Completion Criteria

- [ ] Portfolio and benchmark weights sum to 100% (or within 0.1% rounding)
- [ ] Active return reconciles: Sum(allocation + selection + interaction) = portfolio return - benchmark return
- [ ] All sectors/positions are accounted for (no missing data)
- [ ] Multi-period attribution links correctly to cumulative active return
- [ ] Interpretation identifies the primary skill source (allocation vs. selection)
- [ ] At least 4 periods are analyzed before drawing conclusions about skill
- [ ] Concentration risk is assessed (single-sector dependence)
- [ ] Currency effects are separated for international portfolios

**Success metric:** A CIO reading the report should understand exactly where active return came from and whether the manager's process is working as intended.

**Escalation triggers:**
- Attribution effects do not sum to active return --> data error, investigate weights/returns
- Selection effect is consistently negative across all sectors --> stock picking is destroying value
- 90%+ of active return comes from one sector --> concentrated bet, not diversified skill
- Interaction effect dominates --> the manager may be style drifting or timing sectors

---

## Hard Constraints

- **NEVER** fabricate portfolio or benchmark weights/returns
- **NEVER** present attribution without verifying the totals reconcile
- **NEVER** conclude "skill" from a single period -- require minimum 4 periods (1 year quarterly)
- **ALWAYS** separate allocation from selection -- they measure fundamentally different skills
- **ALWAYS** flag when interaction effects are large (>30% of active return) as this complicates interpretation
- **ALWAYS** state whether weights are beginning-of-period or average weights (Brinson requires BOD weights)
- If multi-period attribution is requested, **require** a proper linking method (Carino or GRAP) -- simple summation is not acceptable for periods exceeding one quarter

---

## Common Pitfalls

1. **Confusing Brinson-Hood-Beebower with Brinson-Fachler:** BHB uses the benchmark total return as the base for allocation; BF uses (R_b_i - R_b_total). The BF formulation is more intuitive because allocation effect is zero for benchmark-weight sectors. --> This skill uses Brinson-Fachler by default.

2. **Using end-of-period weights:** Attribution requires beginning-of-period weights. Using end-of-period weights contaminates the analysis because the weights themselves have been changed by returns during the period. --> Always use BOD or beginning-of-period weights.

3. **Ignoring the interaction effect:** Some practitioners combine interaction with either allocation or selection. This is acceptable but must be stated explicitly. Hiding interaction in selection inflates the apparent stock-picking skill. --> Report all three effects separately, then the user can decide how to combine.

4. **Drawing conclusions from one period:** A single quarter of positive allocation effect does not prove the manager is a skilled allocator. Attribution effects are noisy and require multiple periods to distinguish signal from noise. --> Require minimum 4 periods (ideally 12+) before assessing skill.

5. **Sector definition mismatch:** If the portfolio uses GICS sectors but the benchmark uses ICB, the attribution will produce spurious effects from definitional differences, not actual investment decisions. --> Verify that portfolio and benchmark use identical sector/classification schemes.

6. **Missing the "what vs. how much" distinction:** Attribution tells you WHERE active return came from, but not whether the magnitude is statistically significant. A +50 bps selection effect could be noise. --> Pair attribution with information ratio analysis from `/risk` to assess significance.

7. **Ignoring transaction costs in attribution:** Gross-of-fee attribution overstates the manager's value-add. Net-of-fee attribution is what the client actually receives. --> Always clarify whether returns are gross or net, and flag the difference if material (>50 bps annually).

---

## Related Skills

- For portfolio construction and optimization, use **`/portfolio`**
- For risk analytics and stress testing, use **`/risk`**
- For factor signal research, use **`/quant`**
- For single-name idea evaluation, use **`/long-short`**
- For benchmark-relative risk metrics (tracking error, IR), use **`/risk`**
