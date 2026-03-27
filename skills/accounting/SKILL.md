---
name: accounting
description: |
  Accounting analysis — journal entries, chart of accounts, accruals, and closing process.
  Activate when the user mentions journal entry, adjusting entry, closing entry, accrual,
  deferral, chart of accounts, trial balance, general ledger, accounts receivable,
  accounts payable, depreciation entry, amortization entry, revenue recognition,
  ASC 606, lease accounting, ASC 842, intercompany, consolidation, or asks about
  recording transactions, month-end close, or accounting treatment for a specific event.
---

# Accounting

I handle accounting analysis with the precision of a senior accountant preparing workpapers for review. Every journal entry must balance, every accrual must have a reversal plan, and every accounting treatment must cite the applicable standard. I bridge the gap between raw transactions and the clean financial data that feeds into every other Alpha Stack skill.

---

## Scope & Boundaries

**What this skill DOES:**
- Draft journal entries for complex transactions (M&A, leases, revenue recognition, equity compensation)
- Design and review chart of accounts structures
- Build month-end and year-end close checklists with adjusting entries
- Analyze revenue recognition under ASC 606 (five-step model)
- Model lease accounting under ASC 842 (ROU asset, lease liability)
- Prepare consolidation and intercompany elimination entries
- Calculate and record depreciation, amortization, and impairment
- Reconcile accounts and identify discrepancies
- Translate accounting outputs into inputs for financial analysis tools

**Use a different skill when:**
- Building complete financial statements → `/financial-statements`
- Auditing the books → `/audit`
- Extracting data from raw documents → `/data-entry`
- FP&A and variance analysis → `/fpa`
- Tax planning (estate, corporate) → `/estate` or `/fpa`

---

## Pre-Flight Checks

1. **Transaction type:** What economic event needs to be recorded?
2. **Accounting basis:** GAAP, IFRS, or cash basis?
3. **Entity type:** Corporation, partnership, LLC, nonprofit?
4. **Period:** What accounting period does this apply to?
5. **Materiality:** Is this material enough to warrant a separate entry or can it be grouped?
6. **Supporting documentation:** What source documents exist (invoice, contract, bank statement)?

---

## Phase 1: Journal Entry Preparation

**Goal:** Record economic events with proper debits, credits, and documentation.

### Standard Entry Format
```
Date: [YYYY-MM-DD]
Entry #: [JE-XXXX]
Description: [Clear description of the transaction and business purpose]

| Account | Account # | Debit | Credit |
|---------|-----------|-------|--------|
| [Account name] | [XXXX] | $[X] | |
| [Account name] | [XXXX] | | $[X] |
| **Total** | | **$[X]** | **$[X]** |

Supporting reference: [Invoice #, contract ref, approval]
Reversal: [Auto-reverse in next period? Y/N]
```

### Common Transaction Patterns

**Revenue recognition (ASC 606 — five-step model):**
```
Step 1: Identify the contract — signed agreement, purchase order, or implied
Step 2: Identify performance obligations — distinct goods/services
Step 3: Determine transaction price — fixed, variable, constrained
Step 4: Allocate price to obligations — standalone selling prices
Step 5: Recognize revenue — point in time or over time

Entry (point-in-time, delivery):
  DR  Accounts Receivable        $[X]
    CR  Revenue                          $[X]

Entry (over time, percentage of completion):
  DR  Contract Asset             $[X]
    CR  Revenue                          $[X]

Deferred revenue (payment before delivery):
  DR  Cash                       $[X]
    CR  Deferred Revenue                 $[X]
  [Recognized when obligation satisfied]
```

**Lease accounting (ASC 842):**
```
Operating lease (lessee, at commencement):
  DR  Right-of-Use Asset         $[X] (PV of lease payments)
    CR  Lease Liability                  $[X]

Monthly payment:
  DR  Lease Expense              $[X] (straight-line)
  DR  Lease Liability            $[X] (principal portion)
    CR  Cash                             $[X]
    CR  Right-of-Use Asset               $[X] (amortization)

Finance lease — similar but split interest expense and amortization
```

**Equity compensation (stock options):**
```
Grant date fair value: $[X] per option × [X] options = $[X] total
Vesting period: [X] years

Annual entry:
  DR  Stock Compensation Expense  $[X] (total / vesting years)
    CR  Additional Paid-in Capital        $[X]
```

---

## Phase 2: Month-End Close Process

**Goal:** Systematic close that produces accurate, complete financial statements.

### Close Checklist
```
| # | Task | Owner | Status |
|---|------|-------|--------|
| 1 | Bank reconciliation — all accounts | | [ ] |
| 2 | Accounts receivable — aging review, bad debt estimate | | [ ] |
| 3 | Accounts payable — completeness check, cutoff | | [ ] |
| 4 | Inventory count / valuation (if applicable) | | [ ] |
| 5 | Prepaid expenses — amortize current month | | [ ] |
| 6 | Accrued expenses — payroll, benefits, utilities, interest | | [ ] |
| 7 | Depreciation and amortization | | [ ] |
| 8 | Revenue recognition — deferred revenue roll-forward | | [ ] |
| 9 | Intercompany transactions — elimination entries | | [ ] |
| 10 | Equity — stock comp expense, treasury stock, dividends | | [ ] |
| 11 | Tax provision — current and deferred | | [ ] |
| 12 | Trial balance review — analytical procedures | | [ ] |
| 13 | Management review and approval | | [ ] |
```

### Adjusting Entries Categories
```
1. Accruals — expense incurred but not yet paid
   DR  Expense    CR  Accrued Liability

2. Deferrals — cash received/paid but not yet earned/consumed
   DR  Deferred Revenue    CR  Revenue (as earned)

3. Estimates — bad debt, warranty, depreciation
   DR  Expense    CR  Allowance/Reserve

4. Reclassifications — correct prior mispostings
   DR  Correct Account    CR  Incorrect Account

5. Eliminations — intercompany, consolidation
   DR  Intercompany Revenue    CR  Intercompany Expense
```

---

## Phase 3: Chart of Accounts Design

**Goal:** Structure the CoA to support both reporting and analysis.

```
Standard numbering convention:
  1000-1999  Assets
    1000-1099  Cash and equivalents
    1100-1199  Receivables
    1200-1299  Inventory
    1300-1399  Prepaid and other current
    1500-1599  Fixed assets (gross)
    1600-1699  Accumulated depreciation
    1700-1799  Intangible assets
    1800-1899  Other non-current
  2000-2999  Liabilities
    2000-2099  Accounts payable
    2100-2199  Accrued expenses
    2200-2299  Deferred revenue
    2300-2399  Current debt
    2500-2599  Long-term debt
    2600-2699  Lease liabilities
  3000-3999  Equity
  4000-4999  Revenue
  5000-5999  Cost of goods sold / cost of revenue
  6000-6999  Operating expenses
    6000-6099  Compensation
    6100-6199  Benefits
    6200-6299  Rent and facilities
    6300-6399  Technology and software
    6400-6499  Professional services
    6500-6599  Travel and entertainment
    6600-6699  Marketing
    6700-6799  Depreciation and amortization
  7000-7999  Other income / expense
  8000-8999  Tax provision
  9000-9999  Intercompany
```

**Design principles:**
- Granularity should match reporting needs (don't over-segment for a small company)
- Every account maps to exactly one financial statement line
- Department/cost center segmentation via dimensions, not separate accounts
- Reserve accounts (allowances) are contra-assets, not liabilities

---

## Phase 4: Reconciliation

**Goal:** Verify account balances are accurate and supported.

### Bank Reconciliation
```
Bank balance per statement:      $[X]
(+) Deposits in transit:         $[X]
(-) Outstanding checks:         ($[X])
(+/-) Bank errors:              ($[X])
= Adjusted bank balance:         $[X]

Book balance per GL:             $[X]
(+) Interest earned:             $[X]
(-) Bank fees:                  ($[X])
(-) NSF checks:                 ($[X])
(+/-) Book errors:              ($[X])
= Adjusted book balance:         $[X]

Difference:                      $0 (must reconcile to zero)
```

### Account Reconciliation Template
```
Account: [name and number]
Period: [month-end date]

GL balance:                      $[X]
Supporting detail:
  | Item | Amount | Reference | Age |
  |------|--------|-----------|-----|
  | [X]  | $[X]   | [ref]     | [days] |
  | [X]  | $[X]   | [ref]     | [days] |
  Total supporting detail:       $[X]
Reconciling items:               $[X]
  (Explained and documented)
```

---

## Quality Gates

- [ ] All journal entries balance (debits = credits)
- [ ] Adjusting entries have clear description and supporting reference
- [ ] Revenue recognition follows ASC 606 five-step model
- [ ] Lease entries comply with ASC 842 (ROU asset and liability recorded)
- [ ] Close checklist completed with all items signed off
- [ ] Reconciliations tie to GL with no unexplained differences
- [ ] Accounting treatment cites applicable standard

## Hard Constraints

- **NEVER** record an entry that doesn't balance
- **NEVER** recognize revenue before the performance obligation is satisfied
- **ALWAYS** cite the applicable accounting standard (ASC/IFRS) for non-routine transactions
- **ALWAYS** document the business purpose and supporting reference for every entry

## Common Pitfalls

1. **Cutoff errors** — recording December revenue in January (or vice versa)
2. **Forgetting to reverse accruals** — double-counting expenses
3. **Capitalizing vs expensing** — applying the wrong threshold or useful life
4. **Intercompany not eliminating** — consolidated financials overstate revenue
5. **Deferred revenue misclassification** — current vs long-term based on delivery timeline

## Related Skills

- `/financial-statements` — build complete statements from the trial balance
- `/audit` — audit the accounting work product
- `/data-entry` — extract and validate source data before recording
- `/fpa` — variance analysis on the resulting financials
- `/budget` — budget-to-actual comparison
