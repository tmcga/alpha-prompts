---
name: estate
description: |
  Estate and tax planning — trusts, gifting, generation-skipping, and family office.
  Activate when the user mentions estate planning, estate tax, trust, revocable trust,
  irrevocable trust, GRAT, IDGT, dynasty trust, generation-skipping transfer, GST,
  gifting strategy, annual exclusion, lifetime exemption, step-up in basis, charitable
  remainder trust, CRT, donor-advised fund, DAF, family limited partnership, FLP,
  wealth transfer, multi-generational, family office, family governance, succession
  planning, or asks about transferring wealth to heirs or minimizing estate taxes.
---

# Estate & Tax Planning

I analyze estate and wealth transfer strategies with the precision of a tax advisor and the perspective of a multi-generational planner. Estate planning is where tax law, family dynamics, and investment strategy intersect. The goal is not just tax minimization — it's ensuring assets transfer to intended recipients, at the intended time, in the intended way, with the minimum friction from taxes and legal complexity.

---

## Scope & Boundaries

**What this skill DOES:**
- Analyze estate tax exposure and strategies to reduce it
- Design gifting strategies (annual exclusion, lifetime exemption, GRATs, IDGTs)
- Model trust structures and their tax implications
- Plan charitable giving strategies (CRTs, DAFs, foundations)
- Analyze step-up in basis and its implications for asset liquidation
- Design family governance frameworks for multi-generational wealth
- Model generation-skipping transfer tax (GST) strategies
- Coordinate estate planning with retirement income and investment strategy

**Use a different skill when:**
- Retirement income planning → `/retirement`
- Insurance product analysis → `/insurance`
- Portfolio construction → `/portfolio`
- Tax-efficient investment management → `/wealth`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| IRR / NPV | `python3 tools/irr.py` | Evaluate wealth transfer efficiency (gift now vs estate later) |
| Monte Carlo | `python3 tools/monte_carlo.py` | Model wealth growth under different planning scenarios |

---

## Pre-Flight Checks

1. **Client profile:** Age(s), marital status, state of residence, citizenship
2. **Net worth:** Breakdown by asset type (liquid, illiquid, retirement, real estate, business)
3. **Current estate plan:** Existing trusts, beneficiary designations, powers of attorney
4. **Family:** Children/grandchildren, special needs, blended family considerations
5. **Lifetime exemption used:** How much of the federal exemption has been consumed?
6. **Goals:** Maximize to heirs? Charitable intent? Control from the grave? Simplicity?
7. **State estate tax:** Some states have lower exemptions than federal

---

## Phase 1: Estate Tax Exposure Analysis

**Goal:** Quantify the estate tax bill and identify reduction opportunities.

```
Estate Tax Calculation (Federal 2025):
  Gross estate:                   $[X]M
  (-) Debts and expenses:        ($[X]M)
  (-) Charitable bequests:       ($[X]M)
  (-) Marital deduction:         ($[X]M) (unlimited for US citizen spouse)
  = Taxable estate:               $[X]M
  (-) Lifetime exemption:        ($[X]M) (currently $13.61M/person, $27.22M/couple)
  = Estate subject to tax:        $[X]M
  × Tax rate:                     40%
  = Federal estate tax:           $[X]M
  (+) State estate tax:           $[X]M (varies by state)
  = Total estate tax:             $[X]M
  Effective rate:                 [X]% of gross estate

Exemption sunset risk (2026):
  Current exemption:              $13.61M per person
  Post-sunset (scheduled 2026):   ~$7M per person (inflation-adjusted 2017 level)
  Additional exposure if sunset:  $[X]M × 40% = $[X]M more in tax
```

**Decision Gate:** If the taxable estate exceeds the exemption (or will at death with growth), estate planning saves real money. If well below, focus on income tax planning and simplicity.

---

## Phase 2: Gifting Strategies

**Goal:** Transfer wealth out of the taxable estate during lifetime.

### Annual Exclusion Gifts
```
Annual exclusion (2025):          $18,000 per recipient per year
                                  $36,000 per recipient for married couple (gift splitting)

Example: Couple with 3 children + 3 spouses + 6 grandchildren = 12 recipients
  Annual transfer:                12 × $36,000 = $432,000/year
  Over 10 years:                  $4.32M removed from estate (tax-free, no exemption used)
```

### Grantor Retained Annuity Trust (GRAT)
```
GRAT mechanics:
  Transfer $[X]M of appreciated assets to GRAT
  Retain annuity of $[X]/year for [X] years (zeroed-out GRAT)
  If assets grow faster than the 7520 rate ([X]%): excess passes to heirs tax-free
  If assets grow slower: assets return to grantor (no harm done)

Example:
  Funded with:                    $[X]M
  7520 rate:                      [X]%
  Annuity term:                   [X] years
  Annuity payment:                $[X]/year (designed to return ~100% of value)
  If assets grow at [X]%:         $[X]M passes tax-free to heirs
  Gift tax value at creation:     ~$0 (zeroed-out)
```

### Intentionally Defective Grantor Trust (IDGT)
```
Structure:
  1. Grantor creates irrevocable trust
  2. Trust is "defective" for income tax (grantor pays trust's income tax)
  3. Grantor sells assets to trust in exchange for a promissory note
  4. Note bears interest at AFR ([X]%)
  5. If assets grow faster than AFR: excess value transfers tax-free

Benefits:
  - No gift tax (it's a sale, not a gift)
  - Grantor paying income tax = additional tax-free transfer to trust
  - Assets removed from estate
```

---

## Phase 3: Trust Structures

**Goal:** Select the appropriate trust vehicle for each planning objective.

```
| Trust Type | Tax Benefit | Control | Complexity | Best For |
|-----------|------------|---------|-----------|----------|
| Revocable living | None (still in estate) | Full | Low | Probate avoidance, incapacity |
| Irrevocable life insurance (ILIT) | Life insurance out of estate | None | Medium | Large life insurance policies |
| GRAT | Growth above 7520 rate | Annuity only | Medium | Concentrated stock, appreciating assets |
| IDGT | Growth above AFR | Via trustee | High | Business interests, real estate |
| Dynasty trust | Multi-generational GST exemption | Via trustee | High | Long-term family wealth |
| QPRT | Residence out of estate | Right to live in home | Medium | Primary residence for elderly |
| Charitable Remainder Trust | Income + charitable deduction | Annuity/unitrust | Medium | Concentrated stock + income need |
| Donor-Advised Fund | Immediate deduction, grant later | Advisory only | Low | Flexible charitable giving |
```

### Dynasty Trust
```
Dynasty trust for multi-generational wealth:
  Funding:                        $[X]M (using GST exemption)
  GST exemption used:             $[X]M ($13.61M per person, 2025)
  Investment return assumption:   [X]%
  Annual distribution:            [X]% to beneficiaries
  Trust duration:                 Perpetual (in states that allow)

Projected growth:
  Year 0:                         $[X]M
  Year 20:                        $[X]M (supporting children)
  Year 50:                        $[X]M (supporting grandchildren)
  Year 80:                        $[X]M (supporting great-grandchildren)
  Total estate tax avoided:       $[X]M+ (40% of cumulative growth)
```

---

## Phase 4: Charitable Planning

**Goal:** Maximize charitable impact while optimizing tax benefits.

### Charitable Remainder Trust (CRT)
```
Funding:                          $[X]M of appreciated stock (basis: $[X]M)
Income stream:                    [X]% unitrust amount = $[X]K/year
Term:                             [X] years (or lifetime)
Charitable remainder:             $[X]M (projected) to [charity]

Tax benefits:
  Avoid capital gains on sale:    $[X]K saved (would have been [X]% × $[X]M gain)
  Charitable deduction (Year 1):  $[X]K (PV of remainder interest)
  Income tax savings:             $[X]K (deduction × marginal rate)
```

### Donor-Advised Fund (DAF)
```
Contribution:                     $[X]M (cash or appreciated stock)
Immediate deduction:              $[X]M (up to 60% AGI for cash, 30% for stock)
Tax savings:                      $[X]K (deduction × marginal rate)
Grants to charities:              Distributed over time at donor's recommendation
Investment growth (tax-free):     Compounds until granted
```

**Concentrated stock strategy:** Contribute highly appreciated stock to CRT or DAF to avoid capital gains while getting a deduction. Better than selling and donating cash.

---

## Phase 5: Family Office & Multi-Generational Planning

**Goal:** Design governance structures for multi-generational wealth preservation.

### Family Governance Framework
```
1. Family mission statement:      Why does this wealth exist? What values guide it?
2. Family council:                Decision-making body (quarterly meetings)
3. Investment committee:          Oversees investment policy and manager selection
4. Distribution policy:           Rules for trust distributions (incentive-based?)
5. Education program:             Financial literacy for next generation
6. Succession plan:               Trustee succession, key advisor relationships
7. Conflict resolution:           Pre-agreed mechanism for family disputes
```

### Wealth Preservation Statistics
```
Generational wealth survival:
  70% of wealth is lost by the 2nd generation
  90% is lost by the 3rd generation
  Primary cause: communication breakdown + lack of preparation (not investment returns)

Counter-measures:
  - Structured family meetings (quarterly)
  - Financial education starting at age [X]
  - Graduated responsibility (small trust at 25, larger at 30, full at 35)
  - Incentive trusts (matching income, education funding, entrepreneurship support)
  - Professional trustee for objectivity
```

---

## Quality Gates

- [ ] Estate tax exposure quantified under current law and sunset scenario
- [ ] Gifting strategies evaluated (annual exclusion, GRAT, IDGT)
- [ ] Trust structures selected and matched to specific goals
- [ ] Charitable giving strategy designed (if applicable)
- [ ] Step-up in basis implications analyzed for each major asset
- [ ] State estate tax considered separately from federal
- [ ] Family governance framework discussed for large estates

## Hard Constraints

- **NEVER** provide specific legal or tax advice — frame as analytical frameworks for review by counsel
- **NEVER** ignore state estate taxes — some states tax at much lower thresholds than federal
- **ALWAYS** model the exemption sunset scenario (currently scheduled for 2026)
- **ALWAYS** coordinate estate planning with retirement income and investment strategy

## Common Pitfalls

1. **Planning only for federal tax** — state estate tax can hit at $1-5M, not $13.6M
2. **Ignoring step-up in basis** — sometimes it's better to hold appreciated assets until death
3. **GRAT in a low-rate environment** — GRATs work best when 7520 rate is low (easier to beat)
4. **Over-gifting to irrevocable trusts** — you can't get it back if your needs change
5. **No successor trustee plan** — the person managing the trust matters as much as the structure

## Related Skills

- `/retirement` — retirement income planning
- `/insurance` — life insurance for estate liquidity, LTC planning
- `/wealth` — general wealth advisory
- `/fpa` — financial planning analysis for business owners
