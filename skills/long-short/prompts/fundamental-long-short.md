# Fundamental Long/Short Equity

## Role Context

```
You are a senior long/short equity analyst at a $5B fundamental hedge fund. You think in
terms of variant perception -- where does the market's embedded expectation differ from
reality, and what catalyst will force convergence? Every idea must have an identifiable edge
over consensus, a catalyst with a timeline, an asymmetric risk/reward profile, and a
position size justified by Kelly criterion. You are deeply skeptical of "cheap on multiples"
pitches -- valuation alone is not a catalyst. You always ask: "What does the market already
know, and what am I seeing that it doesn't?"
```

---

## What This Desk Does

Fundamental long/short equity managers build concentrated portfolios of long positions in undervalued securities and short positions in overvalued ones, seeking to generate alpha from stock-specific insight while hedging broad market exposure. The edge comes from deeper fundamental research -- proprietary channel checks, expert network calls, supply chain analysis, and forensic accounting -- that produces a differentiated view (variant perception) before the market reprices. The strategy typically runs 30-60% net long with 150-200% gross exposure, targeting a portfolio Sharpe of 1.0-1.5 with low correlation to equity indices. Position concentration ranges from 20-40 names on the long side and 30-60 on the short side, reflecting the asymmetric payoff profile of each leg.

---

## 1. Idea Generation & Variant Perception

### Build a Variant Perception Case

```
I'm analyzing [company name / ticker] in the [industry] sector.

Current market consensus:
- Revenue growth expectation: [X]%
- Margin trajectory: [expanding / stable / contracting]
- Key narrative: [describe what "everyone believes"]

My variant perception:
- I believe [describe your differentiated view]
- Evidence supporting my view: [proprietary data points, channel checks, expert calls]
- Why the market is wrong: [anchoring bias / stale mental model / misunderstanding of business mix]

Help me stress-test this variant perception:
1. What are the strongest counterarguments to my thesis?
2. What data would DISPROVE my variant view? (pre-mortem: assume I'm wrong -- why?)
3. How differentiated is this view really? Check: sell-side consensus, buy-side positioning
   (13F filings), short interest, options skew -- do any suggest the market already agrees?
4. What is the embedded expectation in the current stock price?
   - Reverse DCF: What growth rate / margin / duration is priced in?
   - Implied expectations: Current P/E vs. historical range, EV/EBITDA vs. peers
5. Size the variant gap: If I'm right, what is fair value? What is the upside/downside ratio?

Framework -- Expected Value of the Position:
  EV = P(right) x Upside + P(wrong) x Downside
  Only proceed if EV > 0 AND the risk/reward ratio exceeds 2:1 for longs, 1.5:1 for shorts.
```

### Screen for Long/Short Candidates

```
I want to generate [long / short] ideas in the [sector / industry] space.

Screening criteria for longs:
- Accelerating revenue growth not yet reflected in estimates
- Margin inflection from [operating leverage / mix shift / cost restructuring]
- Under-followed by sell-side (fewer than [X] analysts)
- Insider buying in the last [X] months
- Short interest above [X]% (potential squeeze + market skepticism I can fade)

Screening criteria for shorts:
- Revenue quality deterioration (channel stuffing, pull-forward, accounting red flags)
- Margin peak with unrecognized headwinds
- Over-earning relative to normalized cycle
- Management turnover or aggressive accounting (DSO expansion, capitalized expenses)
- Valuation requires heroic growth assumptions to justify current price

For each candidate, provide:
1. The consensus narrative and where it might be wrong
2. The most likely catalyst and its timeline
3. A rough expected value calculation
```

---

## 2. Catalyst Identification & Timeline

### Map the Catalyst Calendar

```
For [company name / ticker], map all potential catalysts over the next [6 / 12 / 18] months:

Catalyst categories:
1. **Earnings**: Next report date, key metrics to watch, estimate revision trends
2. **Product cycle**: Product launches, FDA approvals, technology transitions
3. **M&A / corporate action**: Strategic review, activist involvement, takeout probability
4. **Management change**: New CEO/CFO, board composition shifts
5. **Regulatory**: Pending rulings, legislative risk, antitrust review
6. **Capital allocation**: Buyback authorization, dividend initiation, debt refinancing
7. **Index / technical**: Index inclusion/exclusion, lock-up expiry, option expiration

For each catalyst:
- Probability of occurring: [X]%
- Probability of favorable outcome given it occurs: [X]%
- Expected stock price impact if favorable: +[X]%
- Expected stock price impact if unfavorable: -[X]%
- Timeline: [specific date or date range]

Composite catalyst-adjusted expected return:
  E[R] = Sum over catalysts of: P(catalyst) x P(favorable|catalyst) x Impact_favorable
         + P(catalyst) x P(unfavorable|catalyst) x Impact_unfavorable
```

---

## 3. Position Sizing & Kelly Criterion

### Size a Position Using Kelly Framework

```
I have a trade idea in [company / ticker] with the following parameters:

My estimate of probability of winning: [X]%
Expected gain if right (upside to target): +[X]%
Expected loss if wrong (downside to stop): -[X]%
Current portfolio gross exposure: [X]%
Current portfolio net exposure: [X]%
Number of existing positions: [N]
Strategy max gross exposure: [X]%
Strategy max single-name concentration: [X]%

Calculate:
1. Full Kelly fraction:
   f* = (p/a) - (q/b)
   where p = P(win), q = P(loss), b = win/loss ratio, a = 1
   Equivalently: f* = (p x b - q) / b

2. Fractional Kelly (recommended: use 1/4 to 1/2 Kelly for real portfolios):
   f_actual = [0.25 / 0.33 / 0.50] x f*
   Rationale: Full Kelly maximizes geometric growth but has ~50% chance of 50% drawdown.
   Half Kelly gives ~75% of the growth rate with much lower drawdown risk.

3. Adjust for correlation: If this position is [X]% correlated with existing book,
   reduce size by: f_adjusted = f_actual x (1 - avg_correlation_with_book)

4. Check against hard limits:
   - Single name: max [3-5]% of NAV for high conviction, [1-2]% for standard
   - Sector: max [20-25]% gross in any one sector
   - Gross exposure post-trade: must remain below [X]%
   - Net exposure post-trade: must remain within [X]% to [X]% band

5. Position-level stop-loss:
   - Hard stop at [X]% loss from entry (typically 7-15% for longs, 15-25% for shorts)
   - Time stop: If catalyst hasn't materialized within [X] months, reassess
   - Thesis stop: If [specific falsification condition], exit regardless of P&L
```

---

## 4. Short Selling Analysis

### Evaluate a Short Candidate

```
I'm considering shorting [company name / ticker].

Short thesis: [describe why you believe the stock will decline]

Help me evaluate the short-specific risks:

1. **Borrow analysis**:
   - Current borrow rate: [X]% annualized (general collateral < 1%, hard-to-borrow > 5%)
   - Borrow availability: [easy / moderate / hard / very hard to locate]
   - Rebate rate: [X]% (negative rebate = you pay to short)
   - Is borrow stable or at risk of recall?

2. **Crowding risk**:
   - Short interest as % of float: [X]% (above 20% = elevated squeeze risk)
   - Days to cover: [X] days (short interest / avg daily volume)
   - Cost of borrow trend: rising borrow costs signal crowding
   - 13F analysis: How many hedge funds are short? (infer from put/call ratios)

3. **Squeeze risk assessment**:
   - Float characteristics: What % of shares are held by long-term holders (insiders, index)?
   - Recent short interest trend: Rising or falling?
   - Upcoming catalysts that could trigger a squeeze (earnings beat, M&A rumor, Reddit)
   - Options market: Is there significant short-dated call open interest?

4. **Negative catalyst identification**:
   - What specific event will cause the stock to decline?
   - Timeline for the catalyst
   - Is there an asymmetry problem? Shorts have capped upside (stock goes to zero)
     but unlimited downside (stock can go to infinity)

5. **Net expected return after carry costs**:
   Net short return = Price decline - Borrow cost - Dividends paid - Financing cost
   Annualized: Must exceed [hurdle rate] to justify the short vs. using a put spread

Risk/reward skew for shorts:
- Maximum gain: 100% (stock goes to zero) minus carry costs
- Maximum loss: Unlimited (though stops mitigate this)
- Recommendation: Size shorts at 50-70% of equivalent long conviction due to asymmetry
```

---

## 5. Portfolio Construction & Factor Management

### Construct a Factor-Neutral Long/Short Book

```
I'm managing a [long/short equity] portfolio with the following targets:
- Gross exposure target: [150-200]%
- Net exposure target: [20-50]%
- Number of positions: [40-80]
- Sector: [unconstrained / sector-focused in [X]]

Current factor exposures (beta to each factor):
- Market beta: [X]
- Size (SMB): [X]
- Value (HML): [X]
- Momentum (UMD): [X]
- Quality (QMJ): [X]
- Low volatility: [X]

Help me:
1. **Neutralize unintended factor bets**:
   - Target: Market beta [0.0 to 0.3], all style factors within [-0.2, +0.2]
   - Identify which positions are driving each factor tilt
   - Suggest hedge trades or position adjustments to neutralize

2. **Manage sector exposure**:
   - Max gross in any sector: [X]%
   - Max net in any sector: [X]% (to avoid sector bets dominating)
   - Current sector exposures: [list]

3. **Correlation management**:
   - Calculate average pairwise correlation of long book and short book separately
   - Target: Long book avg correlation < 0.3, short book avg correlation < 0.3
   - Long-short pair correlation: Ideally positive (both legs move together, spread compresses)

4. **Gross/net exposure management framework**:
   - Base case net: [X]% (normal conviction)
   - High conviction net: up to [X]% (strong directional view with catalyst support)
   - Defensive net: down to [X]% (macro uncertainty, drawdown regime)
   - Gross drives diversification benefit; net drives market beta

5. **Risk budgeting by position type**:
   - High conviction longs (top 10): [X]% of gross, [X]% of risk budget
   - Core longs (next 15-20): [X]% of gross, [X]% of risk budget
   - Tactical / trading longs: [X]% of gross, [X]% of risk budget
   - Alpha shorts (company-specific thesis): [X]% of gross
   - Factor / ETF shorts (hedging): [X]% of gross
```

### Risk/Reward Skew Analysis

```
For my current portfolio of [N] positions, analyze the aggregate risk/reward profile:

For each position, I have:
- Entry price, current price, target price, stop-loss price
- Conviction level: [high / medium / low]
- Catalyst timeline: [near-term / medium-term / long-dated]

Calculate:
1. Position-level upside/downside ratio: (Target - Current) / (Current - Stop)
2. Portfolio-weighted expected value:
   Portfolio EV = Sum of: Weight_i x [P(hit target)_i x Upside_i + P(hit stop)_i x Downside_i]
3. Win rate required to break even at current sizing
4. Portfolio skewness: Are we positioned for many small wins and few large losses (positive skew)
   or the reverse?
5. Identify positions where risk/reward has deteriorated since entry and should be trimmed

Minimum thresholds:
- Longs: Upside/downside > 2.0x, or trim
- Shorts: Upside/downside > 1.5x (adjusted for carry cost), or cover
- Portfolio aggregate: Weighted average upside/downside > 2.0x
```

---

## Mathematical Frameworks Reference

**Expected Value Framework**:
EV = P(win) x Gain - P(loss) x Loss. Only take trades where EV > 0 and risk/reward > 2:1.

**Kelly Criterion**:
f* = (p x b - q) / b where p = P(win), q = 1-p, b = win/loss ratio.
Use fractional Kelly (0.25-0.5x) in practice to reduce drawdown severity.

**Reverse DCF**:
Solve for the growth rate g in: Price = FCF_1 / (WACC - g).
Compare implied g to your estimate of sustainable growth to find mispricing.

**Factor Neutrality**:
Regress portfolio returns on Fama-French 5 + Momentum. Target alpha t-stat > 2.0
with all factor betas insignificantly different from zero.

---

## See Also

- [`../roles/hedge-fund-analyst.md`](../roles/hedge-fund-analyst.md) -- IC/IR, Black-Litterman, Deflated Sharpe
- [`event-driven.md`](event-driven.md) -- Catalyst-driven positions, activist situations
- [`credit-distressed.md`](credit-distressed.md) -- Equity stubs and capital structure trades
- [`quantitative-systematic.md`](quantitative-systematic.md) -- Factor models and signal testing
