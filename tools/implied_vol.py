#!/usr/bin/env python3
"""Implied volatility solver — extract IV from market option prices.

Usage:
    python implied_vol.py --price 5.50 --spot 100 --strike 105 --time 0.5 --rate 0.05 --type call
"""

import argparse
import math


def norm_cdf(x: float) -> float:
    """Standard normal CDF."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs_price(spot: float, strike: float, time: float, rate: float, vol: float, option_type: str) -> float:
    """Black-Scholes theoretical price."""
    if time <= 0 or vol <= 0:
        if option_type == "call":
            return max(spot - strike * math.exp(-rate * time), 0)
        return max(strike * math.exp(-rate * time) - spot, 0)

    d1 = (math.log(spot / strike) + (rate + 0.5 * vol**2) * time) / (vol * math.sqrt(time))
    d2 = d1 - vol * math.sqrt(time)

    if option_type == "call":
        return spot * norm_cdf(d1) - strike * math.exp(-rate * time) * norm_cdf(d2)
    return strike * math.exp(-rate * time) * norm_cdf(-d2) - spot * norm_cdf(-d1)


def implied_volatility(
    market_price: float,
    spot: float,
    strike: float,
    time: float,
    rate: float,
    option_type: str = "call",
    tol: float = 1e-8,
    max_iter: int = 200,
) -> dict:
    """Solve for implied volatility using bisection method.

    Args:
        market_price: Observed option price.
        spot: Current underlying price.
        strike: Strike price.
        time: Time to expiration (years).
        rate: Risk-free rate.
        option_type: "call" or "put".

    Returns:
        Dict with implied vol, moneyness, intrinsic/time value.
    """
    option_type = option_type.lower()
    # Intrinsic value
    if option_type == "call":
        intrinsic = max(spot - strike * math.exp(-rate * time), 0)
    else:
        intrinsic = max(strike * math.exp(-rate * time) - spot, 0)

    time_value = market_price - intrinsic
    moneyness = spot / strike

    # Bisection search
    vol_low = 0.001
    vol_high = 5.0
    iv = None

    for _ in range(max_iter):
        vol_mid = (vol_low + vol_high) / 2
        price_mid = bs_price(spot, strike, time, rate, vol_mid, option_type)
        diff = price_mid - market_price

        if abs(diff) < tol:
            iv = vol_mid
            break

        if diff > 0:
            vol_high = vol_mid
        else:
            vol_low = vol_mid

    if iv is None:
        iv = (vol_low + vol_high) / 2

    # Verify the solution
    fitted_price = bs_price(spot, strike, time, rate, iv, option_type)

    return {
        "implied_vol": iv,
        "market_price": market_price,
        "model_price": fitted_price,
        "pricing_error": abs(fitted_price - market_price),
        "moneyness": moneyness,
        "intrinsic_value": intrinsic,
        "time_value": time_value,
        "spot": spot,
        "strike": strike,
        "time_to_expiry": time,
    }


def main():
    parser = argparse.ArgumentParser(description="Implied Volatility Solver")
    parser.add_argument("--price", type=float, required=True, help="Market option price")
    parser.add_argument("--spot", type=float, required=True, help="Spot price")
    parser.add_argument("--strike", type=float, required=True, help="Strike price")
    parser.add_argument("--time", type=float, required=True, help="Time to expiry (years)")
    parser.add_argument("--rate", type=float, default=0.05, help="Risk-free rate (default: 0.05)")
    parser.add_argument("--type", dest="option_type", default="call", choices=["call", "put"])
    args = parser.parse_args()

    r = implied_volatility(args.price, args.spot, args.strike, args.time, args.rate, args.option_type)

    print(f"\n{'=' * 50}")
    print(f"  Implied Volatility: {args.option_type.upper()}")
    print(f"{'=' * 50}")
    print(f"  Spot:            ${args.spot:>10.2f}")
    print(f"  Strike:          ${args.strike:>10.2f}")
    print(f"  Time:            {args.time:>10.4f}y")
    print(f"  Market Price:    ${r['market_price']:>10.4f}")
    print(f"{'─' * 50}")
    print(f"  Implied Vol:     {r['implied_vol'] * 100:>10.2f}%")
    print(f"  Model Price:     ${r['model_price']:>10.4f}")
    print(f"  Pricing Error:   ${r['pricing_error']:>10.6f}")
    print(f"{'─' * 50}")
    print(f"  Moneyness (S/K): {r['moneyness']:>10.4f}")
    print(f"  Intrinsic Value: ${r['intrinsic_value']:>10.4f}")
    print(f"  Time Value:      ${r['time_value']:>10.4f}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
