#!/usr/bin/env python3
"""Monte Carlo simulation — portfolio growth, retirement planning, VaR.

Usage:
    python monte_carlo.py --initial 1000000 --return 0.07 --vol 0.15 --years 30 --sims 10000
    python monte_carlo.py --initial 2000000 --return 0.06 --vol 0.12 --years 30 --withdrawal 0.04 --goal 500000
"""

import argparse
import math
import random


def monte_carlo_sim(
    initial: float,
    expected_return: float,
    volatility: float,
    years: int,
    num_sims: int = 10000,
    withdrawal_rate: float = 0.0,
    contribution: float = 0.0,
    goal: float = 0.0,
    seed: int | None = None,
) -> dict:
    """Run Monte Carlo simulation with geometric Brownian motion paths.

    Args:
        initial: Starting portfolio value.
        expected_return: Expected annual return (arithmetic).
        volatility: Annual volatility (std dev of returns).
        years: Investment horizon.
        num_sims: Number of simulation paths.
        withdrawal_rate: Annual withdrawal as fraction of initial (inflation-adjusted).
        contribution: Annual contribution amount.
        goal: Target ending value (for success probability).
        seed: Random seed for reproducibility.

    Returns:
        Dict with percentile outcomes, success probability, and statistics.
    """
    if seed is not None:
        random.seed(seed)

    # Drift adjusted for geometric returns: mu - 0.5*sigma^2
    drift = expected_return - 0.5 * volatility**2
    annual_withdrawal = initial * withdrawal_rate

    terminal_values = []
    worst_path_min = initial
    ruin_count = 0

    for _ in range(num_sims):
        value = initial
        path_min = initial
        ruined = False

        for yr in range(years):
            z = random.gauss(0, 1)
            annual_return = math.exp(drift + volatility * z)
            value *= annual_return
            value += contribution
            value -= annual_withdrawal

            if value <= 0:
                value = 0
                ruined = True
                break

            path_min = min(path_min, value)

        terminal_values.append(value)
        worst_path_min = min(worst_path_min, path_min)
        if ruined:
            ruin_count += 1

    # Sort for percentile extraction
    terminal_values.sort()
    n = len(terminal_values)

    def percentile(pct):
        idx = max(0, min(n - 1, int(n * pct / 100)))
        return terminal_values[idx]

    # Statistics
    mean_terminal = sum(terminal_values) / n

    # Success probability
    if goal > 0:
        successes = sum(1 for v in terminal_values if v >= goal)
        success_prob = successes / n
    else:
        success_prob = None

    worst_dd = (worst_path_min - initial) / initial if initial > 0 else 0

    # Parametric VaR from terminal distribution
    var_5 = percentile(5)
    var_1 = percentile(1)

    return {
        "initial_value": initial,
        "years": years,
        "num_simulations": num_sims,
        "mean_terminal": mean_terminal,
        "percentile_1": var_1,
        "percentile_5": var_5,
        "percentile_10": percentile(10),
        "percentile_25": percentile(25),
        "percentile_50": percentile(50),
        "percentile_75": percentile(75),
        "percentile_90": percentile(90),
        "percentile_95": percentile(95),
        "percentile_99": percentile(99),
        "success_probability": success_prob,
        "ruin_probability": ruin_count / n,
        "worst_case": terminal_values[0],
        "best_case": terminal_values[-1],
        "worst_path_drawdown": worst_dd,
    }


def main():
    parser = argparse.ArgumentParser(description="Monte Carlo Portfolio Simulation")
    parser.add_argument("--initial", type=float, required=True, help="Initial portfolio value")
    parser.add_argument("--return", dest="exp_return", type=float, required=True, help="Expected annual return")
    parser.add_argument("--vol", type=float, required=True, help="Annual volatility")
    parser.add_argument("--years", type=int, required=True, help="Investment horizon")
    parser.add_argument("--sims", type=int, default=10000, help="Number of simulations (default: 10000)")
    parser.add_argument("--withdrawal", type=float, default=0.0, help="Annual withdrawal rate (default: 0)")
    parser.add_argument("--contribution", type=float, default=0.0, help="Annual contribution (default: 0)")
    parser.add_argument("--goal", type=float, default=0.0, help="Target ending value")
    parser.add_argument("--seed", type=int, default=None, help="Random seed")
    args = parser.parse_args()

    r = monte_carlo_sim(
        args.initial,
        args.exp_return,
        args.vol,
        args.years,
        args.sims,
        args.withdrawal,
        args.contribution,
        args.goal,
        args.seed,
    )

    print(f"\n{'=' * 50}")
    print(f"  Monte Carlo Simulation ({r['num_simulations']:,} paths)")
    print(f"{'=' * 50}")
    print(f"  Initial Value:     ${r['initial_value']:>12,.0f}")
    print(f"  Expected Return:   {args.exp_return * 100:>12.1f}%")
    print(f"  Volatility:        {args.vol * 100:>12.1f}%")
    print(f"  Horizon:           {r['years']:>12d} years")
    if args.withdrawal > 0:
        print(f"  Withdrawal Rate:   {args.withdrawal * 100:>12.1f}%")
    if args.contribution > 0:
        print(f"  Annual Contrib:    ${args.contribution:>12,.0f}")
    print(f"{'─' * 50}")
    print("  Terminal Value Distribution:")
    print(f"    1st Percentile:  ${r['percentile_1']:>12,.0f}")
    print(f"    5th Percentile:  ${r['percentile_5']:>12,.0f}")
    print(f"   10th Percentile:  ${r['percentile_10']:>12,.0f}")
    print(f"   25th Percentile:  ${r['percentile_25']:>12,.0f}")
    print(f"   50th (Median):    ${r['percentile_50']:>12,.0f}")
    print(f"   75th Percentile:  ${r['percentile_75']:>12,.0f}")
    print(f"   90th Percentile:  ${r['percentile_90']:>12,.0f}")
    print(f"   95th Percentile:  ${r['percentile_95']:>12,.0f}")
    print(f"   99th Percentile:  ${r['percentile_99']:>12,.0f}")
    print(f"{'─' * 50}")
    print(f"  Mean Terminal:     ${r['mean_terminal']:>12,.0f}")
    print(f"  Best Case:         ${r['best_case']:>12,.0f}")
    print(f"  Worst Case:        ${r['worst_case']:>12,.0f}")
    print(f"{'─' * 50}")
    if r["success_probability"] is not None:
        print(f"  Goal (${args.goal:,.0f}):")
        print(f"    Success Prob:    {r['success_probability'] * 100:>12.1f}%")
    print(f"  Ruin Probability:  {r['ruin_probability'] * 100:>12.1f}%")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
