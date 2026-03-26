# Credit & Distressed Strategies

## Role Context

```
You are a senior credit portfolio manager at a $4B fund specializing in performing credit,
stressed, and distressed debt. You analyze capital structures from the top (investment-grade
senior secured) to the bottom (equity stubs in bankruptcy). You think in terms of credit
spreads, default probabilities, recovery rates, and the legal priority of claims. Every
position requires an explicit view on both probability of default AND loss given default --
spread tightening alone is not a thesis. You are fluent in bond indentures, credit
agreements, intercreditor dynamics, and Chapter 11 reorganization. You understand that
credit is fundamentally asymmetric: capped upside (par), large downside (default + low
recovery), which demands rigorous position sizing and diversification. You never buy a bond
because "the yield is attractive" without modeling the full distribution of outcomes
including impairment.
```

---

## What This Desk Does

Credit and distressed strategies invest across the credit quality spectrum, from investment-grade corporate bonds to deeply distressed debt trading at pennies on the dollar. The performing credit book generates returns from carry (coupon income) and spread compression, with edge from superior credit analysis and relative value identification. The distressed book generates returns from buying debt of companies in or near default at prices below estimated recovery value, often participating actively in restructuring negotiations. Capital structure arbitrage exploits mispricings between different securities of the same issuer -- equity vs. CDS, senior vs. subordinated debt, convertible bonds vs. equity + straight debt. The strategy is capacity-constrained by illiquidity and requires deep legal and accounting expertise alongside financial analysis.

---

## 1. Credit Analysis

### Comprehensive Credit Assessment

```
I'm analyzing [company name / ticker] for a potential [long / short] position in its
[senior secured / senior unsecured / subordinated / high yield] debt.

Issuer profile:
- Sector: [industry]
- Rating: [Moody's / S&P / Fitch]
- Total debt: $[X]B
- LTM EBITDA: $[X]M
- Interest coverage (EBITDA / Interest): [X]x
- Net leverage (Net Debt / EBITDA): [X]x
- Free cash flow: $[X]M
- Nearest maturity: $[X]M due [date]

Current bond pricing:
- Bond: [CUSIP / description, coupon, maturity]
- Price: $[X] (yield: [X]%, spread: +[X] bps over [benchmark])
- Comparable bonds spread: +[X] bps

Perform full credit analysis:

1. **Credit scoring framework**:
   | Factor | Metric | Value | Score (1-5) |
   |--------|--------|-------|-------------|
   | Leverage | Net Debt / EBITDA | [X]x | [X] |
   | Coverage | EBITDA / Interest | [X]x | [X] |
   | Liquidity | Cash + Revolver / Near-term maturities | [X]x | [X] |
   | FCF generation | FCF / Total Debt | [X]% | [X] |
   | Revenue stability | Revenue volatility (5yr) | [X]% | [X] |
   | Asset coverage | Enterprise Value / Total Debt | [X]x | [X] |
   | Management quality | Track record, alignment | [qualitative] | [X] |

   Composite score -> Implied rating: [X]
   Composite score vs. actual rating: [in line / better / worse]

2. **Spread decomposition**:
   Current spread = Risk-free compensation + Default risk premium + Liquidity premium +
                    Ratings migration premium + Systematic risk premium

   Default risk premium = PD x LGD x (1 + risk_premium_multiplier)
   where PD = probability of default, LGD = loss given default

   If current spread > fair spread given my PD and LGD estimates, the bond is cheap
   If current spread < fair spread, the bond is rich

3. **Default probability estimation**:
   a) Market-implied PD:
      PD_implied = Spread / LGD_assumed (rough approximation)
      More precisely: PD = 1 - exp(-spread / (1 - Recovery_rate))

   b) Model-based PD:
      - Altman Z-Score: Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
        where A = Working Capital/TA, B = Retained Earnings/TA, C = EBIT/TA,
              D = Market Equity/Total Liabilities, E = Sales/TA
        Z > 2.99: Safe zone. 1.81 < Z < 2.99: Grey zone. Z < 1.81: Distress zone.
      - Merton model (structural): Default when asset value < debt face value at maturity
        Distance to Default = (ln(V/D) + (mu - 0.5*sigma^2)*T) / (sigma * sqrt(T))
        where V = asset value, D = debt, mu = asset drift, sigma = asset vol

4. **Recovery rate estimation**:
   Recovery depends on:
   - Seniority: Senior secured [40-65]%, Senior unsecured [30-50]%,
     Subordinated [15-30]%, Equity [0-5]%
   - Asset quality: Asset-heavy businesses recover more than asset-light
   - Industry: Utilities/infrastructure > Manufacturing > Retail > Technology
   - Leverage at default: Higher leverage = lower recovery (more claims, same assets)

   My estimated recovery rate for this tranche: [X]%

5. **Relative value**:
   - Spread vs. rating-matched peers: [cheap / fair / rich] by [X] bps
   - Spread vs. historical range: Current percentile [X]%
   - Spread per turn of leverage vs. peers
   - CDS vs. cash bond basis: CDS spread [X] bps vs. bond Z-spread [X] bps
     Positive basis (CDS > bond): Short bond, buy CDS protection
     Negative basis (CDS < bond): Buy bond, buy CDS protection (earn carry with hedge)
```

---

## 2. Capital Structure Arbitrage

### CDS vs. Equity Capital Structure Trade

```
I want to trade the capital structure of [company name]:

Equity: Price $[X], market cap $[X]B, implied vol [X]%
CDS: [5-year] spread [X] bps, notional $[X]M
Debt: Total debt $[X]B, weighted average coupon [X]%
Asset volatility (estimated): [X]%

Capital structure arbitrage using the Merton model:

1. **Merton model setup**:
   The firm's equity is a call option on its assets with strike = face value of debt:
   E = V x N(d1) - D x exp(-rT) x N(d2)

   where:
   d1 = (ln(V/D) + (r + sigma_V^2/2) x T) / (sigma_V x sqrt(T))
   d2 = d1 - sigma_V x sqrt(T)

   V = asset value (unobservable, solve iteratively)
   sigma_V = asset volatility (derived from equity vol and leverage)
   sigma_V = sigma_E x (E / V) x (1 / N(d1))

2. **CDS-equity hedge ratio**:
   The Merton model implies a relationship between CDS spread and equity:
   - If CDS is "too wide" relative to equity price -> Buy CDS protection (receive spread),
     go long equity (Merton says equity is cheap relative to credit risk)
   - If CDS is "too narrow" relative to equity -> Sell CDS protection, short equity

   Hedge ratio: Delta of equity w.r.t. asset value / CDS sensitivity to asset value
   In practice: For every $1M of CDS notional, hedge with [X] shares of equity

3. **Convertible arbitrage**:
   Convertible bond: Price $[X], coupon [X]%, conversion ratio [X], maturity [date]
   Straight bond value (credit component): $[X]
   Conversion value (equity component): [X] shares x $[X] = $[X]
   Option value embedded in convertible: $[X]

   Trade: Buy convertible, short [delta x conversion ratio] shares of equity
   - Earn: Coupon carry + positive gamma (convexity)
   - Risk: Credit deterioration, borrow recall on short, vol compression
   - Greeks: Delta [X], Gamma [X], Vega [X], Rho [X]

4. **Senior vs. subordinated relative value**:
   Senior bond: Price $[X], yield [X]%, spread +[X] bps
   Subordinated bond: Price $[X], yield [X]%, spread +[X] bps
   Spread differential: [X] bps

   Is the subordination premium fair?
   - Model default scenario: Senior recovery [X]%, Sub recovery [X]%
   - Fair spread differential = (PD x (LGD_sub - LGD_senior)) / (1 - PD x LGD_sub)
   - If actual differential > fair differential: Sub is cheap relative to senior
   - Trade: Long sub / Short senior (compression trade)
```

---

## 3. Distressed Investing

### Analyze a Distressed Debt Opportunity

```
[Company name] is in financial distress:
- Status: [pre-filing / Chapter 11 / out-of-court restructuring / exchange offer]
- Filing date (if applicable): [date]
- Total debt: $[X]B across [X] tranches
- LTM EBITDA: $[X]M (or negative: $[X]M operating loss)
- Cash on hand: $[X]M, monthly burn rate: $[X]M
- DIP financing: $[X]M [committed / uncommitteed]

Capital structure and current trading levels:
| Tranche | Face Value | Priority | Current Price | Implied Recovery |
|---------|-----------|----------|---------------|-----------------|
| DIP / Super-priority | $[X]M | 1st | $[X] | [X]% |
| 1st Lien Secured | $[X]M | 2nd | $[X] | [X]% |
| 2nd Lien Secured | $[X]M | 3rd | $[X] | [X]% |
| Senior Unsecured | $[X]M | 4th | $[X] | [X]% |
| Subordinated | $[X]M | 5th | $[X] | [X]% |
| Equity | $[X]M mkt cap | Last | $[X] | [X]% |

Distressed analysis:

1. **Fulcrum security identification**:
   The fulcrum security is the tranche where value "breaks" -- senior to the fulcrum
   recovers par (or close), junior to the fulcrum recovers little or nothing.

   Enterprise value estimate: $[X]M (based on [normalized EBITDA x exit multiple /
   asset liquidation value / comparable transactions])

   Recovery waterfall:
   - DIP claims: $[X]M -> Recovery: [100]% (first priority)
   - Administrative claims: $[X]M -> Recovery: [100]%
   - 1st Lien: $[X]M -> Recovery: [X]% (enterprise value remaining: $[X]M)
   - 2nd Lien: $[X]M -> Recovery: [X]% (enterprise value remaining: $[X]M)
   - Senior Unsecured: $[X]M -> Recovery: [X]% (enterprise value remaining: $[X]M)
   - Sub / Equity: Recovery: [X]%

   Fulcrum security: [identify the tranche where recovery drops below par]

   Strategy: Buy the fulcrum security at [X] cents on the dollar.
   Expected recovery: [X] cents -> Return: [X]%

2. **Plan of reorganization (POR) scenarios**:
   | Scenario | EV Estimate | Fulcrum Recovery | Probability |
   |----------|-------------|-----------------|-------------|
   | High case | $[X]M | [X] cents | [X]% |
   | Base case | $[X]M | [X] cents | [X]% |
   | Low case | $[X]M | [X] cents | [X]% |
   | Liquidation | $[X]M | [X] cents | [X]% |

   E[Recovery] = Sum: P(scenario) x Recovery(scenario)
   E[Return] = (E[Recovery] - Purchase price) / Purchase price

3. **Loan-to-own strategy** (if applicable):
   - Acquire controlling position in the fulcrum security
   - Influence plan of reorganization to convert debt to equity
   - Target: [X]% ownership of reorganized equity
   - Post-reorg equity value estimate: $[X] per share
   - Total return: Debt purchase price -> equity value + accrued interest/fees

4. **Timeline and process**:
   - DIP financing approval: [date]
   - Bar date for claims filing: [date]
   - Plan filing deadline: [date]
   - Confirmation hearing: [date]
   - Emergence from bankruptcy: estimated [date]
   - Total duration: [X] months (average Chapter 11: 12-18 months)

5. **Key risks**:
   - EV estimation error: Distressed EBITDA is unstable; use normalized/projected
   - Process risk: Judges can surprise, competing plans, cram-down disputes
   - Liquidity risk: Distressed debt is illiquid; bid-ask spreads [5-10]+ points
   - Time risk: Capital is locked up during bankruptcy process
   - Priming risk: New DIP financing may subordinate existing claims
```

---

## 4. Credit Long/Short

### Construct a Credit Relative Value Trade

```
I want to construct a [credit pair trade / basis trade / curve trade] in:

Long leg: [Issuer A / Bond CUSIP / CDS] at spread +[X] bps
Short leg: [Issuer B / Bond CUSIP / CDS] at spread +[X] bps
Spread differential: [X] bps
Historical range of differential: [X] to [X] bps (current percentile: [X]%)

Trade types:

1. **Credit pair trade** (long one issuer vs. short another):
   - Thesis: [Issuer A] is fundamentally stronger / has better trajectory than [Issuer B]
   - Spread differential should [widen / compress] from [X] bps to [X] bps
   - DV01-neutral sizing: Match the interest rate sensitivity so you're only exposed to
     spread moves, not rates
   - Long leg DV01: $[X] per bp per $1M notional
   - Short leg DV01: $[X] per bp per $1M notional
   - Hedge ratio: DV01_long / DV01_short = [X]:1

2. **CDS basis trade** (CDS vs. cash bond for same issuer):
   - Cash bond Z-spread: +[X] bps
   - CDS spread: +[X] bps
   - Basis = CDS spread - Bond Z-spread = [X] bps
   - Negative basis (CDS < bond): Buy bond + buy CDS protection. Earn carry with credit hedge.
   - Positive basis (CDS > bond): More complex; short bond + sell CDS protection.
   - Basis drivers: Funding costs, repo rate, bond liquidity, CDS liquidity, cheapest-to-deliver

3. **Credit curve trade** (same issuer, different maturities):
   - Short-end spread: +[X] bps ([X]-year)
   - Long-end spread: +[X] bps ([X]-year)
   - Curve slope: [X] bps
   - If credit is improving: Curve should flatten (long-end tightens more).
     Trade: Long long-end, short short-end.
   - If credit is deteriorating: Curve inverts (short-end widens more, default imminent).
     Trade: Short short-end, long long-end.

4. **Index vs. single-name relative value**:
   - CDX/iTraxx index spread: +[X] bps
   - Single-name CDS spread: +[X] bps
   - Intrinsic value of index (sum of single-name components): +[X] bps
   - Skew: Single-name spread - Index contribution = [X] bps
   - If skew is wide: Buy index protection, sell single-name protection
   - Drivers: Index roll technicals, hedging demand, correlation trading

5. **Expected return and risk**:
   - Carry: Net coupon income on long/short position = [X] bps/year
   - Roll-down: Spread curve roll if held to [X] months = [X] bps
   - Spread change target: [X] bps compression = $[X] P&L
   - Breakeven time: Months of carry needed to offset [X] bps adverse spread move
   - Max loss scenario: What if differential goes to historical extreme? Loss = $[X]
```

---

## 5. Stressed / Distressed Screening

### Screen for Stressed and Distressed Credits

```
I want to screen for [stressed / distressed / potentially mispriced] credits in the
[high yield / investment grade / leveraged loan] universe.

Screening criteria:

1. **Quantitative distress indicators**:
   - Altman Z-Score < [1.81] (distress zone)
     Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(Mkt Equity/Total Liab) + 1.0(Sales/TA)

   - Distance to Default (Merton model) < [2.0] standard deviations
     DD = (ln(V/D) + (mu - 0.5*sigma^2)*T) / (sigma*sqrt(T))
     DD < 1.0 = very high default probability

   - CDS-implied rating significantly worse than agency rating
     CDS spread > [2x] the median for current rating category

   - Interest coverage < [1.5]x (EBITDA barely covers interest)

   - Leverage > [6.0]x Net Debt / EBITDA

2. **Market-based distress signals**:
   - Bond price < $[80] (stressed) or < $[60] (distressed)
   - Yield spread > +[800] bps (stressed) or > +[1500] bps (distressed)
   - Bond price drop > [15]% in last [30] days (acute stress)
   - Equity decline > [50]% in last [6] months (equity signaling credit stress)
   - CDS spread widening > [200] bps in last [60] days

3. **Covenant and maturity analysis**:
   - Nearest maturity wall: $[X]M due within [12] months
   - Revolver availability: $[X]M undrawn (liquidity runway: [X] months at current burn)
   - Covenant headroom: [X]% room on leverage covenant before trip
   - Maintenance vs. incurrence covenants: [maintenance covenants are tighter, trip automatically]
   - Restricted payments basket: Can the company dividend cash to holdco / equity?

4. **Hazard rate analysis** (reduced-form credit model):
   CDS spread = hazard_rate x (1 - Recovery_rate)
   Hazard rate = CDS_spread / (1 - Recovery_rate)

   For CDS spread of [X] bps and recovery assumption of [X]%:
   Annual hazard rate = [X]%
   Cumulative 5-year default probability = 1 - exp(-hazard_rate x 5) = [X]%

   Compare implied PD to fundamental PD from Z-score / Merton model:
   - If market-implied PD > fundamental PD: Bond may be oversold (opportunity)
   - If market-implied PD < fundamental PD: Bond may be overpriced (avoid or short)

5. **Loss Given Default (LGD) estimation**:
   LGD = 1 - Recovery rate

   Recovery rate drivers:
   - Seniority: Senior secured ~ 55%, Senior unsecured ~ 40%, Sub ~ 25%
   - Industry: Capital-intensive industries recover more (tangible assets)
   - Cycle: Recoveries are lower when defaults cluster (fire sale discount)
   - Country: Jurisdiction affects enforcement and bankruptcy efficiency

   Expected Loss = PD x LGD
   Spread should compensate for: Expected Loss + Risk premium + Liquidity premium

   If spread >> Expected Loss + reasonable premiums: Potential long opportunity
   If spread << Expected Loss: Potential short or underweight
```

---

## Mathematical Frameworks Reference

**Merton (Structural) Model**:
Equity = Call option on firm assets with strike = debt face value. E = V*N(d1) - D*e^(-rT)*N(d2). Default occurs when asset value falls below debt at maturity. Distance to Default measures how many standard deviations the firm is from default.

**Reduced-Form (Hazard Rate) Model**:
Default is modeled as a Poisson process with intensity (hazard rate) lambda. P(default by T) = 1 - exp(-lambda*T). Hazard rate is inferred from CDS spreads: lambda = spread / (1 - R). More tractable than structural models for pricing CDS and credit derivatives.

**Altman Z-Score**:
Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MktEquity/TotalLiab) + 1.0(Sales/TA). Z > 2.99 = safe, 1.81-2.99 = grey zone, Z < 1.81 = distress. Originally calibrated on manufacturing firms; use Z'' (four-factor) model for non-manufacturing and private companies.

**Recovery Waterfall**:
In bankruptcy, claims are paid in strict priority: DIP/super-priority -> secured claims -> administrative claims -> senior unsecured -> subordinated -> equity. The fulcrum security is the tranche where enterprise value is exhausted. Securities senior to the fulcrum recover at or near par; junior securities recover pennies or zero.

**CDS-Bond Basis**:
Basis = CDS spread - Bond Z-spread. Negative basis = buy bond + buy CDS protection (earn carry, credit-neutral). Basis is driven by funding costs, liquidity differentials, bond cheapest-to-deliver optionality, and supply/demand technicals.

**Credit Spread Decomposition**:
Spread = Expected loss + Credit risk premium + Liquidity premium + Tax adjustment. Expected loss = PD x LGD. The credit risk premium compensates for systematic default risk (defaults cluster in recessions). The liquidity premium compensates for illiquidity and bid-ask costs.

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- Portfolio construction, risk decomposition
- [`event-driven.md`](event-driven.md) -- Restructuring events, exchange offers, distressed M&A
- [`fundamental-long-short.md`](fundamental-long-short.md) -- Equity stub analysis, equity-credit relative value
- [`global-macro.md`](global-macro.md) -- Macro credit cycles, sovereign distressed, EM credit
