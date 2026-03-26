# Real Estate Private Equity

Prompt templates for real estate private equity investing, covering property valuation, development analysis, REIT analytics, debt structuring, and market analysis.

## Role Context

```
You are a vice president at a real estate private equity fund ($5B AUM) investing across
core-plus, value-add, and opportunistic strategies. You evaluate properties through a
disciplined cash-flow lens: NOI quality, cap rate risk, lease structure, and capital
expenditure requirements. You build ground-up DCF models with explicit assumptions for
rent growth, vacancy, tenant improvement costs, and financing terms. You think in cap
rates and yield on cost for acquisitions, IRR and equity multiples for fund-level returns,
and always stress-test against rising rates, tenant defaults, and supply shocks. Your
analytical rigor extends from single-asset underwriting to portfolio construction and
REIT-level sum-of-the-parts valuation.
```

For foundational PE frameworks (returns analysis, due diligence checklists), see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below are specific to real estate valuation, development, and capital structure.

---

## 1. Property Valuation

### Direct Capitalization and DCF

```
Value a [property type: office / multifamily / industrial / retail] property:

Property details:
- Location: [city, submarket]
- Size: [X] sq ft / [X] units
- Year built / renovated: [X]
- Occupancy: [X]%
- Tenant roster: [anchor tenant(s), WALT, credit quality]

Operating financials (trailing 12 months):
- Gross potential rent: $[X]
- Vacancy and collection loss: ($[X]) → [X]% vacancy rate
- Effective gross income: $[X]
- Other income (parking, storage, laundry): $[X]
- Total revenue: $[X]

Operating expenses:
- Property taxes: $[X]
- Insurance: $[X]
- Utilities: $[X]
- Repairs and maintenance: $[X]
- Property management fee: $[X] ([X]% of EGI)
- General and administrative: $[X]
- Total opex: $[X]

Net Operating Income (NOI) = Total Revenue - Total Opex = $[X]

Valuation Method 1 — Direct Capitalization:
  Property Value = NOI / Cap Rate
  Market cap rate for [property type] in [submarket]: [X]%
  Implied value: $[X] / [X]% = $[X]
  Per sq ft: $[X] (compare to replacement cost of $[X] per sq ft)

Valuation Method 2 — Discounted Cash Flow (10-year hold):
  Year 1-10 cash flows:
  - Revenue growth: [X]% per year (contractual escalators + market rent growth)
  - Expense growth: [X]% per year
  - Capex reserves: $[X] per sq ft per year
  - Tenant improvements on lease renewal: $[X] per sq ft
  - Leasing commissions: [X]% of total lease value
  - NOI growth: [X]% per year (net of capex and leasing costs)

  Terminal value (Year 10):
  - Year 11 NOI: $[X]
  - Terminal cap rate: [X]% (entrance cap + [X]bps for aging / market uncertainty)
  - Terminal value: $[X]
  - Less: disposition costs ([X]% of sale price)

  Discount rate: [X]% (unlevered, based on risk profile)
  NPV of cash flows + terminal value = $[X]

Valuation Method 3 — Comparable Sales:
  Recent transactions for similar properties in the submarket:
  | Property | Date | Size | Price/SF | Cap Rate |
  |----------|------|------|----------|----------|
  | Comp 1   | [X]  | [X]  | $[X]    | [X]%    |
  | Comp 2   | [X]  | [X]  | $[X]    | [X]%    |
  Adjustments for: location, age, tenant quality, lease term remaining
  Implied value: $[X]

Reconciliation: weight the three methods based on reliability of inputs.
```

### Cap Rate Analysis

```
Analyze cap rate dynamics for [property type] in [market]:

Current cap rates:
- Class A [property type]: [X]%
- Class B: [X]%
- Class C: [X]%
- 10-year Treasury yield: [X]%
- Cap rate spread to Treasuries: [X]bps (historical average: [X]bps)

Cap rate decomposition:
  Cap Rate = Risk-Free Rate + Risk Premium - Expected NOI Growth Rate

  Current: [X]% = [X]% + [X]% - [X]%
  If rates rise 100bps and spreads compress 50bps: new cap rate = [X]%
  Impact on property values: ΔValue ≈ -NOI / (Cap Rate)^2 × ΔCap Rate
  For a property with $[X]M NOI: [X]bps of cap rate expansion → $[X]M value decline ([X]%)

Key questions:
1. Are current cap rates justified by the spread to Treasuries vs. historical average?
2. If the 10-year rises to [X]%, what cap rate is implied at average spreads?
3. What NOI growth rate is needed to offset [X]bps of cap rate expansion?
4. Which property types have the most cap rate compression risk? (lowest spread to risk-free)
```

---

## 2. Development Analysis

### Ground-Up Development Pro Forma

```
Underwrite a ground-up development of [property type] in [location]:

Land and predevelopment:
- Land acquisition cost: $[X]M ($[X] per buildable sq ft)
- Entitlement and permitting costs: $[X]M
- Architecture and engineering: $[X]M
- Predevelopment timeline: [X] months

Construction:
- Gross building area: [X] sq ft
- Net rentable area: [X] sq ft (efficiency ratio: [X]%)
- Hard costs: $[X] per sq ft x [X] sq ft = $[X]M
- Soft costs (A&E, legal, permits, insurance): [X]% of hard costs = $[X]M
- Developer fee: [X]% of total project cost = $[X]M
- Construction contingency: [X]% = $[X]M
- Construction timeline: [X] months
- Construction financing: [X]% LTC at [X]% rate, interest reserve = $[X]M

Total development cost: $[X]M ($[X] per sq ft)

Lease-up and stabilization:
- Market rent: $[X] per sq ft (gross / net basis)
- Lease-up pace: [X] sq ft per month ([X] months to [X]% occupancy)
- Concessions: [X] months free rent on average
- Tenant improvements: $[X] per sq ft
- Leasing commissions: $[X] per sq ft
- Stabilization timeline: [X] months post-construction completion

Stabilized operating metrics:
- Stabilized NOI: $[X]M
- Yield on cost = Stabilized NOI / Total Development Cost = [X]%
- Market cap rate for comparable stabilized assets: [X]%
- Development spread = Yield on Cost - Market Cap Rate = [X]bps
  (This spread compensates for development risk; target: 100-200bps)

Stabilized value = Stabilized NOI / Market Cap Rate = $[X]M
Profit on cost = (Stabilized Value - Total Cost) / Total Cost = [X]%

Equity returns:
- Total equity required: $[X]M (total cost - construction loan)
- Equity multiple on development: (Stabilized Value - Debt) / Equity = [X]x
- Development IRR (from land close to stabilized sale): [X]%
- Key risk: if market rents decline [X]% during construction, yield on cost falls to [X]%
  and development spread evaporates
```

---

## 3. REIT Analysis

### NAV and Sum-of-the-Parts

```
Build a net asset value (NAV) model for [REIT name]:

Property portfolio:
| Segment         | NOI ($M) | Cap Rate | Implied Value ($M) |
|-----------------|----------|----------|--------------------|
| [Segment 1]     | $[X]    | [X]%    | $[X]              |
| [Segment 2]     | $[X]    | [X]%    | $[X]              |
| [Segment 3]     | $[X]    | [X]%    | $[X]              |
| Development pipeline | —   | —       | $[X] (at cost)    |
| Land bank       | —        | —       | $[X] (appraised)  |

Gross asset value (GAV): $[X]M

Less liabilities:
- Total debt: ($[X]M)
- Preferred equity: ($[X]M)
- Other liabilities: ($[X]M)

Net asset value: $[X]M
NAV per share: $[X] (on [X]M diluted shares)

Current share price: $[X]
NAV premium / (discount): [X]%

AFFO analysis:
- FFO: $[X]M (net income + depreciation - gains on sale)
- Less: recurring capex ($[X]M), straight-line rent adjustment ($[X]M), leasing costs ($[X]M)
- AFFO: $[X]M
- AFFO per share: $[X]
- AFFO payout ratio: [X]% (dividend / AFFO)
- AFFO multiple: share price / AFFO per share = [X]x

Implied cap rate from stock price:
  EV = Market cap + Net debt + Preferred = $[X]M
  Implied cap rate = Total NOI / EV = [X]%
  Compare to private market cap rates: is the public market pricing assets
  cheaper or richer than the private market?

When does it make sense to buy the REIT vs. direct property?
- If implied cap rate > private market cap rate: REIT is cheap, buy the stock
- If implied cap rate < private market cap rate: private market is cheaper, buy direct
```

---

## 4. Debt Structuring

### Real Estate Capital Stack Design

```
Structure the capital stack for a $[X]M acquisition of [property type]:

Property NOI: $[X]M
Acquisition cap rate: [X]%
Acquisition price: $[X]M (NOI / cap rate)

Senior mortgage:
- LTV: [X]% → loan amount: $[X]M
- DSCR test: NOI / Debt Service ≥ [X]x
  Annual debt service at [X]% rate, [X]-year amortization: $[X]M
  DSCR = $[X]M / $[X]M = [X]x ✓
- Interest-only period: [X] years (common in transitional/value-add)
- During IO: DSCR on IO payments = $[X]M / $[X]M = [X]x
- Loan term: [X] years, [X]-year amortization
- Prepayment: yield maintenance / defeasance / open after [X] years

Mezzanine debt (if applicable):
- LTV: [X]% to [X]% → mezz amount: $[X]M
- Rate: [X]% (fixed or floating + spread)
- Mezz DSCR: [X]x (on combined senior + mezz debt service)
- Intercreditor agreement with senior lender

Preferred equity (if applicable):
- Preferred amount: $[X]M
- Preferred return: [X]% (current pay or accruing)
- Preferred sits above common equity, below debt in waterfall
- Participation: does preferred share in upside beyond pref return?

Common equity:
- Equity required: $[X]M ([X]% of total capitalization)
- GP co-invest: $[X]M ([X]% of equity)
- LP equity: $[X]M

Blended cost of capital:
  WACC = (Equity % x Cost of Equity) + (Debt % x Cost of Debt x (1 - Tax Rate))
       + (Mezz % x Cost of Mezz) + (Pref % x Pref Return)
  WACC = [X]%
  Spread over cap rate: [X]bps (positive spread = positive leverage effect)

Positive leverage test:
  If cap rate > mortgage constant (debt service / loan amount), leverage is accretive
  Cap rate: [X]% vs. mortgage constant: [X]%
  Leverage is [accretive / dilutive] to equity returns
```

### Equity Waterfall with Promote

```
Design the GP/LP waterfall for a real estate fund or deal-level co-invest:

Total equity: $[X]M
- GP contribution: $[X]M ([X]% of equity)
- LP contribution: $[X]M ([X]% of equity)

Waterfall structure (American / European):

Tier 1 — Return of Capital:
  100% of distributions go to return all contributed capital (GP and LP pro rata)

Tier 2 — Preferred Return:
  [X]% preferred return (compounding annually) to all equity holders pro rata
  Pref accrues from date of contribution, reduced by prior distributions

Tier 3 — GP Catch-Up:
  [X]% of distributions to GP until GP has received [X]% of total profits
  (This "catches up" the GP to their promote share on all profits, not just excess)

Tier 4 — Carried Interest Split:
  [X]% to LP / [X]% to GP on all remaining distributions
  (Common: 80/20 after 8% pref; aggressive: 70/30 or tiered promote)

Tiered promote variant:
  IRR < [X]%: no promote (pref only)
  IRR [X]% - [X]%: [X]% promote (e.g., 20%)
  IRR > [X]%: [X]% promote (e.g., 30%)

Model the waterfall at different exit scenarios:
| Exit Value | Total Equity Return | LP MOIC | GP MOIC | LP IRR | GP IRR |
|------------|--------------------:|--------:|--------:|-------:|-------:|
| $[X]M      | $[X]M             | [X]x   | [X]x   | [X]%  | [X]%  |
| $[X]M      | $[X]M             | [X]x   | [X]x   | [X]%  | [X]%  |
| $[X]M      | $[X]M             | [X]x   | [X]x   | [X]%  | [X]%  |

Key: GP MOIC should be significantly higher than LP MOIC due to promote leverage.
This is the incentive for the GP to outperform.
```

---

## 5. Market Analysis

### Supply/Demand and Rent Forecasting

```
Analyze the [property type] market in [metro area / submarket]:

Demand indicators:
- Employment growth: [X]% (total and by sector relevant to property type)
- Population growth / migration trends: [X]%
- Household formation rate: [X] per year
- GDP growth (MSA level): [X]%
- Sector-specific demand drivers:
  - Office: job growth in office-using sectors (FIRE, tech, professional services)
  - Industrial: e-commerce penetration, inventory-to-sales ratio, reshoring trends
  - Multifamily: homeownership rate, affordability gap (rent vs. own), millennial/Gen Z demographics
  - Retail: consumer spending growth, retail sales per sq ft trends

Supply indicators:
- Current inventory: [X]M sq ft / [X] units
- Under construction: [X]M sq ft ([X]% of inventory)
- Planned / entitled: [X]M sq ft
- Construction pipeline as % of inventory vs. historical average
- Barriers to supply: zoning, land availability, construction costs, NIMBYism
- Projected deliveries by year: [X] in 20XX, [X] in 20XX

Market fundamentals:
- Current vacancy rate: [X]% (vs. historical average [X]%)
- Net absorption (trailing 12 months): [X] sq ft
- Absorption as % of new supply: [X]% (> 100% = tightening market)
- Current asking rent: $[X] per sq ft
- Rent growth (trailing 12 months): [X]%
- Concessions: [X] months free rent (widening or narrowing?)

Forecast:
1. Net absorption forecast: [X] sq ft/year based on employment/population growth
2. Net new supply: [X] sq ft/year (under construction + probable starts)
3. Supply/demand balance: net absorption - new supply = [X] sq ft
4. Implied vacancy trajectory: [X]% → [X]% over [X] years
5. Implied rent growth: [X]% per year (function of vacancy vs. equilibrium)
6. Cap rate forecast: [X]% (based on rate environment, spread analysis, investor appetite)
```

---

## Mathematical Frameworks

**NOI Calculation**:

```
Gross Potential Rent (GPR)
- Vacancy and Collection Loss
= Effective Gross Income (EGI)
+ Other Income
= Total Revenue
- Operating Expenses (taxes, insurance, utilities, R&M, management, G&A)
= Net Operating Income (NOI)

Note: NOI excludes debt service, capex, depreciation, and income taxes.
These are below-the-line items that affect returns but not property-level operating income.
```

**Cap Rate and Value**:

```
Cap Rate = NOI / Property Value    (or: Value = NOI / Cap Rate)

Going-in cap rate = Year 1 NOI / Purchase Price
Exit cap rate = Exit Year NOI / Sale Price
Yield on cost = Stabilized NOI / Total Development Cost (for development deals)

Cap rate spread = Cap Rate - 10-Year Treasury Yield
  Historical average spread: ~250-350bps for institutional quality
  Below average spread → cap rates likely to expand → value risk
```

**Equity Multiple and Cash-on-Cash**:

```
Equity Multiple = Total Distributions / Total Equity Invested
  Includes: operating cash flow + refinancing proceeds + sale proceeds

Cash-on-Cash Return = Annual Pre-Tax Cash Flow / Total Equity Invested
  Year 1 CoC = (NOI - Debt Service) / Equity = [X]%
  This measures current yield, not total return

IRR = discount rate that sets NPV of all equity cash flows to zero
  Equity cash flows = -Initial equity, +Annual cash flow (Year 1-n), +Sale proceeds - Debt payoff (Year n)
```

**Positive Leverage Test**:

```
Mortgage Constant (K) = Annual Debt Service / Loan Amount
Cap Rate > K → leverage is accretive (boosts equity returns above unlevered return)
Cap Rate < K → leverage is dilutive (equity returns below unlevered return)

Example:
  Cap rate: 5.5%, Mortgage constant: 4.8% → positive leverage (+70bps accretion)
  Cap rate: 5.5%, Mortgage constant: 6.2% → negative leverage (equity return compressed)
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Core PE returns framework and due diligence
- [`infrastructure.md`](infrastructure.md) — Infrastructure real assets with regulated/contracted revenues
- [`private-credit.md`](private-credit.md) — CMBS, real estate debt structuring, DSCR analysis
- [`special-situations.md`](special-situations.md) — Distressed real estate, NPL portfolios, opportunistic plays
