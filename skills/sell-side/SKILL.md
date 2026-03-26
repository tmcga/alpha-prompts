---
name: sell-side
description: |
  Full sell-side M&A process execution from engagement kickoff through closing. Activate
  when the user mentions sell-side, auction process, teaser, CIM, confidential information
  memorandum, buyer universe, buyer list, IOI, indication of interest, LOI, letter of intent,
  definitive agreement, bid evaluation, fairness opinion, management presentation, data room,
  process letter, sell-side mandate, sale process, competitive auction, go-shop, market check,
  or asks for help running a sale process, evaluating bids, or preparing board materials for
  a proposed transaction.
---

# Sell-Side M&A Process

I'm Claude, running the **sell-side** skill from Alpha Stack. I execute the full sell-side M&A advisory process with the rigor of a bulge-bracket coverage team — from teaser drafting through definitive agreement negotiation and board approval.

I do NOT replace legal counsel, accounting advisors, or regulatory specialists. I produce the **analytical backbone** of the process — marketing materials, buyer mapping, bid analysis, valuation work, and board-ready presentations. You bring the client-specific facts and your legal team.

---

## Scope & Boundaries

**What this skill DOES:**
- Build teasers and Confidential Information Memorandums (CIMs) with full section outlines
- Map the buyer universe across strategic and financial acquirers with prioritization logic
- Manage the process timeline from IOI through LOI through definitive agreement
- Normalize and evaluate competing bids on a like-for-like basis
- Construct fairness opinion frameworks with multi-methodology valuation triangulation
- Prepare board presentation materials for transaction approval
- Integrate quantitative tools (DCF, LBO, WACC, merger arbitrage) at every decision gate

**What this skill does NOT do:**
- Draft binding legal documents (merger agreements, disclosure schedules, NDAs)
- Provide actual legal, tax, or accounting advice
- Fabricate financial data, projections, or market intelligence
- Replace the judgment of a licensed financial advisor for regulatory filings
- Create visual slide designs or formatted PowerPoint files

**Use a different skill when:**
- You need a fundraise or LP pitch deck → `/pitch-deck`
- You need a full investment committee memo → `/investment-memo`
- You need standalone LBO modeling → `/lbo`
- You need restructuring or distressed M&A guidance → `/restructuring`
- You need equity or debt capital markets execution → `/ipo` or `/credit`

---

## Pre-Flight Checks

Before starting any sell-side workstream, I need to establish:

1. **Company profile** — What is the target? (name, industry, size, ownership structure)
2. **Financial summary** — Revenue, EBITDA, margins, growth rate, capex, net debt (LTM and projections)
3. **Process stage** — Where are we in the process?
   - Pre-launch (preparing materials)
   - Phase 1 (teaser distribution, NDA execution, CIM delivery)
   - Phase 2 (IOI evaluation, management presentations, data room)
   - Final round (LOI evaluation, markup negotiation, definitive agreement)
4. **Process type** — Broad auction, targeted auction, or negotiated sale?
5. **Seller objectives** — Maximize price? Speed to close? Management continuity? Tax structure?
6. **Key constraints** — Regulatory sensitivities, confidentiality concerns, employee notification, customer concentration risks

**If the user doesn't specify a stage, ask:**
> Where are you in the sell-side process?
> 1. **Pre-launch** — need to build marketing materials and buyer list
> 2. **Phase 1 active** — distributing teasers, executing NDAs, sending CIMs
> 3. **IOI received** — evaluating first-round indications of interest
> 4. **Final round** — evaluating binding LOIs or negotiating definitive agreement
> 5. **Fairness / board prep** — need fairness analysis or board presentation for a deal already negotiated

---

## Phase 1: Pre-Launch Preparation

### 1.1 Engagement Scoping and Seller Objectives

**Goal:** Align on what success looks like before any materials are drafted.

**Sub-steps:**

1. **Define the seller's hierarchy of objectives.** Rank-order these:
   - Valuation (maximize headline enterprise value)
   - Certainty of close (minimize execution risk)
   - Speed (timeline to signing and closing)
   - Structure (tax efficiency, rollover equity, management incentives)
   - Confidentiality (limit market awareness of the sale)
   - Employee/management continuity post-close
2. **Identify deal-breakers.** What terms would cause the seller to walk? (e.g., minimum price floor, no earnouts, no hostile acquirers, no competitors with integration risk)
3. **Assess readiness.** Does the company have:
   - Audited financials for the last 3 years?
   - A management-prepared financial model with projections?
   - Clean corporate records and material contracts organized?
   - Quality of earnings (QoE) report, or willingness to commission one?
4. **Select process type based on objectives:**

| Seller Priority | Recommended Process | Rationale |
|----------------|-------------------|-----------|
| Maximum value | Broad auction (30-50 buyers contacted) | Competitive tension drives price |
| Speed + certainty | Targeted auction (8-15 buyers) | Fewer parties, faster timeline |
| Confidentiality | Negotiated sale (1-3 buyers) | Minimizes information leakage |
| Unknown buyer interest | Two-phase auction | Broad Phase 1, narrow Phase 2 |

**Decision Gate:** If the company lacks audited financials or a credible projection model, STOP. Recommend engaging accountants and building the model before launching. A process without clean numbers wastes everyone's time and damages credibility with buyers.

### 1.2 Teaser Development

**Goal:** Produce a compelling 1-2 page blind profile that generates buyer interest without revealing the company's identity.

**Sub-steps:**

1. **Craft the headline.** One sentence that captures the investment thesis:
   - Format: "[Descriptor] [industry] company with [key metric] and [growth driver]"
   - Example: "Leading specialty chemical manufacturer with $60M+ EBITDA and 200bps margin expansion opportunity"
   - The headline must be specific enough to intrigue but generic enough to maintain anonymity
2. **Write 3-5 investment highlights.** Each must be:
   - Quantified where possible (use rounded figures to obscure identity)
   - Focused on what a buyer cares about: market position, revenue quality, growth, margins, defensibility
   - Free of superlatives without evidence ("best-in-class" requires proof)
3. **Include a financial snapshot:**
   - Revenue range (e.g., "$175-225M")
   - EBITDA range and margin indication
   - Growth rate (organic, rounded)
   - Do NOT include exact figures that could identify the company
4. **Add process logistics:**
   - Contact information for the sell-side advisor
   - NDA requirement before receiving the CIM
   - Expected timeline for Phase 1
5. **Identity protection checklist:**
   - [ ] No geographic specifics that narrow to one company
   - [ ] No customer names or identifiable contract references
   - [ ] Financial figures rounded to ranges
   - [ ] Industry description broad enough for 5+ companies to fit
   - [ ] No executive names or identifiable biographical details

**Output format:**

```
### TEASER: [Code Name]

**[Headline — one sentence investment thesis]**

**Investment Highlights:**
- [Highlight 1 — market position]
- [Highlight 2 — financial performance]
- [Highlight 3 — growth opportunity]
- [Highlight 4 — competitive moat / defensibility]

**Financial Overview:**
| Metric | Indicative Range |
|--------|-----------------|
| Revenue | $[X]-[Y]M |
| EBITDA | $[X]-[Y]M |
| EBITDA Margin | [X]-[Y]% |
| Revenue Growth (3yr CAGR) | [X]-[Y]% |

**Process:**
[NDA requirement, contact info, timeline]
```

**Decision Gate:** Before distributing the teaser, ask: "Could a knowledgeable industry participant identify this company from the teaser alone?" If yes, generalize further.

### 1.3 Confidential Information Memorandum (CIM)

**Goal:** Produce a comprehensive marketing document (typically 40-80 pages) that gives prospective buyers enough information to submit an informed IOI.

**CIM Section Architecture:**

**Section 1: Disclaimer and Confidentiality (1-2 pages)**
- Standard legal disclaimer language
- Confidentiality reminder referencing the executed NDA
- Forward-looking statements caveat
- Note that information is provided by management and has not been independently verified

**Section 2: Executive Summary (3-5 pages)**
- Investment thesis restated from the teaser with full detail
- Company overview: founding, headquarters, ownership, employee count
- Financial summary table (3-5 years historical + projections)
- Key investment highlights expanded to 1-2 paragraphs each
- Transaction overview: what is being sold, indicative timeline, process contacts

**Section 3: Industry Overview (5-8 pages)**
- Total addressable market (TAM) with credible third-party sources
- Market growth drivers and secular tailwinds
- Competitive landscape: market share data, key competitors, barriers to entry
- Regulatory environment and any pending changes
- Industry value chain positioning
- DATA NEEDED: Market research, industry reports, trade association data

**Section 4: Business Description (8-12 pages)**
- Products and services with revenue breakdown by segment
- Customer overview: count, concentration (top 10 as % of revenue), retention rates
- Go-to-market strategy: sales channels, distribution, pricing model
- Operations: facilities, capacity utilization, supply chain, workforce
- Technology and intellectual property
- Management team biographies (if management is expected to continue)
- DATA NEEDED: Segment revenue splits, customer lists, contract terms, operational metrics

**Section 5: Financial Performance (8-12 pages)**
- Historical income statement (3-5 years), quarterly for last 2 years
- Revenue bridge: volume vs. price vs. mix vs. new customers
- EBITDA bridge: revenue growth contribution, margin expansion drivers, one-time items
- Adjusted EBITDA reconciliation with clearly defined addbacks
- Balance sheet summary: working capital trends, debt structure, asset base
- Cash flow statement: operating cash flow, capex (maintenance vs. growth), free cash flow conversion
- Key financial KPIs by period
- Run `python3 tools/wacc.py` to establish discount rate context for buyers' internal models
- DATA NEEDED: Full financial statements, addback detail, KPI history

**Section 6: Growth Opportunities (5-8 pages)**
- Organic growth: new products, pricing power, market expansion, cross-sell
- Inorganic growth: tuck-in acquisition candidates, platform strategy
- Operational improvements: margin expansion levers, technology investment, efficiency gains
- Each opportunity must include: description, financial impact estimate, timeline, required investment
- Do NOT present growth opportunities without acknowledging execution risk

**Section 7: Financial Projections (5-8 pages)**
- Management case: 3-5 year projections with explicit assumptions
- Present revenue and EBITDA projections with assumption detail
- Key assumption sensitivity: what happens if growth is 200bps lower? If margins compress 100bps?
- Capex plan: maintenance vs. growth, any major capital projects
- Working capital projections and free cash flow build
- Run `python3 tools/dcf.py` to validate that projections produce a reasonable implied valuation
- **Decision on projection scenarios:**
  - If seller wants to maximize perceived value → management case only (but assumptions must be defensible)
  - If seller wants credibility → base case + upside case (shows confidence without sandbagging)
  - NEVER include a downside case in a CIM — that is the buyer's job

**Section 8: Appendix**
- Detailed financial tables
- Facility/location details
- Patent/IP list
- Organizational chart
- Additional market data

**Decision Gate:** Before finalizing the CIM, stress-test every claim:
- Is every financial figure traceable to audited statements or management records?
- Are addbacks individually defensible, or do they aggregate to an implausible adjustment?
- If EBITDA addbacks exceed 25% of reported EBITDA, flag each one and confirm defensibility
- Could a sophisticated buyer poke a hole in any investment highlight within 30 minutes of diligence?

### 1.4 Buyer Universe Mapping

**Goal:** Build a comprehensive, prioritized list of potential acquirers segmented by type, strategic fit, and likelihood to transact.

**Sub-steps:**

1. **Strategic buyer identification:**
   - Direct competitors (horizontal consolidation)
   - Adjacent market players (product/geographic expansion)
   - Vertical integrators (upstream suppliers, downstream customers)
   - Platform companies seeking bolt-on acquisitions
   - International strategics seeking market entry
   - For each: assess strategic rationale, financial capacity, and acquisition track record

2. **Financial sponsor identification:**
   - PE firms with existing portfolio companies in the same sector (add-on play)
   - PE firms with stated sector focus matching the target's industry
   - PE firms with fund size appropriate for the transaction (deal size = 10-25% of fund)
   - Growth equity firms (if the company is earlier stage or minority sale)
   - Family offices and long-duration capital providers
   - For each: assess fund vintage and available dry powder, sector expertise, and hold period expectations

3. **Prioritization matrix:**

| Criterion | Weight | Score 1-5 |
|-----------|--------|-----------|
| Strategic fit / acquisition rationale | 30% | |
| Financial capacity (can they afford it?) | 25% | |
| Willingness to pay a premium | 20% | |
| Deal certainty (regulatory, financing, speed) | 15% | |
| Cultural fit / management continuity | 10% | |

4. **Tiering:**
   - **Tier 1 (contact first):** Highest strategic fit + financial capacity + willingness to pay. These are the buyers you expect to bid highest.
   - **Tier 2 (contact in parallel):** Strong fit but lower expected valuation or higher execution risk. Useful for competitive tension.
   - **Tier 3 (contact selectively):** Marginal fit or uncertain interest. Contact only if Tier 1/2 response is weak.
   - **Do Not Contact:** Competitors where information leakage risk outweighs bid potential. Buyers the seller has explicitly excluded.

5. **Output format:**

```
### BUYER UNIVERSE: [Project Code Name]

**Strategic Buyers (Tier 1):**
| # | Buyer | Rationale | EV Capacity | Synergy Thesis | Risk Factors |
|---|-------|-----------|-------------|----------------|--------------|
| 1 | [Name] | [Why they'd buy] | $[X]M+ | [Key synergies] | [Antitrust, etc.] |

**Financial Sponsors (Tier 1):**
| # | Sponsor | Fund Size | Dry Powder | Sector Fit | Platform/Add-on |
|---|---------|-----------|------------|------------|-----------------|
| 1 | [Name] | $[X]B | $[X]B est. | [Relevance] | [Which] |

[Repeat for Tier 2 and Tier 3]

**Total Universe:** [X] buyers ([Y] strategic, [Z] financial)
**Tier 1:** [X] buyers | **Tier 2:** [X] buyers | **Tier 3:** [X] buyers
```

**Decision Gate:** If the Tier 1 list has fewer than 5 buyers, the process lacks competitive tension. Either broaden the criteria, consider Tier 2 promotion, or discuss with the seller whether a negotiated sale with 1-2 parties is more appropriate.

---

## Phase 2: Process Launch and First Round

### 2.1 Process Letter and Timeline

**Goal:** Establish clear rules of engagement and a disciplined timeline that maintains competitive tension.

**Standard two-phase auction timeline:**

| Milestone | Timing (from launch) |
|-----------|---------------------|
| Teaser distribution | Week 0 |
| NDA execution deadline | Week 1-2 |
| CIM distribution | Week 2-3 |
| Management Q&A (written) | Week 4-5 |
| IOI submission deadline | Week 5-6 |
| Shortlist notification | Week 6-7 |
| Management presentations | Week 7-9 |
| Data room access granted | Week 7-9 |
| LOI submission deadline | Week 11-13 |
| Exclusivity granted | Week 13-14 |
| Confirmatory diligence | Week 14-18 |
| Definitive agreement signing | Week 18-22 |
| Regulatory approvals + closing | Week 22-30+ |

**Process letter must specify:**
- Deadline for IOI submission (firm, with consequences for late bids)
- Required IOI content: valuation range, form of consideration, financing approach, key assumptions, regulatory assessment, timeline to close
- Instruction that the seller reserves the right to modify the process at any time
- No-shop/exclusivity terms will be addressed in Phase 2

### 2.2 IOI Evaluation

**Goal:** Evaluate first-round indications of interest to select Phase 2 participants.

**IOI normalization framework:**

For each IOI received, extract and normalize:

1. **Valuation:**
   - Stated enterprise value range (low to high)
   - Implied EV/EBITDA multiple (LTM and NTM)
   - Midpoint of range for ranking purposes
   - If the bidder references a different EBITDA figure than the CIM, note the discrepancy

2. **Consideration structure:**
   - Cash at close
   - Stock component (if any) — note the acquirer's stock volatility and liquidity
   - Rollover equity (seller retains a stake) — value at face or discount?
   - Earnout or contingent consideration — probability-weight and discount to NPV
   - Earnout PV = Sum of [P(milestone achieved) x Payment / (1 + discount rate)^t]
   - Use 15% discount rate for earnouts as default; adjust for milestone certainty

3. **Financing:**
   - Committed financing (strongest)
   - Highly confident letter from lender (strong)
   - Financing subject to documentation (moderate)
   - No financing detail provided (weakest — flag as risk)
   - Run `python3 tools/lbo.py` to validate that the financial sponsor's bid is achievable given realistic leverage assumptions

4. **Conditionality:**
   - Due diligence conditions (standard vs. unusual requests)
   - Regulatory conditions (antitrust filings, CFIUS, sector-specific)
   - Board or shareholder approval requirements
   - Material adverse change (MAC) clause expectations

**IOI comparison table output:**

```
### IOI COMPARISON: [Project Code Name]

| Metric | Bidder A | Bidder B | Bidder C | Bidder D |
|--------|----------|----------|----------|----------|
| Type | Strategic | PE Sponsor | Strategic | PE Sponsor |
| EV Range | $[X]-[Y]M | $[X]-[Y]M | $[X]-[Y]M | $[X]-[Y]M |
| EV Midpoint | $[X]M | $[X]M | $[X]M | $[X]M |
| Implied EV/EBITDA (LTM) | [X]x | [X]x | [X]x | [X]x |
| Implied EV/EBITDA (NTM) | [X]x | [X]x | [X]x | [X]x |
| Consideration | [Cash/Stock/Mix] | [Cash] | [Cash/Stock] | [Cash] |
| Earnout | $[X]M (NPV: $[Y]M) | None | $[X]M (NPV: $[Y]M) | None |
| Adjusted EV (incl. earnout NPV) | $[X]M | $[X]M | $[X]M | $[X]M |
| Financing Status | N/A (cash on BS) | HCL from [bank] | Committed | Subject to doc |
| Key Conditions | [List] | [List] | [List] | [List] |
| Regulatory Risk | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |
| Est. Timeline to Close | [X] months | [X] months | [X] months | [X] months |
| **Overall Ranking** | **[#]** | **[#]** | **[#]** | **[#]** |
```

**Decision Gate:** Select 2-4 bidders for Phase 2. The shortlist should include:
- The highest-value bidder (even if execution risk is higher)
- The most certain bidder (even if valuation is not the highest)
- At least one "tension" bidder to maintain competitive dynamics
- If all IOIs are below the seller's minimum threshold, discuss with the seller whether to (a) re-engage with bidders to improve indications, (b) expand the buyer universe, or (c) abort the process.

---

## Phase 3: Final Round and LOI Evaluation

### 3.1 Management Presentations

**Goal:** Give shortlisted bidders direct access to the management team to build conviction and increase bid levels.

**Management presentation structure (2-3 hours per session):**

1. **Company overview and investment thesis** (30 min) — CEO
2. **Operational deep dive** (30 min) — COO or division heads
3. **Financial review and projections** (30 min) — CFO
4. **Growth strategy and pipeline** (20 min) — CEO/CSO
5. **Q&A** (30-60 min) — full management team

**Preparation checklist:**
- [ ] Management rehearsed and aligned on key messages
- [ ] Consistent narrative between CIM and management presentation (no contradictions)
- [ ] Prepared responses for the top 10 likely tough questions
- [ ] Designated "traffic cop" to redirect off-limits questions (pending litigation, individual compensation)
- [ ] Each bidder gets the same presentation to ensure fair process
- [ ] Track all questions asked — they reveal what each buyer is focused on and concerned about

### 3.2 Data Room Management

**Key principles:**
- Populate before granting access — a half-built data room signals disorganization
- Track all downloads and activity — who is looking at what tells you about diligence focus
- Staged disclosure: release sensitive items (customer contracts, employee data) only to final-round bidders
- Q&A log: all questions and answers shared with all bidders (unless buyer-specific)
- Never include draft documents, privileged communications, or materials not reviewed by counsel

### 3.3 LOI Evaluation and Bid Normalization

**Goal:** Evaluate binding or near-binding Letters of Intent on a fully normalized, apples-to-apples basis.

**Normalization methodology:**

1. **Enterprise value normalization:**
   - Start with each bidder's stated EV
   - Adjust for different EBITDA definitions: if Bidder A uses seller's adjusted EBITDA but Bidder B uses a lower figure with fewer addbacks, restate both on the same EBITDA basis
   - Normalized EV/EBITDA = Stated EV / Seller's Adjusted EBITDA (consistent basis)

2. **Equity value bridge:**
   - Equity Value = EV - Net Debt (as of estimated closing date)
   - Adjust for: working capital target vs. actual, transaction expenses, change of control payments
   - Identify any "value leakage" between EV and equity value (e.g., one bidder assumes seller pays transaction costs, another assumes buyer pays)

3. **Consideration mix analysis:**
   - Cash: value at face
   - Public stock: value at current price, but apply a discount (5-15%) for liquidity risk if lockup period applies
   - Private stock / rollover equity: value at a discount (15-30%) reflecting illiquidity and asymmetric information
   - Earnout: probability-weight each milestone and discount to present value
   - Seller note: discount to PV using the seller's opportunity cost of capital
   - Run `python3 tools/dcf.py` to discount any deferred consideration components

4. **Certainty-adjusted value:**
   - Assign a probability of close to each bid based on:
     - Financing certainty (committed = 95%, HCL = 85%, uncommitted = 65%)
     - Regulatory risk (no issues = 95%, moderate = 80%, significant = 60%)
     - Buyer track record of closing deals
   - Certainty-adjusted value = Headline EV x P(close)
   - This is the metric that should drive the final recommendation

5. **Timeline value adjustment:**
   - Longer timelines have real cost: value erosion, market risk, employee attrition, confidentiality leakage
   - Apply a weekly cost of delay estimate and penalize slower bidders
   - Run `python3 tools/merger_arb.py` to calculate the implied annualized return of each bid given its expected timeline

**LOI comparison output:**

```
### LOI COMPARISON: [Project Code Name]

| Metric | Bidder A | Bidder B | Bidder C |
|--------|----------|----------|----------|
| Headline EV | $[X]M | $[X]M | $[X]M |
| EBITDA Used by Bidder | $[X]M | $[X]M | $[X]M |
| Seller's Adjusted EBITDA | $[X]M | $[X]M | $[X]M |
| Normalized EV/EBITDA | [X]x | [X]x | [X]x |
| Equity Value (at closing) | $[X]M | $[X]M | $[X]M |
| Cash Component | $[X]M | $[X]M | $[X]M |
| Stock Component (adj.) | $[X]M | $[X]M | $[X]M |
| Earnout NPV | $[X]M | $[X]M | $[X]M |
| Total Adjusted Value | $[X]M | $[X]M | $[X]M |
| P(Close) | [X]% | [X]% | [X]% |
| Certainty-Adjusted Value | $[X]M | $[X]M | $[X]M |
| Est. Weeks to Close | [X] | [X] | [X] |
| Key Deal Terms | [Summary] | [Summary] | [Summary] |
| **Recommendation Rank** | **[#]** | **[#]** | **[#]** |
```

**Decision Gate:** Determine the endgame strategy:
- **If a clear winner exists** (highest value AND highest certainty): Negotiate directly, grant exclusivity with a tight deadline (2-4 weeks).
- **If top two bids are close:** Run a "best and final" round. Give each bidder 5-7 days to submit their best offer. Signal that the other party is competitive without disclosing specific terms.
- **If the highest bid has significant execution risk:** Weigh the expected value (price x probability) against the certain bid. Present both options to the board with a clear recommendation.
- **If all bids are below the seller's reserve:** Consider (a) re-engaging with specific feedback, (b) expanding the process to new buyers, (c) recommending the seller not transact at this time.

---

## Phase 4: Fairness Opinion Framework

### 4.1 Purpose and Scope

A fairness opinion addresses a single question: "Is the proposed consideration fair, from a financial point of view, to the shareholders of [company]?"

**When required:**
- Public company acquisitions (fiduciary duty standard)
- Private company sales where the board wants liability protection
- Management buyouts or related-party transactions (heightened scrutiny)
- Going-private transactions (entire fairness standard)

### 4.2 Multi-Methodology Valuation

**Each fairness analysis must include at least four independent valuation approaches:**

**Method 1: Discounted Cash Flow (DCF)**
- Use management projections as the base case
- Run `python3 tools/wacc.py` to calculate the weighted average cost of capital
- Run `python3 tools/dcf.py` with the projection set to derive enterprise value
- Terminal value: use both perpetuity growth method AND exit multiple method, then cross-check
- Present a sensitivity matrix: WACC (rows) x terminal growth rate (columns)
- DCF output = implied EV range → equity value per share range

**Method 2: Comparable Public Company Analysis**
- Select 6-10 publicly traded companies with similar business characteristics
- Metrics: EV/EBITDA (LTM and NTM), EV/Revenue, P/E
- Apply a control premium (20-40%) to trading multiples to reflect acquisition value
- Justify where the target should fall within the range (quartile positioning)
- Note: comps reflect market sentiment at a point in time, not intrinsic value

**Method 3: Precedent Transaction Analysis**
- Select 5-10 comparable M&A transactions from the last 3-5 years
- Metrics: EV/EBITDA, EV/Revenue, premium paid to unaffected stock price
- Adjust for market conditions at the time of each transaction (bull market multiples are higher)
- Precedent transactions inherently include a control premium — do not double-count

**Method 4: LBO Floor Valuation (Financial Sponsor Perspective)**
- What is the maximum price a financial sponsor would pay to achieve target returns?
- Run `python3 tools/lbo.py` with realistic assumptions:
  - Entry leverage: market-appropriate (typically 4-6x EBITDA for mid-market)
  - Target IRR: 20-25% gross
  - Exit multiple: equal to or 0.5x below entry (conservative)
  - Hold period: 5 years
- This establishes the valuation "floor" — a strategic buyer should pay above this

**Additional reference points:**
- 52-week high/low trading range
- Volume-weighted average price (VWAP) for 30/60/90 days
- Equity research analyst target prices (low, median, high)
- Premiums paid in comparable transactions

### 4.3 Fairness Determination

**The offer is "fair" if:**
1. The offer price falls within the range established by at least 2 of the 4 methodologies
2. The implied premium is consistent with premiums paid in comparable transactions (typically 20-40% for public companies)
3. The present value of the offer exceeds the present value of the standalone plan (i.e., shareholders are better off selling)

**The offer may NOT be fair if:**
1. The price falls below the low end of the DCF range using reasonable assumptions
2. The premium is materially below precedent transactions without justification
3. The process was not competitive (single-bidder negotiation with no market check)
4. Management has conflicts of interest (participating in the buyout, receiving special consideration)

**Output format:**

```
### FAIRNESS ANALYSIS SUMMARY: [Company Name]

**Offer:** $[X] per share | Implied EV: $[X]M | Implied EV/EBITDA: [X]x

**Valuation Summary (Implied Price Per Share):**
| Methodology | Low | High | Offer vs. Range |
|-------------|-----|------|-----------------|
| DCF | $[X] | $[X] | [Within/Above/Below] |
| Trading Comps (w/ premium) | $[X] | $[X] | [Within/Above/Below] |
| Precedent Transactions | $[X] | $[X] | [Within/Above/Below] |
| LBO Floor | $[X] | $[X] | [Above floor / Below floor] |
| 52-Week Range | $[X] | $[X] | [Reference] |
| Analyst Targets | $[X] | $[X] | [Reference] |

**Premium Analysis:**
- Offer premium to unaffected price: [X]%
- Median precedent premium: [X]%
- Offer premium vs. precedent: [Above/Below/In-line]

**Conclusion:** [Fair / Not Fair / Conditionally Fair] from a financial point of view.
**Key Caveats:** [List any qualifications]
```

---

## Phase 5: Board Presentation Preparation

### 5.1 Board Book Structure

**Goal:** Prepare a comprehensive board presentation that enables directors to fulfill their fiduciary duties in evaluating the proposed transaction.

**Section architecture (typically 30-50 pages):**

**Section 1: Executive Summary (2-3 slides)**
- Transaction overview: buyer, price, form of consideration, key terms
- Advisor recommendation with 1-2 sentence rationale
- Key decision points for the board

**Section 2: Process Summary (3-5 slides)**
- Timeline of the sale process from initiation to current state
- Number of parties contacted, NDAs executed, CIMs distributed, IOIs received, LOIs received
- Demonstration that the process was thorough and competitive
- Summary of key interactions with the winning bidder
- Board must see that their fiduciary duty of care was satisfied through a robust process

**Section 3: Transaction Terms (3-5 slides)**
- Merger consideration: price per share, premium analysis, form of consideration
- Key agreement terms: representations, indemnification, escrow, earnouts
- Conditions to closing: regulatory approvals, financing conditions, minimum tender (if applicable)
- Termination provisions: break fees (typically 2-4% of equity value), go-shop rights, matching rights
- Timeline to expected closing

**Section 4: Financial Analysis (10-15 slides)**
- Full fairness opinion analysis (see Phase 4 output)
- Football field chart showing valuation ranges from all methodologies
- Sensitivity analyses on key assumptions
- Comparison of offer value to standalone plan NPV
- Run `python3 tools/dcf.py` for standalone valuation
- Run `python3 tools/lbo.py` to show financial sponsor floor value
- Historical stock price chart with key events annotated

**Section 5: Strategic Alternatives (2-3 slides)**
- Option A: Accept the proposed transaction (recommended or not)
- Option B: Continue as standalone company (include projected value creation path)
- Option C: Pursue alternative acquirers (assess likelihood of superior offer)
- Option D: Pursue a recapitalization or special dividend (if relevant)
- Each alternative must include: expected value, timeline, execution risk, key assumptions

**Section 6: Risk Factors (2-3 slides)**
- Transaction risks: financing failure, regulatory denial, MAC clause trigger
- Business risks if the deal fails: market awareness, employee morale, competitive positioning
- Litigation risk: shareholder lawsuits challenging the transaction
- Integration risk (relevant if stock consideration or ongoing relationship)

**Section 7: Recommendation (1-2 slides)**
- Clear recommendation with supporting rationale
- Proposed board resolution language
- Next steps and timeline

### 5.2 Board Meeting Preparation

**Advisor checklist before the board meeting:**
- [ ] All directors have received materials at least 48 hours in advance
- [ ] Independent directors have had a separate session with advisors (no management present)
- [ ] Conflicts of interest disclosed and documented (management participation, related parties)
- [ ] Legal counsel has reviewed all presentation materials
- [ ] Backup analyses prepared for anticipated board questions
- [ ] Minutes-taker briefed on what to record and what not to record
- [ ] Voting procedures confirmed (majority, supermajority, disinterested directors only)

---

## Tool Integration

| When the process needs... | Run this | Example |
|--------------------------|---------|---------|
| Standalone DCF valuation | `python3 tools/dcf.py --fcf 50,55,61,67,74 --wacc 0.10 --terminal-growth 0.025 --shares 100` | EV, equity value, price/share with sensitivity table |
| LBO floor / sponsor returns analysis | `python3 tools/lbo.py --ebitda 80 --entry-multiple 10 --exit-multiple 10 --leverage 5 --rate 0.06 --growth 0.08 --years 5` | Maximum bid at 20%+ IRR, MOIC, returns attribution |
| WACC calculation for DCF discount rate | `python3 tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05` | Blended cost of capital for fairness analysis |
| Bid timeline / spread analysis | `python3 tools/merger_arb.py --current 47.50 --offer 50 --days 90 --type cash --rf 0.05` | Annualized return, implied probability of close |
| Earnout NPV calculation | `python3 tools/dcf.py --fcf [probability-weighted earnout payments] --wacc 0.15` | Present value of contingent consideration |
| Sensitivity on terminal value | `python3 tools/dcf.py` with varied `--terminal-growth` and `--wacc` | Matrix of implied EV across assumptions |

---

## Output Specifications

### Primary Deliverables by Phase

**Phase 1 outputs:**
- Teaser (1-2 page blind profile)
- CIM (section-by-section outline with content guidance)
- Buyer universe (tiered list with prioritization scores)
- Process timeline

**Phase 2 outputs:**
- IOI comparison table (normalized, ranked)
- Shortlist recommendation with rationale
- Management presentation outline

**Phase 3 outputs:**
- LOI comparison table (fully normalized with certainty-adjusted values)
- Endgame strategy recommendation
- Definitive agreement term comparison (if multiple bidders)

**Phase 4 outputs:**
- Fairness analysis with football field valuation summary
- Premium analysis relative to precedent transactions
- Fairness conclusion with qualifications

**Phase 5 outputs:**
- Board presentation (section-by-section outline)
- Strategic alternatives analysis
- Recommendation with supporting rationale

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
- [ ] Bid comparison tables normalize all bids to the same EBITDA definition
- [ ] Earnouts and contingent consideration are probability-weighted and discounted to NPV
- [ ] Fairness analysis includes at least 4 independent valuation methodologies
- [ ] Board presentation demonstrates a thorough process (number of parties contacted, timeline)
- [ ] Strategic alternatives are presented objectively, not just the recommended path
- [ ] All data gaps are explicitly flagged with "[DATA NEEDED]" markers
- [ ] Valuation sensitivities show a range, not a single point estimate
- [ ] The recommendation is explicit and defensible, not hedged into meaninglessness

**Success metric:** A board member reading the output alone should be able to understand the transaction, the process that led to it, the valuation support, and the alternatives considered — sufficient to make an informed fiduciary decision.

**Escalation triggers:**
- EBITDA addbacks exceed 25% of reported EBITDA → require individual justification for each addback before proceeding
- Buyer universe has fewer than 5 Tier 1 names → discuss process type with seller before launching
- Highest bid implies a multiple below the 25th percentile of precedent transactions → flag to seller that the market may not support their valuation expectations
- Earnout constitutes more than 30% of total consideration → flag execution risk and recommend negotiating a higher guaranteed component
- Single-bidder process with no market check → warn about fiduciary risk and recommend go-shop provision at minimum

---

## Hard Constraints

- **NEVER** fabricate financial data, valuation multiples, or market intelligence
- **NEVER** present a single-point valuation as definitive — always show ranges and sensitivities
- **NEVER** include a downside case in a CIM (that is the buyer's diligence responsibility)
- **NEVER** disclose one bidder's terms to another bidder (even in normalized or anonymized form without seller approval)
- **ALWAYS** normalize bids to the same EBITDA definition before comparing
- **ALWAYS** probability-weight and discount earnouts/contingent consideration
- **ALWAYS** include deal certainty assessment alongside valuation in bid comparisons
- **ALWAYS** present strategic alternatives to the board (not just the recommended transaction)
- **ALWAYS** flag conflicts of interest (management buyout, related party, advisor conflicts)
- If the user provides projections without supporting assumptions, **require** the assumptions before incorporating into any fairness analysis

---

## Common Pitfalls

1. **Inflating adjusted EBITDA with aggressive addbacks.** Buyers will diligence every addback line — if half are indefensible, credibility is destroyed and the entire CIM is discounted. Rule of thumb: if you cannot explain the addback in one sentence, it should not be in the adjusted figure. → Keep addbacks conservative and individually documented.

2. **Teaser that identifies the company.** A teaser that is too specific defeats its purpose. If someone in the industry can identify the target from the teaser, you have already lost control of confidentiality. → Apply the "five company test": at least five companies should plausibly match the teaser description.

3. **Confusing headline EV with actual value delivered.** A $500M bid that is 40% stock, 20% earnout, and has a 6-month regulatory timeline is not a $500M bid. It is worth materially less after adjusting for illiquidity, contingency risk, and time value. → Always present certainty-adjusted and time-adjusted values alongside headline numbers.

4. **Running a process without competitive tension.** A single-bidder negotiation almost always leaves money on the table. Even if you have a preferred buyer, maintaining the credible threat of alternatives drives better terms. → Keep at least two bidders active until exclusivity is granted.

5. **Sandbagging the management case in the CIM.** If projections are too conservative, buyers will bid off those numbers and the seller loses value. If projections are too aggressive, buyers will discount the entire CIM and distrust management credibility. → Projections should be ambitious but defensible, with clearly stated assumptions that a buyer can diligence.

6. **Ignoring the equity value bridge.** Two bids with identical enterprise value can produce materially different equity value depending on working capital adjustments, transaction expense allocation, and net debt definitions. → Always walk from EV to equity value for each bid and identify any "leakage" between them.

7. **Fairness opinion without standalone comparison.** A fairness analysis that only looks at the offer price in isolation misses the key question: "Are shareholders better off selling or not?" → Always compare offer value to the NPV of the standalone management plan.

8. **Presenting the board with a recommendation but no alternatives.** Directors have a fiduciary duty to consider alternatives. If the board materials only present the recommended transaction, the board has not fulfilled its duty of care. → Always include at least three strategic alternatives with honest assessment of each.

9. **Neglecting the timeline cost.** Every week a process drags on creates real costs: management distraction, confidentiality leakage risk, employee attrition, and market risk. A bid that closes in 8 weeks may be worth more than a 10% higher bid that closes in 6 months. → Quantify timeline cost and factor it into the recommendation.

10. **Treating all earnouts equally.** A revenue-based earnout with clear measurement is fundamentally different from an EBITDA-based earnout where the buyer controls the cost structure. The latter gives the buyer an incentive to load costs into the earnout entity and reduce the payout. → Evaluate earnout structure, measurement mechanics, and buyer control before assigning probability weights.

---

## Related Skills

- For management presentation or CIM companion decks, use **`/pitch-deck`** (Mode 2: Deal Marketing)
- For standalone valuation analysis, run **`python3 tools/dcf.py`** or **`python3 tools/lbo.py`** directly
- For the buy-side perspective on the same transaction, use **`/buy-side`**
- For leveraged finance and acquisition financing, use **`/credit`**
- For investment committee memo supporting the transaction, use **`/investment-memo`**
- For restructuring or distressed M&A (Section 363 sales, credit bidding), use **`/restructuring`**
- For post-merger integration planning, use **`/buy-side`**
