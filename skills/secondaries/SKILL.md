---
name: secondaries
description: |
  PE secondaries analysis — LP interest transfers, GP-led continuation vehicles, and NAV lending.
  Activate when the user mentions secondaries, LP secondary, GP-led continuation,
  continuation fund, tender offer, strip sale, NAV lending, NAV line, preferred equity
  on fund, fund restructuring, stapled secondary, LP portfolio, blind pool discount,
  J-curve mitigation, DPI acceleration, or asks about buying or selling PE fund interests.
---

# PE Secondaries Analysis

I analyze secondary transactions in private equity — buying and selling existing fund interests. Secondaries are the liquidity mechanism for an illiquid asset class. The key analytical challenge is valuing a portfolio of companies that you can see but can't control, at a price that compensates for the remaining blind pool risk and generates an acceptable return over a compressed hold period.

---

## Scope & Boundaries

**What this skill DOES:**
- Value LP fund interests using NAV analysis and discount/premium assessment
- Model GP-led continuation vehicle economics (rollover vs. cash-out)
- Analyze LP portfolio sales (strip deals, full portfolio, single-fund)
- Calculate expected returns under various discount-to-NAV scenarios
- Assess blind pool risk and vintage concentration
- Model J-curve mitigation from buying seasoned fund interests
- Analyze NAV lending structures (fund-level credit facilities)
- Evaluate stapled secondaries (commitment to new fund + secondary purchase)

**Use a different skill when:**
- Direct PE investing → `/pe-buyout` or `/pe-growth`
- Private credit → `/private-credit`
- Fund formation and construction → `/vc` (for VC fund math) or `/pe-buyout` (PE fund metrics)

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| IRR / NPV | `python3 tools/irr.py` | Buyer return calculation at various discounts |
| VC Returns | `python3 tools/vc_returns.py` | Fund metrics (TVPI, DPI, RVPI) |
| DCF | `python3 tools/dcf.py` | Cash flow valuation of remaining portfolio |

---

## Pre-Flight Checks

1. **Transaction type:** LP interest sale, GP-led continuation, tender offer, strip sale?
2. **Fund details:** Vintage, strategy, size, GP, current NAV, TVPI, DPI, RVPI
3. **Portfolio data:** Underlying company details, hold periods, recent marks
4. **Remaining commitments:** Unfunded obligations, expected call schedule
5. **Pricing:** Bid/ask as % of NAV
6. **Seller motivation:** Liquidity need, denominator effect, strategy change, regulatory

---

## Phase 1: NAV Analysis & Pricing

**Goal:** Determine fair value relative to reported NAV.

```
Fund snapshot:
  Vintage:              [X]
  Fund size:            $[X]M
  LP commitment:        $[X]M
  Drawn capital:        $[X]M ([X]% called)
  Remaining commitment: $[X]M
  Reported NAV:         $[X]M
  Distributions to date:$[X]M

Fund metrics:
  TVPI (NAV + distributions) / called = [X]x
  DPI (distributions / called) = [X]x
  RVPI (NAV / called) = [X]x
  Net IRR: [X]%
```

### Discount/Premium Assessment

| Factor | Premium | NAV | Discount |
|--------|---------|-----|---------|
| GP quality / track record | Top quartile | Median | Bottom quartile |
| Portfolio quality | Strong performers | Mixed | Impaired assets |
| Fund maturity | Late (2-3yr to exit) | Mid-life | Early (5+ years) |
| Unfunded commitment | <10% remaining | 20-40% | >40% (blind pool) |
| Sector attractiveness | Tailwind sectors | Neutral | Headwind sectors |
| Market conditions | Seller's market | Balanced | Buyer's market |

**Typical pricing ranges:**
- Top-quartile, late-life: 95-105% of NAV
- Median fund, mid-life: 85-95% of NAV
- Bottom-quartile or early: 70-85% of NAV
- Distressed seller / tail-end: 50-75% of NAV

---

## Phase 2: Return Modeling

**Goal:** Calculate expected returns at various purchase prices.

```
Purchase at [X]% of NAV:
  Cost basis: $[X]M (NAV $[X]M × [X]%)
  (+) Remaining unfunded: $[X]M (assumed called over [X] years)
  Total investment: $[X]M

Expected distributions:
  Near-term (Year 1-2): $[X]M (from assets close to exit)
  Medium-term (Year 2-4): $[X]M (from portfolio growth + exits)
  Tail (Year 4+): $[X]M (remaining assets)

Expected total return: $[X]M
MOIC: [X]x
IRR: [X]%
```

### Sensitivity: IRR by Discount and Hold Period

| Discount to NAV | 2-Year Exit | 3-Year Exit | 4-Year Exit |
|-----------------|------------|------------|------------|
| 5% (95% of NAV) | [X]% | [X]% | [X]% |
| 10% (90%) | [X]% | [X]% | [X]% |
| 15% (85%) | [X]% | [X]% | [X]% |
| 20% (80%) | [X]% | [X]% | [X]% |

Run: `python3 tools/irr.py --cfs="[-cost, dist_y1, dist_y2, dist_y3, dist_y4]"`

---

## Phase 3: GP-Led Continuation Vehicles

**Goal:** Analyze a GP-led continuation fund from both GP and LP perspectives.

```
Continuation vehicle structure:
  Asset(s) rolling:              [Company/portfolio description]
  Current GP valuation:          $[X]M
  New vehicle size:              $[X]M
  LP options:
    (a) Cash out at [X]% of NAV  ($[X]M)
    (b) Roll into continuation    (at NAV)
  New investor commitment:       $[X]M at [X]% discount
  GP rollover:                   [X]% of carry + co-invest

Economics:
  New management fee:            [X]% on committed/invested
  New carry:                     [X]% above [X]% pref
  GP crystallized carry:         $[X]M (from old fund marks)
```

**LP decision framework:**
| Factor | Roll | Cash Out |
|--------|------|----------|
| Belief in asset upside | High — more value to create | Low — fully valued |
| GP conflict of interest | Manageable — fairness opinion | Concerning — GP buying from itself |
| Liquidity need | None | Immediate need |
| Discount on new money | Rolls at NAV (no discount) | Cash at NAV |
| Information advantage | Full access as existing LP | N/A |

**Red flags:** GP crystallizing large carry on the transfer, no fairness opinion, new vehicle terms worse than original fund, no LPAC involvement.

---

## Phase 4: NAV Lending

**Goal:** Analyze fund-level credit facilities secured by portfolio NAV.

```
NAV Facility:
  Fund NAV:                      $[X]M
  Advance rate:                  [X]% of NAV
  Facility size:                 $[X]M
  Rate:                          SOFR + [X]bps
  Maturity:                      [X] years
  Covenants:                     Min NAV coverage [X]x, LTV ≤[X]%

Use of proceeds:
  (a) DPI acceleration — distribute cash to LPs
  (b) Bridge unfunded commitments
  (c) Fund GP commitment
  (d) Portfolio company support
```

**Risk assessment:** NAV lending creates fund-level leverage. If portfolio companies decline in value, the fund may face a margin call requiring asset sales at distressed prices.

---

## Quality Gates

- [ ] Fund metrics verified (TVPI, DPI, RVPI, IRR)
- [ ] NAV independently assessed (not just GP-reported)
- [ ] Discount/premium justified with factor analysis
- [ ] Returns modeled at 3+ discount levels
- [ ] Unfunded commitments included in total investment cost
- [ ] GP-led: conflict of interest assessment completed
- [ ] Stress test: what if portfolio marks down 20-30%?

## Hard Constraints

- **NEVER** assume reported NAV is fair value without independent assessment
- **NEVER** ignore unfunded commitments — they are a real cash obligation
- **ALWAYS** assess GP conflict of interest in continuation vehicles
- **ALWAYS** stress test against a 20-30% portfolio markdown

## Common Pitfalls

1. **Trusting stale NAVs** — marks can be 3-6 months old, especially in volatile markets
2. **Ignoring unfunded commitments** — buying a 60%-called fund means you owe 40% more
3. **GP-led at inflated marks** — GP has incentive to mark high to crystallize carry
4. **Concentrating on a single fund** — secondaries work best as diversified portfolios
5. **Forgetting J-curve on remaining commitments** — unfunded calls create negative early cash flows

## Related Skills

- `/pe-buyout` — understanding the underlying buyout investments
- `/pe-growth` — understanding growth equity portfolio companies
- `/private-credit` — NAV lending and fund-level credit
- `/attribution` — fund performance attribution
