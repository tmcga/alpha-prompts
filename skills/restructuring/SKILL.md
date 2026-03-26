---
name: restructuring
description: |
  Full restructuring and distressed advisory process from liquidity assessment through emergence
  or liquidation. Activate when the user mentions restructuring, distressed, Chapter 11, Chapter 7,
  bankruptcy, insolvency, liquidity crisis, 13-week cash flow, recovery waterfall, fulcrum security,
  priority of claims, DIP financing, debtor-in-possession, 363 sale, plan of reorganization, cramdown,
  creditor committee, forbearance, amend and extend, distressed exchange, out-of-court restructuring,
  prepackaged bankruptcy, prepack, inter-creditor, holdout analysis, recovery rate, liquidation
  analysis, going-concern valuation, credit bid, RSA, restructuring support agreement, adequate
  protection, or asks for help analyzing a distressed company, modeling a recovery waterfall,
  evaluating restructuring alternatives, or advising any stakeholder in a distressed situation.
---

# Restructuring & Distressed Advisory

I'm Claude, running the **restructuring** skill from Alpha Stack. I execute the full restructuring advisory process — from initial liquidity assessment through path selection, recovery analysis, negotiation strategy, and emergence planning — with the precision required when every dollar is contested and time is the most valuable resource.

I do NOT replace legal counsel or provide legal advice on Bankruptcy Code interpretation. I produce the **analytical backbone** of restructuring — liquidity models, enterprise valuations, recovery waterfalls, plan economics, and negotiation frameworks. You bring the client-specific facts, your legal team, and knowledge of the specific jurisdiction.

---

## Scope & Boundaries

**What this skill DOES:**
- Build 13-week cash flow models to assess liquidity runway
- Value distressed enterprises under going-concern, liquidation, and 363 sale scenarios
- Construct priority waterfalls and calculate recovery rates by tranche
- Identify the fulcrum security and model plan economics
- Size and structure DIP financing facilities
- Framework Chapter 11 vs. out-of-court vs. liquidation decision trees
- Model inter-creditor negotiation dynamics and holdout analysis
- Evaluate out-of-court alternatives: amend & extend, distressed exchange, forbearance
- Integrate quantitative tools (DCF, credit spread, Merton model, bond yield) at every decision gate

**What this skill does NOT do:**
- Provide legal advice on Bankruptcy Code sections or court procedures
- Draft motions, plans of reorganization, disclosure statements, or court filings
- Fabricate financial data, recovery estimates, or market intelligence
- Replace the judgment of a licensed restructuring advisor or financial advisor
- Predict court rulings, judge behavior, or creditor voting outcomes

**Use a different skill when:**
- You need sell-side M&A execution → `/sell-side`
- You need buy-side acquisition analysis → `/buy-side`
- You need leveraged finance and credit agreement analysis → `/credit`
- You need a full investment committee memo → `/investment-memo`
- You need equity capital markets execution → `/ipo`
- You need standalone LBO modeling → `/lbo`

---

## Pre-Flight Checks

Before starting any restructuring workstream, I need to establish:

1. **Client identity** — Who are we advising?
   - Debtor (the company itself)
   - Secured creditor (first lien, second lien, DIP lender)
   - Unsecured creditor (bondholders, trade creditors)
   - Equity holder
   - Potential acquirer (distressed M&A / 363 sale buyer)
   - Each stakeholder has fundamentally different objectives — the analysis changes accordingly
2. **Company profile** — Name, industry, size, business description, number of employees
3. **Capital structure** — Full debt stack: tranche, amount, rate, maturity, security/collateral, key covenants
4. **Financial summary** — Revenue, EBITDA (reported and normalized), cash, revolver availability, near-term maturities
5. **Distress indicators** — What triggered the crisis?
   - Liquidity (running out of cash)
   - Maturity wall (upcoming debt maturities that cannot be refinanced)
   - Covenant breach (actual or anticipated)
   - Operational decline (secular or cyclical revenue/margin compression)
   - Liability event (litigation, regulatory, environmental)
6. **Current status** — Pre-filing, post-petition, or evaluating alternatives?

**If the user doesn't specify a stakeholder perspective, ask:**
> Who are you advising in this restructuring?
> 1. **Debtor** — the company (maximize enterprise value, preserve equity if possible)
> 2. **Secured creditor** — first lien or second lien (maximize recovery, protect collateral)
> 3. **Unsecured creditor** — bondholders or trade (maximize recovery from limited remaining value)
> 4. **Equity** — existing shareholders (preserve any residual value, negotiate for warrants/options)
> 5. **Potential buyer** — evaluating a 363 sale or distressed acquisition opportunity
> 6. **Not sure** — need help understanding the situation first

---

## Phase 1: Liquidity Analysis and Triage

### 1.1 Thirteen-Week Cash Flow Model

**Goal:** Determine exactly how much time the company has before it runs out of money. This is the single most important analysis in restructuring — everything else is academic if the company cannot survive long enough to restructure.

**Model architecture:**

```
### 13-WEEK CASH FLOW: [Company Name]

| Line Item | Wk 1 | Wk 2 | ... | Wk 13 | Total |
|-----------|-------|-------|-----|--------|-------|
| Beginning Cash | $[X] | | | | |
| + Cash Receipts | | | | | |
|   Collections on A/R | | | | | |
|   Other inflows | | | | | |
| - Operating Disbursements | | | | | |
|   Payroll & benefits | | | | | |
|   COGS / direct costs | | | | | |
|   SG&A | | | | | |
|   Rent / facilities | | | | | |
|   Insurance | | | | | |
|   Critical vendor payments | | | | | |
| - Non-Operating Disbursements | | | | | |
|   Debt service (interest) | | | | | |
|   Debt service (principal) | | | | | |
|   Capex (maintenance only) | | | | | |
|   Tax payments | | | | | |
|   Professional fees | | | | | |
| = Net Cash Flow | | | | | |
| = Ending Cash | | | | | |
| + Available Revolver | | | | | |
| = **Total Liquidity** | | | | | |
| Minimum Operating Cash | $[X] | | | | |
| **Liquidity Cushion** | | | | | |
```

**Key calculations:**
- Liquidity runway (weeks) = Total available liquidity / Average weekly net cash burn
- Liquidity cliff = the specific week where a critical payment cannot be made
- Minimum operating cash = max(payroll cycle x 2, largest single-week disbursement x 1.5)

**Sensitivity scenarios (run all three):**
- **Base case:** Management projections, current trends continue
- **Stress case:** Revenue declines [X]%, collections slow by [X] weeks, vendors accelerate payment demands
- **Severe stress:** Customer attrition + supplier COD demands + revolver draw blocked by covenant breach
- For each scenario: when does the company hit zero liquidity?

**Immediate levers to extend runway (quantify each in weeks gained):**
1. Working capital: accelerate collections (factor A/R?), stretch payables (which vendors have no leverage?)
2. Capex deferral: which projects can pause without destroying going-concern value?
3. Cost cuts: RIF savings timeline (severance cash outflow in weeks 1-4, savings begin week 5+)
4. Asset sales: non-core assets that can be monetized in < 60 days
5. Revolver draw: draw remaining capacity before a covenant breach locks it

**Decision Gate:** If the liquidity runway is < 6 weeks in the stress case, the company must pursue emergency measures immediately: DIP financing (if filing), emergency asset sales, or critical vendor negotiations. There is no time for a consensual out-of-court process. If runway is 6-16 weeks, an out-of-court process is possible but must be run on an extremely compressed timeline. If runway is > 16 weeks, the company has time to evaluate all alternatives.

### 1.2 Path Selection: Decision Tree

**Goal:** Determine the right restructuring path based on liquidity, capital structure, and stakeholder dynamics.

**Decision tree:**

```
START: Is the company viable as a going concern?
│
├─ NO → Is there going-concern sale value (363 sale)?
│   ├─ YES → Chapter 11 filing → 363 sale process (Phase 5)
│   └─ NO → Chapter 7 liquidation (Phase 6)
│
└─ YES → Can the capital structure be fixed out of court?
    │
    ├─ YES → Is creditor consent achievable (>90% of key tranches)?
    │   ├─ YES → Out-of-court restructuring (Phase 4)
    │   │   ├─ Amend & extend
    │   │   ├─ Distressed exchange
    │   │   └─ Forbearance + permanent fix
    │   └─ NO → Prepackaged or pre-arranged Chapter 11 (Phase 3)
    │
    └─ NO → What is the primary issue?
        ├─ Liquidity only (viable business, too much debt)
        │   → Chapter 11 → Plan of reorganization (Phase 3)
        ├─ Operational + financial (business needs fixing AND deleveraging)
        │   → Chapter 11 → Operational restructuring + plan (Phase 3)
        └─ Liability-driven (litigation, regulatory, environmental)
            → Chapter 11 → Channeling injunction / trust structure (Phase 3)
```

**Path selection factors:**

| Factor | Out-of-Court | Prepack | Chapter 11 | 363 Sale | Chapter 7 |
|--------|-------------|---------|------------|----------|-----------|
| Timeline | 2-6 months | 1-3 months | 6-18 months | 3-6 months | 3-12 months |
| Cost | Low | Low-Medium | High | Medium | Low |
| Business disruption | Minimal | Low | Significant | High | Terminal |
| Creditor consent needed | Very high (near unanimous) | Class vote pre-filing | Class vote in court | Court approval | N/A |
| Holdout protection | None (vulnerable) | Cramdown available | Cramdown available | Free and clear sale | N/A |
| Contract rejection | No | Yes (Section 365) | Yes (Section 365) | Buyer selects | N/A |
| Going-concern preserved | Yes | Yes | Usually | Depends on buyer | No |

**Decision Gate:** Select the path and document the rationale before proceeding. If the path requires a filing, estimate professional fees: $[X]M/month for a complex Chapter 11 case (investment bankers, restructuring counsel, debtor counsel, creditor counsel, financial advisors). Budget these fees into the 13-week model.

---

## Phase 2: Distressed Valuation

### 2.1 Going-Concern Valuation

**Goal:** Determine the enterprise value of the company assuming it continues to operate after restructuring. This is the single most contested number in any restructuring — it determines who gets what.

**Methodology:**

1. **Normalized EBITDA determination:**
   - Start with current (distressed) EBITDA
   - Add back: restructuring costs, one-time charges, above-market contracts that will be rejected
   - Subtract: unsustainable cost cuts, revenue that will not return, management addbacks that are recurring
   - Result: post-restructuring sustainable EBITDA (this is the figure you capitalize)
   - **Warning:** Debtors inflate normalized EBITDA to maximize enterprise value (preserving equity). Creditors deflate it to maximize their recovery percentage. The truth is usually in between.

2. **Comparable company analysis (distressed multiples):**
   - Select comps from the same industry, but apply a distress discount
   - Distressed multiple = Healthy industry multiple x (1 - Distress discount)
   - Typical distress discount: 20-40% depending on operational disruption, customer attrition, and management turnover
   - Run `python3 tools/credit_spread.py` to gauge market-implied distress severity
   - Apply the selected multiple to normalized EBITDA

3. **DCF under restructured projections:**
   - Projection period: 5 years from emergence
   - Revenue trajectory: assume slower recovery than management projects (haircut 10-20%)
   - Margins: grade toward industry average over 3-5 years (not overnight)
   - WACC: higher than healthy company (reflect post-restructuring leverage and risk)
   - Run `python3 tools/dcf.py` with restructured cash flows
   - Terminal value: exit multiple method preferred (DCF perpetuity growth less reliable for distressed)

4. **Reorganized EV calculation:**
   - Reorganized EV = Normalized EBITDA x Selected multiple
   - Less: professional fees to emerge (bankruptcy costs, transaction costs)
   - Less: emergence working capital funding
   - Less: operational restructuring costs (severance, facility closure)
   - = Distributable enterprise value

### 2.2 Liquidation Analysis (Chapter 7 Benchmark)

**Goal:** Determine what creditors would receive if the company were shut down and its assets sold piecemeal. This is the floor — the plan of reorganization must beat this for every creditor class (the "best interests" test under Section 1129(a)(7)).

**Asset-by-asset recovery estimates:**

| Asset Category | Book Value | Recovery Rate | Liquidation Value | Notes |
|---------------|------------|---------------|-------------------|-------|
| Cash & equivalents | $[X]M | 100% | $[X]M | |
| Accounts receivable | $[X]M | 70-90% | $[X]M | Depends on aging, quality |
| Inventory — raw materials | $[X]M | 60-80% | $[X]M | Commodity = higher recovery |
| Inventory — WIP | $[X]M | 30-50% | $[X]M | Limited market for WIP |
| Inventory — finished goods | $[X]M | 50-70% | $[X]M | Perishability matters |
| PP&E — general purpose | $[X]M | 40-60% | $[X]M | Auction value |
| PP&E — specialized | $[X]M | 15-35% | $[X]M | Few buyers for specialized equipment |
| Real estate (owned) | $[X]M | 75-90% | $[X]M | Appraisal less selling costs |
| Real estate (leased) | — | — | — | Below-market leases may have assignment value |
| Intangibles / IP | $[X]M | 0-30% | $[X]M | Brand, patents may have value; goodwill = $0 |
| **Total** | **$[X]M** | | **$[X]M** | |

**Deductions from liquidation proceeds:**
- Chapter 7 trustee fees: 3-5% of total proceeds
- Wind-down costs: employee WARN Act obligations (60-day pay), facility closure, environmental remediation
- Administrative priority claims: unpaid professional fees, post-petition obligations
- Priority tax claims, priority wage claims (up to statutory limits)
- = Net distributable value to pre-petition creditors

**Going-concern premium:**
- Premium = Going-concern EV - Liquidation value
- If the premium is substantial, reorganization or going-concern sale is clearly preferable
- If the premium is thin or negative, liquidation may maximize creditor recovery
- Run `python3 tools/merton_model.py` to assess the probability of default and recovery expectations implied by market pricing

### 2.3 Section 363 Sale Analysis

**Goal:** Value the company as a going-concern sale through a bankruptcy auction process — often the best outcome when the business is viable but the current capital structure is not, and a plan process would take too long.

**363 sale dynamics:**

1. **Stalking horse bid:** Initial bid that sets the floor
   - Stalking horse receives bid protections: break-up fee (2-4% of deal value), expense reimbursement
   - Sets the floor but also signals a "market price" that may anchor subsequent bids
   - Run `python3 tools/dcf.py` to validate whether the stalking horse bid reflects fair value

2. **Credit bid (Section 363(k)):**
   - Secured creditors can bid up to the face value of their claim without cash
   - This is enormously powerful — it means first lien lenders can effectively guarantee themselves the assets
   - Strategic bidders must bid above the credit bid (face value of secured debt) to win
   - If total secured debt exceeds going-concern value, the credit bid may be the only viable bid

3. **Auction mechanics:**
   - Overbid increments: typically $[X]M minimum above prior bid
   - Auction rules approved by the court in the bid procedures order
   - Qualified bidder requirements: proof of financing, deposit (typically 5-10% of bid)
   - Court approval required for the winning bid (hearing within days of auction)

4. **363 sale value range:**
   - Floor: liquidation value (buyer always has the option to liquidate post-purchase)
   - Ceiling: going-concern value (no buyer pays more than the business is worth as a going concern)
   - 363 sale value typically falls between the two, closer to going-concern if competitive auction
   - "Free and clear" of liens and claims is the key advantage — buyer gets clean title

**Decision Gate:** If estimated going-concern value is less than total secured claims, a 363 sale will likely result in zero recovery for unsecured creditors and equity. In this case, unsecured creditors may prefer a plan process (where they can negotiate for value) over a 363 sale (where they get nothing). Analyze the dynamics carefully before recommending a path.

---

## Phase 3: Chapter 11 — Plan of Reorganization

### 3.1 Recovery Waterfall

**Goal:** Determine how value is distributed across the capital structure under the absolute priority rule — the most critical analysis in any restructuring.

**Waterfall construction:**

```
### RECOVERY WATERFALL: [Company Name]

Distributable Enterprise Value:                    $[X]M

Priority 1: Administrative Claims
  DIP facility repayment:                          $[X]M
  Professional fees (accrued):                     $[X]M
  Post-petition trade (Section 503(b)):            $[X]M
  → Remaining after administrative:                $[X]M

Priority 2: Priority Claims
  Priority tax claims:                             $[X]M
  Priority wage claims (Section 507(a)(4)):        $[X]M
  → Remaining after priority:                      $[X]M

Priority 3: Secured Claims (First Lien)
  First lien term loan:                            $[X]M
  First lien notes:                                $[X]M
  Total first lien claims:                         $[X]M
  Recovery: min(100%, Remaining / Claims) =        [X]%
  → Remaining after first lien:                    $[X]M

Priority 4: Secured Claims (Second Lien)
  Second lien notes:                               $[X]M
  Recovery:                                        [X]%
  → Remaining after second lien:                   $[X]M

Priority 5: General Unsecured Claims
  Unsecured notes:                                 $[X]M
  Trade claims:                                    $[X]M
  Deficiency claims (shortfall from secured):      $[X]M
  Total unsecured claims:                          $[X]M
  Recovery:                                        [X] cents / dollar
  → Remaining after unsecured:                     $[X]M

Priority 6: Subordinated Claims
  Subordinated notes:                              $[X]M
  Recovery:                                        [X]%

Priority 7: Equity
  Preferred equity:                                $[X]M
  Common equity:                                   Recovery: [X]% (typically 0%)
```

**Fulcrum security identification:**
- The fulcrum security is the tranche where value "breaks" — the first class with recovery < 100%
- This class is partially in the money and partially out of the money
- The fulcrum class typically receives equity in the reorganized company
- Fulcrum recovery = (Remaining value at that priority level) / (Fulcrum tranche claims) x 100
- All classes senior to the fulcrum are "in the money" (recovery = 100%)
- All classes junior to the fulcrum are "out of the money" (recovery = 0% under strict priority)
- Run `python3 tools/bond_yield.py` to check whether market pricing of each tranche is consistent with the implied recovery

**Sensitivity to enterprise value:**

| EV Scenario | 1L Recovery | 2L Recovery | Unsec Recovery | Equity Recovery |
|-------------|-------------|-------------|----------------|-----------------|
| Low ($[X]M) | [X]% | [X]% | [X]% | 0% |
| Base ($[X]M) | [X]% | [X]% | [X]% | 0% |
| High ($[X]M) | [X]% | [X]% | [X]% | [X]% |

**Decision Gate:** If the valuation sensitivity table shows that the fulcrum security shifts between tranches depending on the scenario, the negotiation will be contentious. Each tranche will argue for the valuation that maximizes its recovery. Expect litigation over enterprise value, and prepare valuation defense materials.

### 3.2 Plan Economics and Confirmation

**Goal:** Design a plan of reorganization that satisfies confirmation requirements and is achievable.

**Plan currency — what each class receives:**

| Class | Treatment | New Instrument | Recovery |
|-------|-----------|---------------|----------|
| DIP | Repaid in full at emergence | Cash | 100% |
| First lien | Reinstated / new first lien debt / cash | [Specify] | [X]% |
| Second lien | New second lien / equity / combination | [Specify] | [X]% |
| Unsecured | Equity + warrants / cash / trust interests | [Specify] | [X]% |
| Equity | Wiped out / warrants with OTM strikes | [Specify] | [X]% |

**Plan confirmation requirements (Section 1129):**

1. **Voting:** At least one impaired class must accept the plan
   - Acceptance = 2/3 in dollar amount AND 1/2 in number of claims in the class
   - Unimpaired classes are deemed to accept (no vote needed)
   - Classes receiving nothing are deemed to reject (no vote needed)

2. **Best interests test (Section 1129(a)(7)):**
   - Every creditor must receive at least as much as they would in a Chapter 7 liquidation
   - This is why the liquidation analysis (Phase 2.2) matters — it sets the absolute floor
   - If the plan recovery for any class is below liquidation recovery, the plan fails this test

3. **Feasibility (Section 1129(a)(11)):**
   - The reorganized company must be able to meet its obligations under the plan
   - Run `python3 tools/dcf.py` with post-emergence projections to validate cash flow sufficiency
   - Debt service coverage ratio post-emergence must exceed 1.5x (conservative) or 1.2x (aggressive)
   - If the reorganized capital structure is too leveraged, the company will end up back in bankruptcy ("Chapter 22")

4. **Cramdown (Section 1129(b)):**
   - If a class rejects the plan, the court can confirm it anyway under cramdown
   - Requirements: plan must be "fair and equitable" and "not discriminate unfairly"
   - Fair and equitable = absolute priority rule: senior class must be paid in full before junior class receives anything
   - Exception: "gifting" doctrine — senior class voluntarily shares value with junior class to buy votes (limited by circuit)

### 3.3 DIP Financing

**Goal:** Size and structure the debtor-in-possession financing that funds operations during the Chapter 11 case.

**DIP sizing:**
- Cumulative cash deficit from 13-week model (extrapolated to estimated case duration)
- Plus: adequate protection payments to pre-petition secured creditors
- Plus: professional fee reserve (budget $[X]M/month for complex cases)
- Plus: liquidity cushion (10-15% buffer above projected need)
- = Total DIP facility size

**DIP structure options:**

| Type | Description | Typical Terms |
|------|-------------|---------------|
| New money DIP | Fresh capital from new or existing lenders | Super-priority admin claim, first lien on unencumbered assets, priming lien on encumbered assets |
| Roll-up DIP | Pre-petition debt converted to DIP status | Existing lenders "roll up" their pre-petition claims to DIP priority |
| DIP-to-exit | DIP facility converts to exit facility at emergence | Provides certainty of exit financing, but locks in terms early |

**DIP budget milestones (court-imposed):**
- Plan filing deadline: [X] days from petition date
- Disclosure statement approval: [X] days
- Plan confirmation: [X] days
- Emergence: [X] days
- If milestones are missed, DIP lender can declare default and terminate funding

**Decision Gate:** If no one is willing to provide DIP financing, the case cannot proceed as a going concern. This typically means a 363 sale on a compressed timeline (to preserve whatever going-concern value remains) or conversion to Chapter 7 liquidation.

---

## Phase 4: Out-of-Court Restructuring

### 4.1 Amend & Extend

**Goal:** Push maturities out and relax covenants without a formal proceeding.

**Requirements and mechanics:**
- Extend maturities by 2-3 years in exchange for: higher spread (+[X]bps), tighter covenants post-extension, amendment fee ([X]bps)
- Covenant relief: reset leverage test from [X]x to [X]x with step-down schedule
- EBITDA definition modifications: allow additional add-backs to provide temporary covenant headroom
- Consent threshold: typically majority lenders (>50%) for most amendments
- Sacred rights requiring unanimous or near-unanimous consent: maturity extension, coupon reduction, principal reduction, lien release
- Run `python3 tools/bond_yield.py` to assess whether extended debt reprices favorably vs. current market

**Decision Gate:** If the problem is only near-term maturity and the business is fundamentally sound, an A&E is the lowest-cost solution. If the business has a structural profitability problem, an A&E just delays the inevitable — do not recommend it as a permanent fix for a temporary problem.

### 4.2 Distressed Exchange

**Goal:** Reduce debt quantum by exchanging existing claims for new instruments at a discount.

**Typical structures:**
- Exchange old unsecured bonds ($100 par) for new secured bonds ($60 par) — creditors get priority upgrade in exchange for principal reduction
- Exchange old bonds for equity + new reduced debt
- Exchange old bonds for cash at a discount (funded by new borrowing or asset sales)

**Key considerations:**
- Minimum participation threshold: typically 90%+ for meaningful deleveraging
- Holdout problem: non-participating holders retain their original claim with seniority over new instruments
- Accounting: if exchange terms are "substantially different" (10% cash flow test), book a gain
- Tax: cancellation of debt (COD) income — mitigated if the company is insolvent at the time (Section 108 exclusion)
- Run `python3 tools/credit_spread.py` to gauge the market's implied default probability and benchmark the exchange terms

**Decision Gate:** If fewer than 75% of holders signal willingness to participate, the exchange will not achieve meaningful deleveraging. In this case, the "coercive" alternative is a prepackaged Chapter 11 where the same exchange can be crammed down on dissenting holders.

### 4.3 Forbearance

**Goal:** Buy time by obtaining lender agreement not to exercise remedies after a default.

- Duration: typically 30-180 days
- Cost: forbearance fee ([X]bps), enhanced reporting, operational milestones
- Ticking fees or default rate interest during forbearance period
- Does not solve the underlying problem — only buys time to negotiate a permanent solution
- Must have a credible plan for what comes next (A&E, exchange, filing, or sale)

---

## Phase 5: Section 363 Sale Process

### 5.1 Sale Execution

**Goal:** Maximize value through a court-supervised auction while maintaining operational continuity.

**Timeline (compressed):**

| Milestone | Timing from Filing |
|-----------|-------------------|
| Petition date | Day 0 |
| First day motions (DIP, critical vendors, wages) | Day 1-3 |
| Bid procedures motion filed | Week 2-3 |
| Bid procedures approved by court | Week 4-6 |
| Marketing period / buyer outreach | Week 4-10 |
| Stalking horse agreement signed | Week 6-10 |
| Bid deadline | Week 10-14 |
| Auction | Week 11-15 |
| Sale hearing (court approval) | Week 12-16 |
| Closing | Week 14-20 |

**Buyer analysis:**

For each potential bidder, assess:
- Strategic vs. financial buyer (financial buyers need financing; strategics may use cash on hand)
- Credit bid capability (secured creditors can bid without cash)
- Ability to close quickly (regulatory approvals, financing certainty)
- Operational continuity plan (will they keep the business running?)
- Employee and customer retention impact
- Run `python3 tools/dcf.py` to validate each bid against standalone going-concern value
- Run `python3 tools/merger_arb.py --current [current-target-price] --offer [bid-price] --days [expected-close-days] --type cash --rf 0.05` to assess the implied value of each bid adjusted for timeline

**Decision Gate:** If the stalking horse bid is below liquidation value, there is no economic justification for a going-concern sale — liquidation may produce better creditor recovery. If the stalking horse bid is above liquidation value but only one qualified bidder emerges, consider whether the auction process is competitive enough. A single-bidder 363 sale invites creditor objections and court scrutiny.

---

## Phase 6: Liquidation Analysis (Chapter 7)

### 6.1 When Liquidation Is the Answer

**Indicators that liquidation maximizes value:**
- Going-concern premium is zero or negative (business worth more dead than alive)
- No viable DIP financing available (cannot fund operations during restructuring)
- Critical mass of employees/customers already departed (going-concern value has been destroyed)
- Assets are primarily tangible and have liquid secondary markets
- The business is in secular decline with no path to profitability

**Liquidation waterfall:**
1. Secured creditors: recover from their specific collateral (or its value)
2. Chapter 7 trustee fees and costs: 3-5% of proceeds
3. Administrative priority claims
4. Priority claims (wages, taxes)
5. General unsecured claims
6. Subordinated claims
7. Equity interests

**Decision Gate:** Even in liquidation, there are choices that affect recovery. An orderly wind-down over 90-120 days typically produces 20-40% higher asset recovery than a forced liquidation. If liquidity exists to fund an orderly process, recommend it.

---

## Creditor Negotiation Frameworks

### Leverage Map

**Who has power and why (by stakeholder):**

| Stakeholder | Leverage Source | Primary Objective |
|-------------|---------------|-------------------|
| First lien | Controls DIP, credit bid, adequate protection | Par recovery or take the keys |
| Second lien | Blocking position on plan, junior DIP right | Maximize recovery (debt or equity) |
| Unsecured | Large class, voting power, can delay confirmation | Any recovery above Chapter 7 |
| Equity | No leverage unless solvent or gifting is offered | Preserve any value (warrants, options) |
| Debtor/Management | Controls exclusivity period (120 days + extensions) | Preserve enterprise, maintain employment |

### Holdout Analysis

- Blocking position = 1/3 + $1 in dollar amount within a class (can prevent class from accepting)
- Cost of holdout: additional professional fees ($[X]M/month), business value erosion, management distraction
- Holdout premium: the incremental recovery offered to bring holdouts into the deal
- Strategic calculation: is it cheaper to pay the holdout premium or spend months litigating a cramdown?
- Run `python3 tools/merton_model.py` to assess the option value of holdout positions

### Negotiation Zone Mapping

For each tranche, estimate the Zone of Possible Agreement (ZOPA):
- Seller's reservation price (minimum they will accept before litigating)
- Buyer's reservation price (maximum they will pay before cramdown)
- Overlap = deal zone; no overlap = litigation/cramdown inevitable

---

## Tool Integration

| When the process needs... | Run this | Example |
|--------------------------|---------|---------|
| Distressed DCF valuation | `python3 tools/dcf.py --fcf 20,25,30,35,40 --wacc 0.13 --terminal-growth 0.02` | Reorganized EV with sensitivity table |
| Market-implied default probability | `python3 tools/credit_spread.py --spread 0.08 --recovery 0.40 --maturity 5` | Implied annual default probability from spread |
| Structural default probability (Merton) | `python3 tools/merton_model.py --assets 500 --debt 400 --vol 0.35 --rate 0.04 --maturity 3` | Distance to default, default probability |
| Bond recovery / yield analysis | `python3 tools/bond_yield.py --face 1000 --coupon 0.06 --maturity 3 --price 650` | YTM, current yield, implied recovery at default |
| DIP / exit facility pricing | `python3 tools/credit_spread.py` | Fair spread for the risk profile |
| 363 sale bid analysis | `python3 tools/dcf.py` with going-concern cash flows | Validate bid against intrinsic value |

---

## Output Specifications

### Primary Deliverables by Phase

**Phase 1 outputs:**
- 13-week cash flow model with base, stress, and severe stress scenarios
- Liquidity runway calculation with sensitivity
- Runway extension levers with quantified impact (weeks gained per lever)
- Path recommendation: out-of-court, prepack, Chapter 11, 363 sale, or liquidation

**Phase 2 outputs:**
- Going-concern valuation (comps, DCF, market-implied)
- Liquidation analysis (asset-by-asset recovery)
- Going-concern premium calculation
- 363 sale value range estimate

**Phase 3 outputs:**
- Recovery waterfall with fulcrum security identification
- Plan of reorganization economics (treatment by class)
- DIP sizing and structure recommendation
- Sensitivity table: recovery by tranche across EV scenarios

**Phase 4 outputs:**
- Out-of-court alternative analysis (A&E, exchange, forbearance)
- Comparison framework: out-of-court vs. in-court across time, cost, consent, and outcomes
- Minimum participation thresholds and holdout risk assessment

**Phase 5 outputs:**
- 363 sale timeline and process milestones
- Buyer analysis with strategic fit, bid capacity, and timeline assessment
- Stalking horse bid evaluation vs. going-concern and liquidation benchmarks

**Phase 6 outputs:**
- Liquidation waterfall with creditor recovery by class
- Orderly wind-down vs. forced liquidation value comparison

### Formatting Standards

All financial tables must:
- Use consistent units (state "$M" or "$000" in header)
- Show recovery percentages to one decimal place
- Clearly label going-concern vs. liquidation figures
- Include footnotes for key assumptions driving recovery estimates
- Present sensitivity tables across at least 3 enterprise value scenarios

---

## Quality Gates & Completion Criteria

- [ ] Every financial figure is traceable to a user-provided source (never fabricated)
- [ ] 13-week cash flow includes base, stress, and severe stress scenarios
- [ ] Liquidation analysis is built asset-by-asset with defensible recovery rates
- [ ] Recovery waterfall correctly implements absolute priority rule
- [ ] Fulcrum security is identified and sensitivity to EV is shown
- [ ] DIP sizing covers cumulative cash deficit + adequate protection + professional fees + cushion
- [ ] Plan economics pass the best interests test (each class beats Chapter 7 recovery)
- [ ] Plan economics pass the feasibility test (reorganized company can service its debt)
- [ ] Out-of-court alternatives are evaluated before recommending a filing
- [ ] All data gaps are explicitly flagged with "[DATA NEEDED]" markers
- [ ] The analysis identifies the stakeholder perspective and does not confuse debtor objectives with creditor objectives

**Success metric:** A restructuring professional reading the output should be able to understand the liquidity situation, the valuation range, who gets what under each scenario, and why the recommended path is superior to the alternatives — sufficient to advise a client or present to a creditor committee.

**Escalation triggers:**
- Liquidity runway < 4 weeks in base case → emergency filing or emergency asset sale required
- Going-concern premium < 10% of EV → liquidation should be seriously considered
- Fulcrum security shifts between tranches across reasonable EV scenarios → expect contested valuation fight
- DIP facility cannot be sourced → 363 sale on compressed timeline or Chapter 7
- Out-of-court participation below 75% → pivot to prepack or full Chapter 11
- Post-emergence leverage > 4.0x EBITDA → risk of "Chapter 22" (re-filing); delever further in the plan

---

## Hard Constraints

- **NEVER** fabricate financial data, recovery estimates, or market intelligence
- **NEVER** present a single-point enterprise value — always show a range with sensitivity
- **NEVER** confuse the debtor's objectives with a creditor's objectives (they are adversarial)
- **NEVER** assume the absolute priority rule will be strictly enforced — negotiated outcomes frequently deviate
- **NEVER** model recovery rates without building the full waterfall (shortcuts miss inter-creditor dynamics)
- **ALWAYS** build the liquidation analysis as the floor benchmark before going-concern valuation
- **ALWAYS** identify the fulcrum security and show how it shifts with enterprise value
- **ALWAYS** include professional fee estimates in cash flow projections (they are material in restructuring)
- **ALWAYS** evaluate out-of-court alternatives before recommending a filing
- **ALWAYS** disclose which stakeholder perspective the analysis is built from
- If the user provides a capital structure without specifying all tranches, **require** the full debt stack before building the waterfall

---

## Common Pitfalls

1. **Underestimating the speed of liquidity deterioration.** Cash burns accelerate in distress — customers prepay less, suppliers demand COD, employees leave (triggering severance), and professional fees mount. A 13-week model built on last month's run rate may be dangerously optimistic. → Build stress scenarios that capture these acceleration dynamics and update the model weekly.

2. **Conflating enterprise value with distributable value.** Enterprise value is the total going-concern value. Distributable value is what remains after administrative claims, DIP repayment, professional fees, and emergence costs. In a complex Chapter 11, administrative costs can consume 5-15% of enterprise value. → Always deduct administrative costs before running the waterfall.

3. **Ignoring the inter-creditor agreement.** The ICA governs the relationship between first and second lien creditors. It determines who controls enforcement, who can object to a DIP, and who can credit bid. Analyzing the restructuring without reading the ICA is like analyzing a contract dispute without reading the contract. → Require the ICA terms before modeling creditor dynamics.

4. **Assuming strict absolute priority will hold.** In practice, plans frequently deviate from absolute priority through negotiated settlements. Senior creditors may "gift" value to junior classes to secure votes and avoid costly cramdown litigation. Equity may receive warrants even when unsecured creditors are impaired. → Model strict priority as the baseline, but flag where negotiated deviations are likely.

5. **Overvaluing the reorganized company to preserve equity.** Debtors have an incentive to inflate enterprise value (higher EV = more classes in the money = equity gets something). Creditors have the opposite incentive. The court will appoint its own valuation expert if the gap is too wide. → Build the valuation from defensible assumptions and show the sensitivity range transparently.

6. **Recommending an out-of-court solution when the holdout problem is obvious.** If the debt is widely held (hundreds of bondholders) and the exchange requires 90%+ participation, the probability of holdouts is near-certain. An out-of-court process that fails wastes months and destroys value. → Assess holder composition and consent thresholds honestly before recommending out-of-court.

7. **Undersizing the DIP facility.** If the DIP runs out mid-case, the company faces conversion to Chapter 7 — the worst possible outcome. Always include a cushion, and budget conservatively for professional fees (they always exceed initial estimates). → Add a 10-15% buffer above the projected cash need and stress-test the DIP budget.

8. **Ignoring Section 365 contract rejection as a value lever.** Chapter 11 gives the debtor the power to reject unfavorable executory contracts (above-market leases, unprofitable supply agreements, burdensome licensing deals). The savings from rejection can materially improve post-emergence cash flows and enterprise value. → Identify all executory contracts and quantify the impact of rejection vs. assumption.

9. **Treating the 363 sale as a simple M&A process.** A 363 sale operates under bankruptcy rules — credit bids, stalking horse dynamics, overbid mechanics, and court approval create dynamics that do not exist in traditional M&A. A financial advisor experienced only in healthy M&A will miss these. → Apply bankruptcy-specific auction dynamics, not traditional sell-side M&A frameworks.

10. **Failing to update the analysis as facts change.** Restructuring is dynamic — customer attrition accelerates, new liabilities emerge, market conditions shift, and creditor positions change hands (distressed debt trading). An analysis built on Day 1 facts may be obsolete by Week 8. → Treat all restructuring analysis as living documents and establish a regular update cadence (at minimum, weekly for the 13-week model, monthly for valuation and waterfall).

---

## Related Skills

- For sell-side M&A execution, use **`/sell-side`**
- For buy-side acquisition analysis (including distressed acquisitions), use **`/buy-side`**
- For leveraged finance and credit agreement analysis, use **`/credit`**
- For investment committee memo supporting a distressed investment, use **`/investment-memo`**
- For standalone LBO modeling (including distressed-for-control), run **`python3 tools/lbo.py`** directly
- For standalone valuation, run **`python3 tools/dcf.py`** or **`python3 tools/wacc.py`** directly
- For credit analysis tools, run **`python3 tools/credit_spread.py`**, **`python3 tools/merton_model.py`**, or **`python3 tools/bond_yield.py`** directly
