# Infrastructure Investing

Prompt templates for infrastructure private equity and debt, covering concession analysis, regulated utility valuation, greenfield vs. brownfield risk, energy transition investments, and infrastructure project finance.

## Role Context

```
You are a director at an infrastructure fund ($15B AUM) investing in essential-service
assets with long-duration, inflation-linked cash flows. Your portfolio spans transportation
(toll roads, airports, ports), utilities (regulated electric, water, gas), energy
(renewables, midstream, transmission), and digital infrastructure (data centers, fiber,
towers). You evaluate assets through the lens of cash flow predictability: contracted vs.
regulated vs. merchant revenue, inflation pass-through mechanisms, and regulatory
frameworks. You target 8-12% net IRR for core/core-plus assets and 12-18% for value-add
and greenfield. You think in real (inflation-adjusted) returns, model 20-30 year cash
flows, and obsess over regulatory risk, construction risk, and demand volatility. Every
investment must answer: "What is the essential service, and why can't it be disrupted?"
```

For foundational PE frameworks (returns analysis, due diligence), see [`../roles/pe-analyst.md`](../roles/pe-analyst.md). The prompts below focus on infrastructure-specific valuation, regulatory analysis, and project finance.

---

## 1. Concession Analysis

### Toll Road / Airport / Utility Revenue Modeling

```
Analyze a concession-based infrastructure asset:

Asset profile:
- Type: [toll road / airport / port / water utility]
- Location: [country/region]
- Concession term: [X] years remaining (of [X] total)
- Counterparty: [government entity]
- Revenue model: [regulated tariff / contracted / merchant / hybrid]

Revenue structure:
- Current annual revenue: $[X]M
- Revenue breakdown:
  - Regulated/contracted: [X]% (tariff set by [regulator], escalation: [CPI / CPI+X% / fixed])
  - Volume-dependent: [X]% (traffic, passengers, throughput)
  - Merchant/commercial: [X]% (retail, advertising, ancillary)

For toll roads:
- Average daily traffic (ADT): [X] vehicles
- Traffic growth rate (historical 5-year CAGR): [X]%
- Toll rate: $[X] per vehicle (weighted average across classes)
- Toll escalation mechanism: [CPI annually / regulatory review every X years]
- Traffic elasticity to toll increases: [X]% traffic decline per [X]% toll increase
- GDP elasticity of traffic: [X]% (traffic grows [X]% for each 1% of GDP growth)
- Competing routes: [describe alternatives and capacity constraints]

For airports:
- Passenger traffic: [X]M annual passengers
- Aeronautical revenue per passenger: $[X] (regulated, escalation mechanism: [describe])
- Non-aeronautical revenue per passenger: $[X] (commercial, retail, parking)
- Non-aero as % of total: [X]% (higher is better — provides margin expansion opportunity)
- Traffic recovery trajectory (if post-disruption): [X]% of pre-[event] levels

Demand modeling:
1. Base case: [X]% annual traffic/volume growth (in line with GDP/population growth)
2. Upside: [X]% growth (new development in corridor, induced demand, modal shift)
3. Downside: [X]% growth (recession, competing infrastructure, remote work impact)
4. Stress: [X]% traffic decline (pandemic, economic crisis)
   Revenue impact: $[X]M → $[X]M
   Can the asset service its debt in the stress case? DSCR falls to [X]x

Concession-specific risks:
- Regulatory/political risk: has the government ever modified concession terms?
- Handback conditions: what capex is required to return the asset in contractual condition?
- Extension rights: can the concession be extended in exchange for capital investment?
- Termination provisions: compensation formula if government terminates early
```

---

## 2. Regulated Utility Valuation

### Rate Base and Allowed Return Analysis

```
Value a regulated [electric / water / gas] utility:

Regulatory framework:
- Regulator: [name of regulatory commission]
- Regulatory model: [cost-of-service / incentive-based / hybrid]
- Rate case frequency: every [X] years
- Most recent rate case: [date], next expected: [date]
- Regulatory jurisdiction reputation: [constructive / neutral / hostile]

Rate base and capital plan:
- Current rate base: $[X]M
- Rate base growth (5-year CAGR): [X]%
- Capital expenditure plan: $[X]M over [X] years
  - System modernization: $[X]M
  - Growth capex (new connections): $[X]M
  - Mandated environmental/safety: $[X]M
- Depreciation rate: [X]% per year
- Projected rate base:
  Rate Base(t+1) = Rate Base(t) + Capex - Depreciation
  Year 1: $[X]M → Year 5: $[X]M (CAGR: [X]%)

Allowed return:
- Allowed ROE: [X]% (regulatory-determined)
- Allowed cost of debt: [X]% (based on embedded debt cost)
- Regulatory capital structure: [X]% equity / [X]% debt
- Allowed WACC: (Equity % x ROE) + (Debt % x Cost of Debt) = [X]%

Revenue requirement:
  Revenue Requirement = (Rate Base x Allowed WACC) + Operating Expenses + Depreciation + Taxes

  Rate Base: $[X]M x [X]% WACC = $[X]M (return on capital)
  + Operating expenses: $[X]M
  + Depreciation: $[X]M
  + Taxes (grossed up): $[X]M
  = Revenue requirement: $[X]M
  Current rates generate: $[X]M (over/under-earning by $[X]M)

Valuation:
- Rate base multiple = EV / Rate Base
  Current: [X]x (peers trade at [X]x - [X]x)
  Premium to rate base justified by: growth capex pipeline, constructive regulator,
  earned ROE > allowed ROE
- DCF: 20-year cash flow projection using rate base growth and allowed returns
  Terminal value: rate base in Year 20 x terminal multiple
  WACC for discounting: [X]% (reflect regulated, low-beta cash flows)

Key risks:
1. Regulatory lag: time between capex deployment and rate base inclusion
   Lag of [X] months reduces earned ROE by ~[X]bps
2. Disallowance risk: regulator could reject [X]% of proposed capex
3. Political risk: rate freeze, populist intervention, municipalization threat
4. Earned vs. allowed ROE: if utility consistently under-earns, equity is diluted
```

---

## 3. Greenfield vs. Brownfield

### Development Risk Premium Analysis

```
Compare greenfield development vs. brownfield acquisition for [asset type]:

Brownfield (operating asset):
- Acquisition price: $[X]M
- Current EBITDA: $[X]M
- Yield at acquisition: [X]% (EBITDA / price)
- Track record: [X] years of operating history
- Key risk: overpaying (entry multiple), volume/demand risk, regulatory change
- Target return: [X]% levered IRR (core-plus / value-add)

Greenfield (new-build):
- Total development cost: $[X]M
  - Construction cost: $[X]M
  - Development fees and soft costs: $[X]M
  - Financing costs during construction: $[X]M
  - Contingency: [X]% = $[X]M
- Expected stabilized EBITDA: $[X]M
- Yield on cost: EBITDA / Total Development Cost = [X]%
- Development spread: Yield on cost - Brownfield cap rate = [X]bps
  (Compensation for: construction risk, ramp-up risk, permitting, cost overruns)
- Target return: [X]% levered IRR (value-add / opportunistic)

Risk comparison:

1. **Construction risk**:
   - Cost overrun probability: [X]% chance of [X]% overrun
   - Delay probability: [X]% chance of [X] month delay
   - Impact of 6-month delay on IRR: -[X]bps
   - EPC contract type: [fixed-price / cost-plus / hybrid]
   - Contractor creditworthiness and bonding

2. **Ramp-up risk**:
   - Time from COD to stabilized revenue: [X] months
   - Revenue during ramp: [X]% of stabilized level
   - Working capital / operating losses during ramp: $[X]M

3. **Availability-based payments** (if applicable):
   - Government pays fixed availability fee regardless of demand
   - Shifts demand risk from investor to public sector
   - Availability-based PPP: IRR [X]% lower but with much lower volatility
   - Key risk becomes: construction delivery and performance standards

4. **Permitting and environmental**:
   - Permits secured: [all / partial / none]
   - Environmental impact assessment: [complete / pending]
   - Community opposition risk: [low / moderate / high]
   - Timeline risk from permitting delays: [X] months

Decision framework:
- Development spread > [X]bps: greenfield is justified for the risk
- Development spread < [X]bps: buy brownfield (insufficient compensation for construction risk)
- Rule of thumb: greenfield IRR should exceed brownfield IRR by 300-500bps
```

---

## 4. ESG and Energy Transition

### Renewable Energy Project Finance

```
Underwrite a [solar / onshore wind / offshore wind / battery storage] project:

Project details:
- Technology: [X]
- Capacity: [X] MW
- Location: [X]
- Expected capacity factor: [X]% (P50 resource estimate)
- P90 capacity factor: [X]% (1-in-10 year low production)
- Useful life: [X] years
- Degradation rate: [X]% per year

Revenue structure:
- Power Purchase Agreement (PPA):
  - Offtaker: [utility / corporate / government]
  - PPA price: $[X]/MWh
  - PPA term: [X] years
  - Escalation: [X]% per year (or CPI-linked)
  - Offtaker credit rating: [X]
- Merchant exposure (post-PPA or uncontracted):
  - Current merchant price: $[X]/MWh
  - Forward curve: $[X]/MWh (Year [X])
  - Merchant revenue as % of total: [X]%
- Renewable energy certificates (RECs) / green certificates: $[X]/MWh
- Capacity payments (if applicable): $[X]/MW-year
- Tax credits: [ITC at X% / PTC at $X/MWh for X years]

Annual revenue:
  P50 production: [X] MW x [X]% capacity factor x 8,760 hours = [X] MWh
  PPA revenue: [X] MWh x $[X]/MWh = $[X]M
  Merchant revenue: [X] MWh x $[X]/MWh = $[X]M
  RECs: [X] MWh x $[X] = $[X]M
  Tax credits: $[X]M
  Total Year 1 revenue: $[X]M

Operating costs:
- O&M (fixed): $[X]/kW-year = $[X]M
- O&M (variable): $[X]/MWh = $[X]M
- Land lease: $[X]M
- Insurance: $[X]M
- Grid connection and transmission: $[X]M
- Asset management: $[X]M
- Total opex: $[X]M

EBITDA: $[X]M
EBITDA margin: [X]% (renewables typically 70-85%)

LCOE calculation:
  LCOE = (Total Lifetime Costs including capex, opex, financing) / (Total Lifetime Production)
  Capex: $[X]M, amortized over [X] years
  Annual opex: $[X]M
  WACC: [X]%
  P50 annual production: [X] MWh
  LCOE = $[X]/MWh
  Is LCOE < PPA price? [Yes/No] → [Positive/Negative] project economics

Project finance debt:
  Senior debt: $[X]M ([X]% of total project cost)
  Tenor: [X] years (mini-perm / fully amortizing / sculpted)
  Rate: [X]%
  Target DSCR: [X]x minimum, [X]x average
  Cash sweep: [X]% of excess cash above [X]x DSCR
  Reserve accounts: [X] months of debt service, [X] months of O&M

Equity returns:
  Total project cost: $[X]M
  Equity: $[X]M
  Equity IRR (pre-tax): [X]%
  Equity IRR (after-tax, including tax credits): [X]%
  Cash yield (Year 1): [X]%
  Payback period: [X] years
```

---

## 5. Infrastructure Debt

### Project Finance DSCR and Cash Waterfall

```
Structure project finance debt for [infrastructure asset]:

Asset: [toll road / power plant / water treatment / telecom tower portfolio]
Total project cost: $[X]M
Expected annual EBITDA (stabilized): $[X]M

Debt sizing:
- Target minimum DSCR: [X]x
- Target average DSCR: [X]x
- Maximum debt = EBITDA / (Debt Service at target DSCR)

Method 1 — DSCR sculpting:
  Debt service in each period sculpted to maintain [X]x DSCR:
  Max debt service(t) = CFADS(t) / [X]x
  Where CFADS = Cash Flow Available for Debt Service = EBITDA - Taxes - Working Capital - Maintenance Capex
  Sculpted repayment profile matches the cash flow profile of the asset

Method 2 — Fixed amortization:
  Level annual debt service over [X] years
  DSCR varies year-to-year with cash flow fluctuations
  Minimum DSCR must exceed [X]x in all periods (including downside)

Senior debt terms:
- Amount: $[X]M
- Tenor: [X] years (matching concession or useful life, with [X]-year tail)
- Rate: [X]% fixed / SOFR + [X]bps floating (with interest rate swap)
- Amortization: [sculpted / annuity / bullet with cash sweep]

Cash waterfall (priority of payments):
1. Operating expenses and taxes
2. Senior debt service (interest + scheduled principal)
3. Maintenance reserve account funding ($[X]M target)
4. Debt service reserve account (DSRA): [X] months of debt service = $[X]M
5. Cash sweep: [X]% of excess cash applied to senior debt prepayment
   (Sweep activated when DSCR > [X]x; retained when DSCR < [X]x)
6. Subordinated debt service (if any)
7. Restricted payment conditions test: leverage < [X]x, DSCR > [X]x
8. Distribution to equity holders

Step-up pricing:
- Base spread: SOFR + [X]bps (construction period)
- Step-down to SOFR + [X]bps at COD (commercial operation date)
- Step-up of +[X]bps if leverage > [X]x (margin ratchet)

Lock-up and distribution test:
- Backward-looking DSCR: [X]x (LTM actual)
- Forward-looking DSCR: [X]x (projected 12 months)
- Both must be satisfied to distribute cash to equity
- If either breached: cash trapped in project company accounts
```

---

## Mathematical Frameworks

**WACC for Regulated Assets**:

```
WACC = (E/V) x Re + (D/V) x Rd x (1 - t)

For regulated utilities, the regulator often sets each component:
  E/V = regulatory equity ratio (often 40-50%)
  Re = allowed ROE (typically 9-11% in US, varies by jurisdiction)
  D/V = regulatory debt ratio (often 50-60%)
  Rd = embedded cost of debt (based on actual or benchmark debt costs)
  t = corporate tax rate

Regulatory WACC ≠ Market WACC:
  If market WACC < regulatory WACC: utility earns above market-required returns → premium to rate base
  If market WACC > regulatory WACC: utility earns below market → discount to rate base
```

**Real vs. Nominal Returns**:

```
(1 + Nominal Return) = (1 + Real Return) x (1 + Inflation)

Infrastructure assets with inflation-linked revenue:
  If revenue escalates at CPI and costs are largely fixed:
  Real return ≈ Nominal return - Inflation
  A 10% nominal IRR with 3% inflation = ~6.8% real IRR

For comparing across geographies with different inflation rates:
  Always compare real returns to avoid being fooled by high-inflation nominal yields
  A 15% nominal IRR in a 10% inflation country ≈ 4.5% real IRR
  A 9% nominal IRR in a 2% inflation country ≈ 6.9% real IRR
  The "lower" nominal return is actually the better investment in real terms
```

**Contracted Revenue Analysis**:

```
Revenue certainty spectrum:
  Availability-based (highest certainty): fixed payments for asset availability
  Contracted (PPA, take-or-pay): volume risk transferred but price locked
  Regulated (tariff): price set by regulator, volume subject to demand
  Merchant (lowest certainty): both price and volume at market risk

Contracted revenue ratio = Contracted Revenue / Total Revenue
  > 80%: core infrastructure, lower return target (8-10% equity IRR)
  50-80%: core-plus, moderate return target (10-14%)
  < 50%: value-add/opportunistic, higher return target (14-18%+)

Weighted average contract life (WACL):
  WACL = Σ (Contract Revenue_i x Remaining Term_i) / Σ Contract Revenue_i
  Longer WACL = more cash flow visibility = lower risk premium
```

**LCOE (Levelized Cost of Energy)**:

```
LCOE = Σ(Capex_t + Opex_t + Financing_t) / Σ(Energy_t)
     = [NPV of total lifetime costs] / [NPV of total lifetime energy production]

Both numerator and denominator discounted at WACC.
LCOE < PPA price → positive NPV project
LCOE > merchant price forecast → project may not be viable without subsidies

Sensitivity: each $100/kW reduction in capex reduces LCOE by ~$[X]/MWh
            each 1pp increase in capacity factor reduces LCOE by ~$[X]/MWh
```

---

## See Also

- [`../roles/pe-analyst.md`](../roles/pe-analyst.md) — Core PE returns analysis and due diligence frameworks
- [`real-estate.md`](real-estate.md) — Real asset valuation (cap rates, development analysis)
- [`private-credit.md`](private-credit.md) — Project finance debt structuring, DSCR analysis
- [`special-situations.md`](special-situations.md) — Distressed infrastructure, opportunistic real assets
