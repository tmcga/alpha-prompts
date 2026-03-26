#!/usr/bin/env python3
"""Credit analysis — Altman Z-Score, hazard rates, default probability from spreads.

Usage:
    python credit_spread.py --spread 0.03 --recovery 0.40 --maturity 5
    python credit_spread.py --zscore --wc-ta 0.1 --re-ta 0.2 --ebit-ta 0.15 --eq-debt 0.8 --sales-ta 1.5
"""

import argparse
import math


def altman_zscore(wc_ta: float, re_ta: float, ebit_ta: float, equity_debt: float, sales_ta: float) -> dict:
    """Calculate Altman Z-Score for public manufacturing firms.

    Args:
        wc_ta: Working Capital / Total Assets.
        re_ta: Retained Earnings / Total Assets.
        ebit_ta: EBIT / Total Assets.
        equity_debt: Market Value of Equity / Book Value of Total Debt.
        sales_ta: Sales / Total Assets.

    Returns:
        Dict with Z-Score and zone classification.
    """
    z = 1.2 * wc_ta + 1.4 * re_ta + 3.3 * ebit_ta + 0.6 * equity_debt + 1.0 * sales_ta

    if z > 2.99:
        zone = "Safe"
        description = "Low probability of bankruptcy"
    elif z > 1.81:
        zone = "Grey"
        description = "Moderate risk — further analysis needed"
    else:
        zone = "Distress"
        description = "High probability of bankruptcy"

    return {
        "z_score": z,
        "zone": zone,
        "description": description,
        "components": {
            "working_capital": 1.2 * wc_ta,
            "retained_earnings": 1.4 * re_ta,
            "ebit": 3.3 * ebit_ta,
            "equity_to_debt": 0.6 * equity_debt,
            "sales": 1.0 * sales_ta,
        },
    }


def credit_from_spread(cds_spread: float, recovery_rate: float = 0.40, maturity: float = 5.0) -> dict:
    """Derive default probabilities from CDS/credit spread.

    Args:
        cds_spread: Annual CDS spread (e.g., 0.03 for 300bps).
        recovery_rate: Expected recovery rate (default: 40%).
        maturity: Time horizon in years.

    Returns:
        Dict with hazard rate, cumulative PD, expected loss, and annualized metrics.
    """
    lgd = 1 - recovery_rate

    # Hazard rate (continuous): h = spread / LGD
    hazard_rate = cds_spread / lgd if lgd > 0 else 0

    # Cumulative default probability: PD(T) = 1 - exp(-h * T)
    cum_default_probs = {}
    for yr in range(1, int(maturity) + 1):
        cum_default_probs[yr] = 1 - math.exp(-hazard_rate * yr)

    # Marginal (conditional) default probability per year
    marginal_pds = {}
    for yr in range(1, int(maturity) + 1):
        survival_prev = math.exp(-hazard_rate * (yr - 1))
        survival_curr = math.exp(-hazard_rate * yr)
        marginal_pds[yr] = (survival_prev - survival_curr) / survival_prev if survival_prev > 0 else 0

    # Survival probability at maturity
    survival_prob = math.exp(-hazard_rate * maturity)

    # Expected loss (present value approx)
    expected_loss_pct = (1 - survival_prob) * lgd

    # Implied annual default probability (discrete)
    annual_pd = 1 - math.exp(-hazard_rate)

    return {
        "cds_spread": cds_spread,
        "cds_spread_bps": cds_spread * 10000,
        "recovery_rate": recovery_rate,
        "lgd": lgd,
        "hazard_rate": hazard_rate,
        "annual_default_prob": annual_pd,
        "cumulative_default_probs": cum_default_probs,
        "marginal_default_probs": marginal_pds,
        "survival_probability": survival_prob,
        "expected_loss_pct": expected_loss_pct,
        "maturity": maturity,
    }


def main():
    parser = argparse.ArgumentParser(description="Credit Analysis Tools")
    parser.add_argument("--zscore", action="store_true", help="Run Altman Z-Score")
    parser.add_argument("--wc-ta", type=float, help="Working Capital / Total Assets")
    parser.add_argument("--re-ta", type=float, help="Retained Earnings / Total Assets")
    parser.add_argument("--ebit-ta", type=float, help="EBIT / Total Assets")
    parser.add_argument("--eq-debt", type=float, help="Equity MV / Debt BV")
    parser.add_argument("--sales-ta", type=float, help="Sales / Total Assets")
    parser.add_argument("--spread", type=float, help="CDS spread (e.g., 0.03 for 300bps)")
    parser.add_argument("--recovery", type=float, default=0.40, help="Recovery rate (default: 0.40)")
    parser.add_argument("--maturity", type=float, default=5, help="Maturity in years (default: 5)")
    args = parser.parse_args()

    if args.zscore:
        for field in ["wc_ta", "re_ta", "ebit_ta", "eq_debt", "sales_ta"]:
            if getattr(args, field) is None:
                parser.error(f"Z-Score requires --{field.replace('_', '-')}")
        r = altman_zscore(args.wc_ta, args.re_ta, args.ebit_ta, args.eq_debt, args.sales_ta)

        print(f"\n{'=' * 50}")
        print("  Altman Z-Score Analysis")
        print(f"{'=' * 50}")
        print("  Components:")
        for name, val in r["components"].items():
            print(f"    {name:<20} {val:>8.4f}")
        print(f"{'─' * 50}")
        print(f"  Z-Score:           {r['z_score']:>10.4f}")
        print(f"  Zone:              {r['zone']:>10}")
        print(f"  Assessment:        {r['description']}")
        print("  Thresholds:        >2.99 Safe | 1.81-2.99 Grey | <1.81 Distress")
        print(f"{'=' * 50}\n")

    elif args.spread is not None:
        r = credit_from_spread(args.spread, args.recovery, args.maturity)

        print(f"\n{'=' * 50}")
        print("  Credit Spread Analysis")
        print(f"{'=' * 50}")
        print(f"  CDS Spread:        {r['cds_spread_bps']:>10.0f} bps")
        print(f"  Recovery Rate:     {r['recovery_rate'] * 100:>10.1f}%")
        print(f"  LGD:               {r['lgd'] * 100:>10.1f}%")
        print(f"{'─' * 50}")
        print(f"  Hazard Rate:       {r['hazard_rate'] * 100:>10.2f}%")
        print(f"  Annual PD:         {r['annual_default_prob'] * 100:>10.2f}%")
        print(f"{'─' * 50}")
        print("  Cumulative Default Probabilities:")
        for yr, pd in r["cumulative_default_probs"].items():
            print(f"    Year {yr}:          {pd * 100:>10.2f}%")
        print(f"{'─' * 50}")
        print(f"  Survival at {int(r['maturity'])}Y:  {r['survival_probability'] * 100:>10.2f}%")
        print(f"  Expected Loss:     {r['expected_loss_pct'] * 100:>10.2f}%")
        print(f"{'=' * 50}\n")

    else:
        parser.error("Provide --zscore (with ratios) or --spread")


if __name__ == "__main__":
    main()
