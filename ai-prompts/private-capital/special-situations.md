# Special Situations

Prompt templates for special situations and tactical opportunistic investing, covering rescue financing, distressed-for-control, structured equity solutions, opportunistic real assets, and cross-asset arbitrage.

## Role Context

```
You are a partner at a special situations fund ($4B AUM) that invests across the capital
structure in complex, time-sensitive, and often distressed opportunities. You are equally
comfortable structuring rescue preferred equity for a cash-strapped growth company,
credit-bidding for a bankrupt industrial business, buying non-performing loan portfolios
at a discount, or providing litigation finance. Your edge is structural complexity — you
create value by solving problems that traditional capital providers cannot or will not
touch. You think in terms of risk-adjusted returns, downside-protected structures with
equity upside, and probability-weighted outcomes across multiple scenarios. Every deal
must have asymmetric payoff: limited downside with meaningful upside optionality. Your
target is 15-25% gross IRR with a strong preference for current income or structural
protections that reduce the probability of permanent capital loss.
```

For foundational PE frameworks (LBO math, due diligence), see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below focus on the structural, legal, and analytical complexity unique to special situations.

---

## 1. Rescue Financing

### DIP Lending and Bridge Loan Structuring

```
Evaluate a rescue financing opportunity for [company]:

Situation:
- Company: [name], [industry]
- Revenue: $[X]M, EBITDA: $[X]M (down from $[X]M peak)
- Existing debt: $[X]M senior secured, $[X]M unsecured
- Cash on hand: $[X]M
- Monthly burn / cash drain: $[X]M
- Runway without new capital: [X] months
- Cause of distress: [operational / cyclical / over-leveraged / litigation / customer loss]
- Current status: [out-of-court restructuring / pre-petition / Chapter 11 filed]

Rescue financing proposal:

Option A — DIP Financing (if in Chapter 11):
- DIP facility: $[X]M (new money)
  - Tranche 1: $[X]M roll-up of prepetition secured debt (at par, achieves super-priority)
  - Tranche 2: $[X]M new money
- Super-priority administrative claim: ahead of all prepetition debt
- Adequate protection for existing secured lenders: [replacement liens / cash payments / equity]
- Rate: SOFR + [X]bps (reflects super-priority, short duration)
- OID: [X]%
- Term: [X] months (expected timeline through plan confirmation)
- Milestones: [filing deadline, plan proposal deadline, sale process timeline]
- Budget: DIP budget approved by court, variance tolerance of [X]%
- Equity conversion: right to convert DIP to exit financing or equity in plan

Option B — Bridge Loan (out-of-court):
- Amount: $[X]M
- Security: [first-priority lien on all assets / second lien / specific collateral]
- Rate: [X]% cash + [X]% PIK = [X]% total coupon
- Warrants: [X]% of fully diluted equity (exercise price: $[nominal])
- Term: [X] months (bridge to refinancing, asset sale, or equity raise)
- Covenants: [minimum liquidity, milestones for operational turnaround]
- Conversion right: convert to equity at [X]% discount to next round

Option C — Rescue Preferred Equity:
- Amount: $[X]M
- Liquidation preference: [X]x (senior to all common equity)
- Dividend: [X]% PIK (compounding quarterly)
- Conversion: into [X]% of common equity at our option
- Governance: [X] board seats, consent rights on [M&A, debt, equity issuance, budget]
- Redemption: mandatory at Year [X] if not converted
- Anti-dilution: full ratchet (distress context justifies aggressive protection)

For each option, calculate:
1. All-in yield (including OID, fees, PIK, warrants)
2. Downside recovery: if the company liquidates, what do we recover?
   Liquidation analysis: asset values at FLV → priority of claims → our recovery
3. Base case return: company stabilizes, we exit at par + accrued + warrant value
4. Upside case: company fully recovers, warrants/conversion worth $[X]M
5. Probability-weighted IRR: [X]% x downside + [X]% x base + [X]% x upside = [X]%
```

---

## 2. Distressed-for-Control

### Credit Bid and Plan Sponsor Analysis

```
Evaluate a distressed-for-control opportunity in [company name]:

Company in Chapter 11:
- Pre-petition capital structure:
  | Tranche           | Amount  | Rate    | Recovery Est. |
  |--------------------|---------|---------|--------------|
  | DIP facility       | $[X]M  | S+[X]  | 100%         |
  | First lien TL      | $[X]M  | S+[X]  | [X]%         |
  | Second lien notes  | $[X]M  | [X]%   | [X]%         |
  | Unsecured bonds    | $[X]M  | [X]%   | [X]%         |
  | Trade claims       | $[X]M  | —      | [X]%         |
  | Equity             | —      | —      | 0%           |

- Estimated enterprise value (going concern): $[X]M - $[X]M range
- Fulcrum security: [tranche where value breaks] at $[X]M EV

Strategy 1 — Buy fulcrum debt, equitize through plan:
- Purchase [X lien] debt at $[X] cents on the dollar
- Cost basis: $[X]M face x $[X] = $[X]M cash investment
- In plan of reorganization, debt converts to [X]% of reorganized equity
- Reorganized equity value: $[X]M (at [X]x reorganized EBITDA of $[X]M)
- Our share: [X]% x $[X]M = $[X]M
- MOIC: $[X]M / $[X]M = [X]x
- IRR: [X]% (over [X]-month restructuring timeline)

Strategy 2 — Credit bid via Section 363 sale:
- Credit bid: use our $[X]M of first lien debt as currency (no cash required)
- We bid $[X]M (face value of our debt) for the assets
- Competing cash bids expected at $[X]M - $[X]M
- If we win: acquire assets free and clear of liens and claims
- Post-acquisition investment needed: $[X]M (working capital, capex, key employee retention)
- Total invested: $[X]M (purchase price in debt + cash infusion)
- Exit EBITDA: $[X]M (post-turnaround, Year 3)
- Exit multiple: [X]x → exit value: $[X]M
- MOIC: [X]x, IRR: [X]%

Strategy 3 — Plan sponsor:
- Provide $[X]M of new equity capital as plan sponsor
- Negotiate plan terms: new equity owns [X]% of reorganized company
- Existing equity wiped out, unsecured creditors receive [warrants / small equity / cash]
- Management incentive plan: [X]% of new equity for management
- Exit financing: $[X]M new term loan at [X]x leverage
- Our equity: $[X]M for [X]% of reorganized equity value of $[X]M

Key execution risks:
1. Enterprise valuation dispute: if value is higher than our estimate, recovery to junior
   classes increases and our share of reorganized equity decreases
2. Competing plans: other creditor groups may propose alternative plans
3. Holdout risk: dissenting creditor classes can delay or block plan confirmation
4. Operational risk: the business is in distress for a reason — can management execute?
5. Timeline risk: Chapter 11 takes [X] months; each month of delay erodes IRR
6. Professional fees: legal, financial advisor, and operational consultant costs of $[X]M
```

---

## 3. Structured Equity Solutions

### Preferred Equity and Convertible Note Structuring

```
Structure a non-traditional capital solution for [company situation]:

Situation: [describe — e.g., founder needs liquidity without full sale, company needs growth
capital but doesn't want dilution at current valuation, bridge to IPO, pension buyout, etc.]

Company profile:
- Revenue: $[X]M
- EBITDA: $[X]M
- Current valuation range: $[X]M - $[X]M
- Capital needed: $[X]M
- Purpose: [growth / acquisition / shareholder liquidity / balance sheet]

Structure 1 — Preferred equity with PIK:
- Investment: $[X]M
- Instrument: senior preferred equity
- Liquidation preference: [X]x ($[X]M returned before common gets anything)
- Dividend: [X]% PIK (compounding, no cash drain during growth phase)
- Accrued value at Year 5: $[X]M x (1 + [X]%)^5 = $[X]M
- Participation: [participating / non-participating / capped at X]x
  - Non-participating: we get the greater of preference OR equity conversion value
  - Participating: we get preference PLUS pro-rata common equity share
  - Capped: participating up to [X]x total return, then common only
- Conversion: into [X]% of common equity at our option
- Put right: force redemption at Year [X] at preference value + accrued PIK

Structure 2 — Convertible note:
- Principal: $[X]M
- Coupon: [X]% cash + [X]% PIK
- Maturity: [X] years
- Conversion price: $[X] per share ([X]% premium to current valuation)
- Conversion ratio: [X] shares per $1,000 principal
- Mandatory conversion trigger: IPO at > $[X]M valuation
- Change of control put: 101% of par + accrued
- Anti-dilution: broad-based weighted average

Structure 3 — Revenue-based financing:
- Investment: $[X]M
- Repayment: [X]% of monthly revenue until [X]x invested capital returned
- Cap: repayment capped at [X]x over [X] years
- Revenue range: if revenue is $[X]M-$[X]M/year, annual repayment = $[X]M-$[X]M
- IRR sensitivity: faster growth → faster repayment → higher IRR for investor
- No equity dilution, no board seats, no valuation negotiation

For each structure, model:
| Scenario | Exit Value | Structure 1 Return | Structure 2 Return | Structure 3 Return |
|----------|-----------|-------------------|-------------------|-------------------|
| Bear     | $[X]M    | [X]x MOIC, [X]% IRR | ...              | ...              |
| Base     | $[X]M    | [X]x MOIC, [X]% IRR | ...              | ...              |
| Bull     | $[X]M    | [X]x MOIC, [X]% IRR | ...              | ...              |

Choose the structure based on:
- Company preference (dilution vs. cash burden vs. governance)
- Our risk tolerance (downside protection vs. upside participation)
- Tax efficiency for both parties
- Complexity and enforceability
```

---

## 4. Opportunistic Real Assets

### Distressed Real Estate and NPL Portfolios

```
Evaluate an opportunistic acquisition of [distressed real estate / NPL portfolio]:

Opportunity A — Distressed property acquisition:
- Property: [type, location, size]
- Distress cause: [foreclosure / failed development / overleveraged owner / vacancy]
- Current condition: [X]% occupied, deferred maintenance of $[X]M
- Lender asking price: $[X]M ([X]% of original loan balance)
- Implied cap rate on current NOI: [X]% (distressed, not stabilized)
- Comparable stabilized properties trade at [X]% cap rate

Turnaround plan:
1. Acquire at $[X]M
2. Invest $[X]M in renovation and lease-up
3. Lease-up timeline: [X] months to reach [X]% occupancy
4. Stabilized NOI: $[X]M
5. Stabilized value: $[X]M / [X]% cap rate = $[X]M
6. Total cost basis: $[X]M (acquisition + renovation + carry costs)
7. Profit on cost: ($[X]M - $[X]M) / $[X]M = [X]%
8. Equity IRR (levered): [X]% over [X]-year hold

Opportunity B — Non-performing loan portfolio:
- Seller: [bank / government entity / distressed fund]
- Portfolio: [X] loans, aggregate unpaid principal balance (UPB): $[X]M
- Collateral: [real estate / corporate / consumer / mixed]
- Average loan age: [X] years
- Delinquency status: [X]% 90+ days, [X]% in foreclosure, [X]% REO
- Asking price: $[X]M ([X]% of UPB → [X] cents on the dollar)

Resolution strategy:
1. **Loan modification / restructuring**: [X]% of portfolio (by UPB)
   - Extend term, reduce rate, partial principal forgiveness
   - Expected recovery: [X]% of UPB over [X] years
2. **Foreclosure and asset sale**: [X]% of portfolio
   - Foreclose, take ownership, stabilize, sell
   - Expected recovery: [X]% of UPB over [X] years
3. **Note sale**: [X]% of portfolio (sell sub-performing loans to other buyers)
   - Expected recovery: [X]% of UPB within [X] months
4. **Write-off / litigation**: [X]% of portfolio (uncollectable)
   - Expected recovery: [X]% of UPB

Blended portfolio analysis:
- Weighted average expected recovery: [X]% of UPB = $[X]M
- Purchase price: $[X]M
- Gross profit: $[X]M
- MOIC: [X]x
- IRR: [X]% (depends heavily on resolution timeline)
- Servicing cost: $[X]M/year (special servicer, legal, property management for REO)
- Net IRR: [X]%

Key risks:
- Resolution timeline longer than expected (IRR killer)
- Collateral values decline further
- Legal/regulatory obstacles to foreclosure in [jurisdiction]
- Borrower bankruptcy filings delay collection
```

---

## 5. Cross-Asset Arbitrage

### Regulatory Capital, Insurance-Linked, and Alternative Yield

```
Evaluate a cross-asset special situations opportunity:

Opportunity A — Regulatory capital trade:
- Bank needs to shed $[X]M of risk-weighted assets for capital ratio compliance
- Synthetic risk transfer: bank buys credit protection from us on [portfolio type]
- We provide $[X]M of funded protection (first-loss or mezzanine tranche)
- Premium: [X]% per year ([X]bps of notional)
- Attachment point: [X]% (losses below this are retained by bank)
- Detachment point: [X]% (losses above this are absorbed by senior tranche / bank)
- Expected loss in our tranche: [X]% per year
- Net yield: premium - expected loss = [X]% per year
- Tenor: [X] years
- Key risk: correlation — systemic event causes losses to exceed attachment point rapidly

Opportunity B — Litigation finance:
- Case: [describe — patent, commercial dispute, class action, arbitration]
- Jurisdiction: [X]
- Law firm assessment of merits: [strong / moderate / speculative]
- Expected damages if plaintiff wins: $[X]M
- Probability of favorable outcome: [X]%
- Expected timeline to resolution: [X] years
- Our investment: $[X]M (fund legal costs, plaintiff's operating expenses)
- Return structure: [X]x of invested capital from first proceeds, then [X]% of remaining
- Expected return by scenario:
  Win (full damages): $[X]M → [X]x MOIC, [X]% IRR
  Settlement ([X]% of damages): $[X]M → [X]x MOIC, [X]% IRR
  Loss: $0 → 0x MOIC (total loss)
- Probability-weighted return: [X]% x $[X]M + [X]% x $[X]M + [X]% x $0 = $[X]M
  Probability-weighted MOIC: [X]x

Opportunity C — Royalty stream acquisition:
- Asset: [pharmaceutical / music / mineral / technology] royalty
- Current annual royalty income: $[X]M
- Remaining royalty term: [X] years (or perpetual)
- Growth rate: [X]% per year (or declining at [X]%)
- Asking price: $[X]M
- Implied yield: $[X]M / $[X]M = [X]%
- DCF valuation at [X]% discount rate: $[X]M
- Key risk: [patent cliff, streaming platform changes, commodity price, technology obsolescence]
- Upside: [pipeline drugs, catalog appreciation, exploration success]

Portfolio construction across special situations:
- Target allocation: [X]% rescue/DIP, [X]% distressed-for-control, [X]% structured equity,
  [X]% real assets, [X]% cross-asset
- Correlation between strategies: [low — this is the diversification benefit]
- Portfolio expected return: [X]% gross IRR
- Expected loss rate: [X]% annualized
- Target net-to-LP IRR: [X]%
```

---

## Mathematical Frameworks

**Waterfall Analysis (Priority of Claims)**:

```
In bankruptcy, claims are paid in strict priority:

1. Super-priority (DIP lender, post-petition administrative claims)
2. Secured creditors (up to value of collateral)
3. Priority claims (wages, taxes, customer deposits)
4. General unsecured creditors (bonds, trade payables, rejection damages)
5. Subordinated claims (if contractually subordinated)
6. Preferred equity
7. Common equity

Recovery analysis:
  Enterprise value: $[X]M
  - Super-priority claims: ($[X]M) → 100% recovery
  Remaining: $[X]M
  - Secured claims: ($[X]M) → [X]% recovery (if remaining < claims, haircut)
  Remaining: $[X]M
  - Unsecured claims: ($[X]M) → [X]% recovery
  ...and so on until value is exhausted

The "fulcrum security" is the tranche where recovery transitions from full to partial.
Buying the fulcrum security at the right price is the classic distressed playbook.
```

**Blended Return Calculation**:

```
For investments with multiple return components (coupon, PIK, warrants, equity kicker):

All-in IRR captures all cash flows:
  Year 0: -Investment
  Years 1-n: +Cash coupon (if any)
  Year n: +PIK accrual + Principal return + Warrant value (or conversion value)

Blended yield = Cash yield + PIK yield + OID accretion + Equity kicker annualized value

For warrant/kicker valuation:
  Warrants for [X]% of equity, exercise price $[nominal]
  Equity value at exit: $[X]M
  Warrant value = [X]% x $[X]M - exercise cost = $[X]M
  Annualized warrant contribution to IRR ≈ Warrant value / Investment / Hold period
```

**Risk-Adjusted IRR Framework**:

```
Probability-weighted return:
  E[Return] = Σ (Probability_i x Return_i)

For special situations with discrete outcomes:
  Scenario 1: Full recovery / plan confirmation → [X]% probability → [X]x MOIC
  Scenario 2: Partial recovery / settlement → [X]% probability → [X]x MOIC
  Scenario 3: Liquidation / total loss → [X]% probability → [X]x MOIC

  E[MOIC] = p1 x MOIC1 + p2 x MOIC2 + p3 x MOIC3

Risk-adjusted IRR:
  Solve for the IRR of probability-weighted cash flows
  Or compute certainty-equivalent: discount expected cash flows at risk-free rate + risk premium

Kelly criterion for position sizing:
  f* = (p x b - q) / b
  Where: p = probability of win, q = 1-p, b = ratio of win to loss
  Maximum position = f* x portfolio (in practice, use fraction of Kelly for safety)
```

**Distressed Valuation Anchors**:

```
Distressed companies are valued using:

1. Going-concern DCF (if restructuring maintains the business):
   Use normalized EBITDA x appropriate multiple for a healthy company in the sector
   Typical range: 4-7x for industrial, 6-10x for asset-light, adjusted for size and quality

2. Liquidation value (if business is shut down):
   Orderly liquidation: sell assets over 6-12 months at 60-80% of book value
   Forced liquidation: sell assets in 30-90 days at 30-50% of book value
   Liquidation value sets the floor for any restructuring negotiation

3. Comparable transaction multiples for distressed M&A:
   Distressed transactions typically clear at 30-60% discount to healthy-company multiples
   Premium for assets with competitive moats, customer relationships, IP, or contracts

4. Break-up value:
   Sum of parts if individual divisions/assets are sold separately
   Break-up value > going-concern value → liquidation is value-maximizing
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Core PE frameworks, LBO math (relevant for distressed-for-control)
- [`buyouts.md`](buyouts.md) — Operational turnaround post-acquisition, exit preparation
- [`private-credit.md`](private-credit.md) — Credit underwriting, covenant design (restructuring context)
- [`real-estate.md`](real-estate.md) — Real estate valuation (for distressed property and NPL analysis)
- [`infrastructure.md`](infrastructure.md) — Project finance (for distressed infrastructure assets)
