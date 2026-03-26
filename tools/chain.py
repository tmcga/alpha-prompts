#!/usr/bin/env python3
"""Chained tool workflows — multi-tool analyses in a single call.

Usage: python chain.py --valuation --fcf 100,110,121 --wacc 0.10 --tg 0.025 --lbo-ebitda 100 --entry 10 --exit 11 --leverage 5 --rate 0.06 --growth 0.08
       python chain.py --credit --revenue 680 --ebitda 102 --debt 820 --equity 200 --vol 0.35
"""

import argparse
from dcf import dcf_valuation
from lbo import lbo_returns
from credit_spread import altman_zscore
from merton_model import merton_model
from portfolio_risk import portfolio_metrics, benchmark_relative
from kelly import kelly_criterion


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
    dcf = dcf_valuation(fcfs, wacc_rate, terminal_growth=terminal_growth, net_debt=net_debt, shares=shares)
    result = {
        "dcf": {
            "enterprise_value": dcf["enterprise_value"],
            "equity_value": dcf["equity_value"],
            "price_per_share": dcf["price_per_share"],
            "terminal_value_pct": dcf["terminal_value_pct"],
        },
    }
    ev_low = dcf["enterprise_value"] * 0.85
    ev_high = dcf["enterprise_value"] * 1.15
    if lbo_ebitda and entry_multiple and exit_multiple:
        lbo = lbo_returns(lbo_ebitda, entry_multiple, exit_multiple, leverage, debt_rate, ebitda_growth, years)
        result["lbo"] = {
            "entry_ev": lbo["entry_ev"],
            "exit_ev": lbo["exit_ev"],
            "moic": lbo["moic"],
            "irr": lbo["irr"],
        }
        ev_low = min(ev_low, lbo["entry_ev"] * 0.9)
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
        Dict with Z-Score analysis and Merton default probability.
    """
    result = {}
    if current_assets is not None and current_liabilities is not None and retained_earnings is not None:
        zscore = altman_zscore(
            current_assets=current_assets,
            current_liabilities=current_liabilities,
            total_assets=equity_value + total_debt,
            retained_earnings=retained_earnings,
            ebit=ebitda * 0.85,
            market_equity=equity_value,
            total_liabilities=total_debt,
            revenue=revenue,
        )
        result["zscore"] = zscore
    asset_value = equity_value + total_debt
    merton = merton_model(asset_value, total_debt, risk_free, maturity, asset_vol)
    result["merton"] = {
        "default_probability": merton["default_probability"],
        "distance_to_default": merton["distance_to_default"],
        "equity_value": merton["equity_value"],
        "credit_spread_bps": merton["credit_spread_bps"],
    }
    result["summary"] = {
        "leverage": round(total_debt / ebitda, 1) if ebitda > 0 else None,
        "coverage": round(ebitda / (total_debt * 0.06), 1) if total_debt > 0 else None,
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
