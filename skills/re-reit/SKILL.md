---
name: re-reit
description: |
  Public REIT analysis — NAV, FFO/AFFO, implied cap rates, and sector comparables.
  Activate when the user mentions REIT, FFO, AFFO, NAV discount, NAV premium,
  funds from operations, REIT valuation, REIT dividend, payout ratio, implied cap rate,
  public vs private real estate, REIT sector analysis, same-store NOI growth,
  REIT balance sheet, or asks about publicly traded real estate companies.
---

# REIT Analysis

I analyze publicly traded REITs through three lenses: asset value (NAV), earnings power (FFO/AFFO), and relative value (implied cap rates vs. private market). REITs are unique — they're real estate portfolios wrapped in a corporate structure, so the analysis combines property-level underwriting with equity market valuation.

---

## Scope & Boundaries

**What this skill DOES:**
- Build Net Asset Value (NAV) models by segment with appropriate cap rates
- Calculate and adjust FFO and AFFO (the REIT equivalents of earnings)
- Derive implied cap rates from stock price and compare to private market
- Analyze dividend coverage and sustainability (payout ratios)
- Compare REITs on NAV premium/discount, FFO multiple, dividend yield, and growth
- Evaluate REIT balance sheets (leverage, maturity profile, floating rate exposure)
- Analyze same-store NOI growth, leasing spreads, and occupancy trends

**Use a different skill when:**
- Analyzing a specific property acquisition → `/re-acquisitions`
- Evaluating a development project → `/re-development`
- Structuring private real estate debt → `/re-debt`
- Corporate M&A involving a REIT → `/sell-side` or `/buy-side`

---

## Available Tools

| Tool | Command | When to Use |
|------|---------|-------------|
| Cap Rate | `python3 tools/cap_rate.py` | Segment-level valuation for NAV |
| DCF | `python3 tools/dcf.py` | Cash flow valuation of REIT equity |
| WACC | `python3 tools/wacc.py` | Cost of capital for REIT |
| IRR / NPV | `python3 tools/irr.py` | Total return analysis |

---

## Pre-Flight Checks

1. **REIT name and sector:** Office, industrial, multifamily, retail, healthcare, data center, etc.?
2. **Financial data:** Revenue, NOI by segment, FFO, AFFO, dividend, share count
3. **Balance sheet:** Total debt, net debt, preferred, weighted avg rate, maturity schedule
4. **Portfolio data:** Property count, SF/units, occupancy, same-store NOI growth
5. **Market data:** Current share price, market cap, trading multiples
6. **Comparables:** 3-5 peer REITs for relative valuation

---

## Phase 1: Net Asset Value (NAV)

**Goal:** Value the REIT's real estate portfolio as if selling each segment in the private market.

### Step 1.1: Segment-Level Valuation
```
| Segment       | NOI ($M)  | Cap Rate | Implied Value ($M) |
|---------------|-----------|----------|--------------------|
| [Segment 1]   | $[X]      | [X]%     | $[X]               |
| [Segment 2]   | $[X]      | [X]%     | $[X]               |
| Development   | —         | —        | $[X] (at cost)     |
| Land bank     | —         | —        | $[X] (appraised)   |
| Other assets  |           |          | $[X]               |
───────────────────────────────────────────────────────
Gross Asset Value (GAV):               $[X]M
```

**Cap rate selection:** Use private market transaction cap rates for each segment. Do NOT use the REIT's implied cap rate — that's circular.

### Step 1.2: NAV Calculation
```
Gross Asset Value:           $[X]M
(+) Cash and equivalents:    $[X]M
(+) Other assets:            $[X]M
(-) Total debt:             ($[X]M)
(-) Preferred equity:       ($[X]M)
(-) Other liabilities:      ($[X]M)
(-) G&A capitalized:        ($[X]M) (annual G&A / cap rate as ongoing drag)
───────────────────────────────────────
= Net Asset Value:           $[X]M
÷ Diluted shares:            [X]M
= NAV per share:             $[X]

Current share price:          $[X]
NAV premium / (discount):     [X]%
```

**Interpretation:**
- Trading at >10% discount to NAV → potential value opportunity (or market pricing in risk)
- Trading at >10% premium to NAV → market pricing in growth or management value
- Trading near NAV → fairly valued relative to private market

---

## Phase 2: FFO and AFFO Analysis

**Goal:** Calculate the REIT's sustainable cash earnings and dividend coverage.

### FFO (Funds From Operations)
```
GAAP Net Income:                     $[X]M
(+) Real estate depreciation:        $[X]M
(-) Gains on property sales:        ($[X]M)
(+) Impairment charges:              $[X]M
(+/-) Unconsolidated JV adjustments: $[X]M
= FFO:                               $[X]M
FFO per share:                       $[X]
```

### AFFO (Adjusted FFO)
```
FFO:                                 $[X]M
(-) Recurring capex (maintenance):  ($[X]M)  ← not growth capex
(-) Straight-line rent adjustments: ($[X]M)
(-) Amortization of lease costs:    ($[X]M)
(-) Stock-based compensation:       ($[X]M)
= AFFO:                             $[X]M
AFFO per share:                      $[X]
```

### Dividend Analysis
```
Annual dividend per share:           $[X]
AFFO payout ratio = Dividend / AFFO: [X]%

Payout ratio assessment:
  < 70%:  well-covered, room for growth and retention
  70-85%: healthy, sustainable with modest growth
  85-95%: tight, limited cushion for NOI decline
  > 95%:  at risk — dividend cut probable if NOI softens
```

---

## Phase 3: Implied Cap Rate Analysis

**Goal:** Compare the market's implicit valuation of the real estate to private market pricing.

```
Enterprise Value = Market Cap + Net Debt + Preferred
                 = $[X]M + $[X]M + $[X]M = $[X]M

Implied Cap Rate = Total Portfolio NOI / Enterprise Value = [X]%

Private market cap rate for comparable assets: [X]%

If implied > private: REIT is CHEAP (buy the stock, sell the buildings)
If implied < private: REIT is EXPENSIVE (sell the stock, buy buildings directly)
```

**Spread analysis:**
```
Implied cap rate:          [X]%
Private market cap rate:   [X]%
Spread:                    [X] bps

Historical average spread: ~50-100bps (REITs typically trade slightly wide due to
  management fees, G&A, and lower liquidity premium capture)

Wide spread (>150bps): REIT is cheap vs. private market — potential catalyst from
  M&A, privatization, or asset sales
Negative spread: REIT is expensive — market paying a growth/management premium
```

---

## Phase 4: Relative Valuation

**Goal:** Compare the REIT to sector peers on key metrics.

```
| Metric           | Subject | Peer 1 | Peer 2 | Peer 3 | Sector Avg |
|------------------|---------|--------|--------|--------|------------|
| P/FFO            | [X]x    | [X]x   | [X]x   | [X]x   | [X]x       |
| P/AFFO           | [X]x    | [X]x   | [X]x   | [X]x   | [X]x       |
| NAV Prem/(Disc)  | [X]%    | [X]%   | [X]%   | [X]%   | [X]%       |
| Dividend Yield   | [X]%    | [X]%   | [X]%   | [X]%   | [X]%       |
| AFFO Payout      | [X]%    | [X]%   | [X]%   | [X]%   | [X]%       |
| SS NOI Growth    | [X]%    | [X]%   | [X]%   | [X]%   | [X]%       |
| Net Debt/EBITDA  | [X]x    | [X]x   | [X]x   | [X]x   | [X]x       |
| Occupancy        | [X]%    | [X]%   | [X]%   | [X]%   | [X]%       |
```

**Valuation premium/discount drivers:**
- Higher growth → higher FFO multiple justified
- Better balance sheet → lower risk premium
- Superior same-store NOI growth → operating quality
- Development pipeline → embedded growth option
- Management quality → repeat performance, capital allocation track record

---

## Phase 5: Balance Sheet & Risk Analysis

**Goal:** Assess leverage, liquidity, and maturity risk.

```
Key metrics:
  Net Debt / EBITDA:                [X]x  (target: <6x for IG, <8x for non-IG)
  Fixed Charge Coverage:            [X]x  (EBITDA / (interest + preferred divs))
  % Floating Rate Debt:             [X]%  (higher = more rate sensitivity)
  Weighted Avg Interest Rate:       [X]%
  Weighted Avg Maturity:            [X] years
  Unencumbered Asset Ratio:         [X]x  (unencumbered NOI / unsecured debt)

Maturity schedule:
| Year | Maturities ($M) | % of Total | Refinancing Risk |
|------|----------------|-----------|------------------|
| [Y]  | $[X]           | [X]%      | [Low/Med/High]   |
| [Y+1]| $[X]           | [X]%      |                  |
```

**Credit rating indicators:**
- Investment grade (BBB- or better): net debt/EBITDA <6x, fixed charge >2.5x
- High yield: net debt/EBITDA 6-10x, limited unsecured access

---

## Quality Gates

- [ ] NAV built from segment-level cap rates (not implied from stock price)
- [ ] FFO and AFFO calculated with all standard adjustments
- [ ] Dividend coverage assessed (AFFO payout ratio)
- [ ] Implied cap rate compared to private market
- [ ] Peer comparison on 5+ metrics
- [ ] Balance sheet risk assessed (leverage, maturities, floating rate exposure)

## Hard Constraints

- **NEVER** use the REIT's implied cap rate to calculate its own NAV (circular)
- **NEVER** compare REIT P/E ratios — use FFO or AFFO multiples
- **ALWAYS** adjust FFO to AFFO before assessing dividend sustainability
- **ALWAYS** check if same-store NOI growth is organic or acquisition-driven

## Common Pitfalls

1. **Using GAAP earnings for REITs** — depreciation makes net income meaningless; use FFO/AFFO
2. **Ignoring development pipeline** — value at cost, not stabilized value (risk not yet resolved)
3. **Confusing FFO with AFFO** — AFFO strips out recurring capex; it's the better cash flow measure
4. **NAV without G&A adjustment** — capitalize G&A as a drag on asset value
5. **Sector mismatch in peer comps** — data center REITs trade differently than office REITs

## Related Skills

- `/re-acquisitions` — analyze specific properties in the REIT's portfolio
- `/re-development` — evaluate the REIT's development pipeline
- `/re-debt` — analyze the REIT's debt structure and refinancing risk
- `/long-short` — equity L/S thesis construction for REIT stocks
