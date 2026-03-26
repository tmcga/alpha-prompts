---
name: forecast
description: |
  Rolling forecasts, scenario planning, and cash flow forecasting for CFOs, treasurers,
  and FP&A teams. Activate when the user mentions rolling forecast, cash flow forecast,
  13-week cash flow, liquidity forecast, scenario planning, stress test, base/bull/bear,
  Monte Carlo simulation, revenue forecast, demand forecast, working capital forecast,
  DSO/DPO/DIO modeling, forecast accuracy, MAPE, forecast vs. actual, re-forecast,
  covenant compliance, liquidity runway, or asks for help projecting future financial
  performance or cash positions.
---

# Rolling Forecasts, Scenario Planning & Cash Flow Forecasting

I'm Claude, running the **forecast** skill from Alpha Stack. I build structured financial forecasts with the methodological rigor of a top-tier FP&A team — driver-based models, probabilistic scenarios, and cash flow projections that treasurers and CFOs can rely on for decision-making.

I do NOT replace your planning system. I produce the **analytical framework** — forecasting methodology, driver assumptions, scenario trees, and formatted outputs. You take the logic into your planning tool.

---

## Scope & Boundaries

**What this skill DOES:**
- Build rolling forecasts at 13-week, quarterly, and annual horizons
- Construct direct and indirect cash flow forecasts with liquidity runway analysis
- Design base/bull/bear scenarios with Monte Carlo simulation
- Forecast revenue using pipeline, cohort, bottoms-up, and tops-down methods
- Model working capital dynamics (DSO, DPO, DIO) with seasonal patterns
- Track and improve forecast accuracy using MAPE, bias, and other metrics

**What this skill does NOT do:**
- Generate actual financial data — all actuals and inputs must come from the user
- Replace treasury management systems or planning software
- Produce formatted Excel workbooks — I produce the structure, formulas, and logic
- Perform statutory accounting or tax projections
- Make investment decisions — I provide the analytical basis, you make the call

**Use a different skill when:**
- You need an annual budget build → `/budget`
- You need a full FP&A suite → `/fpa`
- You need LBO modeling with leverage scenarios → `/lbo`
- You need a DCF valuation → run `python3 tools/dcf.py`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Workflow type** — which of the 5 modes are we in?
2. **Forecast horizon** — 13 weeks, quarterly, annual, multi-year?
3. **Company profile** — industry, revenue model, cash cycle characteristics
4. **Data availability** — historical periods available, granularity of data
5. **Purpose** — operational planning, board reporting, lender covenant, liquidity management?
6. **Update cadence** — weekly, monthly, quarterly?

**If the user doesn't specify a workflow, ask:**
> What forecasting workflow do you need?
> 1. **Rolling forecast** (13-week, quarterly, or annual with driver-based projections)
> 2. **Cash flow forecasting** (direct method, indirect method, or 13-week cash model)
> 3. **Scenario planning** (base/bull/bear with Monte Carlo and stress testing)
> 4. **Revenue forecasting** (pipeline, cohort, bottoms-up, or tops-down method)
> 5. **Working capital forecasting** (DSO/DPO/DIO modeling with seasonal patterns)

---

## Mode 1: Rolling Forecast

### Target: Continuously updated forecast replacing static annual budgets

### Phase 1: Forecast Architecture

**Step 1: Determine the Rolling Window**
Choose the appropriate horizon based on business needs:

| Horizon | Best For | Update Cadence | Driver Granularity |
|---------|----------|---------------|-------------------|
| **13-week** | Cash management, operational planning | Weekly | Transaction-level |
| **Quarterly (4-6 quarters out)** | Board reporting, resource allocation | Monthly | Account-level |
| **Annual (12-18 months out)** | Strategic planning, guidance | Monthly or quarterly | Category-level |

**Decision Gate:** If the user wants a 13-week forecast for board reporting or a 12-month forecast for cash management, redirect them to the appropriate horizon. Mismatched horizon and purpose is the most common forecasting error.

**Step 2: Identify Key Drivers**
A driver-based forecast projects 5-10 key business drivers and lets the financials cascade from them. This is fundamentally different from line-item forecasting.

For each P&L line, identify the underlying driver:

| Financial Line | Driver Example (SaaS) | Driver Example (Manufacturing) | Driver Example (Services) |
|---------------|----------------------|-------------------------------|--------------------------|
| Revenue | ARR, new logos, expansion rate, churn | Units shipped x ASP | Billable hours x rate x utilization |
| COGS | Hosting cost per user, support headcount | Raw material cost x units + labor | Delivery headcount x loaded cost |
| Sales & Marketing | Pipeline coverage ratio, CAC, quota-carrying reps | Channel mix, promotion spend per unit | BD headcount, win rate, proposal volume |
| R&D | Engineering headcount, contractor spend | Project budgets, prototype costs | Method development hours |
| G&A | Headcount, facility cost per sqft | Headcount, compliance costs | Headcount, insurance, rent |

**DATA NEEDED:** 12+ months of historical actuals by line item, driver values for the same period, current pipeline/backlog/order data

**Step 3: Build Driver Relationships**
For each driver, establish the statistical relationship to the financial line:
- **Linear:** Revenue = Units x Price (direct multiplication)
- **Step function:** Need 1 additional support rep per 50 new customers
- **Lagged:** Marketing spend in month N drives leads in month N+1 and revenue in month N+3
- **Seasonal:** Apply monthly seasonal indices derived from 2+ years of history
- **Trend:** Apply a trend growth rate on top of seasonal patterns

Run `python3 tools/dcf.py` to validate that the forecast's implied growth trajectory produces a reasonable terminal value — a sanity check on whether the forecast's growth assumptions are internally consistent.

### Phase 2: Forecast Build

**Step 1: Actuals + Forecast Integration**
The rolling forecast always shows:
- **Closed months:** Actual results (locked, not editable)
- **Current month:** Actual-to-date + forecast for remainder
- **Future months:** Pure forecast based on drivers

```
Rolling Forecast Layout (Quarterly, 6 quarters out):
Q1 (Actual) | Q2 (Actual) | Q3 (Act+Fcast) | Q4 (Forecast) | Q1+1 (Fcast) | Q2+1 (Fcast)
```

**Step 2: Trend Extrapolation with Judgment**
For each driver:
1. Calculate the trailing 3-month and 6-month trend
2. Compare to the same period last year (seasonality adjustment)
3. Apply known future changes (new product launch, price increase, contract renewal)
4. Adjust for leading indicators (pipeline, bookings, order backlog, web traffic)

**Hard rule:** Never blindly extrapolate a trend without checking for:
- Capacity constraints (can the business physically deliver 2x volume?)
- Market saturation (is the addressable market large enough to support the growth?)
- Seasonality (is the recent trend seasonal or structural?)
- One-time effects (did a single large deal inflate the trend?)

**Step 3: Leading Indicator Integration**
Incorporate forward-looking data that precedes financial results:

| Leading Indicator | What It Predicts | Typical Lead Time |
|------------------|-----------------|-------------------|
| Sales pipeline value | Revenue | 1-3 quarters |
| Website traffic / demo requests | New customer acquisition | 1-2 months |
| Customer health scores | Churn / renewal rates | 3-6 months |
| Job postings (macro) | Economic activity / demand | 3-6 months |
| Purchasing manager index (PMI) | Manufacturing demand | 1-3 months |
| Consumer confidence index | Consumer spending | 1-2 quarters |
| Backlog / order book | Revenue delivery | Varies by fulfillment cycle |

**Decision Gate:** If leading indicators and trend extrapolation point in opposite directions, flag this divergence explicitly. Do NOT average them — present both signals and let the forecast owner decide which to weight.

### Phase 3: Forecast Accuracy Tracking

**Step 1: Accuracy Metrics**
After each period closes, compute:

- **MAPE (Mean Absolute Percentage Error):**
  `MAPE = (1/n) x SUM(|Actual - Forecast| / |Actual|) x 100`
  - Good: <10% for revenue, <15% for expenses
  - Acceptable: 10-20% for revenue, 15-25% for expenses
  - Poor: >20% for revenue, >25% for expenses

- **Bias (Mean Percentage Error):**
  `Bias = (1/n) x SUM((Actual - Forecast) / |Actual|) x 100`
  - Positive bias = consistently forecasting too low (conservative)
  - Negative bias = consistently forecasting too high (optimistic)
  - Acceptable range: -5% to +5%

- **Forecast Value Added (FVA):**
  Does the forecast beat a naive model (e.g., last year + growth, or trailing average)?
  `FVA = Naive Model Error - Forecast Error`
  - If FVA < 0, the forecast is adding negative value — a naive model would be better

**Step 2: Accuracy Decomposition**
When MAPE exceeds thresholds, diagnose the source:
- **Driver accuracy:** Was the driver forecast wrong? (e.g., we predicted 100 new customers, got 75)
- **Relationship accuracy:** Was the driver correct but the financial relationship wrong? (e.g., 100 customers but lower ACV)
- **Timing accuracy:** Was the total right but the phasing wrong? (e.g., right annual number, wrong quarterly split)
- **One-time items:** Were there unforecastable events? (e.g., legal settlement, M&A)

**Step 3: Continuous Improvement**
Maintain a forecast accuracy scorecard by line item and by forecaster:
- Track MAPE and bias over time (are we getting better or worse?)
- Identify systematic biases by department (sales always optimistic, engineering always conservative?)
- Adjust driver relationships based on actuals (update coefficients, recalibrate seasonality)

---

## Mode 2: Cash Flow Forecasting

### Target: Precise cash position forecasting for liquidity management and covenant compliance

### Phase 1: Method Selection

**Decision Tree — Which Cash Flow Method to Use:**

```
What is the primary purpose?
├── Weekly liquidity management / Will we run out of cash?
│   └── USE DIRECT METHOD (receipts & disbursements), 13-week horizon
├── Monthly/quarterly financial reporting & planning?
│   └── USE INDIRECT METHOD (net income adjustments), quarterly horizon
├── Covenant compliance testing?
│   └── USE BOTH — direct for near-term cash, indirect for covenant definitions
└── All of the above?
    └── BUILD BOTH — they should reconcile to the same ending cash balance
```

### Phase 2: Direct Method (13-Week Cash Flow)

**Goal:** Project cash receipts and disbursements at the transaction level for the next 13 weeks.

**Step 1: Cash Receipts Forecast**
For each week, project cash coming in:

- **Customer collections:**
  - Accounts receivable aging schedule: What is due in each week?
  - Historical collection rates by aging bucket (current, 30-day, 60-day, 90-day)
  - Adjustment for known disputes, credits, or write-offs
  - New billing forecast x expected collection timing
  - Formula: `Weekly Collections = (A/R by aging bucket) x (Collection rate for that bucket)`
- **Other receipts:**
  - Interest income
  - Tax refunds (if expected, with timing)
  - Insurance proceeds
  - Asset sales
  - Intercompany transfers

**Step 2: Cash Disbursements Forecast**
For each week, project cash going out:

- **Payroll:** Exact amounts on exact dates (semi-monthly or biweekly cycle)
- **Accounts payable:** A/P aging schedule with payment terms by vendor
- **Rent/lease payments:** Fixed amounts on fixed dates
- **Debt service:** Principal + interest payments per loan schedule
  - Run `python3 tools/loan_amort.py` for amortization schedules
- **Tax payments:** Estimated tax dates and amounts (quarterly federal/state)
- **Capital expenditures:** Planned payments with milestone timing
- **One-time payments:** Bonus payouts, legal settlements, M&A costs
- **Discretionary payments:** Vendor payments that can be accelerated or deferred

**Step 3: 13-Week Cash Flow Model**

```
13-WEEK CASH FLOW FORECAST

                        Week 1   Week 2   Week 3  ...  Week 13   TOTAL
OPENING CASH BALANCE    $X,XXX

RECEIPTS
  Customer Collections  $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Other Receipts        $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
TOTAL RECEIPTS          $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX

DISBURSEMENTS
  Payroll               $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Accounts Payable      $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Rent/Leases           $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Debt Service          $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Tax Payments          $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Capital Expenditures  $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
  Other Disbursements   $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
TOTAL DISBURSEMENTS     $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX

NET CASH FLOW           $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX
CLOSING CASH BALANCE    $X,XXX   $X,XXX   $X,XXX       $X,XXX   $X,XXX

REVOLVER DRAW/(PAYDOWN) $X,XXX   $X,XXX   $X,XXX       $X,XXX
AVAILABLE LIQUIDITY     $X,XXX   $X,XXX   $X,XXX       $X,XXX

MINIMUM CASH BALANCE    $X,XXX   ← Policy minimum
WEEKS OF RUNWAY         XX       ← At current burn rate
```

**Step 4: Liquidity Runway Calculation**
```
Liquidity Runway (weeks) = (Cash + Available Credit Facility) / Average Weekly Net Burn
```

Flag status:
- **Green:** >26 weeks of runway
- **Yellow:** 13-26 weeks of runway — begin contingency planning
- **Red:** <13 weeks of runway — immediate action required (draw revolver, defer payments, accelerate collections)

### Phase 3: Indirect Method

**Goal:** Project cash flow from operations starting with net income and adjusting for non-cash items and working capital changes.

**Step 1: Start with Net Income Forecast**
Use the P&L forecast from the rolling forecast model.

**Step 2: Non-Cash Adjustments**
Add back / subtract items that affect net income but not cash:
- (+) Depreciation and amortization
- (+) Stock-based compensation
- (+/-) Deferred revenue changes
- (+/-) Deferred tax changes
- (+/-) Unrealized gains/losses
- (+) Amortization of debt issuance costs

**Step 3: Working Capital Changes**
Project the change in each working capital account:
- (+/-) Accounts receivable (decrease = cash inflow)
- (+/-) Inventory (decrease = cash inflow)
- (+/-) Prepaid expenses (decrease = cash inflow)
- (+/-) Accounts payable (increase = cash inflow)
- (+/-) Accrued liabilities (increase = cash inflow)
- (+/-) Deferred revenue (increase = cash inflow)

See Mode 5 for detailed working capital forecasting methodology.

**Step 4: Investing and Financing Cash Flows**
- **Investing:** Capital expenditures, acquisitions, investment purchases/sales
- **Financing:** Debt issuance/repayment, equity issuance, dividends, share repurchases

### Phase 4: Covenant Compliance Testing

For companies with credit facilities, test the forecast against financial covenants:

| Common Covenant | Typical Threshold | How to Test |
|----------------|------------------|-------------|
| Leverage (Debt/EBITDA) | <3.0x - 5.0x | Forecast debt balance / trailing 12-month EBITDA |
| Interest Coverage (EBITDA/Interest) | >2.0x - 3.0x | Forecast EBITDA / forecast interest expense |
| Fixed Charge Coverage | >1.1x - 1.25x | (EBITDA - Capex - Taxes) / (Interest + Mandatory Principal) |
| Minimum Liquidity | >$XM | Forecast cash + available revolver |
| Maximum Capex | <$XM annual | Track cumulative capex against covenant cap |

**Decision Gate:** If any covenant is forecast to be breached within 2 quarters, immediately flag this as a critical finding. Provide:
1. Which covenant, what threshold, when breach occurs
2. How much headroom exists today
3. What operational changes could prevent the breach
4. Whether a covenant amendment or waiver should be pursued proactively

Run `python3 tools/loan_amort.py` to model debt service under different repayment scenarios and test covenant compliance under each.

---

## Mode 3: Scenario Planning

### Target: Structured base/bull/bear scenarios with probabilistic modeling

### Phase 1: Scenario Architecture

**Step 1: Define the Scenarios**
Every scenario set needs exactly three named cases:

| Scenario | Definition | Probability Weight | Purpose |
|----------|-----------|-------------------|---------|
| **Base** | Most likely outcome given current trends and known information | 50-60% | Primary planning basis |
| **Bull** | Upside case if key opportunities materialize | 15-25% | Capacity planning, investment triggers |
| **Bear** | Downside case if key risks materialize | 15-25% | Contingency planning, covenant testing |

**Hard rule:** The base case is NOT the budget. The base case is the current best estimate of what will actually happen. The budget is a plan of record approved by the board. They may differ.

**Step 2: Identify Scenario Drivers**
For each scenario, vary only the 3-5 drivers that matter most. Do NOT create scenarios by moving every line item — that is noise, not signal.

Common scenario drivers by business type:

| Business Type | Key Scenario Drivers |
|--------------|---------------------|
| **SaaS** | New logo win rate, NDR/churn rate, sales cycle length, hiring pace |
| **Manufacturing** | Unit volume, input costs, capacity utilization, FX rates |
| **Services** | Utilization rate, bill rate, headcount, project win rate |
| **Retail/Consumer** | Same-store sales growth, new store openings, traffic/conversion, basket size |
| **Financial Services** | AUM flows, interest rates, credit losses, trading volumes |

**Step 3: Quantify Driver Ranges**
For each driver, define the base/bull/bear values:

```
Driver: New Logo Win Rate
  Bear:  15% (recession, longer sales cycles, budget freezes)
  Base:  25% (continuation of current trends)
  Bull:  35% (market tailwind, new product launch, competitor exit)
  Source: Historical range was 18%-32% over past 8 quarters
```

**Decision Gate:** If the bull and bear cases are not at least 1.5 standard deviations from the base on the primary driver, the scenarios are too narrow to be useful. Widen them.

### Phase 2: Monte Carlo Simulation

**Goal:** Move beyond three discrete scenarios to a full probability distribution.

**Step 1: Define Simulation Parameters**
For each key driver, specify:
- Distribution type (normal, lognormal, triangular, uniform)
- Mean (base case value)
- Standard deviation or min/max (based on historical volatility)
- Correlation structure (are revenue growth and margin positively or negatively correlated?)

**Step 2: Run Simulation**
Run `python3 tools/monte_carlo.py` with appropriate parameters.

Example for revenue simulation:
```
python3 tools/monte_carlo.py --initial 100000000 --return 0.15 --vol 0.25 --years 3 --sims 10000
```

This produces percentile outcomes:
- **P10:** 10th percentile — "things go badly" (roughly aligns with bear)
- **P25:** 25th percentile — "below expectations"
- **P50:** 50th percentile — "most likely" (should align with base)
- **P75:** 75th percentile — "above expectations"
- **P90:** 90th percentile — "things go very well" (roughly aligns with bull)

**Step 3: Interpret Results**
The Monte Carlo output tells you:
- **Width of distribution:** How uncertain is the outcome? (wide = high uncertainty, narrow = high confidence)
- **Skewness:** Is the risk symmetric or is there more downside than upside?
- **Tail risk:** What is the P5 outcome? Can the business survive it?
- **Expected value:** The probability-weighted average — use this for resource planning

### Phase 3: Recession Stress Test

**Goal:** Test whether the business survives a severe downturn.

**Step 1: Define the Recession Scenario**
Use historical recessions as calibration, not imagination:
- Revenue decline: -10% to -30% (calibrate to 2008-2009 or 2020 for the specific industry)
- Customer churn increase: 1.5x to 2x normal rate
- New business pipeline: -30% to -50% conversion
- Payment cycle extension: DSO increases 10-20 days
- Credit facility: Assume revolver availability may be restricted

**Step 2: Model the Impact**
Walk through the P&L and cash flow under recession assumptions:
- Revenue decline → gross profit impact (COGS may not flex as fast if partially fixed)
- Delayed cost actions → operating leverage works in reverse
- Working capital deterioration → cash consumption accelerates
- Debt covenants → test all covenants under stress (this is where breaches happen)

**Step 3: Identify Response Levers**
For the recession scenario, document the playbook:
- **Immediate (Week 1-4):** Hiring freeze, discretionary spend freeze, accelerate collections
- **Short-term (Month 2-3):** Headcount reductions (which roles, what severance cost), vendor renegotiation, capex deferral
- **Medium-term (Month 4-6):** Facility consolidation, product line rationalization, strategic pivots
- Quantify the savings from each lever and the timeline to realize them
- Test whether the levers are sufficient to avoid covenant breach and cash-out

### Phase 4: Sensitivity Analysis

**Goal:** Show how outputs change when individual inputs change.

**Build Tornado Charts** showing the top 10 drivers ranked by impact on EBITDA:

```
EBITDA Sensitivity — Top 10 Drivers (Impact of +/- 1 Standard Deviation)

Revenue growth rate     ████████████████████  +/- $12M
Gross margin            ██████████████████    +/- $10M
Headcount additions     ████████████████      +/- $8M
Customer churn rate     ██████████████        +/- $7M
Average deal size       ████████████          +/- $6M
Sales cycle length      ██████████            +/- $5M
FX rates (EUR/USD)      ████████              +/- $4M
Benefits inflation      ██████                +/- $3M
Facility costs          ████                  +/- $2M
Interest rates          ███                   +/- $1.5M
```

This tells the CFO where to focus management attention: the top 3 drivers account for most of the variance.

---

## Mode 4: Revenue Forecasting

### Target: Best-method revenue forecast based on available data and business model

### Method Selection Decision Tree

```
What data do you have?
├── Active sales pipeline with deal-level data?
│   └── USE PIPELINE-BASED METHOD
│       Best for: B2B, enterprise sales, project-based businesses
├── Subscription data with cohort-level retention and expansion?
│   └── USE COHORT-BASED METHOD
│       Best for: SaaS, subscription, membership businesses
├── Granular unit/volume data with pricing?
│   └── USE BOTTOMS-UP METHOD
│       Best for: Manufacturing, retail, transactional businesses
├── Only market-level data (TAM, market share)?
│   └── USE TOPS-DOWN METHOD
│       Best for: Early-stage companies, new market entry, strategic planning
└── Multiple data sources available?
    └── USE MULTIPLE METHODS AND TRIANGULATE
        The intersection of 2-3 methods is more reliable than any single method
```

### Method 1: Pipeline-Based (Weighted Probability)

**Step 1: Stage-Weighted Pipeline**
For each deal in the pipeline:
```
Weighted Value = Deal Value x Stage Probability x Close Timing Probability
```

Standard stage probabilities (adjust to your historical conversion rates):

| Pipeline Stage | Typical Probability | Timing Confidence |
|---------------|-------------------|-------------------|
| Lead / MQL | 5-10% | Low (quarter uncertain) |
| Discovery / SQL | 15-25% | Low-Medium |
| Demo / Evaluation | 30-40% | Medium |
| Proposal / Negotiation | 50-70% | Medium-High |
| Verbal Commit | 80-90% | High |
| Contract Out | 90-95% | High |
| Closed Won | 100% | Certain |

**Critical check:** Compare stage probabilities to historical conversion rates. If the pipeline says 50% probability at proposal stage but historical data shows only 35% of proposals close, use the historical rate.

**Step 2: Pipeline Coverage Ratio**
```
Pipeline Coverage = Total Weighted Pipeline / Revenue Target
```
- Healthy: 3x-4x coverage (you need $3-4 in pipeline for every $1 of revenue target)
- Concerning: <2x coverage (insufficient pipeline to hit target — flag immediately)
- Excessive: >6x coverage (pipeline may be inflated with stale or unqualified deals)

**Step 3: Pipeline-to-Revenue Conversion Model**
```
Forecast Revenue = (Current pipeline x Weighted conversion) + (Expected new pipeline x Historical conversion) + (Committed/contracted revenue)
```

### Method 2: Cohort-Based (Retention x Expansion)

**Step 1: Define Cohorts**
Group customers by acquisition period (monthly or quarterly cohorts):
```
Cohort Revenue(t+1) = Cohort Revenue(t) x Retention Rate x (1 + Expansion Rate)
```

**Step 2: Retention Curve**
Build a retention curve from historical data:
- Month 1→2 retention: XX% (the biggest drop, especially for self-serve)
- Month 3→4 retention: XX% (stabilization point)
- Month 12→13 retention: XX% (annual renewal benchmark)
- Mature retention (24+ months): XX% (steady-state)

**Step 3: Expansion Revenue**
For retained customers, model expansion:
- Upsell (higher tier): XX% of retained customers upgrade
- Cross-sell (new product): XX% of retained customers add products
- Usage growth (consumption): XX% volume increase per customer
- Price escalators: XX% contractual price increase

**Step 4: New Cohort Acquisition**
Forecast new customer additions per period:
```
Total Revenue = Existing Cohort Revenue (with retention + expansion) + New Cohort Revenue
```

### Method 3: Bottoms-Up (Units x Price)

**Step 1: Volume Forecast**
For each product/segment:
- Historical volume trend (trailing 12 months)
- Seasonal adjustment factors
- Known demand changes (new customer onboarding, customer loss, market shifts)
- Capacity constraints (maximum producible/deliverable volume)

**Step 2: Price Forecast**
- Current price list with effective dates
- Planned price changes with implementation timing
- Historical discount rates by channel/segment
- FX impact for international pricing

**Step 3: Revenue Calculation**
```
Revenue = SUM across products/segments of: (Volume x Net Price x Seasonal Index)
```

### Method 4: Tops-Down (TAM x Share)

**Step 1: Total Addressable Market**
- Market size from credible third-party sources (Gartner, IDC, industry associations)
- Market growth rate (historical and projected)
- Cross-reference multiple sources — market sizing varies widely

**Step 2: Market Share Projection**
- Current market share (calculated from revenue / market size)
- Share trajectory (gaining, stable, or losing share?)
- Competitive dynamics (new entrants, exits, consolidation)

**Step 3: Revenue Derivation**
```
Revenue = TAM x Market Growth Rate x Target Market Share
```

**Warning:** This method is the least precise and should only be used for directional validation or early-stage companies without granular data. It should NEVER be the sole forecasting method for operating companies.

### Triangulation Protocol

When using multiple methods, compare results:
- If methods agree within 10%: High confidence — use the average
- If methods diverge 10-25%: Medium confidence — investigate the divergence, weight toward the method with better historical accuracy
- If methods diverge >25%: Low confidence — do NOT average. Understand why they disagree. Usually one method has a flawed assumption.

---

## Mode 5: Working Capital Forecasting

### Target: DSO/DPO/DIO-based working capital model with seasonal patterns

### Phase 1: Days Metrics Calculation

**Step 1: Compute Current Metrics**
```
DSO (Days Sales Outstanding)   = (Accounts Receivable / Revenue) x Days in Period
DPO (Days Payable Outstanding) = (Accounts Payable / COGS) x Days in Period
DIO (Days Inventory Outstanding) = (Inventory / COGS) x Days in Period
CCC (Cash Conversion Cycle)    = DSO + DIO - DPO
```

**Step 2: Historical Trend Analysis**
Compute DSO, DPO, DIO for each of the last 12+ months:
- Identify seasonal patterns (DSO often spikes in Q4 if customers delay payment over year-end)
- Identify structural trends (is DSO gradually increasing? This signals collection problems)
- Identify outliers (one-time events that distorted the metric)

**DATA NEEDED:** Monthly A/R, A/P, inventory, revenue, and COGS for at least 12 months (24 months preferred for seasonal modeling)

### Phase 2: Working Capital Forecast

**Step 1: DSO Forecast → Accounts Receivable**
```
Forecast A/R = (Forecast Revenue / Days in Period) x Forecast DSO
Change in A/R = Ending A/R - Beginning A/R (cash impact)
```

To forecast DSO:
- Start with trailing 3-month average DSO
- Adjust for seasonal pattern (apply monthly seasonal index from historical data)
- Adjust for known changes (new payment terms with a large customer, collections initiative, new billing system)
- Adjust for mix shift (adding enterprise customers with longer payment terms? Adding consumer with shorter terms?)

**Step 2: DPO Forecast → Accounts Payable**
```
Forecast A/P = (Forecast COGS / Days in Period) x Forecast DPO
Change in A/P = Ending A/P - Beginning A/P (cash impact — increase is positive)
```

To forecast DPO:
- Start with trailing 3-month average DPO
- Adjust for vendor payment term changes
- Adjust for strategic decisions (stretching payables to conserve cash vs. taking early payment discounts)
- Typical trade-off: 2/10 net 30 terms → paying on day 10 gives a 2% discount, equivalent to ~37% annualized return on giving up 20 days of float

**Step 3: DIO Forecast → Inventory**
```
Forecast Inventory = (Forecast COGS / Days in Period) x Forecast DIO
Change in Inventory = Ending Inventory - Beginning Inventory (cash impact — increase is negative)
```

To forecast DIO:
- Start with trailing 3-month average DIO
- Adjust for production planning (building inventory ahead of peak season)
- Adjust for supply chain changes (longer lead times = higher safety stock)
- Adjust for new product launches (initial inventory build)

### Phase 3: Cash Conversion Cycle Optimization

**Step 1: CCC Benchmarking**
Compare the company's CCC to industry benchmarks:
- **Negative CCC:** Collect before you pay — highly desirable (common in subscription, insurance, Amazon)
- **0-30 day CCC:** Efficient — typical for services and software
- **30-60 day CCC:** Average — typical for distribution and light manufacturing
- **60-90+ day CCC:** Capital-intensive — typical for heavy manufacturing, construction
- **Increasing CCC:** Cash trap — working capital consuming more cash each period

**Step 2: Improvement Levers**
Quantify the cash impact of improving each component by 5 days:

```
Cash Released from 5-Day DSO Improvement = (Annual Revenue / 365) x 5
Cash Released from 5-Day DIO Improvement = (Annual COGS / 365) x 5
Cash Cost of 5-Day DPO Reduction = (Annual COGS / 365) x 5
```

**Step 3: Net Working Capital Forecast**
```
Net Working Capital = A/R + Inventory + Prepaids - A/P - Accrued Liabilities - Deferred Revenue
Change in NWC = Cash impact on the cash flow statement
```

A growing company typically CONSUMES working capital (A/R and inventory grow faster than A/P). This is a critical cash flow item that many forecasts underestimate.

### Phase 4: Collection Rate Trend Analysis

**Step 1: Aging Bucket Analysis**
Track the percentage of A/R in each aging bucket monthly:

| Aging Bucket | Month 1 | Month 2 | Month 3 | Trend | Alert |
|-------------|---------|---------|---------|-------|-------|
| Current (0-30) | 65% | 62% | 58% | Declining | Warning |
| 31-60 days | 20% | 22% | 24% | Increasing | Warning |
| 61-90 days | 10% | 10% | 12% | Increasing | Alert |
| 90+ days | 5% | 6% | 6% | Stable | Monitor |

**Decision Gate:** If the current bucket percentage drops below 55% or the 90+ bucket exceeds 10%, this is a collections crisis requiring immediate action — not a forecasting adjustment.

**Step 2: Collection Effectiveness Index (CEI)**
```
CEI = (Beginning A/R + Monthly Revenue - Ending Total A/R) / (Beginning A/R + Monthly Revenue - Ending Current A/R) x 100
```
- Target: >80%
- Acceptable: 70-80%
- Poor: <70% — structural collections problem

---

## Tool Integration

| When the forecast needs... | Run this | Example |
|---------------------------|---------|---------|
| Revenue projection validation | `python3 tools/dcf.py --fcf 80,88,97,107,117 --wacc 0.10 --terminal-growth 0.03 --shares 100` | Validates growth trajectory against implied valuation |
| Probabilistic scenario ranges | `python3 tools/monte_carlo.py --initial 100000000 --return 0.15 --vol 0.25 --years 3 --sims 10000` | P10/P25/P50/P75/P90 outcome ranges |
| Debt service forecasting | `python3 tools/loan_amort.py --principal 50000000 --rate 0.065 --years 7` | Monthly P&I schedule for cash flow model |
| WACC for hurdle rates | `python3 tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05` | Discount rate for NPV of forecast scenarios |
| Macro scenario calibration | `python3 tools/portfolio_risk.py --returns -0.05,0.03,0.07,-0.02,0.04 --benchmark 0.01,0.02,0.03,0.01,0.02` | Historical variance patterns for stress calibration |

---

## Output Specifications

### Rolling Forecast Template

```
### [COMPANY NAME] ROLLING FORECAST — UPDATED [DATE]

                    Q1 (Act)  Q2 (Act)  Q3 (Fcast)  Q4 (Fcast)  Q1+1 (Fcast)  Q2+1 (Fcast)  FULL YEAR
REVENUE
  Product A         $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX
  Product B         $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX
  Total Revenue     $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX

COGS                $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX
GROSS PROFIT        $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX
  Gross Margin %    XX.X%     XX.X%     XX.X%       XX.X%       XX.X%         XX.X%         XX.X%

OPERATING EXPENSES  $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX

EBITDA              $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX        $X,XXX
  EBITDA Margin %   XX.X%     XX.X%     XX.X%       XX.X%       XX.X%         XX.X%         XX.X%

KEY DRIVERS
  New Logos          XX        XX        XX          XX          XX            XX            XX
  Churn Rate         X.X%      X.X%      X.X%        X.X%        X.X%          X.X%
  Avg Deal Size      $X,XXX    $X,XXX    $X,XXX      $X,XXX      $X,XXX        $X,XXX

FORECAST vs. BUDGET
  Revenue Variance   —         —         $X,XXX      $X,XXX      —             —             $X,XXX
  EBITDA Variance    —         —         $X,XXX      $X,XXX      —             —             $X,XXX

FORECAST ACCURACY (prior periods)
  Revenue MAPE:      X.X%     Bias: +/-X.X%
  EBITDA MAPE:       X.X%     Bias: +/-X.X%

SCENARIOS (Full Year)
  Bear (P10):        Revenue $X,XXX    EBITDA $X,XXX
  Base (P50):        Revenue $X,XXX    EBITDA $X,XXX
  Bull (P90):        Revenue $X,XXX    EBITDA $X,XXX
```

### 13-Week Cash Flow Template

See Mode 2, Phase 2, Step 3 for the complete 13-week cash flow layout.

### Scenario Comparison Template

```
### SCENARIO COMPARISON — [DATE]

                        BEAR           BASE           BULL
                        (P10-P25)      (P50)          (P75-P90)
ASSUMPTIONS
  Revenue Growth        X%             X%             X%
  Gross Margin          XX.X%          XX.X%          XX.X%
  New Hires             XX             XX             XX
  Churn Rate            X.X%           X.X%           X.X%

P&L IMPACT
  Revenue               $X,XXX         $X,XXX         $X,XXX
  Gross Profit          $X,XXX         $X,XXX         $X,XXX
  EBITDA                $X,XXX         $X,XXX         $X,XXX

CASH IMPACT
  Ending Cash           $X,XXX         $X,XXX         $X,XXX
  Liquidity Runway      XX weeks       XX weeks       XX weeks

COVENANT COMPLIANCE
  Leverage (Debt/EBITDA) X.Xx          X.Xx           X.Xx    [Limit: X.Xx]
  Coverage (EBITDA/Int)  X.Xx          X.Xx           X.Xx    [Limit: X.Xx]
  Breach?               YES/NO         NO             NO

RESPONSE ACTIONS (if bear materializes)
  1. [Specific action with timing and savings]
  2. [Specific action with timing and savings]
  3. [Specific action with timing and savings]
```

---

## Quality Gates & Completion Criteria

- [ ] Forecast is driver-based (not line-item extrapolation)
- [ ] All driver assumptions are documented with sources
- [ ] Seasonal patterns are reflected (not straight-lined)
- [ ] At least 3 scenarios exist (base/bull/bear) with explicit probability weights
- [ ] Cash flow forecast distinguishes between direct and indirect methods where appropriate
- [ ] Covenant compliance is tested under all scenarios (if debt exists)
- [ ] Forecast accuracy metrics are computed for prior periods
- [ ] Monte Carlo output provides P10/P50/P90 ranges for key financial lines
- [ ] Working capital forecast uses DSO/DPO/DIO dynamics, not static balances
- [ ] Liquidity runway is calculated and rated (green/yellow/red)
- [ ] Forecast vs. budget variance is shown alongside forecast vs. actual

**Success metric:** A CFO could present the forecast package to the board and lenders with confidence that every projection is traceable to an explicit driver assumption and calibrated against historical accuracy.

**Escalation triggers:**
- Liquidity runway falls below 13 weeks in any scenario → immediate flag, begin contingency planning
- Covenant breach forecast within 2 quarters → flag for proactive lender engagement
- Forecast MAPE exceeds 20% for 3 consecutive periods → methodology needs overhaul
- Bull and bear scenarios produce the same directional result → scenarios are too narrow, widen assumptions
- Pipeline coverage falls below 2x → revenue target is at risk, flag to sales leadership

---

## Hard Constraints

- **NEVER** fabricate actual financial data, historical metrics, or market benchmarks
- **NEVER** present a single-point forecast without scenario ranges — false precision is dangerous
- **NEVER** assume last year's seasonality applies without checking for structural changes
- **NEVER** extrapolate a trend beyond the data's reasonable range without flagging the extrapolation risk
- **ALWAYS** distinguish between actuals (locked) and forecast (updateable) in every output
- **ALWAYS** document the forecasting method used and why it was selected
- **ALWAYS** track forecast accuracy over time — a forecast that is never graded never improves
- **ALWAYS** test covenant compliance under the bear case, not just the base case
- **ALWAYS** show the cash flow impact of working capital changes — P&L profitability does not equal cash generation
- If the user provides projections without assumptions, **require** assumptions before incorporating

---

## Common Pitfalls

1. **Confusing precision with accuracy:** A forecast to the dollar is precise but almost certainly inaccurate. A forecast with P10/P50/P90 ranges is less precise but far more useful. → Always provide ranges. Single-point forecasts create a false sense of certainty.

2. **Anchoring to the budget:** The forecast should reflect reality, not wish fulfillment. If the business is trending below budget, the forecast should reflect that — not bend toward the budget because "we'll make it up in Q4." → Compare forecast to actuals trend, not to budget hope.

3. **Ignoring working capital in cash forecasts:** A company can be profitable on the P&L and run out of cash because receivables are growing faster than collections. → Always model the cash conversion cycle separately from P&L profitability.

4. **Stale pipeline assumptions:** Using pipeline stage probabilities from two years ago when the market has changed. If sales cycles have lengthened, stage probabilities have declined. → Recalibrate stage probabilities quarterly using trailing 4-quarter conversion data.

5. **Symmetric scenarios:** Making the bull case "+10% revenue" and the bear case "-10% revenue" without thinking about what drives each. Downside scenarios are usually faster and steeper than upside scenarios. → Build scenarios from causal narratives ("recession hits, customers freeze budgets, churn doubles"), not from symmetric percentage adjustments.

6. **Forecasting revenue without forecasting cost-to-serve:** Revenue growth that requires disproportionate cost growth destroys value. → For every revenue scenario, model the associated cost (headcount, infrastructure, customer acquisition cost) required to achieve it.

7. **Weekly cash forecasts without weekly data:** Building a 13-week cash flow model using monthly averages divided by 4.33. Payroll hits on specific dates. Rent hits on the 1st. Quarterly taxes hit on specific dates. → Use actual payment dates for all known recurring disbursements. Only use averages for variable items.

8. **Ignoring correlation between drivers:** Modeling revenue growth and margin expansion simultaneously in the bull case. In reality, rapid growth often compresses margins (more hiring, more marketing, less operating leverage). → Define the correlation structure between drivers explicitly. Revenue growth and margin often move inversely in the short term.

---

## Related Skills

- For annual budget builds and variance analysis, use **`/budget`**
- For full FP&A analysis and financial modeling, use **`/fpa`**
- For board-ready presentation formatting, use **`/board-deck`**
- For LBO modeling with leverage scenarios, use **`/lbo`**
- For debt service modeling, run `python3 tools/loan_amort.py`
- For valuation sanity checks on forecasts, run `python3 tools/dcf.py`
