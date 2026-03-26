# Example Output: Retirement Planning — Monte Carlo Simulation

> This is an annotated example of what a `/wealth` analysis produces. All data is fictional.

---

## Client Profile

| Parameter | Value |
|-----------|-------|
| Clients | Couple, ages 58 and 55 |
| Total Net Worth | $5,400,000 |
| Retirement Age | 62 (4 years) |
| Planning Horizon | Age 95 (37 years from now) |
| Annual Spending | $180,000 + $25,000 travel (first 10 years) |
| Social Security | $62,000/year starting at age 67 |
| Legacy Goal | $1,000,000+ to children |

---

## Monte Carlo Simulation

```
$ python3 tools/monte_carlo.py --initial 5400000 --return 0.065 --vol 0.14 --years 37 --withdrawal 0.038 --seed 42

==================================================
  Monte Carlo Simulation (10,000 paths)
==================================================
  Initial Value:     $   5,400,000
  Expected Return:            6.5%
  Volatility:                14.0%
  Horizon:                     37 years
  Withdrawal Rate:            3.8%
──────────────────────────────────────────────────
  Terminal Value Distribution:
    1st Percentile:  $           0
    5th Percentile:  $           0
   10th Percentile:  $           0
   25th Percentile:  $   4,814,904
   50th (Median):    $  16,197,323
   75th Percentile:  $  37,056,950
   90th Percentile:  $  71,538,249
   95th Percentile:  $ 106,062,184
──────────────────────────────────────────────────
  Ruin Probability:          11.7%
==================================================
```

> **Reading this output:** The 3.8% withdrawal rate (=$205K on $5.4M) gives an **88.3% success rate** through age 95. The median terminal value is $16.2M — more than enough for the $1M legacy goal. However, the 11.7% ruin probability is meaningful. The left tail (1st-10th percentile = $0) reflects sequence-of-returns risk in the early retirement years.

---

## Key Findings

### 1. Success Probability: 88.3% — Adequate but Not Comfortable

| Scenario | Probability | Terminal Wealth |
|----------|------------|----------------|
| Ruin (money runs out) | 11.7% | $0 |
| Tight (below $500K) | 15.2% | <$500K |
| Comfortable ($500K-$5M) | 22.1% | Modest legacy |
| Affluent ($5M-$20M) | 28.4% | Legacy goal met |
| Wealthy ($20M+) | 34.3% | Significant legacy |

> **The bimodal nature of retirement outcomes:** Because of compounding, outcomes are highly dispersed. In the good scenarios, the couple dies with $16-70M+. In the bad scenarios, they run out of money in their 80s. The difference is almost entirely determined by returns in the first 5-7 years of retirement (sequence-of-returns risk).

### 2. Concentration Risk: The $630K Tech Stock Problem

The single tech position ($630K, 35% of taxable account) creates two risks:
- **Volatility drag:** Single-stock vol is 35-50%, much higher than the 14% portfolio assumption
- **Tax trap:** $400K unrealized gain means selling triggers ~$80K LTCG tax

**Recommendation:** Systematic de-risking over 3 years:
- Year 1: Sell $210K, harvest other losses to offset, net tax ~$15K
- Year 2: Sell $210K, use charitable giving (donor-advised fund) for $50K of shares
- Year 3: Sell remaining $210K, reinvest into diversified index

### 3. Improving the Odds: From 88% to 95%

| Lever | Impact on Success Rate | Tradeoff |
|-------|----------------------|----------|
| Reduce spending to $170K (-$10K) | +3% → 91% | Modest lifestyle adjustment |
| Delay retirement to 64 (+2 years) | +5% → 93% | 2 more years of income + contributions |
| Reduce withdrawal to 3.5% | +4% → 92% | $189K spending vs. $205K |
| All three combined | +9% → 97% | Conservative but very safe |

### 4. Healthcare Gap Strategy (Ages 62-65)

Estimated cost: $28,000/year × 3 years = $84,000 before Medicare eligibility.

Options:
- **ACA marketplace:** $18-24K/year with income management (keep MAGI under cliff)
- **COBRA extension:** $28K/year (18 months max from current employer)
- **Health share ministry:** $8-12K/year (lower cost, less coverage)

**Recommendation:** ACA marketplace with Roth conversion strategy — control MAGI to optimize premium subsidies while converting traditional IRA to Roth during the low-income gap years.

---

## Recommended Portfolio Allocation (Post-Retirement)

| Asset Class | Current | Recommended | Rationale |
|------------|---------|------------|-----------|
| US Large Cap | 40% | 30% | Reduce equity risk at retirement |
| US Small Cap | 5% | 5% | Maintain growth exposure |
| International | 10% | 15% | Diversification benefit |
| Single Tech Stock | 12% | 0% | Eliminate concentration |
| Bonds (IG + TIPS) | 18% | 30% | Income + inflation protection |
| Real Estate (rental) | 12% | 12% | Keep — $38K/year income |
| Cash | 3% | 8% | 2-year spending buffer |

---

## What Kills This Plan

1. **Sequence of returns:** A -30% drawdown in years 1-3 of retirement drops success rate below 70%. Mitigation: 2-year cash buffer + bond tent strategy.
2. **Inflation spike to 5%+:** Spending grows faster than portfolio. Mitigation: TIPS allocation + real estate income (inflation-linked rents).
3. **Long-term care event:** Not modeled here. A 3-year nursing home stay ($100K/year) would consume $300K. Mitigation: Long-term care insurance evaluation needed.
4. **Longevity beyond 95:** Family history suggests possible. If planning to 100, success rate drops to ~80%. Consider longevity annuity for floor income.

---

*This analysis was produced using Alpha Stack's `/wealth` skill with Monte Carlo simulation.*
