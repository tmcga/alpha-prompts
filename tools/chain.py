#!/usr/bin/env python3
"""Chained tool workflows — compose existing tools into multi-step analyses."""

import argparse

_DCF_LOW, _DCF_HIGH = 0.85, 1.15  # +/- 15% confidence band around DCF
_LBO_FLOOR = 0.9  # 10% discount on LBO entry for floor
_ASSUMED_DEBT_COST = 0.06  # default rate for coverage calc


def valuation_triangle(
    fcfs: list[float],
    wacc_rate: float,
    terminal_growth: float,
    net_debt: float = 0,
    shares: float = 1,
    lbo_ebitda: float | None = None,
    entry_multiple: float | None = None,
    exit_multiple: float | None = None,
    leverage: float = 5.0,
    debt_rate: float = 0.06,
    ebitda_growth: float = 0.08,
    years: int = 5,
) -> dict:
    """Run DCF + LBO to produce a unified valuation range.

    Returns:
        Dict with DCF value, LBO value (if inputs provided), and combined range.
    """
    from dcf import dcf_valuation
    from lbo import lbo_returns

    dcf = dcf_valuation(fcfs, wacc_rate, terminal_growth=terminal_growth, net_debt=net_debt, shares=shares)
    result = {
        "dcf": {
            "enterprise_value": dcf["enterprise_value"],
            "equity_value": dcf["equity_value"],
            "price_per_share": dcf["price_per_share"],
            "terminal_value_pct": dcf["terminal_value_pct"],
        },
    }
    ev_low = dcf["enterprise_value"] * _DCF_LOW
    ev_high = dcf["enterprise_value"] * _DCF_HIGH
    if lbo_ebitda and entry_multiple and exit_multiple:
        lbo = lbo_returns(lbo_ebitda, entry_multiple, exit_multiple, leverage, debt_rate, ebitda_growth, years)
        result["lbo"] = {
            "entry_ev": lbo["entry_ev"],
            "exit_ev": lbo["exit_ev"],
            "moic": lbo["moic"],
            "irr": lbo["irr"],
        }
        ev_low = min(ev_low, lbo["entry_ev"] * _LBO_FLOOR)
        ev_high = max(ev_high, lbo["exit_ev"])
    result["range"] = {"ev_low": round(ev_low, 1), "ev_high": round(ev_high, 1)}
    return result


def credit_full(
    revenue: float,
    ebitda: float,
    total_debt: float,
    equity_value: float,
    asset_vol: float = 0.30,
    current_assets: float | None = None,
    current_liabilities: float | None = None,
    retained_earnings: float | None = None,
    risk_free: float = 0.045,
    maturity: float = 5.0,
) -> dict:
    """Run Z-Score + Merton model for integrated credit view.

    Returns:
        Dict with Z-Score analysis (if inputs provided) and Merton default probability.
    """
    from credit_spread import altman_zscore
    from merton_model import merton_model

    result = {}
    if current_assets is not None and current_liabilities is not None and retained_earnings is not None:
        ta = equity_value + total_debt
        zscore = altman_zscore(
            wc_ta=(current_assets - current_liabilities) / ta,
            re_ta=retained_earnings / ta,
            ebit_ta=(ebitda * 0.85) / ta,
            equity_debt=equity_value / total_debt if total_debt > 0 else 0,
            sales_ta=revenue / ta,
        )
        result["zscore"] = zscore
    asset_value = equity_value + total_debt
    merton = merton_model(asset_value, total_debt, asset_vol, risk_free, maturity)
    result["merton"] = {
        "default_probability": merton["default_probability"],
        "distance_to_default": merton["distance_to_default"],
        "equity_value": merton["equity_value"],
        "credit_spread_bps": merton["credit_spread_bps"],
    }
    cost_of_debt = total_debt * _ASSUMED_DEBT_COST
    result["summary"] = {
        "leverage": round(total_debt / ebitda, 1) if ebitda > 0 else None,
        "coverage": round(ebitda / cost_of_debt, 1) if cost_of_debt > 0 else None,
        "default_probability_pct": round(merton["default_probability"] * 100, 2),
    }
    return result


def portfolio_full(
    returns: list[float],
    risk_free: float = 0.045,
    benchmark_returns: list[float] | None = None,
    win_prob: float | None = None,
    win_loss_ratio: float | None = None,
) -> dict:
    """Run portfolio metrics + benchmark relative + Kelly for complete picture.

    Returns:
        Dict with risk metrics, benchmark comparison, and position sizing.
    """
    from portfolio_risk import portfolio_metrics, benchmark_relative
    from kelly import kelly_criterion

    metrics = portfolio_metrics(returns, risk_free)
    result = {"metrics": metrics}
    if benchmark_returns:
        bench = benchmark_relative(returns, benchmark_returns, risk_free)
        result["benchmark"] = bench
    if win_prob is not None and win_loss_ratio is not None:
        sizing = kelly_criterion(win_prob, win_loss_ratio)
        result["kelly"] = sizing
    return result


def main():
    parser = argparse.ArgumentParser(description="Chained Tool Workflows")
    sub = parser.add_subparsers(dest="workflow")
    val = sub.add_parser("valuation", help="DCF + LBO valuation triangle")
    val.add_argument("--fcf", required=True, help="Comma-separated FCFs")
    val.add_argument("--wacc", type=float, required=True)
    val.add_argument("--tg", type=float, required=True, help="Terminal growth")
    val.add_argument("--net-debt", type=float, default=0)
    val.add_argument("--shares", type=float, default=1)
    val.add_argument("--lbo-ebitda", type=float, default=None)
    val.add_argument("--entry", type=float, default=None, help="LBO entry multiple")
    val.add_argument("--exit", type=float, default=None, help="LBO exit multiple")
    val.add_argument("--leverage", type=float, default=5.0)
    val.add_argument("--rate", type=float, default=0.06)
    val.add_argument("--growth", type=float, default=0.08)
    cred = sub.add_parser("credit", help="Z-Score + Merton credit analysis")
    cred.add_argument("--revenue", type=float, required=True)
    cred.add_argument("--ebitda", type=float, required=True)
    cred.add_argument("--debt", type=float, required=True)
    cred.add_argument("--equity", type=float, required=True)
    cred.add_argument("--vol", type=float, default=0.30)
    args = parser.parse_args()
    if args.workflow == "valuation":
        fcfs = [float(x) for x in args.fcf.split(",")]
        r = valuation_triangle(
            fcfs,
            args.wacc,
            args.tg,
            args.net_debt,
            args.shares,
            args.lbo_ebitda,
            args.entry,
            args.exit,
            args.leverage,
            args.rate,
            args.growth,
        )
        print(f"\n{'=' * 55}")
        print("  Valuation Triangle")
        print(f"{'=' * 55}")
        print(f"  DCF Enterprise Value:  ${r['dcf']['enterprise_value']:>12,.1f}")
        print(f"  DCF Equity Value:      ${r['dcf']['equity_value']:>12,.1f}")
        if "lbo" in r:
            print(f"  LBO Entry EV:          ${r['lbo']['entry_ev']:>12,.1f}")
            print(f"  LBO Exit EV:           ${r['lbo']['exit_ev']:>12,.1f}")
            print(f"  LBO MOIC:              {r['lbo']['moic']:>12.2f}x")
            print(f"  LBO IRR:               {r['lbo']['irr'] * 100:>11.1f}%")
        print(f"{'─' * 55}")
        print(f"  Combined EV Range:     ${r['range']['ev_low']:>10,.1f} - ${r['range']['ev_high']:>,.1f}")
        print(f"{'=' * 55}\n")
    elif args.workflow == "credit":
        r = credit_full(args.revenue, args.ebitda, args.debt, args.equity, args.vol)
        print(f"\n{'=' * 55}")
        print("  Credit Analysis")
        print(f"{'=' * 55}")
        print(f"  Leverage:              {r['summary']['leverage']}x")
        print(f"  Interest Coverage:     {r['summary']['coverage']}x")
        print(f"  Default Probability:   {r['summary']['default_probability_pct']}%")
        m = r["merton"]
        print(f"  Distance to Default:   {m['distance_to_default']:.2f}")
        print(f"  Implied Spread:        {m['credit_spread_bps']:.0f} bps")
        print(f"{'=' * 55}\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
