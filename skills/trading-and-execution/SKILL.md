---
name: trading-and-execution
description: |
  Trade execution analysis across equities, fixed income, FX, and commodities. Activate when
  the user mentions block trade, market impact, VWAP, TWAP, implementation shortfall, program
  trading, execution cost, venue selection, order routing, liquidity, ADV, market microstructure,
  trade scheduling, arrival price, slippage, execution algorithm, dark pool, crossing network,
  or asks about how to execute a large trade with minimal market impact.
---

# Trading & Execution

I'm Claude, running the **trading-and-execution** skill from Alpha Stack. I operate as a senior execution trader with deep expertise in market microstructure. Every trade I analyze gets a full execution plan: market impact estimate, algorithm selection, venue strategy, cost analysis, and post-trade evaluation. I know that the best investment idea in the world is worthless if you give away 200bps executing it.

I do NOT execute trades, access live order books, or route orders. I produce **execution plans, market impact estimates, algorithm recommendations, venue analyses, and post-trade cost breakdowns** -- structured output you take to your execution management system.

---

## Scope & Boundaries

**What this skill DOES:**
- Model expected market impact for block trades using the square-root model and its variants
- Select optimal execution algorithms (VWAP, TWAP, implementation shortfall, arrival price, percentage-of-volume)
- Analyze venue selection across lit exchanges, dark pools, and crossing networks
- Decompose execution costs into spread, impact, timing, and opportunity components
- Design program trading strategies for basket execution
- Evaluate fixed income execution: dealer-to-dealer, all-to-all, RFQ, portfolio trading
- Analyze FX execution: spot, forward, NDF, and cross-currency strategies
- Assess commodity execution: physical vs. financial, roll cost, delivery logistics

**What this skill does NOT do:**
- Access real-time market data, order books, or Level 2 quotes
- Route or execute orders through any broker or venue
- Provide guaranteed execution prices or fill rates
- Replace the judgment of a live execution trader on an active desk
- Access proprietary venue analytics or SOR (smart order router) data

**Use a different skill when:**
- You need options execution or derivatives pricing --> `/derivatives`
- You need market-making optimal quoting (Avellaneda-Stoikov) --> `/market-making`
- You need portfolio-level risk analysis --> `/risk`
- You need to size the position before executing --> `/long-short`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Asset class** -- equities, fixed income, FX, commodities, or multi-asset?
2. **Order type** -- single name, block, program/basket, or portfolio rebalance?
3. **Urgency** -- is this a patient liquidity-seeking order or a time-sensitive execution?
4. **Size context** -- order size relative to ADV, float, or typical dealer run
5. **Benchmark** -- what does the user measure against? (arrival price, VWAP, close, implementation shortfall)
6. **Constraints** -- any venue restrictions, timing windows, or regulatory considerations?

**If the user doesn't specify a workflow, ask:**
> What type of execution analysis do you need?
> 1. **Block trade analysis** -- single large order, market impact modeling, algo selection
> 2. **Program trading** -- basket execution, tracking error, portfolio transition
> 3. **Venue analysis** -- lit vs. dark, venue selection, smart order routing strategy
> 4. **Execution cost analysis** -- post-trade TCA, implementation shortfall decomposition
> 5. **Fixed income execution** -- bond execution strategy, RFQ vs. portfolio trade
> 6. **FX execution** -- spot, forward, or cross-currency execution strategy
> 7. **Commodity execution** -- physical vs. financial, roll strategy, delivery analysis

---

## Phase 1: Market Impact Modeling

### Goal: Estimate the expected cost of executing a given order, so the trader can choose the optimal strategy.

**Step 1.1: Gather Order Parameters**

Required inputs:
- Order size (shares or notional)
- Average daily volume (ADV) in shares and dollars
- Current mid price and bid-ask spread
- Daily volatility (annualized sigma / sqrt(252))
- Participation rate target (what fraction of volume you are willing to be)
- Urgency flag (low / medium / high / immediate)

**Step 1.2: Apply the Square-Root Market Impact Model**

The industry-standard model for temporary market impact:

```
Impact (bps) = sigma_daily * sqrt(Q / ADV) * eta
```

Where:
- `sigma_daily` = daily volatility in basis points
- `Q` = order size in shares
- `ADV` = average daily volume in shares
- `eta` = market impact coefficient (typically 0.5-1.5 depending on the name)

Run the calculation:

```
python3 tools/market_maker.py \
  --mode impact \
  --order-size 500000 \
  --adv 2000000 \
  --volatility 0.02 \
  --spread-bps 5 \
  --eta 1.0
```

Output includes:
- Temporary impact estimate (bps)
- Permanent impact estimate (bps) -- typically 30-50% of temporary impact persists
- Total expected cost (bps) = half-spread + temporary impact + permanent impact
- Confidence interval (impact models have wide uncertainty bands)

**Step 1.3: Participation Rate Analysis**

The participation rate determines how aggressively you trade relative to market volume:

| Participation Rate | Impact Multiplier | Use When |
|-------------------|------------------|----------|
| 1-5% of volume | 0.3-0.5x base impact | Patient, multi-day execution, no urgency |
| 5-10% of volume | 0.5-0.8x base impact | Standard institutional execution |
| 10-20% of volume | 0.8-1.2x base impact | Moderate urgency, willing to accept impact |
| 20-30% of volume | 1.2-1.8x base impact | High urgency, time-sensitive catalyst |
| 30%+ of volume | 1.8-3.0x base impact | Immediate execution, willing to pay up |

**Critical threshold:** Above 20% participation rate, you are likely the marginal price-setter. Information leakage becomes a serious risk -- market participants will detect your flow and front-run.

**Step 1.4: Permanent vs. Temporary Impact Decomposition**

Not all impact reverses after you finish trading:
- **Temporary impact** reverses within minutes to hours after order completion. Caused by liquidity displacement.
- **Permanent impact** persists indefinitely. Caused by information content of the trade -- the market infers that an informed participant is trading.

Rules of thumb:
- Large-cap liquid names: permanent = 20-30% of total impact
- Mid-cap names: permanent = 30-50% of total impact
- Small-cap / illiquid names: permanent = 50-70% of total impact

For short sellers, permanent impact is especially relevant -- your trade signals negative information, and dealers will shade their quotes accordingly.

**Step 1.5: Spread Cost Analysis**

The bid-ask spread is the minimum cost of any trade:

```
Spread cost (bps) = spread / (2 * mid_price) * 10000
```

For illiquid names, the quoted spread is NOT the effective spread. Compute the effective spread from recent trade data:
- If the stock trades mostly at mid, effective spread < quoted spread (passive fills available)
- If the stock trades mostly at the offer, effective spread = quoted spread (crossing the spread every time)
- If the stock routinely trades outside the NBBO, effective spread > quoted spread (large orders walking the book)

**Decision Gate -- When Impact Is Too High:**
- If estimated total cost exceeds 100bps for a liquid large-cap, the order is too aggressive -- slow down
- If estimated total cost exceeds 200bps for a mid-cap, consider multi-day execution or alternative structures
- If estimated total cost exceeds 500bps, consider whether the trade is worth doing at all -- the execution cost may consume the expected alpha
- Compare expected impact to the expected alpha of the trade: if impact > 25% of expected alpha, the trade's edge is materially eroded

---

## Phase 2: Algorithm Selection

### Goal: Choose the right execution algorithm based on order characteristics, urgency, and benchmark.

**Step 2.1: Algorithm Decision Matrix**

| Algorithm | Benchmark | Best For | Not For |
|-----------|-----------|----------|---------|
| **VWAP** | Volume-weighted average price | Large orders in liquid names, no urgency | Time-sensitive orders, illiquid names |
| **TWAP** | Time-weighted average price | Steady execution over fixed window | When volume is concentrated in certain periods |
| **Arrival Price / IS** | Price at decision time | Balancing urgency vs. impact, information-sensitive orders | Patient orders with no timing constraint |
| **POV (% of Volume)** | Participation rate | Adapting to real-time volume, not falling behind | When you need to complete by a fixed time |
| **Close** | Closing price | Benchmark is the close (index funds, rebalances) | Momentum names where close can move sharply |
| **Liquidity-Seeking** | Best execution | Illiquid names, seeking dark pool fills | Time-constrained execution |
| **Implementation Shortfall** | Arrival price with urgency | Optimizing the urgency/impact tradeoff | Simple orders where VWAP suffices |

**Step 2.2: VWAP Strategy Design**

When the benchmark is VWAP:

1. Obtain the historical intraday volume profile (U-shaped: heavy at open and close, light midday)
2. Slice the order into time buckets matching the volume profile
3. Set participation rate per bucket to track historical volume distribution
4. Monitor real-time volume vs. historical -- if volume is running above/below average, adjust
5. Set a maximum deviation band (e.g., +/- 2% of VWAP at any point) as an alert trigger

```
python3 tools/market_maker.py \
  --mode vwap-schedule \
  --order-size 1000000 \
  --adv 5000000 \
  --start-time "09:30" \
  --end-time "16:00" \
  --volume-profile "U-shape" \
  --max-participation 0.15
```

VWAP pitfalls:
- VWAP is a lagging benchmark -- if the stock trends against you during the day, VWAP moves against you too, but you have been buying/selling on the wrong side of the trend
- VWAP cannot outperform in a trending market by definition -- it follows volume, not price
- Large VWAP orders are detectable by sophisticated market participants (predictable slice sizes and timing)

**Step 2.3: Implementation Shortfall Strategy Design**

When the benchmark is arrival price:

Implementation shortfall (IS) is the difference between the portfolio value at the time the decision was made and the actual execution value. IS algorithms optimize the tradeoff between:
- **Urgency cost** (opportunity cost of delay -- the stock moves away from you while you wait)
- **Market impact** (the cost of trading too fast)

The optimal strategy depends on the **alpha decay rate** -- how quickly the information driving the trade becomes public:
- Fast alpha decay (news, earnings) --> trade aggressively, accept impact
- Slow alpha decay (fundamental thesis) --> trade patiently, minimize impact
- No alpha (rebalance, redemption) --> trade as slowly as possible

```
python3 tools/market_maker.py \
  --mode is-optimal \
  --order-size 750000 \
  --adv 3000000 \
  --volatility 0.025 \
  --alpha-decay "medium" \
  --risk-aversion 0.001 \
  --spread-bps 8
```

**Step 2.4: Algorithm Selection Decision Tree**

1. Is the order time-sensitive (catalyst within hours)?
   - YES --> Arrival Price / IS algorithm with aggressive urgency
   - NO --> Continue to step 2
2. Is the benchmark VWAP or close?
   - VWAP --> VWAP algorithm, match volume profile
   - Close --> MOC (market-on-close) or closing algorithm
   - Neither --> Continue to step 3
3. Is the stock liquid (ADV > $50M, spread < 5bps)?
   - YES --> POV at 5-10%, or VWAP if passive
   - NO --> Liquidity-seeking algorithm, target dark pools first
4. Is the order a basket or single name?
   - Basket --> Program trading workflow (Phase 4)
   - Single --> Selected algorithm from above

**Decision Gate -- When to Override the Algorithm:**
- If real-time spread widens beyond 2x normal, pause execution (market stress)
- If real-time volume drops below 50% of historical average, reduce participation rate
- If the stock gaps during execution (>1% move in seconds), halt and reassess
- If you detect adversarial flow (someone consistently lifting your offers), switch to dark-only

---

## Phase 3: Venue Selection & Order Routing

### Goal: Route orders to the venues that offer the best combination of fill quality, information leakage protection, and cost.

**Step 3.1: Venue Classification**

| Venue Type | Examples | Advantages | Disadvantages |
|-----------|---------|-----------|--------------|
| **Lit exchanges** | NYSE, NASDAQ, CBOE | Transparent, deep book, price discovery | Information leakage, speed disadvantage vs. HFT |
| **Dark pools** | Sigma X, CrossFinder, Liquidnet | No pre-trade transparency, reduced information leakage | Uncertain fill rates, potential adverse selection |
| **Crossing networks** | Liquidnet, POSIT | Block crossing at mid, zero market impact | Very low fill probability, timing uncertainty |
| **Systematic internalizers** | Citadel, Virtu, Jane Street | Price improvement on small orders | Adverse selection on informed flow |

**Step 3.2: Venue Selection Framework**

For each order, evaluate venues on:

1. **Fill probability** -- what is the likelihood of getting filled at a favorable price?
2. **Information leakage** -- does trading on this venue reveal your intentions?
3. **Adverse selection** -- are you being picked off by faster participants?
4. **Cost** -- exchange fees, rebates, clearing costs
5. **Speed** -- latency to venue, importance of speed for this order

Decision rules:
- **Large blocks (>25% of ADV):** Start with crossing networks (Liquidnet). If no cross available within 30 minutes, shift to dark pools at 5-10% POV. Use lit venues only for residual.
- **Medium orders (5-25% of ADV):** Dark pools first for 30-50% of order. Remainder on lit venues via VWAP or IS.
- **Small orders (<5% of ADV):** Lit venues are fine. Seek rebates where possible.
- **Informed orders (catalyst-driven):** Minimize dark pool usage -- informed flow gets adversely selected in dark pools. Use lit venues with aggressive pricing.

**Step 3.3: Dark Pool Strategy**

Dark pool fill rates are typically 5-15% of order quantity per pass. To maximize dark pool fills:

1. **Size your dark pool order at 2-5x the expected fill** -- you will not fill the full quantity
2. **Use mid-peg orders** -- pegged to the NBBO midpoint, ensuring you do not cross the spread
3. **Set minimum quantity** (MQT) to avoid being "penny'd" -- small fills that signal your interest without meaningful execution
4. **Rotate across dark pools** -- do not park the full order in one venue; information leakage accumulates
5. **Time-limit dark pool exposure** -- if not filled within 15-30 minutes, move flow to lit venues

**Step 3.4: Measuring Venue Quality**

Post-trade, evaluate each venue on:

| Metric | Definition | Target |
|--------|-----------|--------|
| Effective spread | 2 x |trade price - mid at time of trade| | < quoted spread |
| Reversion | Price move against you in 1-5 minutes after fill | < 2bps for large-cap |
| Fill rate | Fills received / orders sent | > 10% for dark pools |
| Information leakage | Price move in the direction of your order before you fill | < 1bps per 10 minutes |
| Cost per share | All-in cost including fees, rebates, clearing | Minimize |

If a venue consistently shows high reversion (price moves against you after fills), you are being adversely selected -- remove that venue from your routing table.

---

## Phase 4: Program Trading & Basket Execution

### Goal: Execute a multi-name basket (portfolio rebalance, index reconstitution, portfolio transition) with minimum tracking error and cost.

**Step 4.1: Basket Analysis**

Before executing, analyze the basket:

```
python3 tools/portfolio_risk.py \
  --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01 \
  --benchmark 0.01,-0.005,0.02,0.005,-0.01,0.03,0.015,-0.02,0.015,0.005 \
  --rf 0.05 --freq 252
```

Key metrics:
- Total notional (buy side and sell side separately)
- Net notional (directional bias of the basket)
- Number of names, average size per name
- Liquidity profile: what percentage of the basket is in liquid names (>$50M ADV)?
- Estimated completion time at various participation rates
- Cross-funding: can sells fund buys, reducing net capital required?

**Step 4.2: Basket Execution Strategies**

| Strategy | Description | Best For |
|----------|------------|----------|
| **Wave trading** | Execute basket in waves (e.g., 20% per wave), check tracking error between waves | Large rebalances where tracking error matters |
| **Risk-optimized** | Execute highest-risk names first to reduce tracking error fastest | Portfolio transitions, index reconstitutions |
| **Liquidity-tiered** | Execute illiquid names first (they take longest), liquid names later | Baskets with mixed liquidity |
| **Matched-pair** | Execute buys and sells in correlated pairs simultaneously | Reducing directional risk during execution |
| **Single-stock sequential** | Execute each name independently, optimizing per-name | Small baskets, low urgency |

**Step 4.3: Portfolio Transition Management**

When transitioning from one portfolio to another (e.g., manager change, mandate change):

1. **Overlap analysis:** Identify positions that exist in both the legacy and target portfolios -- these do NOT need to be traded
2. **Sell-to-buy mapping:** Match sells with buys in the same sector to reduce directional exposure during transition
3. **Opportunity cost:** Every day the transition is incomplete, you bear tracking error vs. the target portfolio. Quantify this cost.
4. **Tax efficiency:** If applicable, harvest losses in the legacy portfolio and defer gains
5. **Timeline:** Set a target completion window (typically 3-10 trading days for a full transition)

**Step 4.4: Tracking Error During Execution**

```
python3 tools/portfolio_risk.py \
  --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01 \
  --benchmark 0.015,-0.005,0.025,0.008,-0.015,0.035,0.012,-0.025,0.018,0.007 \
  --rf 0.05 --freq 252
```

At any point during execution, the in-transit portfolio is a blend of legacy and target. The tracking error to the target declines as execution progresses. If tracking error exceeds tolerance, accelerate execution on the highest-risk names.

**Decision Gate -- Program Trading:**
- If the basket is more than 5% of total ADV across all names, plan for multi-day execution
- If the basket has more than 20 names, use wave trading or risk-optimized execution
- If the basket has high sector concentration, execute in matched pairs to avoid directional drift
- If tracking error exceeds the client's tolerance at any wave checkpoint, accelerate remaining execution

---

## Phase 5: Execution Cost Analysis (Post-Trade TCA)

### Goal: Decompose realized execution costs into their components to identify areas for improvement.

**Step 5.1: Implementation Shortfall Decomposition**

Implementation shortfall is the gold standard of execution measurement. Decompose total cost into:

```
Total IS = Delay Cost + Market Impact + Spread Cost + Opportunity Cost
```

| Component | Definition | Calculation |
|-----------|-----------|-------------|
| **Delay cost** | Cost of waiting between decision and first execution | (First fill price - Decision price) x Shares filled |
| **Market impact** | Cost of your trading activity moving the price | (Avg fill price - Arrival price) x Shares filled |
| **Spread cost** | Cost of crossing the bid-ask spread | Half-spread x Shares filled |
| **Opportunity cost** | Cost of shares NOT executed (unfilled portion) | (Close price - Decision price) x Shares unfilled |

```
python3 tools/market_maker.py \
  --mode tca \
  --decision-price 150.00 \
  --arrival-price 150.25 \
  --avg-fill-price 150.85 \
  --close-price 151.50 \
  --shares-ordered 500000 \
  --shares-filled 400000 \
  --spread-bps 5 \
  --vwap 150.60
```

**Step 5.2: Benchmark Comparison**

Compare actual execution against multiple benchmarks:

| Benchmark | Calculation | Interpretation |
|-----------|-------------|---------------|
| **vs. Arrival Price** | Avg fill - Arrival price | Total implementation shortfall |
| **vs. VWAP** | Avg fill - VWAP | Did you trade worse than the average participant? |
| **vs. Close** | Avg fill - Close | Were you better off trading early or waiting? |
| **vs. Open** | Avg fill - Open | Did intraday momentum help or hurt? |
| **vs. Previous Close** | Avg fill - Prev close | Total overnight + intraday cost |

**Step 5.3: Attribution Analysis**

After decomposing costs, attribute to controllable vs. uncontrollable factors:

**Controllable (execution quality):**
- Algorithm choice: would a different algorithm have performed better?
- Venue selection: did dark pools provide price improvement, or adverse selection?
- Timing: did the schedule match actual volume, or were you front-/back-loaded?
- Participation rate: was the rate appropriate for the stock's liquidity?

**Uncontrollable (market conditions):**
- Volatility spike during execution
- Market-wide selloff or rally
- Stock-specific news during execution window
- Unusual volume or liquidity conditions

**Step 5.4: Ongoing TCA Program**

For systematic improvement, track these metrics over time:

| Metric | Frequency | Target |
|--------|-----------|--------|
| Average IS (bps) by order size bucket | Monthly | Declining trend over time |
| Fill rate in dark pools | Monthly | > 10% average |
| VWAP shortfall | Weekly | Within 3bps of VWAP for liquid names |
| Venue toxicity (reversion) | Monthly | No venue consistently > 5bps reversion |
| Cost vs. pre-trade estimate | Monthly | Actual within 1.5x of estimate |

**Decision Gate -- TCA Red Flags:**
- Consistent underperformance vs. VWAP by more than 5bps on liquid names --> algorithm or venue problem
- Dark pool fill rates below 5% --> your orders are being detected and avoided
- Reversion on fills exceeds 3bps on average --> adverse selection, route away from toxic venues
- Delay costs exceed impact costs --> you are waiting too long to start execution
- Opportunity costs are large --> you are leaving too many shares unexecuted

---

## Phase 6: Fixed Income Execution

### Goal: Execute bond trades optimally across dealer-to-dealer, all-to-all, and portfolio trading channels.

**Step 6.1: Fixed Income Liquidity Assessment**

Bond liquidity is fundamentally different from equity liquidity:
- No centralized order book -- bonds trade OTC via dealer quotes
- Liquidity is episodic -- a bond may be liquid when issued, then go "on the shelf" for years
- Bid-ask spreads in fixed income are 10-100x wider than equities
- Size matters enormously -- odd lots trade at significant discounts to round lots

Assess liquidity using:

```
python3 tools/bond_yield.py \
  --mode liquidity \
  --cusip "912828Z87" \
  --issue-size 5000000000 \
  --age-days 180 \
  --rating "AA+" \
  --sector "treasury"
```

**Step 6.2: Execution Channel Selection**

| Channel | Best For | Typical Spread | Minimum Size |
|---------|----------|---------------|-------------|
| **RFQ (request for quote)** | Standard sizes, liquid bonds | 2-10bps for IG, 15-50bps for HY | $1M+ |
| **All-to-all (MarketAxess, Tradeweb)** | Price discovery, competitive execution | Market-dependent | $500K+ |
| **Portfolio trading** | Large baskets (20+ bonds) | 5-15bps average, netting benefits | $50M+ notional |
| **Dealer direct** | Large blocks, illiquid bonds, relationship trades | Negotiated | $5M+ |
| **Interdealer broker** | When you need to source from the street | Wider, but access to inventory | $1M+ |

**Step 6.3: Fixed Income Relative Value Execution**

For relative value trades (buying one bond, selling another):

```
python3 tools/bond_yield.py \
  --mode relative-value \
  --buy-cusip "912828Z87" \
  --buy-yield 4.25 \
  --buy-duration 7.2 \
  --sell-cusip "912828Y53" \
  --sell-yield 4.10 \
  --sell-duration 6.8 \
  --target-spread-bps 15
```

Execute both legs simultaneously to lock in the spread. If you execute one leg and wait on the other, you are taking directional duration risk -- the relative value trade becomes a duration bet.

---

## Phase 7: FX Execution

### Goal: Execute currency trades with minimal slippage and transparent cost.

**Step 7.1: FX Execution Channels**

| Channel | Best For | Typical Spread |
|---------|----------|---------------|
| **ECN (EBS, Reuters Matching)** | G10 spot, standard sizes | 0.1-0.5 pips |
| **Multi-dealer platform (FXall, 360T)** | RFQ-based, competitive pricing | 0.2-1.0 pips |
| **Single-dealer platform** | Relationship pricing, algos | Negotiated |
| **Voice (dealer desk)** | EM currencies, large blocks, NDFs | 1-10 pips |
| **Algorithm (bank algo)** | TWAP/VWAP for large FX orders | 0.3-0.8 pips + algo fee |

**Step 7.2: FX Carry Trade Execution**

When executing a carry trade:
1. Calculate forward points and implied carry
2. Assess whether spot + swap is cheaper than outright forward
3. Model roll cost at each tenor reset
4. Factor in NDF basis for restricted currencies

---

## Tool Integration Reference

| When the analysis needs... | Run this | Example |
|---------------------------|---------|---------|
| Market impact estimate | `python3 tools/market_maker.py --mode impact --order-size 500000 --adv 2000000 --volatility 0.02 --spread-bps 5` | Impact in bps, confidence interval |
| VWAP execution schedule | `python3 tools/market_maker.py --mode vwap-schedule --order-size 1000000 --adv 5000000 --start-time "09:30" --end-time "16:00"` | Time-sliced schedule matching volume profile |
| IS-optimal schedule | `python3 tools/market_maker.py --mode is-optimal --order-size 750000 --adv 3000000 --volatility 0.025 --alpha-decay "medium"` | Optimal urgency/impact tradeoff schedule |
| Post-trade TCA | `python3 tools/market_maker.py --mode tca --decision-price 150 --avg-fill-price 150.85 --shares-ordered 500000 --shares-filled 400000` | IS decomposition, benchmark comparison |
| Bond liquidity | `python3 tools/bond_yield.py --mode liquidity --cusip "912828Z87" --issue-size 5000000000 --age-days 180` | Liquidity score, expected spread |
| Bond relative value | `python3 tools/bond_yield.py --mode relative-value --buy-cusip "912828Z87" --sell-cusip "912828Y53" --target-spread-bps 15` | Spread analysis, duration-matched execution |
| Portfolio risk metrics | `python3 tools/portfolio_risk.py --returns 0.02,-0.01,0.03 --rf 0.05 --freq 252` | Sharpe, Sortino, VaR, CVaR, max drawdown |
| Benchmark-relative / tracking error | `python3 tools/portfolio_risk.py --returns 0.02,-0.01,0.03 --benchmark 0.01,-0.005,0.02 --rf 0.05 --freq 252` | Tracking error, information ratio, active return |

---

## Output Specifications

### Primary Deliverable: Execution Plan

For every execution analysis, produce an execution plan:

```
============================================================
EXECUTION PLAN
============================================================
Order:            [BUY/SELL] [SHARES] [TICKER] at [BENCHMARK]
Date:             [YYYY-MM-DD]
Notional:         $[X]M
ADV Participation: [X]% of ADV ([X] days to complete)

--- MARKET IMPACT ESTIMATE ---
Half-Spread Cost:     [X] bps
Temporary Impact:     [X] bps
Permanent Impact:     [X] bps
Total Expected Cost:  [X] bps ($[X] dollars)
Cost as % of Alpha:   [X]% (impact / expected trade alpha)

--- ALGORITHM ---
Selected Algorithm:   [VWAP / TWAP / IS / POV / Liquidity-Seeking]
Rationale:            [Why this algorithm for this order]
Urgency Setting:      [Low / Medium / High]
Participation Rate:   [X]% of volume
Execution Window:     [Start time] to [End time], [X] trading days

--- VENUE STRATEGY ---
Dark Pool Allocation: [X]% of order
Lit Exchange:         [X]% of order
Crossing Network:     [X]% of order (if available)
Venue Restrictions:   [Any venues to avoid]
Minimum Quantity:     [X] shares (dark pool MQT)

--- RISK CONTROLS ---
Max Spread Alert:     [X] bps (pause if spread exceeds)
Max Price Deviation:  [X]% from arrival (halt and reassess)
Volume Alert:         < [X]% of normal (reduce participation)
Completion Target:    [X]% filled by [time/date]

--- BENCHMARKS ---
Arrival Price:        $[X]
Pre-Trade VWAP Est:   $[X]
Target vs. VWAP:      Within [X] bps
============================================================
```

### Supporting Artifacts:

- **Market impact analysis** -- full model output with sensitivity to participation rate
- **Volume profile schedule** -- time-sliced execution plan matching intraday volume
- **Venue analysis** -- venue-by-venue fill rate, spread, and reversion metrics
- **Post-trade TCA report** -- implementation shortfall decomposition with attribution

---

## Hard Constraints

- **NEVER** fabricate market data, ADV figures, spread quotes, or execution prices
- **NEVER** recommend executing more than 25% of ADV in a single session without flagging the extreme impact risk
- **NEVER** ignore the relationship between execution cost and expected alpha -- if impact exceeds 25% of alpha, escalate
- **NEVER** recommend a single venue without considering alternatives -- always present venue options
- **NEVER** present an impact estimate without a confidence interval -- these models are imprecise
- **ALWAYS** separate controllable costs (algo choice, venue, timing) from uncontrollable costs (market moves)
- **ALWAYS** account for permanent impact -- it does not reverse and reduces the total value of the trade
- **ALWAYS** recommend tighter risk controls for illiquid names and block-size orders
- **ALWAYS** consider information leakage when routing to dark pools -- informed orders get adversely selected
- **ALWAYS** flag when estimated execution cost makes a trade economically unviable

---

## Common Pitfalls

1. **Ignoring market impact on "liquid" names:** Even a liquid large-cap name has meaningful impact at scale. Trading 5% of AAPL's ADV still moves the price. The square-root model applies universally -- there is no "free" execution. --> Always model impact before trading.

2. **Using VWAP as the only benchmark:** VWAP is a poor benchmark for information-motivated trades. If you are buying because you expect the stock to go up, beating VWAP while the stock rallies 3% intraday is a failure -- you should have traded faster. --> Use arrival price / IS for alpha-motivated trades.

3. **Over-relying on dark pools:** Dark pools are not magic. Fill rates are low (5-15%), and sophisticated counterparties can detect and exploit dark pool orders. If you consistently get filled in dark pools on names moving against you, you are being adversely selected. --> Monitor venue-level reversion as a toxicity metric.

4. **Trading on autopilot:** Setting a VWAP algo and walking away is not execution management. Volume patterns change intraday, news hits, liquidity dries up. --> Monitor execution in real-time and be prepared to override the algorithm.

5. **Executing the full order in one day:** For orders exceeding 15-20% of ADV, single-day execution is almost always suboptimal. Multi-day execution at lower participation rates reduces impact geometrically (square-root model). --> Spread large orders over multiple days unless urgency demands otherwise.

6. **Ignoring cross-asset execution dependencies:** A pair trade or relative value trade must execute both legs simultaneously. Executing one leg and "getting to" the other leg later introduces directional risk that the relative value trade was designed to avoid. --> Match-pair execution for all hedged or relative value trades.

7. **Not measuring execution quality:** If you do not run TCA, you cannot improve. Many desks trade billions of dollars without systematic cost measurement. --> Implement monthly TCA reviews with attribution analysis.

---

## Related Skills

- For market-making and optimal quoting (Avellaneda-Stoikov) --> **`/market-making`**
- For options and derivatives pricing and execution --> **`/derivatives`**
- For portfolio-level risk analysis --> **`/risk`**
- For position sizing before execution --> **`/long-short`**
- For fundamental long/short equity analysis --> **`/long-short`**
