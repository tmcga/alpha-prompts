# Private Equity Analyst

Prompt library for private equity analysts and associates. Covers deal sourcing, due diligence, LBO modeling, portfolio company operations, and exit planning.

## Role Context

```
You are a private equity associate at a middle-market buyout fund ($500M-$5B fund size).
You evaluate deals through the lens of downside protection first, upside second. Every
investment must have a clear value creation plan with operational levers, not just financial
engineering. You think in IRR and MOIC, stress-test every assumption, and always ask: "What
has to go right for this deal to work, and what happens if it doesn't?"
```

---

## 1. Deal Screening & Sourcing

### Initial Deal Screen

```
I'm evaluating a potential acquisition target:

Company overview:
- Industry: [X]
- Revenue: $[X]M
- EBITDA: $[X]M
- EBITDA margin: [X]%
- Revenue CAGR (3yr): [X]%
- Customer concentration: Top customer = [X]% of revenue
- Capex intensity: [X]% of revenue
- Owner/management situation: [founder-led / PE-owned / corporate carve-out]

Asking price: [X]x EBITDA

Run this through a PE screening framework:
1. **Attractive industry?** Fragmented (roll-up potential), growing, non-cyclical, high barriers to entry
2. **Defensible business?** Recurring revenue, switching costs, pricing power, mission-critical product
3. **Margin expansion opportunity?** Current margins vs. best-in-class peers, obvious cost cuts
4. **Revenue growth levers?** Organic (pricing, new products, geographic expansion) + M&A (bolt-ons)
5. **Cash generation?** Low capex, negative working capital cycle, minimal maintenance capex
6. **Debt capacity?** Predictable cash flows, asset base for collateral, industry lending norms
7. **Exit path?** Who are the likely buyers in 3-5 years? Strategic, larger PE, IPO?
8. **Key risks?** What kills this deal? (customer concentration, regulatory, technology disruption, cyclicality)
```

### Comparable Deal Analysis

```
I'm benchmarking a deal at [X]x EBITDA for a [industry] company.

Help me build a comparable deals database:
1. What have similar businesses sold for in the last 3-5 years?
2. Segment by buyer type:
   - Strategic acquirers (typically pay more for synergies)
   - PE buyouts (disciplined on price, lever for returns)
   - PE platform vs. add-on (add-ons trade at lower multiples)
3. What premium/discount should apply based on:
   - Size (larger = higher multiple, "size premium")
   - Growth rate (faster growth = higher multiple)
   - Margin profile (higher margins = higher multiple)
   - Recurring revenue % (more recurring = higher multiple)
4. At [X]x EBITDA, what IRR does the math produce in a base-case LBO?
5. What's the maximum price we can pay and still hit our [X]% IRR hurdle?
```

---

## 2. LBO Modeling

### Full LBO Model Build

```
I'm building an LBO model for [target company].

Operating assumptions:
- Revenue: $[X]M, growing [X]% per year
- EBITDA margin: [X]%, expanding to [X]% by Year 5
- Capex: $[X]M/year (maintenance) + $[X]M (growth, Years 1-2)
- Working capital: [X]% of incremental revenue
- Tax rate: [X]%
- Management rollover: [X]% of equity

Financing assumptions:
- Entry multiple: [X]x EBITDA
- Senior secured (Term Loan B): [X]x EBITDA at L+[X]bps, 1% annual amortization
- Second lien / mezzanine: [X]x EBITDA at [X]%
- Revolver: $[X]M undrawn (for working capital)
- Transaction fees: [X]% of TEV
- Financing fees: [X]% of debt raised

Build the complete model:
1. **Sources & Uses**
   - Sources: Senior debt + Sub debt + Sponsor equity + Management rollover
   - Uses: Equity purchase price + Debt repayment + Transaction fees + Financing fees

2. **Operating model** (5-year projection):
   - Revenue → EBITDA → EBIT → EBT → Net income
   - Cash flow: NI + D&A - Capex - ΔWC - Mandatory debt amortization = FCF for debt paydown

3. **Debt schedule**:
   - Opening balance → Mandatory amortization → Optional prepayment (cash sweep) → Closing balance
   - Interest expense by tranche
   - Leverage ratios: Total Debt/EBITDA, Senior Debt/EBITDA, Interest coverage

4. **Returns analysis** at exit (Year 3, 4, 5):
   - Exit multiple: [X-1]x, [X]x, [X+1]x EBITDA (downside, base, upside)
   - Enterprise value at exit = Exit EBITDA × Exit multiple
   - Equity value = EV - Net debt
   - MOIC = Equity out / Equity in
   - IRR (solve for discount rate where NPV of equity cash flows = 0)

5. **Returns bridge** — decompose IRR into:
   - EBITDA growth contribution
   - Multiple expansion/contraction contribution
   - Debt paydown contribution (free cash flow + amortization)
   - Formula: (1 + IRR)^t ≈ (EBITDA_exit/EBITDA_entry) × (Multiple_exit/Multiple_entry) × (EV_exit/Equity_exit) / (EV_entry/Equity_entry)
```

### Downside / Stress Testing

```
My base case LBO produces [X]x MOIC / [X]% IRR at a [X]x exit in Year 5.

Stress test this deal:
1. **Revenue shortfall**: What if revenue grows at [X-5]% instead of [X]%? New IRR?
2. **Margin compression**: What if EBITDA margins stay flat (no improvement)? New IRR?
3. **Multiple contraction**: Exit at [X-2]x instead of [X]x. New IRR?
4. **Combined downside**: Revenue miss + no margin expansion + multiple contraction. Do we lose money?
5. **Covenant breach**: At what EBITDA decline do we breach the [X]x leverage covenant?
6. **Liquidity crisis**: What if we need to fund $[X]M in unexpected capex? Is the revolver sufficient?
7. **Interest rate sensitivity**: +200bps on floating rate debt. Impact on cash flow and ability to delever?

Key question: In the downside case, what is the MOIC floor? PE rule of thumb: if the downside MOIC is below 1.0x (capital loss), the risk/reward is unattractive.
```

---

## 3. Due Diligence

### Commercial Due Diligence

```
I'm conducting commercial due diligence on [target] in [industry].

Help me structure the key diligence workstreams:

1. **Market analysis**:
   - TAM/SAM/SOM sizing and growth rates
   - Market share and competitive positioning
   - Industry consolidation trends (fragmented → concentrated?)
   - Regulatory environment and upcoming changes

2. **Customer analysis**:
   - Revenue concentration: top 10 customers as % of revenue
   - Customer retention/churn rates by cohort
   - Net revenue retention (expansion vs. contraction)
   - Customer switching costs and contract structure (length, renewal rates)
   - Reference calls: What do customers say about switching?

3. **Competitive dynamics**:
   - Porter's Five Forces analysis
   - Competitive moat: brand, network effects, switching costs, cost advantages, IP
   - Who could disrupt this business? New entrants, technology shifts, regulatory change?

4. **Growth bridge**:
   - Organic: pricing power, volume growth, new products, geographic expansion
   - M&A: bolt-on acquisition pipeline, typical multiples for add-ons
   - Quantify each lever: $[X]M revenue opportunity × probability

5. **Key diligence questions for management meetings**:
   - What would cause a customer to leave?
   - What's the biggest competitive threat in the next 3 years?
   - Where is the low-hanging fruit for margin improvement?
```

### Financial Due Diligence

```
I'm reviewing the Quality of Earnings (QoE) report for [target].

Reported EBITDA: $[X]M
Adjusted EBITDA (per seller): $[X]M

Help me evaluate the EBITDA bridge and adjustments:

1. **Legitimate adjustments** (accept these):
   - One-time transaction costs, lawsuit settlements
   - Owner compensation above market rate (add back excess)
   - Facility closure / restructuring (if truly non-recurring)

2. **Questionable adjustments** (push back):
   - "Run-rate" revenue adjustments (projecting recent wins forward)
   - Recurring "non-recurring" costs (if they show up every year, they're recurring)
   - Stock-based compensation exclusion (real economic cost)
   - Pro forma synergies from recent acquisitions (show me the proof)

3. **Working capital analysis**:
   - Normalize working capital: What is the target NWC for the closing mechanism?
   - Seasonal patterns: Are we buying at a WC trough or peak?
   - DSO/DIO/DPO trends: Is the company stretching payables to inflate cash flow?

4. **Capex analysis**:
   - Maintenance vs. growth capex split
   - Has the company been underinvesting (deferred maintenance that we'll need to fund)?
   - Capex as % of revenue vs. peers

5. **Tax diligence**: NOLs, transfer pricing exposure, pending audits, structural tax rate going forward
```

---

## 4. Value Creation & Portfolio Operations

### 100-Day Plan

```
We've just closed the acquisition of [company] at [X]x EBITDA.

EBITDA: $[X]M
Key value creation thesis: [describe — margin expansion, revenue growth, bolt-on M&A, etc.]

Help me build the 100-day post-close plan:

1. **Quick wins (Days 1-30)**:
   - Cost savings: procurement renegotiation, headcount optimization, facility consolidation
   - Pricing: Can we raise prices? When do contracts renew?
   - Working capital: Tighten collections (reduce DSO), optimize inventory

2. **Strategic initiatives (Days 30-100)**:
   - Revenue: Sales force effectiveness, new customer acquisition, cross-sell/upsell
   - Operations: Lean manufacturing, automation, outsourcing non-core functions
   - M&A: Identify and begin diligence on 2-3 bolt-on targets

3. **KPI dashboard**: What 10 metrics should the board track monthly?
   - Revenue growth (organic), EBITDA margin, FCF conversion
   - Customer retention, pipeline coverage, win rate
   - Leverage ratio, liquidity, debt paydown

4. **Management alignment**:
   - Equity incentive plan structure (management rollover + option pool)
   - Align incentives: MOIC-based vesting, EBITDA ratchets, annual bonus tied to budget
   - What should the management equity pool be? (typically 10-20% of equity)

5. **Governance**: Board composition, reporting cadence, approval thresholds
```

### Add-On Acquisition Strategy

```
Our portfolio company [platform] is pursuing a buy-and-build strategy in [industry].

Platform EBITDA: $[X]M (at [X]x entry multiple)
Target add-on size: $[X-X]M EBITDA
Industry fragmentation: [describe — many small players, no dominant leader]

Help me think through:
1. **Multiple arbitrage**: If we buy add-ons at [X]x and the combined platform trades at [X+2]x, what's the value creation from multiple re-rating alone?
2. **Integration synergies**: Revenue synergies (cross-sell, geographic reach) + Cost synergies (back-office consolidation, procurement scale)
3. **Financing**: Fund add-ons with platform FCF, incremental debt, or equity co-invest?
4. **Pace**: How many acquisitions per year is realistic without execution risk?
5. **Valuation math**:
   - Platform: $[X]M EBITDA × [X]x = $[X]M EV
   - Add 3 bolt-ons at [X]M EBITDA each × [lower]x = $[X]M total acquisition cost
   - Combined EBITDA (with synergies): $[X]M × [platform multiple]x = $[X]M EV
   - Value created = Combined EV - Platform cost - Bolt-on costs
```

---

## 5. Exit Planning

### Exit Readiness Assessment

```
We're preparing [portfolio company] for exit in [X] months.

Current state:
- Hold period: [X] years
- Entry EBITDA: $[X]M at [X]x
- Current EBITDA: $[X]M
- Current leverage: [X]x
- Equity invested: $[X]M

Help me prepare for exit:
1. **Exit route evaluation**:
   - Strategic sale: Who are the 5-10 likely buyers? What would they pay?
   - Secondary buyout (PE-to-PE): What leverage can a new sponsor put on?
   - IPO: Does the company meet minimum thresholds (revenue, growth, profitability)?
   - Dividend recap: Should we take chips off the table before a full exit?

2. **Vendor due diligence prep**: What reports should we commission?
   - Vendor QoE (financial), Commercial DD, IT DD, Legal DD, ESG assessment
   - Fix issues now that will be flagged in buyer DD

3. **Management presentation**: What story are we telling?
   - What we did (value creation track record)
   - What's left to do (remaining upside for the buyer)
   - Financial projections: conservative enough to be credible, ambitious enough to justify the multiple

4. **Expected returns**:
   - MOIC and IRR at [X-1]x, [X]x, [X+1]x exit multiples
   - Returns attribution: How much came from growth, margins, multiple, deleveraging?
   - GP carry calculation: [X]% carry above [X]% preferred return (with European vs. American waterfall)

5. **Process design**: Targeted (2-3 bidders) vs. broad auction? Timeline?
```
