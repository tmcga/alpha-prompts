---
name: data-entry
description: |
  Financial data extraction, cleaning, normalization, and validation. Activate when the
  user mentions data entry, data extraction, data cleaning, normalize data, parse financial
  data, PDF extraction, table extraction, OCR, convert to spreadsheet, standardize format,
  data validation, reconcile data sources, financial data pipeline, or asks about converting
  unstructured financial information into structured, tool-ready formats.
---

# Financial Data Entry & Validation

I transform unstructured financial data into clean, structured, tool-ready formats. I'm the bridge between messy real-world inputs (PDFs, screenshots, earnings transcripts, bank statements) and the precise numerical inputs that Alpha Stack's computational tools require. Every extraction is validated against internal consistency checks before passing downstream.

---

## Scope & Boundaries

**What this skill DOES:**
- Extract financial data from unstructured text (earnings reports, filings, presentations)
- Normalize data into consistent formats (thousands, millions, percentages, decimals)
- Validate extracted data against internal consistency checks (BS balances, CF reconciles)
- Structure data as tool-ready inputs (CLI arguments, JSON, CSV)
- Cross-reference multiple sources to resolve discrepancies
- Build standardized data templates for recurring analysis
- Convert between units (annual ↔ quarterly, per-share ↔ aggregate, nominal ↔ real)

**What this skill does NOT do:**
- OCR images or scan physical documents (requires external tools)
- Access live databases or APIs (use `tools/fetch.py` for market data)
- Store data persistently (use `tools/state.py` for session persistence)

**Use a different skill when:**
- Recording journal entries → `/accounting`
- Analyzing the financial statements → `/financial-statements`
- Running calculations on the data → invoke the relevant tool directly
- Live market data → `tools/fetch.py`

---

## Pre-Flight Checks

1. **Data source:** What document or source contains the data?
2. **Target format:** What tool or analysis will consume this data?
3. **Time period:** What periods need to be captured?
4. **Currency and units:** USD, EUR? Thousands, millions, billions?
5. **Known issues:** Missing periods, restated numbers, different accounting standards?

---

## Phase 1: Data Extraction

**Goal:** Pull numbers from unstructured sources into a structured intermediate format.

### From Financial Statements
```
When extracting from a P&L, balance sheet, or cash flow statement:

1. Identify the unit convention (top of statement: "in thousands" / "in millions")
2. Identify the period(s) and whether fiscal year = calendar year
3. Extract line items into a standard table:

| Line Item | FY2023 | FY2024 | Source | Notes |
|-----------|--------|--------|--------|-------|
| Revenue | $[X]M | $[X]M | 10-K p.[X] | |
| COGS | $[X]M | $[X]M | 10-K p.[X] | |
| Gross Profit | $[X]M | $[X]M | Calculated | Revenue - COGS |
| ... | | | | |

4. Mark calculated fields vs extracted fields
5. Flag any items that required judgment (e.g., reclassifications)
```

### From Earnings Reports / Transcripts
```
Extract key metrics mentioned in earnings:
| Metric | Reported Value | Period | Context | Source Line |
|--------|---------------|--------|---------|-------------|
| Revenue | $[X]M | Q4 2024 | "Revenue was..." | Transcript p.[X] |
| EPS | $[X] | Q4 2024 | "Diluted EPS of..." | Press release |
| Guidance | $[X-Y]M | FY2025 | "We expect revenue..." | Transcript p.[X] |

Flag: GAAP vs non-GAAP (many earnings reports lead with adjusted metrics)
```

### From Rent Rolls / Loan Documents / Offering Memos
```
For real estate:
| Unit/Suite | SF | Tenant | Rent/SF | Annual Rent | Lease Start | Lease End |
|-----------|-----|--------|---------|-------------|-------------|-----------|
| [X] | [X] | [X] | $[X] | $[X] | [date] | [date] |

For credit:
| Tranche | Amount | Rate | Maturity | Amort | Covenants |
|---------|--------|------|----------|-------|-----------|
| [X] | $[X]M | [X]% | [date] | [X]yr | [details] |
```

---

## Phase 2: Data Normalization

**Goal:** Convert all data to a consistent format suitable for computation.

### Unit Standardization
```
Conversion rules applied:
| Source Format | Normalized Format | Rule |
|-------------|------------------|------|
| "$1,234,567" | 1234567 | Remove $, commas |
| "1.2B" | 1200000000 | Billions → raw number |
| "$45.2M" | 45200000 | Millions → raw number |
| "(123)" or "-123" | -123 | Accounting negatives |
| "12.5%" | 0.125 | Percentage → decimal |
| "3.2x" | 3.2 | Multiple → raw number |
| "Q4 FY24" | 2024-12-31 | Fiscal period → date |
| "LTM" | trailing 4 quarters | Sum prior 4 quarters |

All monetary values in: [USD / raw number / same unit as tool expects]
All rates in: [decimal, e.g., 0.065 for 6.5%]
All dates in: [YYYY-MM-DD]
```

### Derived Metrics
```
When source data is incomplete, calculate missing fields:

| Missing | Calculate From | Formula |
|---------|---------------|---------|
| EBITDA | Net income, D&A, interest, tax | NI + D&A + Interest + Tax |
| Free cash flow | Operating CF, capex | OCF - Capex |
| Net debt | Total debt, cash | Debt - Cash |
| EV | Market cap, net debt, preferred, minority | MC + ND + Pref + MI |
| Gross margin | Revenue, COGS | (Rev - COGS) / Rev |
| NWC | Current assets, current liabilities | CA - CL |
```

---

## Phase 3: Data Validation

**Goal:** Verify extracted data is internally consistent before passing to tools.

### Balance Sheet Checks
```
[ ] Assets = Liabilities + Equity (tolerance: $[X])
[ ] Current assets + non-current assets = total assets
[ ] Current liabilities + non-current liabilities = total liabilities
[ ] Retained earnings = prior RE + net income - dividends
[ ] Goodwill unchanged unless acquisition or impairment
```

### Income Statement Checks
```
[ ] Revenue - COGS = Gross profit (exact)
[ ] Gross profit - OpEx = Operating income (exact)
[ ] Tax rate = Tax provision / Pre-tax income (reasonable: 15-30%)
[ ] EPS = Net income / diluted shares (within rounding)
```

### Cash Flow Checks
```
[ ] Beginning cash + net change = ending cash (exact)
[ ] Operating CF starts from net income (indirect method)
[ ] D&A add-back matches P&L D&A
[ ] Capex in investing = change in gross PP&E + disposals
```

### Cross-Source Reconciliation
```
When data comes from multiple sources:
| Field | Source A | Source B | Match? | Resolution |
|-------|---------|---------|--------|-----------|
| Revenue | $[X]M (10-K) | $[X]M (press release) | [Y/N] | [Use 10-K as authoritative] |
| EBITDA | $[X]M (company) | $[X]M (analyst) | [Y/N] | [Different add-backs — document] |
```

---

## Phase 4: Tool-Ready Output

**Goal:** Format validated data as inputs for specific Alpha Stack tools.

### DCF Tool Input
```bash
python3 tools/dcf.py \
  --fcf [comma-separated projected FCFs] \
  --wacc [decimal] \
  --terminal-growth [decimal] \
  --net-debt [number] \
  --shares [number]
```

### LBO Tool Input
```bash
python3 tools/lbo.py \
  --ebitda [number] \
  --entry-multiple [number] \
  --exit-multiple [number] \
  --leverage [number] \
  --rate [decimal] \
  --growth [decimal] \
  --years [number]
```

### RE Debt Tool Input
```bash
python3 tools/re_debt.py \
  --noi [number] \
  --value [number] \
  --rate [decimal] \
  --amort [years] \
  --max-ltv [decimal] \
  --min-dscr [decimal]
```

### Portfolio Risk Tool Input
```bash
python3 tools/portfolio_risk.py \
  --returns [comma-separated decimal returns] \
  --risk-free [decimal]
```

---

## Phase 5: Data Templates

**Goal:** Provide reusable templates for common data collection tasks.

### Company Financial Summary Template
```
| Metric | FY-2 | FY-1 | LTM | FY+1E | FY+2E |
|--------|------|------|-----|-------|-------|
| Revenue | | | | | |
| Revenue growth | | | | | |
| Gross profit | | | | | |
| Gross margin | | | | | |
| EBITDA | | | | | |
| EBITDA margin | | | | | |
| Net income | | | | | |
| Capex | | | | | |
| Free cash flow | | | | | |
| Total debt | | | | | |
| Cash | | | | | |
| Net debt | | | | | |
| Shares outstanding | | | | | |
```

---

## Quality Gates

- [ ] Source documents identified and cited for every extracted number
- [ ] Units normalized (currency, millions/thousands, percentages as decimals)
- [ ] Balance sheet balances (A = L + E)
- [ ] Cash flow reconciles (beginning + change = ending)
- [ ] Cross-source discrepancies resolved and documented
- [ ] Tool-ready output formatted with correct argument names
- [ ] Calculated fields marked as derived (not source data)

## Hard Constraints

- **NEVER** fabricate data — if a number isn't in the source, say it's missing
- **NEVER** pass unvalidated data to computational tools
- **ALWAYS** cite the source document and page/section for every extracted number
- **ALWAYS** flag when using estimated or derived values vs. directly extracted values

## Common Pitfalls

1. **Unit mismatch** — mixing millions and thousands, or percentages and decimals
2. **Fiscal vs calendar year** — a company with June FY end reports FY2024 ending June 2024
3. **GAAP vs non-GAAP** — earnings reports often lead with adjusted numbers
4. **Stale data** — using TTM numbers that don't include the most recent quarter
5. **Rounding errors** — extracted numbers may not sum exactly due to rounding in source

## Related Skills

- `/accounting` — understand how the data was recorded
- `/financial-statements` — analyze the statements containing the data
- `/audit` — verify data accuracy
- `/fpa` — use the cleaned data for financial planning
