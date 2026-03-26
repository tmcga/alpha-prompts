#!/usr/bin/env python3
"""Brinson-Fachler performance attribution — allocation, selection, interaction.

Usage:
    python brinson.py \
        --port-weights 0.30,0.25,0.20,0.15,0.10 \
        --port-returns 0.12,0.08,0.05,0.15,0.03 \
        --bench-weights 0.25,0.25,0.25,0.15,0.10 \
        --bench-returns 0.10,0.09,0.06,0.12,0.04 \
        --sectors Tech,Health,Finance,Energy,Utils
"""

import argparse


def brinson_attribution(
    port_weights: list[float],
    port_returns: list[float],
    bench_weights: list[float],
    bench_returns: list[float],
    sector_names: list[str] | None = None,
) -> dict:
    """Brinson-Fachler performance attribution.

    Decomposes active return into allocation, selection, and interaction effects
    for each sector/asset class.

    Args:
        port_weights: Portfolio weights per sector.
        port_returns: Portfolio returns per sector.
        bench_weights: Benchmark weights per sector.
        bench_returns: Benchmark returns per sector.
        sector_names: Optional labels for each sector.

    Returns:
        Dict with per-sector attribution and totals.
    """
    n = len(port_weights)
    if not (n == len(port_returns) == len(bench_weights) == len(bench_returns)):
        raise ValueError("All input lists must have the same length")

    port_weight_sum = sum(port_weights)
    bench_weight_sum = sum(bench_weights)
    if abs(port_weight_sum - 1.0) > 0.05:
        raise ValueError(f"Portfolio weights must sum to ~1.0, got {port_weight_sum:.3f}")
    if abs(bench_weight_sum - 1.0) > 0.05:
        raise ValueError(f"Benchmark weights must sum to ~1.0, got {bench_weight_sum:.3f}")
    weights_normalized = abs(port_weight_sum - 1.0) < 0.01 and abs(bench_weight_sum - 1.0) < 0.01

    if sector_names is None:
        sector_names = [f"Sector {i + 1}" for i in range(n)]

    # Total returns
    port_total = sum(w * r for w, r in zip(port_weights, port_returns))
    bench_total = sum(w * r for w, r in zip(bench_weights, bench_returns))
    active_return = port_total - bench_total

    # Per-sector attribution (Brinson-Fachler)
    sectors = []
    total_alloc = 0.0
    total_select = 0.0
    total_interact = 0.0

    for i in range(n):
        pw, pr = port_weights[i], port_returns[i]
        bw, br = bench_weights[i], bench_returns[i]

        # Allocation effect: over/underweight in sectors that outperform
        allocation = (pw - bw) * (br - bench_total)

        # Selection effect: stock picking within sector
        selection = bw * (pr - br)

        # Interaction effect: cross-term
        interaction = (pw - bw) * (pr - br)

        total_alloc += allocation
        total_select += selection
        total_interact += interaction

        sectors.append(
            {
                "name": sector_names[i],
                "port_weight": pw,
                "bench_weight": bw,
                "active_weight": pw - bw,
                "port_return": pr,
                "bench_return": br,
                "allocation": allocation,
                "selection": selection,
                "interaction": interaction,
                "total_effect": allocation + selection + interaction,
            }
        )

    return {
        "portfolio_return": port_total,
        "benchmark_return": bench_total,
        "active_return": active_return,
        "total_allocation": total_alloc,
        "total_selection": total_select,
        "total_interaction": total_interact,
        "weights_normalized": weights_normalized,
        "sectors": sectors,
    }


def main():
    parser = argparse.ArgumentParser(description="Brinson-Fachler Performance Attribution")
    parser.add_argument("--port-weights", required=True, help="Portfolio weights (comma-sep)")
    parser.add_argument("--port-returns", required=True, help="Portfolio returns (comma-sep)")
    parser.add_argument("--bench-weights", required=True, help="Benchmark weights (comma-sep)")
    parser.add_argument("--bench-returns", required=True, help="Benchmark returns (comma-sep)")
    parser.add_argument("--sectors", default=None, help="Sector names (comma-sep)")
    args = parser.parse_args()

    pw = [float(x.strip()) for x in args.port_weights.split(",")]
    pr = [float(x.strip()) for x in args.port_returns.split(",")]
    bw = [float(x.strip()) for x in args.bench_weights.split(",")]
    br = [float(x.strip()) for x in args.bench_returns.split(",")]
    names = args.sectors.split(",") if args.sectors else None

    r = brinson_attribution(pw, pr, bw, br, names)

    print(f"\n{'=' * 70}")
    print("  Brinson-Fachler Performance Attribution")
    print(f"{'=' * 70}")
    print(f"  Portfolio Return:   {r['portfolio_return'] * 100:>+8.2f}%")
    print(f"  Benchmark Return:   {r['benchmark_return'] * 100:>+8.2f}%")
    print(f"  Active Return:      {r['active_return'] * 100:>+8.2f}%")
    print(f"{'─' * 70}")

    # Header
    print(
        f"  {'Sector':<12} {'Wt(P)':>6} {'Wt(B)':>6} {'Ret(P)':>7} {'Ret(B)':>7}"
        f" {'Alloc':>7} {'Select':>7} {'Inter':>7} {'Total':>7}"
    )
    print(f"  {'─' * 12} {'─' * 6} {'─' * 6} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7}")

    for s in r["sectors"]:
        print(
            f"  {s['name']:<12} {s['port_weight'] * 100:>5.1f}% {s['bench_weight'] * 100:>5.1f}%"
            f" {s['port_return'] * 100:>+6.1f}% {s['bench_return'] * 100:>+6.1f}%"
            f" {s['allocation'] * 100:>+6.2f}% {s['selection'] * 100:>+6.2f}%"
            f" {s['interaction'] * 100:>+6.2f}% {s['total_effect'] * 100:>+6.2f}%"
        )

    print(f"  {'─' * 12} {'─' * 6} {'─' * 6} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7} {'─' * 7}")
    print(
        f"  {'TOTAL':<12} {'':>6} {'':>6} {'':>7} {'':>7}"
        f" {r['total_allocation'] * 100:>+6.2f}% {r['total_selection'] * 100:>+6.2f}%"
        f" {r['total_interaction'] * 100:>+6.2f}% {r['active_return'] * 100:>+6.2f}%"
    )
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    main()
