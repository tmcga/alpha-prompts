# Structured Products -- MBS, ABS, CLOs, CDOs

```
You are a senior structured products trader and analyst with expertise in mortgage-
backed securities (agency and non-agency), collateralized loan obligations (CLOs),
asset-backed securities (ABS), and bespoke structured credit. You understand
prepayment modeling (CPR, CDR, PSA), waterfall mechanics, OC/IC tests, tranche
subordination, and credit enhancement structures. You can analyze cash flow waterfalls,
calculate expected losses across the capital structure, and evaluate relative value
between tranches and across deals. You think in terms of OAS, WAL (weighted average
life), credit enhancement, excess spread, and the interplay between collateral
performance and structural features. You are current on Dodd-Frank risk retention
rules, Volcker Rule implications, and Basel III/IV securitization capital framework.
```

## What This Desk Does

The structured products desk trades securities backed by pools of loans or receivables. These instruments are divided into tranches with different risk profiles, payment priorities, and credit enhancement levels. MBS traders focus on agency pass-throughs, CMOs, and non-agency RMBS, where prepayment risk is the dominant variable. CLO and ABS traders analyze corporate loan and consumer credit pools, focusing on default rates, recovery assumptions, and waterfall mechanics. The desk requires deep quantitative skills to model cash flows under multiple scenarios, and strong credit judgment to evaluate collateral quality and structural protections.

---

## 1. MBS Analysis

**Prepayment metrics:**
- **CPR (Conditional Prepayment Rate):** annualized percentage of remaining principal that prepays
- **SMM (Single Monthly Mortality):** monthly prepayment rate. SMM = 1 - (1 - CPR)^(1/12)
- **PSA (Public Securities Association) model:** CPR ramps linearly from 0% to 6% over 30 months, then stays at 6%. 100% PSA = this baseline; 200% PSA = double speed.
- **CDR (Conditional Default Rate):** annualized rate of defaults on the pool

**OAS for MBS:**
Unlike corporate bonds, MBS OAS accounts for prepayment optionality. The OAS is the spread to the Treasury curve after modeling thousands of interest rate paths and the associated prepayment behavior on each path.

**IO/PO strip sensitivity:**
- IO (Interest Only): benefits from slower prepayments (more principal outstanding longer), hurt by faster prepayments. Negative effective duration (prices rise when rates rise).
- PO (Principal Only): benefits from faster prepayments (principal returned sooner), hurt by slower prepayments. Very high effective duration.

```
Analyze this MBS for relative value and prepayment risk:

- Security: [CUSIP / POOL_ID]
- Type: [AGENCY_PT / CMO / NON_AGENCY / IO / PO]
- Issuer: [FNMA / FHLMC / GNMA / PRIVATE_LABEL]
- Coupon: [COUPON]%
- WAC (Weighted Average Coupon): [WAC]%
- WAM (Weighted Average Maturity): [WAM] months
- WALA (Weighted Average Loan Age): [WALA] months
- Current factor: [FACTOR]
- Price: [PRICE]
- OAS: [OAS] bps
- Effective duration: [EFF_DUR]
- Prepayment speed (1M / 3M / 6M / 12M CPR): [CPR_1M] / [CPR_3M] / [CPR_6M] / [CPR_12M]

Provide:
1. Prepayment model projection: base case, +100bps rate shock, -100bps rate shock
2. OAS decomposition: how much spread compensates for prepayment uncertainty vs credit
3. WAL (weighted average life) under each prepayment scenario
4. Effective duration and convexity (negative convexity assessment)
5. Relative value: compare to TBA (To Be Announced) of same coupon, and to comparable pools
6. For IO/PO: sensitivity table of price vs CPR scenario
```

```
Compare agency MBS versus investment-grade corporates for a portfolio allocation:

- MBS candidate: [COUPON]% FNMA 30Y, Price [PRICE_MBS], OAS [OAS_MBS] bps
- IG corp candidate: [ISSUER] [COUPON_CORP]% [MATURITY], OAS [OAS_CORP] bps
- Portfolio duration target: [TARGET_DUR]
- Convexity preference: [POSITIVE / NEUTRAL / WILLING_TO_BE_SHORT]

Evaluate:
1. Spread comparison on OAS basis (apples-to-apples after adjusting for prepayment option)
2. Convexity cost of MBS: how much OAS compensates for negative convexity?
3. Carry profile: MBS coupon income vs corporate, after financing
4. Liquidity comparison: bid-ask, repo availability, TBA roll market
5. Scenario analysis: parallel and non-parallel rate shocks
```

---

## 2. CLO Analysis

**CLO structure:**
A CLO pools leveraged loans and issues tranches: AAA, AA, A, BBB, BB, equity.

**Key tests:**
- **OC (Overcollateralization) test:** Par value of collateral / par value of tranche >= OC trigger. Failure diverts cash flows to deleverage senior tranches.
- **IC (Interest Coverage) test:** Interest income from collateral / interest owed on tranche >= IC trigger. Failure diverts interest cash flows.

**Equity IRR drivers:** excess spread, default rate, recovery rate, reinvestment, WAL, call timing.

```
Evaluate this CLO tranche for investment:

- Deal: [CLO_NAME] [VINTAGE]
- Manager: [CLO_MANAGER]
- Tranche: [CLASS] ([RATING])
- Coupon: SOFR + [SPREAD] bps
- Price: [PRICE]
- Discount margin: [DM] bps
- Attachment point: [ATTACH]% / Detachment point: [DETACH]%
- Credit enhancement (subordination): [CE]%
- Current OC test level: [OC_ACTUAL] vs trigger [OC_TRIGGER]
- Current IC test level: [IC_ACTUAL] vs trigger [IC_TRIGGER]
- Collateral par: $[COLLATERAL_PAR]M
- CCC bucket: [CCC_PCT]% (limit: [CCC_LIMIT]%)
- WARF (Weighted Average Rating Factor): [WARF]
- WAS (Weighted Average Spread): [WAS] bps
- Reinvestment period remaining: [REINV_MONTHS] months
- Default rate assumption: [CDR]% annual

Provide:
1. Tranche expected loss under base, stress, and severe scenarios
2. OC cushion: how many defaults (in $ and %) before OC test fails?
3. Cash flow modeling: expected WAL, yield, and principal timing
4. Manager assessment: historical default rate, recovery rate, trading style
5. Relative value vs comparable tranches (same rating, different vintage/manager)
6. Tail risk: scenario where CCC bucket breaches limit, or OC test fails
```

```
Analyze CLO equity for a potential investment:

- Deal: [CLO_NAME], Vintage: [YEAR]
- Equity tranche size: $[EQ_SIZE]M
- Current equity NAV: $[NAV] (as % of par: [NAV_PCT]%)
- WAS (collateral spread): [WAS] bps
- Liability cost (weighted avg): SOFR + [LIB_COST] bps
- Excess spread: [EXCESS] bps
- Current annualized default rate: [DEFAULT_RATE]%
- Recovery rate assumption: [RECOVERY]%
- Reinvestment period end: [REINV_END_DATE]
- Non-call period end: [NC_END_DATE]
- Current distributions: $[DIST] per quarter ([DIST_YIELD]% annualized)

Model:
1. Projected IRR under base case (steady defaults, stable spreads)
2. Upside scenario: spreads tighten, call/reset option value
3. Downside scenario: defaults spike to [STRESS_CDR]%, recoveries fall to [STRESS_RR]%
4. Sensitivity table: IRR vs default rate vs recovery rate matrix
5. Optionality: value of refinancing liabilities vs calling the deal
6. Comparison to buying leveraged loans directly (CLO equity as leveraged loan beta)
```

---

## 3. ABS Evaluation

ABS covers consumer and commercial receivables: auto loans, credit cards, student loans, equipment leases, and more.

**Key collateral metrics by sector:**
- Auto ABS: FICO distribution, LTV, new vs used, term, loss severity, delinquency roll rates
- Credit card ABS: payment rate, yield, charge-off rate, excess spread, early amortization triggers
- Student loan ABS: FFELP (government-guaranteed) vs private, IBR/PAYE enrollment, CDR, forbearance

**Excess spread:**
Excess spread = gross portfolio yield - coupon on liabilities - servicing fee - expected losses.
This is the first line of defense absorbing losses before subordination.

```
Evaluate this ABS deal:

- Asset class: [AUTO / CREDIT_CARD / STUDENT_LOAN / EQUIPMENT / OTHER]
- Issuer/Sponsor: [ISSUER]
- Tranche: [CLASS] ([RATING])
- Coupon: [FIXED/FLOAT] [RATE]%
- Price: [PRICE]
- Credit enhancement: [CE]% (subordination [SUB]% + OC [OC]% + excess spread [XS]%)
- Collateral characteristics:
  - Pool balance: $[POOL_BAL]M
  - Weighted average coupon/APR: [WAC]%
  - Weighted average remaining term: [WART] months
  - FICO (if applicable): [FICO_WA] weighted avg, [FICO_DIST] distribution
  - Delinquency (30+ days): [DQ]%
  - Cumulative net loss (to date): [CNL]%
  - Loss curve benchmark: [LOSS_CURVE] (e.g., "Month 24 of 60 on the static pool loss curve")

Provide:
1. Loss projection: expected cumulative net loss at deal maturity
2. Credit enhancement adequacy: loss multiples at current CE levels
3. Cash flow timing: expected WAL, principal window, extension risk
4. Comparison to issuer's prior vintages (loss performance trend)
5. Trigger analysis: what loss level trips early amortization or performance triggers?
6. Relative value vs comparable deals and vs corporate bonds of same rating
```

---

## 4. Tranche Analysis

**Credit enhancement mechanics:**
- Subordination: junior tranches absorb losses first, protecting senior tranches
- Overcollateralization: collateral exceeds liabilities, providing a cushion
- Excess spread: interest income exceeds costs, captured in a reserve
- Reserve accounts: pre-funded cash reserves for initial losses

**Expected loss by tranche:**
Expected loss = Probability(loss reaches attachment) * Loss given attachment
For a tranche with attachment A and detachment D:
If pool loss L < A: tranche loss = 0
If A <= L <= D: tranche loss = (L - A) / (D - A)
If L > D: tranche loss = 100%

```
Perform tranche analysis for this securitization:

Deal: [DEAL_NAME]
Collateral: [COLLATERAL_TYPE], Pool balance: $[POOL]M

Capital structure:
| Tranche | Rating | Size ($M) | Attach | Detach | CE (%) | Coupon      |
|---------|--------|-----------|--------|--------|--------|-------------|
| A       | [R_A]  | [S_A]     | [AT_A] | [DT_A] | [CE_A] | [COUPON_A]  |
| B       | [R_B]  | [S_B]     | [AT_B] | [DT_B] | [CE_B] | [COUPON_B]  |
| C       | [R_C]  | [S_C]     | [AT_C] | [DT_C] | [CE_C] | [COUPON_C]  |
| D       | [R_D]  | [S_D]     | [AT_D] | [DT_D] | [CE_D] | [COUPON_D]  |
| Equity  | NR     | [S_EQ]    | 0%     | [DT_E] | 0%     | Residual    |

Loss scenarios:
| Scenario     | Cumulative loss | Recovery |
|--------------|-----------------|----------|
| Base         | [LOSS_BASE]%    | [RR_B]%  |
| Stress       | [LOSS_STRESS]%  | [RR_S]%  |
| Severe       | [LOSS_SEVERE]%  | [RR_V]%  |

For each tranche and scenario, calculate:
1. Tranche loss (%) and dollar loss
2. Expected WAL and principal payment timing
3. Yield / discount margin at current price
4. Loss multiple: how many times base-case loss before tranche is impaired?
5. Rating agency stress: does the CE support the current rating?
6. Relative value: spread per unit of expected loss across the capital structure
```

---

## 5. Securitization Structuring

**SPV (Special Purpose Vehicle) mechanics:** Bankruptcy-remote entity isolates assets from the originator. True sale opinion ensures assets cannot be clawed back in originator bankruptcy.

**Risk retention (Dodd-Frank Section 941):**
Sponsor must retain >= 5% of credit risk. Options: vertical slice (5% of each tranche), horizontal slice (first-loss equity), or L-shaped (combination).

**Regulatory capital (Basel III/IV securitization framework):**
- SEC-IRBA: Internal ratings-based approach (requires supervisory approval)
- SEC-ERBA: External ratings-based approach (uses rating agency ratings)
- SEC-SA: Standardized approach (based on capital requirement of underlying pool)
- Capital floor: p = max(capital_required, 15% for senior, 100% for re-securitization)

```
Structure a securitization for this loan portfolio:

- Originator: [ORIGINATOR]
- Asset class: [AUTO_LOANS / MORTGAGES / CORP_LOANS / CREDIT_CARDS / OTHER]
- Pool characteristics:
  - Total balance: $[POOL_BAL]M
  - Number of loans: [NUM_LOANS]
  - Weighted average coupon: [WAC]%
  - Weighted average maturity: [WAM] months
  - Weighted average LTV/CLTV: [LTV]% (if applicable)
  - Geographic concentration: [GEO_CONC]
  - Historical loss rate (originator's portfolio): [HIST_LOSS]%

Design the capital structure:
1. Propose tranche sizes, ratings targets, and credit enhancement levels
2. Set attachment and detachment points for each tranche
3. Determine excess spread capture mechanism (turbo vs reserve account vs OC)
4. Waterfall priority: sequential pay vs pro-rata, with trigger switching provisions
5. Risk retention strategy: vertical, horizontal, or L-shaped? Regulatory compliance.
6. Estimate all-in cost of funds vs unsecured debt and whole-loan financing
7. Regulatory capital treatment for retained tranches (SEC-ERBA or SEC-SA)
```

```
Evaluate a risk retention trade:

- Deal: [DEAL_NAME]
- Sponsor retention method: [VERTICAL / HORIZONTAL / L_SHAPED]
- Retained piece: [DESCRIPTION] ($[SIZE]M, [PCT]% of deal)
- Expected yield on retained piece: [YIELD]%
- Capital charge on retained piece: [CAP_CHARGE]% RWA
- Sponsor cost of equity: [COE]%
- Sponsor cost of debt: [COD]%

Calculate:
1. Return on allocated capital for the retained piece
2. Breakeven loss rate: at what pool loss does the retained piece lose principal?
3. Comparison: does the risk retention create positive or negative economics?
4. Alternative structures that minimize capital impact while satisfying the rule
5. Impact on deal execution: does the retention signal alignment of interest to investors?
```

---

## See Also

- [fixed-income.md](fixed-income.md) -- for spread analysis frameworks applicable to structured credit
- [derivatives.md](derivatives.md) -- for embedded optionality in callable/putable structures
- [market-making.md](market-making.md) -- for structured products secondary market liquidity
