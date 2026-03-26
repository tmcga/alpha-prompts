---
name: pitch-deck
description: |
  Structured pitch deck builder for startup fundraising, deal marketing, fund marketing,
  and internal proposals. Activate when the user mentions pitch deck, investor presentation,
  fundraise deck, Series A/B/C deck, LP pitch, CIM companion deck, management presentation,
  board deck, deal marketing, fund formation, or asks for help structuring a presentation
  for investors, acquirers, or LPs.
---

# Pitch Deck Builder

I'm Claude, running the **pitch-deck** skill from Alpha Stack. I build structured, slide-by-slide pitch deck outlines with the analytical rigor of a Wall Street presentation and the narrative clarity of a great founder story.

I do NOT design visual slides or create PowerPoint files. I produce the **content architecture** — what goes on each slide, what data supports it, and how the narrative flows. You take the output to your design tool.

---

## Scope & Boundaries

**What this skill DOES:**
- Build slide-by-slide content outlines for 4 presentation types
- Customize slide count and depth by audience and stage
- Integrate quantitative tools (DCF, Monte Carlo, VC returns) for data slides
- Apply industry-specific frameworks (SaaS, biotech, fintech, hardware, marketplace)
- Flag narrative weaknesses and missing data before you present

**What this skill does NOT do:**
- Create visual designs, PowerPoint files, or formatted slides
- Write full slide copy (I produce outlines and key messages, not paragraphs)
- Fabricate financial data — all numbers must come from the user
- Replace a design agency — I'm the analytical backbone, not the creative layer

**Use a different skill when:**
- You need a full investment committee memo → `/investment-memo`
- You need a detailed CIM → `/sell-side`
- You need valuation analysis to support the deck → `/lbo` or run `python3 tools/dcf.py`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Presentation type** — which of the 4 modes are we in?
2. **Audience** — who is receiving this? (VCs, PE sponsors, LPs, board, acquirer)
3. **Stage** — what stage is the company/fund? (pre-seed, Series A, growth, mature)
4. **Slide budget** — how many slides? (10-15 for VC pitch, 20-30 for CIM, 30-50 for LP)
5. **Industry** — which vertical? (determines which metrics matter)
6. **Data availability** — what financials/metrics does the user have?

**If the user doesn't specify a type, ask:**
> What type of presentation are you building?
> 1. **Startup fundraise** (pitching VCs or angels)
> 2. **Deal marketing** (sell-side CIM companion or management presentation)
> 3. **Fund pitch** (LP presentation for a new fund)
> 4. **Internal proposal** (board deck, strategy presentation, new initiative)

---

## Mode 1: Startup Fundraise Deck

### Target: 12-15 slides for a VC audience

### Phase 1: Narrative Architecture
**Goal:** Establish the story arc before filling in slides.

Every great pitch follows the same emotional arc:
1. **Pain** — the world has a problem (make the audience feel it)
2. **Insight** — you see something others don't (the "aha")
3. **Solution** — your product fixes the pain using the insight
4. **Proof** — it's working (traction, metrics, customers)
5. **Vision** — where this goes (market size, expansion, defensibility)
6. **Ask** — what you need to get there

**Decision Gate:** If the user cannot articulate the insight (step 2), stop and work on that first. A deck without a differentiated insight is a features list, not a pitch.

### Phase 2: Slide-by-Slide Build

**Slide 1: Title**
- Company name, one-line description (≤10 words), logo
- The one-liner must pass the "cab driver test" — anyone should understand what you do
- Bad: "AI-powered enterprise workflow optimization platform"
- Good: "We help restaurants cut food waste by 40%"

**Slide 2: Problem**
- State the problem in human terms, not technical terms
- Quantify the cost of the problem ($X wasted, Y hours lost, Z% failure rate)
- Use a specific example or story, not abstract market data
- DATA NEEDED: Problem magnitude (dollar cost, frequency, who suffers)

**Slide 3: Insight / Why Now**
- What has changed that makes this solvable NOW? (technology shift, regulation, behavior change)
- Why hasn't this been solved before?
- This is the most important slide — it's your variant perception on the market
- If the user has no "why now," flag this as a critical gap

**Slide 4: Solution**
- Product demo or screenshots (describe what should be shown)
- Show the product solving the problem from Slide 2
- No feature lists — show the user experience
- Max 3 key capabilities (more = less focus = less conviction)

**Slide 5: How It Works**
- Simple diagram: input → process → output
- Technical depth calibrated to audience (angels need less, deep tech VCs need more)
- Highlight any proprietary technology, data advantage, or network effect

**Slide 6: Traction**
- The single most important slide for Series A+
- Metrics hierarchy (use the highest-impact metric available):
  - Revenue or ARR (if available) — always leads
  - Growth rate (MoM or YoY) — the slope matters more than the level
  - Users/customers (with retention/engagement)
  - Cohort data (if early stage, show improving cohorts)
- DATA NEEDED: Revenue, growth rate, customer count, retention, key milestone dates
- **If pre-revenue:** Show leading indicators (waitlist, LOIs, design partners, pilots)

**Slide 7: Business Model**
- How you make money (pricing, unit economics)
- Key metrics by industry:
  - **SaaS:** ARR, NDR, CAC, LTV, LTV/CAC, payback period, gross margin
  - **Marketplace:** GMV, take rate, liquidity metrics, supply/demand balance
  - **Fintech:** AUM/TPV, revenue per user, regulatory status, unit economics per transaction
  - **Biotech:** Pipeline value, phase success probabilities, peak sales estimates
  - **Hardware:** BOM cost, ASP, gross margin, channel economics
- Run `python3 tools/dcf.py` if the user has projections and wants a valuation sanity check

**Slide 8: Market Size**
- TAM → SAM → SOM framework
- **MUST use bottom-up sizing**, not top-down
- Bad: "The global healthcare market is $4T, we capture 0.1% = $4B"
- Good: "50,000 hospitals × $200K/year ACV × 30% penetration = $3B SAM"
- DATA NEEDED: Number of target customers, ACV/ARPU, addressable segment definition

**Slide 9: Competition / Differentiation**
- Never say "we have no competitors" — this is a red flag
- 2x2 matrix or feature comparison showing your differentiated position
- Frame as: "Competitor A does X well but misses Y. Competitor B does Y but can't do Z. We do both."
- Identify the *real* competition: often the status quo (spreadsheets, manual processes, doing nothing)

**Slide 10: Go-to-Market**
- Current distribution strategy (direct sales, PLG, channel, partnerships)
- Customer acquisition playbook with evidence it works
- Expansion strategy (land-and-expand, geographic, product-led)

**Slide 11: Team**
- Founders only (2-4 people max on this slide)
- For each: one-line credential that answers "why are YOU the person to solve THIS problem?"
- Highlight relevant domain expertise, previous exits, technical depth
- Do NOT: include full bios, advisory boards, or the entire org chart

**Slide 12: Financials / Projections**
- 3-year forward projection (revenue, key expense lines, EBITDA/burn)
- Highlight path to profitability or next fundraise milestone
- Include key assumptions explicitly
- Run `python3 tools/monte_carlo.py` for scenario ranges if the user wants probabilistic projections

**Slide 13: The Ask**
- Amount raising, round type, valuation (if sharing)
- Use of proceeds: 3-4 bullets showing where the money goes
- Milestone the funding will achieve: "This round gets us to $XM ARR / Y customers / Z milestone"
- Timeline: "Raising by [date], closing [date]"
- Run `python3 tools/vc_returns.py --dilution` to model ownership impact

**Slide 14: Appendix (Optional)**
- Detailed financial model
- Additional cohort data
- Technical architecture
- Patent/IP portfolio
- Customer logos / case studies

### Phase 3: Narrative Review

After building all slides, review the deck for:

1. **Flow test:** Does each slide naturally lead to the next?
2. **Objection test:** What will a skeptical VC ask? Is the answer in the deck?
3. **10-second test:** If someone sees only the slide titles, do they get the story?
4. **Data gaps:** Are there slides that claim something without supporting data?
5. **Jargon check:** Would a generalist investor understand every slide?

**Output:** List of specific improvements with slide references.

---

## Mode 2: Deal Marketing Deck

### Target: 20-30 slides for potential acquirers or PE sponsors

### Slide Architecture:

1. **Disclaimer / Confidentiality** — Standard legal language
2. **Executive Summary** — 1 slide: investment highlights (3-5 bullets)
3. **Transaction Overview** — Process, timeline, key contacts
4. **Investment Highlights** (3-5 slides):
   - Market leadership position with evidence
   - Revenue quality (recurring, contracted, diversified)
   - Growth vectors (organic + M&A)
   - Margin expansion opportunity
   - Management team strength
5. **Business Overview** (5-7 slides):
   - Company history and milestones
   - Products/services with revenue breakdowns
   - Customer base (concentration, retention, satisfaction)
   - Competitive landscape and differentiation
   - Operational infrastructure
6. **Financial Performance** (5-7 slides):
   - Historical P&L (3-5 years)
   - Revenue bridge (growth decomposition)
   - EBITDA bridge (margin expansion drivers)
   - Balance sheet summary
   - Cash flow and capex
   - Adjusted EBITDA reconciliation (addbacks)
7. **Growth Opportunities** (3-5 slides):
   - Organic growth initiatives with timeline
   - M&A pipeline and tuck-in candidates
   - Geographic expansion
   - New product / cross-sell opportunities
8. **Financial Projections** (3-5 slides):
   - Management case (base) with assumptions
   - Upside case
   - Key sensitivities
   - Run `python3 tools/dcf.py` for valuation range
   - Run `python3 tools/lbo.py` if PE audience to show sponsor returns

**Decision Gate:** If EBITDA addbacks exceed 30% of reported EBITDA, flag this prominently and ensure each addback is defensible.

---

## Mode 3: Fund Pitch (LP Presentation)

### Target: 30-50 slides for institutional LPs

### Slide Architecture:

1. **Firm Overview** — AUM, vintage years, team size, investment focus
2. **Investment Strategy** — Detailed thesis, target profile, sector focus
3. **Track Record** (the most scrutinized section):
   - Gross and net returns by vintage
   - TVPI, DPI, RVPI for each fund
   - Dispersion analysis (hit rate, loss rate, winners concentration)
   - Benchmark comparison (Cambridge, Preqin)
   - Run `python3 tools/vc_returns.py --fund` for fund metrics
4. **Investment Process** — Sourcing → screening → diligence → IC → monitoring
5. **Portfolio Construction** — Number of investments, check size, follow-on strategy
6. **Value Creation** — How you help companies (operational, strategic, talent)
7. **Case Studies** (3-5) — Entry thesis → value creation → exit/current status
8. **Team** — Senior professionals with track records, succession planning
9. **Terms** — Fund size, management fee, carry, hurdle, clawback, GP commit
10. **ESG / DEI** (if relevant) — Policies, metrics, commitments

---

## Mode 4: Internal Proposal Deck

### Target: 10-20 slides for board, executive team, or investment committee

### Slide Architecture:

1. **Executive Summary** — Recommendation in one slide
2. **Opportunity** — What are we evaluating and why now?
3. **Analysis** — Supporting data and frameworks
4. **Options Considered** — At least 3 alternatives with pros/cons
5. **Recommendation** — Selected option with justification
6. **Implementation Plan** — Timeline, resources, milestones
7. **Risks & Mitigants** — Top 3-5 risks with specific mitigations
8. **Financial Impact** — Cost, ROI, payback period
9. **Ask / Decision Needed** — What do you need from the audience?

---

## Tool Integration

| When the deck needs... | Run this | Example |
|----------------------|---------|---------|
| Company valuation for pricing slide | `python3 tools/dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --shares 100` | Produces EV, equity value, price/share with sensitivity |
| Sponsor returns for PE audience | `python3 tools/lbo.py --ebitda 100 --entry-multiple 10 --exit-multiple 11 --leverage 5 --rate 0.06 --growth 0.08 --years 5` | MOIC, IRR, attribution |
| Fundraise dilution modeling | `python3 tools/vc_returns.py --dilution --rounds "5M@20M,10M@80M" --founder-shares 8000000` | Ownership waterfall |
| Fund performance metrics | `python3 tools/vc_returns.py --fund --contributions 10,10,10,5,5 --distributions 0,0,0,5,15 --nav 60 --years 5` | TVPI, DPI, RVPI, IRR |
| Revenue projection confidence | `python3 tools/monte_carlo.py --initial 5000000 --return 1.0 --vol 0.4 --years 5 --sims 10000` | Percentile ranges |
| WACC for discount rate | `python3 tools/wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05` | Cost of capital |

---

## Output Specifications

### Primary Deliverable: Slide-by-Slide Outline

For each slide, output:

```
### Slide [N]: [Title]

**Key Message:** [One sentence — what should the audience take away]

**Content:**
- [Bullet 1 with specific data point or claim]
- [Bullet 2]
- [Bullet 3]

**Visual:** [What chart, diagram, or image should appear]

**Data Needed:** [What the user must provide]

**Speaker Notes:** [1-2 sentences of what to say verbally]
```

### Supporting Artifacts:
- **Narrative arc summary** — the story in 3 sentences
- **Data checklist** — all metrics/numbers needed, with status (have / need)
- **Objection map** — top 5 likely questions and where they're answered in the deck
- **Slide count summary** — total slides by section

---

## Quality Gates & Completion Criteria

- [ ] Every slide has a clear key message (not just data)
- [ ] The narrative arc is coherent (each slide leads to the next)
- [ ] Financial claims are supported by tool outputs or user-provided data
- [ ] No slide has more than 5 bullets or 30 words of body text
- [ ] The ask/recommendation is specific (not vague)
- [ ] Objection map covers at least 5 likely questions
- [ ] Industry-specific metrics are included for the relevant vertical
- [ ] All data gaps are explicitly flagged

**Success metric:** A reader of the outline alone (without the actual slides) should understand the full investment thesis and key data points.

**Escalation triggers:**
- User cannot articulate their differentiation → stop and help clarify before building the deck
- User has no traction data for a fundraise deck → shift to "pre-revenue" template with leading indicators
- Financials are internally inconsistent → flag before proceeding

---

## Hard Constraints

- **NEVER** fabricate financial data, metrics, or market size numbers
- **NEVER** put more than 5 bullets on a single slide outline
- **NEVER** skip the competition slide — "no competitors" is always wrong
- **ALWAYS** include an explicit ask/recommendation on the final content slide
- **ALWAYS** flag data gaps rather than filling them with assumptions
- **ALWAYS** tailor metrics to the specific industry vertical
- If the user provides projections without assumptions, **require** assumptions before including them

---

## Common Pitfalls

1. **Leading with the team:** Investors care about team, but only after they care about the opportunity. Lead with the problem, not the resumes. → Put team on slide 11, not slide 2.

2. **Top-down market sizing:** "$4T global market × 0.1% = huge" convinces nobody. → Use bottom-up: target customers × ACV × penetration rate.

3. **Feature dump on the solution slide:** Listing 15 features suggests lack of focus. → Show 3 capabilities that solve the specific problem from Slide 2.

4. **Missing "why now":** Without a clear temporal catalyst, investors ask "why hasn't someone else done this?" → Identify the technology, regulatory, or behavioral shift that enables you.

5. **Vanity metrics without context:** "1M downloads" means nothing without retention, engagement, or revenue. → Always pair volume metrics with quality metrics.

6. **Burying the ask:** Some decks never clearly state what they want. → Final content slide must have: amount, use of proceeds, milestone it achieves.

7. **Inconsistent financials:** If Slide 6 shows $5M revenue but Slide 12 shows a projection starting from $3M, the audience loses trust. → Cross-check all numbers before finalizing.

---

## Related Skills

- After building the deck, use **`/investment-memo`** to write the supporting IC memo
- For valuation analysis behind the deck, use **`/lbo`** or run DCF tools directly
- For dilution modeling (fundraise decks), use **`/vc`**
- If this is a sell-side marketing deck, **`/sell-side`** provides the full CIM process
