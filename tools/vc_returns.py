#!/usr/bin/env python3
"""Venture capital fund returns and dilution waterfall calculator.

Usage:
    python vc_returns.py --fund --contributions 10,10,10,5,5 --distributions 0,0,0,5,15 --nav 60 --years 5
    python vc_returns.py --dilution --rounds "5M@20M,10M@80M,25M@300M" --founder-shares 8000000
"""

import argparse


def fund_metrics(contributions: list[float], distributions: list[float], nav: float, years: float) -> dict:
    """Calculate VC fund performance metrics (TVPI, DPI, RVPI, IRR)."""
    total_contributed = sum(contributions)
    total_distributed = sum(distributions)

    tvpi = (total_distributed + nav) / total_contributed if total_contributed > 0 else 0
    dpi = total_distributed / total_contributed if total_contributed > 0 else 0
    rvpi = nav / total_contributed if total_contributed > 0 else 0

    # Net IRR via Newton's method on cash flows
    # Cash flows: negative contributions, positive distributions, +NAV at end
    n = len(contributions)
    cash_flows = []
    for i in range(n):
        cf = distributions[i] - contributions[i]
        cash_flows.append(cf)
    # Add NAV to final period
    if cash_flows:
        cash_flows[-1] += nav

    irr = _solve_irr(cash_flows)

    # J-curve: cumulative net cash flow at each period
    j_curve = []
    cumulative = 0
    for i in range(n):
        cumulative += distributions[i] - contributions[i]
        j_curve.append(cumulative)

    return {
        "total_contributed": total_contributed,
        "total_distributed": total_distributed,
        "nav": nav,
        "tvpi": tvpi,
        "dpi": dpi,
        "rvpi": rvpi,
        "net_irr": irr,
        "years": years,
        "j_curve": j_curve,
    }


def _solve_irr(cash_flows: list[float], tol: float = 1e-8, max_iter: int = 200) -> float:
    """Solve IRR using Newton's method."""
    r = 0.10  # initial guess
    for _ in range(max_iter):
        npv = sum(cf / (1 + r) ** t for t, cf in enumerate(cash_flows))
        dnpv = sum(-t * cf / (1 + r) ** (t + 1) for t, cf in enumerate(cash_flows))
        if abs(dnpv) < 1e-14:
            break
        r_new = r - npv / dnpv
        r_new = max(-0.99, min(r_new, 10.0))
        if abs(r_new - r) < tol:
            return r_new
        r = r_new
    return r


def dilution_waterfall(rounds: list[dict], founder_shares: int) -> dict:
    """Calculate ownership dilution across funding rounds."""
    total_shares = founder_shares
    stages = []

    for i, rnd in enumerate(rounds):
        pre_money = rnd["pre_money"]
        invested = rnd["invested"]
        post_money = pre_money + invested
        pool_increase = rnd.get("pool_increase", 0)

        # Price per share
        price_per_share = pre_money / total_shares if total_shares > 0 else 0

        # New shares issued to investor
        new_shares = int(invested / price_per_share) if price_per_share > 0 else 0

        # Option pool shares
        pool_shares = int(total_shares * pool_increase / (1 - pool_increase)) if pool_increase < 1 else 0

        total_shares += new_shares + pool_shares

        # Ownership
        founder_pct = founder_shares / total_shares if total_shares > 0 else 0
        investor_pct = new_shares / total_shares if total_shares > 0 else 0

        stages.append(
            {
                "round": i + 1,
                "invested": invested,
                "pre_money": pre_money,
                "post_money": post_money,
                "price_per_share": price_per_share,
                "new_shares": new_shares,
                "pool_shares": pool_shares,
                "total_shares": total_shares,
                "founder_ownership": founder_pct,
                "round_investor_ownership": investor_pct,
                "implied_valuation": post_money,
            }
        )

    return {
        "founder_shares": founder_shares,
        "final_total_shares": total_shares,
        "final_founder_ownership": founder_shares / total_shares if total_shares > 0 else 0,
        "rounds": stages,
    }


def main():
    parser = argparse.ArgumentParser(description="VC Returns & Dilution Calculator")
    parser.add_argument("--fund", action="store_true", help="Fund metrics mode")
    parser.add_argument("--contributions", help="Comma-sep capital calls")
    parser.add_argument("--distributions", help="Comma-sep distributions")
    parser.add_argument("--nav", type=float, help="Current NAV")
    parser.add_argument("--years", type=float, help="Fund age")
    parser.add_argument("--dilution", action="store_true", help="Dilution waterfall mode")
    parser.add_argument("--rounds", help="Rounds: 'investedM@pre_moneyM,...'")
    parser.add_argument("--founder-shares", type=int, help="Initial founder shares")
    parser.add_argument("--pool-increases", help="Option pool increases per round (comma-sep)")
    args = parser.parse_args()

    if args.fund:
        contribs = [float(x) for x in args.contributions.split(",")]
        dists = [float(x) for x in args.distributions.split(",")]
        r = fund_metrics(contribs, dists, args.nav, args.years)

        print(f"\n{'=' * 50}")
        print("  VC Fund Performance")
        print(f"{'=' * 50}")
        print(f"  Total Contributed: ${r['total_contributed']:>10,.1f}M")
        print(f"  Total Distributed: ${r['total_distributed']:>10,.1f}M")
        print(f"  NAV (Residual):    ${r['nav']:>10,.1f}M")
        print(f"{'─' * 50}")
        print(f"  TVPI:              {r['tvpi']:>10.2f}x")
        print(f"  DPI:               {r['dpi']:>10.2f}x")
        print(f"  RVPI:              {r['rvpi']:>10.2f}x")
        print(f"  Net IRR:           {r['net_irr'] * 100:>10.1f}%")
        print(f"{'─' * 50}")
        print("  J-Curve (cumulative net CF):")
        mx = max(abs(v) for v in r["j_curve"])
        for i, val in enumerate(r["j_curve"]):
            bar_len = max(1, int(abs(val) / mx * 15)) if mx > 0 else 1
            bar = ("+" if val > 0 else "-") * bar_len
            print(f"    Yr {i + 1}: ${val:>8,.1f}M  {bar}")
        print(f"{'=' * 50}\n")

    elif args.dilution:
        pool_increases = [float(x) for x in args.pool_increases.split(",")] if args.pool_increases else []
        rounds = []
        for i, rnd_str in enumerate(args.rounds.split(",")):
            parts = rnd_str.strip().upper().replace("M", "").split("@")
            invested = float(parts[0]) * 1_000_000
            pre_money = float(parts[1]) * 1_000_000
            pool = pool_increases[i] if i < len(pool_increases) else 0
            rounds.append({"invested": invested, "pre_money": pre_money, "pool_increase": pool})

        r = dilution_waterfall(rounds, args.founder_shares)

        print(f"\n{'=' * 60}")
        print("  Dilution Waterfall")
        print(f"{'=' * 60}")
        print(f"  Initial Founder Shares: {r['founder_shares']:>12,}")
        print(f"{'─' * 60}")
        print(f"  {'Round':<7} {'Invested':>10} {'Pre-$':>10} {'Post-$':>10} {'Founder%':>9} {'Round%':>8}")
        print(f"  {'─' * 7} {'─' * 10} {'─' * 10} {'─' * 10} {'─' * 9} {'─' * 8}")
        for s in r["rounds"]:
            print(
                f"  R{s['round']:<6} ${s['invested'] / 1e6:>8.1f}M ${s['pre_money'] / 1e6:>8.1f}M"
                f" ${s['implied_valuation'] / 1e6:>8.1f}M"
                f" {s['founder_ownership'] * 100:>8.1f}% {s['round_investor_ownership'] * 100:>7.1f}%"
            )
        print(f"{'─' * 60}")
        print(f"  Final Founder Ownership: {r['final_founder_ownership'] * 100:>8.1f}%")
        print(f"  Final Total Shares:      {r['final_total_shares']:>12,}")
        print(f"{'=' * 60}\n")

    else:
        parser.error("Specify --fund or --dilution mode")


if __name__ == "__main__":
    main()
