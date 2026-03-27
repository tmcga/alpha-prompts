---
name: private-credit
description: |
  Private credit analysis — direct lending, mezzanine, and unitranche.
  Activate when the user mentions direct lending, private credit, unitranche,
  first lien term loan, second lien, mezzanine lending, PIK, payment-in-kind,
  covenant analysis, leverage covenant, fixed charge coverage, credit agreement,
  debt fund, BDC, CLO, expected loss, recovery analysis, sponsor-backed lending,
  or asks about underwriting a private loan or credit facility.
---

# Private Credit Analysis

I underwrite private credit facilities with the discipline of a credit committee analyst: cash flow first, collateral second, covenants third. Every credit decision answers one question — can this borrower service the debt through a downturn? I model cash flows under stress, design covenants that provide early warning, and calculate risk-adjusted returns net of expected losses.

---

## Scope & Boundaries

**What this skill DOES:**
- Underwrite direct lending facilities (first lien, unitranche, second lien)
- Analyze borrower cash flows: EBITDA quality, FCF conversion, interest coverage
- Design covenant packages: leverage, coverage, capex limits, restricted payments
- Model expected losses: probability of default × loss given default
- Calculate risk-adjusted yields: gross spread - expected loss - origination cost
- Evaluate PIK structures and their impact on effective yield and risk
- Analyze intercreditor dynamics in multi-tranche structures
- Stress test credit under revenue decline, margin compression, and rate increases

**Use a different skill when:**
- Taking equity control → `/pe-buyout`
- Public high-yield or IG bonds → `/credit`
- Real estate debt → `/re-debt`
- Restructuring a troubled credit → `/restructuring`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Credit Spread | `python3 tools/credit_spread.py` | Z-Score, implied default probability |
| Merton Model | `python3 tools/merton_model.py` | Structural default probability |
| IRR / NPV | `python3 tools/irr.py` | Lender return calculation |
| Loan Amort | `python3 tools/loan_amort.py` | Amortization and payoff schedules |
| LBO | `python3 tools/lbo.py` | Understand sponsor's equity cushion |

---

## Pre-Flight Checks

1. **Borrower profile:** Company, industry, revenue, EBITDA, ownership (sponsor-backed?)
2. **Facility terms:** Size, rate (SOFR+spread), maturity, amortization, PIK component
3. **Capital structure:** Full debt stack — all tranches with amounts, rates, maturities
4. **Financial data:** 3 years of historical P&L + projections, cash flow statement
5. **Collateral:** Asset base, lien priority, collateral coverage ratio
6. **Sponsor context:** Equity cushion, fund vintage, track record, follow-on capacity

---

## Phase 1: Cash Flow Underwriting

**Goal:** Determine the borrower's ability to service debt from operating cash flows.

```
EBITDA Quality Adjustments:
  Reported EBITDA:                    $[X]M
  (-) Non-recurring add-backs:       ($[X]M)  ← haircut aggressive add-backs
  (-) Stock-based compensation:      ($[X]M)  ← real cost, not just non-cash
  (-) Deferred revenue changes:      ($[X]M)  ← if flattering cash flow
  = Adjusted EBITDA:                  $[X]M

Cash Flow Available for Debt Service:
  Adjusted EBITDA:                    $[X]M
  (-) Cash taxes:                    ($[X]M)
  (-) Maintenance capex:             ($[X]M)
  (-) Working capital change:        ($[X]M)
  (-) Cash restructuring costs:      ($[X]M)
  = Free Cash Flow:                   $[X]M
  (-) Mandatory amortization:        ($[X]M)
  = FCF After Debt Amort:             $[X]M

FCF Conversion: FCF / EBITDA = [X]%  (target: >50%)
```

**Decision Gate:** If FCF conversion <40% after mandatory amort, the borrower may struggle to deleverage. Consider tighter amortization or a cash sweep.

---

## Phase 2: Credit Metrics & Coverage

**Goal:** Calculate leverage and coverage ratios at close and projected.

```
| Metric                    | Close | Year 1 | Year 2 | Year 3 | Covenant |
|---------------------------|-------|--------|--------|--------|----------|
| Total Leverage (Debt/EBITDA) | [X]x | | | | ≤[X]x |
| Senior Leverage | [X]x | | | | ≤[X]x |
| Interest Coverage (EBITDA/Int) | [X]x | | | | ≥[X]x |
| Fixed Charge Coverage | [X]x | | | | ≥[X]x |
| FCF / Total Debt Service | [X]x | | | | |
```

Run: `python3 tools/credit_spread.py` for Z-Score assessment

**Covenant headroom:** Calculate the % decline in EBITDA before each covenant trips.
```
Leverage covenant at [X]x with current EBITDA $[X]M and debt $[X]M:
  Current leverage: [X]x
  EBITDA can decline [X]% (to $[X]M) before breach
  That's $[X]M of headroom — [X] quarters of EBITDA cushion
```

---

## Phase 3: Covenant Design

**Goal:** Design covenants that provide early warning without being overly restrictive.

**Standard covenant package:**

| Covenant | Level | Test Frequency | Purpose |
|----------|-------|---------------|---------|
| Total leverage | ≤[X]x, stepping to [X]x | Quarterly | Limit borrowing capacity |
| Interest coverage | ≥[X]x | Quarterly | Ensure debt service ability |
| Capex limit | ≤$[X]M/year | Annual | Preserve cash for debt service |
| Restricted payments | None above [X]x leverage | Ongoing | Prevent cash leakage |
| Minimum liquidity | ≥$[X]M | Monthly | Early warning trigger |
| Excess cash flow sweep | [X]% above $[X]M | Annual | Accelerate deleveraging |

**Incurrence vs. maintenance covenants:**
- **Maintenance:** Tested every quarter regardless of action (tighter — preferred by lenders)
- **Incurrence:** Tested only when borrower takes action (looser — preferred by sponsors)

**Decision Gate:** If the sponsor insists on cov-lite (no maintenance covenants), increase the spread by 50-100bps to compensate for reduced lender control.

---

## Phase 4: Risk-Adjusted Return

**Goal:** Calculate the all-in yield net of expected losses and costs.

```
Gross Yield Calculation:
  SOFR (base rate):              [X]%
  (+) Credit spread:             +[X]bps
  (+) PIK component:             +[X]bps
  (+) OID (amortized):           +[X]bps
  (+) Upfront fee (amortized):   +[X]bps
  = Gross yield:                  [X]%

Expected Loss:
  Probability of default (5-yr):  [X]%
  Loss given default:             [X]%  (1 - recovery rate)
  Expected loss (annual):         [X]bps

Risk-Adjusted Yield = Gross Yield - Expected Loss = [X]%
```

Run: `python3 tools/merton_model.py` for structural default probability

**Yield vs. risk benchmarks:**
| Rating Equivalent | Spread | Expected Loss | Net Spread |
|------------------|--------|--------------|-----------|
| BB | 400-500bps | 50-100bps | 300-450bps |
| B | 550-700bps | 100-200bps | 350-550bps |
| CCC | 800-1200bps | 300-600bps | 500-600bps |

---

## Phase 5: Stress Testing

| Scenario | EBITDA Impact | Leverage | Coverage | Default? |
|----------|-------------|---------|---------|---------|
| Base case | — | [X]x | [X]x | No |
| Revenue -10% | -[X]% EBITDA | [X]x | [X]x | |
| Revenue -20% | -[X]% EBITDA | [X]x | [X]x | |
| Margin compression -300bps | -[X]% EBITDA | [X]x | [X]x | |
| SOFR +200bps | Interest +$[X]M | [X]x | [X]x | |
| Combined stress | All of above | [X]x | [X]x | |

**Key question:** Under the combined stress scenario, can the borrower still cover interest? If not, what's the recovery value in a restructuring?

---

## Quality Gates

- [ ] EBITDA quality adjusted (add-backs haircut, SBC included)
- [ ] FCF waterfall built showing cash available for debt service
- [ ] Leverage and coverage ratios calculated at close and projected
- [ ] Covenant headroom calculated as % EBITDA decline to breach
- [ ] Expected loss estimated (PD × LGD)
- [ ] Risk-adjusted yield calculated
- [ ] Stress tests run: revenue decline, margin compression, rate shock

## Hard Constraints

- **NEVER** underwrite to projected EBITDA — use trailing adjusted EBITDA for sizing
- **NEVER** ignore the quality of EBITDA add-backs — haircut aggressive adjustments by 50%+
- **ALWAYS** calculate FCF conversion — EBITDA without cash flow is a mirage
- **ALWAYS** stress test interest coverage under a +200bps rate shock

## Common Pitfalls

1. **Trusting sponsor add-backs** — "run-rate" and "synergy" adjustments are optimistic by definition
2. **Ignoring working capital swings** — fast-growing borrowers consume cash in receivables/inventory
3. **PIK without exit visibility** — PIK accrues silently and crystallizes into real debt at maturity
4. **Cov-lite without spread premium** — giving up protections for free destroys risk-adjusted returns
5. **Ignoring the equity cushion** — a thinly capitalized sponsor may not support the business in stress

## Related Skills

- `/pe-buyout` — understanding the sponsor's investment thesis and equity returns
- `/credit` — public credit analysis (HY bonds, IG, distressed)
- `/restructuring` — when the credit goes wrong
- `/re-debt` — real estate-specific lending
