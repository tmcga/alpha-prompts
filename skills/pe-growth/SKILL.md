---
name: pe-growth
description: |
  Growth equity analysis — minority investments in scaling businesses.
  Activate when the user mentions growth equity, growth investment, minority stake,
  PIPE, pre-IPO, Series D+, late-stage private, revenue growth investment, unit economics,
  path to profitability, rule of 40, governance rights, board seat, protective provisions,
  or asks about investing in a high-growth company without taking control.
---

# Growth Equity Analysis

I analyze minority growth equity investments — the space between venture capital and buyout. Growth equity targets profitable or near-profitable businesses scaling rapidly, where the investment thesis is revenue trajectory and margin expansion, not leverage. The key question is always: is the growth rate durable enough to justify the entry valuation?

---

## Scope & Boundaries

**What this skill DOES:**
- Evaluate revenue quality: recurring vs. transactional, net retention, cohort behavior
- Assess unit economics: LTV/CAC, payback period, contribution margin by segment
- Model path to profitability with operating leverage analysis
- Analyze governance: minority protections, board representation, information rights
- Structure investments: preferred equity, convertible notes, PIPE structures
- Model dilution through future rounds and IPO
- Calculate growth-adjusted valuation (PEG, EV/Revenue, Rule of 40 benchmarking)
- Build investor returns under multiple exit scenarios (IPO, M&A, secondary)

**Use a different skill when:**
- Taking control / leveraged buyout → `/pe-buyout`
- Seed through Series B venture → `/vc`
- Lending to the business → `/private-credit`
- Public equity analysis → `/long-short`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| DCF | `python3 tools/dcf.py` | DCF valuation for profitable growth companies |
| IRR / NPV | `python3 tools/irr.py` | Equity return calculation |
| VC Returns | `python3 tools/vc_returns.py` | Fund metrics, dilution waterfall |
| Kelly | `python3 tools/kelly.py` | Position sizing within portfolio |

---

## Pre-Flight Checks

1. **Company profile:** Revenue, growth rate, gross margin, EBITDA margin, cash burn
2. **Stage:** Revenue range, profitability status, funding history
3. **Proposed terms:** Valuation, investment size, instrument (preferred, common, convertible)
4. **Governance:** Board seat, protective provisions, information rights, drag/tag
5. **Use of proceeds:** Growth capex, hiring, M&A, balance sheet
6. **Exit timeline:** Expected hold period, target liquidity event

---

## Phase 1: Revenue Quality Assessment

**Goal:** Determine whether the growth rate is durable or decelerating.

```
Revenue quality scorecard:
| Metric | Score (1-5) | Notes |
|--------|-------------|-------|
| Recurring revenue % | | >80% = 5, <50% = 1 |
| Net revenue retention | | >130% = 5, <100% = 1 |
| Logo churn | | <5% = 5, >15% = 1 |
| Customer concentration | | Top 10 <20% = 5, >50% = 1 |
| Revenue growth (YoY) | | >50% = 5, <15% = 1 |
| Growth rate deceleration | | Stable = 5, rapid decline = 1 |
| Contract duration | | >2yr avg = 5, month-to-month = 1 |
```

**Cohort analysis:** Track revenue retained by vintage. If recent cohorts retain worse than early cohorts, growth is masking churn.

**Decision Gate:** If net retention <100% and growth is decelerating, the business may not be investable at growth equity valuations.

---

## Phase 2: Unit Economics & Path to Profitability

**Goal:** Determine whether growth spending is efficient and when profitability arrives.

```
Unit Economics:
  Average Contract Value (ACV):    $[X]K
  Gross Margin:                    [X]%
  Customer Acquisition Cost (CAC): $[X]K
  LTV/CAC:                         [X]x (target: >3x)
  CAC Payback (months):            [X] (target: <18)
  Net Revenue Retention:           [X]%

Rule of 40: Revenue Growth % + EBITDA Margin % = [X]
  >40 = strong, 20-40 = acceptable, <20 = concerning

Burn Multiple: Net Burn / Net New ARR = [X]x
  <1x = excellent, 1-2x = good, >2x = inefficient
```

**Path to profitability:**
```
| Metric      | Current | Year 1 | Year 2 | Year 3 | Year 4 |
|-------------|---------|--------|--------|--------|--------|
| Revenue     | $[X]M   |        |        |        |        |
| Gross Margin| [X]%    |        |        |        |        |
| S&M %       | [X]%    |        | ← declining as efficiency scales |
| R&D %       | [X]%    |        |        |        |        |
| G&A %       | [X]%    |        |        |        |        |
| EBITDA %    | [X]%    |        |        |  breakeven? |        |
```

---

## Phase 3: Valuation & Entry Price

**Goal:** Determine a fair entry price using growth-adjusted metrics.

```
Valuation frameworks:
  EV / Revenue (NTM):             [X]x  (growth-adjusted: what multiple per turn of growth?)
  EV / Gross Profit:              [X]x  (normalizes for margin differences)
  PEG Ratio:                      [X]x  (P/E ÷ growth rate)
  Rule of 40 adjusted:            [X]x  (EV/Rev ÷ Rule of 40 score)

Comparable transactions:
| Company | Revenue | Growth | Margin | EV/Rev | Rule of 40 |
|---------|---------|--------|--------|--------|-----------|
| Comp 1  |         |        |        |        |           |
| Comp 2  |         |        |        |        |           |
| Comp 3  |         |        |        |        |           |
| Subject |         |        |        |        |           |
```

**Decision Gate:** If the entry multiple implies the company must maintain current growth rate for 5+ years to deliver target returns, the margin of safety is insufficient.

---

## Phase 4: Governance & Structuring

**Goal:** Secure minority protections that preserve optionality.

**Standard growth equity protections:**
1. **Board representation:** At minimum 1 board seat; observer seat if board seat not available
2. **Protective provisions:** Consent rights on M&A, new debt >$[X]M, new equity issuance, budget changes >20%
3. **Information rights:** Monthly financial reports, annual budget, quarterly board decks
4. **Anti-dilution:** Weighted average (not full ratchet) for down rounds
5. **Pro-rata rights:** Right to participate in future rounds to maintain ownership
6. **Drag-along / tag-along:** Tag-along with majority sale; drag only with [X]% supermajority
7. **Registration rights:** Demand and piggyback rights for IPO
8. **Liquidation preference:** 1x non-participating preferred (standard); avoid >1x or participating

---

## Phase 5: Returns Modeling

**Goal:** Calculate returns under multiple exit scenarios.

```
Investment: $[X]M for [X]% ownership on fully diluted basis
Entry valuation: $[X]M pre-money

Exit scenarios:
| Scenario | Year | EV | Ownership | Proceeds | MOIC | IRR |
|----------|------|-----|-----------|----------|------|-----|
| IPO | [X] | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| M&A | [X] | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| Secondary | [X] | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| Down case | [X] | $[X]M | [X]% | $[X]M | [X]x | [X]% |
```

Run: `python3 tools/irr.py --cfs="[-investment, 0, 0, 0, exit_proceeds]"`

**Dilution modeling:** Account for option pool expansion (typically 2-5% per year) and any future fundraising rounds that dilute the position.

---

## Quality Gates

- [ ] Revenue quality scored with cohort analysis
- [ ] Unit economics calculated (LTV/CAC, payback, Rule of 40)
- [ ] Path to profitability modeled with operating leverage
- [ ] Valuation benchmarked against growth-adjusted comps
- [ ] Governance protections reviewed
- [ ] Returns modeled across 3+ exit scenarios with dilution
- [ ] Stress test: growth deceleration + margin miss + delayed exit

## Hard Constraints

- **NEVER** value a growth equity investment solely on revenue multiple without adjusting for growth rate
- **NEVER** ignore dilution from future rounds and option pool expansion
- **ALWAYS** assess revenue quality (recurring, retention, concentration) before modeling returns
- **ALWAYS** model the path to profitability — growth without a margin trajectory is VC, not growth equity

## Common Pitfalls

1. **Paying for growth that's already decelerating** — check the second derivative
2. **Ignoring dilution** — a 20% position at entry can become 12% by exit
3. **Conflating revenue growth with value creation** — revenue at negative unit economics is value-destructive
4. **Insufficient governance** — minority without protective provisions is a hope trade
5. **Linear path to profitability** — the jump from -10% to +10% margin is harder than it looks

## Related Skills

- `/pe-buyout` — control buyout investments
- `/private-credit` — lending to growth companies
- `/vc` — earlier-stage venture investments
- `/fpa` — SaaS metrics and unit economics deep dive
