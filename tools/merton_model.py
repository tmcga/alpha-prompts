#!/usr/bin/env python3
"""Merton structural credit model — default probability and credit spreads.

Usage:
    python merton_model.py --assets 1000 --debt 600 --vol 0.25 --rate 0.04 --maturity 5
"""

import argparse
import math


def norm_cdf(x: float) -> float:
    """Standard normal CDF."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def norm_pdf(x: float) -> float:
    """Standard normal PDF."""
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def merton_model(asset_value: float, debt_face: float, asset_vol: float, risk_free: float, maturity: float) -> dict:
    """Calculate Merton structural credit model outputs.

    The Merton model treats equity as a European call option on the firm's
    assets with strike equal to debt face value.

    Args:
        asset_value: Current market value of firm assets.
        debt_face: Face value of debt (default barrier).
        asset_vol: Annualized asset volatility.
        risk_free: Risk-free rate.
        maturity: Time to debt maturity (years).

    Returns:
        Dict with distance to default, default probability, equity value,
        credit spread, and risk metrics.
    """
    if maturity <= 0:
        raise ValueError("Maturity must be positive")

    sqrt_t = math.sqrt(maturity)

    # Distance to default
    d1 = (math.log(asset_value / debt_face) + (risk_free + 0.5 * asset_vol**2) * maturity) / (asset_vol * sqrt_t)
    d2 = d1 - asset_vol * sqrt_t

    # Default probability (risk-neutral)
    default_prob = norm_cdf(-d2)

    # Physical (real-world) DD — often reported without drift adjustment
    distance_to_default = d2

    # Equity value = Call option on assets
    equity_value = asset_value * norm_cdf(d1) - debt_face * math.exp(-risk_free * maturity) * norm_cdf(d2)

    # Debt value = Assets - Equity
    debt_value = asset_value - equity_value

    # Credit spread
    risky_yield = -math.log(debt_value / debt_face) / maturity if debt_value > 0 else float("inf")
    credit_spread = risky_yield - risk_free

    # Equity delta (sensitivity of equity to asset value changes)
    equity_delta = norm_cdf(d1)

    # Equity volatility (from asset vol via leverage)
    leverage_ratio = asset_value / equity_value if equity_value > 0 else float("inf")
    equity_vol = asset_vol * equity_delta * leverage_ratio

    # Debt delta
    debt_delta = 1 - equity_delta

    # Expected loss given default (LGD proxy)
    pv_debt = debt_face * math.exp(-risk_free * maturity)
    expected_loss = pv_debt - debt_value
    lgd_proxy = expected_loss / pv_debt if pv_debt > 0 else 0

    return {
        "d1": d1,
        "d2": d2,
        "distance_to_default": distance_to_default,
        "default_probability": default_prob,
        "equity_value": equity_value,
        "debt_value": debt_value,
        "credit_spread": credit_spread,
        "credit_spread_bps": credit_spread * 10000,
        "risky_yield": risky_yield,
        "equity_delta": equity_delta,
        "equity_vol": equity_vol,
        "debt_delta": debt_delta,
        "leverage_ratio": leverage_ratio,
        "expected_loss": expected_loss,
        "lgd_proxy": lgd_proxy,
    }


def main():
    parser = argparse.ArgumentParser(description="Merton Structural Credit Model")
    parser.add_argument("--assets", type=float, required=True, help="Asset value")
    parser.add_argument("--debt", type=float, required=True, help="Debt face value")
    parser.add_argument("--vol", type=float, required=True, help="Asset volatility")
    parser.add_argument("--rate", type=float, default=0.04, help="Risk-free rate (default: 0.04)")
    parser.add_argument("--maturity", type=float, default=5, help="Debt maturity in years (default: 5)")
    args = parser.parse_args()

    r = merton_model(args.assets, args.debt, args.vol, args.rate, args.maturity)

    print(f"\n{'=' * 50}")
    print("  Merton Credit Model")
    print(f"{'=' * 50}")
    print(f"  Asset Value:       ${args.assets:>10,.1f}")
    print(f"  Debt Face Value:   ${args.debt:>10,.1f}")
    print(f"  Asset Volatility:  {args.vol * 100:>10.1f}%")
    print(f"  Risk-Free Rate:    {args.rate * 100:>10.2f}%")
    print(f"  Maturity:          {args.maturity:>10.1f} years")
    print(f"{'─' * 50}")
    print(f"  Distance to Default: {r['distance_to_default']:>8.3f}")
    print(f"  Default Probability: {r['default_probability'] * 100:>8.2f}%")
    print(f"{'─' * 50}")
    print(f"  Equity Value:      ${r['equity_value']:>10,.1f}")
    print(f"  Debt Value:        ${r['debt_value']:>10,.1f}")
    print(f"  Leverage (A/E):    {r['leverage_ratio']:>10.2f}x")
    print(f"{'─' * 50}")
    print(f"  Credit Spread:     {r['credit_spread_bps']:>10.1f} bps")
    print(f"  Risky Yield:       {r['risky_yield'] * 100:>10.2f}%")
    print(f"  Expected Loss:     ${r['expected_loss']:>10,.1f}")
    print(f"  LGD (proxy):       {r['lgd_proxy'] * 100:>10.1f}%")
    print(f"{'─' * 50}")
    print(f"  Equity Delta:      {r['equity_delta']:>10.4f}")
    print(f"  Equity Volatility: {r['equity_vol'] * 100:>10.1f}%")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
