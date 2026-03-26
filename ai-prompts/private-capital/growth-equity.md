# Growth Equity

Prompt templates for growth-stage investing, covering unit economics analysis, revenue quality assessment, minority governance protections, path-to-profitability modeling, and hybrid growth/buyout strategies.

## Role Context

```
You are a principal at a growth equity fund ($2B AUM) investing $30M-$150M per deal in
companies with $20M-$200M+ revenue growing 20-60%+ annually. You take minority or light-
majority positions, typically without leverage. Your edge is pattern recognition across
hundreds of high-growth companies — you know which SaaS metrics actually predict durable
growth, which unit economics are sustainable, and when a company is ready to scale vs.
still searching for product-market fit. You care deeply about revenue quality (recurring
vs. one-time), capital efficiency (burn multiple), and governance protections that protect
your downside in a minority position. Your return target is 3-5x MOIC over 4-6 years,
driven almost entirely by revenue growth and multiple re-rating, not leverage.
```

For foundational PE frameworks and due diligence checklists, see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below focus on growth-specific metrics, governance, and profitability modeling.

---

## 1. Unit Economics Deep Dive

### LTV/CAC and Cohort Analysis

```
Analyze the unit economics for [company name], a [SaaS / marketplace / D2C / fintech] business:

Customer acquisition data:
- Total customers: [X]
- New customers added (last 12 months): [X]
- Blended CAC (fully loaded: sales + marketing + onboarding): $[X]
- CAC by channel: [paid search $X, outbound sales $X, organic/referral $X, partnerships $X]
- Sales cycle length: [X] months
- CAC payback period (months to recover acquisition cost from gross profit): [X] months

Revenue per customer:
- Average contract value (ACV): $[X]
- Gross margin on revenue: [X]%
- Gross profit per customer per year: $[X]

Retention and expansion:
- Logo retention rate: [X]% (annual)
- Net revenue retention (NRR): [X]%
- Expansion revenue sources: [upsell, cross-sell, price increases, usage growth]
- Average customer lifespan (implied by churn): [X] years

Calculate and assess:

1. **LTV calculation**:
   LTV = (ACV x Gross Margin) / (1 - Net Revenue Retention)
   Or for discrete cohorts: sum of discounted gross profit per cohort over observed lifetime
   LTV = $[X]

2. **LTV/CAC ratio**:
   LTV / CAC = [X]x
   Benchmark: > 3x is healthy, > 5x suggests underinvestment in growth
   If LTV/CAC < 3x, identify whether the problem is CAC (too high) or LTV (churn too high)

3. **Payback period**:
   Months to recover CAC = CAC / (Monthly gross profit per customer)
   Target: < 18 months for SaaS, < 12 months for transactional businesses
   Current: [X] months

4. **Cohort analysis**:
   - Show revenue retention curves by quarterly cohort (last 8-12 cohorts)
   - Is NRR improving, stable, or declining across cohorts?
   - Are newer cohorts better or worse than older ones? (product-market fit trajectory)
   - Separate logo churn from revenue churn (losing small customers is different from losing large ones)

5. **Unit economics by segment**:
   - Enterprise vs. mid-market vs. SMB: which segment has best LTV/CAC?
   - By geography: domestic vs. international
   - By product line: core product vs. add-ons
   - Where should incremental sales dollars be allocated?
```

### Contribution Margin Analysis

```
Break down the contribution margin stack for [company]:

Revenue: $[X]M

Level 1 — Gross Profit:
- COGS: hosting/infrastructure $[X]M, customer support $[X]M, professional services $[X]M
- Gross margin: [X]%
- Gross margin trend (last 8 quarters): [improving / stable / declining]
- Path to target gross margin of [X]%: what needs to change?

Level 2 — Contribution Margin (after variable S&M):
- Variable S&M: sales commissions $[X]M, performance marketing $[X]M
- Contribution margin: [X]%
- This measures whether each incremental dollar of revenue is profitable

Level 3 — Operating Margin (after all opex):
- R&D: $[X]M ([X]% of revenue)
- G&A: $[X]M ([X]% of revenue)
- Remaining S&M (fixed): $[X]M ([X]% of revenue)
- Operating margin: [X]%

Key questions:
1. Is contribution margin positive? If not, the business model may not work at any scale.
2. What's the natural operating leverage? As revenue grows [X]%, how much does each opex
   line grow? (R&D should grow slower than revenue, G&A much slower)
3. What does the steady-state margin profile look like at $[X]M revenue?
4. Compare to public comps at similar scale: [list 3-5 companies and their margins at this revenue level]
```

---

## 2. Revenue Quality Assessment

### ARR Quality and Durability

```
Assess the quality and durability of [company]'s $[X]M ARR:

Revenue composition:
- Recurring revenue: [X]% of total (subscriptions, contracts, retainers)
- Recurring but variable: [X]% (usage-based, consumption, transaction fees)
- Non-recurring: [X]% (professional services, one-time implementation, hardware)

ARR quality metrics:
- ARR: $[X]M (define: committed annual recurring revenue as of [date])
- ARR growth rate: [X]% YoY
- Net new ARR this quarter: $[X]M (= new ARR + expansion - contraction - churn)
- Quarterly ARR build:
  Beginning ARR: $[X]M
  + New logo ARR: $[X]M
  + Expansion ARR: $[X]M
  - Contraction ARR: $[X]M
  - Churned ARR: $[X]M
  = Ending ARR: $[X]M

Durability assessment:
1. **Contract structure**: Average contract length [X] years, % multi-year [X]%,
   auto-renewal rate [X]%, weighted average remaining contract term [X] years
2. **Revenue concentration**: Top 10 customers = [X]% of ARR. If any single customer > 10%,
   what is the contract term and renewal risk?
3. **Net Revenue Retention by cohort**: [show quarterly NRR for last 8 quarters]
   Trend: [improving/stable/declining]. If declining, why?
4. **Gross retention vs. net retention**:
   Gross retention: [X]% (measures churn only, no expansion)
   Net retention: [X]% (includes expansion)
   Gap between gross and net = expansion engine health
5. **Logo retention**: [X]% (losing many small logos matters less than losing a few large ones)

Red flags to investigate:
- NRR declining quarter-over-quarter
- Large customer concentration with near-term renewal dates
- Professional services > 20% of revenue (low margin, not scalable)
- Channel partner dependency (reseller concentration)
- Usage-based revenue at risk of volume decline in downturn
```

### Revenue Multiple Regression

```
Help me determine the appropriate revenue multiple for [company] using a regression framework:

Company metrics:
- ARR: $[X]M
- ARR growth rate: [X]%
- Net revenue retention: [X]%
- Gross margin: [X]%
- Rule of 40 score: [growth rate + FCF margin] = [X]
- FCF margin: [X]%
- TAM: $[X]B

Comparable public companies (provide for each):
| Company | ARR Growth | NRR | Gross Margin | Rule of 40 | EV/NTM Revenue |
|---------|-----------|-----|--------------|-----------|----------------|
| [Comp 1]| [X]%     | [X]%| [X]%        | [X]       | [X]x          |
| [Comp 2]| ...      | ... | ...          | ...       | ...            |

Run a regression analysis:
1. **Primary driver**: EV/Revenue = f(Revenue Growth Rate)
   Typically: each 1pp of growth ≈ 0.2-0.5x of EV/Revenue multiple
2. **Adjusted for profitability**: Add Rule of 40 score as explanatory variable
3. **Adjusted for retention**: NRR > 120% commands premium; NRR < 100% is a discount
4. **Implied growth rate from multiple**:
   If market prices [company] at [X]x revenue, what growth rate is implied?
   Formula: Implied growth ≈ (EV/Revenue - Intercept) / Slope coefficient

Apply private company discount:
- Illiquidity discount: 15-30% below public comparables
- Size discount: if smaller than smallest public comp, additional 10-20%
- Control premium (if majority deal): +10-20% for control
- Implied fair value range: [X]x - [X]x NTM revenue = $[X]M - $[X]M enterprise value
```

---

## 3. Governance and Minority Protections

### Term Sheet Governance Provisions

```
I'm negotiating a $[X]M minority growth equity investment for [X]% of [company].
The company has [X] existing investors and is [pre-profit / recently profitable].

Draft and evaluate the key governance and protective provisions:

1. **Board representation**:
   - Board seats: [X] total. We get [X] seat(s), founder has [X], independent [X]
   - Board observer rights if no seat
   - Board approval thresholds for: budget, M&A, debt > $[X]M, executive hiring/firing,
     equity issuance, related-party transactions

2. **Information rights**:
   - Monthly financials within [X] days of month-end
   - Annual audited financials within [X] days of year-end
   - Annual budget and operating plan by [date]
   - Cap table and option pool updates quarterly
   - Right to inspect books and records with reasonable notice

3. **Anti-dilution protection**:
   - Broad-based weighted average anti-dilution (standard)
   - Full ratchet (aggressive — when is this justified?)
   - Pay-to-play: if we don't participate in future rounds, convert to common?

4. **Pro-rata rights**:
   - Right to maintain ownership % in future financing rounds
   - Super pro-rata: right to increase ownership up to [X]%
   - Preemptive rights on any new equity issuance

5. **Liquidity protections**:
   - Drag-along: majority can force sale after [X] years (protect against founder holdout)
   - Tag-along: we participate pro-rata in any founder secondary sale
   - Demand registration rights after [X] years
   - Put option or redemption right after [X] years at fair market value
   - Liquidation preference: [1x non-participating / 1x participating with cap / other]

6. **Negative covenants (consent rights)**:
   - No issuance of senior equity without our consent
   - No change of control / sale below $[X]M without our consent
   - No amendment to charter that adversely affects our rights
   - No related-party transactions above $[X] without board approval
   - No change to capital return policy without our consent

For each provision, rate as: [standard / aggressive / should push harder].
```

---

## 4. Path to Profitability Modeling

### Rule of 40 and Burn Multiple Analysis

```
Model the path to profitability for [company]:

Current state:
- ARR: $[X]M, growing [X]%
- Gross margin: [X]%
- Operating expenses: $[X]M
  - R&D: $[X]M ([X]% of revenue)
  - S&M: $[X]M ([X]% of revenue)
  - G&A: $[X]M ([X]% of revenue)
- Operating loss: ($[X]M)
- FCF: ($[X]M)
- Cash on hand: $[X]M
- Monthly burn: $[X]M
- Cash runway: [X] months

Efficiency metrics:
1. **Rule of 40**: Revenue growth rate + FCF margin = [X]
   Current: [X]% growth + ([X]%) FCF margin = [X]
   Target: > 40 to command premium valuation
   Path: if growth decelerates to [X]%, need FCF margin of [X]% to hit Rule of 40

2. **Burn multiple**: Net burn / Net new ARR = [X]x
   Current: $[X]M burn / $[X]M net new ARR = [X]x
   Benchmark: < 1.0x is excellent, 1-2x is acceptable, > 2x is concerning
   This measures: how much cash do we burn to generate each dollar of new ARR?

3. **Magic number**: Net new ARR / Prior quarter S&M spend = [X]
   Current: [X]. Benchmark: > 0.75 means efficient go-to-market, scale aggressively
   If < 0.5, the GTM engine needs fixing before scaling

4. **Cash runway scenarios**:
   Scenario A — maintain current growth rate:
   - Monthly burn continues at $[X]M → cash out in [X] months
   - Requires $[X]M raise by [date]

   Scenario B — moderate growth to reach breakeven:
   - Reduce ARR growth to [X]% by cutting S&M by [X]%
   - Reach cash flow breakeven in [X] months with $[X]M remaining cash

   Scenario C — aggressive cuts to extend runway:
   - Cut to [X] headcount, reduce burn to $[X]M/month
   - Reach profitability in [X] months
   - But growth slows to [X]%, damaging the multiple

5. **Optimal path**: What growth/profitability combination maximizes enterprise value?
   EV = NTM Revenue x Multiple, where Multiple = f(growth, Rule of 40)
   If slowing growth from [X]% to [X]% improves FCF margin by [X]pp,
   does the Rule of 40 improvement offset the growth deceleration in the multiple?
```

---

## 5. Growth vs. Buyout Hybrid

### Majority Growth and Secondary Analysis

```
Evaluate a hybrid growth/buyout transaction for [company]:

Scenario: Founder owns [X]% and wants partial liquidity. Company has $[X]M ARR growing
[X]% with [X]% EBITDA margin (recently profitable). We are considering:

Option A — Minority growth investment:
- Invest $[X]M for [X]% (all primary capital into the business)
- No leverage, founder retains control
- Our return depends entirely on growth and multiple re-rating
- Limited ability to influence strategy or timing of exit
- Target: [X]x MOIC in [X] years

Option B — Majority recap with secondary:
- Total transaction: $[X]M
  - Primary capital (into company): $[X]M
  - Secondary purchase (from founder): $[X]M
  - Founder retains [X]%, rolls [X]% into new structure
- Modest leverage: [X]x EBITDA ($[X]M term loan)
- We control the board, exit timing, and strategic direction
- Target: [X]x MOIC in [X] years

Option C — Structured preferred equity:
- Invest $[X]M as convertible preferred
- [X]x liquidation preference + [X]% PIK coupon
- Converts to [X]% of common at our option
- Downside protection: get $[X]M back before common in liquidation
- Upside: if company hits $[X]M ARR, convert and participate in equity

Compare the three structures:
1. Return profile at exit values of $[X]M, $[X]M, $[X]M (bear, base, bull)
2. Downside protection: at what exit value do we lose money?
3. Governance and control: ability to influence outcomes
4. Founder alignment: which structure keeps the founder most motivated?
5. Risk-adjusted IRR: probability-weighted returns across scenarios

Use of leverage in growth equity:
- When is modest leverage appropriate? (predictable revenue, positive EBITDA, low capex)
- Leverage quantum: typically 1-3x EBITDA (vs. 4-6x in traditional buyouts)
- Purpose: fund secondary purchase, not operational risk
- Key test: can the company service debt from current cash flow without impacting growth investment?
```

---

## Mathematical Frameworks

**SaaS Valuation Framework**:

```
Enterprise Value = NTM Revenue x EV/Revenue Multiple

Where the multiple is driven by:
  EV/Revenue ≈ α + β₁(Revenue Growth) + β₂(NRR) + β₃(Rule of 40) + β₄(Gross Margin)

Typical regression coefficients (illustrative, varies by market):
  β₁ ≈ 0.3x per 10pp of growth
  β₂ ≈ 0.5x per 10pp of NRR above 100%
  β₃ ≈ 0.15x per point of Rule of 40 above 20
```

**Implied Growth Rate from Multiple**:

```
If a company trades at [X]x NTM revenue, the implied forward growth rate is:
  Implied growth ≈ (Multiple - Base multiple for 0% growth) / β₁

Example: 15x NTM revenue with base multiple of 5x and β₁ of 0.3x per 10pp:
  Implied growth = (15 - 5) / 0.03 = 333% ... or the market expects extraordinary growth
  This framework reveals when a multiple is disconnected from achievable fundamentals
```

**Net Revenue Retention Compounding**:

```
A cohort with NRR of 120% doubles its revenue in ~3.8 years without adding new customers:
  Years to double = ln(2) / ln(NRR) = 0.693 / ln(1.20) ≈ 3.8 years

Revenue from existing customers after n years = Base ARR x NRR^n
  Year 0: $100M
  Year 1: $120M (at 120% NRR)
  Year 3: $173M
  Year 5: $249M

This is why NRR > 120% commands premium multiples: the installed base is a compounding engine.
```

**Burn Multiple and Efficiency**:

```
Burn Multiple = Net Cash Burn / Net New ARR

Interpretation:
  < 1.0x: Exceptional efficiency (each $1 burned generates > $1 of ARR)
  1.0-1.5x: Good
  1.5-2.0x: Needs improvement
  > 2.0x: Unsustainable without significant improvement

Implied steady-state margin: if burn multiple is 1.5x and gross margin is 75%,
  the company needs to reduce S&M intensity to reach profitability.
  Breakeven growth rate ≈ (Total Opex - Gross Profit) / (Gross Margin x Incremental ARR per $1 S&M)
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Core PE frameworks, due diligence checklists
- [`buyouts.md`](buyouts.md) — Operational improvement, exit preparation (relevant for growth-to-buyout transitions)
- [`private-credit.md`](private-credit.md) — Debt structuring for growth companies using modest leverage
- [`special-situations.md`](special-situations.md) — Structured equity and convertible instruments
