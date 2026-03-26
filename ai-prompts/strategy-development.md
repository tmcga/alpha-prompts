# Strategy Development Prompts

Prompt templates for using LLMs to assist with quantitative trading strategy design, parameter tuning, and backtest analysis.

## 1. Design a New Strategy

Use this when you have a trading hypothesis and want to turn it into a concrete strategy implementation.

```
I'm building a trading strategy for the Neural Partners backtesting framework.

Context:
- Strategies inherit from the Strategy base class and implement generate_signals(df) -> pd.Series
- Signals are -1 (short), 0 (flat), or 1 (long)
- The DataFrame has OHLCV columns (open, high, low, close, volume) plus any indicators added by indicators.py
- Available indicators: SMA, EMA, RSI, MACD, ATR, ADX, Bollinger z-score, linear regression residual/z-score, realized volatility

My hypothesis: [describe your trading idea, e.g. "mean reversion works better in low-volatility regimes"]

Please:
1. Suggest which indicators to use and why
2. Define entry/exit conditions with specific thresholds
3. Write the strategy class implementation
4. Suggest parameter ranges for optimization
5. Identify what market conditions this strategy would fail in
```

## 2. Analyze Backtest Results

Use this after running a backtest to get AI interpretation of the results.

```
Here are the backtest results for my [strategy name] strategy:

- Annualized Return: [X]%
- Annualized Volatility: [X]%
- Sharpe Ratio: [X]
- Sortino Ratio: [X]
- Max Drawdown: [X]%
- Win Rate: [X]%
- Profit Factor: [X]
- Number of Trades: [X]
- Period: [start] to [end]
- Asset: [symbol]

Please analyze:
1. Is this strategy viable? What are the red flags?
2. Does the Sharpe ratio hold up given the number of trades (statistical significance)?
3. What does the drawdown-to-return ratio suggest about risk?
4. How might these results differ in live trading (slippage, execution, regime change)?
5. What parameter adjustments would you suggest?
```

## 3. Parameter Optimization Guidance

Use this when deciding which parameters to optimize and what ranges to explore.

```
I have a [strategy type] strategy with these parameters:
- [param1]: currently [value], controls [what it does]
- [param2]: currently [value], controls [what it does]
- [param3]: currently [value], controls [what it does]

The strategy is trading [asset class] on [timeframe] data.

Current performance: Sharpe [X], Max DD [X]%, [X] trades over [period].

Help me:
1. Which parameters are most likely to improve risk-adjusted returns?
2. What ranges should I search for each parameter?
3. Are any of these parameters likely overfitting to historical data?
4. Should I add regime filters (e.g., ADX for trend strength, vol percentile)?
5. What's the minimum number of trades needed to trust the optimization results?
```

## 4. Regime Detection Design

Use this when adding market regime awareness to a strategy.

```
I want to add regime detection to my [strategy name] to only trade in favorable conditions.

The strategy is a [type: mean reversion / trend following / momentum] strategy.

Available regime indicators I can compute:
- ADX (trend strength)
- Realized volatility percentile
- Implied volatility rank (for equity options)
- RSI (overbought/oversold)
- Bollinger bandwidth (squeeze detection)

Questions:
1. Which regime filters make sense for this strategy type?
2. What thresholds should I use (e.g., "only trade when ADX < 25")?
3. Should I use regime as a binary gate (trade/don't trade) or scale position size?
4. How do I avoid over-filtering and reducing the trade count too much?
```

## 5. Ensemble Strategy Weighting

Use this when combining multiple strategies into an ensemble.

```
I'm building an ensemble of these strategies for a multi-asset fund:

1. [Strategy 1]: [type], Sharpe [X], correlation with others [low/med/high]
2. [Strategy 2]: [type], Sharpe [X], correlation with others [low/med/high]
3. [Strategy N]: [type], Sharpe [X], correlation with others [low/med/high]

Current equal-weight ensemble Sharpe: [X]

Help me think about:
1. How should I weight these strategies? (equal weight, inverse-vol, Sharpe-weighted, optimization)
2. Should I use conviction scaling (increase size when multiple strategies agree)?
3. What's the risk of optimizing weights on historical data?
4. How many strategies do I need before the ensemble benefit plateaus?
5. Should any of these strategies be excluded based on correlation?
```
