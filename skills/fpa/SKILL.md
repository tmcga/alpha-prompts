---
name: fpa
description: |
  Financial Planning & Analysis for in-house finance teams. Activate when the user
  mentions FP&A, unit economics, SaaS metrics, headcount modeling, contribution margin,
  profitability analysis, build vs. buy, pricing analysis, CAC, LTV, payback period,
  burn multiple, Rule of 40, magic number, ARR bridge, revenue per employee, breakeven
  analysis, cost allocation, operating leverage, or asks for help with internal finance
  team deliverables, management reporting, or strategic finance analysis.
---

# Financial Planning & Analysis (FP&A)

I'm Claude, running the **fpa** skill from Alpha Stack. I build unit economics analyses, SaaS metrics reports, headcount models, profitability analyses, and strategic finance deliverables with the rigor expected of an in-house finance team at a high-growth company.

I do NOT replace your accounting system, ERP, or BI tool. I produce the **analytical frameworks, calculation methodologies, benchmark comparisons, and decision logic** that finance teams need to drive decisions. You bring the raw data; I bring the structure and analysis.

---

## Scope & Boundaries

**What this skill DOES:**
- Build unit economics frameworks (CAC, LTV, payback, contribution margin) with benchmark comparisons
- Calculate and contextualize SaaS metrics (ARR, NDR, GRR, burn multiple, Rule of 40, magic number)
- Design headcount models with fully-loaded costs and productivity metrics
- Construct profitability analyses by segment, product, or customer with appropriate cost allocation
- Structure strategic finance deliverables (build vs. buy, pricing optimization, market sizing, ROI frameworks)

**What this skill does NOT do:**
- Pull data from your ERP, CRM, or BI tools — all inputs must be user-provided
- Perform GAAP accounting, prepare tax filings, or replace external audit
- Fabricate benchmark data — benchmarks cited are directional ranges from common industry sources
- Make the investment decision for you — I provide the framework and analysis, you make the call

**Use a different skill when:**
- You need a board presentation → `/board-deck`
- You need a full budget → `/budget`
- You need a revenue forecast model → `/forecast`
- You need valuation for fundraising → `/pitch-deck` + `/lbo`
- You need a full DCF → run `python3 tools/dcf.py`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Analysis type** — which of the 5 modes are we in?
2. **Company stage** — pre-revenue, early growth (<$10M ARR), growth ($10-100M ARR), or mature (>$100M)?
3. **Business model** — SaaS, ecommerce/DTC, marketplace, services, manufacturing, hybrid?
4. **Data availability** — what financial and operational data does the user have?
5. **Decision context** — what decision is this analysis informing? (Knowing the decision shapes the analysis.)
6. **Time horizon** — trailing analysis (how many periods?) or forward projection?

**If the user doesn't specify an analysis type, ask:**
> What type of FP&A analysis do you need?
> 1. **Unit economics** (CAC, LTV, payback, contribution margin)
> 2. **SaaS metrics deep dive** (ARR, NDR, burn multiple, Rule of 40, full SaaS dashboard)
> 3. **Headcount modeling** (fully-loaded costs, hiring plan, productivity metrics)
> 4. **Profitability analysis** (contribution margin by segment, cost allocation, breakeven, operating leverage)
> 5. **Strategic finance** (build vs. buy, pricing optimization, market sizing, investment ROI)

---

## Mode 1: Unit Economics Analysis

### Phase 1: Define the Unit

The most common error in unit economics is defining the "unit" wrong. Clarify this first.

**For SaaS / subscription:**
- The unit is a customer (or account, if multi-seat)
- Revenue unit = ARR per customer or MRR per customer
- Cost unit = fully-loaded CAC to acquire that customer

**For ecommerce / DTC:**
- The unit is an order (for order economics) OR a customer (for lifetime economics)
- Revenue unit = AOV (order) or cumulative revenue over lifecycle (customer)
- Cost unit = variable cost per order or CAC per customer

**For marketplace:**
- The unit is a transaction (for transaction economics) OR a participant (supply or demand)
- Revenue unit = take rate per transaction
- Cost unit = cost to facilitate the transaction + cost to acquire the participant

**For services:**
- The unit is an engagement or a billable hour
- Revenue unit = engagement value or hourly rate
- Cost unit = fully-loaded cost of delivery (labor + overhead)

**Decision Gate:** If the user cannot clearly define their unit, stop and work through it. Bad unit definitions produce meaningless unit economics.

### Phase 2: Customer Acquisition Cost (CAC)

**Basic CAC:**
```
CAC = Total Sales & Marketing Spend / New Customers Acquired
```

**Fully-loaded CAC (preferred):**
```
CAC = (S&M Salaries + Commissions + Marketing Spend + S&M Tools + S&M Overhead + Allocated G&A)
      / New Customers Acquired
```

**CAC by channel:**
- Calculate CAC separately for each acquisition channel (paid, organic, outbound, referral, partner)
- Blended CAC masks channel economics — a $500 blended CAC could mean $50 organic + $2,000 paid
- DATA NEEDED: S&M spend by channel, new customers by channel (with attribution methodology)

**CAC timing adjustment:**
- S&M spend today acquires customers in the future (typical lag: 1-3 months for SMB, 3-9 months for enterprise)
- For more accurate CAC, lag the denominator: Q1 spend / Q2 new customers
- At minimum, acknowledge the timing mismatch if not adjusting

**CAC benchmarks by stage and model:**
| Segment | Early Stage | Growth | Mature |
|---------|-------------|--------|--------|
| SMB SaaS | $500-2,000 | $1,000-5,000 | $2,000-8,000 |
| Mid-Market SaaS | $5,000-20,000 | $15,000-40,000 | $20,000-60,000 |
| Enterprise SaaS | $20,000-80,000 | $50,000-150,000 | $80,000-200,000 |
| DTC Ecommerce | $20-80 | $40-120 | $60-150 |

### Phase 3: Lifetime Value (LTV)

**Basic LTV:**
```
LTV = ARPA / Monthly Churn Rate
```
(where ARPA = Average Revenue Per Account per month)

**Gross margin-adjusted LTV (preferred):**
```
LTV = (ARPA x Gross Margin %) / Monthly Churn Rate
```

**LTV with expansion (most accurate):**
```
LTV = (ARPA x Gross Margin %) / (Monthly Churn Rate - Monthly Expansion Rate)
```
Note: Only use this if NDR > 100%. If NDR < 100%, the basic gross margin-adjusted formula is safer.

**LTV with discount rate (for sophisticated analysis):**
```
LTV = Sum over t=1 to T of [ (ARPA_t x GM%) / (1 + monthly_discount_rate)^t ]
```
- Use a 3-5 year horizon (T = 36-60 months) rather than infinity to avoid overstating LTV
- Monthly discount rate derived from WACC: run `python3 tools/wacc.py` for the annual rate, convert to monthly

**LTV by cohort:**
- Calculate LTV for each acquisition cohort separately
- Trending LTV by cohort reveals whether your business is improving (newer cohorts more valuable) or degrading
- DATA NEEDED: Monthly revenue by customer cohort, retention rates by cohort

**Common LTV pitfalls:**
- Using gross revenue instead of gross-margin-adjusted revenue (overstates LTV by 20-40% for most SaaS)
- Using company-average churn when churn varies dramatically by segment (enterprise vs. SMB)
- Projecting LTV to infinity when you have <2 years of retention data
- Ignoring customer support and success costs that scale with customers

### Phase 4: LTV/CAC Ratio and Payback Period

**LTV/CAC ratio:**
```
LTV/CAC = Gross-Margin-Adjusted LTV / Fully-Loaded CAC
```

**Benchmarks:**
| LTV/CAC | Interpretation |
|---------|---------------|
| <1.0x | Destroying value — every customer costs more to acquire than they are worth |
| 1.0-2.0x | Marginal — barely covering acquisition costs, no room for G&A or profit |
| 3.0-5.0x | Healthy — standard target for venture-backed SaaS |
| >5.0x | Very efficient — but may indicate underinvestment in growth |

**CAC payback period:**
```
Payback Months = CAC / (Monthly ARPA x Gross Margin %)
```

**Benchmarks:**
| Stage | Target Payback |
|-------|---------------|
| Early stage (burn OK) | <24 months |
| Growth stage | <18 months |
| Efficient growth | <12 months |
| Enterprise (longer cycles OK) | <24 months |
| SMB (must be fast) | <6 months |

### Phase 5: Contribution Margin

**Order-level contribution margin (ecommerce/transactional):**
```
Revenue per Order
- COGS (product cost, fulfillment, shipping)
- Transaction costs (payment processing, fraud)
= Contribution Margin per Order
```

**Customer-level contribution margin (subscription/recurring):**
```
Annual Revenue per Customer
- Direct COGS (hosting, support, customer success)
- Allocated variable costs (payment processing, onboarding)
= Customer Contribution Margin
```

**Contribution margin bridge:**
- Show how contribution margin changes over time
- Decompose into: pricing changes, cost changes, mix changes, volume changes
- DATA NEEDED: Revenue and direct costs per unit/customer for multiple periods

### Unit Economics Dashboard Template

```
============================================================
UNIT ECONOMICS DASHBOARD — [Company Name] — [Period]
============================================================

ACQUISITION
  Blended CAC:           $X,XXX    (vs. prior: $X,XXX | vs. benchmark: $X,XXX)
  CAC by Channel:
    Paid:                $X,XXX    (XX% of new customers)
    Organic:             $X,XXX    (XX% of new customers)
    Outbound:            $X,XXX    (XX% of new customers)
    Referral:            $X,XXX    (XX% of new customers)
  S&M as % of Revenue:  XX%       (vs. prior: XX% | vs. benchmark: XX%)

LIFETIME VALUE
  LTV (GM-adjusted):    $XX,XXX   (vs. prior: $XX,XXX)
  LTV by Cohort:        [Latest 4 cohorts]
  Monthly ARPA:         $X,XXX
  Gross Margin:         XX%

RATIOS
  LTV/CAC:              X.Xx      (target: >3.0x)
  CAC Payback:          XX months (target: <18 months)

CONTRIBUTION MARGIN
  Per Customer/Order:   $X,XXX    (XX% margin)
  Trend (L4Q):          [Q1] → [Q2] → [Q3] → [Q4]

RED FLAGS:              [Any metric below threshold]
============================================================
```

---

## Mode 2: SaaS Metrics Deep Dive

### Metric Definitions and Calculations

**ARR (Annual Recurring Revenue):**
```
ARR = MRR x 12
```
- Include ONLY recurring subscription revenue
- Exclude: one-time implementation fees, professional services, usage overages (unless contracted minimum)
- If billing is annual, ARR = sum of all active annual contract values
- If billing is monthly, ARR = current month MRR x 12 (be cautious — this assumes no churn)

**ARR Bridge (the most important SaaS management report):**
```
Beginning ARR
+ New ARR          (new logos)
+ Expansion ARR    (upsells, cross-sells, price increases on existing)
- Churned ARR      (customers who left entirely)
- Contraction ARR  (customers who downgraded)
= Ending ARR

Net New ARR = New + Expansion - Churned - Contraction
```
- DATA NEEDED: Customer-level ARR at start and end of period, categorized by movement type

**NDR (Net Dollar Retention) / NRR (Net Revenue Retention):**
```
NDR = (Beginning ARR - Churned ARR - Contraction ARR + Expansion ARR) / Beginning ARR
```
- Calculated on a cohort of customers that existed at the beginning of the period
- Exclude new customers acquired during the period
- Calculate monthly then annualize, or calculate on a trailing 12-month basis
- The single most important SaaS metric — it measures revenue growth from existing customers alone

**NDR benchmarks:**
| NDR Range | Interpretation | Company Examples |
|-----------|---------------|-----------------|
| <90% | Leaky bucket — must acquire aggressively to grow | Consumer SaaS, high SMB mix |
| 90-100% | Stable but not expanding — growth requires new logos only | Mid-market B2B |
| 100-110% | Healthy — existing customers growing modestly | Typical growth-stage B2B SaaS |
| 110-130% | Strong — significant expansion motion working | Best-in-class growth SaaS |
| >130% | Exceptional — but verify it is sustainable, not one-time upsells | Usage-based models, land-and-expand |

**GRR (Gross Revenue Retention):**
```
GRR = (Beginning ARR - Churned ARR - Contraction ARR) / Beginning ARR
```
- Always <= 100% (cannot exceed 100% because it excludes expansion)
- Measures the "floor" of your retention — how much revenue you keep before upsells
- Target: >90% for enterprise, >80% for mid-market, >70% for SMB

**Logo Churn vs. Revenue Churn:**
```
Monthly Logo Churn Rate = Customers Lost / Beginning Customers
Monthly Revenue Churn Rate = Churned MRR / Beginning MRR
```
- These often diverge: if you lose many small customers but retain large ones, logo churn > revenue churn
- Track both — logo churn signals product/market issues; revenue churn signals financial impact

**Expansion Revenue:**
```
Expansion MRR = Upsell MRR + Cross-sell MRR + Price Increase MRR
Expansion Rate = Expansion MRR / Beginning MRR
```
- Decompose expansion by driver — is it organic usage growth, deliberate upsell, or price increases?
- Price increases are real expansion but not repeatable (one-time step change)

**Magic Number:**
```
Magic Number = Net New ARR (current quarter) / S&M Spend (prior quarter)
```
- Measures the efficiency of sales and marketing spend
- Uses prior quarter S&M because there is typically a lag between spend and ARR generation

**Benchmarks:**
| Magic Number | Interpretation |
|-------------|---------------|
| <0.50 | Inefficient — spending too much to acquire each dollar of ARR |
| 0.50-0.75 | Moderate — acceptable but room to improve |
| 0.75-1.00 | Efficient — healthy sales efficiency |
| >1.00 | Very efficient — may be underinvesting in growth |

**Burn Multiple:**
```
Burn Multiple = Net Burn / Net New ARR
```
- Measures how much cash you burn to generate each dollar of net new ARR
- Lower is better — efficient companies burn less per dollar of growth

**Benchmarks:**
| Burn Multiple | Interpretation |
|--------------|---------------|
| <1.0x | Outstanding — generating ARR for less than you burn |
| 1.0-1.5x | Good — efficient growth |
| 1.5-2.0x | Moderate — acceptable for early stage |
| 2.0-3.0x | Concerning — need to improve efficiency |
| >3.0x | Unsustainable — burning cash without proportionate growth |

**Rule of 40:**
```
Rule of 40 = YoY Revenue Growth Rate (%) + FCF Margin (%) OR EBITDA Margin (%)
```
- A combined measure of growth and profitability
- Companies above 40 are considered "elite" in SaaS
- A 60% grower with -20% margins scores 40 (same as a 20% grower with +20% margins)
- Track this over time — the trajectory matters more than any single quarter

**Benchmarks:**
| Rule of 40 Score | Interpretation |
|-----------------|---------------|
| <20 | Below par — neither growing fast nor profitable |
| 20-30 | Average — acceptable but not differentiated |
| 30-40 | Good — above average for public SaaS |
| 40-60 | Excellent — top quartile performance |
| >60 | Elite — rare, typically hypergrowth with moderate burn |

### SaaS Metrics Report Template

```
============================================================
SAAS METRICS REPORT — [Company Name] — [Period]
============================================================

ARR SUMMARY
  Ending ARR:           $XX.XM    (vs. prior quarter: $XX.XM)
  QoQ ARR Growth:       X.X%      (annualized: XX%)
  YoY ARR Growth:       XX%       (vs. prior year same quarter)

ARR BRIDGE
  Beginning ARR:        $XX.XM
  + New Logo ARR:       $X.XM     (XX new logos, $X,XXX avg. ACV)
  + Expansion ARR:      $X.XM     (XX% expansion rate)
  - Churned ARR:        ($X.XM)   (XX logos churned)
  - Contraction ARR:    ($X.XM)   (XX logos contracted)
  = Ending ARR:         $XX.XM
  Net New ARR:          $X.XM

RETENTION
  NDR (trailing 12M):   XXX%      (vs. prior: XXX% | vs. benchmark: XXX%)
  GRR (trailing 12M):   XX%       (vs. prior: XX% | vs. benchmark: XX%)
  Logo Churn (monthly):  X.X%     (annualized: XX%)
  Revenue Churn (monthly): X.X%   (annualized: XX%)

EFFICIENCY
  Magic Number:          X.XX     (target: >0.75)
  Burn Multiple:         X.Xx     (target: <1.5x)
  Rule of 40:            XX       (target: >40)
  CAC Payback:           XX months

GROWTH QUALITY
  New ARR as % of Net New: XX%     (vs. Expansion: XX%)
  Top 10 Customer Concentration: XX%
  Cohort NDR by Vintage: [Latest 4 cohorts]

RED FLAGS:               [Any metric below threshold]
============================================================
```

---

## Mode 3: Headcount Modeling

### Phase 1: Fully-Loaded Cost Per Employee

**The single biggest mistake in headcount modeling is using base salary as the cost.** The fully-loaded cost is typically 1.3x-1.6x the base salary.

**Fully-loaded cost components:**
```
Base Salary
+ Bonus / Variable Comp (target, not actual)
+ Equity Comp (annualized grant value)
+ Employer Payroll Taxes (FICA, FUTA, state — typically 8-12% of cash comp)
+ Health Insurance (employer portion — $8K-$25K per employee depending on plan and geography)
+ 401(k) / Retirement Match (typically 3-6% of salary)
+ Other Benefits (life insurance, disability, wellness — typically 2-4% of salary)
+ Equipment / IT (laptop, software licenses, phone — typically $3K-8K per year)
+ Facilities (allocated rent, utilities — $5K-15K per year in office; $0-2K remote)
+ Recruiting (amortized cost of hire — typically $10K-30K for professional roles, amortized over expected tenure)
+ Training / Development ($1K-5K per year)
+ Travel (role-dependent — $0 for engineering, $5K-20K for sales)
= Fully-Loaded Annual Cost
```

**Quick multiplier by role type:**
| Role | Base Salary Multiplier | Typical Fully-Loaded Cost |
|------|----------------------|--------------------------|
| Engineering (IC) | 1.35-1.50x | Base x 1.4 + equity |
| Engineering (Manager) | 1.35-1.50x | Base x 1.4 + equity |
| Sales (AE) | 1.20-1.35x (excl. commissions) | OTE x 1.25 + equity |
| Sales (SDR/BDR) | 1.25-1.40x | OTE x 1.3 |
| Customer Success | 1.30-1.45x | Base x 1.35 |
| Marketing | 1.30-1.45x | Base x 1.35 + program spend |
| G&A (Finance, HR, Legal) | 1.30-1.45x | Base x 1.35 |
| Executive | 1.40-1.60x | Base x 1.5 + equity + perks |

### Phase 2: Hiring Plan to Budget Reconciliation

**Building the headcount budget:**

1. **Start with the operating plan:** What does the business need to accomplish?
2. **Translate to capacity:** How many people are needed to deliver that plan?
3. **Layer in timing:** When does each role need to start (accounting for ramp time)?
4. **Apply attrition:** Assume X% annual attrition and build replacement hires into the plan
5. **Cost it out:** Apply fully-loaded costs to each role with start-date timing

**Hiring plan waterfall:**
```
Approved Headcount (beginning of year)
+ Planned New Hires (from operating plan)
- Expected Attrition (historical rate x beginning headcount)
+ Backfills (for attritted roles deemed essential)
= Target Ending Headcount

Budget Impact:
  Existing Employees: [full-year cost at current comp]
  New Hires: [partial-year cost based on start date, with ramp]
  Attrition Savings: [partial-year savings based on expected departure timing]
  Merit Increases: [annual increase applied at review date]
  = Total People Cost Budget
```

**Ramp time by role (months to full productivity):**
| Role | Ramp to Full Productivity | Revenue Impact Lag |
|------|--------------------------|-------------------|
| SDR/BDR | 2-3 months | Immediate pipeline impact |
| Account Executive | 4-6 months | 6-9 months to closed revenue |
| Customer Success | 2-3 months | N/A (retention impact) |
| Engineering | 2-4 months | 3-6 months to shipped features |
| Marketing | 1-3 months | 3-6 months to pipeline impact |
| Executive | 3-6 months | 6-12 months to strategic impact |

### Phase 3: Span of Control Analysis

**Span of control = direct reports per manager**

**Benchmarks:**
| Function | Typical Span | Red Flag |
|----------|-------------|----------|
| Engineering | 5-8 | <4 (too many managers) or >10 (managers overwhelmed) |
| Sales (AE team) | 6-10 | <5 or >12 |
| Customer Success | 5-8 | >10 (quality suffers) |
| G&A | 5-8 | <4 (empire building) |
| Executive team | 6-10 | >12 (CEO bottleneck) |

**Span of control too narrow (<4):** Org is management-heavy; overhead costs elevated; decision-making may be slow due to too many layers.
**Span of control too wide (>12):** Managers cannot effectively coach, develop, or unblock their teams; quality and retention suffer.

### Phase 4: Productivity Metrics

**Revenue per employee:**
```
Revenue per Employee = Total Revenue / Average Headcount
```
| Stage | SaaS Benchmark | Services Benchmark |
|-------|---------------|-------------------|
| Early (<$10M) | $100K-200K | $80K-150K |
| Growth ($10-50M) | $150K-250K | $120K-200K |
| Scale ($50-200M) | $200K-350K | $150K-250K |
| Mature (>$200M) | $250K-500K | $180K-300K |

**Gross profit per employee:**
```
Gross Profit per Employee = Gross Profit / Average Headcount
```
- More meaningful than revenue per employee because it adjusts for cost structure
- A $200K revenue per employee with 80% gross margins ($160K GP/employee) is better than $300K revenue per employee with 40% gross margins ($120K GP/employee)

**ARR per sales rep:**
```
ARR per AE = Net New ARR / Average Quota-Carrying AE Count
```
- Benchmark: $500K-$1M for mid-market; $1M-$3M for enterprise
- Compare to OTE to assess sales efficiency: ARR per AE should be 3-5x OTE

**Engineering velocity metrics:**
- Features shipped per sprint per engineer
- Bugs per release
- R&D spend as % of revenue (SaaS benchmark: 15-25%)
- Engineering headcount as % of total (SaaS benchmark: 25-40%)

---

## Mode 4: Profitability Analysis

### Phase 1: Contribution Margin by Segment

**Segment definitions:**
- By product line (Product A, Product B)
- By customer segment (Enterprise, Mid-Market, SMB)
- By geography (North America, EMEA, APAC)
- By channel (Direct, Partner, Self-Serve)
- By customer (top 10-20 individual customers)

**Contribution margin calculation by segment:**
```
Segment Revenue
- Direct COGS (cost directly attributable to serving this segment)
- Variable S&M (commissions, channel fees specific to this segment)
= Segment Contribution Margin

Segment Contribution Margin % = Segment CM / Segment Revenue
```

**What to include in direct costs (allocate) vs. exclude (do not allocate):**
- INCLUDE: Hosting costs by product, sales commissions by deal, support costs by segment
- EXCLUDE: CEO salary, office rent (unless segment has a dedicated office), corporate marketing
- The goal is to answer: "If we shut down this segment, what costs would disappear?"

### Phase 2: Cost Allocation Methodologies

**Method 1: Direct Allocation (simplest)**
- Assign costs only to the segment that directly caused them
- Unallocated costs remain in "Corporate/Overhead"
- Best for: decision-making about segment profitability ("should we keep this segment?")
- Weakness: large unallocated bucket makes total picture incomplete

**Method 2: Step-Down Allocation (moderate complexity)**
- Allocate shared costs sequentially, starting with the department that serves the most other departments
- Example: IT costs allocated first (by headcount), then HR costs (by headcount including allocated IT), etc.
- Best for: more complete view of true cost; management reporting
- Weakness: allocation order changes the result; somewhat arbitrary

**Method 3: Activity-Based Costing / ABC (most accurate)**
- Identify cost drivers (activities) for each shared cost pool
- Allocate based on actual consumption of each activity
- Example: Support costs allocated by ticket volume per segment, not revenue
- Best for: true cost-to-serve analysis, pricing decisions
- Weakness: data-intensive, requires activity tracking

**Choosing a methodology:**
| Decision | Recommended Method |
|----------|-------------------|
| Should we keep or cut a product line? | Direct allocation (what costs disappear?) |
| What is the true cost to serve each customer segment? | ABC (what activities does each segment consume?) |
| How should we set prices? | ABC (need accurate cost-to-serve) |
| Management reporting to board | Step-down (complete but not overly complex) |
| Quick directional analysis | Direct allocation (fast, transparent) |

### Phase 3: Breakeven Analysis

**Unit-level breakeven:**
```
Breakeven Volume = Fixed Costs / Contribution Margin per Unit
```

**Company-level breakeven:**
```
Breakeven Revenue = Fixed Costs / Contribution Margin %
```

**SaaS breakeven (customer count):**
```
Breakeven Customers = Total OpEx / (ARPA x 12 x Gross Margin %)
```

**Time-to-breakeven for new initiatives:**
- Calculate cumulative investment and cumulative contribution margin
- The crossover point is breakeven
- Run `python3 tools/dcf.py` to calculate NPV of the initiative and determine if it clears the hurdle rate
- Run `python3 tools/wacc.py` for the appropriate hurdle rate

### Phase 4: Operating Leverage Analysis

**Operating leverage = the rate at which profits grow relative to revenue growth.**

```
Degree of Operating Leverage = Contribution Margin / Operating Income
```

**Incremental margin analysis (the practical version):**
```
Incremental Margin = Change in Operating Income / Change in Revenue
```
- If revenue grows $10M and operating income grows $4M, incremental margin is 40%
- This tells you: for every additional dollar of revenue, $0.40 falls to operating income
- Mature SaaS companies should show 50-70% incremental margins at scale

**Operating leverage by cost structure:**
| Cost Type | Low Revenue | High Revenue | Leverage Effect |
|-----------|-------------|-------------|-----------------|
| Variable (COGS, commissions) | Scale linearly | Scale linearly | None |
| Semi-variable (support, infra) | Step function | Step function | Moderate |
| Fixed (R&D, G&A, rent) | Full cost | Same cost | High leverage |

**Operating leverage red flags:**
- Revenue growing but margins not expanding = no operating leverage (costs scaling linearly)
- Headcount growing faster than revenue = negative leverage
- G&A growing faster than revenue = org complexity outpacing growth

---

## Mode 5: Strategic Finance

### Build vs. Buy Analysis

**Framework: Total Cost of Ownership over 3-5 years**

**Build costs:**
```
Year 0: Development Cost
  - Engineering headcount (fully-loaded) x development time
  - Infrastructure setup
  - Opportunity cost (what else could engineering build?)

Years 1-N: Ongoing Costs
  - Maintenance engineering (typically 20-30% of build team)
  - Infrastructure / hosting
  - Support and operations
  - Feature enhancements
  - Technical debt and security patches
```

**Buy costs:**
```
Year 0: Implementation
  - License/subscription fees (Year 1)
  - Implementation and integration costs
  - Data migration
  - Training

Years 1-N: Ongoing Costs
  - Annual license/subscription fees (with escalators)
  - Ongoing integration maintenance
  - Internal admin headcount
  - Customization costs
```

**Decision framework:**
1. Calculate NPV of build costs over 5 years: run `python3 tools/dcf.py`
2. Calculate NPV of buy costs over 5 years: run `python3 tools/dcf.py`
3. Compare NPVs — but cost is not the only factor
4. Score qualitative factors (0-5 scale):
   - Strategic importance (is this core to your differentiation?)
   - Speed to market (how fast do you need this?)
   - Customization needs (how unique are your requirements?)
   - Maintenance burden (can you sustain the build long-term?)
   - Vendor risk (is the vendor stable and strategic?)

**Decision rule:**
- If it is core to your competitive differentiation → lean build
- If it is commodity/utility functionality → lean buy
- If you need it in <3 months and build takes 12 → buy now, evaluate build later
- Run `python3 tools/monte_carlo.py` for scenario ranges if cost estimates are uncertain

### Pricing Optimization

**Cost-plus pricing (floor):**
```
Minimum Price = Fully-Loaded Cost to Serve x (1 + Target Margin %)
```
- This sets the floor — never price below this
- DATA NEEDED: Cost to serve per customer (from ABC analysis in Mode 4)

**Value-based pricing (ceiling):**
```
Maximum Price = Customer's Willingness to Pay (informed by value delivered)
```
- Estimate the ROI your product delivers to the customer
- Price at 10-20% of the value you create (the "10x value rule")
- Example: Your product saves the customer $100K/year → price at $10K-20K/year

**Competitive pricing (anchor):**
```
Market Price = Competitor pricing for similar functionality
```
- Price within 20% of competitors unless you have a clear differentiation story
- If pricing above competitors: articulate exactly what justifies the premium
- If pricing below: ensure you are not training the market to undervalue your category

**Pricing structure decisions:**
| Structure | Best For | Watch Out For |
|-----------|---------|---------------|
| Per seat | Predictable, easy to understand | Discourages adoption; "shelfware" risk |
| Usage-based | Aligns cost with value | Revenue volatility; harder to forecast |
| Tiered | Captures willingness to pay by segment | Tier boundaries create friction |
| Flat rate | Simple; fast sales cycle | Leaves money on table with large customers |
| Hybrid (base + usage) | Predictable base with upside | Complexity in quoting and billing |

### Market Sizing for New Initiatives

**Bottom-up sizing (always preferred):**
```
TAM = Total Addressable Customers x ACV
SAM = Addressable Customers in Your Segments x Realistic ACV
SOM = SAM x Expected Penetration Rate (years 1-3)
```

**Key principle:** A market size number is useless without the assumptions behind it. Always show the build-up.

**Penetration rate benchmarks (for new product lines):**
| Year | Optimistic | Base | Conservative |
|------|-----------|------|-------------|
| Year 1 | 3-5% | 1-2% | 0.5-1% |
| Year 2 | 8-12% | 4-6% | 2-3% |
| Year 3 | 15-20% | 8-12% | 4-6% |

### ROI Framework for Investments

**NPV approach (preferred for large investments):**
1. Estimate incremental cash flows (revenue gains + cost savings - investment costs)
2. Determine the appropriate discount rate: run `python3 tools/wacc.py`
3. Calculate NPV: run `python3 tools/dcf.py` with the incremental cash flows
4. Decision rule: invest if NPV > 0 and IRR > hurdle rate

**Payback period approach (for smaller investments):**
```
Payback Period = Initial Investment / Annual Net Cash Benefit
```
- Simple and intuitive but ignores time value of money and cash flows beyond payback
- Use as a secondary metric alongside NPV, not as the primary decision tool

**Lease vs. buy (for capital equipment or real estate):**
- Run `python3 tools/loan_amort.py` to model the buy scenario (loan payments, interest, depreciation)
- Compare NPV of lease payments vs. NPV of buy costs (including maintenance, insurance, residual value)
- Factor in: tax treatment, balance sheet impact, flexibility value

**Scenario analysis for all investment decisions:**
- Run `python3 tools/monte_carlo.py` with key assumptions as random variables
- Report: P10 (downside), P50 (base), P90 (upside) NPV
- Decision rule: invest if P50 NPV > 0 AND P10 NPV is an acceptable loss

---

## Tool Integration

| When the analysis needs... | Run this | Example |
|--------------------------|---------|---------|
| NPV for build vs. buy | `python3 tools/dcf.py --fcf -500,100,200,300,350 --wacc 0.12 --terminal-growth 0.02 --shares 1` | NPV of incremental cash flows |
| Scenario ranges for projections | `python3 tools/monte_carlo.py --initial 1000000 --return 0.5 --vol 0.3 --years 3 --sims 10000` | Percentile ranges for revenue/cost |
| Lease vs. buy comparison | `python3 tools/loan_amort.py --principal 500000 --rate 0.06 --years 5 --frequency monthly` | Amortization schedule and total interest |
| Hurdle rate for investments | `python3 tools/wacc.py --equity 800 --debt 200 --tax 0.25 --rf 0.04 --beta 1.1 --erp 0.055 --cost-of-debt 0.05` | WACC as discount rate |
| Full valuation for strategic options | `python3 tools/dcf.py --fcf 10,15,20,25,30 --wacc 0.10 --terminal-growth 0.03 --shares 100` | Enterprise and equity value |

---

## Output Specifications

### Unit Economics Dashboard
See Mode 1 template above. Output as formatted text block with all metrics, comparatives, and benchmarks.

### SaaS Metrics Report
See Mode 2 template above. Output as formatted text block with ARR bridge, retention metrics, and efficiency metrics.

### Headcount Model
Output as structured table:
```
DEPARTMENT | Current HC | Planned Hires | Attrition | Year-End HC | Fully-Loaded Cost
Engineering |    XX      |      XX       |    XX     |     XX      |    $X.XM
Sales       |    XX      |      XX       |    XX     |     XX      |    $X.XM
...
TOTAL       |    XX      |      XX       |    XX     |     XX      |    $XX.XM
```

### Build vs. Buy Analysis
Output as side-by-side NPV comparison with qualitative scoring matrix.

### Profitability Analysis
Output as contribution margin waterfall by segment with allocation methodology clearly stated.

---

## Quality Gates & Completion Criteria

- [ ] All unit economics use fully-loaded costs, not just direct costs
- [ ] All SaaS metrics use correct calculation methodology (especially NDR — must exclude new customers)
- [ ] All benchmarks are contextualized by stage and industry (not one-size-fits-all)
- [ ] Headcount models include fully-loaded cost, not just base salary
- [ ] Profitability analyses clearly state which cost allocation methodology was used and why
- [ ] Strategic finance deliverables include NPV analysis with explicit discount rate justification
- [ ] All metrics show trends (minimum 4 periods) not just current-period snapshots
- [ ] Assumptions are explicit and testable, not hidden in formulas
- [ ] Data gaps are flagged clearly — never fill gaps with fabricated numbers
- [ ] Every analysis ties back to a specific decision ("this tells us whether we should...")

**Success metric:** A CFO reading the analysis should be able to make a confident decision based on the output alone, with full visibility into methodology, assumptions, and sensitivity.

**Escalation triggers:**
- User is calculating LTV using gross revenue instead of gross-margin-adjusted revenue → correct the methodology
- User is using blended CAC when channel-level CAC varies by >2x → insist on channel-level analysis
- Headcount model uses base salary only → require fully-loaded cost calculation
- Profitability analysis allocates corporate overhead to segments for a shut-down decision → use direct allocation only
- User wants to present vanity metrics (downloads, registered users) as unit economics → redirect to revenue-based metrics

---

## Hard Constraints

- **NEVER** fabricate benchmark data, financial figures, or metric values
- **NEVER** calculate LTV without adjusting for gross margin — gross-revenue LTV overstates value by 20-40%
- **NEVER** present blended CAC when channel-level economics diverge significantly (>2x spread)
- **NEVER** use base salary as headcount cost — always compute fully-loaded cost
- **NEVER** allocate fixed corporate overhead to segments when the decision is whether to keep or cut a segment (use direct allocation for shut-down decisions)
- **ALWAYS** show the trend, not just the current value (minimum 4 periods)
- **ALWAYS** state the cost allocation methodology used and justify the choice
- **ALWAYS** include sensitivity analysis for any projection or NPV calculation
- **ALWAYS** benchmark metrics against stage-appropriate and industry-appropriate peers
- If the user provides metrics that are mathematically inconsistent (e.g., NDR and churn that do not reconcile), **require** reconciliation before proceeding

---

## Common Pitfalls

1. **Vanity metrics masquerading as unit economics:** "We have 500K registered users" is not a unit economic. Revenue, retention, and cost per unit are unit economics. Registered users, app downloads, and social media followers are vanity metrics unless tied to monetization. Always ask: "Does this metric predict or measure revenue?"

2. **Ignoring fully-loaded costs:** A $150K engineer actually costs $200K-$225K when you include payroll taxes, benefits, equipment, facilities, and recruiting amortization. Using base salary in models understates costs by 30-50% and produces wildly optimistic ROI calculations.

3. **Blended metrics hiding segment problems:** A blended CAC of $5,000 looks fine until you discover SMB CAC is $1,000 (good) and Enterprise CAC is $50,000 (possibly bad). Blended metrics are useful for headlines but dangerous for decisions. Always decompose.

4. **LTV calculated to infinity:** Using LTV = ARPA / Churn with a 2% monthly churn rate gives LTV = 50 months of ARPA. But you have 18 months of data. You are projecting customer behavior 32 months beyond your observation window. Cap LTV at 3-5 years or use cohort-based LTV with observed data.

5. **NDR calculated incorrectly:** The most common error is including new customers in the NDR calculation. NDR measures how much revenue you keep and grow FROM EXISTING customers. New customer revenue must be excluded from both the numerator and denominator.

6. **Confusing operating leverage with cost cutting:** Operating leverage means margins expand as revenue grows because fixed costs are spread over more revenue. Cost cutting improves margins at any revenue level. Both improve margins but they have different implications for growth sustainability.

7. **Build vs. buy based on cost alone:** The cheapest option is not always the right option. A build that saves $200K NPV but takes 12 months and consumes your best engineers might cost you $2M in delayed product roadmap. Always include opportunity cost and strategic value.

8. **Market sizing top-down:** "The $50B market times 1% penetration equals $500M" is not analysis. Bottom-up: count the customers, multiply by realistic ACV, apply achievable penetration rates, and show your work.

---

## Related Skills

- For board presentations using these metrics → `/board-deck`
- For budget construction and expense planning → `/budget`
- For revenue forecasting models → `/forecast`
- For fundraising presentations → `/pitch-deck`
- For valuation analysis → `/lbo` or run DCF tools directly
- For detailed venture-stage analysis → `/venture-capital`
