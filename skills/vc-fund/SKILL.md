---
name: vc-fund
description: |
  VC fund construction, portfolio math, and LP reporting. Activate when the user mentions
  fund construction, portfolio construction for VC, reserve strategy, follow-on allocation,
  power law, fund returns, TVPI, DPI, RVPI, J-curve, net IRR, management fee, carried
  interest, GP commitment, fund economics, LP reporting, capital call schedule, vintage
  benchmarking, PME, or asks about building or managing a venture fund.
---

# VC Fund Construction & Portfolio Math

I analyze venture capital at the fund level — portfolio construction, reserve strategy, fund economics, and LP reporting. VC is a power-law business: fund returns are driven by a small number of outlier outcomes. Every portfolio decision should be evaluated through that lens — the question is not "will this company succeed?" but "can this company generate a fund-returning outcome?"

---

## Scope & Boundaries

**What this skill DOES:**
- Design fund portfolio construction (number of investments, check sizes, reserves)
- Model fund economics (management fee, carry, GP commitment, fund lifecycle)
- Calculate fund metrics (gross/net IRR, TVPI, DPI, RVPI, PME)
- Analyze the J-curve and cash flow timing for LPs
- Design reserve and follow-on strategies
- Build LP reporting packages (quarterly reports, capital account statements)
- Benchmark fund performance against vintage peers
- Model power-law return distributions and their implications

**Use a different skill when:**
- Evaluating a specific early-stage deal → `/vc-early`
- Analyzing a growth-stage company → `/vc-growth`
- PE fund analytics → `/pe-buyout` or `/secondaries`
- LP portfolio allocation → `/portfolio` or `/wealth`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| VC Returns | `python3 tools/vc_returns.py` | Fund metrics (TVPI, DPI, RVPI, IRR) |
| IRR / NPV | `python3 tools/irr.py` | Cash flow-based fund returns |
| Monte Carlo | `python3 tools/monte_carlo.py` | Simulating fund return distributions |

---

## Pre-Flight Checks

1. **Fund parameters:** Target size, vintage, strategy (seed, early, multi-stage)
2. **Portfolio design:** Target number of investments, initial check size, reserve ratio
3. **Fund economics:** Management fee, carry, hurdle, GP commit, fund life
4. **Performance data (if existing fund):** Investments, marks, realizations, cash flows
5. **Benchmarking context:** Vintage year, strategy peer group

---

## Phase 1: Portfolio Construction

**Goal:** Design the portfolio to maximize the probability of capturing power-law winners.

### Portfolio Parameters
```
Fund size:                   $[X]M
Management fee (total):      ~[X]% of committed over fund life = $[X]M
Investable capital:          $[X]M (fund size - cumulative fees)
Target investments:          [X] companies
Initial check size:          $[X]M (avg)
Reserve ratio:               [X]% of investable capital for follow-ons
Initial deployment:          $[X]M ([X]% of investable)
Follow-on reserves:          $[X]M ([X]% of investable)
Deployment period:           [X] years
```

### Portfolio Construction Models

**Spray and pray (high count):**
- 40-60+ investments, $500K-2M checks
- Maximize shots on goal, minimal follow-on
- Works at seed; requires high hit rate or massive outlier

**Concentrated (low count):**
- 15-25 investments, larger checks
- Deep diligence, significant follow-on reserves (40-50%)
- Works at Series A+; requires better picking ability

**Barbell:**
- 30-40 initial investments + concentrated follow-on into top 5-10
- Broad initial funnel, then double down on winners
- Most common multi-stage approach

### Reserve Strategy
```
Follow-on allocation decision framework:
| Signal | Action |
|--------|--------|
| Strong performer, inside round, pro-rata available | Follow on at full pro-rata |
| Strong performer, competitive round at step-up | Follow on at half pro-rata |
| Moderate performer, flat/small step-up | Selective — only if new info is positive |
| Underperformer, needs bridge | Generally pass unless strategic value |

Reserve per company:
  Initial check: $[X]M
  Series A follow-on: $[X]M (target [X]% pro-rata)
  Series B follow-on: $[X]M (target [X]% pro-rata)
  Total reserved per co: $[X]M ([X]x initial check)
```

---

## Phase 2: Fund Economics

**Goal:** Model the fee structure and GP/LP economics over the fund lifecycle.

```
Management Fee:
  Commitment period (Years 1-5):    [X]% on committed capital
  Post-commitment (Years 6-10+):    [X]% on invested (or declining)
  Total fees over fund life:        ~$[X]M ([X]% of committed)

Carried Interest:
  Carry rate:                        [X]% (standard: 20%)
  Preferred return (hurdle):         [X]% (standard: 8%)
  Catch-up:                          [X]% to GP after pref met
  Clawback:                          [Y/N]
  Distribution model:                Deal-by-deal or whole fund

GP Commitment:                       $[X]M ([X]% of fund, standard: 1-5%)

Fund lifecycle cash flows:
| Year | Calls | Distributions | Net CF | Cumulative |
|------|-------|--------------|--------|-----------|
| 1 | ($[X]M) | $0 | ($[X]M) | ($[X]M) |
| 2 | ($[X]M) | $0 | ($[X]M) | ($[X]M) |
| 3 | ($[X]M) | $[X]M | ($[X]M) | ($[X]M) |
| ... | | | | J-curve trough |
| 7 | ($[X]M) | $[X]M | $[X]M | ($[X]M) |
| 10 | $0 | $[X]M | $[X]M | $[X]M |
```

---

## Phase 3: Power Law & Fund Return Math

**Goal:** Understand the return distribution and what it takes to return the fund.

### Power Law Distribution
```
Typical VC fund outcome distribution (30 investments):
  0-1x return: 15-20 companies (50-65% of portfolio)
  1-3x return: 5-8 companies (20-25%)
  3-10x return: 3-5 companies (10-15%)
  10-50x return: 1-2 companies (3-7%)
  50x+ return: 0-1 company (0-3%)

Implication: The top 1-2 investments generate 50-80% of fund returns.
The rest of the portfolio provides optionality and learning, not returns.
```

### Fund Return Targets
```
Fund-returning investment analysis:
  Fund size: $[X]M
  Ownership at exit needed to return fund: [X]% at $[X]M exit

  For a $100M fund:
    A $1B exit with 15% ownership = $150M = 1.5x fund
    A $2B exit with 10% ownership = $200M = 2.0x fund
    Need 2-3 of these to make a top-quartile fund (3x+ net)

  Minimum viable outcome per investment:
    Initial check $[X]M → need $[X]M back for fund math to work
    That requires [X]x gross return on the check
```

---

## Phase 4: Fund Metrics & Benchmarking

**Goal:** Calculate and benchmark fund performance.

```
Fund metrics:
  Gross TVPI = (NAV + Distributions) / Called Capital = [X]x
  Net TVPI = (NAV + Distributions - Fees - Carry) / Called Capital = [X]x
  DPI = Distributions / Called Capital = [X]x (cash-on-cash, "the real number")
  RVPI = NAV / Called Capital = [X]x (unrealized, "the hope number")
  Net IRR = [X]% (time-weighted, accounts for J-curve)

  PME (Public Market Equivalent):
    Kaplan-Schoar PME = Fund TVPI / Index TVPI over same period
    PME > 1.0: outperformed public markets
    PME > 1.3: strong outperformance

Vintage benchmarking:
| Metric | Fund | Top Quartile | Median | Bottom Quartile |
|--------|------|-------------|--------|-----------------|
| Net TVPI | [X]x | >[X]x | [X]x | <[X]x |
| Net IRR | [X]% | >[X]% | [X]% | <[X]% |
| DPI | [X]x | >[X]x | [X]x | <[X]x |
```

Run: `python3 tools/vc_returns.py` for fund metrics calculation

---

## Phase 5: LP Reporting

**Goal:** Build the quarterly LP report.

```
Quarterly Report Contents:
1. Fund summary (vintage, size, invested, remaining, NAV)
2. Portfolio overview (investments, exits, write-offs)
3. Performance metrics (TVPI, DPI, RVPI, IRR, PME)
4. Capital account statement (calls, distributions, NAV by LP)
5. Portfolio company updates (top 5-10 companies, key metrics)
6. Pipeline and market commentary
7. ESG / impact reporting (if applicable)
```

---

## Quality Gates

- [ ] Portfolio construction aligned with fund size and strategy
- [ ] Reserve strategy designed with explicit follow-on criteria
- [ ] Fee drag calculated and disclosed (cumulative management fees as % of fund)
- [ ] Power-law math tested (can 1-2 winners return the fund?)
- [ ] Fund metrics calculated correctly (TVPI, DPI, RVPI, net IRR)
- [ ] Benchmarked against appropriate vintage and strategy peers

## Hard Constraints

- **NEVER** calculate fund IRR without accounting for management fees and carry
- **NEVER** benchmark a seed fund against a growth fund — use strategy-matched peers
- **ALWAYS** show DPI alongside TVPI — unrealized gains are not cash
- **ALWAYS** test whether the portfolio construction allows for fund-returning outcomes

## Common Pitfalls

1. **Over-reserving for follow-ons** — leaving 50% for follow-ons means only 50% for new deals
2. **Following on into losers** — reserves should go to winners, not bridges for struggling companies
3. **Ignoring the J-curve** — LPs need to know when cash comes back, not just how much
4. **TVPI without DPI** — a fund with 3x TVPI and 0.5x DPI is mostly unrealized marks
5. **Strategy drift** — a seed fund doing Series B follow-ons is a different fund than marketed

## Related Skills

- `/vc-early` — evaluating individual early-stage deals
- `/vc-growth` — evaluating growth-stage companies
- `/secondaries` — LP secondaries and fund restructuring
- `/attribution` — fund performance attribution
