# Early-Stage Investing -- Seed and Series A

```
You are a senior early-stage venture capital investor at a top-tier fund managing
$500M+ across seed and Series A investments. You have deep expertise in evaluating
founding teams, sizing nascent markets, structuring term sheets, and identifying
product-market fit signals. You think in terms of power law outcomes, founder
quality, and market timing. You are rigorous about ownership targets, dilution
math, and reserve strategy. You have seen 10,000+ pitches and backed 50+
companies, with multiple outcomes exceeding 100x.
```

## What This Desk Does

The early-stage investing team sources, evaluates, and leads investments in companies at the seed and Series A stage -- typically pre-revenue or early-revenue businesses with fewer than 50 employees. The core challenge is making high-conviction bets under extreme uncertainty, where most traditional financial analysis is inapplicable. Instead, the team relies on market sizing frameworks, founder assessment, product-market fit signals, and competitive dynamics to underwrite investments that have the potential for 50-100x+ returns. Ownership targets typically range from 10-20% at entry, with reserves allocated for follow-on rounds.

---

## 1. Market Sizing

Rigorous market sizing is the foundation of any early-stage investment thesis. The key tension is between top-down estimates (which tend to be inflated) and bottom-up calculations (which tend to be conservative). The best opportunities often involve market creation rather than market capture.

```
You are evaluating a market opportunity for [COMPANY_NAME], which operates in
[INDUSTRY/VERTICAL]. The company's product is [PRODUCT_DESCRIPTION] targeting
[CUSTOMER_SEGMENT].

Perform a comprehensive market sizing analysis:

1. TOP-DOWN ANALYSIS:
   - Total Addressable Market (TAM): Define the broadest relevant revenue pool.
   - Serviceable Addressable Market (SAM): What portion can this business model
     realistically address given geography, segment, and channel constraints?
   - Serviceable Obtainable Market (SOM): What share can the company capture in
     5-7 years given competitive dynamics?

2. BOTTOM-UP ANALYSIS:
   - Number of potential customers in target segment: [ESTIMATE]
   - Average revenue per customer: [ESTIMATE]
   - Realistic penetration rate by year (Y1-Y5)
   - Build up to annual revenue at scale

3. MARKET CREATION vs. MARKET CAPTURE:
   - Is this company capturing share in an existing market, or creating a new
     category? If creating, what analogies or demand signals support the thesis?
   - What secular trends (regulatory, demographic, technological) expand the market?

4. MARKET TIMING:
   - Why now? What has changed (technology cost curve, regulation, behavior shift)
     that makes this possible today but not 5 years ago?

Express TAM in both revenue terms and unit economics terms. Flag any assumptions
that require >3x expansion from current market data.
```

```
Analyze the market dynamics for [SECTOR] and determine whether [COMPANY_NAME]
is positioned for market creation or market capture.

For market creation: Estimate the demand curve using analogies from [COMPARABLE_
MARKETS]. What was the adoption S-curve for those markets, and what stage of
the curve does [SECTOR] appear to be in?

For market capture: What is the current market share distribution? Who are the
top 3-5 incumbents, and what percentage of the TAM do they control? Where is
the white space?

Quantify the difference between a "market capture" scenario (company takes [X]%
of existing $[Y]B market) and a "market creation" scenario (market expands to
$[Z]B and company takes [W]% of the new market). What does each scenario imply
for the company's revenue at maturity?
```

---

## 2. Founder Evaluation

At the early stage, the team matters more than almost anything else. The founder evaluation framework assesses multiple dimensions: technical depth, market insight, resilience, recruiting ability, and the elusive "founder-market fit."

```
You are conducting a deep founder assessment for [FOUNDER_NAME(S)], the
founder(s) of [COMPANY_NAME]. Use the following framework:

FOUNDER-MARKET FIT:
- What is the founder's unfair insight about this market? How was it acquired
  (direct experience, research, personal pain point)?
- Rate the founder's domain expertise on a scale of 1-5, with justification.
- Has the founder lived the problem they are solving? For how long?

TECHNICAL DEPTH:
- Can the founder build the v1 product themselves, or do they require a
  technical co-founder? If the latter, assess the CTO/technical co-founder.
- What is the technical moat? Is the founder capable of creating and maintaining
  a meaningful technical advantage?

RESILIENCE AND GRIT INDICATORS:
- Prior startup experience: [DETAILS]. Outcomes?
- Evidence of perseverance through adversity (professional or personal).
- Reference checks: What do former colleagues, reports, and co-founders say?
  Focus on behavior under stress.

RECRUITING AND LEADERSHIP:
- Quality of the first 5-10 hires. Are they A-players? How were they recruited?
- Can this founder attract world-class talent at below-market compensation?
- Evidence of clear communication and vision-setting.

RISK ASSESSMENT:
- Single founder risk? Co-founder relationship health?
- Key person dependency -- what happens if the founder is incapacitated?
- Any red flags from background checks, reference calls, or public record?

Provide a composite score (1-10) with the top 3 strengths and top 3 risks.
```

```
Compare the founding teams of [COMPANY_A] and [COMPANY_B], both competing in
[MARKET]. For each team, assess:
- Complementarity of skill sets (technical, commercial, operational)
- Prior working relationship and duration
- Equity split and vesting structure (flag any unusual arrangements)
- Speed of execution to date (milestones achieved relative to capital raised
  and time elapsed)

Which team has the higher probability of building a category-defining company
in this space, and why?
```

---

## 3. Term Sheet Analysis

Term sheet negotiation at the early stage sets the foundation for the company's capitalization structure through all subsequent rounds. Key elements include valuation, option pool, liquidation preferences, anti-dilution provisions, board composition, and protective provisions.

### Dilution Mathematics

```
Ownership dilution per round:
  Post-Round Ownership = Pre-Round Ownership * (Pre-Money Valuation / Post-Money Valuation)

Option pool shuffle (pre-money pool creation):
  Effective pre-money to existing holders = Stated Pre-Money - Option Pool Increase
  If pre-money = $10M, round size = $5M, new pool = 15% of post:
    Post-money = $15M
    Pool shares = 15% * post = $2.25M equivalent
    Effective pre-money to founders = $10M - $2.25M = $7.75M

Dilution across multiple rounds:
  Founder ownership after N rounds = Initial% * PRODUCT(Pre_i / Post_i) for i=1..N
```

```
Analyze the following term sheet for [COMPANY_NAME]'s [ROUND_NAME] financing:

- Pre-money valuation: $[X]M
- Round size: $[Y]M
- Option pool: [Z]% (pre-money / post-money)
- Liquidation preference: [1x/2x] [non-participating / participating with cap]
- Anti-dilution: [broad-based weighted average / narrow-based / full ratchet]
- Board composition: [DETAILS]
- Protective provisions: [DETAILS]
- Pro-rata rights: [YES/NO], allocated to investors with > [THRESHOLD]
- Drag-along: [DETAILS]
- Information rights: [DETAILS]

Evaluate:
1. What is the effective pre-money valuation after accounting for the option
   pool shuffle? Show the math.
2. Build an ownership table showing all stakeholders pre- and post-round.
3. Model a valuation waterfall at exit values of $[A]M, $[B]M, $[C]M, and
   $[D]M. Show proceeds to each class of stock.
4. How do the liquidation preferences and participation rights affect founder
   economics at each exit scenario?
5. Flag any terms that are outside market norms for a [STAGE] round in [YEAR].
6. What is the implied valuation needed at exit for the investor to achieve a
   [TARGET]x return? What does that imply about required company trajectory?
```

```
Build a pro forma cap table for [COMPANY_NAME] across the following rounds:

- Seed: $[A]M at $[B]M pre-money, [C]% option pool
- Series A: $[D]M at $[E]M pre-money, pool increased to [F]%
- Series B: $[G]M at $[H]M pre-money, pool increased to [I]%

For each round, show:
1. Share price per round
2. Shares outstanding by class (common, preferred by series, option pool)
3. Ownership percentages for: founders, each investor group, option pool
4. Dilution experienced by each prior stakeholder
5. Implied step-up multiple from prior round

Then model the exit waterfall at $[X]M acquisition price, showing proceeds to
each stakeholder under: (a) all common conversion, (b) liquidation preference
exercise, (c) participation with [CAP] cap. Identify the crossover point where
preferred holders convert to common.
```

---

## 4. Product-Market Fit Assessment

Product-market fit is the single most important milestone for an early-stage company. The assessment uses quantitative signals (retention, engagement, growth) and qualitative signals (customer pull, word-of-mouth) to determine whether a company has achieved -- or is approaching -- PMF.

```
Assess product-market fit for [COMPANY_NAME] using the following data and
framework:

QUANTITATIVE SIGNALS:
- Retention curves: Analyze [DAILY/WEEKLY/MONTHLY] retention data.
  - Does the curve flatten (PMF signal) or continue declining (no PMF)?
  - At what level does it flatten? Benchmark: [INDUSTRY_BENCHMARK]%.
  - Cohort analysis: Are newer cohorts retaining better than older ones?

- Engagement metrics:
  - DAU/MAU ratio: [VALUE] (benchmark: >25% strong, >50% exceptional)
  - Time spent per session: [VALUE]
  - Core action frequency: [METRIC] performed [X] times per [PERIOD]

- Growth signals:
  - Organic vs. paid acquisition split: [X]% / [Y]%
  - Viral coefficient (k-factor): [VALUE] (>1.0 = viral growth)
  - NPS score: [VALUE] (>50 = strong PMF signal)

- Revenue signals (if applicable):
  - Net dollar retention: [VALUE]% (>120% = strong expansion revenue)
  - Willingness to pay: conversion rate from free to paid = [VALUE]%

QUALITATIVE SIGNALS:
- Customer pull: Are customers actively seeking out the product, or does the
  company need to push? Evidence of inbound demand?
- Word-of-mouth: What percentage of new users come from referrals?
- Customer quotes: Provide 2-3 representative customer testimonials.
- "Hair on fire" test: Is the problem so acute that customers tolerate a buggy
  or incomplete product?

Rate PMF on a 1-5 scale:
  1 = No PMF (declining retention, no organic growth)
  2 = Early signals (some retention, but curve still declining)
  3 = Emerging PMF (flattening retention, growing organic demand)
  4 = Clear PMF (strong retention, organic growth, expansion revenue)
  5 = Exceptional PMF (viral growth, negative churn, category-defining)
```

---

## 5. Competitive Landscape Mapping

Early-stage competitive analysis must account for incumbents, other startups, adjacent threats, and the sustainability of any early moats.

```
Map the competitive landscape for [COMPANY_NAME] operating in [MARKET]:

INCUMBENT ANALYSIS:
- Identify the top 3-5 incumbents. For each:
  - Revenue, market share, and growth rate
  - Likelihood of building a competing product (build vs. buy vs. ignore)
  - Structural disadvantages that prevent them from competing effectively
    (innovator's dilemma, channel conflict, margin structure, culture)

STARTUP COMPETITORS:
- Identify [N] funded startups in the same or adjacent space.
  - Funding raised, stage, and key investors
  - Product differentiation vs. [COMPANY_NAME]
  - Go-to-market approach differences
  - Team quality comparison (see founder evaluation framework)

ADJACENT THREATS:
- What companies in adjacent markets could expand into this space?
- What platform shifts (AI, mobile, regulatory) could enable new entrants?

MOAT ASSESSMENT (EARLY STAGE):
Rate each moat source (1-5) for [COMPANY_NAME]:
  - Network effects: [SCORE] -- Does each new user make the product more
    valuable for existing users?
  - Data advantages: [SCORE] -- Does usage generate proprietary data that
    improves the product in ways competitors cannot replicate?
  - Switching costs: [SCORE] -- How painful is it for a customer to leave?
  - Brand/trust: [SCORE] -- Relevant in regulated or high-stakes domains.
  - Economies of scale: [SCORE] -- Does unit economics improve with scale
    in ways that create barriers?

What is the most likely competitive response to [COMPANY_NAME]'s success in
the next 12-24 months? How defensible is the company's position?
```

```
For [COMPANY_NAME] in [MARKET], perform a "kill the company" analysis:

1. If you were a well-funded competitor, what would be your strategy to defeat
   [COMPANY_NAME]? What would you build, how would you price it, and how would
   you go to market?
2. If [INCUMBENT] decided to enter this market with unlimited resources, what
   would their playbook look like? What advantages would they have?
3. What technology shift could render [COMPANY_NAME]'s approach obsolete?
4. What regulatory change could destroy or dramatically impair the business?

For each scenario, assess probability (low/medium/high) and severity (low/
medium/high). What mitigations can the company put in place?
```

---

## Mathematical Frameworks

### Ownership and Dilution Table

```
Round-by-round dilution model:

Let S_n = total shares outstanding after round n
Let I_n = new shares issued in round n (investment / price per share)
Let P_n = option pool shares created in round n

S_n = S_{n-1} + I_n + P_n

Ownership of stakeholder X after round n:
  Own_X,n = Shares_X / S_n

Price per share in round n:
  PPS_n = Pre-Money Valuation_n / S_{n-1}

Post-money valuation:
  Post_n = Pre_n + Investment_n

Step-up multiple:
  Step_n = PPS_n / PPS_{n-1}
```

### Valuation Waterfall (Simplified)

```
At exit value E:

1. If E < Total Liquidation Preferences:
   - Preferred holders receive pro-rata share of E based on preference stack
   - Common holders receive $0

2. If E >= Total Liquidation Preferences (non-participating preferred):
   - Each preferred holder chooses MAX(liquidation preference, as-converted share)
   - Crossover point: E where as-converted value = liquidation preference
     Crossover_i = Preference_i / Ownership_i(as-converted)

3. If participating preferred with cap:
   - Preferred receives: Preference + share of remaining, capped at [CAP]x
   - Above cap: converts to common

Proceeds to stakeholder X:
  Proceeds_X = f(E, preference_stack, participation_rights, conversion_terms)
```

---

## See Also

- [Growth-Stage Investing](growth-stage.md) -- Series B+ and late-stage dynamics
- [Crypto / Web3](crypto-web3.md) -- Token-based early-stage structures
- [Biotech / Healthcare](biotech-healthcare.md) -- Specialized early-stage frameworks
- [Platform Operations](platform-operations.md) -- Post-investment value creation
- [Venture Overview](README.md) -- Fund economics and portfolio construction
