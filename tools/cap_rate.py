#!/usr/bin/env python3
"""Real estate valuation — cap rate, NOI analysis, development spread.

Usage:
    python cap_rate.py --noi 5000000 --cap-rate 0.055 --rf 0.04 --growth 0.02
    python cap_rate.py --noi 5000000 --value 90000000
"""

import argparse


def real_estate_valuation(
    noi: float,
    cap_rate: float | None = None,
    property_value: float | None = None,
    risk_free: float = 0.04,
    noi_growth: float = 0.02,
    dev_cost: float | None = None,
) -> dict:
    """Calculate real estate valuation metrics.

    Args:
        noi: Annual Net Operating Income.
        cap_rate: Market cap rate (provide to solve for value).
        property_value: Property value (provide to solve for cap rate).
        risk_free: Risk-free rate for cap rate decomposition.
        noi_growth: Expected NOI growth rate.
        dev_cost: Total development cost (for development spread).

    Returns:
        Dict with property value, cap rate decomposition, and sensitivity.
    """
    # Solve for unknowns
    if cap_rate is not None and property_value is None:
        property_value = noi / cap_rate if cap_rate > 0 else 0
    elif property_value is not None and cap_rate is None:
        cap_rate = noi / property_value if property_value > 0 else 0
    elif cap_rate is not None and property_value is not None:
        pass  # both given, use as-is
    else:
        raise ValueError("Provide either --cap-rate or --value")

    # Cap rate decomposition: cap rate = risk-free + risk premium - growth
    risk_premium = cap_rate - risk_free + noi_growth

    # Value per unit of NOI (inverse of cap rate)
    noi_multiple = 1 / cap_rate if cap_rate > 0 else 0

    # Sensitivity: value impact of 25bps cap rate change
    sensitivity = {}
    for delta_bps in [-100, -50, -25, 25, 50, 100]:
        adj_cap = cap_rate + delta_bps / 10000
        if adj_cap > 0:
            adj_value = noi / adj_cap
            sensitivity[delta_bps] = {
                "cap_rate": adj_cap,
                "value": adj_value,
                "change": adj_value - property_value,
                "change_pct": (adj_value - property_value) / property_value * 100,
            }

    # Development spread
    dev_spread = None
    yield_on_cost = None
    if dev_cost is not None and dev_cost > 0:
        yield_on_cost = noi / dev_cost
        dev_spread = yield_on_cost - cap_rate

    # Gross rent multiplier proxy (assume NOI = 65% of gross rent)
    gross_rent_est = noi / 0.65
    grm = property_value / gross_rent_est if gross_rent_est > 0 else 0

    return {
        "noi": noi,
        "cap_rate": cap_rate,
        "property_value": property_value,
        "noi_multiple": noi_multiple,
        "risk_premium": risk_premium,
        "cap_rate_decomposition": {
            "risk_free": risk_free,
            "risk_premium": risk_premium,
            "growth_deduction": -noi_growth,
        },
        "yield_on_cost": yield_on_cost,
        "development_spread": dev_spread,
        "grm_estimate": grm,
        "sensitivity": sensitivity,
    }


def main():
    parser = argparse.ArgumentParser(description="Real Estate Valuation (Cap Rate)")
    parser.add_argument("--noi", type=float, required=True, help="Net Operating Income")
    parser.add_argument("--cap-rate", type=float, default=None, help="Cap rate (solves for value)")
    parser.add_argument("--value", type=float, default=None, help="Property value (solves for cap rate)")
    parser.add_argument("--rf", type=float, default=0.04, help="Risk-free rate (default: 0.04)")
    parser.add_argument("--growth", type=float, default=0.02, help="NOI growth rate (default: 0.02)")
    parser.add_argument("--dev-cost", type=float, default=None, help="Development cost (optional)")
    args = parser.parse_args()

    r = real_estate_valuation(args.noi, args.cap_rate, args.value, args.rf, args.growth, args.dev_cost)

    print(f"\n{'=' * 50}")
    print("  Real Estate Valuation")
    print(f"{'=' * 50}")
    print(f"  NOI:               ${r['noi']:>12,.0f}")
    print(f"  Cap Rate:          {r['cap_rate'] * 100:>12.2f}%")
    print(f"  Property Value:    ${r['property_value']:>12,.0f}")
    print(f"  NOI Multiple:      {r['noi_multiple']:>12.1f}x")
    print(f"{'─' * 50}")
    d = r["cap_rate_decomposition"]
    print("  Cap Rate Build-Up:")
    print(f"    Risk-Free Rate:  {d['risk_free'] * 100:>12.2f}%")
    print(f"    Risk Premium:    {d['risk_premium'] * 100:>12.2f}%")
    print(f"    Less: Growth:    {d['growth_deduction'] * 100:>12.2f}%")
    print(f"    = Cap Rate:      {r['cap_rate'] * 100:>12.2f}%")
    if r["yield_on_cost"] is not None:
        print(f"{'─' * 50}")
        print("  Development Analysis:")
        print(f"    Dev Cost:        ${args.dev_cost:>12,.0f}")
        print(f"    Yield on Cost:   {r['yield_on_cost'] * 100:>12.2f}%")
        print(f"    Dev Spread:      {r['development_spread'] * 100:>+12.2f}%")
    print(f"{'─' * 50}")
    print("  Cap Rate Sensitivity:")
    for delta, s in r["sensitivity"].items():
        print(f"    {delta:>+4d}bps ({s['cap_rate'] * 100:.2f}%): ${s['value']:>12,.0f}  ({s['change_pct']:>+.1f}%)")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
