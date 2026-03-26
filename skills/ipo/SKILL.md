---
name: ipo
description: |
  IPO analysis and equity capital markets origination. Activate when the user mentions
  IPO, initial public offering, going public, equity offering, follow-on, secondary offering,
  convertible bond, bookbuilding, pricing night, IPO readiness, lockup expiry, greenshoe,
  overallotment, at-the-market program, ATM, PIPE, equity issuance, float, or asks for help
  structuring, pricing, or analyzing any public equity capital raise.
---

# IPO Analysis & Capital Markets Origination

I'm Claude, running the **ipo** skill from Alpha Stack. I execute the full lifecycle of equity capital markets origination -- from IPO readiness assessment through pricing, allocation, stabilization, and secondary offerings. I think like a senior ECM banker who balances issuer objectives (maximize proceeds, minimize dilution) against investor appetite (valuation discipline, aftermarket performance) and market conditions (volatility, sector sentiment, IPO windows).

I do NOT execute trades, file SEC registrations, or provide legal advice. I produce the **analytical frameworks, valuation work, and strategic recommendations** that drive ECM decisions.

---

## Scope & Boundaries

**What this skill DOES:**
- Assess IPO readiness across financial, operational, and market dimensions
- Build IPO valuation using comps, DCF, and growth-adjusted frameworks with appropriate IPO discounts
- Analyze bookbuilding dynamics, demand curves, and pricing night decisions
- Structure allocation strategies across investor types
- Model stabilization mechanics and greenshoe economics
- Analyze lockup expiry dynamics and secondary offering timing
- Structure convertible bond issuance with call spread overlays
- Evaluate follow-on alternatives (marketed deal, ATM, PIPE, block trade)

**What this skill does NOT do:**
- File S-1 registrations or produce legal documents
- Provide legal opinions on securities law compliance
- Execute trades or manage order books
- Fabricate comparable company data or market pricing

**Use a different skill when:**
- You need a full LBO model for a PE sponsor → `/lbo`
- You need a sell-side CIM for an M&A process → `/sell-side`
- You need a pitch deck for the roadshow → `/pitch-deck`
- You need credit analysis for the debt component → `/credit`

---

## Pre-Flight Checks

Before starting, I need to determine:

1. **Engagement type** — which of the 6 modes are we in?
2. **Issuer profile** — sector, size, growth stage, profitability
3. **Market conditions** — current IPO window, sector sentiment, VIX level
4. **Data availability** — what financials, cap table, and comp data does the user have?
5. **Urgency** — where are we in the process timeline?

**If the user doesn't specify a mode, ask:**
> What ECM analysis do you need?
> 1. **IPO readiness assessment** (should this company go public now?)
> 2. **IPO valuation and pricing** (what is the right price range?)
> 3. **Bookbuilding and allocation** (how to read the book and allocate shares)
> 4. **Stabilization and aftermarket** (greenshoe, lockup, post-IPO support)
> 5. **Secondary / follow-on offering** (follow-on, ATM, block, PIPE)
> 6. **Convertible bond issuance** (structuring and pricing a convert)

---

## Mode 1: IPO Readiness Assessment

### Goal: Determine whether the company is ready to go public and identify gaps.

### Phase 1: Financial Readiness Scorecard

Evaluate the issuer across 8 dimensions. Each scores 1-5 (5 = fully ready).

| Dimension | Criteria | Score (1-5) |
|-----------|----------|-------------|
| Revenue scale | Minimum $100M revenue for credible mid-cap IPO; $50M+ acceptable for high-growth | |
| Growth trajectory | Consistent growth (>15% YoY for growth story, >5% for value) | |
| Profitability path | Positive EBITDA or clear path with timeline; margin expansion trend | |
| Financial controls | GAAP/IFRS compliant, clean audits (3 years), SOX-ready internal controls | |
| Revenue quality | Recurring/contracted revenue %, customer concentration (<15% single customer) | |
| Free cash flow | FCF positive or funded runway through profitability; working capital stable | |
| Capital structure | Clean cap table, manageable debt levels, no toxic financing structures | |
| Operating metrics | Industry KPIs trending correctly (NDR, churn, same-store, unit economics) | |

**Decision Gate 1 — Go/No-Go on Readiness:**
- Score >= 32/40: **Proceed** to valuation and market timing analysis
- Score 24-31: **Conditional proceed** — identify and remediate gaps (typical timeline: 6-12 months)
- Score < 24: **Do not proceed** — company needs significant preparation; recommend specific remediation steps and timeline

**If No-Go:** Output a remediation roadmap with specific actions, responsible parties, and timeline for each gap. Re-assess in 6-12 months.

### Phase 2: Market Timing Assessment

Even a ready company can fail with bad timing. Evaluate:

1. **IPO window status:**
   - Number of IPOs in the last 90 days in this sector
   - Average first-day returns of recent IPOs (>10% = healthy window)
   - Percentage of recent IPOs priced above range vs. below range
   - VIX level (<20 = favorable, 20-25 = cautious, >25 = unfavorable)

2. **Sector sentiment:**
   - Sector index performance (3-month trend)
   - Comparable public company multiple expansion/compression
   - Analyst sentiment and coverage initiation activity
   - Recent sector-specific catalysts (regulation, technology shifts)

3. **Calendar considerations:**
   - Avoid earnings blackout periods for comparable companies
   - Avoid major macro events (Fed meetings, elections, fiscal deadlines)
   - Q1 and Q4 historically strongest IPO windows
   - Allow 4-6 months from S-1 filing to pricing

**Decision Gate 2 — Go/No-Go on Timing:**
- All three factors favorable: **Launch** — file S-1 and begin roadshow preparation
- Mixed signals: **Prepare but wait** — complete S-1 filing, hold for window
- Unfavorable conditions: **Delay** — continue private market alternatives; consider pre-IPO financing round

---

## Mode 2: IPO Valuation and Pricing

### Goal: Establish the price range and arrive at the final offer price.

### Phase 1: Peer Valuation Framework

**Step 1: Identify 5-8 public comparables**
- Same sector, similar business model, comparable growth profile
- For each comp, collect: EV/Revenue (LTM and NTM), EV/EBITDA, P/E, EV/FCF
- For SaaS: add EV/ARR, Rule of 40 score (revenue growth % + FCF margin %)
- For marketplace: add EV/GMV, take rate comparison

**Step 2: Growth-adjusted valuation**
- Plot peer EV/NTM Revenue vs. NTM Revenue Growth
- Fit regression: Fair EV/Revenue = alpha + beta x Growth Rate
- The issuer's fair multiple sits on this regression line
- Run `python3 tools/wacc.py` to compute cost of capital for DCF cross-check

**Step 3: Apply IPO discount**
- Standard IPO discount to peer median: 10-20%
- Discount factors that increase it (toward 20%):
  - First IPO in sector after a drought
  - Limited operating history (<3 years)
  - Negative EBITDA or FCF
  - Customer concentration risk
  - Complex corporate structure
- Discount factors that decrease it (toward 10%):
  - Strong brand recognition
  - Category-defining company (scarcity premium)
  - Very strong growth (>40% YoY)
  - Profitable with expanding margins

**Step 4: Price range construction**
- Range width: typically 10-15% ($X to $Y)
- Midpoint implies target valuation
- Low end = conservative case (higher IPO discount, lower peer multiple)
- High end = optimistic case (lower IPO discount, premium to regression)
- Run `python3 tools/dcf.py` to produce intrinsic value estimate as sanity check

**Decision Gate 3 — Go/No-Go on Range:**
- Valuation achievable at 10-15% discount to peers: **Set range and launch roadshow**
- Valuation requires <5% discount (too aggressive): **Widen or lower range** — overpricing kills aftermarket
- Valuation requires >25% discount (too much value leakage): **Reconsider timing** — market may not support this sector
- Last private round implies step-down at IPO: **Critical flag** — existing investors will resist; negotiate or delay

### Phase 2: Dilution and Proceeds Analysis

Calculate for each price point in the range:

1. **Pre-money valuation** = Offer price x Pre-IPO shares outstanding
2. **Primary dilution** = Primary shares / (Pre-IPO shares + Primary shares)
3. **Post-money valuation** = Pre-money + Gross primary proceeds
4. **Fully diluted shares** (treasury stock method):
   - Diluted = Basic + Sum[(Options x (Price - Strike) / Price)] for in-the-money options only
5. **Gross proceeds** = Total shares offered x Offer price
6. **Net proceeds** = Gross - Underwriting discount (7% for IPO) - Offering expenses
7. **Greenshoe proceeds** (if exercised) = 15% of base offering x Offer price

**Step-up analysis:**
- Last private round price: $X → IPO midpoint: $Y
- Step-up multiple: Y / X
- If step-up < 1.0x: **Critical flag** — down-round IPO; expect significant investor pushback

### Phase 3: Valuation Sanity Checks

Before finalizing the range, verify:

- [ ] Implied multiple is within the interquartile range of peer group
- [ ] At the high end, there is still 15-20% upside to peer median (room for aftermarket appreciation)
- [ ] DCF intrinsic value (from `python3 tools/dcf.py`) supports the range
- [ ] Step-up from last private round is reasonable (1.5-3.0x is typical for healthy IPOs)
- [ ] Fully diluted valuation does not create sticker shock vs. peers
- [ ] Use of proceeds narrative justifies the primary offering size

---

## Mode 3: Bookbuilding and Allocation

### Goal: Read the order book, make the pricing night decision, and allocate shares optimally.

### Phase 1: Demand Curve Analysis

Construct the demand curve from investor orders:

1. **Aggregate demand at each price point:**
   - Orders above range (strike price > high end)
   - Orders at top of range
   - Orders at midpoint
   - Orders at bottom of range
   - Limit orders below range

2. **Book quality metrics:**
   - Oversubscription multiple = Total demand / Shares offered
   - Strike-adjusted oversubscription = Demand above midpoint / Shares offered
   - Concentration: Top 10 accounts as % of total demand (>50% = concentrated risk)
   - Investor type mix: Long-only %, Hedge fund %, Retail %
   - Geographic mix: Domestic %, International %
   - Quality-adjusted demand: Weight by investor hold period, AUM, sector expertise

3. **Price elasticity:**
   - How much demand drops between price points
   - Inelastic demand (quality long-only) is more valuable than elastic (price-sensitive HF)
   - If demand drops sharply above midpoint, pricing above range is risky

**Decision Gate 4 — Pricing Night Decision:**
- Book >15x oversubscribed with quality long-only demand: **Price above range** (up to 20% above original top)
- Book 5-15x with balanced demand: **Price at or near top of range**
- Book 2-5x with price-sensitive demand: **Price at midpoint** — do not stretch
- Book <2x or dominated by hedge funds: **Price at bottom or pull the deal** — weak book leads to broken aftermarket
- Book concentrated in <10 accounts: **Caution** — diversify or reduce size

### Phase 2: Allocation Strategy

Allocate shares to optimize long-term aftermarket performance:

**Tier 1: Anchor and cornerstone investors (30-40% of offering)**
- Large long-only institutions with sector expertise
- Minimum hold period commitment (6-12 months)
- These accounts provide stability and signal quality to the market

**Tier 2: Core institutional (30-40% of offering)**
- Diversified long-only managers
- Growth and GARP investors
- Allocate proportionally to order quality (not just size)

**Tier 3: Hedge funds and active traders (15-20% of offering)**
- Provides day-one liquidity and tightens the market
- Limit allocation to prevent excessive flipping
- Track record of aftermarket behavior matters

**Tier 4: Retail and other (5-10% of offering)**
- Retail allocation through syndicate members
- Employee directed share programs
- Friends and family (minimal, avoid controversy)

**Allocation principles:**
- Reward price-insensitive orders (above range, no limit)
- Penalize orders with strings attached (price limits, flip history)
- Ensure geographic diversification for global institutional coverage
- Over-allocate by 15% (greenshoe) to create stabilization capacity

### Phase 3: First-Day Performance Targeting

Model the expected first-day return:

- Target: 10-20% first-day pop
- <10%: Aftermarket may feel heavy; investors underwhelmed
- 10-20%: Optimal — investors rewarded, issuer didn't leave excessive money on the table
- 20-30%: Acceptable for hot deals but issuer left significant money on the table
- >30%: **Mispriced** — issuer's effective cost = 7% spread + 30%+ underpricing = 37%+

**Money left on the table** = (Day 1 close - Offer price) x Total shares offered
- This is a direct cost to the issuer (dilution at below-market price)
- Balance against reputation cost of a broken deal (trading below offer price)

---

## Mode 4: Stabilization and Aftermarket

### Goal: Manage the greenshoe, stabilization, and lockup dynamics.

### Phase 1: Greenshoe Mechanics

The overallotment option (greenshoe) is the underwriter's primary stabilization tool:

1. **At IPO:** Underwriter sells 115% of the base offering (over-allots by 15%)
2. **This creates a naked short position of 15% of the base offering**
3. **If stock rises:** Exercise the greenshoe option — buy shares from the issuer at the offer price to cover the short. Issuer receives additional proceeds.
4. **If stock falls:** Buy shares in the open market below the offer price to cover the short. This buying supports the stock price (stabilization). The underwriter profits on the short.
5. **The greenshoe expires 30 days after pricing.**

**Stabilization decision tree:**
- Stock trading above offer price: **Do not stabilize** — exercise greenshoe, collect additional proceeds
- Stock trading 0-5% below offer price: **Light stabilization** — buy in open market, partial greenshoe exercise
- Stock trading 5-10% below offer price: **Active stabilization** — aggressive buying, no greenshoe exercise
- Stock trading >10% below offer price: **Maximum stabilization** — use full greenshoe capacity; consider penalty bids on flippers

**Penalty bids:** Reclaim the selling concession from syndicate members whose clients flip (sell allocated shares in the first few days). Discourages flipping and supports the aftermarket.

### Phase 2: Lockup Analysis

Standard lockup: 180 days post-IPO for insiders, officers, directors, and pre-IPO shareholders.

**Lockup expiry impact analysis:**
1. **Shares eligible for sale at expiry:** X million shares (Y% of total outstanding)
2. **Overhang ratio:** Locked shares / Current float = Z x current float
3. **Historical impact:** Average stock declines 2-3% in the 5 days around lockup expiry
4. **Factors that worsen the impact:**
   - Large overhang (locked shares > 3x float)
   - Stock has appreciated significantly (holders eager to monetize)
   - Insiders with high cost basis (strong incentive to sell)
   - Weak recent trading volume (market cannot absorb supply)
5. **Factors that mitigate the impact:**
   - Strong fundamental momentum (earnings beats)
   - Insider signaling (public statements of intent to hold)
   - Structured release (staggered lockup with 25% released every 30 days)
   - Secondary offering pre-lockup (orderly distribution vs. chaotic selling)

**Decision Gate 5 — Lockup Strategy:**
- Overhang > 3x float with appreciated stock: **Recommend early lockup release via secondary offering** — orderly is better than chaotic
- Overhang 1-3x with stable trading: **Standard 180-day lockup** — no action needed
- Company wants to do a follow-on within 180 days: **Negotiate partial early release** tied to the follow-on

---

## Mode 5: Secondary and Follow-On Offerings

### Goal: Evaluate and structure post-IPO equity issuance.

### Phase 1: Offering Type Selection

| Option | Discount | Timeline | Best For |
|--------|----------|----------|----------|
| Marketed follow-on | 3-5% to last close | 1-2 days (launch to price) | Large raises ($500M+), broad distribution |
| Overnight deal | 5-7% to last close | Same night | Speed, certainty, moderate size |
| At-the-market (ATM) | 0-2% (market price) | Weeks to months | Ongoing funding, minimal disruption |
| Block trade | 3-5% to last close | Hours | Large shareholder selling, no company dilution |
| PIPE | 5-15% to market | Weeks (negotiated) | Smaller/illiquid issuers, certainty of close |

**Decision tree for offering type:**
1. Is this primary (new shares) or secondary (existing holder selling)?
   - Secondary only → Block trade or registered secondary
   - Primary → Continue to step 2
2. How much capital is needed relative to market cap?
   - <5% of market cap → ATM program (less disruption)
   - 5-15% of market cap → Overnight or marketed deal
   - >15% of market cap → Marketed deal with roadshow (needs broad distribution)
3. How urgent is the capital need?
   - Immediate → Overnight deal
   - Flexible timing → ATM (sell into strength)
   - Strategic (M&A financing) → Marketed deal (signals confidence)

### Phase 2: ATM Program Analysis

For at-the-market programs, model the execution:

- **Shares needed** = Target proceeds / Current share price
- **Daily capacity** = ADTV x Participation rate (typically 10-25%)
- **Shares per day** = Daily capacity shares
- **Days to complete** = Total shares / Shares per day
- **Calendar time** = Trading days / ~21 trading days per month
- **Market impact cost** = f(participation rate, stock liquidity, volatility)
- **Agent commission** = 1-3% of gross proceeds

**Decision Gate 6 — ATM Feasibility:**
- Completion time < 3 months at 15% participation: **Feasible** — proceed with ATM
- Completion time 3-6 months: **Marginal** — consider hybrid (partial ATM + marketed deal)
- Completion time > 6 months: **Not feasible** — use marketed offering instead

### Phase 3: Dilution Impact Analysis

For any equity issuance, calculate:

1. **Share dilution** = New shares / (Existing + New shares)
2. **EPS dilution** = (Old EPS - New EPS) / Old EPS
   - Offset if proceeds are invested at returns > earnings yield
   - Accretive if: Return on deployed capital > (1 / P/E ratio)
3. **NAV dilution** (for REITs/asset-heavy): Dilutive if offer price < NAV/share
4. **Ownership dilution** for existing holders: Each holder's % ownership x (1 - dilution %)

---

## Mode 6: Convertible Bond Issuance

### Goal: Structure and price a convertible bond offering.

### Phase 1: Strategic Rationale

When does a convertible make sense vs. straight equity or debt?

- **vs. Straight equity:** Convert is better when stock is undervalued (higher effective issuance price via conversion premium) or when dilution must be deferred
- **vs. Straight debt:** Convert is better when the issuer needs a lower coupon (converts trade at 300-500 bps below straight HY cost)
- **vs. Both:** Ideal for growth companies that want cheap financing now with dilution only if the stock rises significantly

### Phase 2: Term Structuring

**Key terms to optimize:**

1. **Coupon:** Target significantly below straight debt cost
   - Run `python3 tools/bond_yield.py` to determine the issuer's straight debt cost
   - Convert coupon is typically 50-70% lower than straight HY yield

2. **Conversion premium:** 25-40% over current share price is standard
   - Higher premium = less dilution risk but lower investor appeal
   - Lower premium = more dilution risk but lower coupon
   - Run `python3 tools/convertible.py` to model the coupon/premium tradeoff

3. **Maturity:** 5-7 years standard
4. **Call protection:** Typically non-callable for 3 years; provisional call after that (stock must trade >130% of conversion price for 20 of 30 consecutive days)
5. **Put right:** Investor can put at par on a fundamental change

### Phase 3: Convertible Valuation

Run `python3 tools/convertible.py` with issuer parameters:

1. **Bond floor** = PV of coupon stream + principal at credit-appropriate discount rate
   - This is the minimum value (pure debt value with zero equity optionality)
   - Run `python3 tools/bond_yield.py` for the appropriate credit spread

2. **Equity option value** = Black-Scholes with inputs:
   - S = current stock price
   - K = conversion price (stock price x (1 + conversion premium))
   - sigma = implied volatility (use listed options if available)
   - T = maturity
   - r = risk-free rate
   - q = dividend yield

3. **Theoretical value** = Bond floor + Equity option value
4. **Delta** at issuance: typically 0.30-0.60
5. **Parity** = Conversion ratio x Current stock price
6. **Premium over parity** = (Bond price - Parity) / Parity

### Phase 4: Call Spread Overlay

To raise the effective conversion premium (reduce dilution):

1. **Buy a call** at the conversion price (same strike as the embedded option)
2. **Sell a call** at a higher strike (e.g., 100% premium over current stock price)
3. **Effective conversion premium** raised from ~30% to ~100%
4. **Net cost** = Call spread premium (typically 5-10% of par)
5. **Total issuer cost** = Convert coupon + Amortized call spread cost
6. **Breakeven vs. straight equity** = Price at which the convert + call spread is cheaper than equity issuance

**Decision Gate 7 — Convertible Structure:**
- Call spread raises effective premium above 80% and total cost < straight debt: **Include call spread** — substantial dilution protection
- Call spread cost makes total financing cost > straight debt: **Skip call spread** — defeats the purpose of the convert
- Stock volatility < 25%: **Convertible may not price well** — low vol makes the embedded option cheap, investors demand higher coupon

### Phase 5: Investor Base Analysis

**Convertible arbitrage funds (60-70% of typical allocation):**
- Buy the convert, short delta shares of stock
- Earn: coupon carry + positive gamma (convexity)
- These investors are volatility buyers and credit-agnostic
- Their hedging creates selling pressure on the stock at issuance (delta hedging)

**Outright/long-only investors (30-40%):**
- Buy for hybrid exposure: yield + equity upside
- Do not hedge; provide better aftermarket support
- Prefer higher coupons and lower conversion premiums

**Stock price impact at issuance:**
- Expect 3-7% stock decline at announcement (arb shorting + dilution signal)
- Impact is worse for: small-cap, illiquid stocks, high short interest
- Mitigate by: launching after close, pricing overnight, limiting deal size to <20% of market cap

---

## Tool Integration

| When the analysis needs... | Run this | Example |
|---------------------------|---------|---------|
| Intrinsic value for range-setting | `python3 tools/dcf.py --fcf 80,95,110,125,140 --wacc 0.10 --terminal-growth 0.025 --shares 200` | EV, equity value, price/share with sensitivity table |
| Cost of capital for discount rate | `python3 tools/wacc.py --equity 5000 --debt 1000 --tax 0.25 --rf 0.04 --beta 1.3 --erp 0.055 --cost-of-debt 0.05` | WACC for DCF and bond floor |
| Convertible bond pricing | `python3 tools/convertible.py --stock-price 50 --conversion-premium 0.30 --coupon 0.02 --maturity 5 --vol 0.35 --rf 0.04 --credit-spread 0.03` | Bond floor, option value, theoretical price, delta |
| Straight debt yield for coupon benchmarking | `python3 tools/bond_yield.py --face 1000 --coupon 0.06 --maturity 5 --price 980` | YTM, current yield, spread to benchmark |

---

## Output Specifications

### Primary Deliverable: ECM Analysis Package

For each mode, output:

```
### [Analysis Title]

**Recommendation:** [One sentence — the bottom line]

**Key Metrics:**
- [Metric 1: value and interpretation]
- [Metric 2: value and interpretation]
- [Metric 3: value and interpretation]

**Analysis Detail:**
[Structured analysis per the mode-specific framework above]

**Decision Gate Outcome:** [Pass / Conditional / Fail — with reasoning]

**Risks & Mitigants:**
- [Risk 1]: [Mitigant]
- [Risk 2]: [Mitigant]

**Next Steps:**
1. [Action item with owner and timeline]
2. [Action item with owner and timeline]
```

### Supporting Artifacts:
- **Valuation summary** — peer comps, DCF cross-check, implied multiples at each price point
- **Dilution table** — ownership impact at low, mid, high, and above-range pricing
- **Sensitivity matrix** — valuation across multiple growth rates and multiples
- **Timeline** — key dates from filing through pricing, lockup, and first follow-on eligibility
- **Data gaps** — all missing inputs explicitly flagged with impact on analysis quality

---

## Quality Gates & Completion Criteria

- [ ] Every recommendation passes through the appropriate decision gate
- [ ] Valuation is cross-checked with at least two methods (comps + DCF minimum)
- [ ] Dilution impact is calculated at every price point in the range
- [ ] IPO discount is explicitly justified (not just assumed at 15%)
- [ ] Aftermarket performance target is stated with supporting rationale
- [ ] All tool outputs are incorporated with explicit parameter disclosure
- [ ] Market timing assessment addresses window, sector sentiment, and calendar
- [ ] Risk factors include both issuer-specific and market/execution risks

**Success metric:** A syndicate desk head could use this analysis to make a pricing recommendation to the issuer CEO without additional work.

**Escalation triggers:**
- IPO valuation implies a down-round from last private raise → stop and flag before proceeding
- Book is <2x oversubscribed on pricing night → recommend pulling or downsizing the deal
- Convertible delta hedging would exceed 30% of average daily volume → flag stock impact risk
- Greenshoe fully consumed in first 5 trading days → aftermarket is fragile; recommend issuer silence period

---

## Hard Constraints

- **NEVER** fabricate comparable company data, trading multiples, or market statistics
- **NEVER** recommend pricing above range without a book that supports it (>10x oversubscription)
- **NEVER** skip the IPO discount in valuation — every IPO needs a discount to incentivize investors
- **ALWAYS** calculate dilution at every price point, not just the midpoint
- **ALWAYS** identify the fulcrum investors (accounts whose participation makes or breaks the book)
- **ALWAYS** flag money left on the table if first-day pop exceeds 25%
- **ALWAYS** run both comps and DCF — never rely on a single valuation method
- If the user provides projections without assumptions, **require** assumptions before using them

---

## Common Pitfalls

1. **Pricing to the last private round:** Private round valuations reflect illiquidity discounts, strategic premiums, and structured terms (ratchets, liquidation preferences). Public market valuation is different. → Always build valuation from public comps, not backward from private marks.

2. **Ignoring the greenshoe in dilution math:** The greenshoe adds 15% more shares. Total potential dilution = base offering + greenshoe. → Always show dilution with and without greenshoe exercise.

3. **Overweighting oversubscription:** A 20x oversubscribed book full of hedge funds is worse than a 5x book of long-only institutions. → Quality-adjust the book; weight by investor hold period and AUM.

4. **Misjudging lockup expiry impact:** The stock impact is not just about volume — it is about the *signal*. If insiders sell aggressively at lockup, it signals lack of confidence. → Analyze insider cost basis and incentive structure, not just share volume.

5. **Underpricing convertibles by ignoring call spread costs:** The "cheap coupon" of a convert becomes expensive when you add the call spread overlay. Total cost = coupon + amortized call spread premium. → Always compare total convert cost to straight debt and equity alternatives.

6. **Launching into a closed window:** Even great companies fail in bad markets. The IPO window opens and closes; sector sentiment matters as much as company quality. → Check recent IPO pricing outcomes and aftermarket returns before launching.

7. **Setting the range too narrow:** A narrow range ($18-$19) leaves no room for price discovery. If the book is strong, you cannot price above range by more than 20% without re-filing. → Standard range is 10-15% wide ($17-$20).

---

## Related Skills

- After IPO analysis, use **`/pitch-deck`** (Mode 2: Deal Marketing) to build the roadshow presentation
- For LBO analysis if PE sponsors are in the investor base, use **`/lbo`**
- For credit analysis on the debt side of the capital structure, use **`/credit`**
- For post-IPO equity research initiation framework, use **`/investment-memo`**
- For convertible bond credit analysis, use **`/credit`** with the bond's credit profile
