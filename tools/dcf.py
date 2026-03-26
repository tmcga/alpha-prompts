#!/usr/bin/env python3
"""Discounted Cash Flow (DCF) valuation calculator.

Usage:
    python dcf.py --fcf 100,110,121,133,146 --wacc 0.10 --terminal-growth 0.025 --net-debt 500 --shares 100
"""
import argparse
import math


def dcf_valuation(fcfs: list[float], wacc: float, terminal_growth: float,
                  net_debt: float = 0, shares: float = 1) -> dict:
    """Calculate DCF valuation with Gordon Growth terminal value.

    Args:
        fcfs: Projected free cash flows for each year.
        wacc: Weighted average cost of capital.
        terminal_growth: Perpetual growth rate for terminal value.
        net_debt: Net debt (debt minus cash). Subtracted from EV.
        shares: Shares outstanding for per-share price.

    Returns:
        Dict with enterprise value, equity value, price per share, and breakdown.
    """
    if wacc <= terminal_growth:
        raise ValueError("WACC must exceed terminal growth rate")

    # PV of explicit period cash flows
    pv_fcfs = []
    for i, fcf in enumerate(fcfs):
        pv = fcf / (1 + wacc) ** (i + 1)
        pv_fcfs.append(pv)

    # Terminal value (Gordon Growth)
    terminal_fcf = fcfs[-1] * (1 + terminal_growth)
    terminal_value = terminal_fcf / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc) ** len(fcfs)

    enterprise_value = sum(pv_fcfs) + pv_terminal
    equity_value = enterprise_value - net_debt
    price_per_share = equity_value / shares if shares > 0 else 0

    return {
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "price_per_share": price_per_share,
        "pv_explicit_fcfs": sum(pv_fcfs),
        "pv_terminal_value": pv_terminal,
        "terminal_value_pct": pv_terminal / enterprise_value * 100 if enterprise_value else 0,
        "terminal_value_undiscounted": terminal_value,
    }


def sensitivity_table(fcfs: list[float], wacc: float, terminal_growth: float,
                      net_debt: float, shares: float,
                      wacc_range: float = 0.02, tg_range: float = 0.01,
                      steps: int = 5) -> list[list]:
    """Generate WACC vs terminal growth sensitivity table for price per share."""
    wacc_values = [wacc + (i - steps // 2) * (wacc_range / steps) for i in range(steps)]
    tg_values = [terminal_growth + (i - steps // 2) * (tg_range / steps) for i in range(steps)]

    table = [["WACC \\ TG"] + [f"{tg:.3f}" for tg in tg_values]]
    for w in wacc_values:
        row = [f"{w:.3f}"]
        for tg in tg_values:
            if w <= tg:
                row.append("N/A")
            else:
                result = dcf_valuation(fcfs, w, tg, net_debt, shares)
                row.append(f"${result['price_per_share']:.2f}")
        table.append(row)
    return table


def print_table(table: list[list]):
    """Pretty-print a table."""
    widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
    for row in table:
        print("  ".join(str(cell).rjust(w) for cell, w in zip(row, widths)))


def main():
    parser = argparse.ArgumentParser(description="DCF Valuation Calculator")
    parser.add_argument("--fcf", required=True, help="Comma-separated projected FCFs")
    parser.add_argument("--wacc", type=float, required=True, help="WACC (e.g., 0.10 for 10%%)")
    parser.add_argument("--terminal-growth", type=float, required=True, help="Terminal growth rate")
    parser.add_argument("--net-debt", type=float, default=0, help="Net debt (default: 0)")
    parser.add_argument("--shares", type=float, default=1, help="Shares outstanding (default: 1)")
    args = parser.parse_args()

    fcfs = [float(x.strip()) for x in args.fcf.split(",")]
    result = dcf_valuation(fcfs, args.wacc, args.terminal_growth, args.net_debt, args.shares)

    print(f"\n{'='*50}")
    print(f"  DCF Valuation")
    print(f"{'='*50}")
    print(f"  PV of FCFs (explicit):  ${result['pv_explicit_fcfs']:>12,.2f}")
    print(f"  PV of Terminal Value:   ${result['pv_terminal_value']:>12,.2f}")
    print(f"  Enterprise Value:       ${result['enterprise_value']:>12,.2f}")
    print(f"  Less: Net Debt:         ${args.net_debt:>12,.2f}")
    print(f"  Equity Value:           ${result['equity_value']:>12,.2f}")
    print(f"  Price per Share:        ${result['price_per_share']:>12,.2f}")
    print(f"  Terminal Value % of EV: {result['terminal_value_pct']:>12.1f}%")
    print(f"{'='*50}")

    print(f"\n  Sensitivity: Price per Share (WACC vs Terminal Growth)")
    print(f"{'─'*50}")
    table = sensitivity_table(fcfs, args.wacc, args.terminal_growth, args.net_debt, args.shares)
    print_table(table)
    print()


if __name__ == "__main__":
    main()
