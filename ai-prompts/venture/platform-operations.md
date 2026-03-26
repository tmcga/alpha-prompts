# Portfolio Operations -- Platform Team

```
You are the Head of Platform at a top-tier venture capital firm, responsible
for driving operational value creation across a portfolio of 40+ companies
ranging from seed to pre-IPO. Your team of 15+ functional experts covers
go-to-market strategy, talent and recruiting, board governance, financial
operations, and strategic partnerships. You have operated as a VP or C-level
executive at two venture-backed companies (one acquired, one IPO) before
joining the fund side. You combine pattern recognition across hundreds of
portfolio companies with hands-on operating experience. You know what "good"
looks like at every stage, and you help founders avoid the mistakes that kill
companies between product-market fit and scale.
```

## What This Desk Does

The platform operations team is the value-creation engine of a venture capital firm, working directly with portfolio company founders and executives to accelerate growth, improve operational efficiency, and prepare for exits. Unlike the investment team (which selects companies), the platform team makes those companies more valuable after the check is written. The team operates across five functional areas: go-to-market strategy, talent and recruiting, board governance, financial operations, and strategic partnerships. The best platform teams create a measurable "portfolio premium" -- companies backed by the fund outperform comparable companies on key operational metrics. This work is both reactive (responding to specific company needs) and proactive (identifying common failure modes and intervening before problems escalate).

---

## 1. Go-to-Market Strategy

Go-to-market (GTM) strategy is the most common area where early and growth-stage companies need operational support. The right GTM motion depends on the product, customer segment, price point, and competitive dynamics.

```
Design a go-to-market strategy for [COMPANY_NAME], a [STAGE] company selling
[PRODUCT_DESCRIPTION] to [CUSTOMER_SEGMENT] at an ACV of $[PRICE]:

GTM MOTION SELECTION:
Evaluate which motion is the best fit:

1. Enterprise Sales (ACV > $50K):
   - Sales cycle length: [MONTHS]
   - Required: outbound SDR team, AE team, SE team, CS team
   - Typical ramp time for new AE: [MONTHS]
   - Target quota per AE: $[X]K ARR (benchmark: 4-5x OTE)
   - Org structure: SDR -> AE -> SE -> CS -> AM

2. Product-Led Growth (ACV < $10K or usage-based):
   - Free tier / freemium / free trial: [RECOMMENDATION]
   - Self-serve conversion rate benchmark: [X]%
   - Viral coefficient targets: k > [VALUE]
   - PLG metrics: Time to value, activation rate, PQL conversion
   - Org structure: Growth eng -> Product -> PLG Sales (PLS)

3. Marketplace / Transactional:
   - Supply vs. demand side: Which is harder to acquire?
   - Liquidity metrics: [MATCH_RATE/FILL_RATE/UTILIZATION]
   - Take rate: [X]% (benchmark for [CATEGORY])
   - Chicken-and-egg strategy: [SUPPLY_FIRST/DEMAND_FIRST/SIMULTANEOUS]

CHANNEL STRATEGY:
- Direct vs. channel vs. partner-led: [RECOMMENDATION]
- If channel: target partner types, margin structure, enablement plan
- If partner-led: API/integration strategy, co-sell motions

PRICING STRATEGY:
- Pricing model: [SEAT_BASED/USAGE_BASED/FLAT_RATE/HYBRID/OUTCOME_BASED]
- Pricing tiers: [DETAILS]
- Land-and-expand mechanics: What triggers expansion revenue?
- Competitive pricing benchmark: [COMPARISON]

METRICS AND MILESTONES:
Define success metrics for the next [12/18/24] months:
  - Month 3: [MILESTONE]
  - Month 6: [MILESTONE]
  - Month 12: [MILESTONE]
  - Month 18: [MILESTONE]

What is the expected cost to build the GTM engine to $[TARGET]M ARR?
Model headcount, compensation, tools, and marketing spend.
```

```
[COMPANY_NAME] is transitioning from [CURRENT_MOTION] to [NEW_MOTION] (e.g.,
from founder-led sales to a scalable sales organization, or from enterprise
to PLG, or from direct to channel).

Diagnose the current state:
- Current pipeline generation: [X]% inbound vs. [Y]% outbound
- Current win rate: [Z]%
- Current sales cycle: [N] days
- Current CAC: $[A]
- Current LTV/CAC: [B]x

Design the transition plan:
1. Hiring plan: Roles, sequence, and timeline for the first [N] hires
2. Compensation design: Base, variable, quota, OTE ratios for each role
3. Sales enablement: Playbook, training, tools (CRM, sequencing, analytics)
4. Marketing alignment: What demand gen changes support the new motion?
5. Metrics to track: Leading indicators that the transition is working

What are the top 3 risks in this transition and how do you mitigate them?
```

### LTV/CAC Framework

```
Customer Lifetime Value:
  LTV = ARPA * Gross Margin% / Monthly Churn Rate

  or (for expanding customers):
  LTV = ARPA * Gross Margin% * (1 / (1 - NDR_monthly))
  where NDR_monthly = Net Dollar Retention on a monthly basis

Customer Acquisition Cost:
  CAC = (S&M Spend in Period) / (New Customers Acquired in Period)

  Fully-loaded CAC includes: salaries, commissions, marketing spend,
  tools, allocated overhead

LTV/CAC Ratio:
  Target: > 3x (good), > 5x (excellent)
  Below 1x: losing money on every customer
  Above 10x: possibly underinvesting in growth

CAC Payback Period:
  Payback = CAC / (ARPA * Gross Margin%)
  Target: < 18 months (good), < 12 months (excellent)

Sales Efficiency (Magic Number):
  Magic Number = Net New ARR (Q) / S&M Spend (Q-1)
  Target: > 0.75 (good), > 1.0 (excellent)
  Below 0.5: GTM engine is inefficient

Burn Multiple:
  Burn Multiple = Net Burn / Net New ARR
  Target: < 2x (good), < 1x (excellent)
  Above 3x: unsustainable burn
```

---

## 2. Talent and Recruiting

```
Design a talent strategy for [COMPANY_NAME], currently at [N] employees,
targeting [M] employees in [TIMEFRAME]:

EXECUTIVE SEARCH:
- Open executive roles: [LIST]
- For each role, define:
  - Ideal candidate profile (experience, stage, domain)
  - Must-have vs. nice-to-have qualifications
  - Compensation range: Base $[X-Y]K, Equity [A-B]% (benchmark for [STAGE])
  - Search approach: [RETAINED_SEARCH/NETWORK/INTERNAL_PROMOTE]
  - Timeline to hire: [WEEKS]
  - Interview process: [STAGES_AND_EVALUATORS]

COMPENSATION BENCHMARKING:
- Compare [COMPANY_NAME]'s compensation philosophy to market:
  - Cash percentile target: [X]th (benchmark: 50th for seed, 50-75th for
    Series B+)
  - Equity percentile target: [X]th (higher equity for earlier stage)
  - Total compensation positioning vs. [FAANG/STARTUP/INDUSTRY] benchmarks

Equity guidelines by level and stage:
  | Role           | Seed      | Series A  | Series B  | Series C+ |
  | VP Eng         | 1.0-2.5%  | 0.5-1.5%  | 0.25-0.75%| 0.1-0.4%  |
  | VP Sales       | 0.75-2.0% | 0.4-1.0%  | 0.2-0.5%  | 0.1-0.3%  |
  | VP Product     | 0.75-2.0% | 0.4-1.0%  | 0.2-0.5%  | 0.1-0.3%  |
  | Director       | 0.25-0.75%| 0.1-0.4%  | 0.05-0.2% | 0.02-0.1% |
  | Senior IC      | 0.1-0.5%  | 0.05-0.25%| 0.02-0.1% | 0.01-0.05%|

ORG DESIGN:
- Current org structure: [DESCRIPTION]
- Recommended changes for the next [12/18] months
- Span of control guidelines: [5-8] direct reports per manager
- Key hires that are blocking growth: [ROLES]
- Org scaling benchmarks:
  - 1-10: Founders do everything, no middle management
  - 10-30: First functional leads, lightweight process
  - 30-75: VPs hired, team structure solidifies, first HR hire
  - 75-150: Directors layer added, formal performance management
  - 150-300: SVPs/C-suite fills out, BU structure considered
  - 300+: Full executive team, formal planning cadence, L&D function

CULTURE AND RETENTION:
- Attrition rate: [X]% (voluntary) -- benchmark: <15% for healthy startup
- Top performer retention rate: [Y]%
- Employee NPS or engagement score: [VALUE]
- Key retention risks: [INDIVIDUALS_OR_TEAMS]
- Recommended retention levers: [EQUITY_REFRESH/PROMOTION/SCOPE/COMP]
```

---

## 3. Board Governance

```
Design or evaluate the board governance structure for [COMPANY_NAME] at
[STAGE]:

BOARD COMPOSITION:
- Current board: [LIST_WITH_ROLES: Founder, Investor, Independent]
- Recommended composition by stage:
  - Seed: 3 members (2 founders + 1 lead investor)
  - Series A: 3-5 members (1-2 founders + 1-2 investors + 0-1 independent)
  - Series B: 5 members (1-2 founders + 2 investors + 1-2 independent)
  - Series C+: 5-7 members (1-2 management + 2-3 investors + 2-3 independent)
  - Pre-IPO: 7-9 members (majority independent for NYSE/NASDAQ compliance)

- Observer seats: [LIST] -- who has observation rights?
- Independent director candidates: [SUGGESTIONS] based on company needs
  (industry expertise, public company experience, functional depth)
- Committee structure (Series C+):
  - Audit committee: [MEMBERS] -- at least 1 financial expert
  - Compensation committee: [MEMBERS] -- all independent
  - Nominating/governance committee: [MEMBERS]

MEETING CADENCE AND STRUCTURE:
- Frequency: [MONTHLY/BIMONTHLY/QUARTERLY] (recommend monthly through
  Series A, bi-monthly Series B, quarterly Series C+)
- Meeting duration: [HOURS]
- Recommended agenda structure:
  1. CEO update and key decisions (30 min)
  2. Financial review (20 min)
  3. Strategic topic deep-dive (45 min, rotating: product, GTM, people, etc.)
  4. Closed session (15 min, without management)

INFORMATION RIGHTS:
- Monthly reporting package: [METRICS_LIST]
- Board deck delivery: [DAYS] before meeting
- Financial statements: Monthly P&L, balance sheet, cash flow, budget vs.
  actual
- KPI dashboard: [KEY_METRICS_BY_FUNCTION]
- Annual operating plan: Reviewed and approved by board in [MONTH]
- Investor update (broader syndicate): [MONTHLY/QUARTERLY], [CONTENTS]

PROTECTIVE PROVISIONS:
- Standard investor protective provisions to evaluate:
  - Issuance of new equity
  - Changes to authorized shares
  - Amendments to charter or bylaws
  - Acquisitions, mergers, or asset sales
  - Incurrence of debt above $[THRESHOLD]
  - Change in board size
  - Dividends or distributions
  - Related party transactions

Which provisions are appropriate for [STAGE]? Flag any that are overly
restrictive for the company's operational needs.
```

---

## 4. Financial Operations

```
Assess and improve the financial operations function at [COMPANY_NAME]:

BUDGETING AND FORECASTING:
- Current state: [AD_HOC/ANNUAL_BUDGET/QUARTERLY_REFORECAST/MONTHLY_ROLLING]
- Recommended cadence:
  - Annual operating plan: Built in [MONTH], board-approved
  - Quarterly reforecast: Update assumptions, reproject full year
  - Monthly actuals vs. budget review: Within [N] business days of month end
  - 13-week cash flow forecast: Updated weekly

- Budget model structure:
  - Revenue: [BOTTOMS_UP/TOPS_DOWN/HYBRID] -- by segment, product, geography
  - Headcount: By department, start date, fully loaded cost
  - Non-headcount opex: By category, fixed vs. variable
  - Capital expenditure: By project
  - Cash flow: Operating, investing, financing activities

KPI DASHBOARD:
Design a KPI dashboard for a [STAGE] [BUSINESS_MODEL] company:

  REVENUE AND GROWTH:
  - ARR / MRR and growth rate (MoM, QoQ, YoY)
  - Net new ARR by source (new, expansion, churn, contraction)
  - Pipeline coverage ratio: [X]x

  UNIT ECONOMICS:
  - CAC, LTV, LTV/CAC, payback period
  - Gross margin (blended and by product/segment)
  - Contribution margin by customer cohort

  ENGAGEMENT AND RETENTION:
  - Logo retention and net dollar retention
  - DAU/WAU/MAU (for product-led businesses)
  - NPS or CSAT score

  FINANCIAL HEALTH:
  - Cash balance and runway (months)
  - Monthly burn rate (gross and net)
  - Burn multiple

  PEOPLE:
  - Headcount (actual vs. plan)
  - Attrition rate
  - Open roles and time-to-fill

FUNDRAISING PREPARATION:
- Timeline: Begin preparation [6] months before targeted fundraise
- Key workstreams:
  1. Financial model: 3-year projection with scenario analysis
  2. Data room organization: [CHECKLIST]
  3. Metrics narrative: How to present the company's story through numbers
  4. Investor targeting: [N] targets across [TIERS]
  5. Materials: Deck, memo, financial model, customer references
- Data room checklist:
  - Corporate documents (charter, bylaws, board minutes)
  - Cap table (fully diluted, including all instruments)
  - Financial statements (audited if available)
  - Customer contracts (top 10-20)
  - Employee census and option grants
  - IP documentation (patents, trademarks)
  - Material contracts (vendors, partners, leases)
  - Litigation or regulatory matters
```

---

## 5. Strategic Partnerships

```
Evaluate and design a strategic partnership strategy for [COMPANY_NAME]:

PARTNERSHIP TYPES AND PRIORITIZATION:

1. Technology / API Partnerships:
   - Integration partners: [LIST] -- which platforms do target customers
     already use?
   - API strategy: Build [INBOUND/OUTBOUND/BIDIRECTIONAL] integrations
   - Technical investment required: [ENGINEERING_WEEKS] per integration
   - Expected revenue impact: [X]% of new deals influenced by integration
   - Marketplace listing strategy: [SALESFORCE_APPEXCHANGE/AWS_MARKETPLACE/
     GOOGLE_WORKSPACE/OTHER]

2. Distribution Partnerships:
   - Channel partners: [VARS/SYSTEM_INTEGRATORS/CONSULTANCIES/DISTRIBUTORS]
   - Partner economics: [REFERRAL_FEE/RESELLER_MARGIN/REVENUE_SHARE]
   - Typical partner margin: [X-Y]% (benchmark: 20-40% for resellers)
   - Partner enablement investment: Training, certification, co-marketing
   - Expected pipeline from channel: [X]% of total pipeline at maturity

3. Co-Marketing Partnerships:
   - Co-marketing candidates: [LIST] -- complementary (not competitive)
     products targeting same buyer
   - Joint activities: Webinars, case studies, events, content
   - Lead sharing mechanics: [DETAILS]
   - Investment: [BUDGET] and [HEADCOUNT] allocation

4. Strategic / Corporate Partnerships:
   - Potential strategic partners: [LARGE_COMPANIES] that could be:
     - Major customers (land a lighthouse account)
     - Distribution channels (embed in their platform)
     - M&A acquirers (build a relationship early)
   - Deal structure: [PILOT/POC/LICENSE/JOINT_DEVELOPMENT/INVESTMENT]
   - Risks: Dependency on single partner, IP concerns, exclusivity traps

PARTNERSHIP EVALUATION FRAMEWORK:
For each proposed partnership, score (1-5):
  - Revenue impact: Direct or influenced revenue potential
  - Strategic value: Brand, credibility, market access
  - Effort required: Engineering, sales, legal, management time
  - Risk: Dependency, competitive concerns, execution complexity
  - Timeline to value: Months to meaningful revenue or strategic impact

Priority = (Revenue Impact + Strategic Value) / (Effort + Risk)

Recommend the top 3 partnerships to pursue in the next [6/12] months,
with a resource plan and success metrics for each.
```

### Org Scaling Benchmarks

```
Revenue per employee benchmarks by stage:

  Seed - Series A:     $50-150K ARR per employee
  Series B:            $100-200K ARR per employee
  Series C:            $150-250K ARR per employee
  Pre-IPO:             $200-350K ARR per employee
  Public (scaled):     $250-500K ARR per employee

Department headcount as % of total (Series B-C SaaS):
  Engineering:         25-35%
  Sales:               20-30%
  Marketing:           5-10%
  Customer Success:    10-15%
  G&A:                 10-15%
  Product:             5-10%

Sales team ratios:
  SDR:AE ratio:        2:1 to 3:1
  AE:SE ratio:         3:1 to 5:1
  AE:CSM ratio:        3:1 to 5:1
  Manager:IC ratio:    1:5 to 1:8

Hiring velocity benchmarks:
  Time-to-fill (engineering):    45-75 days
  Time-to-fill (sales):         30-60 days
  Time-to-fill (executive):     60-120 days
  Recruiter capacity:            3-5 hires/month per recruiter
  Offer acceptance rate:         75-85% (target)
```

---

## See Also

- [Early-Stage Investing](early-stage.md) -- Post-seed operational needs
- [Growth-Stage Investing](growth-stage.md) -- Scaling metrics and IPO preparation
- [Crypto / Web3](crypto-web3.md) -- Community and developer ecosystem building
- [Biotech / Healthcare](biotech-healthcare.md) -- Regulatory affairs support
- [Venture Overview](README.md) -- Fund-level platform strategy
- [Private Capital](../private-capital/) -- Operating partner frameworks
