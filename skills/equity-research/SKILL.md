---
name: equity-research
description: |
  Equity research — initiating coverage, earnings models, trading comps, and price targets.
  Activate when the user mentions equity research, initiating coverage, price target,
  comparable company analysis, trading comps, comp table, EV/EBITDA, P/E ratio, PEG ratio,
  sum-of-the-parts, SOTP, segment valuation, equity valuation, coverage initiation,
  sector analysis, industry overview, stock rating, buy/sell/hold rating, target price,
  comp sheet, relative valuation, or asks about analyzing a public stock for a research
  report or building an earnings model.
---

# Equity Research

I produce equity research with the rigor of a senior analyst publishing under their name. Every report starts with a thesis — a clear view on why the stock is mispriced — supported by a proprietary earnings model, multiple valuation methodologies, and a defined catalyst path. The output must be specific enough to act on: a rating, a price target, and the conditions that would change both.

---

## Scope & Boundaries

**What this skill DOES:**
- Initiate coverage with thesis, earnings model, valuation, and price target
- Build comparable company analysis (trading comps) with relevant peer groups
- Construct DCF and sum-of-the-parts (SOTP) valuations
- Derive price targets from multiple methodologies with probability weighting
- Analyze industry structure, competitive positioning, and secular trends
- Build quarterly and annual earnings models with driver-based projections
- Produce bull/base/bear scenario analysis with distinct price targets
- Identify catalysts and define the timeline for thesis realization

**Use a different skill when:**
- Hedge fund L/S with Kelly sizing and portfolio construction → `/long-short`
- Writing an investment committee memo → `/investment-memo`
- Post-earnings reaction and estimate revisions → `/earnings`
- Credit analysis on the same company → `/credit`
- Analyzing a private company → `/pe-growth` or `/pe-buyout`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| DCF | `python3 tools/dcf.py` | Intrinsic value from projected free cash flows |
| WACC | `python3 tools/wacc.py` | Discount rate for DCF |
| IRR / NPV | `python3 tools/irr.py` | Expected return at current price |
| Portfolio Risk | `python3 tools/portfolio_risk.py` | Beta, volatility metrics |
| Kelly | `python3 tools/kelly.py` | Position sizing (for buy-side) |

---

## Pre-Flight Checks

1. **Company:** Name, ticker, sector, market cap
2. **Financials:** Revenue, EBITDA, EPS (LTM and NTM), margins, growth rate
3. **Valuation:** Current price, trading multiples (EV/EBITDA, P/E, EV/Revenue)
4. **Peer group:** 4-8 comparable public companies
5. **Thesis direction:** Bullish, bearish, or neutral — what's the variant view?
6. **Catalyst:** What event will prove the thesis within 12-18 months?

---

## Phase 1: Industry & Competitive Analysis

**Goal:** Understand the playing field before analyzing the player.

### Industry Structure (Porter's Five Forces Lens)
```
| Force | Assessment | Impact on Company |
|-------|-----------|------------------|
| Rivalry intensity | [Low/Med/High] | [pricing power, margin pressure] |
| Threat of new entrants | [Low/Med/High] | [moat durability] |
| Buyer power | [Low/Med/High] | [pricing, switching costs] |
| Supplier power | [Low/Med/High] | [margin risk, input costs] |
| Substitution threat | [Low/Med/High] | [demand risk, disruption] |
```

### Competitive Positioning
```
| Dimension | Company | Competitor A | Competitor B | Competitor C |
|-----------|---------|-------------|-------------|-------------|
| Market share | [X]% | [X]% | [X]% | [X]% |
| Revenue growth | [X]% | [X]% | [X]% | [X]% |
| Gross margin | [X]% | [X]% | [X]% | [X]% |
| R&D intensity | [X]% | [X]% | [X]% | [X]% |
| Customer NPS/retention | [X] | [X] | [X] | [X] |
| Key advantage | [describe] | [describe] | [describe] | [describe] |
```

### Secular Trends
```
Tailwinds:
  1. [Trend] — [X]% CAGR through [year], benefiting [segment]
  2. [Trend] — regulatory/behavioral shift driving adoption

Headwinds:
  1. [Trend] — [threat to growth/margins]
  2. [Trend] — competitive/technology disruption risk
```

---

## Phase 2: Earnings Model

**Goal:** Build a driver-based financial model that produces quarterly and annual projections.

### Revenue Build (Top-Down + Bottom-Up Reconciliation)
```
Segment revenue build:
| Segment | FY-1 | FY0 | FY+1E | FY+2E | FY+3E | Driver |
|---------|------|-----|-------|-------|-------|--------|
| [Seg A] | $[X]M | $[X]M | $[X]M | $[X]M | $[X]M | [units × price / customers × ARPU] |
| [Seg B] | $[X]M | $[X]M | $[X]M | $[X]M | $[X]M | [driver] |
| [Seg C] | $[X]M | $[X]M | $[X]M | $[X]M | $[X]M | [driver] |
| **Total** | **$[X]M** | **$[X]M** | **$[X]M** | **$[X]M** | **$[X]M** | |
| YoY growth | | [X]% | [X]% | [X]% | [X]% | |

Key assumptions:
  Volume growth: [X]% (driven by [market expansion / share gains / new product])
  Pricing: [X]% (driven by [inflation / mix shift / new features])
  FX impact: [X]% (if multinational)
```

### Margin Trajectory
```
| Metric | FY-1 | FY0 | FY+1E | FY+2E | FY+3E |
|--------|------|-----|-------|-------|-------|
| Gross margin | [X]% | [X]% | [X]% | [X]% | [X]% |
| S&M % of rev | [X]% | [X]% | [X]% | [X]% | [X]% |
| R&D % of rev | [X]% | [X]% | [X]% | [X]% | [X]% |
| G&A % of rev | [X]% | [X]% | [X]% | [X]% | [X]% |
| EBITDA margin | [X]% | [X]% | [X]% | [X]% | [X]% |
| Operating margin | [X]% | [X]% | [X]% | [X]% | [X]% |
| Net margin | [X]% | [X]% | [X]% | [X]% | [X]% |

Margin bridge (FY0 → FY+2E):
  Gross margin improvement:  +[X]bps (mix shift / scale / procurement)
  OpEx leverage:             +[X]bps (revenue growing faster than headcount)
  Headwinds:                 -[X]bps (investment in [X])
  Net margin expansion:      +[X]bps
```

### EPS Build
```
| Metric | FY-1 | FY0 | FY+1E | FY+2E | FY+3E |
|--------|------|-----|-------|-------|-------|
| Revenue | $[X]M | | | | |
| EBITDA | $[X]M | | | | |
| D&A | ($[X]M) | | | | |
| EBIT | $[X]M | | | | |
| Interest | ($[X]M) | | | | |
| Pre-tax income | $[X]M | | | | |
| Tax rate | [X]% | | | | |
| Net income | $[X]M | | | | |
| Diluted shares | [X]M | | | | |
| **EPS** | **$[X]** | | | | |
| EPS growth | | [X]% | [X]% | [X]% | [X]% |

| Free cash flow | | | | | |
| Capex | ($[X]M) | | | | |
| FCF | $[X]M | | | | |
| FCF per share | $[X] | | | | |
| FCF yield | [X]% | | | | |
```

---

## Phase 3: Comparable Company Analysis

**Goal:** Value the stock relative to peers on multiple metrics.

### Trading Comps Table
```
| Company | Ticker | Mkt Cap | EV | EV/Rev NTM | EV/EBITDA NTM | P/E NTM | PEG | Rev Gr | EBITDA Mgn |
|---------|--------|---------|-----|-----------|-------------|---------|-----|--------|-----------|
| [Peer 1] | [X] | $[X]B | $[X]B | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| [Peer 2] | [X] | $[X]B | $[X]B | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| [Peer 3] | [X] | $[X]B | $[X]B | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| [Peer 4] | [X] | $[X]B | $[X]B | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| [Peer 5] | [X] | $[X]B | $[X]B | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
|----------|-------|---------|------|-----------|-------------|---------|-----|--------|-----------|
| **Mean** | | | | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| **Median** | | | | [X]x | [X]x | [X]x | [X]x | [X]% | [X]% |
| **Subject** | [X] | $[X]B | $[X]B | **[X]x** | **[X]x** | **[X]x** | **[X]x** | [X]% | [X]% |
| Premium/(discount) | | | | [X]% | [X]% | [X]% | | | |
```

### Comp Selection Criteria
```
Include peers that share:
  - Same industry / end market exposure
  - Similar revenue scale (within 0.3-3x)
  - Similar growth profile (within 10pp)
  - Similar margin structure
  - Same geographic mix (domestic vs international)

Exclude:
  - Companies undergoing M&A (distorted multiples)
  - Companies with one-time events (restructuring, litigation)
  - Companies with fundamentally different business models
```

### Implied Valuation from Comps
```
| Methodology | Multiple | Subject Metric | Implied EV | Implied Price |
|------------|---------|---------------|-----------|--------------|
| EV/Revenue (median) | [X]x | $[X]M rev | $[X]M | $[X] |
| EV/EBITDA (median) | [X]x | $[X]M EBITDA | $[X]M | $[X] |
| P/E (median) | [X]x | $[X] EPS | — | $[X] |
| PEG-adjusted | [X]x | [X]% growth | — | $[X] |
```

---

## Phase 4: DCF Valuation

**Goal:** Establish intrinsic value independent of market sentiment.

Run: `python3 tools/dcf.py --fcf [projected_fcfs] --wacc [X] --terminal-growth [X] --net-debt [X] --shares [X]`
Run: `python3 tools/wacc.py --equity [X] --debt [X] --tax [X] --rf [X] --beta [X] --erp [X] --cost-of-debt [X]`

```
WACC components:
  Risk-free rate:        [X]% (10Y Treasury)
  Beta:                  [X] (2Y weekly vs S&P 500)
  Equity risk premium:   [X]%
  Cost of equity:        [X]%
  Cost of debt (after-tax): [X]%
  Capital weights:       [X]% equity / [X]% debt
  WACC:                  [X]%

DCF output:
  PV of FCFs (explicit): $[X]M
  Terminal value:        $[X]M (at [X]% terminal growth)
  Enterprise value:      $[X]M
  Less net debt:         ($[X]M)
  Equity value:          $[X]M
  Per share:             $[X]

Terminal value as % of EV: [X]%  (flag if >75%)
```

### Sum-of-the-Parts (for multi-segment companies)
```
| Segment | Metric | Multiple | Value | Methodology |
|---------|--------|---------|-------|-------------|
| [Seg A] | $[X]M EBITDA | [X]x | $[X]M | Pure-play comp [X] trades at [X]x |
| [Seg B] | $[X]M Revenue | [X]x | $[X]M | High-growth segment, comp to [X] |
| [Seg C] | $[X]M EBITDA | [X]x | $[X]M | Mature, valued at sector median |
| Corporate costs | ($[X]M) | [X]x | ($[X]M) | Capitalized overhead drag |
| Net debt | | | ($[X]M) | |
| **Equity value** | | | **$[X]M** | |
| **Per share** | | | **$[X]** | |

Conglomerate discount: [X]% (typical: 10-25% for complex companies)
```

---

## Phase 5: Price Target & Rating

**Goal:** Derive a defensible price target and clear rating.

### Valuation Reconciliation
```
| Method | Weight | Value/Share | Contribution |
|--------|--------|-----------|-------------|
| DCF | [X]% | $[X] | $[X] |
| EV/EBITDA comps | [X]% | $[X] | $[X] |
| P/E comps | [X]% | $[X] | $[X] |
| SOTP | [X]% | $[X] | $[X] |
| **Blended target** | **100%** | | **$[X]** |
```

### Scenario Analysis
```
| Scenario | Probability | EPS | Multiple | Price | Return |
|----------|------------|-----|---------|-------|--------|
| Bull | [X]% | $[X] | [X]x | $[X] | +[X]% |
| Base | [X]% | $[X] | [X]x | $[X] | +[X]% |
| Bear | [X]% | $[X] | [X]x | $[X] | -[X]% |
| **Probability-weighted** | 100% | | | **$[X]** | **+[X]%** |

Risk/reward: [X]:1 (upside to bull / downside to bear)
```

### Rating Framework
```
| Rating | Criteria |
|--------|---------|
| Buy / Overweight | >15% upside to 12-month target, favorable risk/reward |
| Hold / Equal Weight | ±15% of target, balanced risk/reward |
| Sell / Underweight | >15% downside, unfavorable risk/reward |
```

**Price target: $[X]** — [X]% upside from current $[X]
**Rating: [Buy/Hold/Sell]**

---

## Phase 6: Catalyst Path & Monitoring

**Goal:** Define what events will prove or disprove the thesis.

```
| # | Catalyst | Timeline | Probability | Impact on Price |
|---|---------|----------|------------|----------------|
| 1 | [Earnings beat / guidance raise] | [date] | [X]% | +/-[X]% |
| 2 | [Product launch / FDA approval] | [date] | [X]% | +/-[X]% |
| 3 | [Market share data point] | [date] | [X]% | +/-[X]% |
| 4 | [M&A / capital allocation] | [date] | [X]% | +/-[X]% |
| 5 | [Macro/regulatory event] | [date] | [X]% | +/-[X]% |

Thesis-killing signals:
  - [Metric] deteriorates below [threshold]
  - [Competitive event] occurs
  - [Management action] that changes the capital allocation thesis
```

---

## Quality Gates

- [ ] Industry structure analyzed (competitive dynamics, secular trends)
- [ ] Earnings model built with driver-based revenue and bottom-up margins
- [ ] Trading comps table with 4+ relevant peers
- [ ] DCF with explicit WACC build-up and sensitivity table
- [ ] SOTP if the company has distinct business segments
- [ ] Price target derived from multiple methodologies with weights
- [ ] Bull/base/bear scenarios with probability-weighted return
- [ ] Catalyst calendar with specific events and timeline

## Hard Constraints

- **NEVER** set a price target from a single valuation method
- **NEVER** use a comp table without explaining why each peer was included
- **ALWAYS** show the earnings model assumptions — the target means nothing without the forecast
- **ALWAYS** include bear case — a research report without downside analysis is advocacy, not analysis

## Common Pitfalls

1. **Terminal value dominance** — if TV is >80% of DCF value, the explicit period assumptions barely matter
2. **Peer group cherry-picking** — including only comps that support your thesis
3. **Linear extrapolation** — projecting current growth rate 5 years forward without modeling deceleration
4. **Ignoring capital allocation** — buybacks, M&A, and dividends change the per-share math significantly
5. **Stale comps** — using yesterday's multiples without adjusting for sector re-rating

## Related Skills

- `/earnings` — post-earnings analysis and estimate revisions
- `/long-short` — hedge fund thesis with position sizing
- `/investment-memo` — formal IC memo write-up
- `/financial-statements` — deep dive into the underlying financials
- `/credit` — credit perspective on the same company
