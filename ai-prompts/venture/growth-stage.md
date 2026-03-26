# Growth-Stage Investing -- Series B+ and Late-Stage

```
You are a senior growth-stage venture capital investor at a leading crossover
fund deploying $100M-$500M checks into Series B through pre-IPO companies. You
have deep expertise in SaaS metrics, unit economics, public market comparable
analysis, IPO readiness, and structured late-stage terms. You think like both
a venture investor (upside optimization) and a public market investor (downside
protection, valuation discipline). You have led 30+ growth rounds and taken 10+
companies public. You are fluent in financial modeling, capital structure, and
governance.
```

## What This Desk Does

The growth-stage investing team leads or co-leads investments in companies at Series B and beyond -- typically businesses with $10M-$200M+ in revenue, proven product-market fit, and a path to profitability or IPO. The core challenge shifts from "will this work?" (early stage) to "how big can this get, and what is it worth?" The team conducts rigorous financial analysis on growth trajectories, margin profiles, and capital efficiency, while also evaluating governance, management depth, and exit optionality. Late-stage investments increasingly incorporate structured terms (liquidation preferences, ratchets, milestones) that provide downside protection. Ownership targets are typically 5-15%, with check sizes ranging from $25M to $500M+.

---

## 1. Growth Metrics Analysis

At the growth stage, quantitative metrics drive the investment decision. The key frameworks are the Rule of 40, burn multiple, magic number, and unit economics.

### SaaS Metrics Benchmarks by Stage

```
                    Series B        Series C        Pre-IPO
ARR                 $10-30M         $30-80M         $80-200M+
YoY Growth          80-150%         50-100%         30-60%
Net Dollar Retention 110-130%       115-140%        120-150%
Gross Margin        60-75%          65-80%          70-85%
Rule of 40 Score    40-70           40-60           40-55
Burn Multiple       1.5-3.0x        1.0-2.0x        0.5-1.5x
Magic Number        0.5-1.0         0.7-1.2         0.8-1.5
LTV/CAC             3-5x            4-7x            5-10x
CAC Payback (mo)    18-24           12-18           8-15
```

```
Analyze the growth metrics for [COMPANY_NAME], a [STAGE] [SAAS/MARKETPLACE/
FINTECH/OTHER] company with the following data:

REVENUE AND GROWTH:
- Current ARR: $[X]M
- ARR 12 months ago: $[Y]M
- ARR 24 months ago: $[Z]M
- Net new ARR this quarter: $[Q]M
- Quarterly net new ARR trend (last 4 quarters): [Q1, Q2, Q3, Q4]

Calculate:
1. YoY revenue growth rate and growth rate trend (accelerating/decelerating)
2. Quarter-over-quarter ARR growth and annualized run rate
3. Net dollar retention: [VALUE]% -- decompose into gross retention + expansion
4. Rule of 40 = Revenue Growth% + FCF Margin% = [VALUE]
5. Burn multiple = Net Burn / Net New ARR = [VALUE]
6. Magic number = Net New ARR (Q) / S&M Spend (Q-1) = [VALUE]

UNIT ECONOMICS:
- Fully-loaded CAC: $[A] (include methodology: S&M / new logos)
- Gross margin adjusted LTV: $[B]
- LTV/CAC ratio: [VALUE]x
- CAC payback period: [VALUE] months

Benchmark all metrics against [STAGE] medians for [SECTOR]. Flag any metrics
that are >1 standard deviation below benchmark. Identify the top 3 metrics
that are most impressive and top 3 that are most concerning.

What revenue growth rate is required to justify a $[VALUATION]M pre-money
valuation at a [X]x forward revenue multiple?
```

```
Model the revenue trajectory for [COMPANY_NAME] under three scenarios:

BASE CASE: Current growth rate decelerates by [X]% per year
  - Year 1 ARR: $[A]M at [G1]% growth
  - Year 2 ARR: $[B]M at [G2]% growth
  - Year 3 ARR: $[C]M at [G3]% growth

UPSIDE CASE: Growth sustains due to [NEW_PRODUCT/MARKET_EXPANSION/UPSELL]
  - Model the incremental revenue from [GROWTH_DRIVER]
  - Quantify the impact on net dollar retention

DOWNSIDE CASE: Growth decelerates faster due to [COMPETITION/SATURATION/CHURN]
  - Model increased churn rate from [X]% to [Y]%
  - Model reduced new logo acquisition by [Z]%

For each scenario, calculate the implied valuation at exit assuming:
  - Public market revenue multiples: [LOW]x / [MID]x / [HIGH]x
  - Apply a [DISCOUNT]% private-to-public discount
  - Time to exit: [N] years

What return multiple does each scenario generate on a $[INVESTMENT]M investment
at a $[PRE_MONEY]M pre-money valuation?
```

### Revenue Multiple Regression

```
Revenue multiple = f(growth_rate, gross_margin, net_retention, FCF_margin, TAM)

Simplified regression model for SaaS:
  EV/NTM Revenue = a + b1*(NTM Growth%) + b2*(Gross Margin%) + b3*(Rule of 40)

Typical coefficients (public SaaS, 2023-2025 regime):
  Intercept: ~2x
  Growth coefficient: ~0.15x per 10pp of growth
  Margin coefficient: ~0.05x per 10pp of gross margin
  Rule of 40 premium: ~0.10x per 10pp above 40

Apply IPO discount of 15-25% for pre-IPO private rounds
Apply illiquidity discount of 20-30% for secondary transactions
```

---

## 2. IPO Readiness Assessment

```
Evaluate [COMPANY_NAME]'s readiness for an initial public offering:

FINANCIAL READINESS:
- Revenue scale: $[X]M ARR (benchmark: >$100M preferred, >$200M for premium)
- Growth rate: [Y]% YoY (benchmark: >30% for compelling growth story)
- Margin profile: Gross margin [A]%, operating margin [B]%, FCF margin [C]%
- Revenue predictability: % recurring, contract duration, backlog visibility
- 3-year audited financials: [COMPLETE/IN PROGRESS/NOT STARTED]
- SOX compliance readiness: [STATUS]

GOVERNANCE AND MANAGEMENT:
- Board composition: [DETAILS] -- do they meet NYSE/NASDAQ independence rules?
- CFO experience: Has the CFO taken a company public before?
- Audit committee: Financial expert present? Independent?
- Management depth: VP+ hires in last 12 months, bench strength
- Investor relations function: [IN PLACE/HIRING/NOT STARTED]
- Legal counsel: Securities counsel retained?

MARKET AND TIMING:
- Current IPO window: [OPEN/CAUTIOUS/CLOSED] for [SECTOR]
- Comparable recent IPOs: [COMP_1, COMP_2, COMP_3]
- Expected trading multiples based on comps: [X-Y]x NTM revenue
- Implied market cap at IPO: $[Z]M
- Minimum viable market cap for institutional interest: $[THRESHOLD]M

S-1 NARRATIVE STRENGTH:
- Is there a clear, differentiated story for public market investors?
- What is the "category" or "theme" the company fits into?
- Risk factors: What are the top 3 risks that public market investors will
  focus on?

Timeline estimate: [MONTHS] to IPO-ready. Key milestones and blockers.
```

---

## 3. Secondary Transaction Analysis

```
Evaluate a proposed secondary transaction in [COMPANY_NAME]:

TRANSACTION DETAILS:
- Seller: [FOUNDER/EARLY_EMPLOYEE/EARLY_INVESTOR]
- Shares offered: [N] shares of [COMMON/PREFERRED] stock
- Proposed price per share: $[X] (vs. last round PPS of $[Y])
- Implied discount to last round: [Z]%
- Last round valuation: $[V]M at [DATE], led by [INVESTOR]
- Current company performance vs. plan at last round: [ABOVE/ON/BELOW]

PRICING ANALYSIS:
1. Is the discount to last round appropriate given:
   - Time elapsed since last round
   - Company performance trajectory
   - Current market conditions for [SECTOR]
   - Liquidity premium / illiquidity discount
   - Common vs. preferred discount (if applicable): typically 15-35%

2. Fair value range using:
   - Last round price adjusted for performance: $[A]
   - Comparable company multiples applied to current metrics: $[B]
   - 409A valuation (if available): $[C]
   - Implied price from recent secondary market trades: $[D]

STRUCTURAL CONSIDERATIONS:
- Right of first refusal (ROFR): Will the company or existing investors
  exercise? What is the ROFR process and timeline?
- Transfer restrictions: Board approval required? Investor consent?
- Information rights: What financial information will the buyer receive?
- Tag-along / co-sale rights: Do other holders have the right to participate?
- Tax implications for seller: QSBS eligibility? Long-term capital gains?

INFORMATION ASYMMETRY RISK:
- Is the company fundraising or contemplating a transaction?
- Are there material nonpublic developments (positive or negative)?
- What is the seller's motivation? (Liquidity need, diversification, signal?)

Recommendation: BUY / PASS / NEGOTIATE TO $[TARGET_PRICE]
```

---

## 4. Down Round and Restructuring

```
Analyze a potential down round or restructuring for [COMPANY_NAME]:

CURRENT SITUATION:
- Last round: Series [X] at $[V]M post-money valuation, [DATE]
- Current proposed round: $[A]M at $[B]M pre-money (implies [C]% down)
- Cash remaining: $[D]M at current burn of $[E]M/month = [F] months runway
- Key issue: [MISSED_PLAN/MARKET_DOWNTURN/COMPETITIVE_LOSS/PIVOT]

ANTI-DILUTION ANALYSIS:
1. Full ratchet: Series [X] preferred price resets from $[P1] to $[P2]
   - Additional shares issued to Series [X]: [N]
   - Dilution to founders/common: from [A]% to [B]%

2. Broad-based weighted average:
   New Conversion Price = Old Price * (CSO + DIV) / (CSO + CONV)
   where:
     CSO = Common shares outstanding (fully diluted) pre-round
     DIV = Shares that would be issued at old price (New Money / Old Price)
     CONV = Shares actually issued at new price (New Money / New Price)

   Calculate the adjusted conversion price and resulting dilution.

3. Narrow-based weighted average: Same formula but CSO excludes option pool
   and common. Show the difference vs. broad-based.

PAY-TO-PLAY PROVISIONS:
- Which existing investors are participating pro-rata? [LIST]
- Which are not participating? [LIST]
- Pay-to-play penalty: Conversion from preferred to common? Loss of
  anti-dilution? Loss of other rights?

RECAPITALIZATION SCENARIOS:
- Reverse stock split: [RATIO] to reset share price above $[THRESHOLD]
- Preferred stock cancellation or conversion
- New option pool grant: [X]% to retain key employees (management carve-out)
- Bridge financing terms if applicable

Model the post-restructuring cap table under each scenario. Show the
economic impact on all stakeholder classes.
```

---

## 5. Late-Stage Term Sheet Dynamics

```
Evaluate the following late-stage term sheet for [COMPANY_NAME]:

STRUCTURED TERMS:
- Investment amount: $[X]M
- Pre-money valuation: $[Y]M (headline)
- Liquidation preference: [MULTIPLE]x [PARTICIPATING/NON-PARTICIPATING]
  with [CAP] cap
- IPO ratchet: If IPO price < $[THRESHOLD], investor receives additional
  shares to guarantee [MINIMUM_RETURN]x return
- Minimum IPO size: $[Z]M market cap required, else auto-conversion blocked
- Milestone-based tranching: $[A]M at close, $[B]M upon achieving [METRIC]
- Most favored nation (MFN): [DETAILS]
- Redemption right: After [N] years, investor can force redemption at [X]x

ANALYSIS:
1. What is the "effective" valuation after accounting for all structural
   protections? Model the investor's guaranteed minimum return vs. headline
   valuation.

   Effective Valuation = Headline Valuation * (1 - Structure Discount)
   where Structure Discount accounts for:
   - Liquidation preference above 1x: ~[X]% discount per additional 1x
   - Participation rights: ~[Y]% discount
   - IPO ratchet: ~[Z]% discount (model at various IPO price scenarios)

2. At what IPO valuation does the ratchet trigger? What is the maximum
   dilution to existing shareholders from the ratchet?

3. Compare this term sheet to a "clean" term sheet at a lower headline
   valuation. At what clean valuation would founders be economically
   equivalent or better off?

4. Model the investor's return profile across exit values from $[LOW]M to
   $[HIGH]M in $[STEP]M increments. Show both the investor's return and
   founder/common dilution at each level.

5. How do these terms interact with prior round preferences? Build the
   full waterfall.
```

---

## Dilution Modeling Framework

```
Multi-round dilution model:

Define for each round i:
  Pre_i = Pre-money valuation
  Inv_i = Investment amount
  Pool_i = Option pool as % of post-money
  Post_i = Pre_i + Inv_i

  Dilution_i = (Inv_i + Pool_increase_i) / Post_i

Cumulative founder ownership after N rounds:
  Own_founder,N = Own_founder,0 * PRODUCT(1 - Dilution_i) for i=1..N

Example path:
  Founding:     100% ownership
  Seed:         100% * (1 - 25%) = 75%
  Series A:     75% * (1 - 30%) = 52.5%
  Series B:     52.5% * (1 - 25%) = 39.4%
  Series C:     39.4% * (1 - 20%) = 31.5%
  Pre-IPO:      31.5% * (1 - 15%) = 26.8%

Implied exit value for founder to reach $[TARGET] wealth:
  Required Exit = $TARGET / (Own_founder,N * (1 - tax_rate))
```

---

## See Also

- [Early-Stage Investing](early-stage.md) -- Seed and Series A frameworks
- [Crypto / Web3](crypto-web3.md) -- Token-based growth-stage dynamics
- [Biotech / Healthcare](biotech-healthcare.md) -- Clinical-stage growth metrics
- [Platform Operations](platform-operations.md) -- Operational value creation at scale
- [Banking - ECM](../banking/) -- IPO execution and capital markets
- [Venture Overview](README.md) -- Fund economics and portfolio construction
