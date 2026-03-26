#!/usr/bin/env python3
"""WACC (Weighted Average Cost of Capital) calculator with CAPM.

Usage:
    python wacc.py --equity 1000 --debt 500 --tax 0.25 --rf 0.04 --beta 1.2 --erp 0.055 --cost-of-debt 0.05
"""

import argparse


def wacc(
    equity_value: float,
    debt_value: float,
    tax_rate: float,
    risk_free: float,
    beta: float,
    equity_risk_premium: float,
    cost_of_debt: float,
    size_premium: float = 0.0,
    country_risk: float = 0.0,
    alpha: float = 0.0,
) -> dict:
    """Calculate WACC using CAPM build-up for cost of equity.

    Args:
        equity_value: Market value of equity.
        debt_value: Market value of debt.
        tax_rate: Marginal tax rate.
        risk_free: Risk-free rate.
        beta: Levered beta.
        equity_risk_premium: Equity risk premium.
        cost_of_debt: Pre-tax cost of debt.
        size_premium: Small-cap size premium (default: 0).
        country_risk: Country risk premium (default: 0).
        alpha: Company-specific alpha/risk (default: 0).

    Returns:
        Dict with WACC, cost of equity, weights, and unlevered beta.
    """
    total_value = equity_value + debt_value
    weight_equity = equity_value / total_value if total_value else 0
    weight_debt = debt_value / total_value if total_value else 0

    # CAPM build-up: r_e = r_f + beta * ERP + size + country + alpha
    cost_of_equity = risk_free + beta * equity_risk_premium + size_premium + country_risk + alpha

    # After-tax cost of debt
    after_tax_debt = cost_of_debt * (1 - tax_rate)

    # WACC
    wacc_value = weight_equity * cost_of_equity + weight_debt * after_tax_debt

    # Unlevered beta (Hamada equation)
    de_ratio = debt_value / equity_value if equity_value else 0
    unlevered_beta = beta / (1 + (1 - tax_rate) * de_ratio)

    return {
        "wacc": wacc_value,
        "cost_of_equity": cost_of_equity,
        "after_tax_cost_of_debt": after_tax_debt,
        "weight_equity": weight_equity,
        "weight_debt": weight_debt,
        "debt_to_equity": de_ratio,
        "unlevered_beta": unlevered_beta,
        "total_value": total_value,
        "size_premium": size_premium,
        "country_risk": country_risk,
        "alpha": alpha,
    }


def main():
    parser = argparse.ArgumentParser(description="WACC Calculator")
    parser.add_argument("--equity", type=float, required=True, help="Market value of equity")
    parser.add_argument("--debt", type=float, required=True, help="Market value of debt")
    parser.add_argument("--tax", type=float, required=True, help="Tax rate (e.g., 0.25)")
    parser.add_argument("--rf", type=float, required=True, help="Risk-free rate")
    parser.add_argument("--beta", type=float, required=True, help="Levered beta")
    parser.add_argument("--erp", type=float, required=True, help="Equity risk premium")
    parser.add_argument("--cost-of-debt", type=float, required=True, help="Pre-tax cost of debt")
    parser.add_argument("--size-premium", type=float, default=0.0, help="Size premium (default: 0)")
    parser.add_argument("--country-risk", type=float, default=0.0, help="Country risk premium (default: 0)")
    parser.add_argument("--alpha", type=float, default=0.0, help="Company-specific alpha (default: 0)")
    args = parser.parse_args()

    r = wacc(
        args.equity,
        args.debt,
        args.tax,
        args.rf,
        args.beta,
        args.erp,
        args.cost_of_debt,
        args.size_premium,
        args.country_risk,
        args.alpha,
    )

    print(f"\n{'=' * 50}")
    print("  WACC Calculation")
    print(f"{'=' * 50}")
    print("  Capital Structure:")
    print(f"    Equity:          ${args.equity:>10,.0f}  ({r['weight_equity'] * 100:.1f}%)")
    print(f"    Debt:            ${args.debt:>10,.0f}  ({r['weight_debt'] * 100:.1f}%)")
    print(f"    Total:           ${r['total_value']:>10,.0f}")
    print(f"    D/E Ratio:       {r['debt_to_equity']:>10.2f}x")
    print(f"{'─' * 50}")
    print("  Cost of Equity (CAPM):")
    print(f"    Risk-Free Rate:  {args.rf * 100:>10.2f}%")
    print(f"    Beta (levered):  {args.beta:>10.2f}")
    print(f"    Beta (unlevered):{r['unlevered_beta']:>10.2f}")
    print(f"    Equity Risk Prem:{args.erp * 100:>10.2f}%")
    if r["size_premium"] > 0:
        print(f"    Size Premium:    {r['size_premium'] * 100:>10.2f}%")
    if r["country_risk"] > 0:
        print(f"    Country Risk:    {r['country_risk'] * 100:>10.2f}%")
    if r["alpha"] > 0:
        print(f"    Alpha:           {r['alpha'] * 100:>10.2f}%")
    print(f"    Cost of Equity:  {r['cost_of_equity'] * 100:>10.2f}%")
    print(f"{'─' * 50}")
    print("  Cost of Debt:")
    print(f"    Pre-tax:         {args.cost_of_debt * 100:>10.2f}%")
    print(f"    Tax rate:        {args.tax * 100:>10.1f}%")
    print(f"    After-tax:       {r['after_tax_cost_of_debt'] * 100:>10.2f}%")
    print(f"{'─' * 50}")
    print(f"  WACC:              {r['wacc'] * 100:>10.2f}%")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
