# Quant Signals: Earnings Momentum Factor

## Research Phase
Signal construction + backtesting

## Signal Type
Fundamental factor — earnings momentum (post-earnings announcement drift)

## Asset Class
US equities — single stock, large and mid cap (Russell 1000 universe)

## Hypothesis
Stocks that beat EPS estimates by >5% exhibit positive drift for 20-40 trading days post-announcement. The drift is stronger when accompanied by upward guidance revision and is weakened by high short interest. Combining earnings surprise with guidance revision creates a composite signal with better Sharpe than either alone.

## Signal Construction
- **Primary Signal:** Standardized Unexpected Earnings (SUE) = (Actual EPS - Consensus EPS) / Std Dev of Estimates
- **Secondary Signal:** Guidance revision score = (New guidance midpoint - Prior guidance midpoint) / Prior guidance midpoint
- **Composite:** 0.6 * SUE_rank + 0.4 * Guidance_rank
- **Filter:** Exclude stocks with short interest > 15% (crowded shorts distort drift)

## Data Available
- OHLCV daily prices for Russell 1000 (5 years)
- Quarterly EPS actuals vs consensus (5 years, 20 quarters)
- Guidance revisions (when available, ~60% of universe provides guidance)
- Short interest (bi-monthly snapshots)
- Sector classifications (GICS)

## Backtest Parameters
- **Universe:** Russell 1000
- **Rebalance:** Weekly (every Monday after earnings announcement window)
- **Holding Period:** 20 trading days
- **Position Sizing:** Equal-weight top/bottom decile
- **Transaction Costs:** 5bps each way
- **Benchmark:** Russell 1000 equal-weight

## Overfitting Concerns
- Testing one primary hypothesis with one secondary modifier — not a parameter sweep
- Will check: out-of-sample (2-year holdout), decay profile, sector neutrality, turnover cost sensitivity

## Try It
```
/quant

Building an earnings momentum signal on Russell 1000. Hypothesis: stocks
beating EPS by >5% drift positively for 20-40 days, especially with upward
guidance revision. Composite signal: 0.6 * SUE rank + 0.4 * guidance revision
rank. Filter out stocks with >15% short interest. Backtest with weekly rebalance,
20-day holding period, equal-weight top/bottom decile, 5bps transaction costs.
5 years of data with 2-year holdout. Help me construct the signal and design
the backtest to avoid overfitting.
```
