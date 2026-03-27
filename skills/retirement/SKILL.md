---
name: retirement
description: |
  Retirement planning and goals-based portfolio construction. Activate when the user
  mentions retirement, retirement planning, Monte Carlo retirement, withdrawal rate,
  4% rule, safe withdrawal, sequence of returns risk, Social Security optimization,
  Roth conversion, required minimum distribution, RMD, retirement income, decumulation,
  goals-based investing, bucket strategy, liability matching, retirement readiness,
  or asks about whether they can afford to retire or how to structure retirement income.
---

# Retirement Planning

I build retirement plans grounded in probability, not certainty. The core question — "can I afford to retire?" — is a Monte Carlo simulation, not a spreadsheet. I model the full distribution of outcomes across market scenarios, sequence-of-returns risk, inflation variability, and longevity uncertainty. Every recommendation includes the probability of success and what changes it.

---

## Scope & Boundaries

**What this skill DOES:**
- Run Monte Carlo simulations across spending, market, and longevity scenarios
- Optimize Social Security claiming strategy (age 62 vs 67 vs 70)
- Model Roth conversion ladders during low-income years
- Design withdrawal sequencing across account types (taxable, tax-deferred, tax-free)
- Build goals-based portfolio allocations with liability matching
- Analyze sequence-of-returns risk and mitigation strategies (bond tent, bucket, annuity floor)
- Calculate RMD schedules and their tax impact
- Stress test against inflation spikes, market crashes, and longevity beyond plan

**Use a different skill when:**
- Estate and trust planning → `/estate`
- Insurance analysis (life, LTC, annuities) → `/insurance`
- Portfolio optimization (institutional) → `/portfolio`
- General risk analytics → `/risk`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Monte Carlo | `python3 tools/monte_carlo.py` | Retirement success probability, terminal wealth distribution |
| IRR / NPV | `python3 tools/irr.py` | Cash flow analysis for pension vs lump sum decisions |
| Portfolio Risk | `python3 tools/portfolio_risk.py` | Risk metrics on retirement portfolio |

---

## Pre-Flight Checks

1. **Client profile:** Age(s), retirement target age, life expectancy planning horizon
2. **Current assets:** By account type (401k, IRA, Roth, taxable, real estate, pension)
3. **Income:** Current income, expected changes, Social Security estimate
4. **Spending:** Current annual spending, expected retirement spending, one-time expenses
5. **Inflation assumption:** Historical average 3%, current environment may differ
6. **Risk tolerance:** Maximum acceptable drawdown, emotional capacity for volatility
7. **Legacy goals:** Desired estate value, charitable intentions

---

## Phase 1: Retirement Readiness Assessment

**Goal:** Determine probability of success and identify the biggest risks.

### Baseline Monte Carlo Simulation

Run: `python3 tools/monte_carlo.py --initial [total_assets] --return [expected_return] --vol [expected_vol] --years [planning_horizon] --withdrawal [withdrawal_rate]`

```
Inputs:
  Total investable assets:    $[X]M
  Annual spending (today $):  $[X]K
  Withdrawal rate:            [X]% (spending / assets)
  Expected return:            [X]% (portfolio weighted)
  Expected volatility:        [X]%
  Planning horizon:           [X] years (to age [X])
  Inflation:                  [X]%

Results (10,000 simulations):
  Success probability:        [X]%
  Median terminal wealth:     $[X]M
  10th percentile:            $[X]
  Ruin probability:           [X]%
  Median ruin age:            [X] (if ruin occurs)
```

### Withdrawal Rate Guidelines
```
| Rate | Risk Level | Notes |
|------|-----------|-------|
| 3.0% | Conservative | >95% success over 30 years historically |
| 3.5% | Moderate | ~93% success, good balance |
| 4.0% | Standard | ~88% success (the "4% rule" — Bengen) |
| 4.5% | Aggressive | ~80% success, requires flexibility |
| 5.0% | High risk | ~70% success, only with guardrails |
```

**Decision Gate:** If success probability <85%, identify the cheapest lever to improve it (spend less, work longer, take more risk, or add guaranteed income).

---

## Phase 2: Social Security Optimization

**Goal:** Determine the optimal claiming age.

```
Social Security options:
| Claiming Age | Monthly Benefit | Annual | Cumulative by Age 85 |
|-------------|-----------------|--------|---------------------|
| 62 | $[X] | $[X]K | $[X]K |
| 67 (FRA) | $[X] | $[X]K | $[X]K |
| 70 (max) | $[X] | $[X]K | $[X]K |

Break-even analysis:
  Delay 62→67: breaks even at age [X]
  Delay 67→70: breaks even at age [X]
  Delay 62→70: breaks even at age [X]

Spousal coordination (if applicable):
  Strategy A: Both claim at 62 → combined $[X]K/year
  Strategy B: Lower earner at 62, higher at 70 → combined $[X]K/year
  Strategy C: Both delay to 70 → combined $[X]K/year
```

**General rule:** Delay if healthy and have other assets to bridge. The 8%/year delayed credit (age 62-70) is a guaranteed real return that no investment matches. Claim early only if health is poor or cash is needed.

---

## Phase 3: Tax-Efficient Withdrawal Sequencing

**Goal:** Minimize lifetime tax burden across account types.

### Account Types and Tax Treatment
```
| Account | Contributions | Growth | Withdrawals |
|---------|-------------|--------|-------------|
| Taxable (brokerage) | After-tax | Capital gains | CG rates (favorable) |
| Tax-deferred (401k/IRA) | Pre-tax | Tax-deferred | Ordinary income |
| Tax-free (Roth) | After-tax | Tax-free | Tax-free |
| HSA | Pre-tax | Tax-free | Tax-free (medical) |
```

### Withdrawal Sequencing Strategy
```
General order (adjust for tax bracket management):
1. Required Minimum Distributions (age 73+) — mandatory, ordinary income
2. Taxable accounts — use for spending up to low tax brackets
3. Tax-deferred accounts — fill remaining low brackets
4. Roth accounts — preserve for last (tax-free growth, no RMDs)

Tax bracket management:
  Current year income:          $[X] (SS + pension + other)
  Space in [X]% bracket:       $[X]
  Withdraw from IRA to fill:   $[X] (converts tax-deferred → spending at lower rate)
```

### Roth Conversion Ladder
```
Low-income years (early retirement before SS/RMDs):
  Year 1 taxable income:       $[X] (only taxable account withdrawals)
  Space to top of [X]% bracket: $[X]
  Optimal Roth conversion:      $[X] (pay [X]% now vs [X]% later)

Projected tax savings:
  Tax on conversion now:        $[X]
  Tax avoided on future RMD:    $[X] (at higher bracket)
  Net savings:                  $[X]
```

---

## Phase 4: Sequence-of-Returns Risk Mitigation

**Goal:** Protect against poor market returns in the first 5-10 years of retirement.

### Why It Matters
```
Two retirees, same average return (7%), different sequences:
  Retiree A: -20% in Year 1, then recovery → runs out at age 82
  Retiree B: +15% in Year 1, then decline → money lasts to 95+

The difference is entirely sequence — same average, wildly different outcomes.
Risk is highest in the 5 years before and after retirement.
```

### Mitigation Strategies

**1. Bond Tent (Rising Equity Glide Path)**
```
Increase bond allocation to [X]% at retirement date
Gradually shift back to equities over 10 years:
  Retirement: 60% bonds / 40% stocks
  Year 5:     45% bonds / 55% stocks
  Year 10:    35% bonds / 65% stocks
```

**2. Cash Buffer / Bucket Strategy**
```
Bucket 1 (Now, 0-2 years):    $[X] in cash/short-term bonds
Bucket 2 (Soon, 3-7 years):   $[X] in intermediate bonds
Bucket 3 (Later, 8+ years):   $[X] in equities (growth)

Spend from Bucket 1, refill from Bucket 2 in good markets.
In bad markets, let Bucket 3 recover — don't sell equities to fund spending.
```

**3. Guaranteed Income Floor**
```
Essential expenses:            $[X]K/year
Social Security covers:        $[X]K/year
Gap to cover with annuity:     $[X]K/year
Annuity cost (SPIA):           ~$[X] per $1K/year of income (age-dependent)
Required purchase:             $[X]K

With floor secured, remaining portfolio can be invested more aggressively.
```

---

## Phase 5: Goals-Based Portfolio Construction

**Goal:** Align asset allocation with specific financial goals and their time horizons.

```
| Goal | Amount | Timeline | Priority | Allocation |
|------|--------|----------|----------|-----------|
| Essential spending (Y1-5) | $[X]K/yr | Immediate | Must-fund | Cash + short bonds |
| Essential spending (Y6-15) | $[X]K/yr | Medium | Must-fund | Intermediate bonds + TIPS |
| Discretionary (travel) | $[X]K/yr | 10 years | Want-to-fund | Balanced 60/40 |
| Legacy | $[X]M | 20+ years | Aspirational | Growth equities |
| Healthcare reserve | $[X]K | As needed | Must-fund | TIPS + HSA |
```

**Allocation by goal priority:**
- Must-fund goals → matched with duration-appropriate bonds, TIPS, annuities
- Want-to-fund goals → balanced allocation, accept some shortfall risk
- Aspirational goals → growth-oriented, outcome is upside-dependent

---

## Phase 6: Stress Testing

| Scenario | Impact | Success Rate | Action |
|----------|--------|-------------|--------|
| -30% market crash in Year 1 | Sequence risk crystallizes | [X]% (vs [X]% base) | Temporary spending cut |
| Inflation 5% for 5 years | Spending grows faster than portfolio | [X]% | TIPS allocation helps |
| Live to 100 (vs 95 plan) | 5 more years of drawdown | [X]% | Annuity floor needed |
| Long-term care event ($100K/yr × 3yr) | $300K unplanned | [X]% | LTC insurance evaluation |
| Both spouses live to 95 | Longer joint spending | [X]% | Delay SS to maximize survivor |

---

## Quality Gates

- [ ] Monte Carlo run with realistic return/vol/inflation assumptions
- [ ] Social Security claiming strategy optimized for household
- [ ] Tax-efficient withdrawal sequence designed across account types
- [ ] Roth conversion opportunity assessed during low-income years
- [ ] Sequence-of-returns risk addressed (bond tent, bucket, or annuity floor)
- [ ] Goals mapped to specific asset allocations by priority and timeline
- [ ] Stress tests: market crash, inflation, longevity, healthcare event

## Hard Constraints

- **NEVER** use a single-point return estimate — always run Monte Carlo or scenario analysis
- **NEVER** recommend a withdrawal rate without showing the probability of success
- **ALWAYS** account for inflation — $100K today ≠ $100K in 20 years
- **ALWAYS** model Social Security as a household optimization, not individual

## Common Pitfalls

1. **Using average returns** — averages hide sequence risk that destroys retirement plans
2. **Ignoring taxes in withdrawal planning** — the order you draw from accounts matters as much as the return
3. **Planning to age 85** — many people live to 95+; plan to 95 minimum
4. **Claiming Social Security at 62 "because I might die"** — statistically, delay wins for most couples
5. **100% equities in retirement** — volatility tolerance changes when you're drawing down, not accumulating

## Related Skills

- `/estate` — estate and tax planning, trusts, gifting
- `/insurance` — life insurance, annuities, long-term care
- `/portfolio` — institutional-grade portfolio optimization
- `/wealth` — general wealth advisory (routes to specialized skills)
