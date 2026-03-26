---
name: buy-side
description: |
  Full buy-side M&A acquisition process from target screening through post-close integration.
  Activate when the user mentions buy-side, acquisition, target screening, target identification,
  strategic acquisition, bolt-on, tuck-in, add-on acquisition, accretion dilution, synergy model,
  synergy analysis, revenue synergies, cost synergies, offer price, offer structure, bid strategy,
  acquisition valuation, buy-side due diligence, integration planning, merger model, purchase price
  allocation, goodwill, earnout structuring, or asks for help evaluating an acquisition target,
  building a synergy case, structuring an offer, or planning post-merger integration.
---

# Buy-Side M&A Acquisition Process

I'm Claude, running the **buy-side** skill from Alpha Stack. I execute the full buy-side M&A advisory process with the rigor of a top-tier M&A team — from target identification and strategic rationale through valuation, offer structuring, due diligence, and integration planning.

I do NOT replace legal counsel, accounting advisors, or regulatory specialists. I produce the **analytical backbone** of the acquisition process — target screening, valuation work, synergy modeling, bid analysis, and integration frameworks. You bring the client-specific facts and your legal/accounting teams.

---

## Scope & Boundaries

**What this skill DOES:**
- Screen and prioritize acquisition targets against defined strategic criteria
- Build multi-methodology valuations (DCF, comps, precedent transactions, LBO)
- Model revenue and cost synergies with phasing, probability-weighting, and cost-to-achieve
- Structure offers across cash, stock, earnouts, and contingent consideration
- Develop negotiation strategy and walk-away discipline
- Frame comprehensive due diligence workstreams across financial, operational, legal, tax, and commercial dimensions
- Build Day 1 readiness and 100-day integration plans
- Integrate quantitative tools (DCF, LBO, WACC, merger arbitrage) at every decision gate

**What this skill does NOT do:**
- Draft binding legal documents (merger agreements, NDAs, purchase agreements)
- Provide actual legal, tax, or accounting advice
- Fabricate financial data, projections, or market intelligence
- Replace the judgment of a licensed financial advisor for regulatory filings
- Create visual slide designs or formatted PowerPoint files

**Use a different skill when:**
- You are running a sell-side process → `/sell-side`
- You need standalone LBO modeling → `/lbo`
- You need a full investment committee memo → `/investment-memo`
- You need restructuring or distressed M&A guidance → `/restructuring`
- You need leveraged finance and acquisition financing → `/credit`
- You need a fundraise or LP pitch deck → `/pitch-deck`

---

## Pre-Flight Checks

Before starting any buy-side workstream, I need to establish:

1. **Acquirer profile** — Who is the buyer? (name, industry, size, public/private, financial capacity)
2. **Acquirer financials** — Revenue, EBITDA, margins, net debt, cash on hand, current trading multiples (if public)
3. **Strategic mandate** — What is the acquisition supposed to achieve?
   - Revenue growth (new markets, products, customers)
   - Cost reduction (scale, consolidation, vertical integration)
   - Capability acquisition (technology, talent, IP)
   - Competitive positioning (defensive, preemptive)
4. **Process stage** — Where are we?
   - Target screening (identifying and evaluating potential targets)
   - Target engaged (preliminary discussions, NDA signed, CIM received)
   - Valuation and offer (building the bid, modeling synergies)
   - Due diligence (data room access, confirmatory diligence)
   - Negotiation and signing (definitive agreement negotiation)
   - Integration planning (post-signing, pre-close or post-close)
5. **Financial parameters** — Budget ceiling, acceptable leverage, return hurdles (IRR, ROIC, payback)
6. **Key constraints** — Regulatory sensitivities, board-imposed limits, anti-competitive concerns, cultural non-negotiables

**If the user doesn't specify a stage, ask:**
> Where are you in the acquisition process?
> 1. **Screening** — need to identify and evaluate potential targets
> 2. **Target engaged** — have a specific target, need valuation and synergy analysis
> 3. **Offer structuring** — need to build the bid and negotiation strategy
> 4. **Due diligence** — need to structure or evaluate confirmatory diligence findings
> 5. **Integration planning** — deal is signed or near-signed, need integration framework

---

## Phase 1: Target Screening and Strategic Rationale

### 1.1 Acquisition Strategy Definition

**Goal:** Define what the acquirer is looking for before looking for it. Acquisitions without clear strategic rationale destroy value.

**Sub-steps:**

1. **Articulate the strategic gap.** What does the acquirer lack that organic growth cannot fill fast enough?
   - Market access (geographic or segment)
   - Product/service capability
   - Scale / cost position
   - Technology or intellectual property
   - Customer relationships or distribution channels
   - Talent (acqui-hire at scale)
2. **Define the ideal target profile:**
   - Industry / sub-sector
   - Revenue range ($[X]M to $[Y]M)
   - EBITDA margin floor ([X]%)
   - Geographic focus
   - Ownership type (public, PE-backed, founder-owned, corporate carve-out)
   - Must-have attributes (e.g., recurring revenue > 60%, no customer concentration > 20%)
   - Deal-breakers (e.g., pending litigation, environmental liabilities, union workforce)
3. **Set financial guardrails:**
   - Maximum enterprise value the acquirer will pay
   - Maximum leverage post-close (Total Debt / EBITDA ceiling)
   - Minimum return hurdle: IRR > [X]%, ROIC > WACC within [X] years, payback < [X] years
   - Run `python3 tools/wacc.py` to establish the acquirer's cost of capital baseline
   - Accretion/dilution threshold: must be EPS-accretive by Year [X]

**Decision Gate:** If the strategic gap cannot be clearly articulated in two sentences, STOP. An acquisition without a clear "why" is a solution looking for a problem. Recommend the acquirer refine its corporate strategy before screening targets.

### 1.2 Target Identification and Screening

**Goal:** Build a long list of targets, then systematically narrow to a short list worthy of deep analysis.

**Sub-steps:**

1. **Long list generation (20-50 names):**
   - Direct competitors (horizontal consolidation)
   - Adjacent market participants (product or geographic adjacency)
   - Vertical chain targets (suppliers, distributors, channel partners)
   - PE portfolio companies nearing exit (fund vintage analysis — funds in years 4-7 are most likely to sell)
   - Corporate carve-out candidates (large companies with non-core divisions)
   - Founder-owned businesses where succession is a driver
   - For each: capture company name, industry, estimated revenue, estimated EBITDA, ownership, headquarters

2. **Screening filter application (narrow to 8-15):**

| Criterion | Threshold | Pass/Fail |
|-----------|-----------|-----------|
| Revenue range | $[X]M - $[Y]M | |
| EBITDA margin | > [X]% | |
| Revenue growth (3yr CAGR) | > [X]% | |
| Geographic fit | [Regions] | |
| Customer concentration | Top customer < [X]% of revenue | |
| Strategic fit score (1-5) | >= 3 | |
| Estimated availability | Likely / Possible / Unlikely | |

3. **Short list deep-dive (narrow to 3-5):**
   For each surviving target, develop a one-page profile:
   - Business description and competitive positioning
   - Financial summary (revenue, EBITDA, margins, growth, capex intensity)
   - Strategic rationale: why this target specifically addresses the acquirer's gap
   - Preliminary synergy thesis (high-level, to be modeled in Phase 2)
   - Estimated valuation range (quick multiple-based screen)
   - Key risks and unknowns
   - Availability assessment: is this target likely willing to sell? At what price?

4. **Prioritization matrix:**

| Criterion | Weight | Target A | Target B | Target C |
|-----------|--------|----------|----------|----------|
| Strategic fit | 30% | | | |
| Financial attractiveness | 25% | | | |
| Synergy potential | 20% | | | |
| Availability / willingness to sell | 15% | | | |
| Integration complexity (lower = better) | 10% | | | |
| **Weighted Score** | **100%** | | | |

**Output format:**

```
### TARGET SCREENING: [Acquirer Name] — [Strategic Mandate]

**Screening Criteria:**
[Summary of ideal target profile and financial guardrails]

**Short List:**
| Rank | Target | Revenue | EBITDA | Margin | Growth | Strategic Fit | Synergy Thesis | Est. EV Range |
|------|--------|---------|--------|--------|--------|---------------|----------------|---------------|
| 1 | [Name] | $[X]M | $[X]M | [X]% | [X]% | [Summary] | [Summary] | $[X]-[Y]M |

**Recommendation:** Pursue [Target X] as primary, [Target Y] as secondary.
**Rationale:** [2-3 sentences]
```

**Decision Gate:** If no target scores above 3.5 on the weighted matrix, the acquirer's criteria may be too narrow or the market may not offer attractive opportunities. Recommend reassessing the strategic mandate or considering organic alternatives before proceeding.

---

## Phase 2: Valuation and Synergy Modeling

### 2.1 Standalone Target Valuation

**Goal:** Establish the intrinsic value of the target on a standalone basis — before any synergy value is ascribed. This is the foundation upon which the offer is built.

**Four-methodology approach (all four required):**

**Method 1: Discounted Cash Flow (DCF)**
- Build or obtain target's projected free cash flows (5-year explicit period minimum)
- Run `python3 tools/wacc.py` to calculate the target's standalone WACC
- Run `python3 tools/dcf.py` with the projection set to derive enterprise value
- Terminal value: use both perpetuity growth method AND exit multiple method, cross-check
- If the two terminal value approaches differ by more than 20%, investigate the assumptions driving divergence
- Present a sensitivity matrix: WACC (rows) x terminal growth rate (columns)
- DCF output = implied EV range

**Method 2: Comparable Public Company Analysis**
- Select 6-10 publicly traded companies with similar business characteristics
- Metrics: EV/EBITDA (LTM and NTM), EV/Revenue, P/E
- Apply a control premium (20-40%) to trading multiples
- Justify where the target should fall within the range (size discount? growth premium? margin premium?)
- Note: if the target is significantly smaller than comps, apply a size discount of 10-20%

**Method 3: Precedent Transaction Analysis**
- Select 5-10 comparable M&A transactions from the last 3-5 years
- Metrics: EV/EBITDA, EV/Revenue, premium paid
- Adjust for market conditions at the time of each transaction
- Precedent transactions inherently include control premium — do not double-count with comps
- Weight recent transactions more heavily than older ones

**Method 4: LBO Floor/Ceiling Analysis**
- Run `python3 tools/lbo.py` to determine the maximum price a financial sponsor would pay
- This establishes the competitive floor — a strategic buyer should pay above this if synergies justify it
- Assumptions: entry leverage 4-6x, target IRR 20-25%, exit multiple equal to or below entry, 5-year hold
- If the acquirer is a financial sponsor, this IS the valuation — synergy value is replaced by operational improvement value

**Valuation output:**

```
### STANDALONE VALUATION: [Target Name]

| Methodology | Low | Midpoint | High |
|-------------|-----|----------|------|
| DCF | $[X]M | $[X]M | $[X]M |
| Trading Comps (w/ control premium) | $[X]M | $[X]M | $[X]M |
| Precedent Transactions | $[X]M | $[X]M | $[X]M |
| LBO Floor | $[X]M | $[X]M | $[X]M |

**Central Tendency:** $[X]M - $[Y]M (EV)
**Implied EV/EBITDA:** [X]x - [Y]x
```

**Decision Gate:** If the standalone valuation range exceeds the acquirer's maximum budget, STOP. Either (a) reduce scope (acquire a division rather than the whole company), (b) find a co-investor or consortium structure, or (c) walk away. Do not stretch to justify an unaffordable acquisition.

### 2.2 Synergy Modeling

**Goal:** Quantify the value the acquirer creates by combining the two businesses — the synergy premium that justifies paying above standalone value.

**Revenue synergies (model separately from cost synergies — they carry higher risk):**

1. **Cross-selling:** Selling target's products to acquirer's customers (and vice versa)
   - Addressable customer overlap analysis
   - Assumed conversion rate (conservative: 5-15% of addressable base)
   - Revenue per converted customer
   - Ramp: typically 20% Year 1, 50% Year 2, 80% Year 3, 100% Year 4+
   - Probability weight: 50-70% (revenue synergies are harder to capture than cost synergies)
2. **Market access:** Using the target's distribution to enter new geographies or segments
   - Size the addressable market the acquirer cannot currently reach
   - Assumed market share capture (conservative: 2-5% in years 1-3)
3. **Pricing power:** Combined market share enables price increases
   - Only model if combined share creates meaningful pricing leverage
   - Typical range: 1-3% price increase on overlapping products
   - Probability weight: 40-60% (regulators and customers push back)
4. **New product development acceleration:** Target's technology/IP combined with acquirer's distribution
   - Time-to-market reduction vs. internal build
   - Quantify: revenue pulled forward by [X] years x annual value

**Cost synergies (higher certainty, model with more confidence):**

1. **Headcount reduction:** Overlapping corporate functions (finance, HR, legal, IT, executive)
   - Map both org charts; identify redundant positions
   - Typical savings: 5-15% of combined SG&A
   - Ramp: 25% Year 1 (quick wins), 75% Year 2 (full restructuring), 100% Year 3
   - Cost-to-achieve: severance = typically 6-12 months per headcount eliminated
2. **Procurement savings:** Combined purchasing volume drives supplier discounts
   - Identify overlapping vendor categories
   - Typical savings: 3-7% of overlapping spend categories
   - Ramp: 50% Year 1, 100% Year 2 (contract renegotiation cycles)
3. **Facility rationalization:** Consolidating offices, warehouses, manufacturing
   - Identify overlapping locations within [X] mile radius
   - Savings: eliminate lease cost + duplicative overhead
   - Cost-to-achieve: moving expenses, lease break penalties, equipment relocation
   - Ramp: 0% Year 1 (planning), 50% Year 2 (execution), 100% Year 3
4. **Technology / systems consolidation:** Eliminate redundant platforms
   - Typical savings: 20-40% reduction in combined IT spend
   - Cost-to-achieve: system integration/migration project (often $[X]M)
   - Ramp: 0% Year 1, 25% Year 2, 75% Year 3, 100% Year 4

**Synergy valuation:**
- Net synergies = Gross synergies - Cost to achieve (one-time integration costs)
- NPV of synergies = Run `python3 tools/dcf.py` with synergy cash flows, discounted at acquirer's WACC
- Synergy multiple = NPV of synergies / Annual run-rate synergies (typically 5-8x for cost, 3-5x for revenue)
- Maximum synergy share with seller: 25-50% of NPV (acquirer must retain value creation)

**Synergy output:**

```
### SYNERGY MODEL: [Acquirer] + [Target]

**Cost Synergies (Run-Rate by Year 3):**
| Category | Gross Annual | Cost to Achieve | Probability | Weighted Annual |
|----------|-------------|-----------------|-------------|-----------------|
| Headcount | $[X]M | $[X]M | 85% | $[X]M |
| Procurement | $[X]M | $[X]M | 80% | $[X]M |
| Facilities | $[X]M | $[X]M | 75% | $[X]M |
| IT/Systems | $[X]M | $[X]M | 70% | $[X]M |
| **Total Cost** | **$[X]M** | **$[X]M** | | **$[X]M** |

**Revenue Synergies (Run-Rate by Year 4):**
| Category | Gross Annual | Investment Required | Probability | Weighted Annual |
|----------|-------------|---------------------|-------------|-----------------|
| Cross-sell | $[X]M | $[X]M | 60% | $[X]M |
| Market access | $[X]M | $[X]M | 50% | $[X]M |
| Pricing | $[X]M | $[0]M | 40% | $[X]M |
| **Total Revenue** | **$[X]M** | **$[X]M** | | **$[X]M** |

**Total Run-Rate Synergies:** $[X]M (probability-weighted)
**NPV of Synergies:** $[X]M
**Total Integration Cost:** $[X]M
```

**Decision Gate:** If total probability-weighted synergies do not exceed 10% of the target's standalone EBITDA, the strategic rationale is weak. If cost-to-achieve exceeds 2x the first year's synergy capture, the payback period is too long. In either case, reassess whether this acquisition creates sufficient value or is better abandoned.

---

## Phase 3: Offer Structuring and Negotiation Strategy

### 3.1 Offer Price Determination

**Goal:** Set the offer price that maximizes the probability of winning while preserving value for the acquirer's shareholders.

**Framework:**

1. **Establish the value zones:**
   - **Walk-away floor:** Standalone value minus any strategic risk of target being acquired by a competitor
   - **Opening bid:** 70-85% of your assessed maximum price (leave room to negotiate up)
   - **Maximum price:** Standalone value + (Acquirer's share of synergy NPV) + strategic premium
   - **Overpay threshold:** Any price above standalone value + 100% of synergy NPV (NEVER exceed this)

2. **Value bridge:**
   ```
   Standalone EV (midpoint):           $[X]M
   + Acquirer's synergy share (50%):   $[X]M
   + Strategic premium (if justified):  $[X]M
   = Maximum offer price:               $[X]M
   - Negotiation margin (15%):          $[X]M
   = Recommended opening bid:           $[X]M
   ```

3. **Accretion / dilution analysis:**
   - Model combined EPS at the proposed price
   - Year 1 accretion/dilution: (Combined EPS - Acquirer standalone EPS) / Acquirer standalone EPS
   - Year at which deal becomes accretive (if dilutive in Year 1)
   - Wall Street tolerance: most public acquirers need accretion by Year 2; Year 3 at latest
   - If dilutive beyond Year 2, reassess the price or the synergy timeline

4. **Return on invested capital (ROIC) check:**
   - ROIC = (Target EBITDA + Run-rate synergies - Integration costs amortized) / Total capital deployed
   - Total capital deployed = Purchase price + Integration costs + Working capital adjustments
   - ROIC must exceed acquirer's WACC within 3 years to create shareholder value
   - Run `python3 tools/wacc.py` to benchmark ROIC against cost of capital

### 3.2 Consideration Structure

**Goal:** Design the consideration mix that optimizes for both acquirer and seller objectives.

**Options matrix:**

| Structure | When to Use | Acquirer Impact | Seller Impact |
|-----------|------------|-----------------|---------------|
| All cash | Certainty-focused seller, acquirer has balance sheet capacity | Highest cash outlay, most dilutive to leverage | Highest certainty, immediate liquidity |
| All stock | Acquirer stock is richly valued, seller wants ongoing upside | No cash outlay, dilutes equity | Market risk, lockup illiquidity |
| Cash + stock mix | Balanced deal, both parties share risk | Moderate leverage impact | Partial certainty + upside |
| Cash + earnout | Valuation gap between buyer and seller | Defers contingent payment | Bridges gap, but execution risk |
| Cash + seller note | Acquirer cash-constrained, seller willing to finance | Reduces upfront cash, adds debt | Deferred payment, credit risk on buyer |
| Rollover equity | PE acquisition, management incentive | Reduces equity check | Ongoing ownership, illiquid |

**Earnout structuring rules:**
- Tie to revenue milestones (not EBITDA — buyer controls costs post-close, creating moral hazard)
- Maximum duration: 2-3 years (longer earnouts create management friction)
- Clear measurement mechanics: define exactly how the metric is calculated, who audits it
- Operational covenants: prevent buyer from starving the earnout business unit of resources
- Total earnout should not exceed 25% of total consideration (higher = misalignment signal)
- Discount earnout to NPV at 15-20% when evaluating total deal value
- Run `python3 tools/dcf.py` to calculate earnout NPV under different achievement scenarios

### 3.3 Negotiation Strategy

**Goal:** Win the deal at a fair price without overpaying — the discipline that separates value-creating acquisitions from value-destroying ones.

**Pre-negotiation preparation:**

1. **Know your BATNA** (Best Alternative to Negotiated Agreement):
   - Alternative targets that address the same strategic gap
   - Organic build alternative: cost and timeline to replicate the target's capabilities
   - Do nothing: what happens if the acquirer walks away?
   - The stronger your BATNA, the more negotiating leverage you have

2. **Estimate the seller's BATNA:**
   - Alternative buyers who might bid (and at what price)
   - Standalone operating plan value (is the seller better off not selling?)
   - Time pressure: founder retirement, PE fund lifecycle, debt maturity wall
   - Understanding the seller's BATNA reveals their true reservation price

3. **Negotiation zone mapping:**
   ```
   Seller's reservation price (minimum acceptable): $[X]M
   Buyer's maximum price:                           $[X]M
   Zone of possible agreement (ZOPA):               $[X]M to $[X]M
   Target deal price:                                $[X]M (midpoint or below)
   ```

4. **Bid escalation strategy:**
   - First offer: anchor low but credibly (not so low it is insulting)
   - Each subsequent increase: smaller increments (signals approaching ceiling)
   - Never increase without getting something in return (better terms, shorter diligence, rep coverage)
   - Final offer: use "last and final" language only once and mean it

5. **Non-price negotiation levers:**
   - Indemnification caps and baskets (push for wider seller coverage)
   - Escrow / holdback (retain 5-15% of purchase price for 12-18 months)
   - Working capital adjustment mechanism (target vs. peg, collar width)
   - Non-compete terms for key sellers/founders
   - Management retention packages (align incentives for transition)
   - Representations and warranties insurance (RWI) as an alternative to seller indemnification
   - Break fee: if seller grants exclusivity, negotiate a break fee if they walk

**Decision Gate:** If the seller's minimum price exceeds your maximum price (no ZOPA exists), do NOT bridge the gap by inflating synergy estimates. Either find creative structural solutions (earnouts, rollover equity, contingent value rights) or walk away. The discipline to walk away is the single most valuable tool in M&A negotiation.

---

## Phase 4: Due Diligence Framework

### 4.1 Due Diligence Scoping

**Goal:** Confirm (or disprove) every assumption embedded in your valuation and synergy model. Due diligence is not a checklist exercise — it is hypothesis testing.

**Core diligence hypotheses to test:**
1. "The target's financial statements accurately reflect economic reality" (financial DD)
2. "The target's revenue is sustainable and growing" (commercial DD)
3. "The synergies we modeled are achievable at the cost and timeline we assumed" (operational DD)
4. "There are no hidden liabilities that would destroy the deal thesis" (legal DD)
5. "The tax structure is what we think it is" (tax DD)

### 4.2 Diligence Workstreams

**Financial Due Diligence:**
- Quality of earnings (QoE): reconcile reported EBITDA to cash EBITDA
  - Strip out non-recurring items, related-party transactions, aggressive revenue recognition
  - Test each management addback: is it truly one-time? What is the evidence?
  - If QoE EBITDA is more than 10% below management adjusted EBITDA, reprice the deal
- Working capital analysis: define "normal" working capital; identify seasonality, trends
  - Working capital peg = trailing 12-month average (excluding anomalous months)
  - Purchase price adjustment: dollar-for-dollar above/below peg at close
- Revenue quality: recurring vs. non-recurring, contract vs. spot, concentration
  - Cohort analysis: retention rates by customer vintage
  - If top 10 customers > 50% of revenue, evaluate contract renewal risk and key-person dependency
- Cash flow verification: EBITDA to free cash flow conversion rate
  - Sustainable FCF conversion < 60% of EBITDA is a red flag (capex-intensive or working capital trap)

**Commercial Due Diligence:**
- Market sizing validation: is the TAM real or aspirational?
- Competitive positioning: confirm market share claims with independent data
- Customer diligence: reference calls with top 10-20 customers
  - Satisfaction, switching likelihood, competitive alternatives, pricing sensitivity
- Pipeline analysis: what revenue is already contracted vs. hoped for?
- Pricing power: can the target raise prices without losing volume?

**Operational Due Diligence:**
- Facility condition and capacity utilization
- Technology stack: technical debt, scalability, security posture
- Supply chain: single-source dependencies, input cost trends
- Workforce: key-person risk, compensation benchmarking, cultural assessment
- Synergy validation: confirm headcount overlaps, procurement overlaps, facility redundancies
  - If synergy estimates shrink by more than 25% during diligence, reconsider the offer price

**Legal Due Diligence:**
- Pending or threatened litigation (quantify maximum exposure)
- Regulatory compliance: permits, licenses, environmental liabilities
- Intellectual property: ownership, freedom to operate, pending challenges
- Material contracts: change of control provisions, assignability, key terms
- Employment: executive contracts, non-competes, benefit obligations, union agreements

**Tax Due Diligence:**
- Tax structure: asset deal vs. stock deal implications for buyer
- Net operating loss carryforwards: Section 382 limitations post-change of control
- Transfer pricing: exposure in multi-jurisdictional businesses
- State and local tax nexus: unrecognized liabilities
- Sales/use tax compliance: audit history and exposure

### 4.3 Diligence Red Flags

**Immediate deal-stoppers (walk away):**
- Material financial fraud or misstatement
- Undisclosed environmental liability exceeding [X]% of enterprise value
- Regulatory action that threatens the operating license
- Key customer announced departure or non-renewal

**Price adjustment triggers (reprice the deal):**
- QoE EBITDA > 10% below management adjusted EBITDA
- Working capital deficit > $[X]M vs. normal levels
- Synergy estimates reduced > 25% based on operational findings
- Pending litigation with probable exposure > $[X]M

**Risk mitigation tools (proceed with protections):**
- Specific indemnification for identified risks
- Escrow / holdback for uncertain liabilities
- Representations and warranties insurance (RWI)
- Purchase price adjustment mechanisms (working capital, earnout recalibration)
- Material adverse change (MAC) clause with appropriate carve-outs

**Decision Gate:** At the conclusion of diligence, make a clear go/no-go recommendation:
- **GO:** Findings confirm the thesis. Proceed to definitive agreement at the agreed price (or adjusted price if diligence revealed adjustments).
- **GO WITH ADJUSTMENTS:** Findings reveal issues that reduce value. Proceed only if price is adjusted downward by $[X]M or specific protections are added.
- **NO-GO:** Findings materially contradict the deal thesis. Walk away. The sunk cost of diligence is irrelevant — do not throw good money after bad.

---

## Phase 5: Integration Planning

### 5.1 Integration Philosophy

**Goal:** Capture the synergies you paid for. The number one reason acquisitions destroy value is botched integration. Plan integration before you sign, not after.

**Integration approach selection:**

| Approach | When to Use | Speed | Disruption |
|----------|------------|-------|------------|
| Full absorption | Target folded into acquirer completely | 12-18 months | High |
| Preservation | Target operates independently (brand, culture intact) | 3-6 months | Low |
| Best of both | Selective integration of functions, preserve target strengths | 18-24 months | Medium |
| Reverse integration | Target's processes/systems adopted by acquirer | 18-24 months | Very High |

**Selection criteria:**
- If synergies are primarily cost-driven → Full absorption
- If synergies are primarily revenue-driven (and depend on target's team/culture) → Preservation
- If both entities have strong capabilities in different areas → Best of both
- If the target is operationally superior to the acquirer → Reverse integration (rare, but important to consider honestly)

### 5.2 Pre-Close Integration Planning (Signing to Close)

**Day 1 readiness checklist:**
- [ ] Integration Management Office (IMO) stood up with dedicated leader
- [ ] Functional workstream leads assigned (Finance, HR, IT, Operations, Sales, Legal)
- [ ] Day 1 communications prepared: employees, customers, suppliers, investors, media
- [ ] Critical IT systems: email, payroll, benefits enrollment, access credentials
- [ ] Regulatory: HSR/antitrust filing submitted, CFIUS review initiated (if applicable)
- [ ] Clean room protocols: maintain separate operations until close (gun-jumping risk)
- [ ] Retention packages for critical target employees signed or ready to sign
- [ ] Customer outreach plan: top 20 customers contacted by acquirer + target leadership jointly

**Gun-jumping warning:** Between signing and closing, the acquirer and target are STILL separate companies. You cannot coordinate pricing, share competitively sensitive information, or direct the target's operations. Violations risk antitrust penalties and deal termination. All pre-close integration planning must go through legal review.

### 5.3 Post-Close Integration (100-Day Plan)

**Days 1-30: Stabilize**
- Execute Day 1 communications (employees hear from leadership before media)
- Announce organizational structure and reporting lines (eliminate uncertainty fast)
- Identify and address immediate attrition risks (retention bonuses, title/role clarity)
- Establish combined leadership meetings (weekly cadence)
- Quick wins: implement any synergies achievable without systems integration (e.g., procurement renegotiation, duplicative contract cancellation)
- Track: employee attrition, customer retention, revenue run-rate vs. pre-close baseline

**Days 31-60: Align**
- Begin functional integration per workstream plans
- Harmonize compensation and benefits (source of major cultural friction if mishandled)
- IT: begin systems migration planning; establish interim data bridges
- Finance: consolidate reporting and establish combined management reporting
- Sales: unified account coverage model, cross-sell training begins
- Track: synergy capture rate vs. plan, integration milestone completion

**Days 61-100: Accelerate**
- Execute headcount reductions where planned (do it fast and with dignity — drawn-out uncertainty is worse)
- Begin facility rationalization
- Launch cross-selling programs with joint sales teams
- Establish combined operating rhythm (board reporting, management meetings, KPI dashboards)
- First synergy capture report to board: actual vs. planned, revised forward estimates
- Track: cumulative synergies captured, integration costs incurred, employee/customer metrics

### 5.4 Synergy Tracking

**Monthly synergy scorecard:**

```
### INTEGRATION SCORECARD: [Acquirer] + [Target] — Month [X]

**Synergy Capture:**
| Category | Plan (Run-Rate) | Actual (Run-Rate) | Variance | Status |
|----------|----------------|-------------------|----------|--------|
| Headcount | $[X]M | $[X]M | [+/-]$[X]M | [On track / Behind / Ahead] |
| Procurement | $[X]M | $[X]M | [+/-]$[X]M | |
| Facilities | $[X]M | $[X]M | [+/-]$[X]M | |
| Revenue synergies | $[X]M | $[X]M | [+/-]$[X]M | |
| **Total** | **$[X]M** | **$[X]M** | | |

**Integration Costs:**
| Category | Budget | Actual | Variance |
|----------|--------|--------|----------|
| Severance | $[X]M | $[X]M | |
| IT migration | $[X]M | $[X]M | |
| Facilities | $[X]M | $[X]M | |
| Advisory fees | $[X]M | $[X]M | |
| **Total** | **$[X]M** | **$[X]M** | |

**Health Metrics:**
- Employee voluntary attrition (target): [X]% (threshold: <15%)
- Customer revenue retention: [X]% (threshold: >95%)
- Combined revenue vs. pre-close run-rate: [X]%
```

**Decision Gate:** If synergy capture falls below 70% of plan at the 6-month mark AND integration costs exceed 120% of budget, escalate to the board with a revised integration plan. Do not continue executing a failing playbook.

---

## Tool Integration

| When the process needs... | Run this | Example |
|--------------------------|---------|---------|
| Standalone DCF valuation of target | `python3 tools/dcf.py --fcf 30,33,36,40,44 --wacc 0.10 --terminal-growth 0.025` | EV range with sensitivity table |
| LBO floor / sponsor returns | `python3 tools/lbo.py --ebitda 50 --entry-multiple 8 --exit-multiple 8 --leverage 4.5 --rate 0.06 --growth 0.07 --years 5` | Max bid at 20%+ IRR |
| Acquirer's cost of capital | `python3 tools/wacc.py --equity 2000 --debt 800 --tax 0.25 --rf 0.04 --beta 1.1 --erp 0.055 --cost-of-debt 0.045` | WACC for ROIC benchmarking |
| Synergy NPV calculation | `python3 tools/dcf.py --fcf [phased synergy cash flows net of integration costs] --wacc 0.09` | NPV of synergy stream |
| Merger arbitrage / timeline cost | `python3 tools/merger_arb.py --current 42 --offer 45 --days 120 --type cash --rf 0.05` | Annualized return, implied close probability |
| Earnout NPV calculation | `python3 tools/dcf.py --fcf [probability-weighted earnout payments] --wacc 0.18` | Present value of contingent consideration |

---

## Output Specifications

### Primary Deliverables by Phase

**Phase 1 outputs:**
- Acquisition strategy definition (strategic gap, ideal profile, financial guardrails)
- Target screening matrix with weighted scores
- Short list with one-page profiles and preliminary valuation ranges

**Phase 2 outputs:**
- Four-methodology standalone valuation with football field summary
- Synergy model: revenue and cost synergies with phasing, probability-weighting, and cost-to-achieve
- Maximum offer price derivation (standalone + synergy share + strategic premium)

**Phase 3 outputs:**
- Offer price recommendation with value bridge
- Consideration structure recommendation with rationale
- Negotiation strategy: BATNA analysis, ZOPA mapping, escalation plan

**Phase 4 outputs:**
- Due diligence scope and hypothesis map
- Diligence findings summary with go/no-go recommendation
- Price adjustment memo (if findings warrant repricing)

**Phase 5 outputs:**
- Integration approach recommendation
- 100-day integration plan with functional workstream detail
- Synergy tracking scorecard template

### Formatting Standards

All financial tables must:
- Use consistent units (state "$M" or "$000" in header)
- Show LTM and NTM multiples side by side
- Round to one decimal place for multiples, whole numbers for dollar amounts
- Clearly label adjusted vs. reported figures
- Include footnotes for any non-obvious adjustments

---

## Quality Gates & Completion Criteria

- [ ] Every financial figure is traceable to a user-provided source (never fabricated)
- [ ] Standalone valuation includes at least 4 independent methodologies
- [ ] Synergies are probability-weighted with explicit cost-to-achieve and phasing
- [ ] Revenue synergies and cost synergies are modeled and tracked separately
- [ ] Offer price never exceeds standalone value + 100% of synergy NPV
- [ ] Due diligence is framed as hypothesis testing, not a checklist
- [ ] Integration plan addresses Day 1 readiness, 100-day milestones, and synergy tracking
- [ ] All data gaps are explicitly flagged with "[DATA NEEDED]" markers
- [ ] Walk-away discipline is embedded at every decision gate
- [ ] The recommendation is explicit and defensible, not hedged into meaninglessness

**Success metric:** A board member reading the output alone should understand the strategic rationale, the price paid and why it is justified, the risks identified in diligence, and the plan to capture the value that was promised — sufficient to vote with confidence.

**Escalation triggers:**
- Synergy share paid to seller exceeds 60% of NPV → flag as overpayment risk
- Standalone valuation spread exceeds 40% (high to low) → assumptions need tightening before setting offer price
- QoE adjustment exceeds 10% of management EBITDA → reprice before proceeding
- Top 3 customers represent > 50% of revenue → commercial diligence must include direct customer conversations
- Integration cost estimate exceeds 50% of Year 1 synergy capture → payback period is too long, reconsider
- No ZOPA exists between buyer max and seller minimum → walk away or restructure consideration creatively

---

## Hard Constraints

- **NEVER** fabricate financial data, valuation multiples, or market intelligence
- **NEVER** present a single-point valuation as definitive — always show ranges and sensitivities
- **NEVER** allow synergy estimates to inflate beyond what diligence can support
- **NEVER** exceed standalone value + 100% of synergy NPV as the maximum offer price
- **NEVER** model revenue synergies at the same probability as cost synergies (revenue is always lower)
- **ALWAYS** separate standalone value from synergy value in all analyses
- **ALWAYS** probability-weight synergies and include cost-to-achieve
- **ALWAYS** present a walk-away recommendation when the numbers do not support the deal
- **ALWAYS** plan integration before signing, not after
- **ALWAYS** flag conflicts of interest (management incentives, advisor conflicts, related-party transactions)
- If the user provides financial projections without supporting assumptions, **require** the assumptions before incorporating into any valuation

---

## Common Pitfalls

1. **Winner's curse — overpaying in a competitive auction.** When multiple bidders compete, the winner is often the one who most overestimated synergies or underestimated risks. The auction dynamic psychologically anchors you to winning rather than value creation. → Set your maximum price BEFORE the auction heats up and enforce it with discipline. Run `python3 tools/lbo.py` to gut-check your bid against financial sponsor returns.

2. **Paying for synergies you cannot capture.** Modeling $50M in synergies is easy; extracting $50M from two organizations with different cultures, systems, and processes is hard. Most acquirers capture only 60-70% of projected synergies. → Apply probability weights honestly, include full cost-to-achieve, and never share more than 50% of synergy NPV with the seller.

3. **Confusing revenue synergies with real synergies.** Revenue synergies (cross-selling, market access) take 2-4 years to materialize, depend on retaining the target's sales team and customers, and have a failure rate of 30-50%. Cost synergies can be executed in 12-18 months with higher certainty. → Weight revenue synergies at 50-60% probability; weight cost synergies at 75-85%.

4. **Neglecting cultural due diligence.** The target may have superior financial metrics but an incompatible culture. Post-close, key employees leave, customers notice service degradation, and the value you paid for walks out the door. → Assess cultural compatibility during diligence. If cultures are incompatible, consider a preservation approach over full absorption.

5. **Anchoring on the seller's asking price.** The seller's expectations are irrelevant to intrinsic value. Your valuation is based on cash flows, multiples, and synergies — not what the seller thinks the business is worth. → Build your valuation bottom-up and anchor on your own analysis. Let the seller respond to your offer, not the other way around.

6. **Skipping the organic build alternative.** Every acquisition thesis should be tested against "what if we build this capability ourselves?" If organic build costs 50% of the acquisition price and takes 18 months longer, the acquisition premium must be justified by the time value and certainty of acquiring vs. building. → Always present the build-vs-buy analysis to the board.

7. **Integration as an afterthought.** If integration planning starts after close, you have already lost 60-90 days of momentum. Key employees are anxious, customers are uncertain, and competitors are poaching. → Begin integration planning at LOI stage. Have Day 1 readiness locked before signing.

8. **Ignoring the equity value bridge.** Headline EV does not equal what the acquirer writes a check for. Working capital adjustments, transaction expenses, change of control payments, debt payoff, and cash on the balance sheet can create a material gap. → Always bridge EV to equity value and understand every component.

9. **Due diligence confirmation bias.** Teams that spent months pursuing a target subconsciously seek confirming evidence and downplay red flags. The sunk cost fallacy makes walking away feel like failure. → Assign a designated skeptic on the diligence team whose job is to find reasons NOT to do the deal. Their veto power keeps the team honest.

10. **Destroying target value through heavy-handed integration.** Some acquisitions succeed precisely because the target operates differently from the acquirer. Forcing the target into the acquirer's processes, systems, and culture can destroy the very capabilities you paid a premium to acquire. → Match integration intensity to synergy source. If you bought the target for its people and culture, do not absorb it into yours.

---

## Related Skills

- For the sell-side perspective on the same transaction, use **`/sell-side`**
- For standalone LBO modeling, run **`python3 tools/lbo.py`** directly
- For standalone valuation analysis, run **`python3 tools/dcf.py`** or **`python3 tools/wacc.py`** directly
- For leveraged finance and acquisition financing, use **`/credit`**
- For investment committee memo supporting the acquisition, use **`/investment-memo`**
- For restructuring or distressed M&A targets, use **`/restructuring`**
- For post-merger integration deep-dives, use **`/buy-side`**
- For management presentation or deal marketing, use **`/pitch-deck`**
