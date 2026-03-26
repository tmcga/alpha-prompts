#!/usr/bin/env python3
"""Kelly Criterion position sizer — optimal bet sizing for edge-based strategies.

Usage:
    python kelly.py --win-prob 0.55 --win-loss-ratio 1.5
    python kelly.py --win-prob 0.60 --win-loss-ratio 2.0 --fraction 0.5
    python kelly.py --outcomes "0.40:2.0,0.35:0.5,0.25:-1.0"
"""
import argparse
import math


def kelly_criterion(win_prob: float, win_loss_ratio: float,
                    fraction: float = 1.0) -> dict:
    """Calculate Kelly fraction for binary outcome bets.

    Args:
        win_prob: Probability of winning (0-1).
        win_loss_ratio: Ratio of average win to average loss.
        fraction: Kelly fraction to apply (0.25=quarter, 0.5=half, 1.0=full).

    Returns:
        Dict with optimal fraction, expected growth, and risk metrics.
    """
    lose_prob = 1 - win_prob
    if win_loss_ratio <= 0:
        raise ValueError("Win/loss ratio must be positive")

    # Full Kelly: f* = p - q/b  (where b = win/loss ratio)
    full_kelly = win_prob - lose_prob / win_loss_ratio
    optimal_fraction = full_kelly * fraction

    # Edge and odds
    edge = win_prob * win_loss_ratio - lose_prob
    expected_return = edge  # per unit bet

    # Expected geometric growth rate: g = p*ln(1 + f*b) + q*ln(1 - f)
    f = max(0, min(optimal_fraction, 0.999))
    if f > 0:
        geo_growth = win_prob * math.log(1 + f * win_loss_ratio) + lose_prob * math.log(1 - f)
    else:
        geo_growth = 0

    # Probability of drawdown: P(drawdown >= d) = d^(1/f - 1) for full Kelly
    # Ruin probability approximation at full Kelly
    if full_kelly > 0 and full_kelly < 1:
        prob_50_dd = 0.5 ** (1 / full_kelly - 1) if full_kelly < 1 else 1.0
        prob_75_dd = 0.75 ** (1 / full_kelly - 1) if full_kelly < 1 else 1.0
    else:
        prob_50_dd = 1.0
        prob_75_dd = 1.0

    return {
        "full_kelly": full_kelly,
        "applied_fraction": optimal_fraction,
        "kelly_multiplier": fraction,
        "edge": edge,
        "expected_return_per_bet": expected_return,
        "geometric_growth_rate": geo_growth,
        "win_probability": win_prob,
        "win_loss_ratio": win_loss_ratio,
        "prob_50pct_drawdown": prob_50_dd,
        "prob_75pct_drawdown": prob_75_dd,
    }


def multi_outcome_kelly(outcomes: list[tuple[float, float]]) -> dict:
    """Kelly for multiple discrete outcomes.

    Args:
        outcomes: List of (probability, payoff_multiple) tuples.
                  Payoff is per $1 bet: 2.0 means you get $2 back on $1.
                  -1.0 means total loss.

    Returns:
        Dict with optimal fraction found via grid search.
    """
    total_prob = sum(p for p, _ in outcomes)
    if abs(total_prob - 1.0) > 0.01:
        raise ValueError(f"Probabilities must sum to 1.0 (got {total_prob:.3f})")

    expected_value = sum(p * payoff for p, payoff in outcomes)

    # Grid search for optimal f (maximizes geometric growth)
    best_f = 0.0
    best_growth = 0.0
    for i in range(1, 1000):
        f = i / 1000.0
        growth = 0.0
        valid = True
        for prob, payoff in outcomes:
            val = 1 + f * payoff
            if val <= 0:
                valid = False
                break
            growth += prob * math.log(val)
        if valid and growth > best_growth:
            best_growth = growth
            best_f = f

    return {
        "optimal_fraction": best_f,
        "geometric_growth_rate": best_growth,
        "expected_value_per_bet": expected_value,
        "num_outcomes": len(outcomes),
    }


def main():
    parser = argparse.ArgumentParser(description="Kelly Criterion Position Sizer")
    parser.add_argument("--win-prob", type=float, help="Win probability (0-1)")
    parser.add_argument("--win-loss-ratio", type=float, help="Avg win / avg loss")
    parser.add_argument("--fraction", type=float, default=1.0,
                        help="Kelly fraction: 0.25, 0.5, 1.0 (default: 1.0)")
    parser.add_argument("--outcomes", type=str, default=None,
                        help="Multi-outcome: 'prob1:payoff1,prob2:payoff2,...'")
    args = parser.parse_args()

    if args.outcomes:
        outcomes = []
        for pair in args.outcomes.split(","):
            prob, payoff = pair.strip().split(":")
            outcomes.append((float(prob), float(payoff)))
        r = multi_outcome_kelly(outcomes)

        print(f"\n{'='*50}")
        print(f"  Kelly Criterion: Multi-Outcome")
        print(f"{'='*50}")
        print(f"  Outcomes:")
        for i, (prob, payoff) in enumerate(outcomes, 1):
            print(f"    {i}. P={prob:.2f}  Payoff={payoff:+.2f}")
        print(f"{'─'*50}")
        print(f"  Expected Value/Bet: {r['expected_value_per_bet']:>+10.4f}")
        print(f"  Optimal Fraction:   {r['optimal_fraction']*100:>10.1f}%")
        print(f"  Geo Growth Rate:    {r['geometric_growth_rate']*100:>10.4f}%")
        print(f"{'='*50}\n")
    else:
        if args.win_prob is None or args.win_loss_ratio is None:
            parser.error("Provide --win-prob and --win-loss-ratio, or --outcomes")
        r = kelly_criterion(args.win_prob, args.win_loss_ratio, args.fraction)

        print(f"\n{'='*50}")
        print(f"  Kelly Criterion: Position Sizing")
        print(f"{'='*50}")
        print(f"  Win Probability:    {r['win_probability']*100:>10.1f}%")
        print(f"  Win/Loss Ratio:     {r['win_loss_ratio']:>10.2f}x")
        print(f"  Edge:               {r['edge']*100:>+10.2f}%")
        print(f"{'─'*50}")
        print(f"  Full Kelly:         {r['full_kelly']*100:>10.1f}%")
        frac_label = {0.25: "Quarter", 0.5: "Half", 1.0: "Full"}.get(
            r['kelly_multiplier'], f"{r['kelly_multiplier']:.0%}")
        print(f"  {frac_label} Kelly:  {r['applied_fraction']*100:>10.1f}%")
        print(f"  Exp Return/Bet:     {r['expected_return_per_bet']*100:>+10.2f}%")
        print(f"  Geo Growth Rate:    {r['geometric_growth_rate']*100:>10.4f}%")
        print(f"{'─'*50}")
        print(f"  Drawdown Risk (at full Kelly):")
        print(f"    P(50% drawdown):  {r['prob_50pct_drawdown']*100:>10.1f}%")
        print(f"    P(75% drawdown):  {r['prob_75pct_drawdown']*100:>10.1f}%")
        print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
