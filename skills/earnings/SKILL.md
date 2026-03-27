---
name: earnings
description: |
  Earnings analysis — preview, post-earnings reaction, estimate revision, and consensus tracking.
  Activate when the user mentions earnings, earnings preview, earnings reaction, beat/miss,
  estimate revision, consensus estimate, whisper number, guidance, earnings surprise,
  earnings call, quarterly results, revenue beat, EPS miss, guidance raise, guidance cut,
  estimate changes, analyst estimates, or asks about analyzing upcoming or recent earnings
  for a public company.
---

# Earnings Analysis

I analyze earnings events — the single most important recurring catalyst for public equities. Every quarter, the market re-prices expectations. I build previews that identify where consensus is vulnerable, analyze results against expectations, track estimate revisions that signal momentum, and assess guidance changes that reshape the forward narrative. Earnings are where the model meets reality.

---

## Scope & Boundaries

**What this skill DOES:**
- Build earnings previews (consensus expectations, key metrics to watch, whisper estimates)
- Analyze reported results vs consensus (beat/miss on revenue, EPS, and key KPIs)
- Evaluate management guidance (raise/maintain/lower, magnitude, credibility)
- Track estimate revisions and their direction/magnitude over time
- Analyze earnings quality (recurring vs one-time, cash vs accrual)
- Assess earnings call commentary for forward-looking signals
- Compare results to the earnings model and identify needed revisions
- Build historical beat/miss patterns for context

**Use a different skill when:**
- Full initiating coverage research report → `/equity-research`
- Formal investment thesis and price target → `/equity-research`
- Hedge fund position sizing → `/long-short`
- Credit implications of earnings → `/credit`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| DCF | `python3 tools/dcf.py` | Re-run valuation with updated estimates |
| IRR / NPV | `python3 tools/irr.py` | Expected return post earnings at new price |

---

## Pre-Flight Checks

1. **Company:** Ticker, sector, market cap, reporting date
2. **Consensus estimates:** Revenue, EPS (GAAP and adjusted), key segment metrics
3. **Prior quarter context:** What happened last quarter? Any ongoing themes?
4. **Guidance:** What did management guide for this quarter and full year?
5. **Key metrics:** What 2-3 non-financial KPIs does the market care about most?
6. **Positioning:** Is the stock trading into the print with fear or optimism?

---

## Phase 1: Earnings Preview

**Goal:** Identify where consensus is vulnerable and what metrics will drive the stock reaction.

### Consensus Expectations
```
| Metric | Consensus | Range (Low-High) | Whisper | Prior Q | YoY |
|--------|-----------|------------------|---------|---------|-----|
| Revenue | $[X]M | $[X]-[X]M | $[X]M | $[X]M | [X]% |
| Gross margin | [X]% | [X]-[X]% | | [X]% | |
| Operating income | $[X]M | | | $[X]M | |
| EPS (adjusted) | $[X] | $[X]-[X] | $[X] | $[X] | [X]% |
| [Key KPI 1] | [X] | | | [X] | |
| [Key KPI 2] | [X] | | | [X] | |
| FY guidance (rev) | $[X]M | | | $[X]M (prior) | |
| FY guidance (EPS) | $[X] | | | $[X] (prior) | |
```

### What Matters Most This Quarter
```
Priority metrics (ranked by likely stock impact):
1. [Metric]: The market is focused on [X] because [reason].
   Consensus: [X]. Our view: [above/below/in-line]. Risk: [X].

2. [Metric]: [Why it matters this quarter].
   Consensus: [X]. Our view: [X]. Risk: [X].

3. [Guidance]: [Full-year revision is the real event because...].
   Current guide: $[X-Y]. Street expects: [raise/maintain].
```

### Earnings Sensitivity
```
Revenue scenarios and EPS impact:
| Revenue | vs Consensus | Implied EPS | Stock Reaction |
|---------|-------------|------------|---------------|
| $[X]M (bear) | -[X]% miss | $[X] | -[X]% to -[X]% |
| $[X]M (base) | in-line | $[X] | -[X]% to +[X]% |
| $[X]M (bull) | +[X]% beat | $[X] | +[X]% to +[X]% |

Guidance scenarios:
| FY Guide | vs Prior | Street Impact | Stock Reaction |
|----------|---------|-------------|---------------|
| Raise to $[X] | +[X]% | NTM EPS to $[X] | +[X]% |
| Maintain $[X] | flat | No change | Neutral |
| Lower to $[X] | -[X]% | NTM EPS to $[X] | -[X]% |
```

### Historical Beat/Miss Pattern
```
| Quarter | Rev Surprise | EPS Surprise | Guidance | Stock 1-Day |
|---------|-------------|-------------|----------|-------------|
| Q-4 | +[X]% | +[X]% | Raised | +[X]% |
| Q-3 | +[X]% | +[X]% | Maintained | -[X]% |
| Q-2 | -[X]% | +[X]% | Lowered | -[X]% |
| Q-1 | +[X]% | +[X]% | Raised | +[X]% |
| Average | +[X]% | +[X]% | | +/-[X]% |

Implied move from options: ±[X]% (straddle-implied)
Historical avg move: ±[X]%
```

---

## Phase 2: Post-Earnings Analysis

**Goal:** Rapidly assess results and determine whether to act.

### Beat/Miss Scorecard
```
| Metric | Consensus | Actual | Surprise | Quality |
|--------|-----------|--------|---------|---------|
| Revenue | $[X]M | $[X]M | +/-[X]% | [Clean/One-time] |
| Gross margin | [X]% | [X]% | +/-[X]bps | |
| EBITDA | $[X]M | $[X]M | +/-[X]% | |
| EPS (adj) | $[X] | $[X] | +/-[X]% | [Buyback-assisted?] |
| [KPI 1] | [X] | [X] | +/-[X]% | |
| [KPI 2] | [X] | [X] | +/-[X]% | |
| FY Rev guide | $[X]M | $[X]M | [Raise/Maintain/Lower] |
| FY EPS guide | $[X] | $[X] | [Raise/Maintain/Lower] |

Headline: [Beat/Miss] on [revenue/EPS/both] with [guidance raise/cut/maintain]
```

### Earnings Quality Assessment
```
Red flags to check:
[ ] Did the beat come from revenue or cost cuts? (Revenue beats are higher quality)
[ ] Did EPS beat come from lower tax rate or share count, not operations?
[ ] Did revenue beat but deferred revenue decline? (Pulling forward future revenue)
[ ] Did cash flow from operations diverge from net income? (Accrual earnings)
[ ] Did the company change segment definitions or KPI calculations?
[ ] Are there large one-time items in "adjusted" earnings?
[ ] Did accounts receivable grow much faster than revenue? (Channel stuffing risk)
```

### Guidance Analysis
```
Guidance change:
  Prior guide:      $[X-Y]M revenue / $[X-Y] EPS
  New guide:        $[X-Y]M revenue / $[X-Y] EPS
  Change:           +/-$[X]M revenue / +/-$[X] EPS
  Implied Q+ run-rate: $[X]M/quarter (is this achievable?)

Guidance credibility:
  Historical guide accuracy: Management typically [beats/meets/misses] by [X]%
  Conservatism level: [Conservative/In-line/Aggressive] based on track record
  Consensus reaction needed: Street estimates need to [rise/fall] by $[X] to match
```

---

## Phase 3: Estimate Revision Tracking

**Goal:** Track the direction and magnitude of consensus estimate changes — the best predictor of future stock performance.

### Revision Dashboard
```
| Period | 30 Days Ago | Current | Change | Direction |
|--------|-----------|---------|--------|----------|
| Q+1 EPS | $[X] | $[X] | +/-[X]% | [Up/Down/Flat] |
| FY EPS | $[X] | $[X] | +/-[X]% | [Up/Down/Flat] |
| FY+1 EPS | $[X] | $[X] | +/-[X]% | [Up/Down/Flat] |
| FY Revenue | $[X]M | $[X]M | +/-[X]% | [Up/Down/Flat] |

Revision breadth:
  Analysts raising: [X] of [X] total
  Analysts cutting: [X] of [X] total
  Net revision ratio: [X]% (positive = net upgrades)
```

### Revision Momentum Signal
```
Earnings revision momentum:
  3-month EPS revision: +/-[X]%
  1-month EPS revision: +/-[X]%
  Acceleration: [Accelerating / Decelerating / Stable]

Research shows:
  - Stocks with positive 3-month EPS revisions outperform over next 3-6 months
  - Magnitude matters: >5% revision = strong signal
  - Breadth matters: 70%+ of analysts moving same direction = high conviction signal
```

---

## Phase 4: Earnings Call Analysis

**Goal:** Extract forward-looking signals from management commentary.

### Key Quotes & Signals
```
| Topic | Quote/Comment | Signal | Implication |
|-------|-------------|--------|-----------|
| Demand | "[exact quote]" | [Positive/Negative/Neutral] | [impact on model] |
| Margins | "[exact quote]" | [Positive/Negative/Neutral] | [impact on model] |
| Competition | "[exact quote]" | [Positive/Negative/Neutral] | [impact on model] |
| Capital allocation | "[exact quote]" | [Positive/Negative/Neutral] | [impact on model] |
| Guidance language | "[exact quote]" | [More/less conservative than prior] | |
```

### Tone Shift Detection
```
Compare language to prior quarter:
  - Did management use more hedging language? ("cautiously optimistic" vs "very confident")
  - Did they address new risks not previously mentioned?
  - Did they change KPI definitions or stop reporting a metric? (Red flag)
  - Did they pre-announce or provide unusual intra-quarter updates?
  - Was Q&A defensive or expansive on forward outlook?
```

---

## Phase 5: Model Update & Price Target Revision

**Goal:** Translate the earnings result into updated estimates and a revised view.

```
Model revision:
| Metric | Prior Estimate | Updated | Change | Reason |
|--------|---------------|---------|--------|--------|
| FY Revenue | $[X]M | $[X]M | +/-[X]% | [guidance raise + beat run-rate] |
| FY EBITDA | $[X]M | $[X]M | +/-[X]% | [margin outperformance] |
| FY EPS | $[X] | $[X] | +/-[X]% | [flow-through] |
| FY+1 Revenue | $[X]M | $[X]M | +/-[X]% | [new baseline + growth] |
| FY+1 EPS | $[X] | $[X] | +/-[X]% | |

Price target revision:
  Prior target: $[X]
  New target: $[X]
  Change: +/-[X]%
  Methodology: [X]x NTM EPS of $[X] (was [X]x × $[X])
  Rating change: [Maintain/Upgrade/Downgrade]
```

---

## Quality Gates

- [ ] Consensus expectations documented with source
- [ ] Key metrics identified and ranked by stock impact
- [ ] Results analyzed vs consensus with quality assessment
- [ ] Guidance change evaluated against historical accuracy
- [ ] Estimate revisions tracked (direction, magnitude, breadth)
- [ ] Earnings call commentary analyzed for forward signals
- [ ] Model updated and price target revised (or maintained with rationale)

## Hard Constraints

- **NEVER** analyze a beat/miss without checking earnings quality (was it real?)
- **NEVER** ignore guidance when it changes — it reshapes the entire forward curve
- **ALWAYS** compare actual to consensus AND to your own model — both comparisons matter
- **ALWAYS** check the cash flow statement — accrual tricks hide in the income statement

## Common Pitfalls

1. **Headline beat, quality miss** — EPS beat from tax rate and buyback, not operations
2. **Ignoring guidance for the beat** — a 5% EPS beat with a 3% guidance cut is net negative
3. **Anchoring to the stock reaction** — the 1-day move is noise; estimate revisions are signal
4. **Missing the KPI** — for many stocks, the non-financial metric (users, NRR, bookings) matters more than EPS
5. **Stale model** — not updating estimates after the print means your target is based on old numbers

## Related Skills

- `/equity-research` — full initiating coverage and earnings model
- `/long-short` — trade the earnings event with proper sizing
- `/financial-statements` — deep dive into the reported numbers
- `/data-entry` — extract data from the earnings release and filing
