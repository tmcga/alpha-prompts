---
name: insurance
description: |
  Insurance and risk transfer analysis — life, disability, annuities, and long-term care.
  Activate when the user mentions life insurance, term life, whole life, universal life,
  variable life, disability insurance, long-term care insurance, LTC, annuity, SPIA, QLAC,
  fixed annuity, variable annuity, indexed annuity, insurance needs analysis, human life
  value, income replacement, key person insurance, buy-sell agreement insurance,
  or asks about insurance coverage needs or comparing insurance products.
---

# Insurance & Risk Transfer Analysis

I analyze insurance products as risk transfer instruments, not investment products. The fundamental question is always: what financial catastrophe are we insuring against, and is the premium justified by the probability and magnitude of that catastrophe? I evaluate insurance needs from first principles, compare products on cost-effectiveness, and integrate insurance into the broader financial plan.

---

## Scope & Boundaries

**What this skill DOES:**
- Calculate life insurance needs using income replacement, human life value, and capital needs methods
- Compare term vs permanent life insurance for specific planning objectives
- Analyze disability insurance coverage gaps and policy features
- Evaluate long-term care insurance vs self-insurance vs hybrid products
- Analyze annuity products (SPIA, QLAC, fixed, variable, indexed) for retirement income
- Model insurance within estate planning (ILIT, second-to-die, estate liquidity)
- Evaluate key person and buy-sell insurance for business owners

**Use a different skill when:**
- Retirement income planning (broader) → `/retirement`
- Estate and trust structuring → `/estate`
- Portfolio construction → `/portfolio`
- Health insurance marketplace → out of scope (regulatory, not analytical)

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Monte Carlo | `python3 tools/monte_carlo.py` | Model self-insurance vs premium scenarios |
| IRR / NPV | `python3 tools/irr.py` | Compare insurance cost vs investment alternative |
| Loan Amort | `python3 tools/loan_amort.py` | Model premium financing |

---

## Pre-Flight Checks

1. **Insurance type:** Life, disability, LTC, annuity, or key person?
2. **Client profile:** Age, health status, family dependents, income, net worth
3. **Existing coverage:** Current policies, group coverage through employer
4. **Planning context:** Estate liquidity? Income replacement? Retirement income? Business?
5. **Budget:** How much premium is acceptable relative to income?
6. **Time horizon:** Temporary need (term) or permanent need (whole life)?

---

## Phase 1: Life Insurance Needs Analysis

**Goal:** Determine the right amount and type of life insurance coverage.

### Three Methods

**Method 1: Income Replacement**
```
Annual income to replace:        $[X]K
Years of replacement needed:     [X] years
Discount rate:                   [X]%
PV of income stream:             $[X]M
(-) Existing coverage:           ($[X]M)
(-) Liquid assets available:     ($[X]M)
(-) Social Security survivor:    ($[X]M PV)
= Additional coverage needed:    $[X]M
```

**Method 2: Capital Needs**
```
Immediate expenses:
  Final expenses/funeral:        $[X]K
  Mortgage payoff:               $[X]K
  Debt payoff:                   $[X]K
  Emergency fund:                $[X]K
  Education funding:             $[X]K
  = Immediate total:             $[X]M

Ongoing expenses:
  Annual living expenses:        $[X]K × [X] years = $[X]M (PV)
  = Ongoing total:               $[X]M

  Total need:                    $[X]M
  (-) Existing resources:        ($[X]M)
  = Coverage gap:                $[X]M
```

**Method 3: Human Life Value**
```
Current income:                  $[X]K
Annual growth rate:              [X]%
Working years remaining:         [X]
Discount rate:                   [X]%
PV of future earnings:           $[X]M
(-) Self-maintenance costs:      ($[X]M) (your own consumption)
= Economic value:                $[X]M
```

### Term vs Permanent Decision
```
| Factor | Term | Permanent (Whole/UL) |
|--------|------|---------------------|
| Need duration | Temporary (kids, mortgage) | Permanent (estate, business) |
| Cost (age 40, $1M) | ~$500-800/yr | ~$8,000-15,000/yr |
| Cash value | None | Yes (tax-deferred growth) |
| Premium | Level for term period | Level for life |
| Best for | Income replacement, debt | Estate liquidity, ILIT, buy-sell |
| Investment component | None | Mediocre (2-4% net of costs) |

Rule: Buy term if the need is temporary. Buy permanent only for specific
estate or business planning needs where the insurance must exist at death.
```

---

## Phase 2: Disability Insurance

**Goal:** Assess income protection against the most likely working-age risk.

```
Coverage analysis:
  Monthly income:                $[X]K
  Group LTD coverage:            [X]% of income = $[X]K/month (taxable if employer-paid)
  Maximum benefit:               $[X]K/month (most group policies cap at $10-15K)
  Gap:                           $[X]K/month

Individual policy to fill gap:
  Benefit amount:                $[X]K/month
  Definition of disability:      Own occupation (preferred) vs any occupation
  Elimination period:            [X] days (90 days standard — longer = cheaper)
  Benefit period:                To age 65 (standard)
  COLA rider:                    [X]% (inflation protection)
  Annual premium:                $[X]K ([X]% of income)
```

**Key insight:** Disability is more likely than death during working years. A 35-year-old has a ~25% chance of being disabled for 90+ days before age 65, but only a ~5% chance of death.

---

## Phase 3: Long-Term Care Analysis

**Goal:** Evaluate LTC insurance vs self-insurance vs hybrid products.

```
LTC cost projection:
  Average annual cost:           $[X]K (nursing home: ~$100K+, home care: ~$60K+)
  Average duration of need:      2.5 years (but distribution is highly skewed)
  Probability of needing LTC:    ~50% for individuals reaching age 65
  Catastrophic scenario (5+ yrs): ~15% probability

Self-insurance analysis:
  Assets available:              $[X]M
  LTC reserve needed (3 years):  $[X]K
  As % of portfolio:             [X]%
  Can the portfolio absorb it?   [assessment]

Traditional LTC insurance:
  Daily benefit:                 $[X]
  Benefit period:                [X] years
  Elimination period:            [X] days
  Inflation protection:          [X]% compound
  Annual premium:                $[X]K (may increase over time)
  Lifetime premium (20 years):   $[X]K

Hybrid product (life + LTC rider):
  Death benefit:                 $[X]M
  LTC benefit pool:              $[X]M (2-3x death benefit)
  Single premium:                $[X]K
  If LTC not needed:             Death benefit paid to heirs
```

**Decision framework:**
- Net worth <$500K → Medicaid planning (attorney, not financial advisor)
- Net worth $500K-$2M → LTC insurance makes sense (can't self-insure fully)
- Net worth $2M-$5M → Hybrid product or partial self-insurance
- Net worth >$5M → Self-insure (LTC cost is manageable relative to assets)

---

## Phase 4: Annuity Analysis

**Goal:** Evaluate annuity products for guaranteed retirement income.

### Single Premium Immediate Annuity (SPIA)
```
Purchase price:                  $[X]K
Monthly income:                  $[X]
Annual payout rate:              [X]% ($annual income / purchase price)
Breakeven age:                   [X] (total payments = purchase price)
Life expectancy advantage:       Lives beyond breakeven → "won" the bet

Comparison to bond ladder:
  Same income from bonds requires: $[X]K at [X]% yield
  SPIA is [X]% cheaper due to mortality credits
  But: no residual value if die early
```

### Qualified Longevity Annuity Contract (QLAC)
```
Purchase (from IRA, up to $200K): $[X]K
Income starts at age:             [X] (typically 80-85)
Monthly income:                   $[X]
Purpose: Pure longevity insurance — covers the "live too long" risk
Reduces RMDs on the amount used to purchase
```

### Fixed Indexed Annuity (FIA)
```
Premium:                         $[X]K
Participation rate:              [X]% of index return
Cap rate:                        [X]% maximum credited
Floor:                           0% (no loss, but no guaranteed gain)
Surrender period:                [X] years
Annual fees:                     [X]% (often embedded, not transparent)

Key question: Does the upside potential after caps and participation rates
beat a simple bond portfolio? Usually no — the complexity benefits the issuer.
```

---

## Phase 5: Business Insurance

**Goal:** Analyze insurance needs for business owners.

### Key Person Insurance
```
Key person:                      [Name, role]
Revenue attributable:            $[X]M ([X]% of total)
Replacement timeline:            [X] months
Coverage needed:                 [X]x annual revenue attributable
  or: [X]x annual compensation + recruiting cost
Policy type:                     Term (matching employment horizon)
Premium:                         $[X]K/year
```

### Buy-Sell Agreement Insurance
```
Business value:                  $[X]M
Owners:                          [X] partners, [X]% each
Each owner's share:              $[X]M
Insurance structure:
  Cross-purchase: Each partner owns policy on others
  Entity-purchase: Business owns policies on all partners
  Hybrid: Combination

Total insurance needed:          $[X]M (covers all buyout scenarios)
Annual premium:                  $[X]K total across all policies
```

---

## Quality Gates

- [ ] Insurance need quantified using at least 2 methods
- [ ] Term vs permanent decision justified by specific planning need
- [ ] Disability coverage gap identified (group + individual)
- [ ] LTC risk assessed with self-insurance threshold analysis
- [ ] Annuity products compared to bond/investment alternatives
- [ ] Business insurance needs addressed (if business owner)
- [ ] All recommendations integrated with retirement and estate plan

## Hard Constraints

- **NEVER** evaluate permanent life insurance as an investment — compare the insurance component separately
- **NEVER** recommend an annuity without comparing to a simple bond ladder alternative
- **ALWAYS** check existing group coverage before recommending individual policies
- **ALWAYS** disclose that insurance premiums are a cost — they reduce investable assets

## Common Pitfalls

1. **Whole life as investment** — the cash value return is typically 2-4% after costs; buy term and invest the difference
2. **Ignoring disability risk** — more likely than death during working years but less commonly insured
3. **LTC insurance too late** — premiums skyrocket after 60, and health issues may make you uninsurable
4. **Variable annuity fees** — mortality & expense charges + sub-account fees + rider fees can exceed 3%/year
5. **Over-insuring** — insurance is for catastrophic risk, not every possible expense

## Related Skills

- `/retirement` — retirement income planning and withdrawal strategy
- `/estate` — estate planning and wealth transfer
- `/wealth` — general wealth advisory
- `/fpa` — financial planning for business owner insurance needs
