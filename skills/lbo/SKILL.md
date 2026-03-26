---
name: lbo
description: |
  End-to-end leveraged buyout model builder for PE sponsors, lenders, and advisors.
  Activate when the user mentions LBO, leveraged buyout, buyout model, sponsor returns,
  PE returns, debt sizing, sources and uses, cash sweep, debt schedule, management equity,
  PIK toggle, MOIC, IRR attribution, exit analysis, dividend recap, or asks for help
  building or reviewing a buyout model for an acquisition, take-private, or recap.
---

# LBO Model Builder

I'm Claude, running the **lbo** skill from Alpha Stack. I build complete leveraged buyout models with the rigor of a PE associate preparing for investment committee. I construct every layer — sources and uses, operating model, debt schedule with cash sweep mechanics, and returns analysis with full attribution.

I do NOT produce Excel files. I produce the **analytical architecture** — every assumption, formula, and output in structured form that you can implement in your spreadsheet or verify against an existing model. Every number is transparent and auditable.

---

## Scope & Boundaries

**What this skill DOES:**
- Build complete LBO models from transaction assumptions through returns output
- Size and structure multi-tranche debt packages (revolver, TLA, TLB, second lien, mezzanine, HoldCo PIK)
- Construct sources and uses with balancing logic
- Build operating models from revenue drivers through unlevered free cash flow
- Model debt schedules with mandatory amortization, cash sweep, and optional prepayment
- Calculate sponsor returns (MOIC, IRR) with full attribution (leverage, multiple expansion, EBITDA growth)
- Run sensitivity and scenario analysis across key assumptions
- Model management equity programs (options, rollover, sweet equity)
- Analyze credit metrics over the hold period (leverage, coverage, FCF yield)

**What this skill does NOT do:**
- Produce Excel or Google Sheets files — I output structured tables and formulas
- Fabricate operating assumptions — all revenue, margin, and growth inputs must come from the user or be explicitly flagged as placeholders
- Replace legal review of credit agreements or intercreditor terms
- Model complex tax structures (Section 338(h)(10), tax receivable agreements) without explicit user inputs
- Provide market-clearing pricing or syndication advice — use `/credit` for that

**Use a different skill when:**
- You need a standalone DCF valuation → run `python3 tools/dcf.py`
- You need a full investment memo → `/investment-memo`
- You need credit agreement analysis or covenant modeling → `/credit`
- You need a sell-side marketing deck → `/sell-side`
- You need VC-style returns with dilution modeling → `/vc`

---

## Pre-Flight Checks

Before building anything, I need to establish the full parameter set. Missing inputs here cascade into garbage outputs downstream.

### 1. Transaction Parameters

| Parameter | Required? | Default if not provided |
|-----------|-----------|------------------------|
| Target company name and description | Yes | — |
| Enterprise value or entry EV/EBITDA multiple | Yes | — |
| LTM EBITDA (and adjusted EBITDA if different) | Yes | — |
| LTM revenue | Yes | — |
| Existing debt to be refinanced | Yes (can be $0) | — |
| Transaction fees (advisory, financing, legal) | No | 2.5% of EV advisory + 2.0% of debt financing |
| Minimum cash on balance sheet at close | No | $0 |

### 2. Operating Assumptions

| Parameter | Required? | Default if not provided |
|-----------|-----------|------------------------|
| Revenue growth rate(s) by year | Yes | — |
| EBITDA margin(s) by year or margin expansion trajectory | Yes | — |
| D&A as % of revenue or dollar amount | No | 3-5% of revenue |
| Capex as % of revenue (maintenance vs. growth) | Yes | — |
| Net working capital as % of revenue and direction of change | No | Held constant as % of revenue |
| Tax rate (cash tax rate, not GAAP) | No | 25% |
| Stock-based compensation (cash vs. non-cash) | No | $0 |

### 3. Capital Structure Assumptions

| Parameter | Required? | Default if not provided |
|-----------|-----------|------------------------|
| Target leverage (total and senior secured) | Yes | — |
| Debt tranches and sizing | Yes (or let me size) | — |
| Interest rates by tranche (fixed or SOFR + spread) | No | Current market benchmarks |
| Amortization schedule by tranche | No | Standard: 0% revolver, 1% TLB, 5-10% TLA |
| Cash sweep percentage and step-downs | No | 50% ECF sweep with leverage step-downs |
| Revolver sizing and expected usage | No | 1.0-1.5x NWC swing |
| Financing fees and OID by tranche | No | 2% fees, 99.0 OID on TLB |

### 4. Exit Assumptions

| Parameter | Required? | Default if not provided |
|-----------|-----------|------------------------|
| Hold period (years) | No | 5 years |
| Exit EV/EBITDA multiple | Yes | — |
| Exit method (sale, IPO, dividend recap, continuation) | No | Sale to strategic or sponsor |

**If the user provides only EBITDA, entry multiple, and leverage, ask:**
> I can build a model with those three inputs, but the output will be rough. To build an IC-quality model, I also need:
> 1. Revenue and revenue growth assumptions (so I can model the full P&L)
> 2. Capex and working capital assumptions (so FCF and cash sweep are accurate)
> 3. Debt structure preferences (tranches, pricing, amortization)
> 4. Exit multiple assumption
>
> Which of these can you provide? I'll use reasonable defaults for the rest and flag them.

---

## Phase 1: Sources & Uses Construction

**Goal:** Build a balanced sources and uses table that ties perfectly and establishes the equity check.

### Step 1.1: Calculate Uses of Funds

Build the uses side first — it determines how much total capital is needed.

1. **Enterprise value:** Entry EBITDA x Entry EV/EBITDA multiple
   - If the user provides total enterprise value directly, back into the implied multiple
   - Sanity check: is the implied multiple reasonable for the sector? (Flag if >15x for non-software, >25x for software)

2. **Existing debt refinanced:** Total existing debt that must be repaid at close
   - Include any make-whole premiums or prepayment penalties
   - If the target has a revolver, assume it is repaid and a new one is put in place

3. **Transaction fees:**
   - Advisory fees: typically 1.0-2.5% of EV (higher for smaller deals)
   - Financing fees: typically 2.0-3.0% of total debt raised
   - Legal, accounting, diligence: typically 0.5-1.0% of EV
   - If the user does not specify, use: advisory 2.0% of EV + financing 2.5% of committed debt + other 0.5% of EV

4. **OID (Original Issue Discount):** Difference between par and issue price on term loans
   - TLB typically issued at 99.0-99.5 (i.e., 50-100bps OID)
   - OID is a use of funds (you raise less than par) and amortizes into interest expense over the life

5. **Cash to balance sheet:** Minimum operating cash required at close
   - If the target is seasonal, size this to the peak cash need

6. **Total uses** = EV + Debt refinanced + Fees + OID + Cash to B/S

### Step 1.2: Size the Debt

Debt sizing follows a hierarchy — work through each constraint and take the binding one.

1. **Leverage-based sizing:**
   - Senior secured debt = Target senior leverage x Adjusted EBITDA
   - Total debt = Target total leverage x Adjusted EBITDA
   - Typical ranges by credit quality:
     - Strong/stable cash flow: 4.0-5.0x senior, 5.0-6.5x total
     - Moderate cyclicality: 3.0-4.0x senior, 4.0-5.5x total
     - Cyclical/volatile: 2.0-3.0x senior, 3.0-4.0x total

2. **Coverage-based sizing:**
   - Minimum interest coverage: EBITDA / Cash interest >= 2.0x (floor)
   - Fixed charge coverage: (EBITDA - Capex) / (Interest + Mandatory amort) >= 1.0x
   - If coverage constraint is tighter than leverage constraint, reduce debt accordingly

3. **Debt service capacity:**
   - Year 1 FCF must be positive after all mandatory debt service
   - Cumulative FCF over hold period should delever the business meaningfully

4. **Allocate debt across tranches (top of the capital structure down):**
   - Revolver: sized to working capital needs, typically undrawn at close
   - Term Loan A (if applicable): bank-held, shorter maturity (5yr), higher amortization (5-10%/yr)
   - Term Loan B: institutional, longer maturity (7yr), 1% annual amortization, SOFR + spread
   - Second lien / Mezzanine: fills the gap between senior debt capacity and total debt target
   - Subordinated / HoldCo PIK: if total leverage target exceeds secured capacity

**Decision Gate:** If total leverage exceeds 6.5x, flag this as aggressive and stress-test whether the business can service the debt through a downturn. If EBITDA must grow every year just to avoid covenant breach, the structure is too tight.

### Step 1.3: Calculate Equity Check

1. **Sponsor equity** = Total uses - Total debt - Any rollover equity - Any seller financing
2. **Equity as % of total capitalization** — should generally be 30-50% for a standard LBO
   - Below 25%: flag as highly leveraged, requires strong cash flow visibility
   - Above 55%: question whether an LBO structure makes sense (low leverage = low returns)
3. **Management rollover:** If management is rolling equity, specify the amount and whether it counts toward the sponsor's equity check

### Step 1.4: Balance and Verify

Run the balancing check:
- **Total sources MUST equal total uses to the penny**
- If they do not balance, adjust the equity check (equity is the plug)
- Display the completed table:

```
SOURCES                          USES
Revolving Credit Facility  $—M   Enterprise Value          $—M
Term Loan A               $—M   Refinance Existing Debt   $—M
Term Loan B               $—M   Advisory Fees             $—M
Second Lien Notes         $—M   Financing Fees            $—M
Mezzanine                 $—M   OID                       $—M
Rollover Equity           $—M   Cash to Balance Sheet     $—M
Sponsor Equity            $—M
─────────────────────────────   ─────────────────────────────
Total Sources             $—M   Total Uses                $—M
```

Run the tool to validate:
```bash
python3 tools/lbo.py \
  --ebitda 150 \
  --entry-multiple 10.0 \
  --exit-multiple 10.0 \
  --leverage 5.5 \
  --rate 0.065 \
  --growth 0.07 \
  --years 5 \
  --tax-rate 0.25 \
  --capex-pct 0.08 \
  --nwc-pct 0.05
```

---

## Phase 2: Operating Model Build

**Goal:** Project revenue, EBITDA, and unlevered free cash flow for each year of the hold period.

### Step 2.1: Revenue Build

Build revenue from the top down or bottom up depending on data availability.

**Top-down approach (when limited data):**
1. Start with LTM revenue
2. Apply year-over-year growth rates
3. If the user provides only a single growth rate, apply it uniformly but flag that year-by-year granularity improves the model
4. Sanity check: does terminal-year revenue imply a market share that is unreasonable?

**Bottom-up approach (when segment data available):**
1. Break revenue into segments (product lines, geographies, customer types)
2. For each segment: volume x price, or customers x ARPU, or units x ASP
3. Model organic growth separately from acquired growth
4. Cross-check: does the sum of segments match the top-down estimate?

### Step 2.2: EBITDA Bridge

Build from revenue to EBITDA explicitly:

1. **Revenue** (from Step 2.1)
2. **(-) COGS** = Revenue x (1 - Gross margin %)
   - If gross margin is expanding, model the trajectory explicitly
3. **= Gross Profit**
4. **(-) SG&A** = Fixed component + Variable component (as % of revenue)
   - Separate fixed vs. variable to understand operating leverage
5. **(-) Other operating expenses** (R&D, one-time items, etc.)
6. **= EBITDA**
7. **EBITDA margin** = EBITDA / Revenue — track year over year

**Decision Gate:** If EBITDA margins are assumed to expand by more than 300bps over the hold period, require the user to specify which cost lines are driving the improvement. Unjustified margin expansion is the most common source of LBO model error.

### Step 2.3: EBITDA to Unlevered Free Cash Flow

This is the critical bridge that feeds the debt schedule:

1. **EBITDA**
2. **(-) Cash taxes on unlevered income**
   - Tax rate x (EBITDA - D&A) — this is a simplification; a full model would compute taxable income after interest
   - For the debt schedule, we will compute after-tax using actual interest expense (see Phase 3)
3. **(+) D&A tax shield** — add back because we compute taxes on unlevered income
4. **(-) Capital expenditures** (maintenance + growth)
   - If the user distinguishes maintenance vs. growth capex, show both
   - Maintenance capex ~ D&A; growth capex is incremental
5. **(-) Change in net working capital**
   - NWC = (Current assets - Cash) - (Current liabilities - Current portion of debt)
   - If NWC as % of revenue is stable, delta NWC = NWC% x delta Revenue
   - Positive revenue growth with stable NWC% = cash outflow (use of cash)
6. **= Unlevered Free Cash Flow**

For the levered FCF (which drives the debt schedule), we further subtract:
7. **(-) Cash interest expense** (computed in the debt schedule)
8. **(-) Mandatory amortization** (computed in the debt schedule)
9. **(+/-) Tax shield from interest** (interest is tax-deductible)
10. **= Levered Free Cash Flow (available for optional prepayment / cash sweep)**

### Step 2.4: Summarize Operating Model

Display as a clean table:

```
($M)                    Year 0   Year 1   Year 2   Year 3   Year 4   Year 5
Revenue                  $—       $—       $—       $—       $—       $—
  Growth %                —%       —%       —%       —%       —%       —%
EBITDA                   $—       $—       $—       $—       $—       $—
  Margin %                —%       —%       —%       —%       —%       —%
(-) D&A                  ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
EBIT                     $—       $—       $—       $—       $—       $—
(-) Taxes @ —%           ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
NOPAT                    $—       $—       $—       $—       $—       $—
(+) D&A                  $—       $—       $—       $—       $—       $—
(-) Capex                ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
(-) Delta NWC            ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
= Unlevered FCF          $—       $—       $—       $—       $—       $—
  FCF Conversion %        —%       —%       —%       —%       —%       —%
```

FCF Conversion = Unlevered FCF / EBITDA. A healthy LBO target converts 60-80% of EBITDA to FCF. Below 50% indicates high capex or working capital intensity — flag this.

---

## Phase 3: Debt Schedule & Cash Sweep Mechanics

**Goal:** Model each debt tranche period by period, with mandatory amortization, cash interest, PIK interest (if applicable), and excess cash flow sweep.

### Step 3.1: Set Up Debt Tranches

For each tranche, establish the following at close:

| Attribute | Revolver | TLA | TLB | 2nd Lien | Mezz |
|-----------|----------|-----|-----|----------|------|
| Principal at close | $0 (undrawn) | $—M | $—M | $—M | $—M |
| Maturity | 5yr | 5yr | 7yr | 8yr | 8yr |
| Interest rate | SOFR+[X] | SOFR+[X] | SOFR+[X] | SOFR+[X] | [X]% fixed |
| Cash vs. PIK | Cash | Cash | Cash | Cash | Cash/PIK toggle |
| Mandatory amort | 0% | 5-10%/yr | 1%/yr | 0% (bullet) | 0% (bullet) |
| Prepayment priority | 1st | 2nd | 3rd | 4th | 5th |
| Call protection | None | None | Soft call 101 Yr1 | NC2, then par | NC3, then declining |

If SOFR-based, require a SOFR assumption (or forward curve). If the user does not specify:
- Use current SOFR + stated spread
- Run `python3 tools/credit_spread.py` to benchmark spreads if needed

### Step 3.2: Mandatory Amortization

For each year, compute scheduled principal payments:

1. **TLA amortization:** Original principal x amortization rate
   - Typically level annual payments: 5%, 5%, 10%, 10%, 70% (balloon)
   - Or equal quarterly installments summing to the annual rate
2. **TLB amortization:** Original principal x 1% per year, paid quarterly (0.25%/quarter)
   - Remainder due as bullet at maturity
3. **Second lien and mezzanine:** Typically bullet maturity, no scheduled amortization
4. **Total mandatory amortization** = Sum across all tranches

### Step 3.3: Interest Expense Calculation

For each tranche, each year:

1. **Beginning balance** = Prior year ending balance (or closing balance for Year 1)
2. **Cash interest** = Average balance x Cash interest rate
   - Average balance = (Beginning + Ending) / 2 — or use beginning balance for simplicity
   - If floating rate: apply the assumed SOFR + spread for that year
3. **PIK interest** (if applicable) = Beginning balance x PIK rate
   - PIK interest adds to principal — it compounds
   - Track PIK accrual separately from original principal
4. **Total interest expense** = Sum of cash interest across all tranches
5. **Revolver interest:** If the revolver is drawn, compute interest on drawn balance + commitment fee on undrawn
   - Commitment fee: typically 25-50bps on undrawn amount

### Step 3.4: Excess Cash Flow Sweep

The ECF sweep is the mechanism by which leveraged free cash flow is used to prepay debt. This is the most technically complex part of the debt schedule.

**Step 3.4.1: Calculate Excess Cash Flow**

The credit agreement definition of ECF typically starts with:

```
Excess Cash Flow = Net Income
  + Depreciation & Amortization
  + Other non-cash charges
  - Capital expenditures (net of financed capex)
  - Scheduled debt principal payments (mandatory amort already paid)
  - Increases in working capital (+ decreases)
  - Cash taxes paid (to extent not already deducted)
  - Permitted investments, acquisitions, and restricted payments made during the period
  - Capital expenditures in excess of budgeted amounts (if credit agreement permits exclusion)
```

Simplified: **ECF ~ Levered FCF after mandatory debt service**

For modeling purposes:
```
ECF = EBITDA - Cash Interest - Cash Taxes - Capex - Delta NWC - Mandatory Amortization
```

**Step 3.4.2: Apply Sweep Percentage**

Typical ECF sweep structure with leverage step-downs:

| Net Leverage | Sweep % |
|-------------|---------|
| > 4.5x | 75% |
| 3.5x - 4.5x | 50% |
| < 3.5x | 25% |
| < 2.5x | 0% |

1. Calculate net leverage at end of period: (Total debt - Cash) / EBITDA
2. Determine applicable sweep percentage from the grid
3. **ECF sweep amount** = ECF x Applicable sweep %
4. If ECF is negative, sweep amount is $0 (no clawback)

**Step 3.4.3: Apply Sweep to Debt Tranches (Waterfall)**

ECF sweep proceeds are applied in order of seniority (unless the credit agreement specifies otherwise):

1. First: reduce Revolver balance to $0
2. Second: prepay TLA
3. Third: prepay TLB (often at par, but check for soft call premium in Year 1)
4. Fourth: prepay Second Lien (subject to call protection — if in NC period, sweep proceeds accumulate as cash or skip)
5. Fifth: prepay Mezzanine (subject to call protection)

**Decision Gate:** If the model shows the business cannot fully sweep the most senior tranche within the hold period, the capital structure may be too aggressive. Flag this for the user and suggest reducing total leverage or extending the hold period.

### Step 3.5: Build the Debt Schedule Table

For each tranche, display:

```
TERM LOAN B ($M)       Year 0   Year 1   Year 2   Year 3   Year 4   Year 5
Beginning Balance       $—       $—       $—       $—       $—       $—
(-) Mandatory Amort     ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
(-) ECF Sweep           ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
(-) Optional Prepay     ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
(+) PIK Accrual         $—       $—       $—       $—       $—       $—
Ending Balance          $—       $—       $—       $—       $—       $—

Cash Interest Expense   $—       $—       $—       $—       $—       $—
PIK Interest Expense    $—       $—       $—       $—       $—       $—
Total Interest          $—       $—       $—       $—       $—       $—
```

Then produce a **consolidated debt summary**:

```
TOTAL DEBT ($M)        Year 0   Year 1   Year 2   Year 3   Year 4   Year 5
Revolver                $—       $—       $—       $—       $—       $—
Term Loan A             $—       $—       $—       $—       $—       $—
Term Loan B             $—       $—       $—       $—       $—       $—
Second Lien             $—       $—       $—       $—       $—       $—
Mezzanine               $—       $—       $—       $—       $—       $—
─────────────────────────────────────────────────────────────────────────
Total Debt              $—       $—       $—       $—       $—       $—
(-) Cash                ($—)     ($—)     ($—)     ($—)     ($—)     ($—)
= Net Debt              $—       $—       $—       $—       $—       $—

Total Leverage          —x       —x       —x       —x       —x       —x
Senior Leverage         —x       —x       —x       —x       —x       —x
Interest Coverage       —x       —x       —x       —x       —x       —x
FCF / Debt Service      —x       —x       —x       —x       —x       —x
```

### Step 3.6: Credit Metric Tracking

Track these metrics each year and flag any that breach thresholds:

| Metric | Healthy Range | Warning | Critical |
|--------|--------------|---------|----------|
| Total leverage | < 5.0x | 5.0-6.5x | > 6.5x |
| Senior leverage | < 4.0x | 4.0-5.0x | > 5.0x |
| Interest coverage | > 2.5x | 2.0-2.5x | < 2.0x |
| Fixed charge coverage | > 1.2x | 1.0-1.2x | < 1.0x |
| FCF yield (FCF/Debt) | > 10% | 5-10% | < 5% |
| Debt/Total cap | < 65% | 65-75% | > 75% |

**If any metric enters "Critical" in any year of the hold period, halt and flag:** "This capital structure may not be sustainable. In Year [X], [metric] reaches [value], which would likely trigger lender concern or covenant breach. Consider reducing leverage by $[X]M or adjusting operating assumptions."

---

## Phase 4: Returns Analysis

**Goal:** Calculate sponsor returns (MOIC, IRR) and decompose them into value creation drivers.

### Step 4.1: Exit Enterprise Value

1. **Exit EBITDA** = Year [N] projected EBITDA (where N = hold period)
2. **Exit EV** = Exit EBITDA x Exit EV/EBITDA multiple
3. **Sanity checks:**
   - If exit multiple > entry multiple: justify with business improvement, sector re-rating, or platform scale
   - If exit multiple = entry multiple: this is the base case (no multiple arbitrage)
   - If exit multiple < entry multiple: flag as conservative but realistic for cyclical businesses or compressed sectors

### Step 4.2: Equity Value at Exit

Build the waterfall from EV to sponsor equity proceeds:

1. **Exit Enterprise Value**
2. **(-) Net debt at exit** = Total debt outstanding at exit - Cash at exit
3. **= Exit Equity Value**
4. **(-) Management equity / co-invest** (if applicable, their pro rata share)
5. **(-) Transaction fees on exit** (typically 1.0-2.0% of exit EV)
6. **= Sponsor Equity Proceeds**

### Step 4.3: MOIC Calculation

```
Gross MOIC = Sponsor Equity Proceeds / Sponsor Equity Invested
Net MOIC = (Sponsor Equity Proceeds - Carry - Fees) / LP Capital Invested
```

MOIC benchmarks by quality:
| MOIC | Assessment |
|------|-----------|
| < 1.5x | Below threshold for most funds |
| 1.5-2.0x | Acceptable, base case for many deals |
| 2.0-2.5x | Good — meets most fund return targets |
| 2.5-3.0x | Strong |
| > 3.0x | Excellent — top quartile outcome |

### Step 4.4: IRR Calculation

Build the cash flow stream:
- Year 0: (-) Sponsor equity invested (negative cash flow)
- Years 1 through N-1: Any interim distributions (dividend recaps, if modeled)
- Year N: (+) Sponsor equity proceeds at exit

IRR is the discount rate that sets the NPV of this stream to zero.

```bash
python3 tools/lbo.py \
  --ebitda 150 \
  --entry-multiple 10.0 \
  --exit-multiple 10.5 \
  --leverage 5.5 \
  --rate 0.065 \
  --growth 0.07 \
  --years 5
```

IRR benchmarks:
| IRR | Assessment |
|-----|-----------|
| < 15% | Below most fund hurdles |
| 15-20% | Meets hurdle, acceptable |
| 20-25% | Good — generates meaningful carry |
| 25-30% | Strong |
| > 30% | Excellent — but verify assumptions are realistic |

### Step 4.5: Returns Attribution

Decompose total value creation into three drivers. This is critical for IC presentations — it shows WHERE the return comes from.

**1. EBITDA Growth Contribution:**
```
Entry Equity Value (at exit EBITDA, entry multiple) =
  (Exit EBITDA x Entry Multiple) - Net Debt at Exit
EBITDA Growth Value = Entry Equity Value - Initial Equity Invested
```

**2. Multiple Expansion Contribution:**
```
Multiple Expansion Value =
  (Exit Multiple - Entry Multiple) x Exit EBITDA
```

**3. Leverage / Debt Paydown Contribution:**
```
Leverage Value = Net Debt at Entry - Net Debt at Exit
  (i.e., total debt repaid over the hold period from cash flow)
```

**Verification:** EBITDA Growth + Multiple Expansion + Leverage = Total Equity Value Created

Display attribution as both dollar amounts and percentage of total return:

```
RETURNS ATTRIBUTION          $M        % of Total
EBITDA Growth               $—M         —%
Multiple Expansion          $—M         —%
Debt Paydown (FCF)          $—M         —%
────────────────────────────────────────────
Total Value Created         $—M        100%

Entry Equity                $—M
Exit Equity                 $—M
Gross MOIC                  —x
Gross IRR                   —%
```

**Decision Gate:** If more than 50% of returns come from multiple expansion, flag this: "Over half of projected returns depend on exit multiple expansion from [X]x to [Y]x. This is a market-dependent assumption. Stress-test with flat and compressed multiples."

---

## Phase 5: Sensitivity & Scenario Analysis

**Goal:** Stress-test the model across the assumptions that matter most and present actionable output.

### Step 5.1: Two-Variable Sensitivity Tables

Build at minimum these three sensitivity matrices:

**Table 1: IRR sensitivity to Exit Multiple x EBITDA Growth**

```
IRR (%)          Exit Multiple
EBITDA CAGR    8.0x    9.0x   10.0x   10.5x   11.0x   12.0x
  3%           —%      —%      —%      —%      —%      —%
  5%           —%      —%      —%      —%      —%      —%
  7%           —%      —%      —%      —%      —%      —%
  9%           —%      —%      —%      —%      —%      —%
 11%           —%      —%      —%      —%      —%      —%
```

**Table 2: IRR sensitivity to Entry Multiple x Leverage**

```
IRR (%)          Entry Leverage (x EBITDA)
Entry EV/EBITDA  4.0x    4.5x    5.0x    5.5x    6.0x    6.5x
  8.0x           —%      —%      —%      —%      —%      —%
  9.0x           —%      —%      —%      —%      —%      —%
 10.0x           —%      —%      —%      —%      —%      —%
 11.0x           —%      —%      —%      —%      —%      —%
 12.0x           —%      —%      —%      —%      —%      —%
```

**Table 3: MOIC sensitivity to Exit Multiple x Hold Period**

```
MOIC (x)         Hold Period (Years)
Exit Multiple    3yr     4yr     5yr     6yr     7yr
  8.0x           —x      —x      —x      —x      —x
  9.0x           —x      —x      —x      —x      —x
 10.0x           —x      —x      —x      —x      —x
 11.0x           —x      —x      —x      —x      —x
 12.0x           —x      —x      —x      —x      —x
```

### Step 5.2: Scenario Analysis

Build three named scenarios with internally consistent assumptions:

**Base Case:**
- Revenue growth, margins, capex as per management projections
- Exit multiple = entry multiple (no expansion assumed)
- Standard cash sweep mechanics
- This is the "what we underwrite" case

**Upside Case:**
- Revenue growth +200bps above base
- Margin expansion from operational improvements (must be specified)
- Exit multiple = entry + 0.5-1.0x (justify with strategic premium or improved business quality)
- Additional value creation (bolt-on M&A, pricing optimization)

**Downside Case:**
- Revenue growth -300-500bps below base (or negative in severe case)
- Margin compression of 100-300bps
- Exit multiple = entry - 1.0-2.0x
- Working capital deterioration
- **Critical check:** Does the downside case still service debt? If not, what breaks first?

For each scenario, show: Entry equity, Exit equity, MOIC, IRR, and credit metrics at the trough.

### Step 5.3: Breakeven Analysis

Answer these questions explicitly:

1. **What exit multiple delivers a 1.0x MOIC?** (i.e., breakeven — get your money back)
2. **What exit multiple delivers a 2.0x MOIC?** (minimum acceptable return for most funds)
3. **What EBITDA decline can the company sustain and still service debt?** (DSCR = 1.0x floor)
4. **At what leverage level does the deal fail to meet the 20% IRR hurdle?**

---

## Phase 6: Exit Analysis

**Goal:** Model specific exit scenarios and their impact on returns.

### Step 6.1: Exit Route Comparison

| Exit Route | Typical Multiple Range | Timeline | Considerations |
|-----------|----------------------|----------|----------------|
| Sale to strategic | Highest (synergy premium) | 3-6 months | Regulatory risk, limited buyer universe |
| Sale to sponsor (SBO) | Market multiple | 3-6 months | Continuation fund, management rollover |
| IPO | Depends on public comps | 6-12 months | Lock-up period, public market risk |
| Dividend recap | N/A (partial exit) | 1-2 months | Debt market conditions, leverage capacity |
| Continuation fund | Negotiated | 2-3 months | GP conflict, LP alignment |

### Step 6.2: Dividend Recap Modeling

If the user wants to model a dividend recap during the hold period:

1. **Recap capacity:** Additional debt that can be raised while maintaining acceptable leverage
   - Max additional debt = (Target recap leverage x EBITDA at recap date) - Existing debt
2. **Recap proceeds to equity:** Additional debt raised - fees
3. **Impact on returns:**
   - MOIC may decrease slightly (higher leverage at exit reduces exit equity)
   - IRR typically increases significantly (earlier cash return on invested capital)
4. **Post-recap credit metrics:** Leverage, coverage must still be within acceptable ranges

### Step 6.3: Exit Year Flexibility

Model returns at each potential exit year (Year 3 through Year 7) to show the optimal exit window:

```
EXIT TIMING ANALYSIS    Year 3   Year 4   Year 5   Year 6   Year 7
Exit EBITDA             $—M      $—M      $—M      $—M      $—M
Exit EV (at —x)         $—M      $—M      $—M      $—M      $—M
Net Debt at Exit        $—M      $—M      $—M      $—M      $—M
Equity Proceeds         $—M      $—M      $—M      $—M      $—M
MOIC                    —x       —x       —x       —x       —x
IRR                     —%       —%       —%       —%       —%
```

Note: MOIC increases with time (more EBITDA growth, more debt paydown) but IRR decreases with time (time value of money). The optimal exit balances these two forces.

---

## Tool Integration

| When the model needs... | Run this | Example |
|------------------------|---------|---------|
| Full LBO returns calculation | `python3 tools/lbo.py` | `python3 tools/lbo.py --ebitda 150 --entry-multiple 10 --exit-multiple 10.5 --leverage 5.5 --rate 0.065 --growth 0.07 --years 5` |
| DCF cross-check on exit value | `python3 tools/dcf.py` | `python3 tools/dcf.py --fcf 80,90,100,110,120 --wacc 0.09 --terminal-growth 0.025 --shares 100` |
| WACC for DCF discount rate | `python3 tools/wacc.py` | `python3 tools/wacc.py --equity 600 --debt 900 --tax 0.25 --rf 0.04 --beta 1.3 --erp 0.055 --cost-of-debt 0.065` |
| Benchmark credit spreads | `python3 tools/credit_spread.py` | `python3 tools/credit_spread.py --spread 0.045 --recovery 0.40 --maturity 7` |
| Sensitivity scenario (low exit) | `python3 tools/lbo.py` with varied inputs | `python3 tools/lbo.py --ebitda 150 --entry-multiple 10 --exit-multiple 9 --leverage 5.5 --rate 0.065 --growth 0.05 --years 5` |
| Validate exit valuation vs. public comps | `python3 tools/dcf.py` | Compare DCF-implied EV to multiple-based exit EV |

### Running the Full Model

For a complete LBO with all outputs:

```bash
python3 tools/lbo.py \
  --ebitda 150 \
  --entry-multiple 10.0 \
  --exit-multiple 10.5 \
  --leverage 5.5 \
  --rate 0.065 \
  --growth 0.07 \
  --years 5 \
  --tax-rate 0.25 \
  --capex-pct 0.04 \
  --nwc-pct 0.08 \
  --da-pct 0.10
```

### Cross-Checking with WACC

After building the LBO, validate the implied cost of equity:

```bash
python3 tools/wacc.py \
  --equity 600 \
  --debt 825 \
  --tax 0.25 \
  --rf 0.04 \
  --beta 1.3 \
  --erp 0.055 \
  --cost-of-debt 0.065
```

The implied IRR from the LBO should exceed the WACC-implied cost of equity, otherwise the deal does not create value.

---

## Output Specifications

### Primary Deliverable: Complete LBO Model

The final output must include all six components in order:

1. **Transaction Summary:** One-paragraph description of the deal, entry valuation, capital structure, and key thesis points
2. **Sources & Uses Table:** Balanced, with every line item labeled
3. **Operating Model:** Revenue through UFCF, Year 0 through exit year
4. **Debt Schedule:** By tranche, with consolidated summary and credit metrics
5. **Returns Analysis:** MOIC, IRR, full attribution table
6. **Sensitivity Tables:** At minimum the three standard matrices (IRR x exit multiple x growth, IRR x entry multiple x leverage, MOIC x exit multiple x hold period)

### Supporting Artifacts:

- **Assumption summary:** Every input assumption in a single table with source (user-provided vs. default)
- **Credit metric dashboard:** Leverage, coverage, and FCF yield tracked annually
- **Breakeven analysis:** Exit multiple for 1.0x and 2.0x MOIC, EBITDA decline for debt service failure
- **Key risk flags:** Any warnings generated during the build process

---

## Quality Gates & Completion Criteria

- [ ] Sources and uses balance to the penny
- [ ] Operating model flows correctly from revenue to UFCF (no broken links)
- [ ] Debt schedule beginning balances match prior year ending balances
- [ ] Total interest expense ties between the debt schedule and the P&L
- [ ] ECF sweep is applied in correct waterfall priority
- [ ] No debt tranche has a negative balance in any year
- [ ] MOIC and IRR are consistent (higher MOIC with longer hold = lower IRR)
- [ ] Returns attribution sums to total equity value created
- [ ] Credit metrics are tracked and flagged against thresholds
- [ ] Sensitivity tables are internally consistent (monotonic where expected)
- [ ] All assumptions are explicitly stated — no hidden inputs
- [ ] Exit equity = Exit EV - Net debt at exit (verified)

**Success metric:** A PE associate should be able to take this output and build a working Excel model in under 2 hours without needing to make any structural decisions — every formula and flow is specified.

**Escalation triggers:**
- Returns depend primarily on multiple expansion → warn and stress-test with flat/compressed multiples
- Leverage exceeds 6.5x at close → require explicit user confirmation and stress-test debt service
- FCF conversion below 50% → flag that the business may not be an ideal LBO candidate
- Any year shows negative levered FCF → flag liquidity risk and check revolver capacity
- EBITDA margins assumed to expand >300bps without specified drivers → require justification

---

## Hard Constraints

- **NEVER** fabricate operating assumptions — if the user has not provided revenue growth, margins, or capex, ask for them or flag defaults prominently
- **NEVER** assume multiple expansion in the base case unless the user explicitly requests it
- **NEVER** present returns without attribution — MOIC and IRR alone are insufficient; always show WHERE the return comes from
- **NEVER** ignore cash sweep mechanics — they are the primary debt reduction mechanism and materially impact returns
- **NEVER** allow sources and uses to be unbalanced — equity is always the plug
- **ALWAYS** track credit metrics annually and flag when they enter warning/critical zones
- **ALWAYS** show at least three scenarios (base, upside, downside)
- **ALWAYS** include sensitivity analysis — a single-point return estimate is not a model, it is a guess
- **ALWAYS** distinguish between cash interest and PIK interest in the debt schedule
- **ALWAYS** verify that the tax shield from interest deductibility is correctly reflected
- If leverage exceeds 7.0x total, **refuse to build** without explicit user acknowledgment: "This leverage level exceeds typical market capacity. Confirm you want me to proceed, and I will flag this throughout the model."

---

## Common Pitfalls

1. **Confusing entry multiple with exit multiple in the base case:** Many junior models accidentally assume multiple expansion as the default. The disciplined base case assumes exit multiple = entry multiple. Multiple expansion is an upside driver, not a base assumption. → Always set exit = entry unless explicitly told otherwise.

2. **Ignoring the circularity between interest expense and cash available for debt paydown:** Interest depends on debt balance, which depends on cash sweep, which depends on cash after interest. This is a circular reference. → Solve iteratively: compute interest on beginning balance, then sweep, then check. For most models, using beginning-of-period balances avoids the circularity with minimal error.

3. **Forgetting OID is a use of funds:** If a $500M TLB is issued at 99.0, you only receive $495M in cash but owe $500M. The $5M OID must appear in uses. → Always include OID as a separate uses line item.

4. **Treating D&A as capex (or vice versa):** D&A is an accounting charge on past capex. Current capex may differ significantly from D&A, especially for growing businesses. → Model capex independently from D&A. Use D&A only for tax calculations.

5. **Applying the cash sweep to the wrong tranches:** The ECF sweep follows the prepayment waterfall specified in the credit agreement, not necessarily seniority. Some agreements sweep TLB pro rata with TLA; others sweep TLA first. → Confirm waterfall priority before building the schedule.

6. **Overstating FCF by ignoring working capital:** Revenue growth requires working capital investment. A business growing 10% with 15% NWC intensity consumes 1.5% of revenue in incremental NWC annually. → Always model delta NWC explicitly, especially for high-growth or seasonal businesses.

7. **Not stress-testing the downside for debt serviceability:** An LBO that returns 25% IRR in the base case but cannot service debt in a 20% EBITDA decline is not a good investment — it is a leveraged bet. → Always run a downside scenario and verify debt service coverage remains above 1.0x.

8. **Double-counting the tax shield:** If you compute taxes on EBIT (after D&A) and then separately add back a "tax shield from interest," you may be double-counting. → Use one consistent method: either compute taxes on EBT (after interest) in the P&L, or compute on EBIT and add back the interest tax shield separately. Never both.

9. **Ignoring management equity dilution:** If management receives options or sweet equity, the sponsor's effective ownership at exit is less than their entry ownership. A 20% management pool on a 2.5x MOIC deal means the sponsor realizes closer to 2.0x on their equity. → Always account for management equity in the exit waterfall.

10. **Presenting MOIC without IRR (or vice versa):** A 3.0x MOIC over 10 years is a ~12% IRR — below most hurdle rates. A 1.8x MOIC over 3 years is a ~22% IRR — excellent. Both metrics are required for a complete picture. → Always present both, and flag when MOIC looks attractive but IRR is below hurdle (long hold) or IRR looks attractive but MOIC is thin (short hold, high leverage).

---

## Related Skills

- For credit agreement analysis and covenant modeling, use **`/credit`**
- For DCF-based valuation (to cross-check exit value), run **`python3 tools/dcf.py`** or use **`/lbo`**
- For the investment memo that accompanies the LBO model, use **`/investment-memo`**
- For sell-side marketing of the deal, use **`/sell-side`**
- For a pitch deck to present the deal, use **`/pitch-deck`** (Mode 2: Deal Marketing)
- For restructuring analysis if the deal goes wrong, use **`/restructuring`**
