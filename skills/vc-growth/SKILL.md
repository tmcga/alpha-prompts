---
name: vc-growth
description: |
  Growth-stage venture capital — Series B+ evaluation, sector-specific frameworks.
  Activate when the user mentions Series B, Series C, growth stage, late-stage venture,
  pre-IPO, growth metrics, net revenue retention, burn multiple, magic number, rule of 40,
  SaaS metrics for VC, biotech rNPV, crypto token economics, web3 governance, secondary
  shares, tender offer, or asks about evaluating a company that has product-market fit
  and is scaling revenue.
---

# Growth-Stage Venture Capital

I evaluate Series B+ investments where the analytical framework shifts from team/market/PMF to unit economics, capital efficiency, and path to liquidity. At this stage the data exists — the question is whether the growth rate justifies the price, whether the unit economics support the burn rate, and whether the company can reach a liquidity event that returns the fund.

---

## Scope & Boundaries

**What this skill DOES:**
- Evaluate growth-stage companies on SaaS metrics, cohort behavior, and capital efficiency
- Analyze sector-specific investments: biotech (rNPV), crypto/web3 (token economics), deeptech
- Model growth trajectories with deceleration curves and efficiency benchmarks
- Assess governance for late-stage preferred (ratchets, IPO provisions, redemption rights)
- Evaluate secondary share purchases and tender offers
- Calculate returns under IPO, M&A, and down-round scenarios
- Benchmark against public comps and recent late-stage transactions

**Use a different skill when:**
- Pre-seed through Series A → `/vc-early`
- VC fund-level portfolio math → `/vc-fund`
- Public equity analysis post-IPO → `/long-short`
- Growth equity in profitable companies → `/pe-growth`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| VC Returns | `python3 tools/vc_returns.py` | Fund metrics, dilution waterfall |
| IRR / NPV | `python3 tools/irr.py` | Return calculation |
| DCF | `python3 tools/dcf.py` | DCF for companies approaching profitability |

---

## Pre-Flight Checks

1. **Stage:** Series B, C, D, pre-IPO, or secondary?
2. **Financials:** ARR/revenue, growth rate, gross margin, burn rate, cash on hand
3. **Unit economics:** NRR, CAC payback, LTV/CAC, magic number, burn multiple
4. **Round terms:** Valuation, amount, instrument, key provisions
5. **Sector:** SaaS, biotech, crypto/web3, deeptech, consumer?
6. **Exit timeline:** Expected path to liquidity (IPO, M&A, secondary)

---

## Phase 1: Growth Metrics & Benchmarking

**Goal:** Determine whether growth is efficient, durable, and fundable.

### Core SaaS/Software Metrics
```
| Metric | Company | Top Decile | Median | Bottom Quartile |
|--------|---------|-----------|--------|-----------------|
| ARR Growth (YoY) | [X]% | >100% | 50-80% | <30% |
| Net Revenue Retention | [X]% | >140% | 110-130% | <100% |
| Gross Margin | [X]% | >80% | 70-80% | <65% |
| Burn Multiple | [X]x | <1x | 1-2x | >3x |
| Magic Number | [X] | >1.0 | 0.5-1.0 | <0.5 |
| Rule of 40 | [X] | >60 | 30-50 | <20 |
| CAC Payback | [X]mo | <12 | 12-24 | >24 |
| LTV/CAC | [X]x | >5x | 3-5x | <3x |
```

### Growth Deceleration Analysis
```
Revenue trajectory:
| Period | ARR | QoQ Growth | YoY Growth | Deceleration |
|--------|-----|-----------|-----------|-------------|
| Q-4 | $[X]M | [X]% | [X]% | — |
| Q-3 | $[X]M | [X]% | [X]% | [X]pp |
| Q-2 | $[X]M | [X]% | [X]% | [X]pp |
| Q-1 | $[X]M | [X]% | [X]% | [X]pp |
| Current | $[X]M | [X]% | [X]% | [X]pp |

Natural deceleration: ~5-10pp per year of YoY growth rate decline
If decelerating faster: market saturation, competition, or execution problems
```

**Decision Gate:** If the burn multiple >2x AND growth is decelerating faster than natural, the company is burning cash without efficient growth. Pass or demand better terms.

---

## Phase 2: Sector-Specific Frameworks

### Biotech / Healthcare (rNPV)
```
Risk-adjusted NPV for pipeline:
| Asset | Phase | P(Success) | Peak Sales | rNPV |
|-------|-------|-----------|-----------|------|
| Drug A | Phase 2 | 30% | $[X]M | $[X]M |
| Drug B | Phase 1 | 15% | $[X]M | $[X]M |
| Drug C | Preclinical | 5% | $[X]M | $[X]M |
| Platform value | — | — | — | $[X]M |
| Total rNPV | | | | $[X]M |
| Less: cash burn to milestones | | | | ($[X]M) |
| Net rNPV | | | | $[X]M |

Phase success probabilities (industry average):
  Preclinical → Phase 1: 50%
  Phase 1 → Phase 2: 65%
  Phase 2 → Phase 3: 35%
  Phase 3 → Approval: 60%
  Cumulative (preclinical to approval): ~7%
```

### Crypto / Web3 (Token Economics)
```
Token analysis:
  Total supply:              [X]M tokens
  Circulating supply:        [X]M ([X]% of total)
  Fully diluted valuation:   $[X]M (total supply × price)
  Circulating market cap:    $[X]M

Token distribution:
| Holder | Allocation | Vesting | Unlock Date |
|--------|-----------|---------|-------------|
| Team/founders | [X]% | [X]yr cliff + [X]yr vest | [date] |
| Investors (all rounds) | [X]% | [X]yr vest | [date] |
| Community/ecosystem | [X]% | Various | Ongoing |
| Treasury | [X]% | Governance-controlled | N/A |

Key questions:
  Protocol revenue: $[X]M annualized (real yield vs. token emissions)
  P/Revenue (fully diluted): [X]x
  Token velocity: [X] (higher = more selling pressure)
  Governance concentration: Top 10 wallets control [X]% of voting power
```

---

## Phase 3: Late-Stage Terms & Governance

**Goal:** Evaluate the incremental governance provisions that appear in growth rounds.

```
Late-stage provisions to scrutinize:
| Provision | Impact | Founder-Friendly | Investor-Friendly |
|-----------|--------|-----------------|-------------------|
| IPO ratchet | Guarantees return if IPO below valuation | None | Full ratchet to IPO price |
| Redemption rights | Forces liquidity after [X] years | None | Mandatory redemption |
| Multiple liquidation pref | Multiples of investment before common | 1x non-participating | 2-3x participating |
| Senior preference | New round first in liquidation stack | Pari passu with prior | Senior to all prior |
| Registration rights | Demand, piggyback, S-3 | Piggyback only | Demand rights |
| Pay-to-play | Protects against free riders | None | Conversion to common |
```

**Structure complexity score:** Count the non-standard terms. If >3 non-standard provisions, the deal is over-engineered — complexity usually benefits the party that proposed it.

---

## Phase 4: Return Modeling

**Goal:** Calculate returns under multiple exit scenarios with dilution.

```
Investment: $[X]M for [X]% at $[X]M post-money

Scenario analysis:
| Scenario | Exit Value | Ownership at Exit | Proceeds | MOIC | IRR |
|----------|-----------|-------------------|----------|------|-----|
| IPO (bull) | $[X]B | [X]% | $[X]M | [X]x | [X]% |
| IPO (base) | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| M&A | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| Down round | $[X]M | [X]% | $[X]M | [X]x | [X]% |
| Shutdown | $0 | — | $[X]M (pref) | [X]x | neg |

Notes:
- Ownership at exit accounts for future dilution (1-2 more rounds + pool refresh)
- Down round scenario includes anti-dilution adjustment
- Shutdown returns = liquidation preference (1x of invested)
```

**Fund return contribution:** Does this single investment have the potential to return [X]% of the fund? For a $500M fund, each investment should have a realistic path to $150M+ in proceeds.

---

## Phase 5: Secondary Share Analysis

**Goal:** Evaluate purchasing existing shares from employees or early investors.

```
Secondary purchase terms:
  Seller:                    [Employee / early investor / founder]
  Shares:                    [X] common shares
  Price per share:           $[X] ([X]% discount to last preferred)
  Implied valuation:         $[X]M
  Transfer restrictions:     ROFR, board approval, information rights?

Discount analysis:
  Last preferred price:      $[X]/share
  409A fair market value:    $[X]/share
  Secondary price:           $[X]/share
  Discount to preferred:     [X]%

Typical secondary discounts:
  High-demand (pre-IPO): 5-15% discount to last round
  Growth stage: 15-30% discount
  Illiquid / early: 30-50% discount
```

---

## Quality Gates

- [ ] Growth metrics benchmarked against stage-appropriate cohorts
- [ ] Growth deceleration curve analyzed
- [ ] Burn multiple and capital efficiency assessed
- [ ] Sector-specific framework applied (rNPV for biotech, token econ for crypto)
- [ ] Late-stage terms scrutinized for non-standard provisions
- [ ] Returns modeled across IPO, M&A, down round, and shutdown
- [ ] Future dilution from additional rounds accounted for

## Hard Constraints

- **NEVER** invest at growth stage without verifiable unit economics
- **NEVER** ignore the burn multiple — it's the single best efficiency metric
- **ALWAYS** model growth deceleration — no company grows at 100% forever
- **ALWAYS** check if the investment can return a meaningful % of the fund

## Common Pitfalls

1. **Valuation anchoring to last round** — private round prices are negotiated, not market-cleared
2. **Ignoring structure** — a $1B valuation with 3x participating preferred is really a $333M common valuation
3. **Linear growth projections** — model the deceleration curve, not the hockey stick
4. **Sector tourism** — biotech and crypto require specialized knowledge; generic VC frameworks fail
5. **Secondary without information** — buying shares without financial access is blind risk

## Related Skills

- `/vc-early` — pre-seed through Series A
- `/vc-fund` — fund construction and portfolio math
- `/pe-growth` — growth equity in profitable companies
- `/long-short` — public market analysis post-IPO
