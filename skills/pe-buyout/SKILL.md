---
name: pe-buyout
description: |
  PE buyout analysis — LBO modeling, operational value creation, and exit planning.
  Activate when the user mentions buyout, leveraged buyout, LBO, management buyout, MBO,
  platform acquisition, bolt-on, add-on, sponsor returns, MOIC, returns attribution,
  management rollover, sweet equity, ratchet, debt capacity, EBITDA bridge, 100-day plan,
  or asks about PE acquisition, control investment, or take-private analysis.
---

# PE Buyout Analysis

I analyze control buyout investments from deal screening through exit. Every buyout is a bet on three levers: EBITDA growth, multiple expansion, and deleveraging. I build complete models that make each lever's contribution explicit and stress-testable, with the rigor of a senior associate presenting to investment committee.

---

## Scope & Boundaries

**What this skill DOES:**
- Screen businesses for buyout attractiveness (cash flow, defensibility, margin opportunity)
- Build complete LBO models with sources & uses, operating projections, and debt schedule
- Decompose returns into EBITDA growth, multiple expansion/contraction, and deleveraging
- Design operational value creation plans with quantified EBITDA bridges
- Structure management equity programs (rollover, sweet equity, ratchets, options)
- Model platform + bolt-on acquisition strategies with accretion analysis
- Analyze exit scenarios (strategic sale, secondary buyout, IPO, dividend recap)
- Stress test returns against revenue decline, margin compression, and rate increases

**Use a different skill when:**
- Growth equity / minority investment → `/pe-growth`
- Private credit / direct lending → `/private-credit`
- LP secondaries or GP-led continuation → `/secondaries`
- Sell-side M&A process → `/sell-side`
- Real estate PE → `/re-acquisitions`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| LBO | `python3 tools/lbo.py` | MOIC, IRR, returns attribution |
| DCF | `python3 tools/dcf.py` | Standalone valuation for entry price |
| WACC | `python3 tools/wacc.py` | Cost of capital, unlevered beta |
| IRR / NPV | `python3 tools/irr.py` | General-purpose equity return calculation |
| Kelly | `python3 tools/kelly.py` | Position sizing within a PE fund |
| Credit Spread | `python3 tools/credit_spread.py` | Z-Score for target companies |

---

## Pre-Flight Checks

1. **Target profile:** Company name, industry, revenue, EBITDA, margins, growth rate
2. **Entry valuation:** Enterprise value, EV/EBITDA multiple, equity value
3. **Capital structure:** Total leverage, debt tranches, rates, amortization
4. **Operating assumptions:** Revenue growth, margin trajectory, capex, working capital
5. **Exit assumptions:** Hold period, exit multiple, exit method
6. **Value creation thesis:** What operational improvements justify the investment?

---

## Phase 1: Deal Screening

**Goal:** Assess whether the business is an attractive buyout candidate before modeling.

**Buyout attractiveness scorecard:**

| Criterion | Strong | Moderate | Weak |
|-----------|--------|----------|------|
| Revenue visibility | Recurring/contracted | Repeat but discretionary | Project-based/lumpy |
| Margin opportunity | Below peers, clear levers | In-line, some upside | At/above peers |
| Cash conversion | FCF/EBITDA >70% | 50-70% | <50% |
| Debt capacity | Stable CF, hard assets | Moderate cyclicality | Highly cyclical |
| Market position | #1-2 in niche | Top 5 | Fragmented, no moat |
| Management | Strong, aligned | Competent, needs support | Needs replacement |
| Growth avenues | Organic + M&A | Organic only | Mature/declining |

**Decision Gate:** If the business fails 3+ criteria, it's not a control buyout — consider growth equity or credit instead.

---

## Phase 2: Sources & Uses and Capital Structure

**Goal:** Build the transaction capital structure.

```
SOURCES                         USES
Senior Term Loan    $[X]M       Enterprise Value      $[X]M
Second Lien/Sub     $[X]M       Transaction Fees      $[X]M
Mezzanine           $[X]M       Financing Fees        $[X]M
Rollover Equity     $[X]M       Refinance Existing    $[X]M
Sponsor Equity      $[X]M       Cash to Balance Sheet $[X]M
─────────────────────────       ──────────────────────────────
Total Sources       $[X]M       Total Uses            $[X]M
```

**Leverage benchmarks by industry:**
| Industry | Total Leverage | Senior | Sub/Mezz |
|----------|---------------|--------|----------|
| Software/SaaS | 5-7x | 4-5x | 1-2x |
| Healthcare services | 5-6x | 3.5-4.5x | 1-1.5x |
| Industrial/manufacturing | 3-5x | 2.5-3.5x | 0.5-1.5x |
| Consumer/retail | 3-4.5x | 2.5-3.5x | 0.5-1x |
| Business services | 5-6.5x | 4-5x | 1-1.5x |

---

## Phase 3: LBO Modeling

**Goal:** Project operating performance and calculate returns.

Run: `python3 tools/lbo.py --ebitda [X] --entry-multiple [X] --exit-multiple [X] --leverage [X] --rate [X] --growth [X] --years [X]`

### Operating Projections (5-Year)
```
| Metric          | Entry  | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|-----------------|--------|--------|--------|--------|--------|--------|
| Revenue         | $[X]M  |        |        |        |        |        |
| Revenue Growth  |        | [X]%   | [X]%   | [X]%   | [X]%   | [X]%   |
| EBITDA          | $[X]M  |        |        |        |        |        |
| EBITDA Margin   | [X]%   |        |        |        |        |        |
| Capex           |        |        |        |        |        |        |
| Free Cash Flow  |        |        |        |        |        |        |
```

### Returns Attribution
```
Entry Equity:        $[X]M
Exit Equity:         $[X]M
MOIC:                [X]x
IRR:                 [X]%

Attribution:
  EBITDA Growth:     [X]x  ([X]% of return)
  Multiple Change:   [X]x  ([X]% of return)
  Deleveraging:      [X]x  ([X]% of return)
```

**Sanity check:** If >50% of returns come from multiple expansion, the thesis is speculative. If >60% comes from deleveraging, the deal is primarily a leverage play, not a value creation story.

---

## Phase 4: Operational Value Creation

**Goal:** Build the EBITDA bridge from entry to exit — the "100-day plan" in numbers.

```
EBITDA Bridge (Entry → Exit):
  Entry EBITDA:                          $[X]M
  (+) Revenue growth (organic):          $[X]M
  (+) Pricing / mix improvement:         $[X]M
  (+) Cost reduction (COGS):             $[X]M
  (+) SG&A optimization:                 $[X]M
  (+) Procurement savings:               $[X]M
  (+) Bolt-on acquisitions:              $[X]M
  (-) Investment / reinvestment:        ($[X]M)
  = Exit EBITDA:                         $[X]M
  EBITDA CAGR:                           [X]%
```

**Value creation categories:**
1. **Revenue synergies:** Cross-sell, geographic expansion, new products, pricing
2. **Cost synergies:** Procurement, headcount, facilities, technology consolidation
3. **Working capital:** Inventory optimization, receivables management, payables extension
4. **Capex efficiency:** Prioritization, shared services, technology-enabled operations
5. **M&A:** Bolt-on acquisitions at lower multiples (buy at 5-7x, consolidate onto platform at 10-12x)

---

## Phase 5: Management Equity & Alignment

**Goal:** Structure management incentives that align with fund returns.

```
Management Equity Structure:
  Rollover equity:     [X]% of pre-transaction equity ($[X]M)
  Sweet equity/MIP:    [X]% of post-close equity (vesting over [X] years)
  Options/Ratchet:     Strike at [X]x MOIC, [X]% additional equity at [X]x+

Total management ownership (fully diluted):
  At entry:            [X]%
  At base case exit:   [X]% (after sweet equity + ratchet vest)
  At upside exit:      [X]% (full ratchet)
```

**Alignment test:** Does management earn more from operational improvement than from financial engineering? If the majority of management's upside comes from leverage, the incentive structure is misaligned.

---

## Phase 6: Exit Analysis

**Goal:** Model multiple exit scenarios with probability-weighted returns.

| Exit Scenario | Probability | Exit Multiple | MOIC | IRR |
|--------------|------------|--------------|------|-----|
| Strategic sale | [X]% | [X]x | [X]x | [X]% |
| Secondary buyout | [X]% | [X]x | [X]x | [X]% |
| IPO | [X]% | [X]x | [X]x | [X]% |
| Dividend recap + hold | [X]% | N/A | [X]x | [X]% |
| **Probability-weighted** | **100%** | | **[X]x** | **[X]%** |

**Decision Gate:** If the probability-weighted IRR is below the fund's hurdle rate (typically 15-20% net), the deal doesn't clear committee.

---

## Phase 7: Sensitivity & Stress Testing

### IRR Sensitivity: Entry Multiple vs. Exit Multiple
| Entry \ Exit | [X-1]x | [X]x | [X+1]x | [X+2]x |
|-------------|--------|------|--------|--------|
| [X-1]x | | | | |
| [X]x | | **base** | | |
| [X+1]x | | | | |

### Stress Scenarios
| Scenario | Assumption | MOIC | IRR | Equity at Risk |
|----------|-----------|------|-----|---------------|
| Revenue miss -15% | Growth halves | [X]x | [X]% | |
| Margin compression -200bps | Cost inflation | [X]x | [X]% | |
| Multiple contraction -2x | Market correction | [X]x | [X]% | |
| Rate shock +300bps | Floating rate debt | [X]x | [X]% | |
| Combined downside | All of the above | [X]x | [X]% | |

---

## Quality Gates

- [ ] Buyout attractiveness screened before modeling
- [ ] Sources & uses balanced
- [ ] Returns decomposed into EBITDA growth / multiple / leverage
- [ ] EBITDA bridge from entry to exit with quantified initiatives
- [ ] Management equity structure reviewed for alignment
- [ ] Multiple exit scenarios with probability-weighted returns
- [ ] Sensitivity table and stress tests completed

## Hard Constraints

- **NEVER** present an IRR without returns attribution (growth vs. multiple vs. leverage)
- **NEVER** assume multiple expansion as the primary return driver without justification
- **ALWAYS** stress test against revenue miss + margin compression + multiple contraction
- **ALWAYS** check FCF conversion — EBITDA growth means nothing without cash flow

## Common Pitfalls

1. **Paying for growth twice** — buying at a premium multiple AND modeling aggressive growth
2. **Ignoring working capital** — fast-growing businesses consume cash in receivables and inventory
3. **Straight-line margin expansion** — identify specific cost levers, not just "we'll get more efficient"
4. **Bolt-on accretion math without integration cost** — acquisition synergies take time and money
5. **Exit multiple = entry multiple** — market conditions change over 5 years

## Related Skills

- `/pe-growth` — minority growth equity investments
- `/private-credit` — direct lending and subordinate debt
- `/secondaries` — LP secondaries and GP-led continuation vehicles
- `/lbo` — focused LBO modeling tool (lighter than full buyout analysis)
- `/sell-side` — when running the sell-side process for portfolio companies
