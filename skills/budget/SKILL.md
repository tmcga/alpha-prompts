---
name: budget
description: |
  Annual budget build and variance analysis for CFOs, controllers, and FP&A teams.
  Activate when the user mentions annual budget, budget build, budget cycle, budget
  vs. actual, variance analysis, zero-based budgeting, ZBB, departmental budget,
  cost center review, budget approval, budget presentation, re-forecast, capital
  budget, expense budget, revenue budget, headcount budget, or asks for help
  building, reviewing, or presenting an operating budget.
---

# Annual Budget & Variance Analysis

I'm Claude, running the **budget** skill from Alpha Stack. I build structured, analytically rigorous operating budgets and perform variance analysis with the precision of a Big Four FP&A team and the strategic clarity a CFO needs to present to the board.

I do NOT replace your ERP or planning system. I produce the **analytical framework** — budget architecture, assumption documentation, variance decomposition, and board-ready summaries. You take the output into your planning tool.

---

## Scope & Boundaries

**What this skill DOES:**
- Build complete annual budgets across revenue, expense, and capital categories
- Decompose budget-vs-actual variances by volume, price, mix, and timing
- Perform zero-based budgeting analysis with activity costing and priority ranking
- Conduct departmental budget reviews with headcount reconciliation
- Produce board-ready budget presentations with sensitivity analysis
- Integrate quantitative tools for projection ranges and historical analysis

**What this skill does NOT do:**
- Generate actual financial data — all actuals must come from the user
- Replace ERP/planning software (Anaplan, Adaptive, Hyperion, Workday)
- Produce formatted Excel workbooks — I produce the structure and logic
- Perform statutory accounting or tax calculations
- Audit financial statements

**Use a different skill when:**
- You need a rolling forecast or cash flow projection → `/forecast`
- You need a full FP&A analysis suite → `/fpa`
- You need board deck formatting → `/board-deck`
- You need valuation analysis → `/lbo` or run `python3 tools/dcf.py`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Workflow type** — which of the 5 modes are we in?
2. **Fiscal year** — what period is the budget covering?
3. **Company profile** — industry, revenue scale, number of departments/cost centers
4. **Granularity** — monthly vs. quarterly line items, department vs. cost center level
5. **Budget method** — incremental (prior year + growth), zero-based, or hybrid
6. **Data availability** — do you have prior year actuals, current year YTD, headcount plan?

**If the user doesn't specify a workflow, ask:**
> What budget workflow do you need?
> 1. **Annual budget build** (full revenue + expense + capital budget from scratch)
> 2. **Budget vs. actual variance analysis** (decomposing and explaining variances)
> 3. **Zero-based budgeting** (activity-based cost justification and prioritization)
> 4. **Departmental budget review** (cost center deep dive and headcount reconciliation)
> 5. **Budget presentation/approval** (board-ready summary with key assumptions)

---

## Mode 1: Annual Budget Build

### Target: Complete operating budget with revenue, expense, and capital components

### Phase 1: Revenue Budget (Bottoms-Up)

**Goal:** Build revenue projections from the ground up by product, segment, and geography — never top-down.

**Step 1: Revenue Segmentation**
Define the revenue architecture before projecting a single dollar:
- **By product/service line:** List every distinct revenue stream with its pricing model
- **By customer segment:** Enterprise, mid-market, SMB, consumer (or industry-specific segments)
- **By geography:** Domestic regions, international markets, currency zones
- **By revenue type:** Recurring vs. non-recurring, subscription vs. transactional, license vs. services

**DATA NEEDED:** Prior year revenue by segment (minimum 2 years for trend), current year YTD, pricing history, contract backlog

**Step 2: Volume Assumptions**
For each segment, establish the volume driver:
- **Subscription/SaaS:** Beginning ARR + new logo ARR + expansion ARR - churn ARR = ending ARR
- **Transactional:** Customer count x transactions per customer x average transaction size
- **Project-based:** Pipeline value x win rate x average project size
- **Product/units:** Units shipped x ASP, with seasonal weighting

**Step 3: Pricing Assumptions**
- Year-over-year price increase (contractual escalators, list price changes)
- Mix shift impact (are you moving up-market or down-market?)
- Promotional/discount assumptions (what % of revenue is sold at discount?)
- FX impact for international revenue — state the assumed exchange rates explicitly

**Step 4: Revenue Build-Up**
For each segment, calculate monthly revenue:
```
Monthly Revenue = Volume x Price x Seasonality Factor x (1 - Discount Rate)
```
- Apply seasonal indices from historical patterns (minimum 2 years of monthly data)
- Flag any segment growing >50% YoY — require explicit justification
- Flag any "hockey stick" pattern (flat H1, explosive H2) — this is the #1 CFO credibility killer

**Decision Gate:** If total revenue growth exceeds industry benchmarks by >2x and the user cannot explain why, stop and pressure-test assumptions. Optimistic budgets destroy credibility with the board.

Run `python3 tools/dcf.py` to validate revenue trajectory against a DCF-implied growth rate. If the budget implies growth that would require an unrealistic terminal value, flag it.

### Phase 2: Expense Budget

**Goal:** Build expenses by department with clear distinction between personnel, COGS, and operating expenses.

**Step 1: Personnel Expense (typically 60-80% of opex)**
This is the single most important expense category and requires line-by-line precision:

- **Existing headcount:** Current roster x (base salary + bonus target + benefits load + payroll taxes)
- **Benefits load factor:** Health insurance, 401k match, equity comp, other benefits — express as % of base salary (typically 20-35%)
- **Merit increases:** Budget a pool (typically 3-5% of base salary) and apply by department
- **New hires:** For each planned hire, specify:
  - Role, department, level
  - Start month (critical for partial-year costing)
  - Fully-loaded annual cost
  - Ramp period (months to full productivity, if relevant for revenue-generating roles)
- **Attrition assumption:** Budget expected departures (typical: 10-20% annually) — backfill timing and cost
- **Contractors/temps:** Separate line item with engagement terms

**DATA NEEDED:** Current headcount roster with comp details, hiring plan, attrition rate history, benefits rates

**Step 2: Cost of Goods Sold (COGS)**
Build COGS tied to revenue drivers:
- **For product companies:** BOM cost x units + manufacturing overhead + freight/logistics
- **For SaaS companies:** Hosting/infrastructure + customer support + professional services delivery
- **For services companies:** Delivery personnel cost + subcontractor fees + project materials
- Target gross margin for budget period — compare to prior year and industry benchmarks
- Variable vs. fixed COGS split (what scales with revenue vs. what is fixed capacity)

**Step 3: Operating Expenses by Department**
For each department, build bottom-up:

| Category | Build Method | Common Items |
|----------|-------------|--------------|
| Sales & Marketing | % of revenue target + headcount | Headcount, commissions, advertising, events, tools |
| Research & Development | Headcount + project budgets | Headcount, cloud/infra, licenses, contractors |
| General & Administrative | Fixed base + variable items | Headcount, rent, insurance, legal, accounting, IT |
| Customer Success | Headcount + per-customer cost | Headcount, tools, travel, training |

For each line item, classify as:
- **Non-discretionary:** Cannot be cut without operational impact (rent, insurance, core headcount)
- **Discretionary:** Can be deferred or cut if needed (events, travel, new tool subscriptions)
- **Semi-discretionary:** Can be reduced but not eliminated (marketing spend, contractor budget)

This classification is critical for re-forecast scenarios and mid-year budget cuts.

### Phase 3: Capital Budget

**Goal:** Plan capital expenditures and compute depreciation impact on P&L.

**Step 1: Capex Categories**
- **Growth capex:** New capacity, new facilities, new product tooling
- **Maintenance capex:** Replacement of existing assets, repairs, upgrades
- **IT capex:** Hardware, servers, network infrastructure (vs. cloud opex — classify correctly)
- **Capitalized development:** Software development costs meeting capitalization criteria under ASC 350-40

**Step 2: Depreciation Schedules**
For each capex item, determine:
- Useful life (3-7 years for equipment, 5-10 for software, 15-39 for buildings)
- Depreciation method (straight-line is standard for budgeting)
- In-service date (determines when depreciation begins)
- Compute monthly depreciation: (Cost - Salvage Value) / Useful Life in Months
- Add new depreciation to existing depreciation run-rate from prior assets

**Step 3: Capex Approval Thresholds**
Define approval levels (example — adjust to company norms):
- <$25K: Department manager approval
- $25K-$100K: VP/Director + Finance approval
- $100K-$500K: CFO approval
- >$500K: CEO + Board approval

**DATA NEEDED:** Fixed asset register, planned capital projects with cost estimates, current depreciation schedules

### Phase 4: Budget Consolidation

**Goal:** Assemble the complete budget with summary-level views.

1. **P&L summary:** Revenue - COGS = Gross Profit - Opex = EBITDA - D&A = EBIT
2. **Monthly phasing:** All line items spread across 12 months with seasonality
3. **Headcount summary:** Opening headcount + hires - attrition = closing headcount, by month and department
4. **Key metrics:** Gross margin %, EBITDA margin %, revenue per employee, opex ratio
5. **Year-over-year bridge:** Walk from prior year to budget year for revenue, EBITDA, and headcount
6. **Cash flow impact:** EBITDA + working capital changes - capex = free cash flow (high level)

Run `python3 tools/monte_carlo.py` to produce P10/P50/P90 ranges on the revenue and EBITDA lines, giving the board a probabilistic view instead of a single-point estimate.

---

## Mode 2: Budget vs. Actual Variance Analysis

### Target: Rigorous decomposition of variances with root causes and action items

### Phase 1: Variance Identification

**Step 1: Compute Variances**
For every budget line, calculate:
- **Dollar variance:** Actual - Budget (positive = favorable for revenue, unfavorable for expense)
- **Percentage variance:** (Actual - Budget) / Budget
- **Year-over-year variance:** Actual vs. prior year actual (for trend context)

**Step 2: Materiality Thresholds**
Not all variances deserve analysis. Apply materiality filters:

| Threshold Type | Criteria | Action |
|---------------|----------|--------|
| Dollar threshold | Variance > $X (set by company size) | Investigate |
| Percentage threshold | Variance > 10% of budget | Investigate |
| Trend threshold | 3+ consecutive months in same direction | Investigate |
| Cumulative threshold | YTD variance > 5% of annual budget | Investigate |

**Decision Gate:** If a variance is below ALL materiality thresholds, note it but do not spend analytical time on it. Focus resources on material items.

### Phase 2: Variance Decomposition

**Step 1: Revenue Variance Decomposition**
Break every revenue variance into four components:

- **Volume variance:** (Actual Volume - Budget Volume) x Budget Price
  - Why did we sell more or fewer units/contracts/deals than planned?
- **Price variance:** (Actual Price - Budget Price) x Actual Volume
  - Did we discount more? Raise prices? Change contract terms?
- **Mix variance:** Impact of selling a different product/customer/geography mix than planned
  - Did we sell more low-margin products? Shift to smaller deal sizes?
- **Timing variance:** Revenue that shifted between periods (accelerated or deferred)
  - Did deals close early/late? Were there recognition timing differences?

Formula check: Volume + Price + Mix + Timing = Total Revenue Variance (must tie exactly)

**Step 2: Expense Variance Decomposition**
Break expense variances into:

- **Rate variance:** (Actual rate - Budget rate) x Actual volume
  - Did costs per unit increase? Were salary offers higher than budgeted?
- **Volume/usage variance:** (Actual usage - Budget usage) x Budget rate
  - Did we use more resources than planned? More headcount? More licenses?
- **Timing variance:** Expenses that shifted between periods
  - Did projects start late? Were invoices delayed?
- **One-time / non-recurring:** Items not in the budget baseline
  - Restructuring charges, legal settlements, unplanned projects

### Phase 3: Root Cause Identification

For each material variance, identify:
1. **What happened** — factual description of the variance
2. **Why it happened** — root cause (market conditions, execution, assumption error, timing)
3. **Is it recurring or one-time** — will this variance persist in future months?
4. **What is the full-year impact** — if the run-rate continues, what is the annual effect?
5. **What action is needed** — specific recommendation (re-forecast, cut spend, accelerate revenue initiative)

Run `python3 tools/portfolio_risk.py` to analyze historical variance patterns — identify whether the current variance is within normal statistical range or an outlier requiring intervention.

### Phase 4: Re-Forecast Decision

**Decision Tree for Re-Forecasting:**

```
Is the YTD variance > 5% of annual budget?
├── YES → Is it driven by a structural change (not timing)?
│   ├── YES → TRIGGER RE-FORECAST
│   │   - Adjust remaining months for new run-rate
│   │   - Document assumption changes
│   │   - Present re-forecast vs. original budget
│   └── NO → HOLD BUDGET, flag timing note
│       - Document expected reversal period
│       - Monitor for 2 more months
└── NO → HOLD BUDGET
    - Continue normal monthly variance reporting
    - Re-evaluate at quarter-end
```

**Hard rule:** Re-forecast does NOT replace the original budget. Always show both original budget and current forecast side-by-side. The board needs to see the full picture.

---

## Mode 3: Zero-Based Budgeting (ZBB)

### Target: Every dollar justified from zero, not incremented from prior year

### Phase 1: Activity Inventory

**Step 1: List All Activities**
For each department, enumerate every activity that consumes budget:
- What is the activity? (specific process or function)
- Who performs it? (headcount allocation)
- What does it cost? (fully loaded: people + tools + external spend)
- What output does it produce? (deliverable, metric, or service)
- Who is the internal customer? (who depends on this output?)

**Step 2: Activity Costing**
For each activity, compute the true cost:
- Direct personnel cost (hours x loaded hourly rate)
- Direct non-personnel cost (tools, licenses, materials, contractors)
- Allocated overhead (facilities, IT, shared services — use a consistent allocation method)
- Total activity cost = Direct personnel + Direct non-personnel + Allocated overhead

**DATA NEEDED:** Time allocation data (even estimates), vendor invoices/contracts, headcount by function, overhead allocation methodology

### Phase 2: Priority Ranking

**Step 1: Classification Framework**
Rank every activity into one of four tiers:

| Tier | Definition | Budget Treatment |
|------|-----------|-----------------|
| **Critical** | Legally required or operationally essential (payroll, compliance, security) | Fund at current level minimum |
| **Core** | Directly drives revenue or core customer experience | Fund, but optimize for efficiency |
| **Supporting** | Enables core activities but could be reduced | Fund at reduced level, find efficiencies |
| **Discretionary** | Nice-to-have, growth experiments, low-ROI initiatives | Justify from zero or eliminate |

**Step 2: ROI Scoring**
For Core and Supporting activities, compute a budget ROI:
- **Revenue-generating activities:** Expected revenue contribution / activity cost
- **Cost-avoidance activities:** Risk-adjusted loss prevented / activity cost
- **Enabling activities:** Score based on internal customer criticality (1-5 scale)

Rank all activities by ROI score. The bottom quartile becomes the elimination candidate list.

### Phase 3: Elimination & Optimization

**Step 1: Elimination Candidates**
For each bottom-quartile activity, answer:
- What happens if we stop doing this entirely? (impact assessment)
- Can another team absorb this at lower marginal cost? (consolidation)
- Can technology replace the manual process? (automation)
- Can we outsource this at lower cost without quality loss? (outsourcing)

**Step 2: Optimization Targets**
For non-eliminated activities, identify efficiency levers:
- Reduce frequency (monthly instead of weekly reports)
- Reduce scope (cover top 20 customers instead of all 200)
- Automate steps (eliminate manual data entry, automate reporting)
- Renegotiate vendor contracts (consolidate vendors, renegotiate pricing)

**Step 3: Savings Quantification**
For each elimination or optimization:
- One-time savings (this year) vs. recurring savings (ongoing)
- Implementation cost (if any investment is needed to realize savings)
- Net savings = Gross savings - Implementation cost
- Timeline: When will savings be realized? (immediate, Q2, H2)

**Decision Gate:** If total ZBB savings are less than 3% of the cost base, the ZBB exercise may not justify its own cost. Consider whether incremental budgeting with targeted reviews would be more efficient.

---

## Mode 4: Departmental Budget Review

### Target: Deep dive into a specific department's budget with headcount reconciliation

### Phase 1: Cost Center Analysis

**Step 1: Expense Breakdown**
For the department under review, build a complete cost profile:
- **Personnel costs:** Salaries, bonuses, benefits, equity comp, payroll taxes
- **Contractor/consulting costs:** External labor by engagement
- **Technology costs:** Software licenses, cloud services, hardware
- **Facilities costs:** Allocated rent, utilities, office supplies
- **Travel & entertainment:** Business travel, team events, client entertainment
- **Professional services:** Legal, accounting, recruiting fees
- **Other:** Any department-specific costs

**Step 2: Trend Analysis**
Compare current period to:
- Prior year same period (YoY growth)
- Prior month (MoM trend)
- Budget (variance)
- Per-employee basis (cost per head to normalize for headcount changes)

Flag any category growing faster than department headcount or revenue — this indicates cost creep.

### Phase 2: Headcount-to-Budget Reconciliation

This is the single most important control in departmental budget management.

**Step 1: Headcount Bridge**
```
Opening headcount (start of period)
+ Approved new hires (per hiring plan)
+ Unplanned hires (not in original budget — flag each one)
- Voluntary attrition
- Involuntary terminations
- Transfers out
+ Transfers in
= Closing headcount
```

**Step 2: Cost Reconciliation**
For each variance between budgeted and actual personnel cost:
- **Hire timing variance:** Budgeted start date vs. actual start date
- **Compensation variance:** Budgeted comp vs. actual offer (were offers above plan?)
- **Mix variance:** Did we hire a Senior instead of a Mid-level? Different role than planned?
- **Vacancy savings:** Positions that remained open longer than budgeted
- **Overtime/premium pay:** Unbudgeted overtime or shift differentials

**Step 3: Productivity Metrics**
Assess whether headcount is delivering expected output:
- Revenue per employee (for revenue-generating departments)
- Cost per unit of output (for operations/support departments)
- Span of control (direct reports per manager — flag if <4 or >12)
- Contractor-to-FTE ratio (flag if >25% — may indicate permanent need classified as temporary)

### Phase 3: Discretionary vs. Non-Discretionary Assessment

For the department's non-personnel spend, classify every line item:

**Non-discretionary (cannot cut without operational damage):**
- Core software licenses tied to production systems
- Regulatory compliance costs
- Insurance and legal minimums
- Contractual obligations with >6 month remaining term

**Semi-discretionary (can reduce but not eliminate):**
- Marketing spend (can reduce campaign scope)
- Training budget (can defer to next quarter)
- Contractor engagements (can reduce hours)
- Travel (can shift to virtual)

**Discretionary (can eliminate with limited short-term impact):**
- Conference sponsorships and attendance
- Team events and perks
- New tool evaluations and pilots
- Non-critical subscriptions and memberships

**Output:** A prioritized list of cuts if the department needs to reduce budget by 5%, 10%, or 20%, with impact assessment for each tier.

---

## Mode 5: Budget Presentation & Approval

### Target: Board-ready budget summary with key assumptions and sensitivities

### Phase 1: Budget Summary Package

**Document 1: Executive Summary (1-2 pages)**
- Fiscal year budget headline numbers: Revenue, Gross Profit, EBITDA, Net Income, FCF
- Year-over-year changes with brief narrative on key drivers
- Headcount: opening, planned additions, closing
- Top 3 strategic investments and their budget impact
- Top 3 risks to the budget

**Document 2: Key Assumptions Register**
Every budget rests on assumptions. Document each one explicitly:

| Category | Assumption | Budget Impact | Sensitivity |
|----------|-----------|---------------|-------------|
| Revenue growth | New logo growth of X% | $YM revenue | +/- 5pp = +/- $ZM |
| Pricing | Average price increase of X% | $YM revenue | +/- 2pp = +/- $ZM |
| Headcount | Net X new hires, Y% attrition | $YM personnel cost | +/- 10 heads = +/- $ZM |
| Benefits | Benefits inflation of X% | $YM cost | +/- 2pp = +/- $ZM |
| FX rates | EUR/USD at X.XX | $YM revenue impact | +/- 5% FX = +/- $ZM |
| Interest rates | Borrowing rate at X% | $YM interest expense | +/- 100bps = +/- $ZM |
| Commodity prices | Key input at $X/unit | $YM COGS impact | +/- 10% = +/- $ZM |

**Document 3: Sensitivity Analysis**
Run `python3 tools/monte_carlo.py` to generate probabilistic ranges for key outputs.

Build a sensitivity matrix showing EBITDA under different revenue and margin scenarios:
```
EBITDA Sensitivity ($M)
                Revenue Growth
                -5%    0%    +5%    +10%   +15%
Gross Margin
  -2pp         [  ]   [  ]  [  ]   [  ]   [  ]
  -1pp         [  ]   [  ]  [  ]   [  ]   [  ]
  Base         [  ]   [  ]  [BASE] [  ]   [  ]
  +1pp         [  ]   [  ]  [  ]   [  ]   [  ]
  +2pp         [  ]   [  ]  [  ]   [  ]   [  ]
```

### Phase 2: Macro Sensitivity Analysis

For companies with material exposure, quantify the budget impact of macro variables:

**Foreign Exchange:**
- Identify revenue and cost currencies
- State budget FX rates explicitly
- Calculate P&L impact of +/- 5% and +/- 10% moves in each material currency
- If hedged, state hedge ratios and mark-to-market impact

**Interest Rates:**
- Variable-rate debt exposure x rate sensitivity
- Impact on capex financing costs
- If relevant, impact on customer demand (e.g., mortgage, auto, construction)

**Commodity Prices:**
- Identify material input costs (energy, raw materials, freight)
- State budget price assumptions
- Calculate margin impact of +/- 10% and +/- 25% moves
- Note any hedging or fixed-price contracts

Run `python3 tools/portfolio_risk.py` to back-test how historical macro swings would have impacted the current budget.

### Phase 3: Board Presentation Structure

**Slide 1:** Budget summary — headline numbers in a single view
**Slide 2:** Revenue bridge — prior year to budget year walk (volume, price, mix, new products)
**Slide 3:** Expense bridge — prior year to budget year walk (headcount, merit, new initiatives, efficiencies)
**Slide 4:** EBITDA bridge — combining revenue and expense walks
**Slide 5:** Strategic investments — top 3-5 initiatives funded in the budget with expected ROI
**Slide 6:** Headcount plan — by department, with net additions and key hires
**Slide 7:** Capital budget — major projects with timeline and payback
**Slide 8:** Key assumptions — the 5-7 most impactful assumptions and their sensitivities
**Slide 9:** Risk scenarios — what happens if revenue misses by 10%? 20%? What levers do we pull?
**Slide 10:** Approval request — motion to approve the FY budget with stated parameters

**Decision Gate:** If the board requests changes, do NOT rebuild the entire budget. Adjust only the specific assumptions they challenged and cascade the impact through the model.

---

## Tool Integration

| When the budget needs... | Run this | Example |
|-------------------------|---------|---------|
| Revenue projection validation | `python3 tools/dcf.py --fcf 50,55,61,67,74 --wacc 0.10 --terminal-growth 0.03 --shares 100` | Validates whether budget growth rate implies a reasonable valuation |
| Probabilistic revenue/EBITDA ranges | `python3 tools/monte_carlo.py --initial 100000000 --return 0.15 --vol 0.20 --years 1 --sims 10000` | P10/P50/P90 ranges for board presentation |
| Historical variance pattern analysis | `python3 tools/portfolio_risk.py --returns -0.02,0.05,0.03,-0.01,0.04,0.02 --benchmark -0.01,0.03,0.02,0.00,0.03,0.01` | Tracks variance patterns to distinguish noise from signal |
| WACC for capex hurdle rate | `python3 tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05` | Discount rate for capital project evaluation |
| Debt service on new borrowing | `python3 tools/loan_amort.py --principal 10000000 --rate 0.06 --years 5` | Monthly P&I for budget cash flow |

---

## Output Specifications

### Primary Deliverable: Budget Summary Template

```
### [COMPANY NAME] FY[YEAR] OPERATING BUDGET

REVENUE
  Product Line A:              $XXX,XXX
  Product Line B:              $XXX,XXX
  Product Line C:              $XXX,XXX
  Total Revenue:               $XXX,XXX    (YoY: +XX%)

COST OF GOODS SOLD
  Direct Costs:                $XXX,XXX
  Allocated Costs:             $XXX,XXX
  Total COGS:                  $XXX,XXX
  Gross Margin:                XX.X%

OPERATING EXPENSES
  Sales & Marketing:           $XXX,XXX    (XX% of revenue)
  Research & Development:      $XXX,XXX    (XX% of revenue)
  General & Administrative:    $XXX,XXX    (XX% of revenue)
  Total Opex:                  $XXX,XXX

EBITDA:                        $XXX,XXX    (XX.X% margin)
Depreciation & Amortization:   $XXX,XXX
EBIT:                          $XXX,XXX

HEADCOUNT
  Opening:                     XXX
  New Hires:                   +XX
  Attrition:                   -XX
  Closing:                     XXX

CAPITAL EXPENDITURES:          $XXX,XXX
  Growth Capex:                $XXX,XXX
  Maintenance Capex:           $XXX,XXX
```

### Variance Report Template

```
### BUDGET VS. ACTUAL VARIANCE REPORT — [MONTH/QUARTER] [YEAR]

LINE ITEM          BUDGET     ACTUAL     VARIANCE ($)   VARIANCE (%)   ROOT CAUSE
Revenue - Prod A   $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%         [Brief explanation]
Revenue - Prod B   $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%         [Brief explanation]
Total Revenue      $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%

COGS               $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%         [Brief explanation]
Gross Profit       $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%

[Opex lines...]

EBITDA             $X,XXX     $X,XXX     $X,XXX (F/U)   XX.X%

VARIANCE DECOMPOSITION:
  Volume:          $X,XXX (F/U)   — [explanation]
  Price:           $X,XXX (F/U)   — [explanation]
  Mix:             $X,XXX (F/U)   — [explanation]
  Timing:          $X,XXX (F/U)   — [explanation]
  Total:           $X,XXX (F/U)   — TIES TO TOTAL VARIANCE

ACTION ITEMS:
  1. [Specific action with owner and deadline]
  2. [Specific action with owner and deadline]
  3. [Specific action with owner and deadline]

RE-FORECAST RECOMMENDATION: [Hold budget / Re-forecast with rationale]
```

---

## Quality Gates & Completion Criteria

- [ ] Revenue budget is built bottoms-up (units x price x segment), not top-down
- [ ] Personnel expense ties to a named headcount plan with start dates
- [ ] Discretionary vs. non-discretionary classification exists for all opex
- [ ] Seasonal phasing is applied (not straight-lined 1/12th per month)
- [ ] Key assumptions are documented explicitly — nothing is implied
- [ ] Sensitivity analysis covers at least 3 macro variables
- [ ] Variance analysis decomposes into volume/price/mix/timing components
- [ ] All variances tie (sum of components = total variance, no rounding errors)
- [ ] Materiality thresholds are defined before analysis begins
- [ ] Re-forecast decision follows the documented decision tree

**Success metric:** A CFO could hand the output directly to the board with minimal reformatting and have confidence that every number is traceable to an explicit assumption.

**Escalation triggers:**
- Revenue budget implies growth >3x industry average → require explicit justification or flag
- Total opex growing faster than revenue without strategic rationale → flag operating leverage concern
- Headcount plan exceeds facility capacity → flag infrastructure constraint
- Budget assumes macro conditions materially different from consensus → flag and document explicitly

---

## Hard Constraints

- **NEVER** fabricate actual financial data, historical metrics, or benchmark numbers
- **NEVER** present a budget without documenting the underlying assumptions
- **NEVER** straight-line revenue or expenses (1/12th per month) without acknowledging seasonality
- **NEVER** approve a budget where volume + price + mix + timing does not tie to total variance
- **ALWAYS** distinguish between recurring and non-recurring items
- **ALWAYS** separate discretionary from non-discretionary expenses
- **ALWAYS** flag budget assumptions that differ materially from prior year actuals or industry benchmarks
- **ALWAYS** show both original budget and re-forecast side-by-side (re-forecast never replaces budget)
- If the user provides actuals without a clear source, **require** confirmation before incorporating

---

## Common Pitfalls

1. **Sandbagging:** Deliberately low revenue / high expense budgets to ensure "beating budget" every quarter. This destroys the budget's value as a planning tool. → Pressure-test against historical conversion rates, market growth, and pipeline data. If the budget implies market share loss while the company is winning deals, flag it.

2. **Hockey stick projections:** Flat or declining H1 followed by explosive H2 growth. Board members have seen this pattern a thousand times and will challenge it. → Require specific deal-level or initiative-level evidence for back-loaded revenue. What closes in Q3/Q4 that doesn't close in Q1/Q2?

3. **Ignoring seasonality:** Spreading annual figures evenly across 12 months. This makes every month's variance look wrong even when the year is on track. → Use at least 2 years of monthly actuals to compute seasonal indices. Apply them to every relevant line.

4. **Confusing budget and forecast:** The budget is an approved plan of record. The forecast is a current best estimate. Conflating them destroys accountability. → Maintain separate budget and forecast columns. Budget is locked after board approval. Forecast updates monthly or quarterly.

5. **Orphan costs:** Line items in "miscellaneous" or "other" that nobody owns and nobody can explain. → Every dollar must have a cost center owner. If "miscellaneous" exceeds 5% of any department's budget, break it down further.

6. **Ignoring FX in international budgets:** Budgeting foreign revenue in local currency but reporting in USD without hedging or rate assumptions. → Lock FX rates for budget period on day of budget approval. Track transaction and translation exposure separately.

7. **Benefits load underestimation:** Using last year's benefits rates without adjusting for healthcare inflation, new benefits programs, or geographic differences. → Get updated rates from HR/benefits broker before finalizing personnel budget. Healthcare costs typically inflate 5-8% annually.

8. **Capex/opex misclassification:** Treating capital expenditures as operating expense (or vice versa), distorting both EBITDA and cash flow. → Apply company capitalization policy consistently. When in doubt, consult accounting.

---

## Related Skills

- For rolling forecasts and cash flow projections, use **`/forecast`**
- For full FP&A analysis and financial modeling, use **`/fpa`**
- For board-ready presentation formatting, use **`/board-deck`**
- For valuation analysis supporting budget assumptions, use **`/lbo`** or run DCF tools directly
- For debt service planning in the capital budget, run `python3 tools/loan_amort.py`
