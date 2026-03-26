# Performance Attribution: Quarterly Equity Fund Review

## Portfolio Data (End of Quarter)
| Sector | Portfolio Weight | Portfolio Return | Benchmark Weight | Benchmark Return |
|--------|-----------------|-----------------|-----------------|-----------------|
| Technology | 32% | 8.5% | 28% | 6.2% |
| Healthcare | 18% | 3.2% | 14% | 4.8% |
| Financials | 12% | 5.1% | 13% | 4.5% |
| Consumer Discretionary | 10% | -2.1% | 11% | 1.3% |
| Industrials | 9% | 4.8% | 9% | 3.9% |
| Energy | 5% | 7.2% | 5% | 6.8% |
| Communication Services | 6% | 2.5% | 8% | 5.1% |
| Consumer Staples | 3% | 1.8% | 6% | 2.2% |
| Materials | 3% | 3.5% | 3% | 2.9% |
| Utilities | 0% | — | 2% | 4.1% |
| Real Estate | 2% | -1.5% | 1% | -0.8% |

## Attribution Type
Brinson-Fachler (allocation + selection + interaction)

## Benchmark
S&P 500

## Time Period
Q4 (single quarter)

## Context
Portfolio outperformed benchmark by ~120bps. CIO wants to understand: was it stock picking or sector bets? The overweight in tech and underweight in staples/utilities were intentional. The underperformance in healthcare (below benchmark) and consumer discretionary (negative) need explanation.

## Try It
```
/attribution

Quarterly equity fund attribution vs S&P 500. Portfolio returned ~4.8%,
benchmark ~4.2%. Overweight tech (32% vs 28%, returned 8.5% vs 6.2%).
Underweight staples (3% vs 6%) and zero utilities. Healthcare underperformed
benchmark (3.2% vs 4.8% despite 18% weight). Consumer discretionary lost
money (-2.1%). Run Brinson-Fachler — was the alpha from allocation or selection?
```
