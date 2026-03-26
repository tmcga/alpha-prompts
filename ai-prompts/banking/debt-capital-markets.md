# Debt Capital Markets

## Role Context

```
You are a senior DCM banker covering investment grade corporate issuers, sovereigns, and
supranational/agency (SSA) borrowers. You advise on benchmark bond issuance, liability
management, and credit rating strategy. You think in terms of credit spreads, new issue
concessions, curve placement, and investor base composition. You understand that IG
issuers prioritize cost of capital, maturity profile optimization, and maintaining
investment grade ratings. You are fluent in swap-adjusted economics, cross-currency
issuance, and ESG-linked financing structures.
```

---

## What This Desk Does

Debt Capital Markets helps investment grade borrowers access the public bond market efficiently. The desk advises on timing (when to issue), structure (fixed vs. floating, tenor, currency, callable features), and pricing (where the bond should land relative to secondary spreads and new issue concessions). DCM also handles liability management — helping issuers optimize their existing debt stack through tender offers, exchange offers, and consent solicitations. The market is enormous: IG corporate issuance exceeds $1.5 trillion annually in USD alone. Unlike leveraged finance where credit risk dominates, IG DCM is a rates and spread product where basis points matter and execution speed is critical. The desk coordinates with syndicate (for pricing and allocation), credit research (for investor positioning), and treasury teams at the issuer.

---

## 1. New Issue Pricing

### Spread Analysis and Curve Placement

```
[Issuer name] (rated [S&P: X / Moody's: X]) is considering a benchmark bond offering.

Issuer profile:
- Sector: [X]
- Revenue: $[X]B, EBITDA: $[X]B
- Total debt: $[X]B, Net leverage: [X]x
- Existing bonds outstanding: [list key maturities and spreads]

Market context:
- IG index spread (CDX IG or iTraxx): [X]bps
- 30-day trend: [tighter/wider by X bps]
- Recent supply: $[X]B issued this week in IG
- Risk sentiment: [risk-on / risk-off / neutral]

Proposed offering:
- Size: $[X]B
- Tenor options: [3yr / 5yr / 7yr / 10yr / 30yr or multi-tranche]
- Currency: [USD / EUR / GBP / multi-currency]

Help me determine pricing:

1. **Secondary spread analysis**:
   - Where do the issuer's existing bonds trade?
   - Interpolated spread at target maturity using issuer's own curve
   - Issuer spread curve: plot spread vs. maturity for all outstanding bonds
   - Fair value spread at [X]-year = Interpolated spread from existing curve

2. **Comparable issuer analysis (fair value)**:
   - Identify 4-6 issuers with same rating and sector
   - Secondary spreads at comparable maturity point
   - Adjust for: credit quality differences, liquidity, issue size, coupon
   - Fair value range: [X]bps to [X]bps over benchmark Treasury

3. **New issue concession (NIC)**:
   - NIC = Reoffer spread - Fair value secondary spread
   - Typical NIC by tenor: 2-5bps (short end), 5-10bps (10yr), 10-15bps (30yr)
   - NIC varies with market conditions: higher in volatile markets, lower in strong demand
   - NIC has been [X]bps on average for similar issuers in the last 30 days

4. **Pricing timeline**:
   - Announcement and initial price thoughts (IPTs): T+[X]bps area
   - Price guidance (after initial orders): T+[X]bps (+/-2bps)
   - Launch and final pricing: T+[X]bps
   - Typical tightening from IPTs to final: [10-25]bps for well-received deals
   - Book coverage required for aggressive tightening: >3x oversubscribed

5. **Multi-tranche optimization**:
   - 5yr/10yr/30yr split: optimize issuer's weighted average maturity and cost
   - Swapped cost comparison: fixed rate bond swapped to floating
     All-in swapped cost = Bond coupon - Swap rate + SOFR (receive fixed, pay floating)
   - Cross-currency swapped cost: issue in EUR, swap to USD
     USD equivalent cost = EUR coupon + Cross-currency basis swap spread
```

---

## 2. Credit Rating Advisory

### Rating Agency Engagement Strategy

```
[Company name] currently rated [S&P: X / Moody's: X / Fitch: X] is planning
[strategic action: e.g., a large acquisition, shareholder return program, or debt-funded
investment] that may impact credit ratings.

Current credit metrics:
- Debt/EBITDA: [X]x
- FFO/Debt: [X]%
- EBITDA/Interest: [X]x
- FCF/Debt: [X]%
- Debt/Capital: [X]%

Pro forma metrics (after planned action):
- Debt/EBITDA: [X]x (up from [X]x)
- FFO/Debt: [X]% (down from [X]%)

Help me navigate the rating agency process:

1. **S&P methodology**:
   - Business risk profile: [Excellent / Strong / Satisfactory / Fair / Weak / Vulnerable]
     Based on: industry risk, competitive position, country risk
   - Financial risk profile: [Minimal / Modest / Intermediate / Significant / Aggressive / Highly leveraged]
     S&P core ratio: FFO/Debt thresholds by category
   - Anchor rating = intersection of business risk and financial risk on S&P matrix
   - Modifiers: diversification, capital structure, financial policy, liquidity, management
   - Rating outcome = Anchor +/- modifiers

2. **Moody's methodology**:
   - Moody's uses scorecard approach with weighted factors:
     Scale and diversification: [X]% weight
     Business profile: [X]% weight
     Profitability and efficiency: [X]% weight
     Leverage and coverage: [X]% weight
     Financial policy: [X]% weight
   - Grid-implied rating vs. actual rating: how large is the gap?
   - Moody's adjustments: operating leases (capitalized), pensions, hybrid equity credit

3. **Downgrade risk assessment**:
   - How far are pro forma metrics from the downgrade trigger?
   - Metric cushion = (Current metric - Downgrade threshold) / Current metric
   - Timeline to return to pre-transaction leverage levels: [X] years
   - Will the agency give credit for a deleveraging commitment?
   - Negative outlook probability: consider prior agency commentary and sector outlook

4. **Rating defense strategy**:
   - Commit to specific leverage targets with timeline
   - Offer financial policy guardrails (e.g., cap shareholder returns until leverage < Xx)
   - Present conservative management projections (agencies penalize misses)
   - Pre-meeting preparation: anticipate agency concerns and prepare mitigants
   - Consider hybrid instruments that receive partial equity credit (50% from S&P, Moody's)
```

---

## 3. Liability Management

### Tender Offer and Exchange Strategy

```
[Issuer name] wants to optimize its debt maturity profile and reduce interest expense.

Existing debt stack:
| Bond | Coupon | Maturity | Outstanding | Current Price | YTW   | Spread |
|------|--------|----------|-------------|---------------|-------|--------|
| [A]  | [X]%   | [date]   | $[X]M       | [X]           | [X]%  | [X]bps |
| [B]  | [X]%   | [date]   | $[X]M       | [X]           | [X]%  | [X]bps |
| [C]  | [X]%   | [date]   | $[X]M       | [X]           | [X]%  | [X]bps |
| [D]  | [X]%   | [date]   | $[X]M       | [X]           | [X]%  | [X]bps |

Current market conditions:
- Issuer's new issue spread at [X]yr: [X]bps
- Benchmark Treasury [X]yr yield: [X]%

Goals: [reduce coupon / extend maturity / smooth maturity wall / reduce total debt]

Evaluate liability management options:

1. **Cash tender offer**:
   - Target bonds: highest coupon and/or nearest maturity
   - Tender price: typically at or near make-whole price
     Make-whole = PV of remaining cash flows discounted at T+[spread] (per indenture)
   - Tender premium = Offer price - Market price
   - NPV savings = PV(old coupon stream) - Tender price - PV(new issuance coupon stream)
   - Early tender premium: additional [X] points for bonds tendered in first [10] days
   - Acceptance priority: by maturity (nearest first) or pro rata

2. **Exchange offer** (old bonds for new bonds):
   - Exchange ratio: $[X] par new bonds per $[X] par old bonds
   - Advantage: no cash outlay, extends maturity, can reduce coupon
   - Exchange premium = New bond value / Old bond value - 1
   - Accounting treatment: modification vs. extinguishment (10% cash flow test)

3. **Consent solicitation** (amend existing bond terms):
   - Strip covenants from outstanding bonds (typically paired with tender)
   - Consent payment: [X] points per $1,000 par
   - Minimum participation threshold: [X]% (often 50% for amendments, higher for key terms)
   - Exit consent: tendering bondholders consent to remove protections for remaining holders

4. **Economic analysis**:
   - All-in cost comparison: old debt vs. new debt (including transaction costs)
   - Weighted average coupon: before and after
   - Weighted average maturity: before and after
   - NPV savings / (cost): present value of interest expense changes net of premiums and fees
   - Breakeven analysis: at what spread does the transaction become NPV-positive?
```

---

## 4. Green / ESG Bond Frameworks

### ESG-Linked Issuance

```
[Issuer name] is considering issuing a [green bond / social bond / sustainability bond /
sustainability-linked bond (SLB)] to align its financing with ESG commitments.

Issuer ESG profile:
- ESG rating: [MSCI: X / Sustainalytics: X / ISS: X]
- Carbon emissions: Scope 1: [X] tCO2e, Scope 2: [X] tCO2e, Scope 3: [X] tCO2e
- Reduction target: [X]% by [year] (baseline: [year])
- Eligible green projects: [list: e.g., renewable energy, green buildings, clean transport]

Proposed structure:
- Size: $[X]M
- Tenor: [X] years
- Type: [Use of Proceeds (green/social) vs. Sustainability-Linked (KPI-based)]

Help me structure and price:

1. **Use of Proceeds bond (Green/Social/Sustainability)**:
   - ICMA Green Bond Principles alignment: Use of proceeds, Project evaluation and selection,
     Management of proceeds, Reporting
   - Eligible categories: [renewable energy, energy efficiency, clean transport, green buildings,
     pollution prevention, sustainable water, biodiversity]
   - Proceeds tracking: segregated account or portfolio approach
   - Impact reporting: annual report on allocation and environmental impact metrics
   - Second-party opinion (SPO): Sustainalytics, Vigeo Eiris, CICERO — expected assessment

2. **Sustainability-Linked Bond (SLB)**:
   - KPI selection: [e.g., Scope 1+2 emissions intensity, renewable energy %, diversity metric]
   - Sustainability Performance Target (SPT): [X]% improvement by [year]
   - Step-up coupon: +[25]bps if SPT not met at observation date
   - Step-down: -[X]bps if SPT exceeded (less common)
   - Verification: annual third-party verification of KPI achievement
   - ICMA SLB Principles: materiality, measurability, ambition, external verification

3. **Greenium analysis** (pricing benefit of ESG label):
   - Greenium = Conventional bond spread - Green bond spread (same issuer, same maturity)
   - Typical greenium: 1-5bps for IG corporates, variable for HY
   - Greenium is larger when: ESG investor demand is strong, framework is credible,
     issuer has strong ESG credentials
   - Is the greenium sufficient to offset SPO costs ($50-150K) and reporting costs?
   - Dedicated ESG investor base: who are the natural buyers?

4. **Regulatory considerations**:
   - EU Taxonomy alignment (for European issuers/investors)
   - EU Green Bond Standard (voluntary but becoming market standard)
   - SEC climate disclosure requirements (for US issuers)
   - Greenwashing risk: what claims must be substantiated?
```

---

## 5. Sovereign and SSA Issuance

### Sovereign Bond Pricing and Auction Analysis

```
[Sovereign issuer / SSA entity] is planning a benchmark bond offering.

Issuer profile:
- Entity: [e.g., Republic of X / KfW / EIB / World Bank]
- Rating: [S&P: X / Moody's: X]
- Existing curve: [list key outstanding benchmarks and yields]
- Annual funding program: $[X]B, [X]% completed year-to-date

Proposed issuance:
- Size: $[X]B equivalent
- Currency: [USD / EUR / GBP / JPY / Local currency]
- Tenor: [X] years
- Format: [Syndication / Auction / Tap of existing bond]

Analyze:

1. **Yield curve analysis**:
   - Plot issuer's existing yield curve
   - Identify gaps and relative value on the curve
   - Optimal tenor = maturity point with steepest curve (most value to issuer)
   - Interpolated fair value yield at target maturity
   - Spread to sovereign benchmark (for SSAs):
     SSA spread = SSA yield - Government bond yield at same maturity

2. **Auction dynamics** (for sovereign auctions):
   - Bid-to-cover ratio: Total bids / Amount offered (target: > 2.0x)
   - Tail = Lowest accepted yield - Average yield (tighter tail = stronger auction)
   - Primary dealer obligations: minimum bid requirements, market-making commitment
   - When-issued (WI) trading: pre-auction price discovery
   - Auction concession = WI yield - Secondary yield of closest existing bond

3. **Syndication approach** (for large/new benchmarks):
   - Book target: [X]x oversubscribed
   - Investor type allocation targets:
     Central banks/official institutions: [X]%
     Banks/bank treasuries: [X]%
     Asset managers: [X]%
     Insurance/pension: [X]%
     Hedge funds: [X]%
   - Geographic distribution targets: [Americas X%, EMEA X%, APAC X%]
   - Price tightening from IPTs to reoffer: [X]bps

4. **Tap vs. new bond decision**:
   - Tap existing bond: adds to outstanding (improves liquidity), no new line on curve
     Tap price = Secondary market price +/- NIC
   - New bond: creates new benchmark point, but splits liquidity across more lines
   - Decision factors: existing bond outstanding size, curve gaps, investor preference

5. **Cross-currency considerations** (if issuing outside home currency):
   - All-in swapped cost = Foreign currency coupon + Cross-currency basis swap
   - Is it cheaper to issue in USD, EUR, or home currency after swap?
   - Basis swap dynamics: negative basis = cheaper to issue in foreign currency
   - Investor diversification benefit of multi-currency issuance program
```

---

## Mathematical Frameworks

Building on [`../roles/investment-banker.md`](../roles/investment-banker.md):

**Spread Measures**:
- G-spread = Bond yield - Interpolated government bond yield at same maturity
- I-spread = Bond yield - Interpolated swap rate at same maturity
- Z-spread: constant spread added to each point on the spot curve such that
  Price = Sum[CF_t / (1 + r_t + Z)^t] where r_t = spot rate at time t
- OAS = Z-spread - Option cost (for callable/puttable bonds)
- ASW (asset swap spread) = Bond coupon - Swap rate + (Par - Bond price) / Annuity factor

**New Issue Concession**:
- NIC = Reoffer spread - Fair value spread
- Fair value spread = Interpolated spread from issuer's secondary curve or peer composite
- Effective NIC = Reoffer spread - Secondary spread (3-5 days post-issuance)
  If the bond tightens significantly post-issue, NIC was likely too generous

**Duration and Sensitivity**:
- Modified duration = Macaulay duration / (1 + y/n)
- Price change for spread move: dP/P = -Modified duration x dSpread + 0.5 x Convexity x dSpread^2
- DV01 = Price x Modified duration / 10,000 (dollar value of 1bp move)
- Carry = Bond yield - Funding rate (repo rate or SOFR)
- Roll-down return = Price gain from rolling down the curve over holding period

**Swap-Adjusted Economics**:
- All-in fixed cost = Bond coupon
- All-in floating cost = Bond coupon - Swap rate + SOFR = SOFR + (Bond spread - Swap spread)
- Cross-currency swapped cost = Foreign coupon + XCCY basis swap spread
  If USD/EUR XCCY basis = -20bps, EUR issuer saves 20bps by issuing in USD and swapping

---

## See Also

- [Investment Banker Role — Capital Structure](../roles/investment-banker.md) — optimal capital structure, cost of capital
- [Leveraged Finance](leveraged-finance.md) — sub-investment grade debt markets
- [Equity Capital Markets](equity-capital-markets.md) — equity side of capital raising
- [Restructuring](restructuring.md) — distressed debt, liability management in extremis
- [Equity Research](equity-research.md) — credit research parallels
