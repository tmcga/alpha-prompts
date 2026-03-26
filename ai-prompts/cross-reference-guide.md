# Cross-Reference Guide: Same Event, Different Desks

The same company, the same headline, the same data — and five completely different reactions depending on which desk you sit at. An equity research analyst sees a rating decision. A merger arb trader sees a spread. A restructuring banker sees a fee opportunity. A VC sees a market map shifting.

This guide provides complete, fill-in-the-blank prompt templates organized by scenario. Each scenario presents a single triggering event, then shows how professionals across different Wall Street functions would analyze it using fundamentally different frameworks, metrics, and decision criteria.

**How to use this guide:** Find the scenario closest to your situation, pick the desk perspective that matches your role (or borrow from adjacent ones), fill in the bracketed fields, and send the prompt to your LLM of choice. Combine perspectives for a 360-degree view.

---

## Scenario 1: Evaluating a Public Technology Company

*Trigger: A publicly traded technology company has reported earnings, released a new product, or is experiencing a meaningful change in fundamentals. Different desks approach the same company with entirely different objectives.*

---

### As an Equity Research Analyst

```
You are a sell-side equity research analyst covering [sector, e.g., enterprise software]
at a bulge bracket bank. You are writing a research note on [COMPANY NAME] ([TICKER])
following [CATALYST: e.g., Q3 earnings release / product launch / management change].

Current share price: $[PRICE]
Your prior rating: [Buy / Hold / Sell]
Your prior price target: $[PRIOR PT]
Consensus EPS estimate for next quarter: $[CONSENSUS EPS]
Reported EPS: $[REPORTED EPS]

Produce the following:

1. EARNINGS QUALITY ANALYSIS
   - Revenue beat/miss vs. consensus: quantify the delta and whether it was
     driven by organic growth, pricing, or one-time items
   - Gross margin trajectory: compare to prior 4 quarters and identify mix shift effects
   - Operating leverage: SG&A and R&D as % of revenue vs. prior periods
   - Free cash flow conversion: FCF / Net Income ratio and trend
   - Deferred revenue and RPO growth vs. revenue growth (leading indicator test)

2. FORWARD ESTIMATES REVISION
   - Build a quarterly revenue model for the next 4 quarters using:
     - Reported ARR or bookings run-rate
     - Net retention rate (if disclosed) applied to existing customer base
     - New customer acquisition trends (logo adds x average ACV)
     - Seasonal patterns from prior years
   - Derive EPS estimates using management's operating margin guidance
     and your tax rate assumption of [TAX RATE, e.g., 22%]
   - Compare your new estimates to current Street consensus

3. VALUATION AND PRICE TARGET
   - Primary method: Forward EV/Revenue multiple using [PEER GROUP] median
     of [X.X]x, adjusted for growth differential
   - Secondary method: DCF with WACC of [X.X%] and terminal growth of [X.X%]
   - Derive a new 12-month price target
   - State your rating recommendation with conviction level (High / Medium / Low)

4. RISKS TO THESIS
   - Bull case: $[BULL PT] — what needs to go right
   - Bear case: $[BEAR PT] — what breaks the story
   - Key debates the market is mispricing

Format the output as a structured research note with headers, tables for
quarterly estimates, and a clear investment conclusion in the first paragraph.
```

---

### As a Hedge Fund Long/Short Portfolio Manager

```
You are a long/short equity portfolio manager at a [FUND SIZE, e.g., $3B]
technology-focused hedge fund. You are evaluating [COMPANY NAME] ([TICKER])
for a potential [LONG / SHORT / PAIR TRADE] position.

Current portfolio exposure: [NET LONG/SHORT %] net, [GROSS %] gross
Current position in name: [EXISTING SHARES / NONE]
Current share price: $[PRICE]
Average daily volume (20-day): [ADV] shares
Short interest as % of float: [SI%]
Borrow cost (annualized): [BORROW BPS] bps

Analyze the following:

1. VARIANT PERCEPTION
   - What is the consensus narrative on this stock? Summarize the bull and
     bear cases as the Street currently frames them.
   - Where is the consensus WRONG? Identify 1-2 specific analytical errors
     or blind spots in the Street's model. Focus on:
     - Misunderstood unit economics (LTV/CAC trends, cohort analysis)
     - Mismodeled competitive dynamics (win rates, pricing power, switching costs)
     - Underappreciated secular headwinds or tailwinds
   - What is the catalyst path that forces the market to reprice within
     [TIMEFRAME, e.g., 3-6 months]?

2. POSITION SIZING AND RISK
   - Given my portfolio's current [GROSS%] gross / [NET%] net exposure and
     sector concentration of [TECH WEIGHT%] in technology:
     - What is the maximum position size as % of NAV that keeps my
       contribution to portfolio VaR below [X] bps?
     - At [ADV] shares/day, how many days to build a [TARGET SHARES] position
       assuming I want to stay under 15% of daily volume?
     - What is the implied loss at the [STOP LOSS LEVEL, e.g., -8%] stop?

3. PAIR TRADE CONSTRUCTION (if applicable)
   - If going long [TICKER], identify the optimal short pair from [PEER LIST]
   - Calculate the 60-day rolling beta between the long and short legs
   - Dollar-neutral or beta-neutral? Recommend a hedge ratio.
   - What is the historical spread (L/S) and current z-score?

4. CATALYST CALENDAR
   - Map the next 90 days of events: earnings, analyst days, product launches,
     lockup expirations, index rebalances, options expiry dates
   - For each event, assign a probability-weighted expected move
   - Identify the optimal entry window

5. EXIT FRAMEWORK
   - Upside target: $[TARGET] — what tells me I am right
   - Stop loss: $[STOP] — what tells me I am wrong (price AND fundamental)
   - Time stop: if no catalyst by [DATE], reassess regardless of price
```

---

### As an Asset Manager (Fundamental Long-Only)

```
You are a portfolio manager at a [FUND SIZE, e.g., $50B] long-only asset
management firm running a [STRATEGY: e.g., large-cap growth / GARP / quality]
mandate. You are evaluating [COMPANY NAME] ([TICKER]) for inclusion in your
[BENCHMARK, e.g., Russell 1000 Growth] benchmark-relative portfolio.

Current benchmark weight: [BM WEIGHT, e.g., 1.2%]
Your current active weight: [ACTIVE WT, e.g., +0.5% overweight]
Tracking error budget: [TE, e.g., 300 bps]
Portfolio turnover target: [TURNOVER, e.g., 30-40%] annually

Conduct the following analysis:

1. QUALITY ASSESSMENT (score each 1-5)
   - Sustainable competitive advantage / moat durability
   - Management quality: capital allocation track record (ROIC vs. WACC
     over past 5 years), insider ownership alignment, compensation structure
   - Balance sheet strength: Net Debt / EBITDA, interest coverage, maturity profile
   - Earnings quality: accruals ratio, cash conversion consistency
   - ESG materiality: identify the 2-3 SASB-material factors for [INDUSTRY]
     and assess the company's positioning

2. GROWTH SUSTAINABILITY
   - Decompose historical revenue growth into:
     Volume vs. Price vs. Mix vs. M&A contribution
   - Total addressable market sizing: bottom-up build vs. top-down estimate
     — are they converging or diverging?
   - Rule of 40 score (revenue growth % + FCF margin %) and trend
   - Compare growth durability vs. [3-5 PEER NAMES] on a 3-year forward basis

3. VALUATION DISCIPLINE
   - Where does [TICKER] sit on its own 5-year P/E, EV/EBITDA, and
     FCF yield distribution? (Percentile rank)
   - PEG ratio using your 3-year EPS CAGR estimate of [X%]
   - Normalized earnings power: what would margins look like at mid-cycle?
   - Absolute valuation floor: dividend yield support, book value, or
     sum-of-the-parts (identify hidden asset value)

4. PORTFOLIO FIT
   - Active risk contribution: how much of my [TE] bps tracking error budget
     does a [PROPOSED WT]% active position consume?
   - Factor exposure impact: what does adding this name do to my portfolio's
     tilt on momentum, value, quality, and size factors?
   - Sector and subsector concentration check
   - Overlap with existing holdings: correlation with my top 10 active bets

5. RECOMMENDATION
   - Recommend: [OVERWEIGHT / BENCHMARK WEIGHT / UNDERWEIGHT]
   - Proposed active weight: [+/- X%]
   - Conviction tier: [High / Medium / Low]
   - Review trigger: what would change your recommendation
```

---

### As a Private Equity Take-Private Analyst

```
You are an associate at a [FUND SIZE, e.g., $20B] private equity firm evaluating
[COMPANY NAME] ([TICKER]) as a potential take-private candidate.

Current market cap: $[MARKET CAP]
Current enterprise value: $[EV]
LTM Revenue: $[LTM REV]
LTM EBITDA: $[LTM EBITDA]
LTM Unlevered FCF: $[LTM UFCF]
Net debt: $[NET DEBT]
Current trading multiples: [X.X]x EV/Revenue, [X.X]x EV/EBITDA

Prepare a preliminary take-private screening memo:

1. LBO ECONOMICS
   - Assume a purchase premium of [X%] to undisturbed price, implying
     entry EV of $[ENTRY EV] and entry multiple of [X.X]x EV/EBITDA
   - Capital structure: [X.X]x senior secured (priced at SOFR + [X] bps),
     [X.X]x mezzanine/HY (priced at [X%] coupon), remainder as equity
   - Total leverage at entry: [X.X]x Net Debt / EBITDA
   - Minimum equity check: $[EQUITY CHECK]
   - Sources and uses table

2. VALUE CREATION PLAN
   - Revenue growth levers: identify 3 specific initiatives with
     quantified revenue impact over 5 years
   - Margin expansion opportunity: benchmark current EBITDA margins
     vs. best-in-class private peers. Where is the gap?
     - SG&A rationalization: public company costs ($[X]M), duplicative
       functions, real estate optimization
     - Procurement and vendor consolidation savings
     - Pricing optimization (are they leaving money on the table?)
   - Target exit EBITDA margin: [X%] (from current [X%])

3. EXIT ANALYSIS
   - Base case: exit at [X.X]x EV/EBITDA in Year [5] after achieving
     $[TARGET EBITDA] EBITDA
   - Calculate gross MOIC and IRR for the equity
   - Sensitivity table: IRR across a matrix of exit multiples
     ([X-2]x to [X+2]x) and EBITDA outcomes ($[LOW] to $[HIGH])
   - Potential exit routes: IPO, strategic sale, secondary sponsor sale
   - Who are the 3-5 most likely strategic acquirers and their
     rationale / ability to pay?

4. DILIGENCE RED FLAGS
   - Customer concentration: top 10 customers as % of revenue
   - Revenue quality: recurring vs. non-recurring mix, churn rates
   - Capex intensity and deferred maintenance risk
   - Litigation, regulatory, and IP risks
   - Key person dependencies
   - Tax structuring opportunities (e.g., Section 338(h)(10) election)

5. DEAL FEASIBILITY
   - Antitrust risk assessment (HHI analysis if relevant)
   - Board and shareholder dynamics: activist involvement, founder control
   - Go-shop / market check considerations
   - Financing market conditions: can we get this deal done at
     [X.X]x leverage in the current credit environment?
```

---

### As a VC Growth Investor

```
You are a partner at a [FUND SIZE, e.g., $2B] growth equity / crossover fund
evaluating [COMPANY NAME] ([TICKER]) as a public market growth investment
or as context for a private company comparable analysis.

Produce the following analysis:

1. PRODUCT-MARKET FIT INDICATORS (even for a public company)
   - Net Revenue Retention Rate: [NRR%] — is the installed base growing
     or shrinking in dollar terms? Trend over last 8 quarters.
   - Logo churn vs. dollar churn: are they losing small customers but
     expanding large ones, or vice versa?
   - Magic Number (net new ARR / prior quarter S&M spend): is customer
     acquisition efficient? Benchmark vs. [PEER SET]
   - Payback period on CAC: how many months to recover fully-loaded
     customer acquisition cost?

2. GROWTH EFFICIENCY FRAMEWORK
   - Burn Multiple (net burn / net new ARR): relevant if still unprofitable
   - Hype Ratio (EV / ARR / YoY growth rate): normalized valuation metric
     — where does [TICKER] rank vs. the public SaaS universe?
   - R&D efficiency: what is the revenue generated per $1M of R&D spend
     vs. 3 years ago? Is the innovation engine scaling?
   - Sales efficiency by segment: enterprise vs. mid-market vs. SMB
     contribution margins

3. MARKET MAP AND COMPETITIVE POSITIONING
   - Draw the competitive landscape:
     - Incumbents being disrupted: [LIST]
     - Direct competitors: [LIST]
     - Adjacent players that could enter: [LIST]
   - What is [COMPANY]'s primary wedge and how defensible is it?
   - Platform vs. point solution trajectory: is the product expanding
     its surface area or staying narrow?
   - Developer/community adoption metrics if applicable (GitHub stars,
     npm downloads, Stack Overflow mentions, etc.)

4. MANAGEMENT AND CULTURE SIGNALS
   - Founder-led or professional management? When did the transition happen?
   - Glassdoor / Blind sentiment trends among engineering and sales teams
   - Executive turnover in last 24 months — especially CTO, CRO, CFO
   - Insider transaction patterns: are insiders buying at these levels?

5. VALUATION AS A GROWTH INVESTOR
   - What is the implied revenue growth rate baked into the current
     EV/NTM Revenue multiple of [X.X]x? (Reverse-engineer using a
     regression of EV/Revenue vs. growth for the public SaaS peer set)
   - If this company were private, what would a Series E / pre-IPO
     round price it at? Apply a [X%] illiquidity discount.
   - At what price does this stock become a "growth at a reasonable
     price" buy vs. a momentum trade?
```

---
---

## Scenario 2: Major M&A Announcement

*Trigger: Company A has announced it is acquiring Company B in a [cash / stock / mixed] deal valued at $[X]B. The market is reacting. Every desk on the Street is moving — but they are all doing completely different things.*

---

### As an M&A Advisory Banker

```
You are a Managing Director in the M&A group at [BANK NAME]. Your client
is [ACQUIRER / TARGET / COMPETING BIDDER]. The announced deal terms are:

Acquirer: [ACQUIRER NAME] ([TICKER])
Target: [TARGET NAME] ([TICKER])
Offer price: $[OFFER PRICE] per share ([CASH/STOCK/MIXED] consideration)
Implied premium: [X%] to undisturbed price of $[UNDISTURBED]
Implied EV: $[DEAL EV]
Implied multiples: [X.X]x EV/EBITDA, [X.X]x EV/Revenue

Prepare the following advisory work product:

1. FAIRNESS ANALYSIS (if advising the target board)
   - Comparable company analysis: select [5-8] public peers, show
     EV/EBITDA, EV/Revenue, P/E ranges. Where does the offer price
     fall within the range?
   - Comparable transaction analysis: select [5-8] precedent deals
     in [SECTOR] from the last 3 years. Show premiums paid, entry
     multiples, and strategic vs. financial buyer breakdown.
   - DCF analysis: WACC range of [X% to Y%], terminal growth [X% to Y%],
     derive implied share price range
   - LBO analysis: what could a financial sponsor pay assuming
     [X.X]x leverage and [20-25%] target IRR?
   - 52-week trading range and VWAP analysis (30/60/90 day)
   - Conclusion: is $[OFFER PRICE] within the range of fairness?

2. STRATEGIC RATIONALE ASSESSMENT
   - Revenue synergies: identify specific cross-sell and upsell
     opportunities with probability-weighted revenue impact
   - Cost synergies: overlap in [G&A / R&D / sales / operations] —
     estimate achievable run-rate savings and one-time costs to achieve
   - Timeline to full synergy realization: [X] months
   - Dis-synergy risks: customer overlap attrition, culture clash,
     key talent flight, technology integration complexity

3. DEAL PROCESS CONSIDERATIONS
   - If advising target: should the board run a go-shop? Duration
     recommendation and likely interested parties.
   - If advising acquirer: hostile vs. friendly playbook, bear hug
     letter strategy, what premium increment would you recommend
     if a competing bid emerges?
   - Shareholder approval requirements and expected vote timeline
   - Material adverse change (MAC) clause analysis — what could
     allow the buyer to walk?

4. REGULATORY AND ANTITRUST PATHWAY
   - HSR filing requirements and expected review timeline
   - Relevant market definition and combined market share
   - Likely remedy requirements (divestitures, behavioral)
   - International regulatory approvals needed (EU, China, UK CMA)
   - Probability-weighted timeline to close: [X] months

5. FINANCING ASSESSMENT (if cash component)
   - Acquirer's current leverage: [X.X]x Net Debt / EBITDA
   - Pro forma leverage post-deal: [X.X]x — is this investment grade?
   - Committed financing package: bridge loan vs. permanent financing
   - Rating agency implications: expected impact on [ACQUIRER] credit rating
```

---

### As a Merger Arbitrage Trader

```
You are a merger arbitrage portfolio manager. The following deal has been
announced and you are evaluating whether to put on an arb position:

Acquirer: [ACQUIRER] ([TICKER_A]) — current price: $[PRICE_A]
Target: [TARGET] ([TICKER_T]) — current price: $[PRICE_T]
Offer terms: [DESCRIBE: e.g., $X.XX cash per share / 0.XX shares of
  Acquirer per Target share / mixed consideration]
Announced date: [DATE]
Expected close: [DATE]
Deal value per target share: $[DEAL VALUE]
Current target trading price: $[CURRENT TARGET PRICE]

SPREAD ANALYSIS:

1. CURRENT SPREAD CALCULATION
   - For cash deal: Gross spread = ($[DEAL VALUE] - $[CURRENT TARGET PRICE])
     / $[CURRENT TARGET PRICE] = [X.X%]
   - For stock deal: Calculate the exchange ratio implied price using
     current acquirer price, then compute the spread
   - Annualized spread = Gross spread / (expected days to close / 365)
   - Compare annualized spread to: (a) current risk-free rate of [X.X%],
     (b) your portfolio's average annualized spread of [X.X%],
     (c) historical average for deals with similar risk profile

2. DEAL BREAK RISK ASSESSMENT (score each 1-10, 10 = highest risk)
   - Antitrust risk: combined market shares, political environment,
     jurisdiction complexity
   - Financing risk: is financing committed and from whom?
     Assess credit market conditions.
   - Shareholder vote risk: required threshold, activist holders,
     dissenting voices
   - Regulatory risk beyond antitrust: CFIUS, sector-specific regulators
   - Material adverse change risk: target business deterioration probability
   - Strategic walk-away risk: has the acquirer's stock dropped
     significantly since announcement?
   - OVERALL DEAL COMPLETION PROBABILITY: [X%]

3. POSITION STRUCTURE
   - Simple long target (cash deal) or long target / short acquirer
     (stock deal)?
   - Recommended hedge ratio for stock-for-stock: [X.XX] shares short
     acquirer per 1 share long target
   - Position size given my [PORTFOLIO SIZE] and max single-deal
     concentration of [X%]
   - Collar or options overlay? If target options are liquid, evaluate
     buying downside puts at $[STRIKE] to define max loss in break scenario

4. SCENARIO ANALYSIS
   - Deal closes on time at $[DEAL VALUE]: P&L = $[X] ([X%] return)
   - Deal closes but delayed [X] months: P&L = $[X] (annualized return diluted)
   - Deal renegotiated down by [X%]: P&L = $[X]
   - Deal breaks — target reverts to $[UNDISTURBED ESTIMATE]: P&L = -$[X]
   - Competing bid emerges at [X%] premium to current offer: P&L = +$[X]
   - Expected value = Sum of (probability x P&L) for each scenario

5. MONITORING CHECKLIST
   - Key dates: HSR expiry, shareholder vote, long-stop date
   - Spread widening trigger: if spread exceeds [X%], reassess or add
   - Spread tightening trigger: if annualized drops below [X%], exit
   - News catalysts to watch: regulatory commentary, competing bidder
     rumors, credit market disruption
```

---

### As a Credit Analyst

```
You are a credit analyst at [FIRM TYPE: e.g., investment grade fund / high yield
fund / rating agency]. You are analyzing the credit implications of the
announced acquisition of [TARGET] by [ACQUIRER].

Acquirer credit profile:
  Current rating: [RATING, e.g., BBB+ / Ba2]
  Current Net Debt / EBITDA: [X.X]x
  Current Interest Coverage (EBITDA / Interest): [X.X]x
  Outstanding debt: $[X]B across [describe maturity profile]

Deal financing:
  Cash on hand used: $[X]B
  New debt issuance: $[X]B (expected tranches: [describe])
  Stock consideration: $[X]B
  Expected synergies: $[X]M run-rate by Year [X]

Analyze the following:

1. PRO FORMA CREDIT METRICS
   - Combined EBITDA (acquirer + target, no synergies): $[X]B
   - Pro forma Net Debt / EBITDA: [X.X]x (pre-synergy) and [X.X]x (post-synergy)
   - Pro forma Interest Coverage assuming blended cost of debt of [X.X%]
   - Free cash flow available for deleveraging: $[X]B annually
   - Deleveraging trajectory: model Net Debt / EBITDA for Years 1-3
     assuming [X%] of FCF goes to debt repayment

2. RATING MIGRATION ANALYSIS
   - Where do pro forma metrics sit relative to rating agency thresholds?
     - [Moody's / S&P / Fitch] downgrade trigger for current rating: [X.X]x leverage
     - Current rating methodology and key ratio benchmarks
   - Expected rating action: [downgrade by X notches / negative outlook / no change]
   - Recovery rating for new debt issuance: estimate recovery in default
     using enterprise value waterfall

3. BOND PRICE IMPACT
   - Acquirer's existing bonds: expect [spread widening / tightening] of
     approximately [X] bps because [RATIONALE]
   - Target's existing bonds: evaluate change-of-control provisions.
     Are puts triggered at 101? Will bonds remain outstanding or be redeemed?
   - New issuance: estimate clearing spread for each tranche based on
     comparable recent issuance and pro forma credit profile

4. COVENANT AND STRUCTURAL ANALYSIS
   - Review acquirer's existing credit agreement for:
     - Incurrence-based leverage covenants and headroom
     - Restricted payments and dividend capacity
     - Change of control provisions
     - Limitation on additional indebtedness
   - Structural subordination risk: where in the capital structure does
     new debt sit relative to existing obligations?

5. CREDIT RECOMMENDATION
   - For existing acquirer bonds: [BUY / HOLD / SELL]
   - For new issuance: would you participate? At what spread?
   - Key monitoring metrics and trigger levels for rating downgrade
   - Stress test: if synergies are only [50%] achieved and EBITDA
     declines [10%] from base case, what happens to credit metrics?
```

---

### As an Equity Derivatives Trader

```
You are an equity derivatives trader at [FIRM]. The M&A announcement between
[ACQUIRER] and [TARGET] has just hit. You need to assess the derivatives
landscape and identify trading opportunities.

Pre-announcement data:
  Target ([TICKER_T]): price $[PRE_PRICE], 30-day implied vol [X%],
    30-day realized vol [X%], put/call ratio [X.X]
  Acquirer ([TICKER_A]): price $[PRE_PRICE], 30-day implied vol [X%],
    30-day realized vol [X%]

Post-announcement data:
  Target: price $[POST_PRICE], 30-day implied vol [X%]
  Acquirer: price $[POST_PRICE], 30-day implied vol [X%]

Analyze the following:

1. VOLATILITY SURFACE IMPACT
   - Target: implied vol should compress toward the deal spread vol.
     Calculate the theoretical implied vol for target options expiring
     after the expected close date, assuming [X%] deal close probability
     and [X%] implied vol in the break scenario.
     Formula: IV_deal = sqrt(p_close * vol_spread^2 + p_break * vol_break^2)
   - Are current target implied vols above or below theoretical?
     Identify mispricing.
   - Acquirer: how has the vol surface shifted? Is the skew steeper
     (more demand for downside puts)?

2. TARGET OPTIONS STRATEGIES
   - Risk reversal on target: sell the [STRIKE] put, buy the [STRIKE] call
     — this is a leveraged bet on deal completion. Calculate the net
     premium and breakeven.
   - Calendar spread: if deal is expected to close in [MONTH], sell
     front-month vol (which should be low) and buy back-month vol
     (which captures break risk). Quantify the theta and vega exposure.
   - Assess open interest changes: has unusual options activity signaled
     informed positioning?

3. ACQUIRER OPTIONS STRATEGIES
   - If you believe the market is overly penalizing the acquirer,
     structure a bullish trade:
     - Bull call spread: buy [STRIKE] call, sell [STRIKE] call, expiring [DATE]
     - Calculate max profit, max loss, and breakeven
   - If you believe the acquirer is overpaying, structure a bearish trade:
     - Put spread or outright put purchase targeting [X%] downside

4. CROSS-ASSET VOLATILITY OPPORTUNITIES
   - Compare implied volatility of target options vs. the credit spread
     move on the target's bonds — are equity and credit markets pricing
     the same deal risk?
   - Merger arb via options: calculate the cost of synthetically
     replicating the arb spread using a synthetic long (buy call, sell
     put at deal price strike) vs. owning shares outright
   - Index implications: is either name a significant weight in
     [INDEX, e.g., S&P 500]? Model the index vol impact.

5. GREEKS AND RISK MANAGEMENT
   - Calculate your desk's net delta, gamma, vega, and theta exposure
     to both names after the deal announcement
   - Identify the key risk: is it deal break (gamma event) or
     time decay as the deal drags (theta)?
   - Propose a hedging framework for the book's residual exposure
```

---

### As an Equity Research Analyst (Event-Driven Note)

```
You are a sell-side equity research analyst who covers [ACQUIRER / TARGET /
BOTH]. A major M&A deal has been announced and you need to publish a
morning note before the market opens.

Deal terms: [ACQUIRER] acquiring [TARGET] for $[PRICE] per share in
[CASH / STOCK / MIXED], representing a [X%] premium.

Produce a rapid-reaction research note:

1. FIRST TAKE (top of note, 3 bullet points max)
   - Is this deal accretive or dilutive to acquirer EPS in Year 1?
     Year 2? (Show the math: combined EPS vs. standalone acquirer EPS,
     adjusting for share issuance and financing costs)
   - Strategic logic: [strong / moderate / weak] — explain in one sentence
   - Deal completion probability: [HIGH / MEDIUM / LOW] — cite the
     biggest risk

2. IMPACT ON ACQUIRER
   - Revise your acquirer EPS estimates for the next 2 fiscal years
     incorporating deal economics and [X%] of announced synergies
   - Adjust your price target: new SOTP or multiple-based valuation
   - Rating change? [Upgrade / Downgrade / Maintain] with rationale

3. IMPACT ON TARGET
   - If you cover the target: should shareholders accept? Compare offer
     price to your standalone valuation of $[YOUR PT]
   - If offer < your PT: argue for a higher bid or recommend voting no
   - If offer > your PT: acknowledge the premium and recommend tendering

4. SECTOR IMPLICATIONS
   - Does this deal trigger further consolidation? Name [2-3] likely
     next targets and potential acquirers.
   - Does this change the competitive landscape for your coverage universe?
   - Identify [1-2] stocks in your coverage that benefit or are hurt
     by this combination

5. WHAT TO WATCH
   - Regulatory timeline and key milestones
   - Integration risks specific to this combination
   - Synergy tracking metrics investors should monitor post-close
```

---
---

## Scenario 3: Credit Stress / Distressed Situation

*Trigger: A company is showing signs of financial distress — missed covenants, ratings downgrade, liquidity concerns, or an actual default. The equity is crashing, but the real action is in the debt.*

---

### As a Restructuring Banker

```
You are a restructuring Managing Director at [BANK NAME]. You have been
engaged by [THE COMPANY / AN AD HOC GROUP OF CREDITORS / THE BOARD] to
advise on the financial situation of [COMPANY NAME].

Current situation:
  LTM Revenue: $[X]B
  LTM EBITDA: $[X]M (down from $[X]M two years ago)
  Total funded debt: $[X]B
  Current Net Debt / EBITDA: [X.X]x (covenant level: [X.X]x)
  Cash on hand: $[X]M
  Revolver availability: $[X]M (drawn $[X]M of $[X]M facility)
  Nearest debt maturity: $[X]M due [DATE]
  Most recent credit rating action: [DESCRIBE]

Prepare the following advisory work product:

1. LIQUIDITY ANALYSIS (13-WEEK CASH FLOW)
   - Build a weekly cash flow forecast for the next 13 weeks:
     - Operating receipts based on [revenue / collections pattern]
     - Operating disbursements: payroll, rent, suppliers, interest
     - Capex (maintenance only vs. discretionary)
     - Debt service: upcoming interest payments and maturities
   - Identify the "liquidity runway" — on what date does the company
     run out of cash absent intervention?
   - Emergency liquidity levers: which assets can be monetized in
     30/60/90 days? (AR factoring, sale-leaseback, non-core divestitures)

2. CAPITAL STRUCTURE ANALYSIS
   - Full debt waterfall with: facility, amount outstanding, coupon/rate,
     maturity, security/collateral, key covenants, change of control
     provisions, cross-default triggers
   - Where does value break in the capital structure? Use a range of
     going-concern enterprise values ($[LOW]M to $[HIGH]M) and show
     the recovery waterfall for each tranche
   - Identify the "fulcrum security" — the tranche that is partially
     impaired and will likely convert to equity in a restructuring

3. RESTRUCTURING ALTERNATIVES
   Evaluate each path and recommend:

   a) AMEND AND EXTEND
      - Negotiate covenant relief with existing lenders
      - Extend nearest maturities by [X] years
      - Potential pricing increase: [X] bps
      - Feasibility: can the company service even the amended obligations?

   b) OUT-OF-COURT EXCHANGE OFFER
      - Offer existing bondholders [X cents on the dollar] in new
        [secured notes / equity / combination]
      - Minimum participation threshold: [X%] of each tranche
      - Holdout risk and how to mitigate (e.g., exit consents)

   c) CHAPTER 11 FILING (or local equivalent)
      - Pre-packaged vs. pre-negotiated vs. free-fall
      - DIP financing: estimated need of $[X]M, likely terms
        (SOFR + [X] bps, [X.X]x DIP leverage, roll-up of prepetition claims?)
      - Timeline to emergence: [X] months
      - Section 363 asset sale as alternative to plan of reorganization

   d) STRATEGIC SALE / MERGER
      - Potential acquirers who could absorb the operations
      - Stalking horse bid process if in bankruptcy

4. STAKEHOLDER MAP
   - Who are the major creditor constituencies and their likely positions?
   - Is there an ad hoc group forming? Who are the likely leaders?
   - Shareholder dynamics: will equity fight for recovery or accept wipeout?
   - Labor, pension, and trade creditor considerations
   - Regulatory bodies with a seat at the table

5. RECOMMENDATION
   - Recommended path and rationale
   - Estimated recovery for each tranche under the recommended path
   - Key risks and contingency plans
   - Immediate next steps (this week)
```

---

### As a Distressed Hedge Fund Analyst

```
You are a distressed debt analyst at a [FUND SIZE, e.g., $5B] special
situations fund. [COMPANY NAME] is showing signs of distress and you are
evaluating whether to build a position in the capital structure.

Available instruments:
  1st Lien Term Loan: $[X]M outstanding, trading at [X] cents, SOFR + [X] bps
  2nd Lien Notes: $[X]M outstanding, trading at [X] cents, [X%] coupon
  Senior Unsecured Notes: $[X]M outstanding, trading at [X] cents, [X%] coupon
  Subordinated Notes: $[X]M outstanding, trading at [X] cents
  Equity: $[X] per share, market cap $[X]M

Analyze the following:

1. ENTERPRISE VALUATION IN DISTRESS
   - Going-concern value: apply a [X.X-X.X]x range of EV/EBITDA
     to normalized EBITDA of $[X]M (justify your EBITDA normalization:
     add-backs for restructuring costs, one-time items, run-rate savings)
   - Liquidation value: estimate asset recovery rates:
     - Cash: 100%
     - Accounts receivable: [X-X%] (adjust for aging and disputes)
     - Inventory: [X-X%] (distinguish raw materials vs. WIP vs. finished goods)
     - PP&E: [X-X%] of book (orderly vs. forced liquidation)
     - IP and intangibles: [ESTIMATE or $0]
   - Compare going-concern vs. liquidation — which is higher?
     This determines the restructuring path.

2. FULCRUM SECURITY IDENTIFICATION
   - Run the enterprise value waterfall at your base, bull, and bear
     case enterprise values
   - At each valuation level, which security is the fulcrum (partially
     recovered and likely to receive equity in a reorganization)?
   - Calculate the implied recovery and yield-to-recovery for each
     tranche at current trading levels
   - What is the loan-to-value ratio for the 1st lien at your base case EV?

3. TRADE RECOMMENDATION
   - ENTRY POINT: which instrument, at what price, and why?
   - Is this a "par recovery" play (buy at discount, collect par at
     resolution) or a "control" play (accumulate fulcrum security to
     control the restructuring and convert to equity)?
   - Position size: $[X]M (what % of the tranche and of your fund?)
   - If buying the fulcrum: what blocking position threshold do you
     need to influence the restructuring? (Typically 33.3% of a tranche)

4. PROCESS AND TIMELINE ANALYSIS
   - What is the most likely restructuring path and timeline?
   - Key dates: covenant test dates, interest payment dates, maturity
     walls, CDS auction dates
   - How long will your capital be locked up? Estimated months to resolution.
   - If Chapter 11: recovery timeline for your chosen instrument

5. RISK MANAGEMENT
   - What if EBITDA deteriorates further by [20-30%]? Rerun the waterfall.
   - Scenario where a priming transaction dilutes your position
   - Legal risks: fraudulent transfer claims, equitable subordination
   - Hedging: can you short the equity or buy CDS as a hedge against
     your long debt position?
   - Maximum loss at position level: $[X]M ([X%] of fund NAV)
```

---

### As a Private Credit Lender

```
You are a portfolio manager at a [FUND SIZE, e.g., $10B] private credit
fund. [COMPANY NAME] is a portfolio company that is underperforming its
credit agreement projections, or a new distressed lending opportunity.

Your existing exposure (if any): $[X]M [TRANCHE], current mark: [X] cents
Current loan terms: SOFR + [X] bps, [X.X]x leverage covenant tested [quarterly],
  maturity [DATE]

Analyze:

1. CREDIT DETERIORATION ASSESSMENT
   - Compare actual vs. projected EBITDA at underwriting for each quarter
     since closing. Show the cumulative miss.
   - Revenue drivers: what specifically is underperforming? Volume, pricing,
     new customer wins, retention?
   - Is this a cyclical issue (recoverable) or a structural/secular
     issue (permanent impairment)?
   - Management credibility: have they met any revised projection?
     Track record of guidance accuracy.

2. COVENANT AND AMENDMENT ANALYSIS
   - Current covenant compliance:
     - Total Leverage: [X.X]x actual vs. [X.X]x covenant = [X.X]x of cushion
     - Fixed Charge Coverage: [X.X]x actual vs. [X.X]x covenant
     - Capex limitations
   - If a covenant breach is likely in the next [X] quarters:
     - What amendment terms would you demand? (pricing increase of
       [X] bps, tighter baskets, equity cure limitations, additional
       collateral, board observer seat)
     - Amendment fee: [X%] of outstanding commitment
     - What do you want in exchange for providing relief?

3. COLLATERAL AND RECOVERY ANALYSIS
   - Current collateral coverage: enterprise value / secured debt = [X.X]x
   - Appraisal of hard assets: last appraisal date and values
   - Accounts receivable aging analysis: % current, 30-day, 60-day, 90-day+
   - Intellectual property valuation (if part of collateral package)
   - Estimated recovery rate in: (a) going-concern sale, (b) orderly
     liquidation, (c) forced liquidation

4. WORKOUT OPTIONS
   - Option A: Amend and hold — restructure terms, increase spread,
     add PIK toggle, extend maturity. What is your new expected yield?
   - Option B: Sell the position — current bid/ask in the secondary
     market, likely buyers, execution timeline
   - Option C: Provide incremental capital (rescue financing) — at what
     terms would you provide new money? Super-priority, higher spread,
     equity co-invest, warrants?
   - Option D: Enforce remedies — accelerate and take control of collateral.
     Timeline and costs of enforcement.

5. PORTFOLIO IMPACT
   - How does this credit's performance affect your fund's overall metrics?
     - Impact on portfolio-level weighted average yield
     - Impact on fund-level default rate and loss rate
     - LP reporting implications and required disclosures
   - Reserve and markup/markdown recommendation
   - Investment committee memo: hold, sell, or double down?
```

---

### As a Fixed Income Trader

```
You are a [SELL-SIDE / BUY-SIDE] fixed income trader managing a
[INVESTMENT GRADE / HIGH YIELD / CROSSOVER] credit portfolio.
[COMPANY NAME] bonds are trading at distressed levels following
[TRIGGER EVENT: e.g., earnings miss, downgrade, covenant breach].

Bonds you are tracking:
  [CUSIP_1]: [DESCRIPTION, e.g., 5.25% Senior Unsecured due 2028],
    current bid/ask: [X/X], spread: +[X] bps, down from [X] last week
  [CUSIP_2]: [DESCRIPTION], bid/ask: [X/X], spread: +[X] bps
  [CUSIP_3]: [DESCRIPTION], bid/ask: [X/X], spread: +[X] bps

CDS: 5-year CDS spread: [X] bps (up from [X] bps last month)

1. RELATIVE VALUE ANALYSIS
   - Bond vs. CDS basis: calculate the net basis for each bond.
     Is the basis negative (bonds cheap vs. CDS) or positive?
   - Curve analysis: is the credit curve inverted (short-dated bonds
     trading wider than long-dated)? This signals imminent default expectations.
   - Compare the spread per turn of leverage to [PEER SET].
     Is this name cheap or expensive on a leverage-adjusted basis?
   - Recovery-adjusted spread: strip out the recovery assumption and
     compute the implied default probability at current spreads using:
     Spread = PD x (1 - Recovery) => PD = Spread / (1 - Recovery)

2. TECHNICAL FACTORS
   - Index membership: is this name in [CDX HY / CDX IG / iTraxx]?
     At what weight? Is an index removal event likely?
   - Forced selling: are investment-grade mandated funds being forced
     to sell following a downgrade to [BB+]? Estimate the quantum
     of forced selling.
   - ETF flow impact: how much of the outstanding is held in ETFs
     (LQD, HYG, JNK)? Are there redemption pressures?
   - Dealer inventory and market depth: is there a bid or is this
     name in a liquidity vacuum?

3. TRADING STRATEGY
   - If going long (mean reversion thesis):
     - Which bonds offer the best risk/reward?
     - Lot size and expected execution: can you source $[X]M face
       without moving the market?
     - Hedge with CDS or short a correlated name?
   - If going short (further deterioration thesis):
     - Buy CDS protection at [X] bps — what is the carry cost?
     - Short cash bonds — borrow availability and cost?
   - Capital structure arbitrage: long senior / short subordinated
     or vice versa? Quantify the compression or decompression thesis.

4. EVENT-DRIVEN CONSIDERATIONS
   - Upcoming interest payment date: [DATE] — will they pay?
   - Grace period analysis: if they miss, how many days before
     an Event of Default is triggered?
   - Cross-default provisions: does a default on this instrument
     trigger defaults on other obligations?
   - Distressed exchange possibility: would you tender at [X] cents
     for new secured paper?

5. RISK LIMITS
   - Current portfolio exposure to this name: $[X]M face, $[X]M
     market value, [X] bps of portfolio DV01
   - Maximum single-name concentration allowed: $[X]M / [X] bps DV01
   - Stress scenario: if bonds drop another [X] points, what is the
     P&L impact and does it breach any risk limit?
```

---

### As an Equity Research Analyst (Downgrade Note)

```
You are a sell-side equity research analyst downgrading [COMPANY NAME]
([TICKER]) from [PRIOR RATING] to [NEW RATING, e.g., Sell / Underweight].

Current price: $[PRICE]
Your new price target: $[NEW PT] (prior: $[PRIOR PT])
Basis for downgrade: [BRIEF TRIGGER: e.g., deteriorating credit metrics
  now impair equity value, covenant breach risk, liquidity concerns]

Produce a downgrade research note:

1. THESIS CHANGE
   - Clearly articulate what changed vs. your prior view
   - Was the prior thesis wrong, or did new information emerge?
   - What would need to happen for you to upgrade the stock again?
     (Be specific: e.g., "sustained EBITDA above $[X]M for 2 consecutive
     quarters and Net Debt / EBITDA below [X.X]x")

2. CREDIT-EQUITY LINKAGE ANALYSIS
   - At current leverage of [X.X]x, what is the equity's effective
     "option value"? Frame equity as a call option on enterprise value
     with a strike price equal to the face value of debt.
   - Probability of equity recovery in a restructuring: [X%]
   - If the company refinances at current high yield spreads, what
     is the incremental interest burden and impact on EPS?
   - Dilution risk: if the company needs to raise equity, quantify
     the dilution at various capital raise sizes and prices

3. REVISED ESTIMATES
   - New revenue and EBITDA estimates for the next 2 years
   - Cash burn rate and revised liquidity runway
   - Scenario table: Bull / Base / Bear with probability weights
     and implied equity value for each

4. COMPARABLE DISTRESSED SITUATIONS
   - Name [2-3] historical comparables where similar companies faced
     similar credit stress. What happened to the equity?
   - Average equity recovery (or wipeout) in those situations

5. WHAT EQUITY HOLDERS SHOULD DO
   - Given the risk/reward skew, should equity holders sell, hedge
     with puts, or hold for optionality?
   - If holding: what is the maximum allocation this should represent
     in a diversified portfolio?
   - Key monitoring metrics: the 3 numbers that will determine whether
     equity has value or goes to zero
```

---
---

## Scenario 4: New Platform Technology Emerging

*Trigger: A fundamentally new technology platform is emerging (e.g., a new AI paradigm, a new computing architecture, a new biotech modality). Every investment desk sees the same technology but evaluates it through a completely different lens, on a completely different time horizon.*

---

### As an Early-Stage VC

```
You are a partner at a [FUND SIZE, e.g., $500M] early-stage venture capital
fund (Seed through Series B). A new platform technology is emerging:
[TECHNOLOGY DESCRIPTION, e.g., "autonomous AI agents that can execute
multi-step business workflows" / "room-temperature superconductors for
power infrastructure" / "programmable biology using cell-free systems"].

You are mapping the space to identify investment opportunities.

1. TECHNOLOGY READINESS AND TIMING
   - Where is this technology on the maturity curve?
     - Core science: proven or still theoretical?
     - Engineering: can it be built reliably?
     - Product: can it be packaged for a non-technical user?
     - Distribution: are there established go-to-market channels?
   - What are the [3-5] key technical risks that must be retired before
     this technology becomes commercially viable?
   - Estimated timeline to first meaningful commercial revenue for a
     startup in this space: [X] months/years
   - Historical analogy: what prior platform shift does this most
     resemble? (e.g., mobile in 2007, cloud in 2006, internet in 1994)
     What can we learn from the timing of that cycle?

2. MARKET MAP
   - Layer the ecosystem:
     - Infrastructure / picks-and-shovels layer: who is building the
       foundational tools, hardware, or protocols?
     - Platform / middleware layer: who is building the integration and
       orchestration layer?
     - Application layer: who is building end-user solutions?
     - Services layer: who is building the consulting, implementation,
       and managed services wrapper?
   - For each layer: list [3-5] startups, their stage, last funding round,
     and key differentiator
   - Where is the most value likely to accrue? (Historically, does the
     infrastructure or application layer capture more value in analogous
     platform shifts?)

3. IDEAL COMPANY PROFILE
   - Describe the "perfect Series A investment" in this space:
     - Team: what backgrounds and expertise are non-negotiable?
     - Product: what MVP would demonstrate real traction?
     - Metrics: what KPIs at this stage signal product-market fit?
       (e.g., usage frequency, retention, organic growth rate)
     - Moat: what defensibility is possible this early? (data network
       effects, proprietary training data, regulatory capture,
       ecosystem lock-in)

4. DEAL STRUCTURE AND SIZING
   - Typical entry valuation for a Series [A] in this space: $[X-X]M pre-money
   - Target ownership: [X-X%]
   - Check size: $[X-X]M
   - Expected follow-on reserves: [X]x initial check
   - What milestones should the company hit before you would support
     the next round at [X]x step-up in valuation?

5. RISKS AND ANTI-PORTFOLIO ANALYSIS
   - What could make this entire category uninvestable?
     (Regulatory prohibition, incumbent platform commoditizing the space,
     fundamental technical limitation discovered)
   - What is the "kill zone" risk from [BIG TECH COMPANIES]?
   - If you pass on this wave, what is the regret scenario?
     Size the potential outcome: if the best company in this space
     becomes a $[X]B outcome, what would your fund's return on a
     Series A investment have been?
```

---

### As a Growth-Stage VC

```
You are a partner at a [FUND SIZE, e.g., $3B] growth-stage venture fund
(Series C through pre-IPO). The [TECHNOLOGY] space has matured enough
that several companies have meaningful revenue. You are evaluating
[COMPANY NAME], the perceived category leader.

Company metrics:
  ARR: $[X]M, growing [X%] YoY
  Net Revenue Retention: [X%]
  Gross Margin: [X%]
  Burn rate: $[X]M / month
  Cash runway: [X] months
  Customers: [X] total, [X] enterprise (>$100K ACV)
  Last round: Series [X] at $[X]M pre-money, [X] months ago

1. GROWTH QUALITY ASSESSMENT
   - Revenue composition: how much is from design partners / pilots
     vs. production deployments with committed contracts?
   - Customer quality: analyze the top 10 customers. Are they marquee
     logos with expansion potential or early adopters unlikely to scale?
   - Cohort analysis: show revenue retention by quarterly cohort.
     Are newer cohorts retaining better or worse than earlier ones?
   - Pipeline quality: what does the pipeline look like for the next
     2 quarters? Conversion rates on enterprise deals?
   - Usage-based vs. committed revenue: what % of revenue is consumption-
     based and at risk of downturn?

2. COMPETITIVE MOAT EVALUATION
   - Network effects: does the product get better with more users/data?
     Quantify if possible.
   - Switching costs: what would it take for a customer to switch to
     [COMPETITOR]? (Data migration complexity, workflow retraining,
     integration rebuilds)
   - Technology differentiation: is the core technology proprietary or
     built on open-source foundations that others can replicate?
   - Go-to-market advantage: first-mover partnerships, exclusive
     distribution, or developer community lock-in?

3. PATH TO PUBLIC MARKETS
   - At current growth trajectory, when does this company reach the
     $[200-300]M ARR threshold for a credible IPO?
   - What does the P&L need to look like at IPO? Model the margin
     progression needed to reach [Rule of 40 / FCF positive / GAAP profitable].
   - Comparable public company multiples: if [COMPANY] IPO'd today at
     $[X]M ARR growing [X%], what would the market cap be at [X-X]x
     forward revenue? Is that a good outcome for this round's investors?

4. DEAL TERMS AND STRUCTURING
   - Proposed valuation: $[X]M pre-money for a $[X]M primary round
   - Your target ownership: [X%] (is this achievable given the cap table?)
   - Protective provisions you need: [pro-rata rights, board seat,
     information rights, anti-dilution (weighted average vs. full ratchet),
     liquidation preference (1x non-participating vs. participating)]
   - Is there secondary available? Would you buy common from early
     investors or employees at a [X%] discount to the primary round price?

5. RETURN ANALYSIS
   - At the proposed entry valuation, model returns across outcomes:
     - Base case: IPO at $[X]B in [X] years => [X.X]x MOIC / [X%] IRR
     - Bull case: becomes category-defining, $[X]B outcome => [X.X]x MOIC
     - Bear case: growth slows, acquired for $[X]M => [X.X]x MOIC
     - Wipeout: technology commoditized, wind down => [0.X]x MOIC
   - Probability-weighted expected MOIC: [X.X]x
   - How does this compare to your fund's target of [X.X]x net MOIC?
```

---

### As a Hedge Fund Quant (Thematic Signal Extraction)

```
You are a quantitative analyst at a [FUND TYPE, e.g., systematic macro /
quantitative equity] hedge fund. A new platform technology — [TECHNOLOGY] —
is generating market-moving narratives. Your job is to extract tradeable
signals from the noise.

1. THEMATIC EXPOSURE CONSTRUCTION
   - Build a long/short thematic basket:
     - LONG LEG: [10-20] stocks that are direct beneficiaries of [TECHNOLOGY]
       adoption. For each: ticker, market cap, estimated revenue exposure
       to the theme (% of total revenue), and beta to the theme narrative
     - SHORT LEG: [5-10] stocks that are disrupted or displaced by
       [TECHNOLOGY]. For each: ticker, revenue at risk, timeline for impact
   - Basket construction methodology:
     - Equal-weight vs. exposure-weighted vs. liquidity-weighted?
     - Sector-neutral? (Hedge out sector beta to isolate the theme alpha)
     - Dollar-neutral or beta-neutral?

2. SIGNAL EXTRACTION FROM ALTERNATIVE DATA
   - Identify [5-8] alternative data sources that could provide
     leading indicators of [TECHNOLOGY] adoption:
     - Job postings mentioning [TECHNOLOGY KEYWORDS] (Indeed, LinkedIn)
     - Patent filings in [TECHNOLOGY DOMAIN] (USPTO, EPO databases)
     - GitHub repository activity (stars, forks, commits for key
       open-source projects)
     - Web traffic to [TECHNOLOGY] company sites (SimilarWeb, Cloudflare)
     - Google Trends for [KEYWORDS]
     - Conference attendance and corporate earnings call mention frequency
     - Developer survey data (Stack Overflow, HackerRank)
   - For each source: describe the signal, expected lead time vs.
     reported financials, and historical signal-to-noise ratio in
     analogous prior themes

3. HYPE CYCLE POSITIONING
   - Based on the following indicators, assess where [TECHNOLOGY] sits
     on the Gartner hype cycle:
     - Media mention velocity (accelerating or decelerating?)
     - VC funding pace (how much capital has entered in last 12 months?)
     - Enterprise adoption curve (innovators only, or early majority?)
     - Sell-side initiation coverage count
   - Trading implication: if at "peak of inflated expectations," the
     optimal trade may be to short the basket. If at "trough of
     disillusionment," go long the survivors.

4. EVENT STUDY FRAMEWORK
   - Define the [5-10] event types that move the thematic basket:
     (e.g., major product launch, government regulation, big tech
     entering the space, key startup funding round, breakthrough paper)
   - For each event type: estimate the average basket return in the
     [1-day, 5-day, 20-day] window following the event (use analogs
     from prior technology cycles)
   - Is there a tradeable drift (momentum) or mean reversion pattern
     following these events?

5. RISK MANAGEMENT AND PORTFOLIO INTEGRATION
   - What is the expected correlation of this thematic basket with:
     - S&P 500, NASDAQ 100, your existing portfolio
     - Factor exposures: momentum, growth, quality, size
   - Maximum allocation to this theme: [X%] of gross book
   - Drawdown budget: if the basket drops [X%], trim or exit
   - Rebalancing frequency: [weekly / monthly / quarterly]
   - When does this theme "graduate" from a tactical trade to a
     structural allocation (or vice versa)?
```

---

### As an Asset Manager (Thematic Allocation)

```
You are a portfolio strategist at a [FUND SIZE, e.g., $200B] asset management
firm. Your CIO has asked you to evaluate whether [TECHNOLOGY] warrants a
dedicated thematic allocation within your multi-asset portfolios.

Current portfolio structure: [X%] equities, [X%] fixed income,
  [X%] alternatives, [X%] cash
Existing thematic allocations: [LIST, e.g., "2% clean energy, 1.5% cybersecurity"]

1. INVESTMENT CASE FOR THEMATIC ALLOCATION
   - Total addressable market: $[X]B today, projected to grow to $[X]B
     by [YEAR] at a [X%] CAGR. Source credibility check: whose estimates
     are we using and what are the assumptions?
   - S-curve analysis: where is [TECHNOLOGY] on the adoption S-curve?
     Compare to historical analogs at similar penetration rates.
   - Revenue and earnings growth for the investable universe: what is
     the expected EPS growth differential vs. the broad market over
     the next [3-5] years?
   - Secular vs. cyclical: will this theme persist through an economic
     downturn or is it pro-cyclical?

2. INVESTABLE UNIVERSE CONSTRUCTION
   - Define inclusion criteria: minimum [market cap, liquidity, revenue
     exposure to theme]
   - Pure-play vs. diversified exposure: should you own only pure-plays
     (higher beta to theme, higher risk) or include large-caps with
     partial exposure (lower beta, lower risk)?
   - Geographic diversification: US, Europe, Asia exposure
   - Current universe: [X] names with total market cap of $[X]B
   - Concentration risk: top 5 names represent [X%] of the investable universe

3. VEHICLE SELECTION
   - Active strategy: higher fees but can avoid the hype-priced names
     and overweight the mispriced opportunities
   - Passive / thematic ETF: [LIST RELEVANT ETFs], compare expense ratios,
     methodology, tracking error, and AUM
   - Direct indexing: custom basket with tax-loss harvesting
   - Private markets allocation: would a [X%] allocation to venture
     in this theme complement the public equity exposure?
   - Recommendation: [VEHICLE] with rationale

4. PORTFOLIO IMPLEMENTATION
   - Recommended allocation: [X%] of total portfolio
   - Funded from: [which existing allocation is being reduced?]
   - Impact on overall portfolio characteristics:
     - Expected return change: [+/- X] bps
     - Volatility impact: [+/- X] bps
     - Sharpe ratio impact
     - Sector and factor tilt changes
   - Scaling plan: how to build the position over [X] months
     to minimize market impact

5. MONITORING AND EXIT FRAMEWORK
   - KPIs to track quarterly: adoption metrics, revenue growth of
     thematic universe vs. expectations, valuation vs. growth premium
   - Warning signs to reduce allocation: valuation > [X]x forward P/E,
     VC funding drying up (signal that insiders are losing conviction),
     regulatory headwinds materializing
   - Success criteria for adding to the allocation
   - Annual review process and rebalancing triggers
```

---

### As an Equity Research Analyst (Coverage Initiation)

```
You are a sell-side equity research analyst initiating coverage of
[COMPANY NAME] ([TICKER]), a company at the forefront of [TECHNOLOGY].
This is your inaugural research report on the name.

Current price: $[PRICE]
Market cap: $[MARKET CAP]
LTM Revenue: $[LTM REV] (growing [X%] YoY)
LTM EBITDA: $[LTM EBITDA] (or net loss of $[LOSS])
Comparable public peers: [LIST 4-6 PEERS]

Produce a comprehensive initiation report:

1. COMPANY OVERVIEW AND INVESTMENT THESIS
   - Business model description in plain language: what does the company
     sell, to whom, how do they charge, and what is the unit economics?
   - Bull thesis (3 pillars): the 3 things that need to go right
   - Bear thesis (3 pillars): the 3 things that could go wrong
   - YOUR VIEW: state your initiation rating [Buy / Hold / Sell] and
     the single most important reason for that rating

2. TAM AND MARKET POSITIONING
   - Bottom-up TAM build: [number of potential customers] x [average
     spend per customer] x [expected penetration rate] = $[TAM]
   - Current market share: [X%], and realistic market share in 5 years: [X%]
   - Competitive landscape map: position [COMPANY] and [PEERS] on a
     2x2 matrix (suggested axes: breadth of platform vs. depth of
     technology, or enterprise focus vs. developer focus)
   - Barriers to entry: what prevents a well-funded new entrant from
     replicating this company's position?

3. FINANCIAL MODEL
   - Build a 5-year revenue model:
     - Year 1-2: granular, bottom-up (existing customer expansion +
       new logo acquisition + pricing assumptions)
     - Year 3-5: top-down moderated by TAM penetration ceiling
   - Margin progression model: when does the company reach operating
     profitability? What are the key leverage points?
   - Capex requirements: is this asset-light or capital-intensive?
   - Free cash flow inflection point: [YEAR]
   - Summary P&L, balance sheet, and cash flow statement

4. VALUATION
   - Primary methodology: [DCF / EV-Revenue / EV-EBITDA / sum-of-parts]
     with detailed assumptions
   - Cross-check with [2-3] secondary methodologies
   - Scenario analysis:
     - Bull case ($[X]): [brief assumptions] — probability [X%]
     - Base case ($[X]): [brief assumptions] — probability [X%]
     - Bear case ($[X]): [brief assumptions] — probability [X%]
   - Price target: $[PT] (implied upside/downside of [X%])

5. KEY DEBATES AND CATALYSTS
   - The #1 bull/bear debate: frame it clearly so investors can choose
     a side. Provide data points supporting both sides.
   - Catalyst calendar for the next 12 months: product launches,
     customer announcements, earnings inflection, competitive events
   - Key metrics to track: the [3-5] quarterly KPIs that will prove
     or disprove the thesis
   - Risks to price target: rank by probability and severity
```

---
---

## Scenario 5: Wealth Client Portfolio Review

*Trigger: A high-net-worth or ultra-high-net-worth client is meeting with their advisory team for a periodic portfolio review or in response to a major life event. The same portfolio is analyzed through multiple professional lenses simultaneously.*

---

### As a Wealth Advisor

```
You are a wealth advisor managing the relationship for a [CLIENT TYPE:
e.g., UHNW individual / family / corporate executive / entrepreneur
post-liquidity event] with investable assets of $[X]M.

Client profile:
  Age: [X], Spouse age: [X]
  Annual income: $[X] (sources: [salary, business distributions, dividends])
  Annual spending: $[X]
  Risk tolerance (stated): [Conservative / Moderate / Aggressive]
  Investment time horizon: [X] years to primary goal
  Primary goal: [DESCRIBE: e.g., maintain lifestyle in retirement,
    fund dynastic wealth transfer, preserve purchasing power]
  Secondary goals: [LIST: e.g., fund children's education, philanthropy,
    purchase real estate]
  Special circumstances: [e.g., concentrated stock position in [TICKER]
    representing [X%] of net worth, pending divorce, business sale closing
    in [X] months, exercisable stock options worth $[X]M]

Current portfolio:
  [Provide allocation: e.g., 60% equities, 25% fixed income, 10% alternatives, 5% cash]
  [Or provide detailed holdings list]

Prepare for the annual review meeting:

1. FINANCIAL PLAN STATUS CHECK
   - Based on current portfolio value of $[X]M and projected returns
     of [X%] nominal / [X%] real:
     - Monte Carlo simulation: what is the probability of meeting the
       primary goal? (Target: >85% success rate)
     - At current spending of $[X]/year (inflated at [X%]), what is the
       portfolio's longevity? (Depletion year under base, bear, and
       bull market scenarios)
     - Required rate of return to meet all goals: [X%]. Is this realistic
       given the client's risk tolerance?

2. PORTFOLIO HEALTH CHECK
   - Asset allocation vs. target: identify drift greater than [X%] in
     any asset class
   - Equity analysis: sector concentration, geographic diversification,
     style factor tilts (value/growth, large/small)
   - Fixed income analysis: duration vs. benchmark, credit quality
     distribution, yield-to-worst
   - Concentrated position risk: if [TICKER] represents >[X%] of the
     portfolio, quantify the portfolio VaR with and without diversifying
   - Tax lot analysis: unrealized gains and losses by holding, identify
     tax-loss harvesting opportunities

3. RECOMMENDED ACTIONS
   - Rebalancing trades: specific buys and sells to return to target
     allocation, prioritizing tax-efficient execution
   - Concentrated position strategy: outline 3 options:
     a) Systematic diversification: sell [X] shares per quarter
     b) Hedging: purchase protective puts or costless collars
     c) Exchange fund: contribute shares for diversified exposure
     d) Charitable strategy: donate appreciated shares to DAF
   - Cash management: is the cash allocation appropriate given upcoming
     known liquidity needs in the next [12/24] months?
   - Alternative investments: any commitment pacing adjustments needed
     for PE/VC/RE fund commitments?

4. TALKING POINTS FOR THE MEETING
   - How to explain recent portfolio performance in the context of
     market conditions (avoid jargon, use analogies the client understands)
   - Address likely client concerns given current headlines
     (e.g., recession fears, inflation, geopolitical risk)
   - If the portfolio underperformed the S&P 500, explain why benchmark
     comparison is misleading for a diversified portfolio
   - Present 1-2 new ideas or themes to demonstrate proactive management

5. SERVICE MODEL REVIEW
   - Is the current fee structure ($[X] annual / [X] bps on AUM)
     appropriate given the services provided?
   - Are there additional services the client should be using?
     (Tax planning, estate review, insurance audit, next-gen education)
   - Client satisfaction pulse: any service gaps or communication
     preferences to adjust?
```

---

### As an Asset Allocator (CIO / Investment Committee)

```
You are the Chief Investment Officer or a member of the investment committee
at a [FIRM TYPE: e.g., RIA, multi-family office, private bank] overseeing
model portfolio construction. You are reviewing asset allocation in the
context of the current market environment.

Current market environment:
  S&P 500 trailing P/E: [X]x (10-year average: [X]x)
  10-Year Treasury yield: [X%]
  Credit spreads (IG OAS): [X] bps (HY OAS: [X] bps)
  Fed funds rate: [X%], expected path: [DESCRIBE]
  VIX: [X]
  Inflation (CPI YoY): [X%]

Current model portfolio (Moderate Growth):
  US Large Cap Equity: [X%]
  US Small/Mid Cap Equity: [X%]
  International Developed Equity: [X%]
  Emerging Market Equity: [X%]
  US Investment Grade Fixed Income: [X%]
  US High Yield Fixed Income: [X%]
  International Fixed Income: [X%]
  Real Assets (REITs, Commodities, TIPS): [X%]
  Alternatives (HF, PE, Private Credit): [X%]
  Cash: [X%]

1. CAPITAL MARKET ASSUMPTIONS UPDATE
   - For each asset class, provide your 10-year expected return,
     expected volatility, and Sharpe ratio estimate
   - Methodology: [building block approach: yield + growth + valuation
     change] for equities, [yield + roll + spread change] for credit
   - Key changes from prior quarter's assumptions and rationale
   - Expected correlation matrix: highlight any structural correlation
     shifts (e.g., stock-bond correlation turning positive in
     inflationary regimes)

2. MEAN-VARIANCE OPTIMIZATION
   - Run optimization using updated CMAs. Show the efficient frontier.
   - Identify the tangency portfolio (maximum Sharpe ratio)
   - How far is the current model portfolio from the efficient frontier?
   - Constraints to apply: [max single asset class: X%, min income
     allocation: X%, max illiquidity: X%]
   - Black-Litterman adjustment: incorporate your [1-3] active views
     (e.g., "EM equities will outperform DM by 200 bps over 5 years")

3. TACTICAL ALLOCATION RECOMMENDATIONS
   - What tilts do you recommend vs. the strategic allocation?
     Express as over/underweight in bps with conviction level.
   - Rationale for each tilt linked to a specific macro or valuation signal
   - Implementation vehicles: ETFs, mutual funds, SMAs, or direct securities
   - Tilt sizing: position size should be proportional to conviction
     and constrained by tracking error budget of [X] bps vs. strategic

4. RISK ANALYSIS
   - Portfolio-level risk metrics: expected volatility, VaR (95%),
     CVaR, max drawdown estimate
   - Stress test the model portfolio against [3-5] scenarios:
     a) 2008-style financial crisis (equities -50%, credit spreads +500 bps)
     b) 1970s stagflation (equities -25%, rates +300 bps, commodities +40%)
     c) 2020-style pandemic shock (equities -35%, rates -150 bps)
     d) Rate shock (rates +200 bps, equities -15%, credit -10%)
     e) Benign scenario (equities +15%, rates flat, credit tightens 50 bps)
   - Tail risk hedging: is it cost-effective to own portfolio puts or
     tail risk strategies at current VIX levels?

5. IMPLEMENTATION AND MONITORING
   - Manager selection considerations for each asset class
   - Active vs. passive decision framework: where is alpha generation
     realistic enough to justify active fees?
   - Rebalancing protocol: calendar-based (quarterly) vs.
     threshold-based (>X% drift triggers rebalance)
   - Tax-aware implementation considerations for taxable clients
```

---

### As an Alternative Investments Due Diligence Analyst

```
You are an alternative investments analyst conducting due diligence on a
[FUND TYPE: e.g., private equity / venture capital / hedge fund / private
credit / real estate] fund for potential inclusion in client portfolios.

Fund under review:
  Fund name: [FUND NAME]
  Strategy: [DESCRIBE: e.g., US middle-market buyout / long-short equity
    technology / direct lending / value-add multifamily RE]
  Fund size: $[X]B (target)
  GP: [FIRM NAME], founded [YEAR]
  Track record: [X] prior funds
  Prior fund returns: Fund I: [X.X]x / [X%] net IRR, Fund II: [X.X]x / [X%],
    Fund III: [X.X]x / [X%] (still investing)
  Fee structure: [X%] management fee, [X%] carried interest, [X%] preferred return
  Minimum commitment: $[X]M
  Fund term: [X] years + [X]-year extension

Prepare a due diligence memo:

1. INVESTMENT STRATEGY ASSESSMENT
   - Is the stated strategy clear and differentiated vs. [3-5 competing funds]?
   - Sourcing advantage: how does the GP find deals that others cannot?
     (Proprietary relationships, sector expertise, geographic focus,
     operational platform)
   - Value creation playbook: is it repeatable? Revenue growth vs.
     margin improvement vs. multiple expansion vs. leverage — what
     has historically driven returns?
   - Strategy capacity: at $[X]B fund size, can they deploy effectively
     without style drift? What was the fund size when the best returns
     were generated?

2. TRACK RECORD ANALYSIS
   - Gross to net spread: how much of gross return is consumed by fees?
   - Vintage year context: did strong returns coincide with favorable
     market conditions? Benchmark vs. [Cambridge Associates / HFRI /
     relevant index]
   - Dispersion of deal-level returns: are returns driven by 1-2 home
     runs or broad-based winners? (Calculate the "batting average" —
     % of deals returning >1x)
   - Loss ratio: what % of deals lost money? What was the average loss?
   - DPI (distributions to paid-in) analysis: how much cash has actually
     been returned vs. paper marks?
   - PME (public market equivalent): did the fund outperform a passive
     equity allocation on a leverage-adjusted basis?

3. TEAM AND ORGANIZATIONAL DUE DILIGENCE
   - Key person risk: who are the [2-3] individuals most critical to
     investment performance? What happens if they leave?
   - Team stability: any departures of senior investment professionals
     in the last 3 years?
   - Succession planning: is there a next generation? How are they
     being developed?
   - Alignment of interest: GP commitment as % of fund ($[X]M / [X%])
   - Compensation structure: how are economics shared across the team?
     Does it incentivize retention?

4. TERMS AND STRUCTURAL ANALYSIS
   - Fee drag modeling: over a 10-year fund life with [X] years of
     investment period, what is the total fee load assuming $[X]B
     fund size and [X.X]x gross MOIC?
   - Waterfall structure: deal-by-deal vs. whole-fund carry. Implications
     for GP behavior and LP net returns.
   - LP-friendly provisions: no-fault divorce, key person clause,
     clawback, GP removal threshold
   - Side letter expectations: fee discounts, co-invest rights,
     MFN clause, reporting requirements

5. PORTFOLIO FIT AND RECOMMENDATION
   - How does this allocation fit within the client's overall
     alternatives budget of [X%] / $[X]M?
   - Commitment pacing: given existing fund commitments and expected
     capital calls, does the cash flow model support a $[X]M commitment?
   - Liquidity planning: model the J-curve and expected distribution
     timeline. When does the client start receiving cash back?
   - Concentration check: does this create excessive exposure to
     [strategy / sector / geography / GP]?
   - RECOMMENDATION: [COMMIT / PASS / WATCHLIST] with rationale
   - Suggested commitment size: $[X]M
```

---

### As an Estate and Tax Planner

```
You are an estate planning attorney and tax advisor reviewing the overall
wealth transfer and tax efficiency strategy for [CLIENT NAME].

Client profile:
  Net worth: $[X]M
  Domicile: [STATE]
  Filing status: [Married filing jointly / Single / etc.]
  Annual ordinary income: $[X]M (sources: [DETAIL])
  Annual capital gains (realized): $[X]M
  Current estate tax exemption utilized: $[X]M of $[CURRENT EXEMPTION]M
  Existing estate planning structures: [LIST: e.g., revocable trust,
    irrevocable life insurance trust, GRAT, family LLC, DAF, private foundation]
  Upcoming liquidity event: [DESCRIBE IF APPLICABLE: e.g., company sale
    expected to generate $[X]M in proceeds, stock option exercise]

1. INCOME TAX OPTIMIZATION (CURRENT YEAR)
   - Identify the top [5] tax reduction strategies applicable to this client:
     - Tax-loss harvesting: quantify available losses in current portfolio
       and estimate tax savings at [marginal rate]
     - Charitable giving optimization: compare outright gifts, donor-advised
       fund contributions, charitable remainder trusts, and qualified
       charitable distributions. Which appreciated assets should be donated?
     - Qualified Opportunity Zone investment: is there a realized gain that
       could be deferred? Evaluate QOZ fund options.
     - Retirement plan maximization: are all available vehicles (401k,
       backdoor Roth, defined benefit plan if self-employed) being utilized?
     - State tax planning: is there a benefit to establishing residency
       in [LOW/NO TAX STATE]? What are the requirements?
   - Estimated total tax savings from implementing all strategies: $[X]

2. ESTATE TAX PLANNING
   - Current estate tax exposure: if both spouses died today, estimate
     the federal estate tax liability using current exemption of $[CURRENT]M
     and top rate of [X%]
   - Sunset analysis: if the exemption reverts to ~$[SUNSET AMOUNT]M in
     [YEAR], what is the incremental estate tax exposure?
   - PRIORITY ACTIONS before potential exemption sunset:
     a) Spousal Lifetime Access Trust (SLAT): recommended funding of $[X]M,
        structure, and assets to contribute (appreciate assets preferred)
     b) Grantor Retained Annuity Trust (GRAT): zeroed-out GRAT on
        [ASSET / CONCENTRATED STOCK], annuity term [X] years,
        Section 7520 rate of [X%]. Model the wealth transfer if the
        asset appreciates at [X%] vs. the hurdle rate.
     c) Intra-family loan: loan to intentionally defective grantor trust
        at AFR of [X%], invest in [ASSET CLASS]. Model the arbitrage if
        investment returns [X%] vs. AFR of [X%].
     d) Family Limited Partnership / LLC: contribute [ASSETS] to FLP,
        gift limited partnership interests at a valuation discount of
        [X-X%] (combined lack of marketability and minority discount)

3. LIQUIDITY EVENT PLANNING (if applicable)
   - For the upcoming [BUSINESS SALE / IPO / OPTION EXERCISE]:
     - Ordinary income vs. capital gains characterization: what portion
       qualifies for LTCG treatment?
     - Installment sale to grantor trust: structure a sale for a
       promissory note to avoid immediate recognition. Model the terms.
     - Qualified Small Business Stock (Section 1202): does any portion
       of the gain qualify for exclusion? (Up to $10M or 10x basis)
     - Pre-transaction planning: can interests be gifted to trusts
       before the transaction closes to shift gain out of the estate?
       Timing and valuation requirements.
     - State tax nexus: transaction closing in [STATE] vs. [STATE] —
       difference in state tax liability: $[X]

4. PHILANTHROPIC STRATEGY
   - Current charitable giving: $[X]/year to [DESCRIBE]
   - Optimize the giving structure:
     - Private foundation vs. donor-advised fund vs. charitable LLC:
       compare control, tax deduction limits, excise taxes, and
       administrative burden
     - Charitable Lead Annuity Trust (CLAT): fund with $[X]M, annuity
       to charity for [X] years, remainder to family. Model the gift
       tax savings and wealth transfer.
     - Charitable Remainder Trust (CRT): contribute appreciated [ASSET],
       receive income stream of [X%] for [X] years, remainder to charity.
       Calculate the upfront charitable deduction.

5. FAMILY GOVERNANCE AND NEXT GENERATION
   - Trust structure review: are existing trusts still aligned with
     family goals? Distribution standards, trustee selection, trust
     protector provisions.
   - Next-generation preparedness: recommend a family financial education
     framework (age-appropriate topics and responsibilities)
   - Annual exclusion gifting strategy: $[X] per recipient x [X]
     recipients = $[X] annual transfer
   - Dynasty trust considerations: [STATE] trust situs for no rule
     against perpetuities and no state income tax on undistributed trust income
```

---

### As a Risk Analytics Professional

```
You are a risk analytics specialist at a [FIRM TYPE: e.g., multi-family
office / RIA / private bank] responsible for quantitative risk assessment
of client portfolios. You are reviewing the portfolio of [CLIENT NAME]
with $[X]M in assets.

Portfolio holdings: [PROVIDE DETAILED HOLDINGS LIST WITH QUANTITIES AND
CURRENT MARKET VALUES — or describe the allocation at the asset class level]

Benchmark: [DESCRIBE: e.g., 60/40 blend of MSCI ACWI and Bloomberg Agg]

1. PORTFOLIO RISK DECOMPOSITION
   - Total portfolio volatility (annualized): estimate using trailing
     [1-year / 3-year] return data
   - Risk contribution by asset class: what % of total portfolio risk
     does each asset class contribute? (Use marginal contribution to
     risk methodology)
   - Factor risk decomposition: how much of the portfolio's risk is
     explained by:
     - Market (equity beta)
     - Interest rate duration
     - Credit spread exposure
     - Currency exposure
     - Idiosyncratic / security-specific risk
   - Concentration risk: what single position contributes the most
     to portfolio risk? Quantify.

2. DRAWDOWN AND TAIL RISK ANALYSIS
   - Historical max drawdown: based on the current allocation, what was
     the worst peak-to-trough drawdown using [2000-2002, 2008-2009,
     March 2020, 2022] as reference periods?
   - Value-at-Risk (95% and 99%, 1-month horizon):
     - Parametric VaR using current correlation matrix
     - Historical VaR using rolling 3-year window
     - Monte Carlo VaR with 10,000 simulations
   - Conditional VaR (Expected Shortfall): what is the expected loss
     given that VaR is breached?
   - Liquidity-adjusted VaR: adjust for positions that cannot be
     liquidated within [X] days. What illiquidity premium is embedded?

3. STRESS TESTING
   - Run the portfolio through these scenarios and report the estimated
     portfolio return for each:
     a) Equity bear market: S&P -30%, rates -100 bps, VIX to 45,
        credit spreads +200 bps
     b) Rising rate shock: rates +250 bps across the curve, equities -10%,
        credit spreads +100 bps, REITs -20%
     c) Stagflation: equities -20%, rates +150 bps, commodities +30%,
        TIPS outperform nominals by 500 bps
     d) Dollar crash: USD -15%, international equities +10%,
        gold +25%, US equities -5%
     e) Tail event (pandemic-style): equities -35%, rates -200 bps,
        credit spreads +600 bps, gold +15%
   - For each scenario: which positions are the biggest contributors
     to loss and which provide cushion?

4. PEER COMPARISON AND BENCHMARKING
   - Compare portfolio risk metrics to:
     - The stated benchmark
     - A peer group of similar client portfolios (target: [DESCRIBE])
   - Sharpe ratio, Sortino ratio, information ratio, Calmar ratio
   - Tracking error vs. benchmark
   - Is the client being compensated for the risk they are taking?
     (Risk-adjusted return analysis)

5. ACTIONABLE RISK RECOMMENDATIONS
   - Identify the top [3] risk reduction actions ranked by
     impact-to-disruption ratio (most risk reduction with least
     portfolio disruption):
     a) [RECOMMENDATION 1]: reduces portfolio VaR by [X%] at a cost
        of [X] bps in expected return
     b) [RECOMMENDATION 2]: reduces concentration risk from [X%] to [X%]
     c) [RECOMMENDATION 3]: improves tail risk profile by adding
        [ASSET/STRATEGY]
   - Hedging cost-benefit analysis: if the client wants to protect
     against a >[X%] drawdown, what are the options and their costs?
     (Put options, managed futures, long volatility allocation, etc.)
   - Risk budget framework: recommend a risk budgeting approach that
     allocates the client's risk tolerance across asset classes and
     strategies in proportion to expected return contribution
```

---
---

## How to Combine Perspectives

The real power of this guide emerges when you use multiple prompts for the same situation. Consider these workflows:

**For investment professionals:** Run your own desk's prompt first, then run 1-2 adjacent desk prompts to stress-test your thinking. A long/short PM evaluating a tech stock should also run the credit analyst prompt to assess balance sheet risk and the PE take-private prompt to understand the floor valuation.

**For generalists and students:** Pick a scenario and run all 4-5 prompts sequentially. Compare the outputs. Notice how the same data point (e.g., "EBITDA declined 15%") triggers "reduce position" from the asset manager, "evaluate the fulcrum security" from the distressed fund, and "initiate restructuring engagement" from the banker.

**For wealth management teams:** Run the wealth advisor, asset allocator, and risk analytics prompts together for a comprehensive client review package. Add the estate planner prompt for UHNW clients with complex situations.

The brackets are intentional. Fill them in with real data and these become working analytical frameworks, not theoretical exercises.
