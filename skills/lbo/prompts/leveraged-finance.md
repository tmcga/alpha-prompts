# Leveraged Finance

## Role Context

```
You are a senior leveraged finance banker specializing in high yield bonds and leveraged
loans. You structure acquisition financings, recapitalizations, and refinancings for
sub-investment-grade borrowers. You think in terms of credit risk, covenant protection,
debt capacity, and capital structure optimization. You are deeply familiar with credit
agreement mechanics, EBITDA definitions and add-backs, and the interplay between
rating agency methodology and investor appetite. You balance the borrower's desire for
flexibility against the lender's need for downside protection.
```

---

## What This Desk Does

Leveraged Finance originates and structures debt financing for companies rated below investment grade — typically in the context of LBOs, acquisitions, recapitalizations, and refinancings. The desk works on both leveraged loans (bank debt, broadly syndicated, and direct lending) and high yield bonds (public or Rule 144A). A core skill is structuring capital structures that maximize proceeds for the borrower while remaining executable in the syndication market. This requires fluency in credit agreement terms, rating agency expectations, and investor base preferences. LevFin bankers sit between the M&A team (which needs committed financing for deals) and the capital markets team (which distributes the paper).

---

## 1. Credit Agreement Analysis

### Covenant Review and EBITDA Definition

```
I am reviewing a credit agreement for [borrower name], a [description] with LTM EBITDA
of $[X]M and total debt of $[X]M ([X]x leverage).

The credit agreement defines "Consolidated EBITDA" with the following add-backs:
- [List specific add-backs, e.g., restructuring charges up to $XM, pro forma synergies
  for acquisitions, stock-based compensation, management fees, cost savings add-backs
  with a cap of X% of EBITDA]

Covenant type: [Maintenance / Incurrence / Springing]

Help me analyze:

1. **EBITDA definition and add-backs**:
   - Categorize each add-back as standard, aggressive, or borrower-favorable
   - Calculate "Reported EBITDA" vs. "Credit Agreement EBITDA" vs. "Cash EBITDA"
     Adjusted EBITDA = Reported EBITDA + Permitted add-backs
     Cash EBITDA = Adjusted EBITDA - SBC - Capitalized items (most conservative)
   - How large is the gap? (>20% gap is a red flag for credit investors)
   - Which add-backs are capped and which are uncapped?

2. **Maintenance vs. incurrence covenants**:
   - Maintenance: tested quarterly regardless of action (e.g., Total leverage < [X]x)
     Violation = technical default, triggers negotiation/waiver
   - Incurrence: tested only when borrower takes a specific action (e.g., new debt, RP)
     Threshold typically set 0.5-1.0x above current leverage
   - Springing: maintenance covenant that activates only if revolver > [X]% drawn
   - What is the current headroom under each covenant?
     Headroom = (Covenant threshold - Actual metric) / Actual metric x 100%

3. **Key provisions to flag**:
   - EBITDA cure rights (equity cure provisions)
   - Restricted payments (dividends, buybacks, distributions to equity)
   - Permitted investments and permitted debt baskets
   - Asset sale mandatory prepayment and excess cash flow sweep
   - J.Crew / Chewy-style trapdoor provisions (unrestricted subsidiary transfers)
   - Incremental facility capacity: how much additional debt can be raised?
     Incremental capacity = Greater of $[X]M and [X]x EBITDA, subject to leverage test
```

### Permitted Baskets and Builder Provisions

```
I need to map the restricted payments, permitted investments, and permitted debt
baskets for [borrower name]'s credit agreement.

Key financial metrics:
- LTM Adjusted EBITDA: $[X]M
- Total net leverage: [X]x
- Interest coverage: [X]x
- Cumulative excess cash flow since closing: $[X]M
- Cumulative retained income since closing: $[X]M

Help me build a capacity analysis:

1. **Restricted payment capacity**:
   - General basket: $[X]M or [X]% of EBITDA (greater of)
   - Builder basket: typically 50% of cumulative consolidated net income (if positive)
     + 100% of new equity contributions (the "Available Amount")
   - Leverage-based capacity: unlimited RPs if total net leverage < [X]x
   - What is the total available capacity today?

2. **Permitted debt capacity**:
   - Ratio debt: additional first lien if secured net leverage < [X]x
   - Fixed dollar baskets by type (e.g., $[X]M general, $[X]M capital leases)
   - Contribution debt: debt incurred with proceeds of equity contributions
   - How does incremental equivalent debt (IED) differ from a standard incremental?

3. **Practical implications**:
   - Can the borrower dividend recap? How much?
   - Can it make a bolt-on acquisition of $[X]M without lender consent?
   - Can it move material IP to an unrestricted subsidiary?
```

---

## 2. Leveraged Loan Structuring

### Capital Structure and Pricing

```
I am structuring leveraged loan financing for [transaction description: e.g., a $2B LBO
of a healthcare services company by a PE sponsor].

Target company:
- LTM EBITDA: $[X]M (Adjusted EBITDA: $[X]M with add-backs)
- LTM Revenue: $[X]M
- Capex: $[X]M, Working capital needs: $[X]M seasonal
- Business characteristics: [cyclicality, recurring revenue %, asset base]

Sponsor equity contribution: $[X]M ([X]% of total sources)

Structure a capital structure with:

1. **Debt tranches**:
   - Revolver: $[X]M, [X]-year maturity, S+[X]bps, [X]% commitment fee
     Sizing: typically 1.0-1.5x working capital needs
   - Term Loan A (if bank market): $[X]M, [X]-year, S+[X]bps, [X]% annual amortization
   - Term Loan B (institutional): $[X]M, [X]-year, S+[X]bps, 1% annual amortization
     OID: [X]% (effective yield = coupon + OID amortization over expected life)
   - Delayed draw term loan (DDTL): $[X]M for future acquisitions, ticking fee [X]bps
   - Second lien or mezzanine (if needed): $[X]M, S+[X]bps or [X]% fixed

2. **Sources & uses**:
   Sources: TLA + TLB + Second lien + Rollover equity + New equity = Total
   Uses: Equity purchase price + Refinance existing debt + Fees + OID + Cash to B/S

3. **Credit metrics at close**:
   - Total leverage: Total debt / Adj. EBITDA = [X]x
   - Senior secured leverage: Senior secured / Adj. EBITDA = [X]x
   - Interest coverage: Adj. EBITDA / Total interest expense = [X]x
   - Fixed charge coverage: (EBITDA - Capex) / (Interest + Mandatory amort) = [X]x
   - Debt / Total capitalization: [X]%

4. **Pricing benchmarks**: What are current market clearing levels for:
   - Single-B vs. BB rated TLBs
   - Average OID and SOFR floors
   - Flex provisions: what should the commitment letter flex look like?

5. **Syndication strategy**: Who are the natural buyers?
   - CLOs (largest buyer of leveraged loans, focus on spread, constraints on CCC)
   - Loan mutual funds and ETFs (need liquidity)
   - Banks (hold revolver and TLA)
```

---

## 3. High Yield Bond Analysis

### Bond Structure and Documentation

```
I am analyzing a high yield bond issuance for [issuer name]:

Proposed terms:
- Size: $[X]M
- Maturity: [X] years
- Coupon: [X]% [fixed / floating / toggle]
- Ranking: [Senior secured / Senior unsecured / Subordinated]
- Registration: [144A / RegS / Registered]
- Rating: [S&P: X / Moody's: X]

Help me analyze:

1. **Call schedule**:
   - Non-call period: [X] years (typically NC2 for 5yr, NC3 for 8yr, NC4 for 10yr)
   - Make-whole period: T+[X]bps (during NC period, redemption at make-whole price)
     Make-whole price = Greater of (par, PV of remaining payments discounted at T+spread)
   - Declining call prices: [par + 1/2 coupon], [par + 1/4 coupon], [par]
   - Equity clawback: up to [35]% at [par + coupon] within [3] years from proceeds of
     equity offerings
   - 10% at [103] annually (10% special redemption provision)

2. **Key indenture provisions**:
   - Change of control: put at [101]% of par
   - Limitation on additional indebtedness (incurrence test: leverage < [X]x)
   - Restricted payments covenant and builder basket
   - Asset sale covenant (reinvestment period, excess proceeds offer)
   - Limitation on liens, limitation on sale-leaseback
   - Merger covenant (successor must assume obligations)

3. **Relative value analysis**:
   - Yield to worst (YTW): min(yield to each call date, yield to maturity)
   - Spread to worst: YTW - interpolated Treasury yield
   - Compare to: same-rated bonds, same-sector bonds, issuer's existing curve
   - Z-spread and OAS for more precise spread measurement
   - Current yield = Annual coupon / Market price
   - YTW vs. current yield vs. YTM — when does each matter?

4. **Recovery analysis** (for distressed scenarios):
   - Enterprise value in stress / Total debt by seniority
   - Waterfall: Admin claims > DIP > First lien > Second lien > Unsecured > Sub
   - Expected recovery rate by position in the capital structure
```

---

## 4. Debt Capacity Analysis

### Leverage and Coverage Framework

```
Assess the debt capacity of [company name] for [purpose: acquisition financing /
recapitalization / refinancing].

Financial profile:
- Revenue: $[X]M, Revenue growth: [X]%
- EBITDA: $[X]M, EBITDA margin: [X]%
- EBITDA volatility (peak-to-trough decline): [X]%
- Capex: $[X]M (maintenance: $[X]M, growth: $[X]M)
- Working capital intensity: [X]% of revenue
- Current debt: $[X]M, Current leverage: [X]x

Determine maximum debt capacity using:

1. **Rating agency methodology**:
   - S&P: Debt/EBITDA, FFO/Debt, EBITDA/Interest for target rating [X]
     FFO = Net income + D&A + Deferred taxes + Other non-cash - WC changes
   - Moody's: Debt/EBITDA, (EBITDA - Capex)/Interest, RCF/Net debt
     Moody's typically adjusts for operating leases and pensions
   - Map company metrics to rating grid: where does it fall?
   - Maximum debt at target rating = EBITDA x Max leverage for that rating

2. **Leverage comparables**:
   - Peer group median leverage by credit rating
   - Industry-specific leverage norms (asset-light vs. asset-heavy)
   - LBO leverage benchmarks by sector (current market: [X]x senior, [X]x total)

3. **Coverage-based capacity**:
   - Minimum interest coverage: [X]x (stress test at higher rates)
     Max interest expense = EBITDA / Min coverage ratio
     Max debt = Max interest expense / Weighted avg cost of debt
   - Fixed charge coverage: (EBITDA - Capex - Taxes) / (Interest + Mandatory amort) > 1.0x

4. **Cash flow-based capacity**:
   - FCF = EBITDA - Cash interest - Cash taxes - Capex - WC changes
   - Debt paydown capacity: cumulative FCF over 5-7 years
   - Leverage trajectory: does the company delever to < [X]x within [X] years?
   - Stress scenario: what happens to coverage if EBITDA drops [20-30]%?

5. **Market capacity** (what the market will clear today):
   - CLO constraints (max single-B exposure, max CCC bucket)
   - Investor fatigue in the sector
   - Recent comparable issuances and clearing levels
```

---

## 5. Covenant Compliance Modeling

### Forecast Covenant Metrics and Headroom

```
[Company name] has the following financial covenants under its credit agreement:

Covenant requirements (tested quarterly on LTM basis):
- Maximum total net leverage: [X]x (stepping down to [X]x by Q[X] [year])
- Minimum interest coverage: [X]x
- Maximum capex: $[X]M per year (with [X]% carryforward if unused)
- Minimum liquidity: $[X]M (cash + revolver availability)

Current financial position:
- LTM EBITDA: $[X]M
- Total debt: $[X]M, Cash: $[X]M
- LTM interest expense: $[X]M
- Revolver: $[X]M committed, $[X]M drawn

Quarterly projections (next 8 quarters):
[Provide quarterly Revenue, EBITDA, Capex, Cash flow projections or state assumptions]

Build a covenant compliance model:

1. **Quarterly covenant calculations**:
   - Net leverage = (Total debt - Cash) / LTM Adjusted EBITDA (rolling 4 quarters)
   - Interest coverage = LTM EBITDA / LTM Cash interest
   - Track each metric vs. covenant threshold each quarter

2. **Headroom analysis**:
   - Headroom (%) = (Covenant limit - Actual) / Actual x 100
   - EBITDA cushion = EBITDA x (1 - Actual leverage / Max leverage)
     "How much can EBITDA decline before covenant breach?"
   - Revenue shortfall threshold: what revenue decline triggers a breach?

3. **Stress scenarios**:
   - Base case: management projections
   - Downside: [X]% revenue decline, margin compression of [X]bps
   - Severe stress: [X]% revenue decline (2008/2020-like scenario)
   - In which quarter does each scenario first breach a covenant?

4. **Cure and remediation options** (if breach is likely):
   - Equity cure: sponsor injects equity counted as EBITDA (limited to [X] times)
   - Covenant waiver or amendment (cost: [X]bps amendment fee + tighter terms)
   - Asset sale to pay down debt and reduce leverage
   - Revolver paydown to stay below springing covenant trigger

5. **Early warning dashboard**: flag when headroom drops below [15]%
```

---

## Mathematical Frameworks

Building on [`../roles/investment-banker.md`](../roles/investment-banker.md):

**Leverage Ratios**:
- Total leverage = Total debt / EBITDA
- Senior secured leverage = First lien debt / EBITDA
- Net leverage = (Total debt - Cash) / EBITDA
- Secured net leverage = (Secured debt - Cash) / EBITDA

**Coverage Ratios**:
- Interest coverage = EBITDA / Cash interest expense
- Fixed charge coverage = (EBITDA - Capex) / (Cash interest + Mandatory amort + Cash taxes)
- Debt service coverage = (EBITDA - Capex - Cash taxes) / (Interest + Scheduled principal)

**Yield Calculations**:
- Current yield = Annual coupon / Clean price
- YTM: solve for y in Price = Sum[C/(1+y)^t] + Par/(1+y)^n
- YTW = min(YTM, YTC_1, YTC_2, ..., YTC_n) where YTC = yield to each call date
- Effective yield with OID: (Par - OID) invested, receive full coupon; solve for yield

**Credit Default Probability**:
- Spread = PD x LGD / (1 - PD), approximately: PD = Spread / LGD
- Cumulative default probability (from spread): 1 - e^(-spread x t / LGD)
- Recovery rate = 1 - LGD

---

## See Also

- [Investment Banker Role — LBO and Capital Structure](../roles/investment-banker.md) — LBO mechanics, optimal capital structure, WACC
- [Mergers & Acquisitions](mergers-and-acquisitions.md) — acquisition financing in the context of M&A processes
- [Debt Capital Markets](debt-capital-markets.md) — investment grade issuance, the other side of the credit spectrum
- [Restructuring](restructuring.md) — what happens when leveraged credits go wrong
- [PE Analyst Role](../roles/pe-analyst.md) — sponsor perspective on leverage and returns
