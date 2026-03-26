#!/usr/bin/env python3
"""Convertible bond pricer — bond floor, parity, embedded option value.

Usage:
    python convertible.py --face 1000 --coupon 0.02 --maturity 5 --spread 0.03 --stock 50 --ratio 15 --vol 0.30 --rate 0.04
"""

import argparse
import math


def norm_cdf(x: float) -> float:
    """Standard normal CDF."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def convertible_bond(
    face: float,
    coupon_rate: float,
    maturity: float,
    credit_spread: float,
    stock_price: float,
    conversion_ratio: float,
    stock_vol: float,
    risk_free: float,
) -> dict:
    """Price a convertible bond as bond floor + embedded call option.

    Args:
        face: Face/par value.
        coupon_rate: Annual coupon rate.
        maturity: Years to maturity.
        credit_spread: Credit spread over risk-free (for bond floor discounting).
        stock_price: Current underlying stock price.
        conversion_ratio: Number of shares per bond.
        stock_vol: Stock volatility (annualized).
        risk_free: Risk-free rate.

    Returns:
        Dict with bond floor, parity, theoretical value, conversion premium, and Greeks.
    """
    discount_rate = risk_free + credit_spread
    coupon = face * coupon_rate

    # Bond floor (straight bond value)
    bond_floor = 0
    for t in range(1, int(maturity) + 1):
        cf = coupon if t < int(maturity) else coupon + face
        bond_floor += cf / (1 + discount_rate) ** t

    # Conversion value (parity)
    parity = stock_price * conversion_ratio

    # Embedded option: Black-Scholes call on conversion_ratio shares
    # Strike = face value (bondholder gives up face to convert)
    effective_strike = face / conversion_ratio  # per-share conversion price
    if maturity > 0 and stock_vol > 0:
        d1 = (math.log(stock_price / effective_strike) + (risk_free + 0.5 * stock_vol**2) * maturity) / (
            stock_vol * math.sqrt(maturity)
        )
        d2 = d1 - stock_vol * math.sqrt(maturity)
        call_per_share = stock_price * norm_cdf(d1) - effective_strike * math.exp(-risk_free * maturity) * norm_cdf(d2)
        option_delta = norm_cdf(d1)
    else:
        call_per_share = max(stock_price - effective_strike, 0)
        option_delta = 1.0 if stock_price > effective_strike else 0.0

    embedded_option_value = call_per_share * conversion_ratio

    # Theoretical convertible value
    theoretical_value = bond_floor + embedded_option_value

    # Conversion premium
    conversion_premium = (theoretical_value - parity) / parity if parity > 0 else 0

    # Breakeven: years to recoup premium via coupon advantage
    # (Assumes stock pays no dividend)
    income_advantage = coupon  # convertible coupon - stock dividend (assumed 0)
    premium_dollars = theoretical_value - parity
    breakeven_years = premium_dollars / income_advantage if income_advantage > 0 else float("inf")

    # Profile classification
    bond_pct = bond_floor / theoretical_value * 100 if theoretical_value > 0 else 0
    equity_pct = embedded_option_value / theoretical_value * 100 if theoretical_value > 0 else 0

    if parity > bond_floor * 1.3:
        profile = "Equity-like"
    elif parity < bond_floor * 0.8:
        profile = "Busted (bond-like)"
    else:
        profile = "Balanced"

    # Delta of the convertible (sensitivity to stock)
    convertible_delta = option_delta * conversion_ratio

    return {
        "bond_floor": bond_floor,
        "parity": parity,
        "embedded_option": embedded_option_value,
        "theoretical_value": theoretical_value,
        "conversion_premium": conversion_premium,
        "conversion_premium_dollars": premium_dollars,
        "breakeven_years": breakeven_years,
        "conversion_price": effective_strike,
        "profile": profile,
        "bond_component_pct": bond_pct,
        "equity_component_pct": equity_pct,
        "delta": convertible_delta,
        "delta_per_share": option_delta,
    }


def main():
    parser = argparse.ArgumentParser(description="Convertible Bond Pricer")
    parser.add_argument("--face", type=float, default=1000, help="Face value (default: 1000)")
    parser.add_argument("--coupon", type=float, required=True, help="Annual coupon rate")
    parser.add_argument("--maturity", type=float, required=True, help="Years to maturity")
    parser.add_argument("--spread", type=float, required=True, help="Credit spread")
    parser.add_argument("--stock", type=float, required=True, help="Stock price")
    parser.add_argument("--ratio", type=float, required=True, help="Conversion ratio (shares/bond)")
    parser.add_argument("--vol", type=float, required=True, help="Stock volatility")
    parser.add_argument("--rate", type=float, default=0.04, help="Risk-free rate (default: 0.04)")
    args = parser.parse_args()

    r = convertible_bond(
        args.face, args.coupon, args.maturity, args.spread, args.stock, args.ratio, args.vol, args.rate
    )

    print(f"\n{'=' * 50}")
    print("  Convertible Bond Analysis")
    print(f"{'=' * 50}")
    print(f"  Face Value:        ${args.face:>10,.2f}")
    print(f"  Coupon:            {args.coupon * 100:>10.2f}%")
    print(f"  Maturity:          {args.maturity:>10.1f} years")
    print(f"  Credit Spread:     {args.spread * 100:>10.2f}%")
    print(f"  Stock Price:       ${args.stock:>10.2f}")
    print(f"  Conversion Ratio:  {args.ratio:>10.1f}")
    print(f"  Conversion Price:  ${r['conversion_price']:>10.2f}")
    print(f"{'─' * 50}")
    print(f"  Bond Floor:        ${r['bond_floor']:>10.2f}  ({r['bond_component_pct']:.1f}%)")
    print(f"  Parity:            ${r['parity']:>10.2f}")
    print(f"  Embedded Option:   ${r['embedded_option']:>10.2f}  ({r['equity_component_pct']:.1f}%)")
    print(f"  Theoretical Value: ${r['theoretical_value']:>10.2f}")
    print(f"{'─' * 50}")
    print(f"  Conv Premium:      {r['conversion_premium'] * 100:>10.1f}%  (${r['conversion_premium_dollars']:.2f})")
    bev = f"{r['breakeven_years']:.1f}y" if r["breakeven_years"] < 100 else "N/A"
    print(f"  Breakeven:         {bev:>10}")
    print(f"  Profile:           {r['profile']:>10}")
    print(f"{'─' * 50}")
    print(f"  Delta (total):     {r['delta']:>10.2f}")
    print(f"  Delta (per share): {r['delta_per_share']:>10.4f}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
