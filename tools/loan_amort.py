#!/usr/bin/env python3
"""Loan amortization schedule calculator.

Usage:
    python loan_amort.py --principal 500000 --rate 0.065 --years 30
    python loan_amort.py --principal 500000 --rate 0.065 --years 30 --extra 500
"""

import argparse
import math


def loan_amortization(principal: float, annual_rate: float, years: int, extra_payment: float = 0.0) -> dict:
    """Calculate loan amortization schedule and summary.

    Args:
        principal: Loan principal amount.
        annual_rate: Annual interest rate.
        years: Loan term in years.
        extra_payment: Extra monthly payment toward principal.

    Returns:
        Dict with monthly payment, total interest, schedule, and payoff info.
    """
    monthly_rate = annual_rate / 12
    n_payments = years * 12

    # Standard monthly payment (P&I)
    if monthly_rate > 0:
        monthly_payment = (
            principal * monthly_rate * (1 + monthly_rate) ** n_payments / ((1 + monthly_rate) ** n_payments - 1)
        )
    else:
        monthly_payment = principal / n_payments

    # Build amortization schedule
    balance = principal
    total_interest = 0.0
    total_principal_paid = 0.0
    schedule = []
    actual_months = 0

    for month in range(1, n_payments + 1):
        if balance <= 0:
            break

        interest = balance * monthly_rate
        scheduled_principal = monthly_payment - interest
        actual_principal = scheduled_principal + extra_payment
        actual_principal = min(actual_principal, balance)  # don't overpay

        balance -= actual_principal
        if balance < 0.01:
            balance = 0

        total_interest += interest
        total_principal_paid += actual_principal
        actual_months = month

        # Store yearly summaries (every 12th month or final month)
        if month % 12 == 0 or balance == 0:
            schedule.append(
                {
                    "month": month,
                    "year": math.ceil(month / 12),
                    "balance": balance,
                    "cumulative_interest": total_interest,
                    "cumulative_principal": total_principal_paid,
                }
            )

    # Savings from extra payments
    standard_total_interest = monthly_payment * n_payments - principal
    interest_saved = standard_total_interest - total_interest
    months_saved = n_payments - actual_months

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "term_years": years,
        "monthly_payment": monthly_payment,
        "extra_payment": extra_payment,
        "total_payment": monthly_payment + extra_payment,
        "total_interest": total_interest,
        "total_cost": principal + total_interest,
        "actual_payoff_months": actual_months,
        "actual_payoff_years": actual_months / 12,
        "interest_saved": interest_saved,
        "months_saved": months_saved,
        "schedule": schedule,
    }


def main():
    parser = argparse.ArgumentParser(description="Loan Amortization Calculator")
    parser.add_argument("--principal", type=float, required=True, help="Loan amount")
    parser.add_argument("--rate", type=float, required=True, help="Annual interest rate (e.g., 0.065)")
    parser.add_argument("--years", type=int, required=True, help="Loan term in years")
    parser.add_argument("--extra", type=float, default=0, help="Extra monthly payment (default: 0)")
    args = parser.parse_args()

    r = loan_amortization(args.principal, args.rate, args.years, args.extra)

    print(f"\n{'=' * 50}")
    print("  Loan Amortization")
    print(f"{'=' * 50}")
    print(f"  Principal:         ${r['principal']:>12,.2f}")
    print(f"  Interest Rate:     {r['annual_rate'] * 100:>12.3f}%")
    print(f"  Term:              {r['term_years']:>12d} years")
    print(f"{'─' * 50}")
    print(f"  Monthly Payment:   ${r['monthly_payment']:>12,.2f}")
    if r["extra_payment"] > 0:
        print(f"  Extra Payment:     ${r['extra_payment']:>12,.2f}")
        print(f"  Total Monthly:     ${r['total_payment']:>12,.2f}")
    print(f"{'─' * 50}")
    print(f"  Total Interest:    ${r['total_interest']:>12,.2f}")
    print(f"  Total Cost:        ${r['total_cost']:>12,.2f}")
    if r["extra_payment"] > 0:
        print(f"{'─' * 50}")
        print(f"  Early Payoff:      {r['actual_payoff_years']:>12.1f} years")
        print(f"  Months Saved:      {r['months_saved']:>12d}")
        print(f"  Interest Saved:    ${r['interest_saved']:>12,.2f}")
    print(f"{'─' * 50}")
    print("  Annual Balance Summary:")
    print(f"    {'Year':>4}  {'Balance':>14}  {'Cum Interest':>14}  {'Cum Principal':>14}")
    for s in r["schedule"][:10]:
        print(
            f"    {s['year']:>4}  ${s['balance']:>13,.2f}  ${s['cumulative_interest']:>13,.2f}"
            f"  ${s['cumulative_principal']:>13,.2f}"
        )
    if len(r["schedule"]) > 10:
        print(f"    ... ({len(r['schedule']) - 10} more years)")
        s = r["schedule"][-1]
        print(
            f"    {s['year']:>4}  ${s['balance']:>13,.2f}  ${s['cumulative_interest']:>13,.2f}"
            f"  ${s['cumulative_principal']:>13,.2f}"
        )
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
