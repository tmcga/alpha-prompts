#!/usr/bin/env python3
"""Black-Scholes options pricing calculator with full Greeks.

Usage:
    python black_scholes.py --spot 100 --strike 105 --time 0.5 --rate 0.05 --vol 0.2 --type call
    python black_scholes.py --spot 100 --strike 105 --time 0.5 --rate 0.05 --vol 0.2 --div 0.02 --type call
"""

import argparse
import math


def norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def norm_pdf(x: float) -> float:
    """Standard normal probability density function."""
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def black_scholes(
    spot: float, strike: float, time: float, rate: float, vol: float, option_type: str = "call", div_yield: float = 0.0
) -> dict:
    """Calculate Black-Scholes price and Greeks.

    Args:
        spot: Current price of the underlying.
        strike: Strike price.
        time: Time to expiration in years.
        rate: Risk-free interest rate.
        vol: Annualized volatility.
        option_type: "call" or "put".
        div_yield: Continuous dividend yield.

    Returns:
        Dict with price, delta, gamma, vega, theta, rho, vanna, charm.
    """
    option_type = option_type.lower()
    if time <= 0:
        if option_type == "call":
            intrinsic = max(spot - strike, 0)
        else:
            intrinsic = max(strike - spot, 0)
        return {"price": intrinsic, "delta": 0, "gamma": 0, "vega": 0, "theta": 0, "rho": 0, "vanna": 0, "charm": 0}

    # Adjusted spot for continuous dividends
    s_adj = spot * math.exp(-div_yield * time)
    sqrt_t = math.sqrt(time)

    d1 = (math.log(s_adj / strike) + (rate + 0.5 * vol**2) * time) / (vol * sqrt_t)
    d2 = d1 - vol * sqrt_t

    df = math.exp(-rate * time)
    qf = math.exp(-div_yield * time)

    if option_type == "call":
        price = s_adj * norm_cdf(d1) - strike * df * norm_cdf(d2)
        delta = qf * norm_cdf(d1)
        rho = strike * time * df * norm_cdf(d2) / 100
    else:
        price = strike * df * norm_cdf(-d2) - s_adj * norm_cdf(-d1)
        delta = qf * (norm_cdf(d1) - 1)
        rho = -strike * time * df * norm_cdf(-d2) / 100

    gamma = qf * norm_pdf(d1) / (spot * vol * sqrt_t)
    vega = spot * qf * norm_pdf(d1) * sqrt_t / 100
    theta = (
        -(spot * qf * norm_pdf(d1) * vol) / (2 * sqrt_t)
        + div_yield * spot * qf * norm_cdf(d1 if option_type == "call" else -d1) * (1 if option_type == "call" else -1)
        - rate * strike * df * norm_cdf(d2 if option_type == "call" else -d2) * (1 if option_type == "call" else -1)
    ) / 365

    # Higher-order Greeks
    vanna = -qf * norm_pdf(d1) * d2 / vol  # dDelta/dVol
    charm = (
        -qf
        * norm_pdf(d1)
        * (d2 * (2 * (rate - div_yield) * time - d2 * vol * sqrt_t) / (2 * time * vol * sqrt_t))
        / 365
    )  # dDelta/dTime per day

    # Put-call parity check
    call_price = s_adj * norm_cdf(d1) - strike * df * norm_cdf(d2)
    put_price = strike * df * norm_cdf(-d2) - s_adj * norm_cdf(-d1)
    parity_lhs = call_price - put_price
    parity_rhs = s_adj - strike * df

    return {
        "price": price,
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho,
        "vanna": vanna,
        "charm": charm,
        "d1": d1,
        "d2": d2,
        "put_call_parity_check": abs(parity_lhs - parity_rhs) < 1e-10,
    }


def main():
    parser = argparse.ArgumentParser(description="Black-Scholes Options Pricer")
    parser.add_argument("--spot", type=float, required=True, help="Spot price")
    parser.add_argument("--strike", type=float, required=True, help="Strike price")
    parser.add_argument("--time", type=float, required=True, help="Time to expiry (years)")
    parser.add_argument("--rate", type=float, default=0.05, help="Risk-free rate (default: 0.05)")
    parser.add_argument("--vol", type=float, required=True, help="Volatility (e.g., 0.20)")
    parser.add_argument("--type", dest="option_type", default="call", choices=["call", "put"])
    parser.add_argument("--div", type=float, default=0.0, help="Continuous dividend yield (default: 0)")
    args = parser.parse_args()

    r = black_scholes(args.spot, args.strike, args.time, args.rate, args.vol, args.option_type, args.div)

    print(f"\n{'=' * 50}")
    print(f"  Black-Scholes: {args.option_type.upper()}")
    print(f"{'=' * 50}")
    print(f"  Spot:    ${args.spot:>8.2f}    Strike: ${args.strike:>8.2f}")
    print(f"  Time:    {args.time:>8.4f}y   Vol:    {args.vol * 100:>8.1f}%")
    print(f"  Rate:    {args.rate * 100:>8.2f}%")
    print(f"{'─' * 50}")
    print(f"  Price:   ${r['price']:>8.4f}")
    print(f"  Delta:   {r['delta']:>+9.4f}")
    print(f"  Gamma:   {r['gamma']:>9.4f}")
    print(f"  Vega:    {r['vega']:>9.4f}   (per 1% vol)")
    print(f"  Theta:   {r['theta']:>9.4f}   (per day)")
    print(f"  Rho:     {r['rho']:>9.4f}   (per 1% rate)")
    print(f"  Vanna:   {r['vanna']:>9.4f}   (dDelta/dVol)")
    print(f"  Charm:   {r['charm']:>9.4f}   (dDelta/dT per day)")
    print(f"{'─' * 50}")
    print(f"  d1:      {r['d1']:>9.4f}")
    print(f"  d2:      {r['d2']:>9.4f}")
    print(f"  Put-Call Parity: {'OK' if r['put_call_parity_check'] else 'FAIL'}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
