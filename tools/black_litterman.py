#!/usr/bin/env python3
"""Black-Litterman portfolio optimizer — equilibrium returns with investor views.

Usage:
    python black_litterman.py \
        --weights 0.5,0.3,0.2 \
        --cov "0.04,0.01,0.005;0.01,0.03,0.008;0.005,0.008,0.02" \
        --views "1,0,-1" --view-returns 0.02 \
        --tau 0.05 --risk-aversion 2.5
"""

import argparse


# --- Minimal matrix operations (no numpy) ---


def mat_zeros(rows: int, cols: int) -> list[list[float]]:
    return [[0.0] * cols for _ in range(rows)]


def mat_mult(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, n, p = len(A), len(A[0]), len(B[0])
    C = mat_zeros(m, p)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def mat_add(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scale(A: list[list[float]], s: float) -> list[list[float]]:
    return [[A[i][j] * s for j in range(len(A[0]))] for i in range(len(A))]


def mat_transpose(A: list[list[float]]) -> list[list[float]]:
    m, n = len(A), len(A[0])
    return [[A[j][i] for j in range(m)] for i in range(n)]


def mat_inverse(A: list[list[float]]) -> list[list[float]]:
    """Gauss-Jordan matrix inverse."""
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[pivot] = M[pivot], M[col]
        div = M[col][col]
        if abs(div) < 1e-14:
            raise ValueError("Matrix is singular")
        M[col] = [x / div for x in M[col]]
        for row in range(n):
            if row != col:
                factor = M[row][col]
                M[row] = [M[row][j] - factor * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def vec_to_col(v: list[float]) -> list[list[float]]:
    return [[x] for x in v]


def col_to_vec(M: list[list[float]]) -> list[float]:
    return [row[0] for row in M]


# --- Black-Litterman ---


def black_litterman(
    market_weights: list[float],
    cov_matrix: list[list[float]],
    risk_aversion: float,
    tau: float,
    P: list[list[float]] | None = None,
    Q: list[float] | None = None,
    omega: list[list[float]] | None = None,
    asset_names: list[str] | None = None,
) -> dict:
    """Black-Litterman model: equilibrium returns blended with investor views."""
    n = len(market_weights)
    if asset_names is None:
        asset_names = [f"Asset {i + 1}" for i in range(n)]

    Sigma = cov_matrix
    w_mkt = vec_to_col(market_weights)
    # Implied equilibrium returns: Pi = delta * Sigma * w_mkt
    pi_col = mat_mult(mat_scale(Sigma, risk_aversion), w_mkt)
    pi = col_to_vec(pi_col)

    if P is not None and Q is not None:
        tau_Sigma = mat_scale(Sigma, tau)
        if omega is None:
            omega = mat_mult(mat_mult(P, tau_Sigma), mat_transpose(P))

        tau_Sigma_inv = mat_inverse(tau_Sigma)
        omega_inv = mat_inverse(omega)
        Pt = mat_transpose(P)
        left_inv = mat_inverse(mat_add(tau_Sigma_inv, mat_mult(mat_mult(Pt, omega_inv), P)))
        right_sum = mat_add(mat_mult(tau_Sigma_inv, vec_to_col(pi)), mat_mult(mat_mult(Pt, omega_inv), vec_to_col(Q)))
        posterior_col = mat_mult(left_inv, right_sum)
        posterior = col_to_vec(posterior_col)
        optimal_col = mat_mult(mat_inverse(mat_scale(Sigma, risk_aversion)), posterior_col)
        optimal_weights = col_to_vec(optimal_col)
    else:
        posterior = pi[:]
        optimal_weights = market_weights[:]

    total_w = sum(optimal_weights)
    normalized_weights = [w / total_w for w in optimal_weights] if abs(total_w) > 1e-10 else optimal_weights
    port_return = sum(w * r for w, r in zip(normalized_weights, posterior))
    port_var = 0
    for i in range(n):
        for j in range(n):
            port_var += normalized_weights[i] * normalized_weights[j] * Sigma[i][j]
    port_risk = port_var**0.5

    return {
        "equilibrium_returns": pi,
        "posterior_returns": posterior,
        "market_weights": market_weights,
        "optimal_weights": normalized_weights,
        "raw_weights": optimal_weights,
        "asset_names": asset_names,
        "portfolio_return": port_return,
        "portfolio_risk": port_risk,
        "risk_aversion": risk_aversion,
        "tau": tau,
    }


def main():
    parser = argparse.ArgumentParser(description="Black-Litterman Portfolio Optimizer")
    parser.add_argument("--weights", required=True, help="Market cap weights (comma-sep)")
    parser.add_argument("--cov", required=True, help="Covariance matrix (rows sep by ;)")
    parser.add_argument("--risk-aversion", type=float, default=2.5, help="Risk aversion (default: 2.5)")
    parser.add_argument("--tau", type=float, default=0.05, help="Tau parameter (default: 0.05)")
    parser.add_argument("--views", default=None, help="Views pick matrix rows (rows sep by ;)")
    parser.add_argument("--view-returns", default=None, help="View returns (comma-sep)")
    parser.add_argument("--assets", default=None, help="Asset names (comma-sep)")
    args = parser.parse_args()

    weights = [float(x.strip()) for x in args.weights.split(",")]
    cov = [[float(x.strip()) for x in row.split(",")] for row in args.cov.split(";")]
    names = args.assets.split(",") if args.assets else None

    P, Q = None, None
    if args.views and args.view_returns:
        P = [[float(x.strip()) for x in row.split(",")] for row in args.views.split(";")]
        Q = [float(x.strip()) for x in args.view_returns.split(",")]

    r = black_litterman(weights, cov, args.risk_aversion, args.tau, P, Q, asset_names=names)

    print(f"\n{'=' * 65}")
    print("  Black-Litterman Portfolio Optimization")
    print(f"{'=' * 65}")
    print(f"  Risk Aversion: {r['risk_aversion']:.2f}    Tau: {r['tau']:.3f}")
    print(f"{'─' * 65}")
    print(f"  {'Asset':<12} {'Mkt Wt':>7} {'Equil R':>8} {'BL R':>8} {'Opt Wt':>7} {'Delta':>7}")
    print(f"  {'─' * 12} {'─' * 7} {'─' * 8} {'─' * 8} {'─' * 7} {'─' * 7}")

    for i, name in enumerate(r["asset_names"]):
        mw = r["market_weights"][i]
        eq = r["equilibrium_returns"][i]
        bl = r["posterior_returns"][i]
        ow = r["optimal_weights"][i]
        delta = ow - mw
        print(
            f"  {name:<12} {mw * 100:>6.1f}% {eq * 100:>+7.2f}% {bl * 100:>+7.2f}% {ow * 100:>6.1f}% {delta * 100:>+6.1f}%"
        )

    print(f"{'─' * 65}")
    print(f"  Portfolio Expected Return: {r['portfolio_return'] * 100:>+.2f}%")
    print(f"  Portfolio Risk (Vol):      {r['portfolio_risk'] * 100:>.2f}%")
    print(f"{'=' * 65}\n")


if __name__ == "__main__":
    main()
