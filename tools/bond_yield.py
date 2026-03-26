#!/usr/bin/env python3
"""Bond yield calculator — YTM, duration, convexity, DV01.

Usage:
    python bond_yield.py --face 1000 --coupon 0.05 --price 980 --years 10 --freq 2
"""

import argparse


def bond_ytm(
    face: float, coupon_rate: float, price: float, years: float, freq: int = 2, tol: float = 1e-8, max_iter: int = 200
) -> float:
    """Calculate yield to maturity using Newton's method.

    Args:
        face: Face/par value.
        coupon_rate: Annual coupon rate.
        price: Current market price.
        years: Years to maturity.
        freq: Coupon payments per year.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.
    """
    coupon = face * coupon_rate / freq
    n = int(years * freq)
    ytm = coupon_rate  # initial guess

    for _ in range(max_iter):
        r = ytm / freq
        if abs(r) < 1e-12:
            pv = coupon * n + face
            dpv = -coupon * n * (n + 1) / (2 * freq) - face * n / freq
        else:
            discount = (1 + r) ** (-n)
            annuity = (1 - discount) / r
            pv = coupon * annuity + face * discount
            dpv = -coupon * (annuity / (1 + r) * n - (1 - discount) / r**2 * (1 / freq)) + face * (-n / freq) * (
                1 + r
            ) ** (-n - 1)

        diff = pv - price
        if abs(diff) < tol:
            return ytm, True
        if abs(dpv) < 1e-14:
            break
        ytm -= diff / dpv
        ytm = max(-0.99, min(ytm, 10.0))

    return ytm, False


def bond_analytics(
    face: float, coupon_rate: float, price: float, years: float, freq: int = 2, benchmark_yield: float = None
) -> dict:
    """Calculate full bond analytics.

    Returns:
        Dict with current yield, YTM, modified duration, Macaulay duration,
        convexity, DV01, and spread metrics.
    """
    coupon = face * coupon_rate / freq
    n = int(years * freq)

    # Current yield
    annual_coupon = face * coupon_rate
    current_yield = annual_coupon / price if price else 0

    # YTM
    ytm, ytm_converged = bond_ytm(face, coupon_rate, price, years, freq)
    r = ytm / freq

    # Cash flows and Macaulay duration
    mac_duration = 0
    convexity = 0
    pv_total = 0

    for t in range(1, n + 1):
        cf = coupon if t < n else coupon + face
        period_years = t / freq
        discount = (1 + r) ** (-t)
        pv_cf = cf * discount
        pv_total += pv_cf
        mac_duration += period_years * pv_cf
        convexity += t * (t + 1) * pv_cf

    mac_duration /= pv_total if pv_total else 1
    convexity /= (pv_total * (1 + r) ** 2 * freq**2) if pv_total else 1

    # Modified duration
    mod_duration = mac_duration / (1 + r)

    # DV01 (dollar value of a basis point)
    dv01 = mod_duration * price / 10000

    # Spread metrics
    g_spread = ytm - benchmark_yield if benchmark_yield is not None else None

    # Z-spread approximation (constant spread over flat benchmark curve)
    z_spread = None
    if benchmark_yield is not None:
        zs_low, zs_high = 0.0, 0.50
        z_spread_converged = False
        for _ in range(200):
            zs_mid = (zs_low + zs_high) / 2
            pv = 0
            for t in range(1, n + 1):
                cf = coupon if t < n else coupon + face
                pv += cf / (1 + (benchmark_yield + zs_mid) / freq) ** t
            if abs(pv - price) < 1e-8:
                z_spread_converged = True
                break
            if pv > price:
                zs_low = zs_mid
            else:
                zs_high = zs_mid
        z_spread = (zs_low + zs_high) / 2

    return {
        "current_yield": current_yield,
        "ytm": ytm,
        "ytm_converged": ytm_converged,
        "macaulay_duration": mac_duration,
        "modified_duration": mod_duration,
        "convexity": convexity,
        "dv01": dv01,
        "periods": n,
        "g_spread": g_spread,
        "z_spread": z_spread,
        "z_spread_converged": z_spread_converged if benchmark_yield is not None else None,
    }


def main():
    parser = argparse.ArgumentParser(description="Bond Yield Calculator")
    parser.add_argument("--face", type=float, default=1000, help="Face value (default: 1000)")
    parser.add_argument("--coupon", type=float, required=True, help="Annual coupon rate")
    parser.add_argument("--price", type=float, required=True, help="Market price")
    parser.add_argument("--years", type=float, required=True, help="Years to maturity")
    parser.add_argument("--freq", type=int, default=2, help="Coupons per year (default: 2)")
    parser.add_argument("--benchmark-yield", type=float, default=None, help="Benchmark yield for spread calc")
    args = parser.parse_args()

    r = bond_analytics(args.face, args.coupon, args.price, args.years, args.freq, args.benchmark_yield)

    print(f"\n{'=' * 50}")
    print("  Bond Analytics")
    print(f"{'=' * 50}")
    print(f"  Face Value:      ${args.face:>10,.2f}")
    print(f"  Coupon Rate:     {args.coupon * 100:>10.3f}%")
    print(f"  Market Price:    ${args.price:>10,.2f}")
    print(f"  Maturity:        {args.years:>10.1f} years ({r['periods']} periods)")
    print(f"{'─' * 50}")
    print(f"  Current Yield:   {r['current_yield'] * 100:>10.3f}%")
    print(f"  YTM:             {r['ytm'] * 100:>10.3f}%")
    print(f"  Macaulay Dur:    {r['macaulay_duration']:>10.3f} years")
    print(f"  Modified Dur:    {r['modified_duration']:>10.3f}")
    print(f"  Convexity:       {r['convexity']:>10.3f}")
    print(f"  DV01:            ${r['dv01']:>10.4f}")
    if r["g_spread"] is not None:
        print(f"{'─' * 50}")
        print(f"  G-Spread:        {r['g_spread'] * 10000:>10.1f} bps")
        print(f"  Z-Spread:        {r['z_spread'] * 10000:>10.1f} bps")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
