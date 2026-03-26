# Alternatives Allocation

```
You are a senior alternatives investment officer at a large institutional allocator (pension
fund, endowment, sovereign wealth fund, or family office) overseeing $5-50B in alternative
investments across private equity, hedge funds, real assets, and private credit. You think
in terms of total portfolio impact, illiquidity budgets, commitment pacing, and manager
selection. You understand that alternatives serve multiple roles — return enhancement,
diversification, income generation, and inflation protection — but that complexity, fees,
and illiquidity must be justified by genuine net-of-fee alpha or unique risk characteristics.
You are rigorous about due diligence, skeptical of reported marks and smoothed returns,
and focused on how each alternative allocation interacts with the liquid portfolio.
```

## What This Desk Does

The alternatives allocation team selects, sizes, and monitors investments in private equity, hedge funds, real estate, infrastructure, natural resources, and private credit within an institutional portfolio. Unlike liquid market investing, alternatives require multi-year commitment horizons, careful cash flow management (the J-curve), and specialized due diligence covering both investment and operational risks. The team must balance the return premium from illiquidity against the need for cash flow predictability, manage vintage year diversification, and continuously assess whether net-of-fee returns justify the complexity premium. With endowments like Yale pioneering 50%+ alternatives allocations and pension funds increasingly following, the team's decisions on commitment pacing, manager selection, and secondary market activity materially impact total portfolio outcomes over decades.

---

## 1. Private Equity Allocation Framework

Managing PE commitments, cash flows, and vintage diversification to maintain target exposure through time.

**PE Return Metrics:**
- TVPI (Total Value to Paid-In) = (Distributions + NAV) / Contributions
- DPI (Distributions to Paid-In) = Distributions / Contributions (realized return)
- RVPI (Residual Value to Paid-In) = NAV / Contributions (unrealized)
- IRR = discount rate that equates PV(contributions) = PV(distributions + NAV)
- PME (Public Market Equivalent) = Kaplan-Schoar: compares PE cash flows invested in a public index

### Commitment Pacing Model

```
I need to build a PE commitment pacing plan to achieve and maintain a [X]% target allocation:

Current PE program:
- Total portfolio AUM: $[X]B
- Current PE NAV: $[X]B ([X]% of total portfolio)
- Target PE allocation: [X]% of total portfolio
- Unfunded commitments: $[X]B
- NAV + Unfunded = $[X]B (total PE exposure)

Historical program data:
- Average drawdown rate: [X]% of commitments per year (typically 25-35%)
- Average distribution rate: [X]% of NAV per year (typically 15-25%)
- Average fund life: [X] years
- Historical net IRR: [X]%

Cash flow modeling assumptions:
- Expected call schedule: Year 1: [X]%, Year 2: [X]%, Year 3: [X]%, Year 4-6: [X]%
- Expected distribution schedule: Year 4: [X]%, Year 5: [X]%, Year 6-10: [X]%

Help me:
1. **Steady-state commitment pace**: How much should I commit per year to maintain target allocation?
   - Rule of thumb: Annual commitment = target_NAV x (1/avg_fund_life + growth_rate)
   - More precise: Model contributions and distributions year-by-year for 10-year projection
2. **J-curve management**: In early years, contributions > distributions; cash drag on portfolio
   - Peak J-curve negative = typically -5 to -15% of commitments in years 1-3
   - Mitigation: Use secondary purchases, co-investments, continuation vehicles
3. **Vintage year diversification**: Spread commitments across vintages to reduce timing risk
   - Target: No single vintage > [X]% of total PE NAV
   - Adjustment: Over-commit in attractive vintages (distressed years), under-commit when multiples peak
4. **Over-commitment ratio**: How much to over-commit relative to target NAV?
   - Over-commitment ratio = total_unfunded / target_NAV (typically 1.3-1.6x)
   - Depends on drawdown/distribution rates and capital call line usage
5. **Liquidity stress test**: What if capital calls spike while distributions dry up?
   - Model worst case: 2008-2009 scenario — calls at [X]% of commitments, distributions near zero
   - Liquidity source: What assets can be sold to fund calls? Cost of forced liquidation?
6. **Manager selection framework**: GP concentration limits, strategy diversification
   - Max [X]% to single GP, diversify across buyout/growth/VC/special situations/geography
```

### PE Cash Flow Modeling

```
Model the expected cash flows for a PE fund commitment:

Fund: [GP name], Strategy: [buyout / growth / venture / special situations]
Vintage year: [X]
Commitment: $[X]M
Fund size: $[X]B
Expected net IRR: [X]%
Expected net TVPI: [X]x
Investment period: [X] years, Fund life: [X] years + [X] year extensions

Build a year-by-year cash flow projection:

1. **Contributions (capital calls)**:
   - Investment period: [X]% drawn per year for [X] years
   - Fees and expenses: [X]% management fee on committed/invested capital
   - Model: contributions_t = commitment x drawdown_rate_t
2. **Distributions**:
   - Harvest period begins year [X], accelerates through years [X]-[X]
   - Distribution waterfall: return of capital first, then preferred return, then carry
   - Model: distributions_t = NAV_t x distribution_rate_t
3. **NAV projection**: NAV_t = NAV_{t-1} + contributions_t - distributions_t + appreciation_t
4. **IRR and TVPI at various exit multiples**:
   - Bear case ([X]x gross MOIC): Net IRR = [X]%, Net TVPI = [X]x
   - Base case ([X]x gross MOIC): Net IRR = [X]%, Net TVPI = [X]x
   - Bull case ([X]x gross MOIC): Net IRR = [X]%, Net TVPI = [X]x
5. **Fee drag analysis**: Gross-to-net bridge
   - Management fee drag: ~[X] bps annually
   - Carried interest at [X]% over [X]% preferred return
   - Gross TVPI [X]x -> Net TVPI [X]x (fee drag = [X]x)
6. **PME calculation**: Compare cash flows as if invested in [benchmark index]
   - PME > 1.0 = PE outperformed public markets; PME < 1.0 = public markets were better
```

---

## 2. Hedge Fund Due Diligence

Evaluating hedge fund managers for inclusion in an institutional portfolio across investment, operational, and terms dimensions.

### Hedge Fund Manager Assessment

```
Evaluate [fund name] for a potential $[X]M allocation:

Fund overview:
- Strategy: [long/short equity / global macro / credit / relative value / event-driven / multi-strat]
- AUM: $[X]B, Capacity: $[X]B
- Track record: [X] years live
- Fees: [X]% management + [X]% performance (+ [X]% pass-through expenses if applicable)
- Liquidity: [monthly / quarterly] with [X]-day notice, [X]-year lock-up
- High water mark: [yes / no], Hurdle rate: [X]%

Performance:
- Annualized return (net): [X]%
- Annualized volatility: [X]%
- Sharpe ratio: [X]
- Maximum drawdown: [X]%, Recovery time: [X] months
- Correlation to S&P 500: [X], Correlation to 60/40: [X]
- Up capture: [X]%, Down capture: [X]%
- Beta to equity market: [X]

Help me conduct due diligence:

1. **Investment assessment**:
   - What is the claimed edge? Is it scalable? Is it eroding?
   - Factor decomposition: Run returns through Fama-French + momentum + credit + vol factors
   - Alpha (residual after factor regression): [X]% — is it statistically significant? (t > 2.0)
   - Is the track record long enough? t_stat = Sharpe x sqrt(years)
   - Style drift analysis: Have factor exposures changed materially over time?

2. **Operational due diligence**:
   - Fund administrator: [name] — independent? reputable?
   - Auditor: [name] — Big 4?
   - Prime broker(s): [names] — counterparty diversification?
   - Valuation policy: How are illiquid positions marked? Side pocket usage?
   - Key person risk: What happens if PM leaves?
   - Regulatory: SEC registered? NFA? Compliance infrastructure?
   - Cybersecurity and business continuity

3. **Terms analysis**:
   - Fee netting across strategy sleeves
   - Most favored nation (MFN) clause available?
   - Gates and suspension provisions
   - Fund-level vs investor-level high water mark
   - Clawback provisions on crystallized carry

4. **Portfolio fit**:
   - How does adding [X]% allocation affect total portfolio Sharpe, drawdown, and liquidity?
   - Correlation to existing hedge fund allocations: does this add diversification?
   - Role: return enhancer, diversifier, drawdown mitigator, or volatility reducer?

5. **Red flags**: High AUM growth, declining alpha, style drift, unusual fee structure,
   concentrated counterparty risk, lack of transparency, related-party transactions
```

---

## 3. Real Assets Allocation

Investing in real estate, infrastructure, and natural resources for inflation protection, income generation, and diversification.

### Real Assets Portfolio Construction

```
I'm building/reviewing a real assets allocation within my total portfolio:

Current allocation:
- Real estate: [X]% (benchmark target: [X]%)
  - Core: [X]%, Value-add: [X]%, Opportunistic: [X]%
  - Listed REITs: [X]%, Private real estate: [X]%
- Infrastructure: [X]% (target: [X]%)
  - Core/regulated: [X]%, Value-add: [X]%
- Natural resources: [X]% (target: [X]%)
  - Timber/farmland: [X]%, Energy: [X]%, Metals/mining: [X]%

Macro environment:
- Inflation (trailing/expected): [X]% / [X]%
- Real yields: [X]%
- Real estate cap rates: [X]% (vs historical [X]%)
- Infrastructure equity discount rates: [X]%

Help me evaluate:
1. **Inflation hedging effectiveness**:
   - Correlation with CPI: Real estate [X], infrastructure [X], commodities [X], TIPS [X]
   - Inflation beta: How much does each asset class return increase per 1% inflation surprise?
   - Real estate: Lease escalators, replacement cost growth
   - Infrastructure: Regulated returns often linked to CPI, concession pricing
   - Natural resources: Direct commodity price exposure

2. **Income and yield assessment**:
   - Real estate NOI yield: [X]%, Infrastructure cash yield: [X]%, Timber cash yield: [X]%
   - Compare to fixed income yields — real assets should offer premium for illiquidity

3. **Diversification benefits**:
   - Correlation to equities: [X] (real estate), [X] (infrastructure), [X] (commodities)
   - Note: Listed REITs correlate ~0.6-0.7 to equities; private RE ~0.1-0.3 (partly smoothing)
   - Beware: Smoothed private asset returns overstate diversification benefit

4. **Public vs private implementation**:
   - Listed (liquid, transparent, correlated to equity markets, market-cap pricing)
   - Private (illiquid, smoothed returns, NAV-based pricing, manager selection alpha opportunity)
   - Hybrid: Public core + private satellite

5. **Risk assessment**: Leverage in real estate, regulatory risk in infrastructure,
   commodity price volatility, geopolitical risk in natural resources
```

---

## 4. Secondary Market Transactions

Buying and selling LP interests in existing PE/real asset funds, including GP-led continuation vehicles.

### Secondary Market Pricing and Execution

```
I'm evaluating a secondary market transaction:

Transaction type: [LP interest sale / LP interest purchase / GP-led continuation vehicle]

If LP interest purchase:
- Fund: [GP name], Vintage: [X], Strategy: [buyout / VC / real estate / infrastructure]
- Fund size: $[X]B
- Current NAV: $[X]M (as of [date])
- Unfunded commitment: $[X]M
- Remaining fund life: [X] years
- Pricing: [X]% of NAV (discount/premium)
- GP track record: prior fund TVPI [X]x, DPI [X]x

If GP-led continuation vehicle:
- Continuation vehicle assets: [describe portfolio companies being rolled]
- Proposed terms: [X]% management fee, [X]% carry, [X]% preferred return
- New economic reset: carry crystallized on old fund, new carry starts on continuation NAV
- LP options: roll existing interest, sell at offered price, or elect cash distribution

Help me evaluate:
1. **NAV quality assessment**: How reliable is the reported NAV?
   - Last valuation date: [X] — how stale?
   - Valuation methodology: Third-party appraisals? Market comps? DCF?
   - Markup/markdown history: Trend in quarterly NAV changes
   - Sector-specific risk: Are underlying assets in sectors with recent price declines?

2. **Pricing analysis**: Is the [X]% discount/premium to NAV attractive?
   - Historical average secondary pricing: [X]% of NAV for this strategy/vintage
   - Implied IRR at offered price given expected remaining distributions
   - Comparable transactions: recent secondary pricing for similar GP quality/vintage

3. **Cash flow projection**: Model expected remaining contributions and distributions
   - Year-by-year projection from today through fund wind-down
   - IRR at various exit scenarios (base/bull/bear)

4. **For GP-led continuation**: Alignment and conflict analysis
   - Is the GP motivated by carry crystallization? Are they properly incentivized on new vehicle?
   - Quality of rolled assets: Are these the best or worst assets in the portfolio?
   - Fairness opinion: Independent valuation of rolled assets

5. **Portfolio impact**: How does this transaction affect my PE program?
   - Impact on vintage diversification, GP concentration, strategy mix
   - Does buying secondaries at a discount increase expected PE program IRR?
   - Secondaries as a J-curve mitigation tool: immediate NAV exposure, shorter duration
```

---

## 5. Portfolio Impact Analysis

Quantifying how alternative allocations affect total portfolio characteristics: return, risk, Sharpe ratio, drawdown, and liquidity.

### Alternatives Impact Modeling

```
Analyze the impact of adding/changing alternatives allocation in my total portfolio:

Current portfolio (before change):
- Expected return: [X]%, Volatility: [X]%, Sharpe: [X]
- Maximum drawdown (95th percentile): [X]%
- Liquidity: [X]% available within 30 days

Proposed change: Add/increase [alternative type] from [X]% to [X]%, funded by reducing [asset class]

Alternative characteristics:
- Expected return: [X]% (net of fees)
- Expected volatility: [X]% (mark-to-market, not smoothed)
- Correlation to equities: [X], Correlation to bonds: [X]
- Liquidity profile: [X]-year lock-up, [X]% redeemable per quarter
- Fee drag: [X] bps (management) + [X] bps (performance fee, expected)

Help me quantify:
1. **Sharpe ratio impact**: New portfolio Sharpe vs old
   - Sharpe_new = E[R_new] / sigma_new
   - The addition improves Sharpe if: E[R_alt] / sigma_alt > Sharpe_existing x rho(alt, portfolio)
2. **Marginal contribution to risk**: How much portfolio risk does the new allocation add?
   - MCTR_alt = beta_alt_to_portfolio x sigma_portfolio
   - Optimal sizing: Increase allocation until MCTR_alt x lambda = E[R_alt]
3. **Drawdown impact**: Monte Carlo simulation of portfolio drawdowns with and without alternatives
   - Conditional drawdown: What happens in a 2008-style event? (correlation spike to ~0.8)
   - Use regime-dependent correlations, not unconditional
4. **Liquidity impact**: Total portfolio liquidity profile
   - Day 1 liquidity, 30-day liquidity, 90-day liquidity, 1-year liquidity
   - Stress test: Can I meet a 10% redemption request without fire-selling illiquid assets?
5. **Fee efficiency**: Is the net-of-fee return premium over liquid alternatives sufficient?
   - Compare: PE at [X]% net vs levered small-cap value at [X]% with 10 bps fee
   - Hedge fund at [X]% net vs factor replication at [X]% with 30 bps fee
6. **Break-even alpha**: What minimum alpha must the alternative deliver to justify inclusion?
   - Break-even = fee_drag + illiquidity_cost + complexity_cost + monitoring_cost

Decision framework: Alternatives improve the portfolio if the genuine, risk-adjusted,
net-of-fee return premium exceeds the illiquidity cost, operational complexity, and
the opportunity cost of capital locked in long-duration vehicles.
```

---

## Mathematical Reference

**PE Cash Flow Identity:** NAV_t = NAV_{t-1} + Contributions_t - Distributions_t + Value_Change_t

**TVPI / DPI / RVPI:**
- TVPI = (Cumulative_Distributions + Current_NAV) / Cumulative_Contributions
- DPI = Cumulative_Distributions / Cumulative_Contributions
- RVPI = Current_NAV / Cumulative_Contributions
- TVPI = DPI + RVPI

**IRR:** Solve for r: sum_t [CF_t / (1+r)^t] = 0, where CF_t = contributions (negative) + distributions (positive)

**PME (Kaplan-Schoar):** PME = FV(distributions, invested in index) / FV(contributions, invested in index). PME > 1 implies PE outperformed.

**Sharpe Improvement Test:** Adding asset improves portfolio Sharpe if:
SR_new_asset > SR_existing_portfolio x correlation(new_asset, existing_portfolio)

**Illiquidity Premium Estimation:** Illiquidity premium = private_asset_return - comparable_public_asset_return - fees - smoothing_bias_adjustment. Typical estimates: 100-300 bps for PE, 50-150 bps for private RE, 0-100 bps for hedge funds (debatable).

**Commitment Pacing (steady state):** Annual_commitment = Target_NAV x (distribution_rate + portfolio_growth_rate) / average_drawdown_rate

---

## See Also

- [Multi-Asset Allocation](multi-asset.md) — alternatives within the total strategic allocation framework
- [Risk & Performance Analytics](risk-analytics.md) — VaR and scenario analysis including illiquid assets
- [Active Equity](active-equity.md) — public equity benchmarks for PME comparison
- [Hedge Fund Analyst Role](../roles/hedge-fund-analyst.md) — factor decomposition for hedge fund return analysis
- [PE Analyst Role](../roles/pe-analyst.md) — LBO modeling, deal structuring, and portfolio operations
