#!/usr/bin/env python3
"""Alpha Stack MCP Server — 23 finance tools for Claude Desktop.

Exposes all Alpha Stack computational tools as MCP tools that Claude Desktop
can invoke directly through natural language conversation.
"""

import json
import os
import sys
import traceback

# Add tools/ to import path (preserves standalone CLI usage of each tool)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))

from mcp.server.fastmcp import FastMCP

# Import all tool functions
from dcf import dcf_valuation
from lbo import lbo_returns
from wacc import wacc as wacc_calc
from black_scholes import black_scholes as bs_calc
from implied_vol import implied_volatility as iv_calc
from convertible import convertible_bond as cb_calc
from bond_yield import bond_analytics as bond_calc
from merton_model import merton_model as merton_calc
from credit_spread import altman_zscore, credit_from_spread
from portfolio_risk import portfolio_metrics, benchmark_relative
from kelly import kelly_criterion, multi_outcome_kelly
from brinson import brinson_attribution
from black_litterman import black_litterman as bl_calc
from monte_carlo import monte_carlo_sim
from merger_arb import merger_arb as ma_calc
from cap_rate import real_estate_valuation
from vc_returns import fund_metrics, dilution_waterfall
from loan_amort import loan_amortization
from market_maker import optimal_quotes

mcp = FastMCP("alpha-stack")


def _fmt(result: dict) -> str:
    return json.dumps(result, indent=2, default=str)


def _safe_call(fn, *args, **kwargs) -> str:
    try:
        return _fmt(fn(*args, **kwargs))
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return f"Error: {type(e).__name__}: {e}"


# ── Valuation & Corporate Finance ──────────────────────────────────────────


@mcp.tool(name="dcf_valuation")
async def _dcf(
    fcfs: list[float],
    wacc: float,
    terminal_growth: float | None = None,
    exit_multiple: float | None = None,
    net_debt: float = 0,
    shares: float = 1,
) -> str:
    """DCF valuation with Gordon Growth or exit multiple terminal value.

    Args:
        fcfs: Projected free cash flows for each year (e.g. [100, 110, 121])
        wacc: Weighted average cost of capital (e.g. 0.10 for 10%)
        terminal_growth: Perpetual growth rate for Gordon Growth method
        exit_multiple: Exit EV/FCF multiple (alternative to terminal_growth)
        net_debt: Net debt subtracted from enterprise value (default 0)
        shares: Shares outstanding for per-share price (default 1)
    """
    return _safe_call(dcf_valuation, fcfs, wacc, terminal_growth, exit_multiple, net_debt, shares)


@mcp.tool(name="lbo_returns")
async def _lbo(
    ebitda: float,
    entry_multiple: float,
    exit_multiple: float,
    leverage: float,
    interest_rate: float,
    ebitda_growth: float,
    years: int,
    amortization_pct: float = 0.01,
    tax_rate: float | None = None,
    capex_pct: float | None = None,
    nwc_pct: float | None = None,
    da_pct: float | None = None,
) -> str:
    """LBO returns calculator — MOIC, IRR, and returns attribution.

    Args:
        ebitda: Entry EBITDA
        entry_multiple: Entry EV/EBITDA multiple
        exit_multiple: Exit EV/EBITDA multiple
        leverage: Entry Debt/EBITDA ratio
        interest_rate: Blended interest rate on debt
        ebitda_growth: Annual EBITDA growth rate
        years: Hold period in years
        amortization_pct: Annual mandatory debt amortization as pct of initial debt
        tax_rate: Corporate tax rate (enables detailed FCF build)
        capex_pct: CapEx as pct of EBITDA (default 10% when tax_rate provided)
        nwc_pct: NWC change as pct of EBITDA growth (default 5% when tax_rate provided)
        da_pct: D&A as pct of EBITDA (default 10% when tax_rate provided)
    """
    return _safe_call(
        lbo_returns,
        ebitda,
        entry_multiple,
        exit_multiple,
        leverage,
        interest_rate,
        ebitda_growth,
        years,
        amortization_pct,
        tax_rate,
        capex_pct,
        nwc_pct,
        da_pct,
    )


@mcp.tool(name="wacc")
async def _wacc(
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
) -> str:
    """WACC calculator with CAPM build-up for cost of equity.

    Args:
        equity_value: Market value of equity
        debt_value: Market value of debt
        tax_rate: Marginal corporate tax rate
        risk_free: Risk-free rate (e.g. 10Y Treasury yield)
        beta: Levered equity beta
        equity_risk_premium: Equity risk premium
        cost_of_debt: Pre-tax cost of debt
        size_premium: Small-cap size premium (default 0)
        country_risk: Country risk premium (default 0)
        alpha: Company-specific alpha (default 0)
    """
    return _safe_call(
        wacc_calc,
        equity_value,
        debt_value,
        tax_rate,
        risk_free,
        beta,
        equity_risk_premium,
        cost_of_debt,
        size_premium,
        country_risk,
        alpha,
    )


# ── Options & Derivatives ──────────────────────────────────────────────────


@mcp.tool(name="black_scholes")
async def _bs(
    spot: float,
    strike: float,
    time: float,
    rate: float,
    vol: float,
    option_type: str = "call",
    div_yield: float = 0.0,
) -> str:
    """Black-Scholes options pricing with full Greeks (delta, gamma, vega, theta, rho, vanna, charm).

    Args:
        spot: Current underlying price
        strike: Strike price
        time: Time to expiration in years
        rate: Risk-free interest rate
        vol: Annualized volatility (e.g. 0.20 for 20%)
        option_type: "call" or "put"
        div_yield: Continuous dividend yield (default 0)
    """
    return _safe_call(bs_calc, spot, strike, time, rate, vol, option_type, div_yield)


@mcp.tool(name="implied_volatility")
async def _iv(
    market_price: float,
    spot: float,
    strike: float,
    time: float,
    rate: float,
    option_type: str = "call",
) -> str:
    """Solve for implied volatility from a market option price.

    Args:
        market_price: Observed market option price
        spot: Current underlying price
        strike: Strike price
        time: Time to expiration in years
        rate: Risk-free interest rate
        option_type: "call" or "put"
    """
    return _safe_call(iv_calc, market_price, spot, strike, time, rate, option_type)


@mcp.tool(name="convertible_bond")
async def _cb(
    face: float,
    coupon_rate: float,
    maturity: float,
    credit_spread: float,
    stock_price: float,
    conversion_ratio: float,
    stock_vol: float,
    risk_free: float,
) -> str:
    """Price a convertible bond — bond floor, parity, embedded option, conversion premium.

    Args:
        face: Face/par value (e.g. 1000)
        coupon_rate: Annual coupon rate
        maturity: Years to maturity
        credit_spread: Credit spread over risk-free for bond floor
        stock_price: Current underlying stock price
        conversion_ratio: Number of shares per bond
        stock_vol: Stock volatility (annualized)
        risk_free: Risk-free rate
    """
    return _safe_call(
        cb_calc, face, coupon_rate, maturity, credit_spread, stock_price, conversion_ratio, stock_vol, risk_free
    )


# ── Fixed Income & Credit ──────────────────────────────────────────────────


@mcp.tool(name="bond_analytics")
async def _bond(
    face: float,
    coupon_rate: float,
    price: float,
    years: float,
    freq: int = 2,
    benchmark_yield: float | None = None,
) -> str:
    """Bond analytics — YTM, duration (Macaulay & modified), convexity, DV01, G/Z-spread.

    Args:
        face: Face/par value (e.g. 1000)
        coupon_rate: Annual coupon rate
        price: Current market price
        years: Years to maturity
        freq: Coupon payments per year (default 2 for semi-annual)
        benchmark_yield: Benchmark yield for spread calculation (optional)
    """
    return _safe_call(bond_calc, face, coupon_rate, price, years, freq, benchmark_yield)


@mcp.tool(name="merton_model")
async def _merton(
    asset_value: float,
    debt_face: float,
    asset_vol: float,
    risk_free: float,
    maturity: float,
) -> str:
    """Merton structural credit model — distance to default, default probability, credit spread.

    Args:
        asset_value: Current market value of firm assets
        debt_face: Face value of debt (default barrier)
        asset_vol: Annualized asset volatility
        risk_free: Risk-free rate
        maturity: Time to debt maturity in years
    """
    return _safe_call(merton_calc, asset_value, debt_face, asset_vol, risk_free, maturity)


@mcp.tool(name="altman_zscore")
async def _zscore(
    wc_ta: float,
    re_ta: float,
    ebit_ta: float,
    equity_debt: float,
    sales_ta: float,
) -> str:
    """Altman Z-Score bankruptcy prediction (Safe / Grey / Distress zones).

    Args:
        wc_ta: Working Capital / Total Assets
        re_ta: Retained Earnings / Total Assets
        ebit_ta: EBIT / Total Assets
        equity_debt: Market Value of Equity / Book Value of Total Debt
        sales_ta: Sales / Total Assets
    """
    return _safe_call(altman_zscore, wc_ta, re_ta, ebit_ta, equity_debt, sales_ta)


@mcp.tool(name="credit_from_spread")
async def _credit(
    cds_spread: float,
    recovery_rate: float = 0.40,
    maturity: float = 5.0,
) -> str:
    """Derive default probabilities from CDS/credit spread — hazard rate, cumulative PD, expected loss.

    Args:
        cds_spread: Annual CDS spread (e.g. 0.03 for 300bps)
        recovery_rate: Expected recovery rate (default 40%)
        maturity: Time horizon in years (default 5)
    """
    return _safe_call(credit_from_spread, cds_spread, recovery_rate, maturity)


# ── Portfolio & Risk ───────────────────────────────────────────────────────


@mcp.tool(name="portfolio_metrics")
async def _port(
    returns: list[float],
    risk_free: float = 0.0,
    periods_per_year: int = 12,
) -> str:
    """Portfolio risk metrics — Sharpe, Sortino, Calmar, max drawdown, VaR, CVaR.

    Args:
        returns: List of periodic returns (e.g. monthly: [0.02, -0.01, 0.03, ...])
        risk_free: Annual risk-free rate (default 0)
        periods_per_year: 12 for monthly, 252 for daily (default 12)
    """
    return _safe_call(portfolio_metrics, returns, risk_free, periods_per_year)


@mcp.tool(name="benchmark_relative")
async def _bench(
    returns: list[float],
    benchmark: list[float],
    periods_per_year: int = 12,
) -> str:
    """Benchmark-relative metrics — tracking error, information ratio, active return.

    Args:
        returns: Portfolio periodic returns
        benchmark: Benchmark periodic returns (same length)
        periods_per_year: 12 for monthly, 252 for daily (default 12)
    """
    return _safe_call(benchmark_relative, returns, benchmark, periods_per_year)


@mcp.tool(name="kelly_criterion")
async def _kelly(
    win_prob: float,
    win_loss_ratio: float,
    fraction: float = 1.0,
) -> str:
    """Kelly Criterion position sizer — optimal bet fraction, geometric growth rate, drawdown risk.

    Args:
        win_prob: Probability of winning (0-1)
        win_loss_ratio: Ratio of average win to average loss
        fraction: Kelly fraction to apply (0.25=quarter, 0.5=half, 1.0=full)
    """
    return _safe_call(kelly_criterion, win_prob, win_loss_ratio, fraction)


@mcp.tool(name="multi_outcome_kelly")
async def _multi_kelly(
    outcomes: list[list[float]],
) -> str:
    """Kelly Criterion for multiple discrete outcomes — optimal fraction via ternary search.

    Args:
        outcomes: List of [probability, payoff] pairs. Probabilities must sum to 1.0.
                  Payoff is per $1 bet: 2.0 means you get $2 back, -1.0 means total loss.
                  Example: [[0.4, 2.0], [0.35, 0.5], [0.25, -1.0]]
    """
    tuples = [(p, r) for p, r in outcomes]
    return _safe_call(multi_outcome_kelly, tuples)


@mcp.tool(name="brinson_attribution")
async def _brinson(
    port_weights: list[float],
    port_returns: list[float],
    bench_weights: list[float],
    bench_returns: list[float],
    sector_names: list[str] | None = None,
) -> str:
    """Brinson-Fachler performance attribution — allocation, selection, interaction effects.

    Args:
        port_weights: Portfolio weights per sector
        port_returns: Portfolio returns per sector
        bench_weights: Benchmark weights per sector
        bench_returns: Benchmark returns per sector
        sector_names: Sector labels (optional)
    """
    return _safe_call(brinson_attribution, port_weights, port_returns, bench_weights, bench_returns, sector_names)


@mcp.tool(name="black_litterman")
async def _bl(
    market_weights: list[float],
    cov_matrix: list[list[float]],
    risk_aversion: float,
    tau: float,
    P: list[list[float]] | None = None,
    Q: list[float] | None = None,
    asset_names: list[str] | None = None,
) -> str:
    """Black-Litterman portfolio optimizer — equilibrium returns blended with investor views.

    Args:
        market_weights: Market capitalization weights per asset
        cov_matrix: Covariance matrix (NxN nested list)
        risk_aversion: Risk aversion parameter (typically 2-3)
        tau: Uncertainty scaling parameter (typically 0.025-0.05)
        P: Views pick matrix (KxN). Each row is a view portfolio (optional)
        Q: View return expectations (K-vector) (optional)
        asset_names: Asset labels (optional)
    """
    return _safe_call(bl_calc, market_weights, cov_matrix, risk_aversion, tau, P, Q, asset_names=asset_names)


@mcp.tool(name="monte_carlo_sim")
async def _mc(
    initial: float,
    expected_return: float,
    volatility: float,
    years: int,
    num_sims: int = 10000,
    withdrawal_rate: float = 0.0,
    contribution: float = 0.0,
    goal: float = 0.0,
) -> str:
    """Monte Carlo portfolio simulation — terminal value distribution, success/ruin probability.

    Args:
        initial: Starting portfolio value
        expected_return: Expected annual return
        volatility: Annual volatility
        years: Investment horizon in years
        num_sims: Number of simulation paths (default 10000)
        withdrawal_rate: Annual withdrawal as fraction of initial (default 0)
        contribution: Annual contribution amount (default 0)
        goal: Target ending value for success probability (default 0)
    """
    return _safe_call(
        monte_carlo_sim, initial, expected_return, volatility, years, num_sims, withdrawal_rate, contribution, goal
    )


# ── M&A & Special Situations ──────────────────────────────────────────────


@mcp.tool(name="merger_arb")
async def _ma(
    current_price: float,
    offer_price: float,
    days_to_close: int,
    risk_free: float = 0.05,
    downside_price: float | None = None,
    cvr_value: float = 0.0,
    cvr_prob: float = 0.0,
) -> str:
    """Merger arb spread analysis — gross/annualized spread, implied deal probability, risk/reward.

    Args:
        current_price: Current target stock price
        offer_price: Offer price (cash deal) or implied offer (ratio * acquirer price)
        days_to_close: Expected days to deal close
        risk_free: Annual risk-free rate (default 5%)
        downside_price: Estimated price if deal breaks (default 80% of current)
        cvr_value: Contingent value right face value (default 0)
        cvr_prob: Probability CVR pays out (default 0)
    """
    return _safe_call(
        ma_calc, current_price, offer_price, days_to_close, risk_free, downside_price, cvr_value, cvr_prob
    )


# ── Real Estate, VC & Lending ──────────────────────────────────────────────


@mcp.tool(name="real_estate_valuation")
async def _re(
    noi: float,
    cap_rate: float | None = None,
    property_value: float | None = None,
    risk_free: float = 0.04,
    noi_growth: float = 0.02,
    dev_cost: float | None = None,
) -> str:
    """Real estate valuation — cap rate analysis, NOI-based pricing, development spread, sensitivity.

    Args:
        noi: Annual Net Operating Income
        cap_rate: Market cap rate (provide to solve for property value)
        property_value: Property value (provide to solve for cap rate)
        risk_free: Risk-free rate (default 4%)
        noi_growth: Expected NOI growth rate (default 2%)
        dev_cost: Total development cost for development spread analysis (optional)
    """
    return _safe_call(real_estate_valuation, noi, cap_rate, property_value, risk_free, noi_growth, dev_cost)


@mcp.tool(name="fund_metrics")
async def _fund(
    contributions: list[float],
    distributions: list[float],
    nav: float,
    years: float,
) -> str:
    """VC fund performance metrics — TVPI, DPI, RVPI, net IRR, J-curve.

    Args:
        contributions: Capital called per period
        distributions: Cash returned per period
        nav: Current net asset value (residual value)
        years: Fund age in years
    """
    return _safe_call(fund_metrics, contributions, distributions, nav, years)


@mcp.tool(name="dilution_waterfall")
async def _dilution(
    rounds: list[dict],
    founder_shares: int,
) -> str:
    """VC dilution waterfall — ownership evolution across funding rounds.

    Args:
        rounds: List of round dicts, each with keys: "invested" (amount), "pre_money" (valuation),
                and optional "pool_increase" (option pool expansion as decimal, e.g. 0.10 for 10%).
                Example: [{"invested": 5000000, "pre_money": 20000000, "pool_increase": 0.10}]
        founder_shares: Initial number of founder shares
    """
    return _safe_call(dilution_waterfall, rounds, founder_shares)


@mcp.tool(name="loan_amortization")
async def _loan(
    principal: float,
    annual_rate: float,
    years: int,
    extra_payment: float = 0.0,
) -> str:
    """Loan amortization — monthly payment, interest/principal split, early payoff savings.

    Args:
        principal: Loan principal amount
        annual_rate: Annual interest rate (e.g. 0.065 for 6.5%)
        years: Loan term in years
        extra_payment: Extra monthly payment toward principal (default 0)
    """
    return _safe_call(loan_amortization, principal, annual_rate, years, extra_payment)


# ── Quantitative Trading ───────────────────────────────────────────────────


@mcp.tool(name="optimal_quotes")
async def _mm(
    mid_price: float,
    inventory: int,
    risk_aversion: float,
    volatility: float,
    time_remaining: float,
    order_intensity: float,
) -> str:
    """Avellaneda-Stoikov optimal market making — reservation price, optimal spread, bid/ask quotes.

    Args:
        mid_price: Current mid/fair price
        inventory: Current inventory position (positive=long, negative=short)
        risk_aversion: Risk aversion parameter (gamma). Higher = tighter risk control
        volatility: Price volatility per unit time
        time_remaining: Time remaining in trading session (0-1)
        order_intensity: Order arrival rate (kappa). Higher = more aggressive quoting
    """
    return _safe_call(optimal_quotes, mid_price, inventory, risk_aversion, volatility, time_remaining, order_intensity)


if __name__ == "__main__":
    mcp.run(transport="stdio")
