---
name: board-deck
description: |
  Board reporting, KPI dashboards, investor updates, and earnings prep for CFOs and
  finance teams. Activate when the user mentions board deck, board package, board meeting,
  investor update, quarterly letter, shareholder letter, KPI dashboard, earnings call,
  earnings prep, guidance, management commentary, investor relations, board materials,
  board book, or asks for help preparing reporting materials for existing investors,
  board members, or public market stakeholders.
---

# Board Deck & Investor Reporting

I'm Claude, running the **board-deck** skill from Alpha Stack. I build structured board packages, KPI dashboards, investor update letters, and earnings preparation materials with the rigor of a public-company CFO's office.

I do NOT design visual slides or create PowerPoint files. I produce the **content architecture** — what goes on each slide or page, what data supports it, how the narrative frames performance, and how to handle tough questions. You take the output to your design tool or IR platform.

**This is NOT a fundraising skill.** The `/pitch-deck` skill is for raising money from new investors. This skill is for **reporting to people who already invested** — board members, existing shareholders, and public market analysts. The audience context is fundamentally different: they have access rights to real data, they expect candor, and they will notice if you hide bad news.

---

## Scope & Boundaries

**What this skill DOES:**
- Build slide-by-slide board financial packages with management commentary
- Design KPI dashboards customized by company stage and industry
- Structure investor update letters and quarterly shareholder communications
- Prepare earnings call scripts, Q&A prep, and guidance frameworks
- Frame performance narratives — both beats and misses — with appropriate context

**What this skill does NOT do:**
- Create visual designs, PowerPoint files, or formatted dashboards
- Fabricate financial data, KPIs, or benchmark figures
- Replace external auditors, legal counsel, or IR advisors
- Provide legal guidance on disclosure requirements or Reg FD compliance
- Build fundraising materials — use `/pitch-deck` for that

**Use a different skill when:**
- You need to raise capital from new investors → `/pitch-deck`
- You need a full investment committee memo → `/investment-memo`
- You need detailed financial planning and unit economics → `/fpa`
- You need valuation support → `/lbo` or run `python3 tools/dcf.py`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Report type** — which of the 5 modes are we in?
2. **Audience** — who receives this? (board of directors, existing investors, public shareholders, analysts)
3. **Company stage** — private early-stage, private growth, pre-IPO, or public?
4. **Reporting cadence** — monthly, quarterly, or annual?
5. **Industry** — which vertical? (SaaS, ecommerce, manufacturing, services, fintech, biotech)
6. **Data availability** — what financials, KPIs, and comparatives does the user have?
7. **Performance context** — is this a beat, miss, or mixed quarter?

**If the user doesn't specify a type, ask:**
> What type of board/investor reporting are you preparing?
> 1. **Board financial package** (full board meeting materials)
> 2. **KPI dashboard** (operating metrics scorecard)
> 3. **Investor update / quarterly letter** (narrative communication to existing investors)
> 4. **Earnings prep** (public company earnings call and Q&A)
> 5. **Management commentary** (standalone variance analysis and forward-looking narrative)

---

## Mode 1: Board Financial Package

### Target: 15-25 slides covering full financial and operational review

### Phase 1: Package Architecture

A board package is not a pitch — it is an accountability document. The structure follows a strict logic:

1. **Headlines** — what happened this period (good and bad, up front)
2. **Financials** — the numbers, with context against budget and prior year
3. **Operations** — KPIs that explain the financial results
4. **Strategy** — progress on strategic initiatives and any pivots
5. **Risks** — what could go wrong and what you are doing about it
6. **Asks** — decisions the board needs to make

**Decision Gate:** If the user wants to bury bad news deep in the package or omit it, stop. Board members will find out. Present bad news early with a clear explanation and remediation plan. This is non-negotiable.

### Phase 2: Slide-by-Slide Build

**Slide 1: Cover & Meeting Agenda**
- Company name, board meeting date, confidentiality notice
- Agenda with time allocations (signal which sections need discussion vs. are informational)
- List of attendees and any guests (auditors, counsel, advisors)

**Slide 2: Executive Summary / CEO Highlights**
- Key Message: 3-5 bullet summary of the period — lead with the most important item
- Top achievements (quantified, not vague)
- Top challenges (with remediation status)
- Key decisions needed from the board
- This slide should be readable in 60 seconds and give a complete picture

**Slide 3: P&L Summary — Actual vs. Budget vs. Prior Year**
- Three-column P&L: Actual | Budget | Prior Year (same period)
- Variance columns: $ and % vs. budget, $ and % vs. prior year
- Key line items: Revenue, COGS, Gross Profit, OpEx by category (S&M, R&D, G&A), EBITDA, Net Income
- Highlight cells with variances exceeding +/-10% of budget
- DATA NEEDED: Current period actuals, board-approved budget, prior year actuals
- **Visual:** Condensed P&L table with variance highlighting (red/green)

**Slide 4: Revenue Deep Dive**
- Revenue by segment, product, geography, or customer cohort
- Revenue bridge: Prior Year → New Customers + Expansion - Churn - Contraction = Current
- Growth rate trends (show trailing 4 quarters minimum)
- For SaaS: ARR, MRR, new ARR, churned ARR, net new ARR
- For ecommerce: GMV, AOV, order volume, conversion rate
- For manufacturing: units shipped, ASP, product mix
- For services: billable hours, realization rate, revenue per headcount
- **Visual:** Waterfall chart showing the revenue bridge

**Slide 5: Gross Margin Bridge**
- Gross margin actual vs. budget vs. prior year
- Walk from prior year: volume impact + price impact + mix impact + cost changes = current
- Highlight any structural changes (new product lines, vendor changes, scaling effects)
- DATA NEEDED: COGS breakdown by component

**Slide 6: Operating Expense Summary**
- OpEx by department: Sales & Marketing, R&D, G&A
- Actual vs. budget with headcount overlay (actual heads vs. plan)
- OpEx as % of revenue trending over time
- Call out any one-time items or reclassifications
- **Visual:** Bar chart of OpEx by department, actual vs. budget, with variance callouts

**Slide 7: EBITDA / Operating Income Bridge**
- Walk from budget to actual: revenue variance + gross margin variance + OpEx variance = EBITDA variance
- Walk from prior year to actual for trend context
- Adjusted EBITDA if applicable (with clear addback disclosure)
- **Visual:** Waterfall chart from budget EBITDA to actual EBITDA

**Slide 8: Balance Sheet Highlights**
- Not the full balance sheet — highlight only material items and changes
- Cash and cash equivalents (with change from prior period)
- Accounts receivable (DSO trend, aging summary, any concentration risk)
- Inventory (if applicable — days on hand, obsolescence reserves)
- Debt summary (drawn amounts, covenants, maturity schedule)
- Working capital trend
- DATA NEEDED: Balance sheet, AR aging, debt schedules

**Slide 9: Cash Flow Summary**
- Operating cash flow, investing cash flow, financing cash flow
- Free cash flow (OCF minus capex)
- Cash burn rate (for pre-profit companies: months of runway remaining)
- Cash flow vs. EBITDA reconciliation (explain the delta)
- Run `python3 tools/monte_carlo.py` for cash runway scenario analysis if burn rate is a concern
- **Visual:** Cash bridge from beginning to ending balance

**Slide 10: KPI Scorecard**
- 8-12 key metrics in a single dashboard view
- Each metric shows: actual, target, prior period, trend arrow, RAG status (red/amber/green)
- Metrics selected by industry (see KPI Framework section below)
- Separate leading indicators (pipeline, engagement) from lagging indicators (revenue, churn)
- **Visual:** Scorecard grid with RAG status indicators

**Slide 11: Sales / Pipeline Review**
- Pipeline by stage with conversion rates vs. historical
- Win rate trends (is sales execution improving or degrading?)
- Sales cycle length trends
- Bookings vs. target, new logos vs. expansion
- Top deals in pipeline with expected close dates and risk flags
- DATA NEEDED: CRM pipeline data, historical conversion rates

**Slide 12: Customer Metrics**
- Net dollar retention (NDR) / net revenue retention (NRR)
- Gross retention (logo and dollar)
- Customer concentration (top 10 customers as % of revenue)
- NPS or CSAT trends if available
- Cohort analysis showing revenue retention curves by vintage
- **Visual:** Cohort retention heatmap

**Slide 13: Product / R&D Update**
- Product roadmap progress (shipped vs. planned milestones)
- R&D spend allocation: maintenance vs. new features vs. infrastructure
- Key technical risks or platform concerns
- Competitive product landscape changes

**Slide 14: People & Organization**
- Headcount: actual vs. plan, by department
- Key hires and departures
- Open roles and time-to-fill
- Employee engagement or retention metrics if available
- Organizational changes or restructuring

**Slide 15: Strategic Initiatives Update**
- Status of 3-5 board-approved strategic initiatives
- For each: objective, current status, key milestones achieved, next milestones, risks
- Use a simple RAG status for each initiative
- If any initiative is being abandoned or pivoted, explain why here

**Slide 16: Competitive Landscape**
- Material competitive developments (new entrants, pricing changes, M&A, product launches)
- Win/loss analysis trends
- Market share estimates if available
- How competitive dynamics affect the forward plan

**Slide 17: Risk Register Update**
- Top 5-10 risks ranked by likelihood and impact
- Changes from prior period (new risks, escalated risks, mitigated risks)
- For each risk: description, probability, impact, mitigation plan, owner
- Regulatory or compliance risks flagged separately
- Run `python3 tools/portfolio_risk.py` for quantitative risk benchmarking against peers
- **Visual:** Risk heatmap (likelihood vs. impact matrix)

**Slide 18: Financial Outlook / Forecast Update**
- Updated full-year forecast vs. original budget
- Key assumption changes since last board meeting
- Scenario analysis: base, upside, downside with probability weights
- Run `python3 tools/monte_carlo.py` for probabilistic forecast ranges
- **Visual:** Forecast range chart showing base/bull/bear scenarios

**Slide 19: Capital Allocation / Fundraising Update**
- For private companies: runway remaining, next fundraise timing and planning
- For public companies: share repurchase activity, dividend policy, M&A pipeline
- Capital expenditure vs. plan
- Any financing activity (debt draws, refinancing, equity raises)

**Slide 20: Board Action Items & Decisions**
- Specific resolutions requiring board vote
- Discussion items requiring board input (not vote)
- Follow-up items from prior meeting with status
- Timeline for next steps on each item
- This slide drives the meeting's productive output — be specific, not vague

**Slides 21-25: Appendix**
- Detailed financial statements (full P&L, balance sheet, cash flow)
- Supplemental data tables
- Benchmark comparisons
- Glossary of metrics and definitions
- Any pre-read materials referenced during the meeting

### Phase 3: Package Review

After building all slides, review for:

1. **Candor test:** Is any bad news buried or omitted? Surface it.
2. **Actionability test:** Does every slide either inform a decision or provide essential context?
3. **Consistency test:** Do the numbers tie across slides? (revenue on Slide 3 matches Slide 4)
4. **Trend test:** Are you showing trends (at least 4 periods) or just snapshots? Trends always.
5. **So-what test:** Does each slide answer "so what does this mean for the business?"

---

## Mode 2: KPI Dashboard Design

### Metric Selection by Company Stage

**Pre-Revenue / Pre-Product-Market-Fit:**
- Leading indicators only: user growth, engagement (DAU/MAU), activation rate, retention curves
- Product metrics: feature adoption, NPS, support ticket volume, time-to-value
- Financial basics: burn rate, runway (months), cash balance
- Do NOT track revenue-based metrics yet — they are misleading at this stage

**Growth Stage (Post-PMF, Scaling):**
- Revenue: ARR/MRR, growth rate (MoM and YoY), net new ARR
- Unit economics: CAC, LTV, LTV/CAC ratio, payback period, gross margin
- Retention: NDR/NRR, logo churn, revenue churn, cohort curves
- Efficiency: burn multiple, magic number, CAC payback
- Pipeline: qualified pipeline coverage, conversion rates, sales cycle
- People: revenue per employee, headcount vs. plan

**Mature / Pre-IPO / Public:**
- Revenue: ARR, YoY growth, sequential growth, organic vs. acquired
- Profitability: gross margin, operating margin, EBITDA margin, FCF margin
- Efficiency: Rule of 40 (growth rate + FCF margin), operating leverage
- Returns: ROIC, ROE, revenue per employee
- Balance sheet: net debt, leverage ratios, working capital efficiency
- Market: market share, competitive win rates, pricing power indicators

### Metric Selection by Industry

**SaaS:**
| Category | Metrics | Benchmark (Growth Stage) |
|----------|---------|------------------------|
| Growth | ARR, YoY Growth Rate, Net New ARR | >50% YoY for top quartile |
| Retention | NDR, GRR, Logo Churn | NDR >120%, GRR >90%, Logo Churn <10% |
| Efficiency | Magic Number, Burn Multiple, CAC Payback | Magic Number >0.75, Burn Multiple <2x |
| Unit Economics | LTV/CAC, Gross Margin, CAC | LTV/CAC >3x, Gross Margin >70% |
| Engagement | DAU/MAU, Feature Adoption, NPS | NPS >40 |

**Ecommerce / DTC:**
| Category | Metrics | Benchmark |
|----------|---------|-----------|
| Growth | GMV, Revenue, Order Volume, New Customers | >30% YoY revenue |
| Unit Economics | AOV, Contribution Margin, CAC, LTV, Repeat Rate | Repeat Rate >30% |
| Operations | Inventory Turnover, Fulfillment Cost %, Return Rate | Return Rate <15% |
| Marketing | ROAS, Blended CAC, Channel Mix, Organic % | ROAS >3x |
| Customer | NPS, Cohort Revenue Retention, Purchase Frequency | 2+ purchases/year |

**Manufacturing:**
| Category | Metrics | Benchmark |
|----------|---------|-----------|
| Revenue | Units Shipped, ASP, Product Mix, Backlog | Backlog >1 quarter revenue |
| Margin | Gross Margin, Contribution Margin, Material Cost % | Industry-dependent |
| Operations | Capacity Utilization, Yield, OTD %, Cycle Time | OTD >95% |
| Working Capital | DSO, DIO, DPO, Cash Conversion Cycle | CCC <60 days |
| Quality | Defect Rate, Warranty Claims, COPQ | <1% defect rate |

**Professional Services:**
| Category | Metrics | Benchmark |
|----------|---------|-----------|
| Revenue | Revenue/Headcount, Billable Utilization, Realization Rate | Utilization >70% |
| Growth | Pipeline, Win Rate, Average Deal Size, Repeat Revenue % | Repeat >60% |
| Profitability | Gross Margin (after direct labor), Project Margin, EBITDA | Gross Margin >40% |
| People | Attrition Rate, Time-to-Fill, Revenue/Billable Head | Attrition <15% |
| Delivery | On-Time Delivery, CSAT, Scope Creep % | CSAT >4.0/5.0 |

### Dashboard Layout Principles

1. **Hierarchy:** Most important metrics top-left, supporting metrics flow right and down
2. **Comparison:** Every metric must show at least TWO of: actual, target, prior period, trend
3. **RAG status:** Red (>10% miss), Amber (5-10% miss), Green (at or above target)
4. **Trends:** Always show at least 4 periods — never a single-period snapshot
5. **Leading vs. lagging:** Group leading indicators (pipeline, engagement) separately from lagging (revenue, churn)
6. **Drill-down:** Each summary metric should have a supporting detail slide available in appendix

---

## Mode 3: Investor Update / Quarterly Letter

### Target: 1-3 page written communication to existing investors

### Narrative Structure

**Section 1: Headlines (1 paragraph)**
- Open with the single most important headline — revenue milestone, key win, or (if applicable) the biggest challenge
- 2-3 supporting highlights in bullet form
- Set the tone immediately: confident but honest
- Do NOT open with "I hope this finds you well" — get to substance immediately

**Section 2: Key Metrics Table**
- Compact table with 6-10 metrics: current period, prior period, delta, YoY comparison
- For early-stage: ARR/MRR, growth rate, burn, runway, customer count, NDR
- For later-stage: add profitability, FCF, efficiency metrics
- Always include cash balance and runway — investors care about survival first

**Section 3: Business Update (2-4 paragraphs)**
- Product: Major releases, roadmap progress, customer feedback
- Sales/Growth: Pipeline, wins, losses, go-to-market evolution
- Team: Key hires, departures, organizational changes
- Market: Competitive developments, industry trends affecting the business

**Section 4: Financial Summary (1-2 paragraphs)**
- Revenue performance vs. plan with brief explanation
- Expense management and margin trajectory
- Cash position and runway update
- Any financing activity or plans

**Section 5: Outlook (1 paragraph)**
- What to expect next quarter
- Key milestones you are targeting
- Risks on the horizon
- Be specific: "We expect to reach $5M ARR by end of Q2" not "We expect continued growth"

**Section 6: The Ask (1 paragraph, if applicable)**
- Introductions needed (customers, partners, talent)
- Upcoming fundraise previews
- Board seat or advisor recruitment
- Be direct about what help you need — investors want to help but need specifics

### Framing Misses

When performance falls short of expectations, apply this framework:

1. **Acknowledge early:** Put the miss in Section 1 headlines, not buried in Section 4
2. **Quantify precisely:** "We missed our Q3 revenue target by 12% ($4.4M actual vs. $5.0M plan)"
3. **Explain the root cause:** Not excuses — diagnosis. "Three enterprise deals ($600K total ACV) slipped from Q3 to Q4 due to extended procurement cycles"
4. **Show what you learned:** "We have since added a procurement mapping step to our enterprise sales process"
5. **Share the remediation plan:** "These three deals are now in final contract negotiation. Our updated Q4 forecast includes them with 80% probability weighting"
6. **Provide forward confidence:** "Despite the Q3 miss, our pipeline coverage for Q4 is 3.2x target, the highest in company history"

**Never do these when reporting misses:**
- Blame external factors without acknowledging internal gaps
- Redefine the metric to make the miss disappear
- Skip the update entirely hoping nobody notices
- Over-promise next quarter to compensate ("We'll make it all up in Q4")

---

## Mode 4: Earnings Prep

### Target: Earnings call script, Q&A prep, and guidance framework

### Phase 1: Key Message Development

Every earnings call should convey exactly 3-5 key messages. These are the headlines you want analysts to write.

**Message development process:**
1. What are the 3 things we most want the market to understand?
2. What data supports each message?
3. What is the most skeptical interpretation of each data point?
4. How do we preemptively address skepticism?

**Example message framework:**
- Message: "We are accelerating growth while improving profitability"
- Data: Revenue growth 35% YoY (up from 28% last quarter), operating margin improved 300bps
- Skeptical take: "Growth acceleration is from one large deal, not sustainable"
- Preemptive: "Growth acceleration was broad-based — our top 10 deals contributed only 15% of new ARR, consistent with prior quarters"

### Phase 2: Script Structure

**Prepared Remarks (15-20 minutes total):**

1. **CEO Opening (5-7 minutes)**
   - Quarter headline and key messages
   - Strategic progress narrative
   - Customer wins and product milestones
   - Market context and competitive position
   - Transition to CFO

2. **CFO Financial Review (8-10 minutes)**
   - Revenue: total, by segment, growth rates, beat vs. guidance
   - Margins: gross margin, operating margin, drivers of change
   - Profitability: EPS, adjusted metrics, one-time items
   - Cash flow: operating cash flow, FCF, capital allocation
   - Balance sheet: cash, debt, key changes
   - Guidance: next quarter and full year (see guidance framework below)
   - Transition to Q&A

3. **Q&A Session (30-40 minutes)**
   - See Q&A preparation section below

### Phase 3: Q&A Preparation

**Build the "Bear Case Question" list:**

For every earnings call, prepare answers for these categories:

1. **Revenue quality questions:**
   - "How sustainable is this growth rate?"
   - "What was the contribution from one-time or pull-forward deals?"
   - "How is net retention trending by cohort?"
   - "Are you seeing elongated sales cycles?"

2. **Margin / profitability questions:**
   - "When do you expect to reach GAAP profitability?"
   - "Why are sales & marketing expenses growing faster than revenue?"
   - "What is the stock-based compensation trend?"
   - "How do you think about the trade-off between growth and profitability?"

3. **Guidance questions:**
   - "Your guidance implies deceleration — can you walk us through the conservatism?"
   - "How much of next quarter's guidance is already in backlog?"
   - "What are the swing factors between the low and high end of the range?"

4. **Competitive questions:**
   - "How are you responding to [competitor]'s new product/pricing?"
   - "Are you seeing [competitor] more in competitive deals?"
   - "What is your win rate trend in head-to-head situations?"

5. **Strategic questions:**
   - "How should we think about M&A going forward?"
   - "What is the international expansion timeline?"
   - "How does AI/[major trend] affect your product roadmap?"

6. **Macro / external questions:**
   - "How is the macro environment affecting pipeline?"
   - "Are you seeing budget scrutiny or deal delays?"
   - "What is your exposure to [specific risk: currency, regulation, tariffs]?"

**For EACH question, prepare:**
- The direct answer (2-3 sentences)
- The supporting data point
- The bridge back to a key message
- The "do not say" list (phrases that could create problems)

### Phase 4: Guidance Framework

**Setting guidance:**
- Set guidance you have >75% confidence of beating
- The range (low to high) should be achievable 60-90% of the time
- Run `python3 tools/monte_carlo.py` to generate probability-weighted ranges
- Guidance = P75 outcome (low end) to P40 outcome (high end)
- Never set guidance assuming everything goes right

**Beat and raise cadence:**
- Ideal pattern: beat current quarter by 1-3% and raise full year by ~half the beat
- Consistent small beats build credibility; large beats suggest sandbagging
- If you beat by >5%, expect questions about whether you are deliberately low-balling

**Handling a guidance miss:**
- If you will miss guidance, pre-announce (do not surprise on earnings day)
- Frame the miss: temporary (deal timing) vs. structural (market shift)
- Provide a credible path back to prior trajectory or reset expectations cleanly
- Run `python3 tools/monte_carlo.py` with updated assumptions to show the new range

**Peer comparison framing:**
- Run `python3 tools/portfolio_risk.py` to benchmark your metrics against peer group
- Know your percentile rank on: growth, margin, Rule of 40, NDR, FCF margin
- Be ready to explain why you are above or below peers on each dimension
- Never say "we don't compare ourselves to competitors" — analysts will compare you anyway

---

## Mode 5: Management Commentary

### Explaining Variances

**Variance commentary framework (for every material line item):**

1. **State the variance:** "Revenue was $12.3M, $0.8M (7%) above budget and $2.1M (21%) above prior year"
2. **Decompose the drivers:** "The beat was driven by: (a) $0.5M from stronger-than-expected enterprise expansion, (b) $0.4M from early close of two Q2 pipeline deals, partially offset by (c) $0.1M shortfall in SMB new logos"
3. **Assess sustainability:** "The enterprise expansion strength reflects our new customer success program and is expected to continue. The deal pull-forward is a timing benefit that will reduce Q2 pipeline by approximately $0.4M"
4. **Adjust forward view:** "We are raising our full-year revenue forecast by $0.5M to reflect the sustainable component of the Q1 beat"

**Materiality threshold for commentary:**
- Revenue: explain any line >5% variance from budget
- Expenses: explain any line >10% variance from budget or >$100K absolute
- Cash flow: explain any item >$250K variance from forecast
- KPIs: explain any metric with >5% miss from target or meaningful trend change

### Forward-Looking Statement Structure

**When making forward-looking statements:**
1. Lead with the factual basis: "Based on our current pipeline of $45M and historical conversion rates of 25-30%..."
2. State the projection: "...we expect Q2 revenue of $11.5M to $12.0M"
3. Identify key assumptions: "This assumes no material change in sales cycle length and stable close rates"
4. Flag risks to the projection: "Key risks include: (1) enterprise budget cycle delays, (2) competitive pricing pressure in mid-market"
5. Note the confidence interval: "We have 80% confidence in the low end of this range and 50% confidence in the high end"

### Risk Factor Updates

**When risk factors change materially:**
1. Identify the change: "Customer concentration risk has increased — our top customer now represents 18% of ARR, up from 12% last quarter due to a large expansion deal"
2. Assess impact: "This creates revenue concentration risk but also validates our enterprise expansion motion"
3. Present mitigation: "We are actively diversifying by (a) accelerating mid-market sales hiring, (b) pursuing enterprise deals across 3 additional verticals"
4. Set a remediation timeline: "We expect top-customer concentration to return below 15% by Q4 as new enterprise logos close"

---

## Tool Integration

| When the report needs... | Run this | Example |
|------------------------|---------|---------|
| Guidance probability ranges | `python3 tools/monte_carlo.py --initial 12000000 --return 0.08 --vol 0.15 --years 1 --sims 10000` | Percentile ranges for revenue guidance |
| Scenario analysis for cash runway | `python3 tools/monte_carlo.py --initial 25000000 --return -0.20 --vol 0.30 --years 3 --sims 10000` | Probability of running out of cash |
| Peer performance benchmarking | `python3 tools/portfolio_risk.py` | Risk-adjusted returns vs. peer set |
| Forward valuation sanity check | `python3 tools/dcf.py --fcf 5,8,12,16,20 --wacc 0.12 --terminal-growth 0.03 --shares 100` | Implied valuation from projections |
| Weighted cost of capital for hurdle rate | `python3 tools/wacc.py --equity 500 --debt 200 --tax 0.25 --rf 0.04 --beta 1.3 --erp 0.055 --cost-of-debt 0.06` | Discount rate for investment decisions |

---

## Output Specifications

### Board Package: Slide-by-Slide Outline

For each slide, output:

```
### Slide [N]: [Title]

**Key Message:** [One sentence — the takeaway for the board]

**Content:**
- [Bullet 1 with specific data or claim]
- [Bullet 2]
- [Bullet 3]

**Visual:** [Chart type, table format, or diagram description]

**Data Needed:** [What the user must provide]

**Commentary Notes:** [Key talking points for the presenter]
```

### Investor Update Letter

Output as a structured document:
```
**Subject Line:** [Company Name] Q[X] [Year] Update — [Headline]

**Section 1: Headlines**
[Opening paragraph + 3 bullets]

**Section 2: Key Metrics**
[Metric table]

**Section 3: Business Update**
[2-4 paragraphs organized by function]

**Section 4: Financial Summary**
[1-2 paragraphs]

**Section 5: Outlook**
[1 paragraph with specific targets]

**Section 6: Asks**
[Specific help needed]
```

### Earnings Prep Package

Output includes:
- Key message document (3-5 messages with supporting data)
- Prepared remarks script outline (CEO + CFO sections)
- Q&A document (20-30 questions with prepared answers)
- Guidance walkdown (from internal forecast to published guidance)

---

## Quality Gates & Completion Criteria

- [ ] Every slide/section has a clear "so what" message (not just data)
- [ ] Bad news is presented early and directly with remediation plans
- [ ] All financials show at least 3 comparatives (actual vs. budget vs. prior year)
- [ ] KPIs show trends (minimum 4 periods) not just point-in-time snapshots
- [ ] Forward-looking statements include assumptions and risk factors
- [ ] Variance commentary decomposes drivers and assesses sustainability
- [ ] All data gaps are explicitly flagged rather than papered over
- [ ] Numbers are internally consistent across all slides/sections
- [ ] Board action items are specific and decision-ready
- [ ] Earnings Q&A covers bear case questions with prepared responses

**Success metric:** A board member reading the package alone (without the live presentation) should understand exactly what happened, why, and what needs to happen next.

**Escalation triggers:**
- User wants to omit or bury material bad news → stop and insist on disclosure with appropriate framing
- Financial data is internally inconsistent → flag and reconcile before proceeding
- Guidance range is unrealistically narrow → run Monte Carlo to demonstrate realistic dispersion
- No comparatives available (budget or prior year) → build the package but flag that comparatives are essential for future quarters

---

## Hard Constraints

- **NEVER** help obscure, omit, or minimize bad news — always present it with context and a remediation plan
- **NEVER** fabricate financial data, KPIs, or benchmark figures
- **NEVER** show single-period snapshots without trend context (minimum 4 periods)
- **NEVER** present guidance without underlying assumptions and scenario analysis
- **ALWAYS** show actuals against at least two comparatives (budget and prior year)
- **ALWAYS** decompose variances into component drivers — "we missed" is not analysis
- **ALWAYS** include a forward-looking view — boards need to know where you are going, not just where you have been
- **ALWAYS** separate leading indicators from lagging indicators in dashboards
- If the user provides financials that do not reconcile, **require** reconciliation before building the package

---

## Common Pitfalls

1. **Hiding the miss:** Putting bad news on Slide 22 of a 25-slide deck. Board members are not fooled — they read the whole package. Put challenges on Slide 2, right after the executive summary. Candor builds trust; evasion destroys it.

2. **Snapshots without trends:** Showing "NDR is 115%" without context. Is that up from 105% or down from 125%? Always show the trend. A good metric trending down is more concerning than a mediocre metric trending up.

3. **Too many metrics:** A dashboard with 50 KPIs communicates nothing. Choose 8-12 that matter, with clear RAG status. Every metric on the dashboard should have an owner and an action plan if it turns red.

4. **Variance commentary that describes but does not explain:** "Revenue was $0.5M below budget" is description. "Revenue was $0.5M below budget due to 3 enterprise deal slips totaling $0.7M, partially offset by $0.2M SMB overperformance" is explanation. Always explain.

5. **No forward-looking view:** Boards need to approve strategy and allocate resources. If the package only looks backward, it is an audit report, not a board deck. Every section should connect historical performance to the forward plan.

6. **Sandbagging guidance then celebrating beats:** Consistently setting guidance at the P90 outcome and then "beating" by 10% erodes credibility with analysts. Aim for consistent 1-3% beats that demonstrate predictability.

7. **Ignoring peer context:** "Our growth rate is 25%" means nothing without context. If peers are growing at 40%, you are underperforming. If peers are growing at 15%, you are outperforming. Always know your peer benchmarks.

8. **Action items without owners or deadlines:** "Explore international expansion" is not an action item. "VP Sales to present EMEA market entry plan at Q2 board meeting" is an action item. Every ask should have an owner, a deliverable, and a deadline.

---

## Related Skills

- For fundraising presentations to new investors → `/pitch-deck`
- For detailed unit economics and SaaS metrics analysis → `/fpa`
- For full investment committee memos → `/investment-memo`
- For valuation support behind projections → `/lbo` or run DCF tools directly
- For cash flow forecasting and runway analysis → `/forecast`
- For budget construction → `/budget`
