---
name: vc-early
description: |
  Early-stage venture capital — pre-seed through Series A evaluation, term sheets, and cap tables.
  Activate when the user mentions seed round, Series A, pre-seed, angel investment, SAFE, convertible
  note, term sheet, cap table, pro-rata, anti-dilution, liquidation preference, option pool,
  vesting schedule, valuation cap, discount rate, pre-money, post-money, founder dilution,
  or asks about evaluating an early-stage startup or structuring a seed/Series A investment.
---

# Early-Stage Venture Capital

I evaluate early-stage investments (pre-seed through Series A) where the analytical challenge is fundamentally different from later stages: there's limited financial data, so the assessment is about team, market, and product-market fit trajectory rather than unit economics. I structure term sheets that protect downside while preserving founder alignment, and I model cap tables to show dilution through future rounds.

---

## Scope & Boundaries

**What this skill DOES:**
- Evaluate early-stage companies on team, market, product, and traction
- Analyze and structure term sheets (priced rounds, SAFEs, convertible notes)
- Build and model cap tables through multiple funding rounds
- Calculate dilution impact on founders, employees, and early investors
- Structure option pools and analyze their dilution impact
- Assess pre-money/post-money valuation reasonableness
- Model conversion mechanics for SAFEs and convertible notes
- Analyze anti-dilution provisions and their impact on various scenarios

**Use a different skill when:**
- Series B+ / growth-stage analysis → `/vc-growth`
- VC fund construction and portfolio math → `/vc-fund`
- Growth equity (profitable companies) → `/pe-growth`
- Startup pitch deck building → `/pitch-deck`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| VC Returns | `python3 tools/vc_returns.py` | Dilution waterfall, fund metrics |
| IRR / NPV | `python3 tools/irr.py` | Investment return calculation |

---

## Pre-Flight Checks

1. **Stage:** Pre-seed, seed, or Series A?
2. **Company profile:** What they do, founding date, team background
3. **Traction:** Users, revenue, waitlist, LOIs, pilots, design partners
4. **Round terms:** Amount raising, valuation (or cap/discount for SAFEs), instrument type
5. **Existing cap table:** Founders, prior investors, option pool
6. **Your role:** Lead investor, follow-on, angel?

---

## Phase 1: Company Evaluation

**Goal:** Assess the investment without relying on financial projections (which are fiction at this stage).

### The Four Pillars (Early Stage)

**1. Team Assessment**
```
| Criterion | Strong Signal | Weak Signal |
|-----------|--------------|-------------|
| Founder-market fit | Deep domain experience, lived the problem | Career pivot, no industry experience |
| Technical ability | Can build v1 without outsourcing | Needs to hire all technical talent |
| Prior startup experience | Founded/scaled before (even if failed) | First-time, corporate background only |
| Complementarity | Distinct skills (tech + business + domain) | Overlapping backgrounds |
| Obsession level | Working on this for 1yr+, deep rabbit hole | Pivoted recently, exploring |
| Unfair advantage | Unique insight, access, or IP | Replicable idea |
```

**2. Market Assessment**
```
TAM / SAM / SOM:
  TAM (Total Addressable): $[X]B — the entire category
  SAM (Serviceable Addressable): $[X]B — the segment they can reach
  SOM (Serviceable Obtainable): $[X]M — realistic 5-year capture

Market assessment:
  Is it growing >20% annually? [Y/N]
  Is it being created (new category) or disrupted (existing)? [new/disruption]
  Are incumbents vulnerable? Why? [regulation, technology shift, generational]
  Timing: Why now? [cost curve, regulation, behavior change, enabling technology]
```

**3. Product Assessment**
```
| Metric | Signal |
|--------|--------|
| Working product? | Demo > prototype > mockup > slide |
| Usage data? | DAU/MAU > signups > waitlist > nothing |
| User feedback? | Paying customers > design partners > surveys |
| Retention? | Any cohort data showing repeat usage |
| PMF indicators? | "Would be very disappointed" >40% (Sean Ellis test) |
```

**4. Traction & Trajectory**
```
Stage-appropriate traction:
  Pre-seed: Problem validation, team assembled, prototype
  Seed: MVP live, initial users, early retention signal
  Series A: Clear PMF, $1-3M ARR or strong usage metrics, repeatable acquisition

Growth rate (for seed+):
  MoM revenue growth: >15% = strong, 10-15% = good, <10% = concerning
  User growth: >20% MoM for consumer, >10% for B2B
```

**Decision Gate:** At pre-seed/seed, invest in teams and markets. At Series A, require evidence of product-market fit. If there's no PMF signal at Series A, it's too early or the product isn't working.

---

## Phase 2: Term Sheet Analysis

**Goal:** Evaluate and structure deal terms that balance investor protection with founder alignment.

### Priced Round Mechanics
```
Pre-money valuation:         $[X]M
Investment amount:           $[X]M
Post-money valuation:        $[X]M (pre + investment)
Investor ownership:          [X]% (investment / post-money)

Option pool (pre-money):     [X]% (typically 10-20%)
  Creates dilution to founders BEFORE the investment
  Effective pre-money to founders = Pre-money - Option pool value
```

### SAFE / Convertible Note Mechanics
```
SAFE terms:
  Amount:                    $[X]K
  Valuation cap:             $[X]M
  Discount:                  [X]% (typically 15-25%)
  Most Favored Nation:       [Y/N]
  Pro-rata rights:           [Y/N]

Conversion at next priced round:
  If priced round at $[X]M pre-money:
    Cap conversion price:    $[Cap] / [fully diluted shares]
    Discount conversion:     [Round price] × (1 - discount)
    Converts at:             LOWER of cap price and discount price
    Shares issued:           SAFE amount / conversion price
```

### Key Term Sheet Provisions
```
| Term | Founder-Friendly | Investor-Friendly | Standard |
|------|-----------------|-------------------|----------|
| Liquidation preference | 1x non-participating | >1x or participating | 1x non-participating |
| Anti-dilution | Broad-based weighted avg | Full ratchet | Broad-based weighted avg |
| Board seats | Founder majority | Investor majority | 2 founders + 1 investor + 1 independent |
| Protective provisions | Narrow list | Extensive veto rights | Standard set (M&A, debt, new equity) |
| Drag-along | Supermajority (>66%) | Simple majority | Majority of preferred |
| Pay-to-play | None | Full ratchet to common | Broad-based conversion |
| Vesting | 4yr/1yr cliff (standard) | Re-vesting on new round | 4yr/1yr cliff |
```

---

## Phase 3: Cap Table Modeling

**Goal:** Model ownership through current and future rounds showing dilution impact.

```
Pre-Round Cap Table:
| Holder | Shares | Ownership |
|--------|--------|-----------|
| Founder A | [X] | [X]% |
| Founder B | [X] | [X]% |
| Seed investors | [X] | [X]% |
| Option pool (allocated) | [X] | [X]% |
| Option pool (unallocated) | [X] | [X]% |
| SAFE holders | [X] (on conversion) | [X]% |
| Total | [X] | 100% |
```

Run: `python3 tools/vc_returns.py` for dilution waterfall

### Dilution Through Future Rounds
```
| Event | Founder A | Founder B | Seed | Series A | Pool | New |
|-------|-----------|-----------|------|----------|------|-----|
| Founding | 50% | 50% | — | — | — | — |
| Option pool | 40% | 40% | — | — | 20% | — |
| Seed ($3M at $10M) | 31% | 31% | 23% | — | 15% | — |
| Series A ($10M at $40M) | 25% | 25% | 18% | 20% | 12% | — |
| Series B ($25M at $120M) | 21% | 21% | 15% | 17% | 15% | 11% |
```

**Key insight:** Founders who start at 50% each typically hold 15-25% by Series B. If founder ownership drops below 10% before profitability, alignment problems emerge.

---

## Phase 4: Valuation Reasonableness

**Goal:** Assess whether the entry price gives sufficient return potential.

```
Entry valuation:             $[X]M post-money
Target return:               [X]x (fund strategy dependent)
Required exit value:         $[X]M (entry × target return ÷ ownership at exit)
Implied exit revenue:        $[X]M (at [X]x revenue multiple)
Is that revenue achievable?  [assessment based on market size and growth]

Valuation benchmarks (2024-2025):
  Pre-seed: $5-12M post-money
  Seed: $10-25M post-money
  Series A: $25-75M post-money (PMF required)

Red flags:
  - Pre-seed at >$15M with no product
  - Seed at >$30M with <$100K ARR
  - Series A at >$80M with <$2M ARR
```

---

## Quality Gates

- [ ] Team assessed on founder-market fit and complementarity
- [ ] Market sized (TAM/SAM/SOM) with credible methodology
- [ ] Traction evaluated against stage-appropriate benchmarks
- [ ] Term sheet provisions reviewed (liquidation pref, anti-dilution, board, protective)
- [ ] Cap table modeled through current round + 2 future rounds
- [ ] Founder dilution path checked (>10% at profitability?)
- [ ] Valuation reasonableness tested against required exit value

## Hard Constraints

- **NEVER** value an early-stage company on DCF — there are no reliable cash flows to discount
- **NEVER** accept a SAFE without understanding conversion mechanics at every possible valuation
- **ALWAYS** model the option pool shuffle — it's dilutive to founders, not investors
- **ALWAYS** check if the target return requires an unrealistic exit valuation

## Common Pitfalls

1. **Anchoring on TAM** — a $50B TAM means nothing if the startup can capture $5M
2. **Ignoring the option pool shuffle** — a 20% pool on $10M pre-money means founders are really selling at $8M
3. **Participating preferred** — at early stage this is punitive; push for non-participating
4. **Full ratchet anti-dilution** — destroys founder incentives in a down round
5. **Overweighting traction, underweighting team** — at pre-seed, team IS the investment

## Related Skills

- `/vc-growth` — Series B+ and growth-stage analysis
- `/vc-fund` — fund construction and portfolio math
- `/pe-growth` — growth equity for profitable companies
- `/pitch-deck` — building the fundraise deck
