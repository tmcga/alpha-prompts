# Portfolio Construction: Multi-Asset Endowment Allocation

## Objective
Long-term growth with inflation protection — university endowment

## Asset Universe
| Asset Class | Current Weight | Expected Return | Expected Vol | Notes |
|-------------|---------------|-----------------|-------------|-------|
| US Large Cap Equity | 30% | 8.5% | 16% | S&P 500 index |
| US Small Cap Equity | 8% | 10.0% | 22% | Russell 2000 |
| International Developed | 15% | 7.5% | 18% | MSCI EAFE |
| Emerging Markets | 7% | 9.5% | 24% | MSCI EM |
| US Investment Grade Bonds | 15% | 4.8% | 5% | Bloomberg Agg |
| TIPS | 5% | 3.5% | 6% | Inflation protection |
| Real Estate (REITs) | 8% | 7.0% | 17% | FTSE NAREIT |
| Private Equity | 7% | 12.0% | 25% | Vintage diversified |
| Hedge Funds (L/S) | 5% | 6.5% | 10% | Multi-manager |

## Constraints
- **Minimum Equity:** 40% (board mandate)
- **Maximum Illiquid Assets:** 20% (PE + real estate)
- **Maximum Single Asset Class:** 35%
- **ESG:** Exclude fossil fuel producers (affects EM allocation)
- **Spending Rule:** 5% annual distribution — need to beat spending + inflation

## Benchmark
60/40 blend: 60% MSCI ACWI + 40% Bloomberg Global Agg

## Rebalancing
Quarterly, with 3% drift threshold triggering interim rebalancing

## Views (for Black-Litterman)
1. EM equities will outperform DM by 200bps over next 12 months (conviction: moderate)
2. US rates will decline 75bps, benefiting IG bonds (conviction: high)
3. Real estate will underperform equities by 300bps due to office vacancy (conviction: low)

## Try It
```
/portfolio

University endowment, $2B AUM. Current allocation: 30% US large cap, 8% small
cap, 15% international, 7% EM, 15% IG bonds, 5% TIPS, 8% REITs, 7% PE, 5%
hedge funds. Constraints: min 40% equity, max 20% illiquid, ESG exclusion on
fossil fuels. 5% annual spending rule. Benchmark is 60/40 ACWI/Global Agg.
I have 3 views: EM outperforms DM by 200bps, US rates decline 75bps, real
estate underperforms on office vacancy. Run Black-Litterman and optimize.
```
