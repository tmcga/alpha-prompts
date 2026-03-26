# Private Credit

Prompt templates for direct lending and private credit investing, covering credit underwriting, loan structuring, covenant design, portfolio monitoring, and yield analysis.

## Role Context

```
You are a managing director at a private credit fund ($8B AUM) providing senior secured,
unitranche, and second lien financing to middle-market companies with $15M-$150M EBITDA.
You underwrite credit through the lens of downside protection: your upside is capped at
the coupon, so every deal must survive the stress case. You focus on cash flow durability,
asset coverage, covenant tightness, and structural protections. You think in terms of
yield-to-worst, expected loss, and portfolio-level default assumptions. You know that in
private credit, you eat like a bird (earn spread) and defecate like an elephant (absorb
losses) — so the margin of safety must be substantial. Your fund targets 8-12% net returns
with minimal principal loss.
```

For foundational PE frameworks (relevant for evaluating sponsor-backed borrowers), see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below focus on credit-specific underwriting, structuring, and monitoring.

---

## 1. Credit Underwriting

### Cash Flow Lending Analysis

```
Underwrite a cash flow loan to [borrower name], a sponsor-backed [industry] company:

Borrower profile:
- Sponsor: [PE firm name], fund vintage [year]
- Acquisition price: [X]x EBITDA
- Revenue: $[X]M
- Reported EBITDA: $[X]M
- Seller-adjusted EBITDA: $[X]M (includes run-rate adjustments)
- Our adjusted EBITDA: $[X]M (after haircuts to questionable add-backs)
- EBITDA margin: [X]%
- Revenue cyclicality: [low / moderate / high]
- Customer concentration: top customer [X]% of revenue

Proposed financing:
- Senior secured term loan: $[X]M ([X]x our adjusted EBITDA)
- Revolver: $[X]M
- Total leverage: [X]x

Credit analysis framework:

1. **EBITDA quality and adjustments**:
   Reported EBITDA: $[X]M
   - Less: run-rate revenue adjustments we don't credit: ($[X]M)
   - Less: recurring "non-recurring" costs added back: ($[X]M)
   - Less: SBC add-back reversal (it's a real cost): ($[X]M)
   - Plus: below-market management contract savings: $[X]M
   Our base case EBITDA: $[X]M
   Haircut to seller's number: [X]% (typical acceptable range: 5-15%)

2. **Free cash flow available for debt service (FCCR)**:
   EBITDA: $[X]M
   - Cash interest expense: ($[X]M)
   - Cash taxes: ($[X]M)
   - Maintenance capex: ($[X]M)
   - Working capital needs: ($[X]M)
   = Free cash flow: $[X]M
   FCCR = FCF / Total Debt Service (principal + interest) = [X]x
   Minimum acceptable FCCR: 1.2x (below 1.0x = the company cannot service its debt)

3. **Leverage analysis**:
   Total debt / EBITDA: [X]x
   Senior secured / EBITDA: [X]x
   Net debt / EBITDA: [X]x
   Comparison to industry peers: [X]x average
   Maximum leverage we are comfortable with: [X]x (based on cash flow stability)

4. **Stress testing**:
   Revenue decline scenario: -[X]% revenue → EBITDA of $[X]M → leverage of [X]x
   At what EBITDA level does FCCR breach 1.0x? $[X]M (implies [X]% EBITDA decline)
   Probability of breaching FCCR covenant: [low / moderate / elevated]
   Historical peak-to-trough EBITDA decline for this industry: [X]%
   Does the company survive its industry's worst historical downturn? [yes / no]

5. **Collateral and recovery analysis**:
   Enterprise value at [X]x distressed EBITDA ($[X]M): $[X]M
   Less: super-priority claims (DIP, admin): ($[X]M)
   Available for our tranche: $[X]M
   Recovery on our $[X]M loan: [X]% → [X] cents on the dollar
   Even in distress, we recover [above / below] par
```

### Asset-Based Lending Assessment

```
Evaluate an asset-based lending facility for [borrower]:

Borrower profile:
- Industry: [manufacturing / distribution / retail]
- Revenue: $[X]M
- EBITDA: $[X]M (cash flow may be weak or volatile)
- Why ABL vs. cash flow: [limited EBITDA, cyclical business, turnaround, asset-rich]

Collateral analysis:

Accounts receivable:
- Gross A/R: $[X]M
- Less: ineligible (> 90 days past due, concentration limits, intercompany, foreign): ($[X]M)
- Eligible A/R: $[X]M
- Advance rate: [X]% (typically 80-85%)
- A/R borrowing base: $[X]M

Inventory:
- Gross inventory: $[X]M (raw materials $[X]M, WIP $[X]M, finished goods $[X]M)
- Less: ineligible (slow-moving, obsolete, perishable, in-transit): ($[X]M)
- Eligible inventory: $[X]M
- Advance rate: [X]% (typically 50-65% of NOLV for finished goods, less for WIP/raw)
- Inventory borrowing base: $[X]M

Fixed assets (equipment, real estate):
- Appraised value (FLV / OLV): $[X]M
- Advance rate: [X]% (typically 75-85% of NOLV)
- Fixed asset borrowing base: $[X]M

Total borrowing base: $[X]M
Facility size (capped at): $[X]M
Excess availability at closing: $[X]M

Key structural protections:
- Dominion trigger: if availability falls below $[X]M, cash dominion kicks in
- Borrowing base certificate: [monthly / weekly] reporting
- Field exam frequency: [annual / semi-annual / triggered by availability threshold]
- Springing fixed charge coverage ratio at [X]x when availability < $[X]M
```

---

## 2. Loan Structuring

### Unitranche Term Sheet

```
Structure a unitranche facility for [borrower] in connection with [sponsor]'s acquisition:

Transaction:
- Enterprise value: $[X]M ([X]x EBITDA)
- Sponsor equity: $[X]M
- Management rollover: $[X]M
- Total debt required: $[X]M

Proposed unitranche terms:
- Facility size: $[X]M term loan + $[X]M revolver
- Leverage: [X]x total ([X]x through term loan, revolver undrawn at close)
- Rate: SOFR + [X]bps (floor: [X]bps)
- OID: [X]% ([X] points of upfront discount)
- Maturity: [X] years (bullet / amortization schedule)
- Amortization: [X]% per annum (quarterly payments)
- Call protection: [X]% in Year 1, [X]% in Year 2, par thereafter (non-call period: [X] months)
- SOFR floor: [X]bps

Delayed draw term loan (DDTL):
- Commitment: $[X]M for acquisitions within [X] months of close
- Ticking fee: [X]bps on undrawn amount
- Same pricing and terms as initial term loan
- Leverage test for draws: total leverage ≤ [X]x pro forma for acquisition

Incremental facility:
- Permitted incremental debt: $[X]M or [X]x incremental leverage
- MFN sunset: [X] months (new debt priced within [X]bps of existing)
- Same collateral and guarantee package

Agreement on Agreements (AoA) — first lien / last out split (if applicable):
- First-out: $[X]M at SOFR + [X]bps (lower risk, lower spread)
- Last-out: $[X]M at SOFR + [X]bps (higher risk, higher spread)
- Blended rate to borrower: SOFR + [X]bps
- First-out lender controls remedies until repaid in full
```

---

## 3. Covenant Design

### Financial Covenant Package

```
Design the financial covenant package for a $[X]M senior secured loan to [borrower]:

Borrower EBITDA: $[X]M
Total leverage at close: [X]x
FCCR at close: [X]x

1. **Total net leverage covenant**:
   Maximum total net debt / LTM EBITDA:
   - Closing: [X]x
   - Q4 Year 1: [X]x (step-down of [X]x)
   - Q4 Year 2: [X]x
   - Q4 Year 3 and thereafter: [X]x
   Testing frequency: quarterly, based on LTM EBITDA
   Cushion at close: [X]% below covenant level
   (Rule of thumb: 20-30% cushion provides adequate early warning)

2. **Fixed charge coverage ratio (FCCR)**:
   Minimum (EBITDA - Capex - Taxes) / (Interest + Scheduled Principal) ≥ [X]x
   Testing: quarterly, LTM basis
   Cushion at close: [X]%

3. **EBITDA definition** (critical — the most negotiated term):
   Starting point: net income + interest + taxes + D&A
   Permitted add-backs:
   - Non-cash charges (SBC, write-downs): [capped at $X or X% of EBITDA]
   - Transaction costs and one-time integration costs: [capped at $X]
   - Run-rate cost savings from completed actions: [capped at X% of EBITDA,
     must be achieved within 18 months]
   - Pro forma EBITDA for acquisitions: [permitted for LTM contribution]
   TOTAL add-back cap: [X]% of unadjusted EBITDA or $[X]M
   (Fight hard on this — loose EBITDA definitions mask deterioration)

4. **Restricted payments covenant**:
   No dividends or distributions unless:
   - Pro forma leverage ≤ [X]x (inside leverage covenant by [X] turn)
   - No default or event of default
   - Builder basket: 50% of cumulative excess cash flow
   - Annual limit: $[X]M

5. **Capital expenditure covenant**:
   Maximum annual capex: $[X]M (maintenance) + $[X]M (growth, with carryforward)
   Unused growth capex carries forward [X] year(s)

6. **Equity cure rights**:
   Sponsor can inject equity to cure covenant breach
   - Maximum [X] cures during loan life
   - No more than [X] consecutive quarters
   - Cure amount: minimum needed to bring back into compliance
   - Cure equity counts as EBITDA (or reduces net debt) for testing purposes
```

---

## 4. Portfolio Monitoring

### Watch List and Early Warning System

```
Design a portfolio monitoring framework for a private credit fund with [X] positions:

Tier 1 — Green (performing as expected):
- Leverage within [X]x of covenant
- FCCR > [X]x
- Revenue and EBITDA in line with or above underwriting case
- Financial reporting received on time
- No material adverse changes
- Action: standard quarterly review

Tier 2 — Yellow (watch list):
Trigger criteria (any one triggers escalation):
- Leverage within [X]x of covenant (approaching breach)
- FCCR between [X]x and [X]x
- Revenue or EBITDA [X]%+ below budget for [X] consecutive quarters
- Financial reporting delayed by more than [X] days
- Key management departure
- Loss of material customer (> [X]% of revenue)
- Sponsor equity cure exercised
- Action: monthly review, direct management engagement, sponsor dialogue

Tier 3 — Orange (heightened concern):
Trigger criteria:
- Covenant breach (even if cured)
- [X] consecutive quarters of EBITDA decline
- Liquidity concern: revolver draws > [X]% of commitment
- Industry-wide stress event
- Sponsor disengagement signals
- Action: weekly monitoring, amendment/waiver negotiation, independent advisors retained

Tier 4 — Red (restructuring):
Trigger criteria:
- Payment default (interest or principal)
- Breach of financial or non-financial covenants with no cure path
- Going concern qualification from auditors
- Bankruptcy filing or threat
- Action: restructuring workstream activated, engage restructuring counsel,
  evaluate DIP/exit lending, recovery analysis, credit bid evaluation

For each Tier 2+ position, prepare:
1. Situation summary: what happened and why
2. Current financial snapshot: revenue, EBITDA, leverage, liquidity, covenant headroom
3. Recovery analysis: enterprise value at [X]x distressed multiple → recovery [X]%
4. Sponsor assessment: will they support with equity cure / incremental capital?
5. Recommended action: amend and extend / waive / restructure / sell position / litigate
```

---

## 5. Yield Analysis

### All-In Yield Calculation

```
Calculate the all-in yield for a proposed private credit investment:

Loan terms:
- Commitment: $[X]M
- Funded amount at close: $[X]M
- Base rate: SOFR ([X]%)
- Spread: +[X]bps
- SOFR floor: [X]bps
- OID: [X]% (upfront fee, recognized over life)
- Commitment fee on undrawn: [X]bps
- Upfront arrangement fee: [X]%
- Amortization: [X]% per year
- Expected hold period: [X] years (maturity: [X] years)
- Call protection: [X]% in Year 1, [X]% in Year 2

Yield components:

1. **Current cash yield**:
   (SOFR + Spread) on funded balance = [X]%
   If SOFR < floor: effective rate = Floor + Spread = [X]%
   Current yield: [X]%

2. **OID amortization** (accretion to yield):
   OID: [X]% over [X] year expected life
   Annualized OID yield: [X]% / [X] years = [X]% per year

3. **Upfront fee** (amortized):
   [X]% / [X] year expected life = [X]% per year

4. **Commitment fee income**:
   Undrawn amount ($[X]M) x [X]bps = $[X] per year
   As % of funded amount: [X]%

5. **Call protection value** (if called early):
   If prepaid in Year 1: additional [X]% = [X]% annualized uplift
   If prepaid in Year 2: additional [X]% = [X]% annualized uplift
   Probability-weighted prepayment benefit: [X]%

Gross all-in yield:
   Cash yield: [X]%
   + OID: [X]%
   + Upfront fee: [X]%
   + Commitment fees: [X]%
   + Expected prepayment benefit: [X]%
   = Gross yield: [X]%

Less: expected credit losses:
   Probability of default (annual): [X]%
   Loss given default: [X]%
   Expected annual loss = PD x LGD = [X]%
   Over [X] year hold: cumulative expected loss = [X]%
   Annualized expected loss: [X]%

Net expected yield: Gross yield - Expected loss = [X]%

Less: fund-level expenses:
   Management fee: [X]% per year
   Fund operating expenses: [X]% per year
   Carried interest (on excess above hurdle): equivalent to ~[X]% annual drag

Net-to-LP yield: [X]%
```

### Expected Loss Framework

```
Build an expected loss model for a private credit portfolio:

Portfolio overview:
- Number of positions: [X]
- Total commitments: $[X]M
- Average position size: $[X]M
- Weighted average leverage: [X]x
- Weighted average spread: SOFR + [X]bps

Expected loss = Probability of Default (PD) x Loss Given Default (LGD) x Exposure at Default (EAD)

1. **Probability of Default (PD)**:
   Historical default rates for middle-market leveraged loans:
   - < 4x leverage: [X]% annual PD
   - 4-5x leverage: [X]% annual PD
   - 5-6x leverage: [X]% annual PD
   - > 6x leverage: [X]% annual PD
   Cycle-adjusted PD: weight historical benign/stress periods
   Portfolio weighted average PD: [X]%

   Cumulative PD over [X]-year hold period:
   Cumulative PD ≈ 1 - (1 - Annual PD)^n = [X]%

2. **Loss Given Default (LGD)**:
   Recovery rates by seniority:
   - First lien senior secured: [X]% recovery (LGD = [X]%)
   - Second lien: [X]% recovery (LGD = [X]%)
   - Unitranche: [X]% recovery (LGD = [X]%)
   - Mezzanine / unsecured: [X]% recovery (LGD = [X]%)
   Portfolio weighted average LGD: [X]%

3. **Exposure at Default (EAD)**:
   Funded exposure: $[X]M
   + Expected revolver draws at default: [X]% of unfunded = $[X]M
   Total EAD: $[X]M

4. **Portfolio expected loss**:
   Annual expected loss = PD x LGD x EAD = [X]% x [X]% x $[X]M = $[X]M
   As % of portfolio: [X]%
   Cumulative expected loss over fund life: [X]%

5. **Stress scenario**:
   Recession: PD increases to [X]%, LGD increases to [X]%
   Stressed annual loss: [X]%
   Stressed cumulative loss over fund life: [X]%
   Can the portfolio absorb stressed losses and still return [X]% net to LPs?

6. **Concentration risk**:
   Largest position: $[X]M ([X]% of portfolio)
   If the largest position defaults with [X]% recovery:
   Loss = $[X]M x (1 - [X]%) = $[X]M
   Impact on portfolio return: -[X]bps annualized
   Diversification benefit: what is the correlation assumption between defaults?
```

---

## Mathematical Frameworks

**Yield to Maturity Components**:

```
All-In Yield = Cash Coupon + OID Accretion + Fee Amortization + Prepayment Benefit
             = (SOFR + Spread) + (OID / Expected Life) + (Fees / Expected Life) + E[Prepay Premium]

For floating rate loans:
  Yield is expressed as spread to SOFR: "SOFR + [X]bps all-in"
  Total return = SOFR path + spread + fees - credit losses
```

**Expected Loss Formula**:

```
Expected Loss = PD x LGD x EAD

Where:
  PD = Probability of Default (annual or cumulative)
  LGD = Loss Given Default = 1 - Recovery Rate
  EAD = Exposure at Default (funded + expected unfunded draws)

Annualized expected loss rate = Annual PD x LGD
Portfolio loss budget = Gross yield - Target net yield - Operating expenses
  If expected loss < loss budget: the portfolio can absorb defaults and hit return targets
```

**Debt Service Coverage**:

```
FCCR = (EBITDA - Capex - Taxes) / (Cash Interest + Mandatory Principal Payments)

Interest Coverage = EBITDA / Cash Interest Expense

Leverage = Total Debt / EBITDA
Net Leverage = (Total Debt - Cash) / EBITDA

Debt Yield = NOI (or EBITDA) / Total Debt
  Debt yield > cost of debt → cash flow covers debt service
  Debt yield is leverage-invariant and preferred by some lenders over LTV for CRE
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Sponsor-backed company analysis, LBO math, due diligence
- [`buyouts.md`](buyouts.md) — LBO financing context (you are structuring the debt for these deals)
- [`real-estate.md`](real-estate.md) — Real estate debt (CMBS, construction lending, DSCR)
- [`special-situations.md`](special-situations.md) — Rescue financing, DIP lending, distressed credit
