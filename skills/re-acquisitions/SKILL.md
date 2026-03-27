---
name: re-acquisitions
description: |
  Real estate acquisition underwriting — core, value-add, and opportunistic strategies.
  Activate when the user mentions property acquisition, underwriting, value-add,
  renovation, multifamily acquisition, industrial purchase, office building, retail center,
  comparable sales, NOI analysis, cap rate, going-in yield, hold period returns,
  cash-on-cash, equity multiple, property-level IRR, or lease roll analysis.
---

# Real Estate Acquisitions

I run acquisition underwriting for income-producing real estate across all property types and investment strategies. I build every analysis with the discipline of a real estate PE associate preparing for investment committee: explicit assumptions, transparent cash flows, and rigorous stress testing.

---

## Scope & Boundaries

**What this skill DOES:**
- Value properties using direct capitalization, DCF (10-year hold), and comparable sales
- Build NOI from rent roll fundamentals (GPR → vacancy → EGI → other income → OpEx → NOI)
- Analyze cap rate dynamics, spreads to Treasuries, and rate sensitivity
- Model value-add / renovation scenarios with cost basis and stabilized yield
- Analyze lease structures, WALT, tenant credit, renewal economics, and lease roll exposure
- Calculate levered returns (cash-on-cash, equity multiple, IRR) across multiple exit scenarios
- Stress test against cap rate expansion, rent decline, vacancy spikes, and rate increases

**Use a different skill when:**
- Ground-up development → `/re-development`
- Debt sizing and capital stack structuring → `/re-debt`
- REIT or public market real estate analysis → `/re-reit`
- Portfolio allocation to real estate → `/wealth` or `/portfolio`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Cap Rate & Valuation | `python3 tools/cap_rate.py` | Direct cap valuation, cap rate decomposition, sensitivity |
| NOI Builder | `python3 tools/re_noi.py` | Build NOI from rent roll, project forward with growth |
| DCF | `python3 tools/dcf.py` | 10-year hold period DCF valuation |
| IRR / NPV | `python3 tools/irr.py` | Equity-level IRR, NPV, MOIC, payback |
| Debt Sizing | `python3 tools/re_debt.py` | Size the loan to determine equity required |
| Loan Amort | `python3 tools/loan_amort.py` | Debt service schedule |
| Equity Waterfall | `python3 tools/re_waterfall.py` | GP/LP promote structure for fund deals |
| Depreciation | `python3 tools/depreciation.py` | Tax depreciation (MACRS 27.5/39yr) |

---

## Pre-Flight Checks

1. **Investment strategy:** Core, core-plus, value-add, or opportunistic?
2. **Property type:** Multifamily, office, industrial, retail, hospitality, alternative?
3. **Location:** MSA, submarket, class (A/B/C)?
4. **Financial data:** NOI (in-place and projected), occupancy, rent per unit/SF, OpEx breakdown
5. **Transaction terms:** Price, cap rate, hold period, financing terms
6. **Value-add scope (if applicable):** Renovation budget, rent premium, timeline

---

## Phase 1: NOI Build-Up

**Goal:** Construct NOI from fundamentals — never accept a single number without decomposing it.

```
Gross Potential Rent (GPR) = Units × Rent/Unit × 12
(-) Vacancy & Collection Loss = GPR × (1 - Occupancy)
= Effective Gross Income (EGI)
(+) Other Income (parking, laundry, fees): typically 3-8% of GPR
= Total Revenue
(-) Operating Expenses:
    Property taxes, insurance, utilities, R&M, management (3-5% of EGI),
    G&A, landscaping, turnover costs, pest control
(-) Capital Reserves: $250-500/unit/year (multifamily) or $0.15-0.50/SF (commercial)
= Net Operating Income (NOI)
```

Run: `python3 tools/re_noi.py --units [X] --rent [X] --occupancy [X] --opex-ratio [X] --years 5`

**Sanity checks:**
- OpEx ratio: Multifamily 35-50%, Office 30-45%, Industrial 15-25%, Retail 20-35%
- NOI per unit: Compare to submarket comps
- Implied value per unit/SF at market cap rate: Compare to replacement cost

**Decision Gate:** If in-place NOI relies on above-market rents or unsustainable occupancy, flag the risk and model a downside case with normalized assumptions.

---

## Phase 2: Valuation (Three Methods)

**Goal:** Establish property value using independent methods and reconcile.

### Direct Capitalization
```
Value = NOI / Cap Rate
```
Run: `python3 tools/cap_rate.py --noi [X] --cap-rate [X]`

### Discounted Cash Flow (10-Year Hold)
- Year 1-10 NOI with rent growth, expense growth, capex reserves, leasing costs
- Terminal value = Year 11 NOI / (Going-in cap + 25-50bps for aging)
- Discount rate: Core 6-8%, Value-add 8-11%, Opportunistic 12%+

### Comparable Sales
- 3-5 recent transactions in the submarket
- Adjust for location, age, tenant quality, lease structure, lot size

### Reconciliation Weights
| Strategy | Direct Cap | Comps | DCF |
|----------|-----------|-------|-----|
| Stabilized | 50% | 30% | 20% |
| Value-add | 30% | 20% | 50% |
| Development | 10% | 30% | 60% |

---

## Phase 3: Value-Add / Renovation Modeling

**Goal:** Underwrite renovation economics with yield on cost and profit on cost targets.

```
Purchase Price:              $[X]M (going-in cap: [X]%)
(+) Renovation Capex:        $[X]M ($[X] per unit)
(+) Carry Costs:             $[X]M (debt service + operating deficit during reno)
= Total Basis:               $[X]M

Post-Renovation:
  Rent Premium:              $[X]/unit/month above unrenovated comps
  Stabilized Occupancy:      [X]%
  Stabilized NOI:            $[X]M

Yield on Cost = Stabilized NOI / Total Basis
Stabilized Value = Stabilized NOI / Exit Cap Rate
Profit on Cost = (Stabilized Value - Total Basis) / Total Basis
```

**Targets:** Yield on cost 100-200bps above going-in cap. Profit on cost 15-30%.

Run: `python3 tools/re_development.py --land [purchase_price] --hard [reno_cost] --noi [stabilized_noi] --exit-cap [X]`

---

## Phase 4: Lease Roll & Tenant Analysis

**Goal:** Identify lease expiration risk and mark-to-market opportunity.

For each major tenant:
1. **Lease type:** NNN, gross, or modified gross
2. **Current vs. market rent:** Above/below market and by how much
3. **Term remaining and WALT** across the rent roll
4. **Renewal probability:** Based on tenant industry, fit, relocation cost
5. **Tenant credit:** Investment grade, national, regional, local
6. **Co-tenancy and kick-out clauses**

```
| Year | SF Expiring | % of Total | Current Rent | Market Rent | Mark-to-Market |
|------|-------------|-----------|-------------|-------------|----------------|
| 1    | [X] SF      | [X]%      | $[X]/SF     | $[X]/SF     | +/-[X]%        |
| 2    | [X] SF      | [X]%      | $[X]/SF     | $[X]/SF     | +/-[X]%        |
```

**Decision Gate:** If >25% of rent roll expires in any single year, model a downside case with 50% renewal probability and 6-month downtime on vacated space.

---

## Phase 5: Returns Analysis

**Goal:** Calculate levered equity returns across base, upside, and downside scenarios.

```
Equity Cash Flows:
  Year 0: -(Purchase Price + Closing Costs - Loan Proceeds) = -Equity Invested
  Years 1-N: NOI - Debt Service = Pre-Tax Cash Flow
  Year N: Sale Proceeds - Loan Payoff - Closing Costs

Cash-on-Cash (Year 1) = (NOI - Debt Service) / Equity Invested
Equity Multiple = Total Distributions / Equity Invested
IRR = discount rate where NPV of equity cash flows = 0
```

Run: `python3 tools/irr.py --cfs="[equity_cfs]"` and `python3 tools/re_waterfall.py --equity [X] --cfs [X]`

### Sensitivity Table (IRR)
| Exit Cap \ Rent Growth | 2% | 3% | 4% |
|----------------------|------|------|------|
| 5.0% | [X]% | [X]% | [X]% |
| 5.5% | [X]% | [X]% | [X]% |
| 6.0% | [X]% | [X]% | [X]% |

---

## Phase 6: Stress Testing

**Goal:** Break the thesis before committing capital.

| Stress Scenario | Assumption Change | Impact on IRR | Kill Thesis? |
|----------------|-------------------|--------------|-------------|
| Cap rate expansion +100bps | Exit at [X+1]% vs [X]% | -[X]% IRR | |
| Vacancy spike to [X+10]% | 12-month elevated vacancy | -[X]% IRR | |
| Rent decline -10% | Market correction | -[X]% IRR | |
| Rate shock +200bps | Refi at higher rate | -[X]% IRR | |
| Major tenant default | Largest tenant vacates | -[X]% IRR | |

**Decision Gate:** If any plausible single-factor stress drops IRR below the return hurdle, the deal needs structural protection (lower price, higher reserves, or a different capital structure).

---

## Quality Gates

- [ ] NOI built from fundamentals (not just a number from the broker)
- [ ] Three independent valuation methods with reconciliation
- [ ] Cap rate sensitivity analysis included
- [ ] Debt sized from DSCR/LTV/DY constraints (not just assumed)
- [ ] Lease roll schedule analyzed with mark-to-market
- [ ] Returns across base/upside/downside scenarios
- [ ] Stress tests run and documented
- [ ] No hallucinated market data

## Hard Constraints

- **NEVER** use a cap rate without justifying it relative to Treasuries and market comps
- **NEVER** present a single IRR without a sensitivity table
- **ALWAYS** build NOI from components — never accept a number without decomposing it
- **ALWAYS** test for positive leverage before recommending debt

## Common Pitfalls

1. **Trusting the broker's pro forma NOI** — always rebuild from fundamentals
2. **Ignoring capex reserves** — deferred maintenance destroys returns
3. **Linear rent growth forever** — model a cycle, not a straight line
4. **Forgetting lease-up costs on value-add** — TI, LC, free rent add up fast
5. **Assuming exit cap = going-in cap** — cap rates can expand

## Related Skills

- `/re-development` — ground-up construction analysis
- `/re-debt` — capital stack structuring and debt sizing
- `/re-reit` — public REIT valuation
- `/lbo` — for operating company real estate (hotel, senior living operators)
