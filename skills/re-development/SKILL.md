---
name: re-development
description: |
  Ground-up real estate development analysis — entitlement through stabilization.
  Activate when the user mentions development pro forma, ground-up construction,
  yield on cost, development spread, construction financing, LTC, hard costs,
  soft costs, lease-up, stabilization, construction interest, entitlement,
  build-to-suit, spec development, or asks about development feasibility.
---

# Real Estate Development

I analyze ground-up real estate development from site acquisition through stabilization. Every development is a bet on three things: construction cost, lease-up timing, and exit cap rate. I build every pro forma to make those bets explicit and stress-testable.

---

## Scope & Boundaries

**What this skill DOES:**
- Build complete development cost budgets (land, hard, soft, contingency, construction interest)
- Model lease-up schedules with absorption, concessions, TI, and commissions
- Calculate yield on cost, development spread, and profit on cost
- Structure construction financing (LTC, interest reserve, draw schedules)
- Analyze permanent financing take-out scenarios
- Model entitlement risk and timeline uncertainty
- Compare build vs. buy economics

**Use a different skill when:**
- Acquiring a stabilized property → `/re-acquisitions`
- Structuring the capital stack → `/re-debt`
- Analyzing a REIT's development pipeline → `/re-reit`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Development Pro Forma | `python3 tools/re_development.py` | Full cost build, yield on cost, profit on cost |
| Cap Rate | `python3 tools/cap_rate.py` | Exit valuation, development spread |
| NOI Builder | `python3 tools/re_noi.py` | Stabilized NOI projection |
| Debt Sizing | `python3 tools/re_debt.py` | Permanent financing take-out |
| IRR / NPV | `python3 tools/irr.py` | Developer equity returns |
| Equity Waterfall | `python3 tools/re_waterfall.py` | JV promote structure |
| Loan Amort | `python3 tools/loan_amort.py` | Permanent debt service |

---

## Pre-Flight Checks

1. **Property type:** Multifamily, office, industrial, retail, mixed-use, hospitality?
2. **Site details:** Location, acreage, zoning, entitlement status
3. **Program:** Units/SF, building type, stories, parking ratio
4. **Cost inputs:** Land price, hard cost per SF, soft cost percentage
5. **Market rents:** Current asking rents for comparable new construction
6. **Timeline:** Construction duration, lease-up pace, total to stabilization
7. **Financing:** Construction loan terms (LTC, rate, interest reserve)

---

## Phase 1: Development Budget

**Goal:** Build the total development cost from first principles.

```
Land Acquisition:                $[X]M  ($[X] per buildable SF)
(+) Entitlement & Permitting:    $[X]M
(+) Hard Costs:                  $[X]/SF × [X] SF = $[X]M
(+) Soft Costs:                  [15-25]% of hard costs = $[X]M
    (Architecture, engineering, legal, permits, insurance, testing)
(+) Developer Fee:               [3-5]% of total project cost = $[X]M
(+) Construction Contingency:    [5-10]% of hard costs = $[X]M
(+) Construction Interest:       Avg draw × rate × duration = $[X]M
(+) Lease-Up Costs:              TI + LC + free rent = $[X]M
───────────────────────────────────────────────────────────────
= Total Development Cost (TDC):  $[X]M  ($[X] per SF)
```

Run: `python3 tools/re_development.py --land [X] --hard [X] --noi [X] --exit-cap [X] --months [X]`

**Hard cost benchmarks (2024-2025):**
| Property Type | Low | Mid | High |
|--------------|------|------|------|
| Multifamily (wood-frame) | $150/SF | $200/SF | $275/SF |
| Multifamily (concrete) | $250/SF | $325/SF | $450/SF |
| Industrial/Warehouse | $80/SF | $120/SF | $175/SF |
| Office (Class A) | $300/SF | $400/SF | $550/SF |
| Retail | $150/SF | $225/SF | $350/SF |

---

## Phase 2: Lease-Up & Stabilization

**Goal:** Model the path from certificate of occupancy to stabilized NOI.

```
Market rent (new construction):   $[X]/SF or $[X]/unit/month
Net rentable area:                [X] SF (efficiency ratio: [X]%)
Lease-up pace:                    [X] units/month or [X] SF/month
Time to stabilization:            [X] months at [X]% occupancy
Lease-up concessions:             [X] months free rent (average)
Tenant improvements:              $[X]/SF
Leasing commissions:              [X]% of total lease value
```

**Absorption benchmarks:**
- Multifamily: 15-30 units/month (market-dependent)
- Office: 500-2,000 SF/month per 10,000 SF built
- Industrial: Faster — often pre-leased or build-to-suit
- Retail: Slowest — anchor first, in-line follows

**Operating deficit during lease-up:** Budget 6-12 months of expenses + debt service as negative cash flow before stabilization.

---

## Phase 3: Development Returns

**Goal:** Calculate risk-adjusted returns and compare to acquisition alternative.

```
Stabilized NOI:       $[X]M

Yield on Cost = Stabilized NOI / TDC = [X]%
Market Cap Rate:      [X]%
Development Spread = Yield on Cost - Market Cap Rate = [X] bps

Stabilized Value = Stabilized NOI / Market Cap Rate = $[X]M
Profit on Cost = (Stabilized Value - TDC) / TDC = [X]%
```

**Minimum thresholds:**
| Metric | Threshold | Why |
|--------|----------|-----|
| Development spread | ≥100 bps | Compensates for construction + lease-up risk |
| Profit on cost | ≥20% | Minimum for spec development |
| Yield on cost vs. cap rate | YoC > cap rate | Otherwise buy stabilized |

**Decision Gate:** If yield on cost ≤ market cap rate, the developer is creating less value than buying an existing asset. Kill the deal or renegotiate land basis.

---

## Phase 4: Construction Financing

**Goal:** Structure the construction loan and equity requirement.

```
Construction Loan:
  Loan-to-Cost (LTC):          [X]% → Loan: $[X]M
  Rate:                         SOFR + [X] bps (floating on drawn balance)
  Term:                         [X] months + [X] month extension
  Interest Reserve:             $[X]M (funded at close)
  Recourse:                     Completion guarantee, cost overrun guarantee
  Draw Schedule:                Monthly based on construction progress

Developer Equity:               TDC - Construction Loan = $[X]M
Equity as % of TDC:             [X]%
```

**Key lender requirements:**
- Pre-leasing: Office/retail often require 30-50% pre-leased for funding
- Multifamily: Usually funded on spec with strong sponsor track record
- Cost overrun reserve: 5-10% of hard costs, released upon completion
- Completion guarantee: Sponsor guarantees project will be finished

---

## Phase 5: Permanent Financing Take-Out

**Goal:** Model the transition from construction loan to permanent mortgage.

Run: `python3 tools/re_debt.py --noi [stabilized_NOI] --value [stabilized_value] --rate [perm_rate] --min-dscr 1.25 --max-ltv 0.70`

```
Construction loan payoff:        $[X]M
Permanent loan proceeds:         $[X]M (sized from DSCR/LTV/DY)
Cash out / (shortfall):          $[X]M
Developer equity remaining:      $[X]M
```

If permanent loan doesn't cover construction loan payoff → equity gap that needs mezzanine, preferred equity, or additional sponsor equity.

---

## Phase 6: Stress Testing

| Scenario | Change | Impact | Kill? |
|----------|--------|--------|-------|
| Hard cost overrun +15% | TDC increases $[X]M | YoC drops [X]bps | |
| Lease-up takes 2x longer | 12 more months of carry | IRR drops [X]% | |
| Rent achievable -10% | Stabilized NOI down [X]% | Profit on cost drops to [X]% | |
| Exit cap expansion +75bps | Stabilized value down [X]% | May not cover construction loan | |
| Construction delay +6 months | Additional interest + opportunity cost | IRR drops [X]% | |

**The development killer question:** "What rent do we need to achieve breakeven yield on cost equal to the market cap rate?" If that rent is above current market, the project is speculating on rent growth, not creating value.

---

## Quality Gates

- [ ] Complete cost budget with hard costs benchmarked to property type
- [ ] Lease-up timeline validated against submarket absorption rates
- [ ] Development spread calculated and justified (≥100bps)
- [ ] Construction financing structured with interest reserve
- [ ] Permanent take-out modeled with DSCR/LTV constraints
- [ ] Stress tests: cost overrun, delayed lease-up, lower rents, cap expansion
- [ ] No fabricated construction costs or market rents

## Hard Constraints

- **NEVER** assume hard costs without benchmarking to property type and market
- **NEVER** model lease-up faster than submarket absorption data supports
- **ALWAYS** include construction interest in total development cost
- **ALWAYS** calculate development spread — if it's negative, the deal doesn't pencil

## Common Pitfalls

1. **Forgetting construction interest** — it's 5-10% of total cost
2. **Aggressive lease-up pace** — verify against actual absorption in submarket
3. **Ignoring soft costs** — A&E, legal, permits, insurance, testing add 15-25%
4. **No contingency** — construction always costs more than the budget
5. **Assuming exit = build-to-suit cap rate** — spec gets a wider cap rate

## Related Skills

- `/re-acquisitions` — buy vs. build comparison
- `/re-debt` — capital stack structuring for the entire project
- `/re-reit` — how REITs value their development pipeline
- `/lbo` — for operating businesses occupying the real estate
