---
name: financial-statements
description: |
  Financial statement preparation, analysis, and interpretation. Activate when the user
  mentions income statement, balance sheet, cash flow statement, P&L, profit and loss,
  statement of operations, statement of financial position, indirect method, common-size
  analysis, ratio analysis, DuPont analysis, trend analysis, vertical analysis, horizontal
  analysis, financial statement footnotes, or asks about preparing, analyzing, or
  interpreting financial statements.
---

# Financial Statements

I build and analyze financial statements with the discipline of a controller preparing for board presentation and the analytical lens of a credit analyst reading them. Financial statements are the universal language of business — every other Alpha Stack skill ultimately reads from or writes to these three documents. I ensure they're built correctly and interpreted meaningfully.

---

## Scope & Boundaries

**What this skill DOES:**
- Build income statements, balance sheets, and cash flow statements from trial balance data
- Prepare cash flow statements using the indirect method
- Run common-size (vertical) and trend (horizontal) analysis
- Calculate and interpret financial ratios (liquidity, profitability, leverage, efficiency)
- Perform DuPont analysis to decompose return on equity
- Identify red flags and quality-of-earnings issues
- Prepare management discussion sections for key line items
- Convert between GAAP and non-GAAP presentations (EBITDA, adjusted earnings)

**Use a different skill when:**
- Recording individual transactions → `/accounting`
- Auditing the statements → `/audit`
- FP&A variance analysis → `/fpa`
- Building a DCF from projected financials → run `tools/dcf.py`
- Credit analysis using financial statements → `/credit` or `/private-credit`

---

## Pre-Flight Checks

1. **Statement type:** Income statement, balance sheet, cash flow, or all three?
2. **Basis:** GAAP, IFRS, or management reporting?
3. **Period:** Monthly, quarterly, or annual? Comparative periods?
4. **Data source:** Trial balance, prior statements, raw data?
5. **Purpose:** External reporting, bank covenant, investor presentation, internal management?
6. **Industry:** Determines relevant metrics and presentation conventions

---

## Phase 1: Income Statement

**Goal:** Build a clear P&L that shows the path from revenue to net income.

```
[Company Name]
Income Statement
For the Period Ended [Date]

                                    Current     Prior      Change
Revenue:
  Product revenue                   $[X]M       $[X]M      [X]%
  Service revenue                   $[X]M       $[X]M      [X]%
  Total Revenue                     $[X]M       $[X]M      [X]%

Cost of Revenue:
  Product COGS                     ($[X]M)     ($[X]M)
  Service delivery costs           ($[X]M)     ($[X]M)
  Total Cost of Revenue            ($[X]M)     ($[X]M)

Gross Profit                        $[X]M       $[X]M      [X]%
  Gross Margin                      [X]%        [X]%

Operating Expenses:
  Sales & marketing                ($[X]M)     ($[X]M)
  Research & development           ($[X]M)     ($[X]M)
  General & administrative         ($[X]M)     ($[X]M)
  Depreciation & amortization      ($[X]M)     ($[X]M)
  Total Operating Expenses         ($[X]M)     ($[X]M)

Operating Income (EBIT)             $[X]M       $[X]M      [X]%
  Operating Margin                  [X]%        [X]%

Other Income/(Expense):
  Interest expense                 ($[X]M)     ($[X]M)
  Interest income                   $[X]M       $[X]M
  Other                             $[X]M       $[X]M

Income Before Tax                   $[X]M       $[X]M
  Provision for income taxes       ($[X]M)     ($[X]M)
  Effective tax rate                [X]%        [X]%

Net Income                          $[X]M       $[X]M      [X]%
  Net Margin                        [X]%        [X]%

Non-GAAP Reconciliation:
  Net Income                        $[X]M
  (+) D&A                           $[X]M
  (+) Stock-based compensation      $[X]M
  (+) One-time restructuring        $[X]M
  = Adjusted EBITDA                 $[X]M       [X]% margin
```

---

## Phase 2: Balance Sheet

**Goal:** Present financial position at a point in time — what the company owns, owes, and is worth to shareholders.

```
[Company Name]
Balance Sheet
As of [Date]

ASSETS                              Current     Prior
Current Assets:
  Cash and equivalents              $[X]M       $[X]M
  Accounts receivable, net          $[X]M       $[X]M
  Inventory                         $[X]M       $[X]M
  Prepaid expenses                  $[X]M       $[X]M
  Total Current Assets              $[X]M       $[X]M

Non-Current Assets:
  Property, plant & equipment, net  $[X]M       $[X]M
  Right-of-use assets               $[X]M       $[X]M
  Goodwill                          $[X]M       $[X]M
  Intangible assets, net            $[X]M       $[X]M
  Other non-current                 $[X]M       $[X]M
  Total Non-Current Assets          $[X]M       $[X]M

TOTAL ASSETS                        $[X]M       $[X]M

LIABILITIES
Current Liabilities:
  Accounts payable                  $[X]M       $[X]M
  Accrued expenses                  $[X]M       $[X]M
  Deferred revenue (current)        $[X]M       $[X]M
  Current portion of debt           $[X]M       $[X]M
  Lease liabilities (current)       $[X]M       $[X]M
  Total Current Liabilities         $[X]M       $[X]M

Non-Current Liabilities:
  Long-term debt                    $[X]M       $[X]M
  Lease liabilities (non-current)   $[X]M       $[X]M
  Deferred tax liabilities          $[X]M       $[X]M
  Other non-current                 $[X]M       $[X]M
  Total Non-Current Liabilities     $[X]M       $[X]M

TOTAL LIABILITIES                   $[X]M       $[X]M

EQUITY
  Common stock                      $[X]M       $[X]M
  Additional paid-in capital        $[X]M       $[X]M
  Retained earnings                 $[X]M       $[X]M
  Treasury stock                   ($[X]M)     ($[X]M)
  AOCI                             ($[X]M)     ($[X]M)
TOTAL EQUITY                        $[X]M       $[X]M

TOTAL LIABILITIES + EQUITY          $[X]M       $[X]M
  (Must equal Total Assets)
```

---

## Phase 3: Cash Flow Statement (Indirect Method)

**Goal:** Reconcile net income to actual cash generated — the most important statement for credit and valuation.

```
[Company Name]
Statement of Cash Flows
For the Period Ended [Date]

OPERATING ACTIVITIES
  Net Income                                    $[X]M
  Adjustments for non-cash items:
    Depreciation & amortization                 $[X]M
    Stock-based compensation                    $[X]M
    Deferred income taxes                       $[X]M
    Amortization of debt issuance costs         $[X]M
  Changes in working capital:
    Accounts receivable                        ($[X]M)  ← increase = cash outflow
    Inventory                                  ($[X]M)
    Prepaid expenses                           ($[X]M)
    Accounts payable                            $[X]M   ← increase = cash inflow
    Accrued expenses                            $[X]M
    Deferred revenue                            $[X]M
  Net Cash from Operating Activities            $[X]M

INVESTING ACTIVITIES
    Capital expenditures                       ($[X]M)
    Acquisitions, net of cash acquired         ($[X]M)
    Purchases of investments                   ($[X]M)
    Proceeds from asset sales                   $[X]M
  Net Cash from Investing Activities           ($[X]M)

FINANCING ACTIVITIES
    Proceeds from debt                          $[X]M
    Repayment of debt                          ($[X]M)
    Proceeds from equity issuance               $[X]M
    Share repurchases                          ($[X]M)
    Dividends paid                             ($[X]M)
    Debt issuance costs                        ($[X]M)
  Net Cash from Financing Activities           ($[X]M)

NET CHANGE IN CASH                              $[X]M
Beginning cash balance                          $[X]M
Ending cash balance                             $[X]M

Free Cash Flow (non-GAAP):
  Operating cash flow                           $[X]M
  (-) Capital expenditures                     ($[X]M)
  = Free Cash Flow                              $[X]M
  FCF Margin                                    [X]%
```

---

## Phase 4: Financial Ratio Analysis

**Goal:** Extract meaning from the statements through comparative ratios.

```
LIQUIDITY
  Current Ratio = Current Assets / Current Liabilities = [X]x
  Quick Ratio = (Cash + Receivables) / Current Liabilities = [X]x
  Cash Ratio = Cash / Current Liabilities = [X]x

PROFITABILITY
  Gross Margin = Gross Profit / Revenue = [X]%
  Operating Margin = EBIT / Revenue = [X]%
  Net Margin = Net Income / Revenue = [X]%
  Return on Assets = Net Income / Total Assets = [X]%
  Return on Equity = Net Income / Total Equity = [X]%

LEVERAGE
  Debt/Equity = Total Debt / Total Equity = [X]x
  Debt/EBITDA = Total Debt / EBITDA = [X]x
  Interest Coverage = EBIT / Interest Expense = [X]x
  Net Debt/EBITDA = (Total Debt - Cash) / EBITDA = [X]x

EFFICIENCY
  Days Sales Outstanding = (AR / Revenue) × 365 = [X] days
  Days Inventory Outstanding = (Inventory / COGS) × 365 = [X] days
  Days Payable Outstanding = (AP / COGS) × 365 = [X] days
  Cash Conversion Cycle = DSO + DIO - DPO = [X] days
  Asset Turnover = Revenue / Total Assets = [X]x

DUPONT DECOMPOSITION
  ROE = Net Margin × Asset Turnover × Equity Multiplier
      = [X]%     × [X]x           × [X]x
      = [X]%
```

---

## Phase 5: Quality-of-Earnings Red Flags

**Goal:** Identify areas where the financial statements may not reflect economic reality.

```
| Red Flag | What to Check | Implication |
|----------|--------------|-------------|
| Revenue growing faster than cash collections | AR growing faster than revenue | Aggressive revenue recognition |
| Capitalizing operating costs | Capex growing while opex flat | Inflating earnings |
| Inventory build-up | DIO increasing | Demand softening or obsolescence |
| Declining cash conversion | OCF/Net Income < 1x | Earnings quality deteriorating |
| Frequent one-time charges | "Non-recurring" items every quarter | Recurring costs disguised |
| Related party transactions | Revenue from affiliates | Potential channel stuffing |
| Audit opinion changes | Qualified opinion or going concern | Serious issues |
| Deferred revenue declining | For subscription businesses | Future revenue at risk |
```

---

## Quality Gates

- [ ] All three statements prepared (P&L, BS, CFS)
- [ ] Balance sheet balances (A = L + E)
- [ ] Cash flow reconciles to change in cash balance
- [ ] Common-size analysis completed for trend identification
- [ ] Key ratios calculated and compared to prior period and industry
- [ ] Quality-of-earnings red flags checked
- [ ] Non-GAAP reconciliation provided if adjusted metrics used

## Hard Constraints

- **NEVER** present adjusted/non-GAAP metrics without showing the reconciliation from GAAP
- **NEVER** ignore the cash flow statement — it's the hardest to manipulate
- **ALWAYS** verify the balance sheet balances before presenting
- **ALWAYS** compare to prior period — a single period in isolation is meaningless

## Common Pitfalls

1. **Ignoring working capital changes** — net income ≠ cash flow; the bridge matters
2. **Confusing EBIT and EBITDA** — D&A is real economic cost for capital-intensive businesses
3. **Missing off-balance-sheet items** — operating leases (pre-ASC 842), SPEs, guarantees
4. **Revenue without cash** — if DSO is growing, the revenue may not be collectible
5. **Comparing companies on different bases** — GAAP vs IFRS, fiscal year timing

## Related Skills

- `/accounting` — record the transactions that produce these statements
- `/audit` — verify the statements are materially correct
- `/fpa` — analyze variances and build forecasts from the statements
- `/credit` — use statements for credit analysis
- `/data-entry` — extract financial data from source documents
