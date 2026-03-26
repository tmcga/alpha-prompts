# Restructuring & Distressed Advisory

## Role Context

```
You are a senior restructuring advisor with experience across in-court and out-of-court
processes. You think in terms of liquidity runways, enterprise value preservation, and
recovery waterfalls. You understand Chapter 11 mechanics, inter-creditor dynamics, and
the game theory that drives distressed negotiations. You are equally comfortable advising
debtors (maximizing enterprise value, minimizing dilution of existing equity) and creditors
(maximizing recovery, protecting priority). You are precise with Bankruptcy Code sections,
plan confirmation requirements, and the practical realities of distressed situations where
time pressure and information asymmetry define the outcome.
```

---

## What This Desk Does

Restructuring advisory helps companies in financial distress navigate their options — from out-of-court negotiations that avoid the cost and stigma of bankruptcy to formal Chapter 11 (or equivalent) reorganization processes. The desk advises debtors (the company), secured creditors, unsecured creditors, or equity holders — each with different objectives and leverage. The analytical core is a 13-week cash flow (how long can the company survive?), an enterprise valuation (is there value for each tranche?), and a recovery waterfall (who gets what?). Restructuring is the most adversarial corner of investment banking: every dollar recovered by one stakeholder is a dollar lost by another. The best advisors combine rigorous financial analysis with negotiation strategy and deep knowledge of bankruptcy law.

---

## 1. Liquidity Analysis

### 13-Week Cash Flow Model

```
[Company name] is experiencing financial distress. I need to build a 13-week cash flow
forecast to assess liquidity and determine the timeline for action.

Current liquidity position:
- Cash on hand: $[X]M
- Revolver availability: $[X]M (committed: $[X]M, drawn: $[X]M, letters of credit: $[X]M)
- Minimum operating cash requirement: $[X]M
- Upcoming debt maturities: $[X]M due [date], $[X]M due [date]

Weekly operating data:
- Revenue run-rate: $[X]M/week (trend: [stable / declining at X%/month])
- Cash collections lag: [X] weeks (DSO: [X] days)
- Key weekly disbursements: Payroll $[X]M, Rent $[X]M, Suppliers $[X]M, Other $[X]M
- Critical vendor payments: [list vendors and amounts that cannot be delayed]

Build:

1. **Weekly cash flow model (13 weeks)**:
   - Beginning cash balance
   + Cash receipts (collections on A/R, other inflows)
   - Operating disbursements (payroll, COGS, SG&A, rent, insurance)
   - Non-operating disbursements (debt service, capex, taxes, professional fees)
   = Net cash flow for the week
   = Ending cash balance
   + Available revolver capacity
   = Total liquidity

2. **Liquidity runway analysis**:
   - Weeks until cash reaches minimum operating requirement
   - Weeks until total liquidity (cash + revolver) is exhausted
   - Identify the "liquidity cliff" — the specific week where critical payments cannot be made
   - Liquidity runway = Total available liquidity / Avg weekly cash burn

3. **Sensitivity analysis**:
   - Base case: management projections
   - Stress case: [X]% revenue decline, [X]-week collection slowdown, [X]% vendor acceleration
   - Severe stress: customer attrition + supplier cash-on-delivery demands
   - In each scenario: when does the company run out of money?

4. **Immediate levers to extend runway**:
   - Working capital: accelerate collections, stretch payables (which vendors have leverage?)
   - Capex deferral: which projects can be paused without destroying value?
   - Cost cuts: headcount reduction savings timeline (severance vs. ongoing savings)
   - Asset sales: non-core assets that can be monetized quickly
   - Quantify each lever in weeks of additional runway

5. **DIP financing needs** (if Chapter 11 is likely):
   - New money DIP: $[X]M to fund operations through restructuring
   - Roll-up DIP: convert pre-petition revolver to DIP with priority
   - Adequate protection for existing secured creditors
   - Budget for professional fees (typically $[X]M/month for complex cases)
```

---

## 2. Plan of Reorganization

### Waterfall Analysis and Recovery Rates

```
[Company name] is in Chapter 11 (or evaluating a restructuring). I need to build a
recovery waterfall to determine how value is distributed across the capital structure.

Capital structure (pre-petition):
| Tranche              | Amount    | Rate   | Maturity | Security         |
|----------------------|-----------|--------|----------|------------------|
| DIP Facility         | $[X]M    | [X]%   | [date]   | Super-priority   |
| First Lien TL        | $[X]M    | [X]%   | [date]   | First lien       |
| First Lien Notes     | $[X]M    | [X]%   | [date]   | First lien       |
| Second Lien Notes    | $[X]M    | [X]%   | [date]   | Second lien      |
| Unsecured Notes      | $[X]M    | [X]%   | [date]   | None             |
| Trade Claims         | $[X]M    | —      | —        | None             |
| Subordinated Notes   | $[X]M    | [X]%   | [date]   | None             |
| Preferred Equity     | $[X]M    | —      | —        | —                |
| Common Equity        | —        | —      | —        | —                |

Total claims: $[X]M

Enterprise value estimate: $[X]M (going-concern basis)
Liquidation value estimate: $[X]M

Build the waterfall:

1. **Strict priority waterfall** (absolute priority rule):
   Administrative claims (DIP repayment, professional fees): $[X]M
   → Remaining value: EV - Administrative claims
   First lien secured claims: $[X]M → Recovery: min(100%, Remaining / Claims) = [X]%
   → Remaining after first lien
   Second lien secured claims: $[X]M → Recovery: [X]%
   → Remaining after second lien
   Unsecured claims (notes + trade): $[X]M → Recovery: [X] cents on the dollar
   → Remaining after unsecured
   Subordinated claims: → Recovery: [X]%
   Equity: → Recovery: [X]% (typically 0% unless solvent restructuring)

2. **Fulcrum security identification**:
   - The fulcrum security is the tranche where value "breaks" — partly in the money
   - Fulcrum = first tranche with recovery < 100% (where value is insufficient to fully repay)
   - This tranche typically receives equity in the reorganized company
   - Fulcrum recovery = (Remaining value at that level) / (Fulcrum tranche claims) x 100

3. **Plan of reorganization (illustrative)**:
   - DIP: repaid in full in cash at emergence
   - First lien: [new first lien debt at par / cash / mix]
   - Second lien: [new second lien / equity / combination at X% recovery]
   - Unsecured: [equity + warrants at X% recovery / cash at X cents]
   - Equity: [wiped out / receive warrants with strikes above plan value]

4. **Plan confirmation requirements** (Section 1129):
   - At least one impaired class must vote to accept (2/3 in amount, 1/2 in number)
   - Best interests test: each creditor receives at least as much as in Chapter 7 liquidation
   - Feasibility: the reorganized company can meet its obligations
   - Cramdown (Section 1129(b)): court can confirm over dissenting class if "fair and equitable"
     and "does not discriminate unfairly"
   - Absolute priority rule in cramdown: senior class must be paid in full before junior
     receives anything (subject to "gifting" doctrine limitations)

5. **Sensitivity to enterprise value**:
   Build recovery matrix across EV assumptions:
   | EV Scenario   | 1L Recovery | 2L Recovery | Unsec Recovery | Equity |
   | Low ($[X]M)   | [X]%        | [X]%        | [X]%           | 0%     |
   | Base ($[X]M)  | [X]%        | [X]%        | [X]%           | 0%     |
   | High ($[X]M)  | [X]%        | [X]%        | [X]%           | [X]%   |
```

---

## 3. Distressed Valuation

### Going-Concern vs. Liquidation Analysis

```
I need to value [company name] under both going-concern and liquidation scenarios for
a restructuring analysis.

Company profile:
- Industry: [X]
- Revenue: $[X]M (declining [X]% annually)
- EBITDA (normalized): $[X]M
- EBITDA (current, distressed): $[X]M
- Total assets (book value): $[X]M
- Key assets: [list: real estate, equipment, inventory, IP, contracts, licenses]

Perform:

1. **Going-concern valuation** (reorganized entity):
   - Use normalized EBITDA (post-restructuring cost structure): $[X]M
   - Apply distressed comp multiples: [X]x to [X]x EV/EBITDA
     Distressed multiples are typically 1-3x below healthy industry multiples
   - DCF with restructured projections:
     Higher WACC (reflecting post-restructuring risk): [X]%
     Slower growth assumptions, higher capex needs
   - Reorganized EV = Normalized EBITDA x Selected multiple
   - Subtract: Professional fees, emergence costs, working capital needs

2. **Liquidation analysis (Chapter 7)**:
   - Asset-by-asset recovery estimates:
     Cash and equivalents: 100%
     Accounts receivable: [70-90]% (depends on quality, aging)
     Inventory: [50-80]% (raw materials > WIP > finished goods; perishability matters)
     PP&E: [20-60]% (specialized vs. general purpose)
     Real estate: [appraisal value less selling costs, typically 80-90% of market]
     Intangibles/goodwill: [0-20]% (IP may have value; goodwill = 0 in liquidation)
   - Total liquidation proceeds = Sum of recovery on each asset category
   - Less: Chapter 7 trustee fees (3-5% of proceeds), wind-down costs, priority claims
   - Net distributable value to creditors

3. **Section 363 sale** (going-concern sale in bankruptcy):
   - Sold free and clear of liens, claims, and encumbrances
   - Credit bid: secured creditor can bid up to face value of its claim (Section 363(k))
   - Stalking horse bid: initial bid that sets the floor + bid protections (break-up fee, expense reimbursement)
   - Overbid increments: typically $[X]M minimum overbid
   - Auction dynamics: who are the likely bidders?
   - 363 sale value typically between liquidation and going-concern reorganization value

4. **Going-concern premium**:
   - Premium = Going-concern EV - Liquidation value
   - Represents value of: assembled workforce, customer relationships, contracts, brand
   - If premium is small or negative, liquidation may be the best outcome
   - Break-up analysis: is the company worth more sold in pieces than as a whole?
```

---

## 4. Creditor Negotiation Frameworks

### Inter-Creditor Dynamics and Holdout Analysis

```
I am advising [debtor / first lien creditors / second lien creditors / unsecured
creditors / ad hoc group] in the restructuring of [company name].

Capital structure and claims:
- First lien (held by: [X] institutions, ad hoc group holds [X]%): $[X]M
- Second lien (held by: [X] institutions): $[X]M
- Unsecured bonds (widely held, [X] holders): $[X]M
- Trade creditors (critical vendors: $[X]M, non-critical: $[X]M): $[X]M total
- Estimated enterprise value: $[X]M (going-concern)

Inter-creditor agreement key terms:
- Standstill period: [X] days (second lien cannot enforce during this period)
- Release of liens: first lien can release collateral up to [X]% without second lien consent
- DIP priming: first lien can consent to priming DIP; second lien has junior DIP right

Analyze the negotiation dynamics:

1. **Leverage map** (who has power and why):
   - First lien: control DIP financing, can credit bid in 363 sale
   - Second lien: may have blocking position on plan if impaired class
   - Unsecured: large class, vote counts — can delay/complicate confirmation
   - Equity: no leverage unless solvent or "gifting" is offered to buy votes
   - Management/debtor: controls the exclusivity period (120 days, extendable)

2. **Holdout analysis**:
   - Can any single creditor or group block the plan?
     Blocking position = 1/3+1 in dollar amount of a class (since 2/3 needed to accept)
   - Cost of holdout: additional professional fees, delay, value destruction
   - Holdout premium: how much must be offered to bring holdouts into the deal?
   - Strategic considerations: is it cheaper to cramdown or negotiate?

3. **Negotiation zones** (ZOPA for each tranche):
   - First lien ZOPA: par in cash through 100% equity with take-back debt
   - Second lien ZOPA: [X]% recovery in new debt or equity
   - Unsecured ZOPA: [X] cents on dollar in equity + warrants
   - Where do the zones overlap? That is where the deal gets done.

4. **Game theory dynamics**:
   - Two-party vs. multi-party negotiation complexity
   - First-mover advantage: who proposes the initial restructuring support agreement (RSA)?
   - Death trap provision: incentivize class to vote in favor (better recovery if class accepts)
   - Gifting: senior class "gifts" value to junior class to secure votes (Czyzewski/DBSD doctrine)
   - Make-whole litigation: does the acceleration clause trigger the make-whole premium?

5. **Timeline pressure**:
   - Liquidity runway constrains negotiation time
   - DIP budget milestones (court-imposed deadlines for plan filing)
   - Exclusivity expiration: if debtor doesn't file plan, creditors can file competing plans
   - Estimating total restructuring timeline: pre-petition negotiation [X] months +
     Chapter 11 process [X] months + emergence [X] months
```

---

## 5. Out-of-Court Restructuring

### Amend & Extend, Distressed Exchange, Forbearance

```
[Company name] is exploring out-of-court alternatives to address upcoming maturities
and tight covenants, hoping to avoid a formal bankruptcy filing.

Situation:
- Near-term maturity wall: $[X]M due in [X] months
- Current leverage: [X]x (covenant limit: [X]x, headroom: [X]%)
- Covenant breach expected in Q[X] [year]
- Liquidity: $[X]M (cash + revolver availability)
- Credit facility lenders: [X] banks, lead arranger: [X]
- Bond holders: widely held / concentrated (ad hoc group holds [X]%)

Evaluate out-of-court options:

1. **Amend & extend (A&E)**:
   - Extend maturities by [2-3] years in exchange for: higher spread (+[X]bps),
     tighter covenants, fees ([X]bps consent fee)
   - Covenant relief: reset leverage covenant from [X]x to [X]x with step-down
   - EBITDA definition changes: allow additional add-backs
   - Required consent: typically majority lenders (>50%) for amendments
   - For bond amendments: need indenture trustee and bondholder consent
     (typically >50% for most amendments, >90% for sacred rights: maturity, coupon, principal)

2. **Distressed exchange**:
   - Exchange existing bonds for: new secured bonds (priority upgrade) at a discount
     e.g., $[X] par of unsecured bonds for $[X] par of new secured bonds (X cents recovery)
   - Or: bonds exchanged for equity + new debt
   - Minimum participation threshold: [X]% to proceed
   - Accounting: if exchange terms are "substantially different" (10% cash flow test),
     book gain = Par - Fair value of new instruments
   - Tax: cancellation of debt (COD) income — mitigated if insolvent (Section 108 exclusion)

3. **Forbearance agreement**:
   - Lenders agree not to exercise remedies for a defined period ([30-180] days)
   - In exchange: forbearance fee ([X]bps), enhanced reporting, milestones for permanent fix
   - Ticking fees if milestones are missed
   - Forbearance buys time but does not solve the underlying problem

4. **Comparison framework**:
   | Factor          | A&E            | Distressed Exchange | Chapter 11     |
   |-----------------|----------------|---------------------|----------------|
   | Time to complete| [2-4] months   | [2-6] months        | [6-18] months  |
   | Cost            | Low            | Medium              | High           |
   | Creditor consent| Majority       | High threshold      | Class vote     |
   | Business impact | Minimal        | Moderate (stigma)   | Significant    |
   | Holdout risk    | Low (bank deal)| Medium-High         | Cramdown avail |
   | Covenant relief | Yes            | Yes                 | Yes            |

5. **Prepackaged / pre-arranged bankruptcy** (hybrid):
   - If out-of-court fails, negotiate plan and RSA pre-filing
   - Prepack: all classes vote before filing → emerge in 30-60 days
   - Pre-arranged: key terms agreed, vote solicitation in Chapter 11 → 3-6 months
   - Advantages: speed, certainty, lower cost, less business disruption
   - RSA milestones: filing deadline, plan filing, confirmation hearing dates
```

---

## Mathematical Frameworks

Building on [`../roles/investment-banker.md`](../roles/investment-banker.md):

**Recovery Waterfall**:
- Recovery_i = min(Claims_i, max(0, Distributable value - Sum of senior claims)) / Claims_i
- Distributable value = Enterprise value - Administrative costs - DIP repayment
- Fulcrum security: tranche where cumulative claims exceed distributable value

**Liquidity Metrics**:
- Liquidity runway (weeks) = (Cash + Available revolver) / Weekly net cash burn
- Minimum liquidity = Max(Minimum operating cash, Largest single-week disbursement x 2)
- Cash conversion cycle = DSO + DIO - DPO (in days); stressed CCC = CCC + collection delays

**Distressed Valuation Adjustments**:
- Reorganized EV = Normalized EBITDA x Distressed multiple
  Distressed multiple = Healthy multiple x (1 - Distress discount)
  Typical distress discount: 20-40% depending on operational disruption
- Liquidation recovery by asset: Cash (100%), A/R (70-90%), Inventory (40-80%), PP&E (20-60%), Intangibles (0-20%)

**Plan Value Distribution**:
- Total plan value = New equity value + New debt at par + Cash distributions
- Recovery rate_i = (Value allocated to class_i) / (Allowed claims of class_i) x 100
- Implied EV at emergence = New debt + New equity value
- Equity value to creditors: use reorganized company DCF or comparable multiple

**DIP Sizing**:
- DIP size = Cumulative cash deficit over restructuring period + Adequate protection payments
  + Professional fee reserve + Liquidity cushion (typically 10-15% buffer)

---

## See Also

- [Investment Banker Role — Valuation](../roles/investment-banker.md) — DCF and comparable valuation fundamentals
- [Leveraged Finance](leveraged-finance.md) — credit agreements, covenants, and the structures that lead to distress
- [Mergers & Acquisitions](mergers-and-acquisitions.md) — Section 363 sales, distressed M&A
- [Debt Capital Markets](debt-capital-markets.md) — liability management, exchange offers
- [PE Analyst Role](../roles/pe-analyst.md) — distressed-for-control investing
