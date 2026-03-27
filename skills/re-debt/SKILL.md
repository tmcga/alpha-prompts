---
name: re-debt
description: |
  Real estate debt structuring across the full capital stack. Activate when the user
  mentions DSCR, LTV, debt yield, mortgage constant, positive leverage, mezzanine debt,
  preferred equity, capital stack, CMBS, construction loan, bridge loan, permanent
  financing, refinancing, interest-only, debt service, loan sizing, multi-tranche,
  subordinate debt, intercreditor, or asks about structuring real estate debt.
---

# Real Estate Debt Structuring

I structure real estate capital stacks from senior mortgage through preferred equity. Every debt decision comes down to three questions: how much can I borrow, what does it cost, and does leverage help or hurt my equity returns? I size loans from binding constraints, test for positive leverage, and structure multi-tranche stacks that optimize the cost of capital while maintaining covenant headroom.

---

## Scope & Boundaries

**What this skill DOES:**
- Size senior mortgages from DSCR, LTV, and debt yield constraints (identify the binding one)
- Test for positive/negative leverage (cap rate vs. mortgage constant)
- Structure multi-tranche capital stacks (senior, mezzanine, preferred equity, common equity)
- Analyze construction loans (LTC, interest reserve, draw schedules, recourse)
- Model bridge-to-permanent financing transitions
- Calculate blended cost of capital across the stack
- Analyze refinancing scenarios and cash-out proceeds
- Stress test debt structures against rate increases and NOI declines

**Use a different skill when:**
- Underwriting the property itself → `/re-acquisitions`
- Development feasibility → `/re-development`
- REIT balance sheet analysis → `/re-reit`
- Corporate credit analysis → `/credit`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Debt Sizing | `python3 tools/re_debt.py` | Size loan from DSCR/LTV/DY, multi-tranche analysis |
| Loan Amort | `python3 tools/loan_amort.py` | Amortization schedule, payoff analysis |
| Equity Waterfall | `python3 tools/re_waterfall.py` | GP/LP split with promote |
| IRR / NPV | `python3 tools/irr.py` | Levered equity returns |
| WACC | `python3 tools/wacc.py` | Blended cost of capital |

---

## Pre-Flight Checks

1. **Property type and strategy:** Stabilized, transitional, or development?
2. **NOI:** In-place and projected (the lender underwrites to the lower)
3. **Property value:** Appraised or purchase price
4. **Debt terms available:** Rate, amort, term, IO period, prepayment
5. **Target leverage:** LTV and DSCR constraints from lender
6. **Capital stack needs:** How much total leverage? Is subordinate debt needed?
7. **Borrower profile:** Recourse vs. non-recourse, sponsor net worth

---

## Phase 1: Senior Debt Sizing

**Goal:** Determine max loan from three independent constraints — the most restrictive wins.

### Constraint 1: Loan-to-Value (LTV)
```
Max Loan = Property Value × Max LTV
Typical: 60-65% (CMBS), 65-75% (bank/life co), 70-80% (agency multifamily)
```

### Constraint 2: Debt Service Coverage Ratio (DSCR)
```
Max Annual Debt Service = NOI / Min DSCR
Max Loan = Max DS / Mortgage Constant
Typical minimum: 1.20x (aggressive), 1.25x (standard), 1.35x (conservative/CMBS)
```

### Constraint 3: Debt Yield
```
Max Loan = NOI / Min Debt Yield
Typical minimum: 8% (aggressive), 9-10% (standard), 12% (conservative)
Debt yield is leverage-neutral — it doesn't change with amortization or rate
```

Run: `python3 tools/re_debt.py --noi [X] --value [X] --rate [X] --amort 30 --max-ltv [X] --min-dscr [X] --debt-yield [X]`

**Decision Gate:** Identify which constraint binds. If DSCR binds (not LTV), the property has a high debt service burden relative to income. If debt yield binds, the lender views the asset as higher risk.

---

## Phase 2: Positive Leverage Test

**Goal:** Determine whether debt helps or hurts equity returns.

```
Mortgage Constant (K) = Annual Debt Service / Loan Amount

If Cap Rate > K → Positive leverage (equity returns ABOVE unlevered)
If Cap Rate < K → Negative leverage (equity returns BELOW unlevered)
If Cap Rate = K → Leverage-neutral
```

**Example:**
```
NOI: $2,000,000 on a $40,000,000 property (5.0% cap)
Loan: $28,000,000 at 6.5%, 30-year amort
Annual DS: $2,123,000
Mortgage Constant: 7.58%

Cap Rate (5.0%) < Mortgage Constant (7.58%) → NEGATIVE LEVERAGE
Every dollar of debt destroys equity return
```

This property needs lower leverage or a lower rate to work. Run the debt sizing tool to find the break-even loan amount where cap rate = mortgage constant.

---

## Phase 3: Multi-Tranche Capital Stack

**Goal:** Structure subordinate debt when senior alone isn't sufficient.

```
Capital Stack:
| Tranche          | Amount  | LTV Range | Rate   | Cumulative DSCR |
|------------------|---------|-----------|--------|-----------------|
| Senior mortgage  | $[X]M   | 0-65%     | [X]%   | [X]x            |
| Mezzanine debt   | $[X]M   | 65-80%    | [X]%   | [X]x            |
| Preferred equity | $[X]M   | 80-90%    | [X]%   | N/A             |
| Common equity    | $[X]M   | 90-100%   | residual| N/A             |
```

Run: `python3 tools/re_debt.py` (multi_tranche function via MCP or Python import)

**Key differences:**
| Feature | Mezzanine | Preferred Equity |
|---------|-----------|-----------------|
| Position | Debt (has lien) | Equity (no lien) |
| Foreclosure rights | Yes (after senior) | No |
| Tax treatment | Interest deductible | Dividend (not deductible) |
| Typical rate | 10-15% | 12-18% |
| Intercreditor | Requires agreement | None needed |
| Bankruptcy | Secured claim | Equity interest |

**Decision Gate:** If combined DSCR (senior + mezz) falls below 1.0x, the capital stack cannot service all debt from current NOI. Either reduce leverage or require an interest reserve.

---

## Phase 4: Loan Types by Strategy

| Strategy | Loan Type | Typical Terms |
|----------|----------|---------------|
| Core/stabilized | Agency (Fannie/Freddie), CMBS, life co | 65-75% LTV, 3.5-5.5%, 5-10yr term, 30yr amort |
| Value-add | Bridge loan | 70-80% LTC, SOFR+300-500, 2-3yr term, IO |
| Development | Construction loan | 60-70% LTC, SOFR+300-500, 18-36mo, IO on draws |
| Distressed | Hard money | 50-65% LTV, 10-15%, 1-2yr, IO, points |

### Bridge Loan Mechanics
```
Bridge loan for value-add:
  LTC: [X]% of total cost (purchase + renovation + carry)
  Rate: SOFR + [X]bps (floating)
  Term: [X] years + [X] extensions
  IO: Typically full term (no amortization)
  Exit: Refinance to permanent or sell

Interest rate cap requirement:
  Most bridge lenders require a SOFR cap
  Cap cost: [X]bps upfront for [X]-year cap at [X]% strike
```

---

## Phase 5: Refinancing Analysis

**Goal:** Model refinance proceeds and equity release.

```
Current property value:    $[X]M (at stabilized cap rate)
Existing loan balance:     $[X]M
New loan sizing:           Based on DSCR/LTV/DY constraints

New loan proceeds:         $[X]M
Less: Existing loan payoff ($[X]M)
Less: Prepayment penalty   ($[X]M)
Less: Closing costs        ($[X]M)
───────────────────────────
= Cash-out to equity:      $[X]M
```

**Tax advantage:** Refinancing proceeds are not taxable income (unlike a sale). A cash-out refi can return capital to investors without triggering capital gains.

---

## Phase 6: Stress Testing

| Scenario | Impact on DSCR | Action Required |
|----------|---------------|-----------------|
| NOI decline -10% | DSCR drops from [X]x to [X]x | Covenant breach? Cash trap? |
| Rate increase +200bps (floating) | DSCR drops from [X]x to [X]x | Rate cap protects to [X]% |
| Cap expansion +100bps on refi | Refi proceeds < current balance | Equity shortfall of $[X]M |
| Both NOI decline + rate increase | Combined DSCR [X]x | Default risk assessment |

**Key question:** At what NOI decline does DSCR breach 1.0x? That's the breakeven NOI. If it requires only a 10-15% decline, the structure is fragile.

---

## Quality Gates

- [ ] Loan sized from all three constraints (DSCR, LTV, DY) with binding identified
- [ ] Positive leverage test performed
- [ ] Multi-tranche stack shows cumulative DSCR at each level
- [ ] Blended cost of capital calculated
- [ ] Refinancing / exit scenario modeled
- [ ] Stress tests include rate shock + NOI decline
- [ ] No assumed debt terms without sourcing from market

## Hard Constraints

- **NEVER** size a loan without checking all three constraints (DSCR, LTV, debt yield)
- **NEVER** recommend leverage without testing if it's positive or negative
- **ALWAYS** show cumulative DSCR when adding subordinate debt
- **ALWAYS** stress test floating rate debt against a +200bps rate increase

## Common Pitfalls

1. **Sizing only to LTV** — DSCR or debt yield often binds tighter
2. **Ignoring negative leverage** — in a high-rate environment, more debt can reduce equity IRR
3. **Forgetting prepayment penalties** — yield maintenance or defeasance on early payoff
4. **Assuming rates at origination hold** — floating rate debt needs rate cap analysis
5. **Mezz without intercreditor** — senior lender has consent rights over subordinate debt

## Related Skills

- `/re-acquisitions` — underwriting the property being financed
- `/re-development` — construction loan structuring
- `/re-reit` — public REIT balance sheet and capital markets analysis
- `/credit` — corporate credit and structured finance analysis
