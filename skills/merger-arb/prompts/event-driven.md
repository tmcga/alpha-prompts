# Event-Driven Strategies

## Role Context

```
You are a senior event-driven portfolio manager at a $3B multi-strategy fund. You specialize
in merger arbitrage, spin-offs, activist situations, and special situations where a
corporate event creates a definable catalyst with a quantifiable probability and timeline.
You think in expected value terms: every position is a probability-weighted bet on an event
outcome. You are rigorous about deal break risk, regulatory timelines, and the difference
between "cheap" and "mispriced conditional on event probability." You size positions using
the Kelly criterion applied to event probabilities, and you always know your portfolio's
aggregate exposure to deal breaks, market correlation, and event clustering risk. You never
confuse the spread with the edge -- the spread compensates for risk; the edge comes from
superior probability estimation.
```

---

## What This Desk Does

Event-driven strategies extract returns from corporate events -- mergers, spin-offs, restructurings, activist campaigns, tender offers, and other catalysts that create temporary mispricings with identifiable resolution dates. The edge comes from estimating event probabilities more accurately than the market-implied probability embedded in the spread. Unlike directional strategies, event-driven returns are largely uncorrelated with broad markets during normal times, though they exhibit tail correlation during systemic stress (when multiple deals break simultaneously). The strategy generates consistent carry-like returns punctuated by occasional losses from deal breaks or adverse event outcomes. A well-managed event book runs 20-40 positions, targets 8-15% annual returns with a Sharpe ratio of 1.0-1.5, and maintains strict position sizing to survive the inevitable multi-deal break scenario.

---

## 1. Merger Arbitrage

### Analyze a Merger Arbitrage Opportunity

```
A merger has been announced:
- Acquirer: [company name / ticker]
- Target: [company name / ticker]
- Deal terms: [cash offer at $X / stock-for-stock at X.XX ratio / cash + stock mix]
- Announcement date: [date]
- Expected close date: [date]
- Current target price: $[X]
- Deal price / implied value: $[X]
- Current spread: $[X] ([X]%)

Analyze this merger arb opportunity:

1. **Spread decomposition**:
   Gross spread = (Deal price - Current price) / Current price = [X]%
   Annualized spread = Gross spread x (365 / Days to close) = [X]%

   The spread compensates for:
   - Deal break risk: The primary risk
   - Time value of money: Opportunity cost of capital
   - Financing cost: Cost of carry on the position
   - Market risk (for stock deals): Beta exposure until close

   Merger arb return formula:
   E[R] = P(close) x Spread_if_close + P(break) x Loss_if_break

   Implied break probability from spread:
   P(break) = Spread / (Spread + |Loss_if_break|)
   where Loss_if_break ~ target price drops to pre-announcement "unaffected" price

2. **Deal probability assessment**:
   Score each risk factor (1-10 scale, 10 = highest risk):

   | Risk Factor | Score | Notes |
   |-------------|-------|-------|
   | Regulatory (antitrust) | [X] | [HSR, EU, China SAMR, sector regulators] |
   | Financing conditionality | [X] | [Fully committed? Bridge loan? Leverage level?] |
   | Shareholder approval | [X] | [% needed, largest shareholders' stance] |
   | Material adverse change (MAC) | [X] | [Target business deterioration risk] |
   | Strategic rationale strength | [X] | [Is this a "must-do" deal or opportunistic?] |
   | Bidder's ability to walk | [X] | [Reverse break fee size, specific performance?] |
   | Competing bid risk | [X] | [Could a topping bid emerge?] |

   My estimated deal close probability: [X]%
   Market-implied probability: [X]%
   Edge = My estimate - Market implied = [X]% (positive = I think deal is more likely than market does)

3. **Downside analysis (deal break scenario)**:
   - Unaffected price (pre-announcement): $[X]
   - Expected target price if deal breaks: $[X] (may be above unaffected if strategic value persists)
   - Loss if break: ($[X] - Current price) / Current price = -[X]%
   - Break fee payable to target: $[X] ([X]% of deal value, provides some downside cushion)

4. **Stock deal hedging** (if applicable):
   - Exchange ratio: [X] acquirer shares per target share
   - Hedge: Short [X] shares of acquirer per 1 share of target (delta-adjusted for collar if applicable)
   - Collar terms: [if applicable, floor and cap exchange ratios]
   - Residual market risk: [describe any unhedgeable component]

5. **Timeline and catalysts to monitor**:
   - HSR/antitrust filing: [date] -- Second request risk: [X]%
   - Shareholder vote: [date]
   - Regulatory approvals: [list each jurisdiction and expected timeline]
   - Outside date (drop-dead date): [date]
   - If close is delayed past expected date, spread typically [widens / compresses]
```

### Portfolio-Level Merger Arb Risk

```
I'm running a merger arb book with [N] active positions:

[List each deal: name, spread, probability, size, days to close]

Analyze portfolio-level risks:

1. **Expected portfolio return**:
   E[R_portfolio] = Sum_i: Weight_i x P(close_i) x Spread_i + Weight_i x P(break_i) x Loss_i

2. **Deal break correlation**:
   - In normal markets, deal breaks are approximately independent
   - In stress (2008, 2020), deal breaks cluster: financing dries up, regulatory stance hardens
   - Stress scenario: Model [3-5] simultaneous breaks. Portfolio loss = ?
   - Correlation adjustment: If avg pairwise break correlation = rho, then:
     Portfolio break variance >> sum of individual break variances

3. **Concentration limits**:
   - Max single deal: [X]% of NAV (typically 5-10%)
   - Max single sector: [X]% (regulatory correlation within sectors)
   - Max cash deals: [X]% (financing risk correlation)
   - Max cross-border: [X]% (geopolitical regulatory correlation)

4. **Gross/net exposure**:
   - Gross: Sum of absolute position sizes
   - Net market beta: What is the portfolio's residual equity beta after hedging?
   - In stock deals, imperfect hedging leaves residual spread risk
```

---

## 2. Spin-Off Analysis

### Evaluate a Spin-Off Opportunity

```
[Parent company] is spinning off [SpinCo] with the following terms:
- Record date: [date]
- Distribution date: [date]
- Distribution ratio: [X] shares of SpinCo per [Y] shares of parent
- SpinCo business: [describe]
- SpinCo expected financials: Revenue $[X]M, EBITDA $[X]M, Net income $[X]M
- Parent pro-forma financials post-spin: Revenue $[X]M, EBITDA $[X]M

Analyze the spin-off opportunity:

1. **Stub value analysis**:
   Before spin: Parent market cap = $[X]B
   SpinCo estimated value: $[X]B (based on [comparable company multiples / DCF])
   Stub value (parent ex-SpinCo) = Parent market cap - SpinCo value = $[X]B
   Stub implied multiple: [X]x EBITDA vs. peers at [X]x

   If stub is cheap: Buy parent pre-spin, hold both pieces
   If stub is rich: Buy parent pre-spin, short SpinCo when-issued or post-distribution

2. **Forced selling dynamics** (primary source of alpha):
   - Index funds: SpinCo may not qualify for parent's index. Forced selling of [X]M shares
     estimated over [X] days post-distribution
   - Mandate mismatch: If parent is large-cap and SpinCo is small-cap, large-cap-only funds
     must sell SpinCo
   - Sector mismatch: If SpinCo is in a different sector than parent, sector funds must sell
   - Estimate forced selling volume: [X]% of SpinCo float over [X]-day period
   - Price impact of forced selling: Creates temporary undervaluation of [X-Y]%

3. **Index reconstitution**:
   - Will SpinCo be added to any index? (Russell 2000 inclusion if small-cap)
   - Timeline for index inclusion: [X] weeks/months post-spin
   - Index inclusion typically creates [X]% buying pressure

4. **Hidden value identification**:
   - Was SpinCo undervalued within the conglomerate discount?
   - Does SpinCo have a better growth profile than the parent?
   - New management team with equity incentives aligned with SpinCo performance?
   - Tax-free spin vs. taxable -- implications for parent holders

5. **Trade structure**:
   - Pre-spin: Buy parent, expect combined value > current market cap
   - Post-spin: Buy SpinCo during forced selling window, target [X]% return
   - Pairs: Long SpinCo / Short parent (if stub is overvalued)
   - Timeline: Hold [X] months for re-rating as forced selling abates and coverage initiates
```

---

## 3. Activist Investing Analysis

### Evaluate an Activist Campaign

```
An activist investor has taken a position in [target company]:
- Activist: [name / fund]
- Ownership stake: [X]% as per 13D filing
- Stated objectives: [board seats / strategic review / M&A / capital return / operational changes]
- Target company market cap: $[X]B
- Target company current valuation: [X]x EV/EBITDA vs. peers at [X]x

Analyze the activist situation:

1. **Board and ownership dynamics**:
   - Board composition: [X] directors, [X] independent, [X] classified/staggered
   - Poison pill: [yes/no], threshold [X]%
   - Other significant holders: [list top 5 institutional holders and likely stance]
   - ISS/Glass Lewis likely recommendation: [support activist / support management]
   - Proxy fight probability: [X]%

2. **Operational improvement potential**:
   - Margin gap vs. best-in-class peers: [X] bps
   - SG&A as % of revenue vs. peers: [X]% vs. [X]%
   - Capital allocation efficiency: ROIC [X]% vs. WACC [X]%
   - Achievable margin improvement: [X] bps over [X] years
   - Value creation from margin improvement: $[X] per share

3. **Strategic alternatives**:
   - Sum-of-parts valuation: $[X] per share (vs. current $[X])
   - Takeout premium: Strategic buyer could pay [X]x EBITDA = $[X] per share
   - LBO analysis: PE buyer at [X]x leverage could pay $[X] per share
   - Probability of sale/merger: [X]%

4. **Campaign economics**:
   - Activist's average cost basis (estimated from 13D): $[X]
   - Activist's likely target price: $[X] (based on stated objectives and typical campaigns)
   - Campaign duration: Typical [12-24] months
   - Success rate for this type of campaign: [X]% (historically, activists win board seats ~60%)

5. **Expected value calculation**:
   | Outcome | Probability | Target Price | Return |
   |---------|------------|--------------|--------|
   | Full activist success | [X]% | $[X] | +[X]% |
   | Partial success (compromise) | [X]% | $[X] | +[X]% |
   | Activist fails, status quo | [X]% | $[X] | [X]% |
   | Company deteriorates | [X]% | $[X] | -[X]% |

   E[R] = Sum: P(outcome) x Return(outcome) = [X]%
```

---

## 4. Special Situations

### Analyze a Special Situation Opportunity

```
Situation type: [rights offering / tender offer / dutch auction / litigation optionality /
recapitalization / exchange offer]

Details:
- Company: [name / ticker]
- Situation description: [describe the corporate action]
- Key terms: [pricing, timeline, conditions]
- Current stock price: $[X]

For **rights offerings**:
- Subscription price: $[X] (discount to market: [X]%)
- Rights ratio: [X] new shares per [X] existing shares
- Oversubscription privilege: [yes/no]
- Transferable rights: [yes/no]
- Strategy: Buy rights at discount, exercise, sell shares. Or buy stock pre-record date
  for the embedded option value of the rights.
- Key risk: Dilution effect on existing shares, participation rate uncertainty

For **tender offers / dutch auctions**:
- Tender price / price range: $[X] to $[X]
- Number of shares sought: [X]M ([X]% of outstanding)
- Proration risk: If oversubscribed, you may only tender [X]% of shares
- Odd lot privilege: Shares below [100] shares tendered in full (no proration)
- Strategy: Buy below tender price, tender shares
- Expected return: (Tender price - Purchase price) / Purchase price x P(accepted)

For **litigation optionality**:
- Pending litigation: [describe case]
- Potential damages / settlement: $[X] per share
- Probability of favorable outcome: [X]%
- Timeline to resolution: [X] months
- Market's current pricing of litigation: $[X] per share of embedded value
- Strategy: If market underprices the option value, buy the stock for the litigation call option
- Key framework: Litigation value = P(win) x Award - P(lose) x Legal_costs_already_priced_in
```

---

## 5. Event Probability and Position Sizing

### Size an Event-Driven Book Using Expected Value

```
I have [N] event-driven positions to size within a portfolio:

| Event | Type | Probability | Win Return | Loss Return | Correlation to Market | Timeline |
|-------|------|-------------|------------|-------------|----------------------|----------|
| Deal A | Merger arb | [X]% | +[X]% | -[X]% | [X] | [X] months |
| Deal B | Spin-off | [X]% | +[X]% | -[X]% | [X] | [X] months |
| Deal C | Activist | [X]% | +[X]% | -[X]% | [X] | [X] months |

Position sizing framework:

1. **Kelly criterion per event**:
   f_i* = (p_i x b_i - q_i) / b_i
   where b_i = |Win return_i| / |Loss return_i| (win/loss ratio)

   Use fractional Kelly: f_actual = 0.25 x f* to 0.50 x f*
   Rationale: Event probabilities have estimation error; fractional Kelly is robust

2. **Portfolio-level Kelly with correlation**:
   When events are correlated (e.g., multiple mergers break in market stress):
   f_portfolio = f_individual x (1 - avg_pairwise_event_correlation)

   Stress test: What if [3] deals break simultaneously?
   Max acceptable portfolio loss in stress scenario: [X]% of NAV
   -> This constrains maximum gross event exposure

3. **Annualized return by event type**:
   Annualized return = (1 + Expected return)^(365/Days to resolution) - 1

   Merger arb: Typically [4-8]% spread over [3-6] months = [8-20]% annualized
   Spin-offs: Typically [10-25]% over [3-12] months = [15-30]% annualized (higher variance)
   Activist: Typically [15-40]% over [12-24] months = [10-25]% annualized (long duration)

   Capital allocation: Prefer higher annualized return per unit of risk

4. **Event clustering risk management**:
   - Track aggregate exposure to common break scenarios:
     a) Market crash (all deals at risk): [X]% of NAV exposed
     b) Regulatory regime change: [X]% of NAV in regulatory-dependent deals
     c) Financing freeze: [X]% of NAV in leveraged/cash deals
   - Hedge: Buy index puts or VIX calls sized to offset [X]% of event book in stress

5. **Position-level and portfolio-level limits**:
   - Single event max: [5-10]% of NAV
   - Single sector exposure (event type): [20-30]% of NAV
   - Total event gross exposure: [80-150]% of NAV
   - Net market beta of event book: Target [0.0 to 0.3]
   - Cash reserve: Keep [10-20]% undeployed for new opportunities
```

---

## Mathematical Frameworks Reference

**Merger Arb Spread Formula**:
Gross spread = (Deal price - Market price) / Market price.
Annualized spread = Gross spread x (365 / Days to close).
Implied break probability = Spread / (Spread + |Downside if break|).

**Break-Even Probability**:
P_breakeven = |Loss if break| / (Spread + |Loss if break|).
If your estimated P(close) > P_breakeven, the trade has positive expected value.

**Event Expected Value**:
EV = P(success) x Gain + P(failure) x Loss.
Only take positions where EV > 0 AND the spread compensates for illiquidity and tail risk.

**Annualized Return for Event Strategies**:
R_annual = (1 + R_event)^(365/T) - 1, where T = days to event resolution.
Compare across events on an annualized, risk-adjusted basis.

**Kelly for Binary Events**:
f* = p - q/b = p - (1-p) x |Loss|/Gain.
For a merger with 90% close probability, 5% upside, 30% downside:
f* = 0.90 - (0.10 x 30/5) = 0.90 - 0.60 = 0.30 (30% of capital).
Use 1/3 Kelly = 10% position size in practice.

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- Portfolio construction, risk decomposition
- [`fundamental-long-short.md`](fundamental-long-short.md) -- Fundamental analysis for activist targets
- [`credit-distressed.md`](credit-distressed.md) -- Distressed events, restructuring situations
- [`global-macro.md`](global-macro.md) -- Macro events (elections, referendums, policy changes)
