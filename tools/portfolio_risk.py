#!/usr/bin/env python3
"""Portfolio risk calculator — Sharpe, Sortino, max drawdown, VaR.

Usage:
    python portfolio_risk.py --returns 0.02,-0.01,0.03,0.01,-0.02,0.04,0.01,-0.03,0.02,0.01 --rf 0.04
    python portfolio_risk.py --file returns.csv --rf 0.04
"""

import argparse
import math
import csv


def portfolio_metrics(returns: list[float], risk_free: float = 0.0, periods_per_year: int = 12) -> dict:
    """Calculate portfolio risk and return metrics.

    Args:
        returns: List of periodic returns (e.g., monthly).
        risk_free: Annual risk-free rate.
        periods_per_year: Periods per year for annualization (12=monthly, 252=daily).

    Returns:
        Dict with all key risk metrics.
    """
    n = len(returns)
    if n < 2:
        raise ValueError("Need at least 2 return observations")

    rf_periodic = risk_free / periods_per_year

    # Mean and standard deviation
    mean_return = sum(returns) / n
    variance = sum((r - mean_return) ** 2 for r in returns) / (n - 1)
    std_dev = math.sqrt(variance)

    # Annualized
    ann_return = (1 + mean_return) ** periods_per_year - 1
    ann_vol = std_dev * math.sqrt(periods_per_year)

    # Sharpe ratio
    sharpe = (ann_return - risk_free) / ann_vol if ann_vol > 0 else 0

    # Sortino ratio (downside deviation)
    downside_returns = [min(r - rf_periodic, 0) for r in returns]
    downside_var = sum(r**2 for r in downside_returns) / (n - 1)
    downside_dev = math.sqrt(downside_var) * math.sqrt(periods_per_year)
    sortino = (ann_return - risk_free) / downside_dev if downside_dev > 0 else 0

    # Max drawdown
    cumulative = 1.0
    peak = 1.0
    max_dd = 0.0
    drawdowns = []
    for r in returns:
        cumulative *= 1 + r
        peak = max(peak, cumulative)
        dd = (cumulative - peak) / peak
        drawdowns.append(dd)
        max_dd = min(max_dd, dd)

    # Calmar ratio
    calmar = ann_return / abs(max_dd) if max_dd != 0 else 0

    # VaR (historical, 95%)
    sorted_returns = sorted(returns)
    var_index = max(0, int(n * 0.05) - 1)
    var_95 = -sorted_returns[var_index]

    # CVaR / Expected Shortfall (95%)
    tail_returns = sorted_returns[: int(n * 0.05) + 1]
    cvar_95 = -sum(tail_returns) / len(tail_returns) if tail_returns else 0

    # Win rate
    wins = sum(1 for r in returns if r > 0)
    win_rate = wins / n

    # Cumulative return (reuse cumulative from drawdown loop)
    cumulative_return = cumulative - 1

    # Parametric VaR (normal assumption)
    param_var_95 = -(mean_return - 1.645 * std_dev)

    result = {
        "ann_return": ann_return,
        "ann_volatility": ann_vol,
        "sharpe": sharpe,
        "sortino": sortino,
        "max_drawdown": max_dd,
        "calmar": calmar,
        "var_95": var_95,
        "var_95_parametric": param_var_95,
        "cvar_95": cvar_95,
        "win_rate": win_rate,
        "cumulative_return": cumulative_return,
        "num_periods": n,
        "best_period": max(returns),
        "worst_period": min(returns),
    }
    return result


def benchmark_relative(returns: list[float], benchmark: list[float], periods_per_year: int = 12) -> dict:
    """Calculate benchmark-relative metrics.

    Args:
        returns: Portfolio periodic returns.
        benchmark: Benchmark periodic returns (same length).
        periods_per_year: Annualization factor.

    Returns:
        Dict with tracking error, information ratio, active return.
    """
    n = min(len(returns), len(benchmark))
    active = [returns[i] - benchmark[i] for i in range(n)]

    mean_active = sum(active) / n
    active_var = sum((a - mean_active) ** 2 for a in active) / (n - 1)
    tracking_error = math.sqrt(active_var) * math.sqrt(periods_per_year)

    ann_active = mean_active * periods_per_year
    info_ratio = ann_active / tracking_error if tracking_error > 0 else 0

    return {
        "active_return": ann_active,
        "tracking_error": tracking_error,
        "information_ratio": info_ratio,
    }


def main():
    parser = argparse.ArgumentParser(description="Portfolio Risk Calculator")
    parser.add_argument("--returns", help="Comma-separated returns")
    parser.add_argument("--file", help="CSV file with returns (one per line)")
    parser.add_argument("--benchmark", help="Comma-separated benchmark returns")
    parser.add_argument("--rf", type=float, default=0.0, help="Annual risk-free rate (default: 0)")
    parser.add_argument("--freq", type=int, default=12, help="Periods per year: 12=monthly, 252=daily (default: 12)")
    args = parser.parse_args()

    if args.returns:
        returns = [float(x.strip()) for x in args.returns.split(",")]
    elif args.file:
        returns = []
        with open(args.file) as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip():
                    try:
                        returns.append(float(row[0].strip()))
                    except ValueError:
                        continue
    else:
        parser.error("Provide --returns or --file")

    r = portfolio_metrics(returns, args.rf, args.freq)

    print(f"\n{'=' * 50}")
    print(f"  Portfolio Risk Analysis ({r['num_periods']} periods)")
    print(f"{'=' * 50}")
    print(f"  Annualized Return:   {r['ann_return'] * 100:>+8.2f}%")
    print(f"  Annualized Vol:      {r['ann_volatility'] * 100:>8.2f}%")
    print(f"  Cumulative Return:   {r['cumulative_return'] * 100:>+8.2f}%")
    print(f"{'─' * 50}")
    print(f"  Sharpe Ratio:        {r['sharpe']:>8.2f}")
    print(f"  Sortino Ratio:       {r['sortino']:>8.2f}")
    print(f"  Calmar Ratio:        {r['calmar']:>8.2f}")
    print(f"{'─' * 50}")
    print(f"  Max Drawdown:        {r['max_drawdown'] * 100:>8.2f}%")
    print(f"  VaR (95% hist):      {r['var_95'] * 100:>8.2f}%")
    print(f"  VaR (95% param):     {r['var_95_parametric'] * 100:>8.2f}%")
    print(f"  CVaR (95%):          {r['cvar_95'] * 100:>8.2f}%")
    print(f"{'─' * 50}")
    print(f"  Win Rate:            {r['win_rate'] * 100:>8.1f}%")
    print(f"  Best Period:         {r['best_period'] * 100:>+8.2f}%")
    print(f"  Worst Period:        {r['worst_period'] * 100:>+8.2f}%")

    if args.benchmark:
        bench = [float(x.strip()) for x in args.benchmark.split(",")]
        br = benchmark_relative(returns, bench, args.freq)
        print(f"{'─' * 50}")
        print(f"  Active Return:       {br['active_return'] * 100:>+8.2f}%")
        print(f"  Tracking Error:      {br['tracking_error'] * 100:>8.2f}%")
        print(f"  Information Ratio:   {br['information_ratio']:>8.2f}")

    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
