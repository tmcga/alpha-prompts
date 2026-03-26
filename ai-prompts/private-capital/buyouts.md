# Leveraged Buyouts

Prompt templates for large-cap and mid-cap leveraged buyout investing, covering operational improvement, platform build-outs, management incentive design, exit preparation, and LP communication.

## Role Context

```
You are a senior associate at a large-cap buyout fund managing $10B+ in AUM. Your fund
targets control acquisitions of businesses with $50M-$500M EBITDA, typically at 8-12x entry
multiples with 4-6x leverage. You think in terms of value creation plans with quantifiable
operational levers, not financial engineering alone. Every deal must answer three questions:
(1) What is the defensible competitive advantage? (2) What are the specific operational
improvements we will execute? (3) What does the exit look like and who are the buyers?
You are rigorous about returns attribution — decomposing every dollar of value created into
growth, margin expansion, multiple movement, and leverage effects.
```

For foundational LBO math, returns bridge decomposition, deal screening, and due diligence frameworks, see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below extend those foundations with buyout-specific operational and strategic depth.

---

## 1. Operational Improvement Thesis

### Margin Expansion Playbook

```
I'm building the margin expansion case for [target company]:

Current state:
- Revenue: $[X]M
- Gross margin: [X]% (peers at [X]%)
- EBITDA margin: [X]% (peers at [X]%)
- SG&A as % of revenue: [X]%
- COGS breakdown: materials [X]%, labor [X]%, overhead [X]%
- Procurement spend: $[X]M across [X] suppliers

Develop a detailed margin expansion playbook:

1. **Procurement optimization**:
   - Category-by-category spend analysis
   - Supplier consolidation opportunity (reduce from [X] to [X] suppliers)
   - Volume rebate renegotiation (what's achievable at scale?)
   - Sourcing alternatives (near-shoring, dual-sourcing for resilience)
   - Timeline: savings typically 60-70% realized within 12-18 months
   - Target: [X]bps of gross margin improvement = $[X]M EBITDA impact

2. **Pricing power assessment**:
   - When do contracts renew? What's the historical price increase cadence?
   - Price elasticity: can we push [X]% price increases without volume loss?
   - Value-based pricing: are we undercharging for mission-critical products?
   - Mix shift: can we steer toward higher-margin products/services?
   - Target: [X]bps of gross margin improvement

3. **Overhead rationalization**:
   - Headcount benchmarking vs. peers (revenue per employee, spans of control)
   - Facility footprint optimization (consolidation, lease renegotiation)
   - IT systems consolidation (reduce redundant tools and licenses)
   - Shared services implementation for back-office functions
   - Target: [X]bps of EBITDA margin improvement

4. **Management upgrade ROI**:
   - Cost of hiring a new CFO/COO: $[X]M (comp + recruiter + transition)
   - Expected impact: new CFO typically delivers 100-300bps of margin improvement
     through financial discipline, KPI visibility, and cost control
   - Payback period on management upgrade investment

Quantify total EBITDA bridge:
   Current EBITDA: $[X]M
   + Procurement savings: $[X]M
   + Pricing uplift: $[X]M
   + Overhead reduction: $[X]M
   + Revenue growth contribution: $[X]M
   = Target EBITDA (Year 3): $[X]M
   Implied margin expansion: [X]bps
```

### Operational KPI Framework

```
Design a monthly KPI dashboard for a PE-owned [industry] company with $[X]M revenue.

Tier 1 — Board-level (reported monthly to the fund):
- Revenue growth (organic, like-for-like, total with acquisitions)
- EBITDA and EBITDA margin (actual vs. budget vs. prior year)
- Free cash flow conversion: FCF / EBITDA (target: [X]%+)
- Net leverage: Net Debt / LTM EBITDA
- Liquidity: cash + undrawn revolver

Tier 2 — Management-level:
- Gross margin by product line / business unit
- Customer metrics: retention rate, NPS, pipeline coverage ratio
- Employee metrics: turnover, open headcount, revenue per FTE
- Working capital: DSO, DIO, DPO trends
- Capex: actual vs. budget, maintenance vs. growth split

Tier 3 — Operational (weekly):
- Order intake, backlog, book-to-bill ratio
- Production yield, utilization rates, on-time delivery
- Sales pipeline: new opportunities, conversion rate, average deal size

For each KPI, specify: definition, data source, frequency, target, and red/amber/green thresholds.
```

---

## 2. Platform and Add-On Strategy

### Buy-and-Build Value Creation Model

```
Our platform company [name] is executing a buy-and-build strategy in [industry]:

Platform company:
- EBITDA: $[X]M, acquired at [X]x
- Total equity invested: $[X]M
- Current leverage: [X]x

Add-on acquisition pipeline:
- Target size: $[X-X]M EBITDA each
- Expected entry multiple: [X-X]x (vs. platform at [X]x)
- Number of planned acquisitions: [X] over [X] years
- Revenue synergies per deal: [X]% cross-sell uplift over 2 years
- Cost synergies per deal: [X]% of target SG&A (back-office elimination)

Model the buy-and-build value creation:

1. **Multiple arbitrage math**:
   Small company acquired at [X]x EBITDA
   Immediately re-rated to platform multiple of [X]x upon consolidation
   Value created per $1 of acquired EBITDA = ([X]x - [X]x) = $[X] of EV
   For $[X]M of cumulative acquired EBITDA: $[X]M of arbitrage value

2. **Synergy value**:
   Revenue synergies: $[X]M incremental revenue at [X]% margin = $[X]M EBITDA
   Cost synergies: $[X]M per deal x [X] deals = $[X]M total EBITDA
   Combined synergy EBITDA at exit multiple: $[X]M x [X]x = $[X]M EV

3. **Integration execution risk**:
   - What is the realistic integration timeline per acquisition? (6-12 months)
   - Maximum absorption pace: can management handle [X] deals/year?
   - Integration capital required: IT systems, rebranding, severance
   - What % of projected synergies should we haircut? (typically 20-30%)

4. **Returns attribution**:
   Total equity value at exit = platform organic growth + multiple arbitrage
     + synergy capture + leverage paydown
   Decompose MOIC into: organic MOIC + M&A contribution
   If organic MOIC is < 1.5x, the strategy is overly dependent on M&A execution
```

### Integration Playbook

```
We just signed an LOI to acquire [add-on target] for our platform [platform name].

Add-on: $[X]M revenue, $[X]M EBITDA, [X] employees, [X] locations
Platform: $[X]M revenue, $[X]M EBITDA

Build a 120-day integration plan:

Pre-close (Day -30 to 0):
- Regulatory/antitrust clearance requirements
- Day 1 communications plan (employees, customers, suppliers)
- IT systems assessment: what can be integrated, what runs standalone?
- Key employee retention agreements (identify critical 10-15 people)

Phase 1 — Stabilize (Days 1-30):
- Retain customers: personal outreach from combined leadership to top 20 accounts
- Retain talent: communicate equity incentives, role clarity, reporting lines
- Quick wins: implement platform procurement contracts on add-on spend
- Financial integration: chart of accounts alignment, reporting consolidation

Phase 2 — Integrate (Days 30-90):
- Consolidate back-office: finance, HR, IT, legal under platform shared services
- Sales integration: cross-selling training, unified CRM, territory alignment
- Branding: migrate to platform brand or maintain as sub-brand?
- Facility rationalization: which locations overlap?

Phase 3 — Optimize (Days 90-120):
- Full P&L integration and synergy tracking vs. plan
- Customer satisfaction pulse check (any attrition signals?)
- Talent assessment: who from add-on is A-player, who is redundant?
- Report synergy capture to the investment committee: actual vs. projected
```

---

## 3. Management Equity Program Design

### Equity Incentive Structuring

```
Design a management equity program for a buyout of [company]:

Transaction details:
- Enterprise value: $[X]M
- Equity check from fund: $[X]M
- Management rollover: $[X]M ([X]% of their existing equity)
- Target hold period: [X] years
- Target exit MOIC: [X]x on total equity

Structure the management equity pool:

1. **Rollover equity**:
   - Management rolls [X]% of proceeds into new equity at same valuation as fund
   - Rollover amount: $[X]M, representing [X]% of total equity
   - Alignment mechanism: management has real money at risk

2. **Sweet equity / option pool**:
   - Pool size: [X]% of fully diluted equity (market: 10-20%)
   - Strike price: at entry valuation (par value or nominal cost)
   - Vesting: [X]% time-based (4-year with 1-year cliff), [X]% performance-based
   - Performance hurdles: vest at [X]x MOIC, full vest at [X]x MOIC, with linear interpolation
   - Good leaver / bad leaver provisions

3. **Ratchet mechanism**:
   - If fund achieves [X]x MOIC, management pool ratchets up to [X]% of equity
   - If fund achieves [X]x MOIC, ratchets to [X]%
   - This creates outsized incentive for management to drive above-target returns
   - Model the dilution impact on fund returns at each ratchet tier

4. **Economic illustration**:
   At [X]x fund MOIC on $[X]M equity:
   - Total equity value: $[X]M
   - Fund share (pre-ratchet): [X]% = $[X]M → [X]x MOIC on fund equity
   - Management share (post-ratchet): [X]% = $[X]M
   - Management total return: rollover return + sweet equity value
   - Management cash-on-cash: $[X]M invested → $[X]M proceeds = [X]x

5. **Tax considerations**:
   - Carried interest vs. ordinary income treatment on sweet equity
   - Section 83(b) election timing for US-based management
   - Structure as partnership profits interests vs. stock options
```

---

## 4. Exit Preparation

### Dual-Track Exit Process

```
We are preparing [portfolio company] for exit. Evaluate a dual-track IPO/M&A process:

Company profile:
- Revenue: $[X]M, growing [X]% organically
- EBITDA: $[X]M, margin [X]%
- Net leverage: [X]x
- Hold period: [X] years
- Equity invested (total including add-ons): $[X]M

IPO track analysis:
- Minimum public market thresholds: revenue, profitability, growth
- Comparable public companies trade at [X-X]x EV/EBITDA
- Expected IPO discount: [X-X]% to trading multiples
- Implied IPO valuation: $[X]M EV → $[X]M equity → [X]x MOIC
- Lock-up period: 180 days (delays full exit by 6+ months)
- Ongoing public company costs: $[X]M/year (audit, compliance, D&O insurance)
- Secondary offering required for full exit (additional 6-12 months)

M&A track analysis:
- Strategic buyers: [list 3-5 with rationale and estimated willingness to pay]
- Expected strategic premium: [X]% over financial buyer price (synergy-driven)
- Secondary buyout: larger PE fund at [X]x (new leverage capacity)
- Expected M&A valuation: $[X]M EV → [X]x MOIC
- Clean exit: full proceeds at close (minus escrow/earnout)

Decision framework:
- If M&A bids exceed IPO valuation by > [X]%, take the M&A exit (certainty premium)
- If IPO valuation is significantly higher, file S-1 but maintain M&A optionality
- Dividend recap consideration: extract $[X]M dividend pre-exit to de-risk
  (Recap math: if we take [X]x dividend now, remaining equity needs only [X]x to hit target)
```

### Vendor Due Diligence Preparation

```
Commission and prepare for vendor due diligence on [portfolio company] ahead of exit:

Reports to commission:
1. **Vendor Financial DD (Quality of Earnings)**:
   - Clean EBITDA bridge with defensible adjustments
   - Normalize for: one-time costs, management fees, run-rate of recent wins
   - Working capital analysis: propose target NWC for SPA
   - Proactive: address known issues before buyer's advisors find them

2. **Commercial DD**:
   - Independent market sizing and competitive positioning
   - Customer reference interviews (pre-select strongest advocates)
   - Addressable market growth validation

3. **IT and Cybersecurity assessment**:
   - Systems architecture overview and technical debt quantification
   - Cybersecurity posture: penetration testing, compliance certifications
   - Migration complexity if buyer wants to re-platform

4. **ESG / Sustainability report**:
   - Carbon footprint baseline and trajectory
   - Workforce diversity metrics, employee engagement scores
   - Governance: board composition, risk management framework

5. **Management presentation polish**:
   - Equity story: "[Company] is the leading [X] in [market] with [X]% market share,
     [X]% organic growth, and a clear pathway to $[X]M EBITDA through [lever 1],
     [lever 2], and continued bolt-on M&A."
   - Leave upside for the buyer: don't show a fully optimized business
   - Projections: budget-plus credibility (slightly above recent run-rate)
```

---

## 5. Co-Investment and LP Communication

### Co-Investment Memo

```
Draft a co-investment memo for [deal name] to present to our LP co-investors:

Investment summary:
- Company: [name], [industry], [geography]
- Transaction: [control buyout / majority recap / take-private]
- Enterprise value: $[X]M ([X]x LTM EBITDA)
- Equity required: $[X]M (fund: $[X]M, co-invest: $[X]M)
- Co-invest allocation: pro-rata to [X] LPs based on [commitment size / relationship tier]
- Co-invest terms: [no fees/no carry / reduced fee and carry]
- Minimum co-invest ticket: $[X]M

Structure the memo:

1. **Executive summary** (1 page):
   - Why we are investing (thesis in 3 bullets)
   - Entry valuation context (vs. precedent transactions)
   - Target returns: [X]x MOIC / [X]% gross IRR over [X] years

2. **Value creation plan**:
   - Lever 1: [operational improvement] → $[X]M EBITDA impact
   - Lever 2: [revenue growth / M&A] → $[X]M EBITDA impact
   - Lever 3: [leverage paydown] → reduces net debt by $[X]M

3. **Risk factors and mitigants**:
   - Risk 1: [describe] → Mitigant: [describe]
   - Downside case: [X]x MOIC (capital preservation even in stress)
   - Key assumption sensitivities table

4. **Returns analysis**:
   Base: [X]x MOIC / [X]% IRR (exit at [X]x in Year [X])
   Bull: [X]x MOIC / [X]% IRR
   Bear: [X]x MOIC / [X]% IRR
   Probability-weighted: [X]x MOIC

5. **ILPA-compliant disclosures**:
   - Conflicts of interest (if any affiliated parties involved)
   - Fund-level concentration (deal as % of fund)
   - Allocation policy for co-invest capacity
   - Timeline: LPs have [X] business days to confirm participation
```

### Quarterly LP Reporting

```
Prepare the quarterly portfolio update for [fund name] as of [quarter-end date]:

Fund-level summary:
- Vintage year: [X]
- Fund size: $[X]B
- Called capital: [X]% ($[X]M)
- Distributions: $[X]M ([X]x DPI)
- NAV: $[X]M
- Total value (NAV + distributions): $[X]M ([X]x TVPI)
- Net IRR since inception: [X]%
- PME (vs. [index]): [X]x

For each portfolio company, report:
1. Company name, sector, investment date, equity invested
2. Current valuation methodology: [comparable trading multiples / DCF / recent transaction]
3. Valuation: current EV, equity value, MOIC (gross), IRR (gross)
4. Operating performance vs. budget:
   - Revenue: actual $[X]M vs. budget $[X]M ([X]% variance)
   - EBITDA: actual $[X]M vs. budget $[X]M
   - Net leverage: [X]x (vs. [X]x at entry)
5. Key developments this quarter (2-3 bullets)
6. Value creation progress vs. 100-day plan / investment thesis

ILPA reporting standards compliance:
- Gross and net returns (net of fees and carry)
- Fee and expense disclosure (management fees, transaction fees, monitoring fees)
- GP commitment: $[X]M ([X]% of fund)
- Carried interest accrued: $[X]M (above [X]% preferred return hurdle)
```

---

## Mathematical Frameworks

**Returns Attribution (Value Bridge)**:

The total return on a buyout investment decomposes into four components:

```
MOIC = (EBITDA_exit / EBITDA_entry)          ... EBITDA growth
     x (Multiple_exit / Multiple_entry)       ... multiple expansion
     x (EV_exit / Equity_exit)               ... leverage effect at exit
     / (EV_entry / Equity_entry)             ... leverage effect at entry
```

Equivalently, the IRR can be decomposed:

```
(1 + IRR)^n ≈ Growth contribution x Margin contribution x Multiple contribution x Leverage contribution

Where:
  Growth contribution = Revenue_exit / Revenue_entry
  Margin contribution = Margin_exit / Margin_entry
  Multiple contribution = EV/EBITDA_exit / EV/EBITDA_entry
  Leverage contribution = (EV/Equity)_entry / (EV/Equity)_exit  [deleveraging effect]
```

**Entry Multiple and Break-Even**:

```
Maximum entry multiple = Exit EBITDA x Exit Multiple - Net Debt at Exit
                         ÷ Equity Invested
                         solved for target MOIC

Break-even EBITDA = (Equity Invested + Net Debt at Exit) / Exit Multiple
  If exit EBITDA falls below this level, equity value = 0
```

**Dividend Recap Math**:

```
Pre-recap equity invested: $E
Dividend extracted: $D (funded by incremental debt)
Remaining equity at risk: $E - $D (but technically still $E invested)
Required exit equity for target MOIC:
  Without recap: Target MOIC x $E
  With recap: (Target MOIC x $E) - $D ... from remaining equity at exit
Effective MOIC on remaining capital = (Exit equity - D) / E
  But total MOIC = (D + Exit equity) / E ... always higher with successful recap
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Core LBO math, deal screening, due diligence, 100-day plan
- [`growth-equity.md`](growth-equity.md) — Minority investing, growth metrics, governance protections
- [`private-credit.md`](private-credit.md) — Debt structuring and covenant design (relevant for LBO financing)
- [`special-situations.md`](special-situations.md) — Distressed buyouts, structured equity, rescue financing
