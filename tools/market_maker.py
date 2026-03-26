#!/usr/bin/env python3
"""Avellaneda-Stoikov optimal market making — reservation price and optimal quotes.

Usage:
    python market_maker.py --mid 100 --inventory 50 --gamma 0.01 --vol 0.02 --time 0.5 --intensity 1.5
"""

import argparse
import math


def optimal_quotes(
    mid_price: float,
    inventory: int,
    risk_aversion: float,
    volatility: float,
    time_remaining: float,
    order_intensity: float,
) -> dict:
    """Calculate Avellaneda-Stoikov optimal market making quotes.

    The model computes an inventory-adjusted reservation price and optimal
    bid-ask spread that maximizes expected utility of terminal wealth.

    Args:
        mid_price: Current mid/fair price.
        inventory: Current inventory position (positive=long, negative=short).
        risk_aversion: Risk aversion parameter (gamma). Higher = tighter risk control.
        volatility: Price volatility (per unit time).
        time_remaining: Time remaining in trading session (0-1).
        order_intensity: Order arrival rate (kappa). Higher = more aggressive quoting.

    Returns:
        Dict with reservation price, optimal spread, bid/ask, and risk metrics.
    """
    sigma = volatility
    gamma = risk_aversion
    T = time_remaining
    q = inventory
    k = order_intensity

    # Reservation price: r(s, q, t) = s - q * gamma * sigma^2 * (T - t)
    # Inventory penalty pushes price away from fair value based on position
    inventory_penalty = q * gamma * sigma**2 * T
    reservation_price = mid_price - inventory_penalty

    # Optimal spread: delta = gamma * sigma^2 * T + (2/gamma) * ln(1 + gamma/k)
    spread_component_risk = gamma * sigma**2 * T
    spread_component_intensity = (2 / gamma) * math.log(1 + gamma / k)
    optimal_spread = spread_component_risk + spread_component_intensity

    # Optimal quotes
    bid_price = reservation_price - optimal_spread / 2
    ask_price = reservation_price + optimal_spread / 2

    # Bid-ask around mid
    bid_distance = mid_price - bid_price
    ask_distance = ask_price - mid_price

    # Inventory risk: q^2 * gamma * sigma^2 * T
    inventory_risk = q**2 * gamma * sigma**2 * T

    # Expected P&L per unit time (from spread capture)
    # Approximate: spread * order_intensity * exp(-k * spread/2) per side
    expected_fill_rate = k * math.exp(-k * optimal_spread / 2)
    expected_pnl_per_fill = optimal_spread / 2

    return {
        "mid_price": mid_price,
        "reservation_price": reservation_price,
        "inventory_adjustment": -inventory_penalty,
        "optimal_spread": optimal_spread,
        "optimal_spread_bps": optimal_spread / mid_price * 10000,
        "bid_price": bid_price,
        "ask_price": ask_price,
        "bid_distance": bid_distance,
        "ask_distance": ask_distance,
        "spread_risk_component": spread_component_risk,
        "spread_intensity_component": spread_component_intensity,
        "inventory": inventory,
        "inventory_risk": inventory_risk,
        "expected_fill_rate": expected_fill_rate,
        "expected_pnl_per_fill": expected_pnl_per_fill,
    }


def main():
    parser = argparse.ArgumentParser(description="Avellaneda-Stoikov Market Maker")
    parser.add_argument("--mid", type=float, required=True, help="Mid price")
    parser.add_argument("--inventory", type=int, default=0, help="Current inventory (default: 0)")
    parser.add_argument("--gamma", type=float, required=True, help="Risk aversion parameter")
    parser.add_argument("--vol", type=float, required=True, help="Price volatility")
    parser.add_argument("--time", type=float, default=1.0, help="Time remaining (default: 1.0)")
    parser.add_argument("--intensity", type=float, default=1.5, help="Order arrival intensity (default: 1.5)")
    args = parser.parse_args()

    r = optimal_quotes(args.mid, args.inventory, args.gamma, args.vol, args.time, args.intensity)

    print(f"\n{'=' * 50}")
    print("  Avellaneda-Stoikov Market Maker")
    print(f"{'=' * 50}")
    print(f"  Mid Price:         ${r['mid_price']:>10.4f}")
    print(f"  Inventory:         {r['inventory']:>+10d}")
    print(f"  Risk Aversion:     {args.gamma:>10.4f}")
    print(f"  Volatility:        {args.vol:>10.4f}")
    print(f"  Time Remaining:    {args.time:>10.4f}")
    print(f"{'─' * 50}")
    print(f"  Reservation Price: ${r['reservation_price']:>10.4f}")
    print(f"  Inventory Adj:     ${r['inventory_adjustment']:>+10.4f}")
    print(f"{'─' * 50}")
    print(f"  Optimal Spread:    ${r['optimal_spread']:>10.4f}  ({r['optimal_spread_bps']:.1f} bps)")
    print(f"    Risk Component:  ${r['spread_risk_component']:>10.4f}")
    print(f"    Intensity Comp:  ${r['spread_intensity_component']:>10.4f}")
    print(f"{'─' * 50}")
    print(f"  Bid Price:         ${r['bid_price']:>10.4f}  (-{r['bid_distance']:.4f} from mid)")
    print(f"  Ask Price:         ${r['ask_price']:>10.4f}  (+{r['ask_distance']:.4f} from mid)")
    print(f"{'─' * 50}")
    print(f"  Inventory Risk:    ${r['inventory_risk']:>10.4f}")
    print(f"  Exp Fill Rate:     {r['expected_fill_rate']:>10.4f}/unit time")
    print(f"  Exp P&L/Fill:      ${r['expected_pnl_per_fill']:>10.4f}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
