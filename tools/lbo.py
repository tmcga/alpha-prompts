#!/usr/bin/env python3
"""LBO (Leveraged Buyout) returns calculator.

Usage:
    python lbo.py --ebitda 100 --entry-multiple 10 --exit-multiple 10 --leverage 5 --rate 0.06 --growth 0.05 --years 5
"""

import argparse


def lbo_returns(
    ebitda: float,
    entry_multiple: float,
    exit_multiple: float,
    leverage: float,
    interest_rate: float,
    ebitda_growth: float,
    years: int,
    amortization_pct: float = 0.01,
    tax_rate: float = None,
    capex_pct: float = None,
    nwc_pct: float = None,
    da_pct: float = None,
) -> dict:
    """Calculate LBO returns with MOIC, IRR, and attribution.

    Args:
        ebitda: Entry EBITDA.
        entry_multiple: EV / EBITDA at entry.
        exit_multiple: EV / EBITDA at exit.
        leverage: Total Debt / EBITDA at entry.
        interest_rate: Blended interest rate on debt.
        ebitda_growth: Annual EBITDA growth rate.
        years: Hold period.
        amortization_pct: Annual mandatory amortization as % of initial debt.
        tax_rate: Corporate tax rate (enables detailed FCF build).
        capex_pct: CapEx as % of EBITDA.
        nwc_pct: Change in NWC as % of EBITDA growth.
        da_pct: D&A as % of EBITDA.

    Returns:
        Dict with MOIC, IRR, equity values, debt schedule, and returns attribution.
    """
    detailed_fcf = tax_rate is not None

    # Entry
    entry_ev = ebitda * entry_multiple
    entry_debt = ebitda * leverage
    entry_equity = entry_ev - entry_debt

    # Debt schedule and cash flows
    debt_balance = entry_debt
    debt_schedule = [entry_debt]
    ebitda_schedule = [ebitda]

    for yr in range(1, years + 1):
        yr_ebitda = ebitda * (1 + ebitda_growth) ** yr
        prev_ebitda = ebitda * (1 + ebitda_growth) ** (yr - 1)
        ebitda_schedule.append(yr_ebitda)

        interest = debt_balance * interest_rate
        mandatory_amort = entry_debt * amortization_pct

        if detailed_fcf:
            da = yr_ebitda * (da_pct or 0.10)
            ebit = yr_ebitda - da
            taxes = max(0, (ebit - interest)) * tax_rate
            capex = yr_ebitda * (capex_pct or 0.10)
            delta_nwc = (yr_ebitda - prev_ebitda) * (nwc_pct or 0.05)
            fcf_for_paydown = yr_ebitda - taxes - capex - delta_nwc - interest
        else:
            fcf_for_paydown = yr_ebitda * 0.5 - interest

        total_paydown = min(debt_balance, max(0, fcf_for_paydown) + mandatory_amort)
        debt_balance = max(0, debt_balance - total_paydown)
        debt_schedule.append(debt_balance)

    # Exit
    exit_ebitda = ebitda * (1 + ebitda_growth) ** years
    exit_ev = exit_ebitda * exit_multiple
    exit_equity = exit_ev - debt_balance

    # Returns
    moic = exit_equity / entry_equity if entry_equity > 0 else 0
    irr = moic ** (1 / years) - 1 if moic > 0 and years > 0 else 0

    # Attribution
    growth_contribution = (exit_ebitda / ebitda - 1) * entry_multiple / entry_equity
    multiple_contribution = (exit_multiple - entry_multiple) * exit_ebitda / entry_equity
    deleverage_contribution = (entry_debt - debt_balance) / entry_equity

    return {
        "entry_ev": entry_ev,
        "entry_debt": entry_debt,
        "entry_equity": entry_equity,
        "exit_ebitda": exit_ebitda,
        "exit_ev": exit_ev,
        "exit_debt": debt_balance,
        "exit_equity": exit_equity,
        "moic": moic,
        "irr": irr,
        "debt_paydown": entry_debt - debt_balance,
        "attribution": {
            "ebitda_growth": growth_contribution,
            "multiple_change": multiple_contribution,
            "deleveraging": deleverage_contribution,
        },
        "debt_schedule": debt_schedule,
        "ebitda_schedule": ebitda_schedule,
    }


def main():
    parser = argparse.ArgumentParser(description="LBO Returns Calculator")
    parser.add_argument("--ebitda", type=float, required=True, help="Entry EBITDA")
    parser.add_argument("--entry-multiple", type=float, required=True, help="Entry EV/EBITDA")
    parser.add_argument("--exit-multiple", type=float, required=True, help="Exit EV/EBITDA")
    parser.add_argument("--leverage", type=float, required=True, help="Entry Debt/EBITDA")
    parser.add_argument("--rate", type=float, default=0.06, help="Interest rate (default: 0.06)")
    parser.add_argument("--growth", type=float, default=0.05, help="EBITDA growth (default: 0.05)")
    parser.add_argument("--years", type=int, default=5, help="Hold period (default: 5)")
    parser.add_argument("--tax-rate", type=float, default=None, help="Tax rate (enables detailed FCF)")
    parser.add_argument("--capex-pct", type=float, default=None, help="CapEx %% of EBITDA (default: 10%%)")
    parser.add_argument("--nwc-pct", type=float, default=None, help="NWC change %% of EBITDA growth (default: 5%%)")
    parser.add_argument("--da-pct", type=float, default=None, help="D&A %% of EBITDA (default: 10%%)")
    args = parser.parse_args()

    r = lbo_returns(
        args.ebitda,
        args.entry_multiple,
        args.exit_multiple,
        args.leverage,
        args.rate,
        args.growth,
        args.years,
        tax_rate=args.tax_rate,
        capex_pct=args.capex_pct,
        nwc_pct=args.nwc_pct,
        da_pct=args.da_pct,
    )

    print(f"\n{'=' * 50}")
    print("  LBO Returns Analysis")
    print(f"{'=' * 50}")
    print(f"  Entry EV:        ${r['entry_ev']:>10,.1f}  ({args.entry_multiple:.1f}x EBITDA)")
    print(f"  Entry Debt:      ${r['entry_debt']:>10,.1f}  ({args.leverage:.1f}x EBITDA)")
    print(f"  Entry Equity:    ${r['entry_equity']:>10,.1f}")
    print(f"{'─' * 50}")
    print(f"  Exit EBITDA:     ${r['exit_ebitda']:>10,.1f}  ({args.growth * 100:.1f}% CAGR)")
    print(f"  Exit EV:         ${r['exit_ev']:>10,.1f}  ({args.exit_multiple:.1f}x EBITDA)")
    print(f"  Exit Debt:       ${r['exit_debt']:>10,.1f}")
    print(f"  Exit Equity:     ${r['exit_equity']:>10,.1f}")
    print(f"{'─' * 50}")
    print(f"  MOIC:            {r['moic']:>10.2f}x")
    print(f"  IRR:             {r['irr'] * 100:>10.1f}%")
    print(f"  Debt Paydown:    ${r['debt_paydown']:>10,.1f}")
    print(f"{'─' * 50}")
    print("  Returns Attribution:")
    a = r["attribution"]
    total = a["ebitda_growth"] + a["multiple_change"] + a["deleveraging"]
    for label, val in [
        ("EBITDA Growth", a["ebitda_growth"]),
        ("Multiple Change", a["multiple_change"]),
        ("Deleveraging", a["deleveraging"]),
    ]:
        pct = val / total * 100 if total else 0
        print(f"    {label:<18} {val:>6.2f}x  ({pct:>5.1f}%)")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
