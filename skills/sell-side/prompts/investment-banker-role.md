# Investment Banker

Prompt library for investment banking analysts and associates. Covers valuation, deal structuring, financial modeling, and the quantitative frameworks used in M&A, capital markets, and restructuring.

## Role Context

```
You are a senior investment banking analyst. You think in terms of enterprise value,
capital structure, and relative valuation. Every analysis must be defensible in a pitch book
and withstand scrutiny from a managing director. You are precise with financial terminology,
conservative with assumptions, and always triangulate valuation using multiple methodologies.
```

---

## 1. Valuation

### DCF Valuation

```
I'm building a DCF model for [company name / description] in [industry].

Financial data:
- Revenue (LTM): $[X]
- EBITDA margin: [X]%
- Capex as % of revenue: [X]%
- Revenue growth rate (next 3-5 years): [X]%
- Current debt: $[X]
- Cash: $[X]
- Shares outstanding: [X]M
- Tax rate: [X]%

Help me build a rigorous DCF:

1. **Unlevered Free Cash Flow projection** (5-10 year explicit period):
   UFCF = EBIT × (1 - tax) + D&A - Capex - ΔWorking Capital

2. **WACC calculation**:
   WACC = (E/V) × r_e + (D/V) × r_d × (1 - t)
   where r_e = r_f + β × (r_m - r_f)  [CAPM]
   - What risk-free rate, equity risk premium, and beta should I use?
   - Should I use levered or unlevered beta? Re-lever to target capital structure?

3. **Terminal value** (choose and justify):
   - Gordon Growth: TV = UFCF_terminal × (1 + g) / (WACC - g)
   - Exit multiple: TV = EBITDA_terminal × EV/EBITDA_multiple
   - What terminal growth rate is defensible? (typically 2-3%, never above GDP growth)

4. **Sensitivity analysis**: WACC (±100bps) vs. terminal growth rate (±50bps) matrix

5. **Sanity checks**: Does the implied exit multiple make sense? Does TV as % of enterprise value concern you?
```

### Comparable Company Analysis

```
I'm doing a comps analysis for [target company] in [industry].

Target financials:
- Revenue: $[X]
- EBITDA: $[X]
- Net Income: $[X]
- Revenue growth: [X]%
- EBITDA margin: [X]%

Comparable companies: [list names or describe criteria]

Help me:
1. Select the right peer group (same industry, size, growth profile, margin structure)
2. Calculate and compare these multiples:
   - EV/Revenue (for high-growth or pre-profit companies)
   - EV/EBITDA (primary multiple for most sectors)
   - EV/EBIT (when D&A varies significantly across peers)
   - P/E (for mature, stable-earnings companies)
   - PEG ratio (P/E normalized by growth)
3. Determine where the target should trade within the peer range:
   - Premium: higher growth, better margins, market leader
   - Discount: smaller scale, lower margins, higher risk
4. Calculate the implied valuation range: Target metric × peer multiple range
5. Address pitfalls: cyclicality (use normalized earnings), one-time items (adjust EBITDA), different fiscal years (calendarize)
```

### Precedent Transaction Analysis

```
I'm analyzing precedent M&A transactions for a [target description] in [industry].

Target characteristics:
- Revenue: $[X]
- EBITDA: $[X]
- Growth rate: [X]%

Relevant transactions: [list or describe criteria — same industry, similar size, recent vintage]

Help me:
1. Build a precedent transaction table with:
   - Date, acquirer, target, deal value, EV/Revenue, EV/EBITDA, premium to unaffected price
2. Adjust for:
   - Control premium (typically 20-40% over trading price)
   - Synergy expectations (how much of synergy value was paid away?)
   - Market conditions at time of deal (bull vs. bear market)
   - Strategic vs. financial buyer (strategics typically pay more for synergies)
3. Calculate the implied valuation range for my target
4. Explain why precedent transactions typically yield higher multiples than trading comps
5. Flag stale transactions (>3 years old) and explain when they're still relevant
```

---

## 2. M&A Analysis

### Accretion/Dilution Analysis

```
Acquirer is considering buying Target:

Acquirer:
- Share price: $[X]
- Shares outstanding: [X]M
- EPS (LTM): $[X]
- P/E multiple: [X]x
- Cost of debt (pre-tax): [X]%

Target:
- Offer price: $[X] per share (or $[X] total equity value)
- Shares outstanding: [X]M
- EPS (LTM): $[X]
- Net income: $[X]M

Deal structure: [X]% cash / [X]% stock
Expected synergies: $[X]M pre-tax
Transaction fees: $[X]M

Help me calculate:
1. Pro forma EPS under 100% cash, 100% stock, and proposed mix
2. Accretion/dilution at each structure
3. Break-even synergies needed to make the deal accretive
4. The formula:
   - Pro forma net income = Acquirer NI + Target NI + Synergies×(1-t) - Financing cost×(1-t) - Amortization of intangibles
   - Pro forma shares = Acquirer shares + new shares issued (if stock deal)
   - Accretive if Pro forma EPS > Acquirer standalone EPS
5. Sensitivity: accretion/dilution across different offer prices and cash/stock mixes
```

### LBO Model

```
A PE sponsor is evaluating an LBO of [target company].

Target:
- EBITDA (LTM): $[X]M
- EBITDA growth: [X]% per year
- Capex: $[X]M/year
- Working capital changes: $[X]M/year

Deal assumptions:
- Entry multiple: [X]x EBITDA
- Debt capacity: [X]x EBITDA (total leverage)
- Senior debt rate: [X]%
- Subordinated debt rate: [X]%
- Debt paydown: mandatory amortization + cash sweep
- Sponsor equity: remainder after debt

Help me build the LBO returns analysis:
1. Sources & uses of funds
2. Debt schedule with amortization and cash sweep
3. Free cash flow available for debt paydown each year
4. Exit analysis at Year [3/4/5]:
   - Exit multiple = Entry multiple (base case)
   - Equity value = Enterprise value at exit - Net debt at exit
   - MOIC = Equity at exit / Equity invested
   - IRR = MOIC^(1/years) - 1 (approximate, solve exactly with cash flows)
5. Returns attribution: How much of the return comes from:
   - EBITDA growth (operational improvement)
   - Multiple expansion (market/sentiment)
   - Debt paydown (financial engineering)
   - Formula: IRR ≈ EBITDA_growth_contribution + multiple_change_contribution + deleveraging_contribution
```

---

## 3. Capital Structure & Financing

### Optimal Capital Structure

```
Company profile:
- Industry: [X]
- EBITDA: $[X]M
- Current debt: $[X]M
- Current equity market cap: $[X]M
- Interest coverage: [X]x
- Credit rating: [X]

Help me analyze the optimal capital structure:
1. Modigliani-Miller framework:
   - V_levered = V_unlevered + PV(tax shields) - PV(financial distress costs)
   - Tax shield = D × r_d × t (annual), PV = D × t (if permanent debt)
2. Target credit metrics by rating:
   - Debt/EBITDA, Interest coverage, FFO/Debt for each rating category
3. WACC minimization: find the leverage ratio that minimizes WACC
   - As debt increases: tax shield benefit vs. rising r_d and financial distress risk
4. Peer comparison: where does this company sit vs. industry capital structure norms?
5. Practical considerations: covenant headroom, refinancing risk, cyclicality of cash flows
```

---

## 4. Financial Statement Analysis

### Quality of Earnings

```
I'm analyzing [company]'s financial statements for [purpose: due diligence / credit analysis / equity research].

Key financials (3 years):
- Revenue: [Y1], [Y2], [Y3]
- EBITDA: [Y1], [Y2], [Y3]
- Net income: [Y1], [Y2], [Y3]
- Operating cash flow: [Y1], [Y2], [Y3]
- Capex: [Y1], [Y2], [Y3]

Help me identify red flags and assess earnings quality:
1. Cash conversion: OCF / Net Income ratio (should be >1.0 for quality earnings)
2. Accruals analysis: High accruals (NI >> OCF) suggest aggressive accounting
   - Accrual ratio = (NI - OCF) / Average total assets
3. Revenue quality: Organic vs. acquisition-driven growth, recurring vs. one-time
4. Working capital trends: DSO, DIO, DPO — are they stretching?
5. Off-balance sheet: Operating leases (now capitalized under IFRS 16/ASC 842), guarantees, variable interest entities
6. Adjustments: What EBITDA add-backs are legitimate vs. aggressive?
   - Legitimate: truly one-time restructuring, M&A costs
   - Aggressive: recurring "non-recurring" charges, stock-based comp exclusion, "run-rate" adjustments
```

---

## 5. Industry-Specific Frameworks

### Technology Company Valuation

```
I'm valuing a [SaaS / marketplace / fintech / hardware] company.

Key metrics:
- ARR: $[X]M
- Revenue growth: [X]%
- Net revenue retention: [X]%
- Gross margin: [X]%
- Rule of 40 score: Growth% + FCF margin% = [X]

Help me apply tech-specific frameworks:
1. SaaS multiples: EV/ARR vs. EV/Revenue — when to use which?
2. Rule of 40 valuation: Companies above 40 trade at a premium. Quantify the premium.
3. LTV/CAC analysis: LTV = ARPU × Gross margin / Churn rate. Target LTV/CAC > 3x.
4. Cohort analysis: How does revenue retention by vintage inform valuation?
5. Path to profitability: At what scale does this company reach FCF breakeven?
```

### Bank & Financial Institution Valuation

```
I'm valuing a [commercial bank / investment bank / insurance company].

Key metrics:
- Book value per share: $[X]
- Tangible book value per share: $[X]
- ROE: [X]%
- ROA: [X]%
- NIM (net interest margin): [X]%
- CET1 ratio: [X]%

Help me apply financial institution valuation:
1. Price/Book and Price/Tangible Book — the primary multiple for banks
   - P/B should reflect ROE vs. cost of equity: P/B = (ROE - g) / (r_e - g)
   - Banks trading below 1.0x TBV are earning below their cost of equity
2. Excess return model: Value = Book + PV(future excess returns)
   where excess return = (ROE - COE) × Book value
3. Dividend discount model (preferred for regulated financials):
   V = D₁ / (r_e - g), constrained by regulatory capital requirements
4. Why DCF doesn't work for banks (debt is an operating liability, not financing)
5. Key risk metrics: NPL ratio, provision coverage, liquidity coverage ratio
```
