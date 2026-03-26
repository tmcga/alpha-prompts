"""Test suite for all 19 Alpha Stack finance tools (23 functions)."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

from dcf import dcf_valuation
from lbo import lbo_returns
from wacc import wacc
from black_scholes import black_scholes
from implied_vol import implied_volatility
from convertible import convertible_bond
from bond_yield import bond_analytics
from merton_model import merton_model
from credit_spread import altman_zscore, credit_from_spread
from portfolio_risk import portfolio_metrics, benchmark_relative
from kelly import kelly_criterion, multi_outcome_kelly
from brinson import brinson_attribution
from black_litterman import black_litterman
from monte_carlo import monte_carlo_sim
from merger_arb import merger_arb
from cap_rate import real_estate_valuation
from vc_returns import fund_metrics, dilution_waterfall
from loan_amort import loan_amortization
from market_maker import optimal_quotes


# ── DCF ────────────────────────────────────────────────────────────────────


class TestDCF:
    def test_gordon_growth(self):
        r = dcf_valuation([100, 110, 121], wacc=0.10, terminal_growth=0.025)
        assert r["enterprise_value"] > 0
        assert r["tv_method"] == "gordon_growth"
        assert 0 < r["terminal_value_pct"] < 100

    def test_exit_multiple(self):
        r = dcf_valuation([100, 110, 121], wacc=0.10, exit_multiple=12)
        assert r["enterprise_value"] > 0
        assert r["tv_method"] == "exit_multiple"

    def test_equity_value(self):
        r = dcf_valuation([100], wacc=0.10, terminal_growth=0.025, net_debt=500, shares=100)
        assert r["equity_value"] == r["enterprise_value"] - 500
        assert r["price_per_share"] == r["equity_value"] / 100

    def test_wacc_must_exceed_growth(self):
        with pytest.raises(ValueError):
            dcf_valuation([100], wacc=0.02, terminal_growth=0.03)


# ── LBO ────────────────────────────────────────────────────────────────────


class TestLBO:
    def test_basic(self):
        r = lbo_returns(100, 10, 10, 5, 0.06, 0.05, 5)
        assert r["moic"] > 0
        assert r["irr"] > 0
        assert r["entry_equity"] == 100 * 10 - 100 * 5

    def test_detailed_fcf(self):
        r = lbo_returns(100, 10, 11, 5, 0.06, 0.08, 5, tax_rate=0.25, capex_pct=0.08)
        assert r["moic"] > 0

    def test_attribution_components(self):
        r = lbo_returns(100, 10, 11, 5, 0.06, 0.05, 5)
        a = r["attribution"]
        # All three attribution components should be present and non-zero
        assert a["ebitda_growth"] > 0
        assert a["multiple_change"] > 0
        assert a["deleveraging"] > 0


# ── WACC ───────────────────────────────────────────────────────────────────


class TestWACC:
    def test_basic(self):
        r = wacc(1000, 500, 0.25, 0.04, 1.2, 0.055, 0.05)
        assert 0 < r["wacc"] < 0.20
        assert abs(r["weight_equity"] + r["weight_debt"] - 1.0) < 1e-10

    def test_size_premium(self):
        r1 = wacc(1000, 500, 0.25, 0.04, 1.2, 0.055, 0.05)
        r2 = wacc(1000, 500, 0.25, 0.04, 1.2, 0.055, 0.05, size_premium=0.02)
        assert r2["cost_of_equity"] > r1["cost_of_equity"]


# ── Black-Scholes ──────────────────────────────────────────────────────────


class TestBlackScholes:
    def test_call(self):
        r = black_scholes(100, 105, 0.5, 0.05, 0.2)
        assert r["price"] > 0
        assert 0 < r["delta"] < 1
        assert r["put_call_parity_check"]

    def test_put(self):
        r = black_scholes(100, 95, 0.5, 0.05, 0.2, "put")
        assert r["price"] > 0
        assert -1 < r["delta"] < 0

    def test_case_insensitive(self):
        r = black_scholes(100, 105, 0.5, 0.05, 0.2, "CALL")
        assert r["price"] > 0

    def test_at_expiry(self):
        r = black_scholes(110, 105, 0, 0.05, 0.2)
        assert r["price"] == 5

    def test_dividend_reduces_call(self):
        r1 = black_scholes(100, 100, 1, 0.05, 0.2, div_yield=0.0)
        r2 = black_scholes(100, 100, 1, 0.05, 0.2, div_yield=0.03)
        assert r2["price"] < r1["price"]

    def test_greeks_exist(self):
        r = black_scholes(100, 100, 0.5, 0.05, 0.2)
        for key in ["delta", "gamma", "vega", "theta", "rho", "vanna", "charm"]:
            assert key in r


# ── Implied Volatility ─────────────────────────────────────────────────────


class TestImpliedVol:
    def test_roundtrip(self):
        """Price with BS, then recover the vol."""
        bs = black_scholes(100, 105, 0.5, 0.05, 0.20)
        iv = implied_volatility(bs["price"], 100, 105, 0.5, 0.05)
        assert abs(iv["implied_vol"] - 0.20) < 0.001

    def test_moneyness(self):
        r = implied_volatility(5.0, 100, 110, 0.5, 0.05)
        assert abs(r["moneyness"] - 100 / 110) < 1e-6


# ── Convertible Bond ──────────────────────────────────────────────────────


class TestConvertible:
    def test_basic(self):
        r = convertible_bond(1000, 0.02, 5, 0.03, 50, 15, 0.30, 0.04)
        assert r["bond_floor"] > 0
        assert r["parity"] == 50 * 15
        assert r["theoretical_value"] > r["bond_floor"]

    def test_profile_classification(self):
        r = convertible_bond(1000, 0.02, 5, 0.03, 50, 15, 0.30, 0.04)
        assert r["profile"] in ["Equity-like", "Balanced", "Busted (bond-like)"]


# ── Bond Analytics ─────────────────────────────────────────────────────────


class TestBondYield:
    def test_par_bond(self):
        r = bond_analytics(1000, 0.05, 1000, 10)
        assert abs(r["ytm"] - 0.05) < 0.001

    def test_discount_bond(self):
        r = bond_analytics(1000, 0.05, 980, 10)
        assert r["ytm"] > 0.05

    def test_spread(self):
        r = bond_analytics(1000, 0.05, 980, 10, benchmark_yield=0.04)
        assert r["g_spread"] is not None
        assert r["z_spread"] is not None
        assert r["g_spread"] > 0


# ── Merton Model ──────────────────────────────────────────────────────────


class TestMerton:
    def test_basic(self):
        r = merton_model(1000, 600, 0.25, 0.04, 5)
        assert 0 < r["default_probability"] < 1
        assert r["equity_value"] > 0
        assert r["equity_value"] + r["debt_value"] == pytest.approx(1000, rel=1e-6)

    def test_high_leverage_more_risk(self):
        r1 = merton_model(1000, 300, 0.25, 0.04, 5)
        r2 = merton_model(1000, 800, 0.25, 0.04, 5)
        assert r2["default_probability"] > r1["default_probability"]


# ── Credit Spread ──────────────────────────────────────────────────────────


class TestCreditSpread:
    def test_zscore_safe(self):
        r = altman_zscore(0.3, 0.4, 0.3, 2.0, 1.5)
        assert r["zone"] == "Safe"

    def test_zscore_distress(self):
        r = altman_zscore(-0.1, -0.2, 0.02, 0.3, 0.5)
        assert r["zone"] == "Distress"

    def test_credit_from_spread(self):
        r = credit_from_spread(0.03, 0.40, 5)
        assert r["hazard_rate"] == pytest.approx(0.05, rel=1e-6)
        assert r["annual_default_prob"] > 0
        assert r["survival_probability"] > 0
        assert len(r["cumulative_default_probs"]) == 5


# ── Portfolio Risk ─────────────────────────────────────────────────────────


class TestPortfolioRisk:
    returns = [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.01, -0.03, 0.02, 0.01]

    def test_basic(self):
        r = portfolio_metrics(self.returns, 0.04)
        assert "ann_return" in r
        assert "sharpe" in r
        assert r["max_drawdown"] <= 0
        assert r["num_periods"] == 10

    def test_win_rate(self):
        r = portfolio_metrics(self.returns)
        assert r["win_rate"] == 0.7

    def test_benchmark_relative(self):
        bench = [0.01, 0.00, 0.02, 0.01, -0.01, 0.03, 0.01, -0.02, 0.01, 0.01]
        r = benchmark_relative(self.returns, bench)
        assert "tracking_error" in r
        assert "information_ratio" in r


# ── Kelly Criterion ────────────────────────────────────────────────────────


class TestKelly:
    def test_positive_edge(self):
        r = kelly_criterion(0.55, 1.5)
        assert r["full_kelly"] > 0
        assert r["edge"] > 0

    def test_no_edge(self):
        r = kelly_criterion(0.40, 1.0)
        assert r["full_kelly"] <= 0

    def test_half_kelly(self):
        r = kelly_criterion(0.55, 1.5, fraction=0.5)
        assert r["applied_fraction"] == pytest.approx(r["full_kelly"] * 0.5)

    def test_multi_outcome(self):
        r = multi_outcome_kelly([(0.5, 2.0), (0.5, -1.0)])
        assert r["optimal_fraction"] > 0
        assert r["geometric_growth_rate"] > 0


# ── Brinson Attribution ───────────────────────────────────────────────────


class TestBrinson:
    def test_attribution_sums(self):
        r = brinson_attribution(
            [0.5, 0.5],
            [0.10, 0.05],
            [0.5, 0.5],
            [0.08, 0.06],
        )
        total = r["total_allocation"] + r["total_selection"] + r["total_interaction"]
        assert abs(total - r["active_return"]) < 1e-10

    def test_sector_names(self):
        r = brinson_attribution(
            [0.5, 0.5],
            [0.10, 0.05],
            [0.5, 0.5],
            [0.08, 0.06],
            sector_names=["Tech", "Health"],
        )
        assert r["sectors"][0]["name"] == "Tech"


# ── Black-Litterman ──────────────────────────────────────────────────────


class TestBlackLitterman:
    def test_no_views(self):
        r = black_litterman([0.6, 0.4], [[0.04, 0.01], [0.01, 0.03]], 2.5, 0.05)
        assert len(r["equilibrium_returns"]) == 2
        assert r["optimal_weights"] == pytest.approx([0.6, 0.4], abs=0.01)

    def test_with_views(self):
        r = black_litterman(
            [0.6, 0.4],
            [[0.04, 0.01], [0.01, 0.03]],
            2.5,
            0.05,
            P=[[1, -1]],
            Q=[0.02],
        )
        # View says asset 1 outperforms asset 2 by 2%
        assert r["posterior_returns"][0] > r["posterior_returns"][1]


# ── Monte Carlo ───────────────────────────────────────────────────────────


class TestMonteCarlo:
    def test_basic(self):
        r = monte_carlo_sim(1000000, 0.07, 0.15, 10, num_sims=1000, seed=42)
        assert r["mean_terminal"] > 0
        assert r["percentile_5"] < r["percentile_50"] < r["percentile_95"]

    def test_ruin_with_high_withdrawal(self):
        r = monte_carlo_sim(100000, 0.05, 0.20, 30, num_sims=1000, withdrawal_rate=0.15, seed=42)
        assert r["ruin_probability"] > 0

    def test_goal_probability(self):
        r = monte_carlo_sim(1000000, 0.07, 0.15, 10, num_sims=1000, goal=1500000, seed=42)
        assert r["success_probability"] is not None
        assert 0 <= r["success_probability"] <= 1


# ── Merger Arb ────────────────────────────────────────────────────────────


class TestMergerArb:
    def test_cash_deal(self):
        r = merger_arb(45, 50, 90)
        assert r["gross_spread"] > 0
        assert r["annualized_spread"] > r["gross_spread"]
        assert 0 < r["implied_probability"] < 1

    def test_cvr(self):
        r1 = merger_arb(45, 50, 90)
        r2 = merger_arb(45, 50, 90, cvr_value=5, cvr_prob=0.6)
        assert r2["gross_spread"] > r1["gross_spread"]
        assert r2["cvr_expected_value"] == 3.0


# ── Real Estate ───────────────────────────────────────────────────────────


class TestCapRate:
    def test_value_from_cap_rate(self):
        r = real_estate_valuation(5000000, cap_rate=0.05)
        assert r["property_value"] == 100000000

    def test_cap_rate_from_value(self):
        r = real_estate_valuation(5000000, property_value=100000000)
        assert r["cap_rate"] == pytest.approx(0.05)

    def test_development_spread(self):
        r = real_estate_valuation(5000000, cap_rate=0.05, dev_cost=80000000)
        assert r["yield_on_cost"] is not None
        assert r["development_spread"] > 0


# ── VC Returns ────────────────────────────────────────────────────────────


class TestVCReturns:
    def test_fund_metrics(self):
        r = fund_metrics([10, 10, 10], [0, 0, 5], 30, 3)
        assert r["tvpi"] == pytest.approx((5 + 30) / 30, rel=0.01)
        assert r["dpi"] == pytest.approx(5 / 30, rel=0.01)

    def test_dilution(self):
        rounds = [
            {"invested": 5e6, "pre_money": 20e6, "pool_increase": 0.10},
            {"invested": 10e6, "pre_money": 80e6},
        ]
        r = dilution_waterfall(rounds, 8000000)
        assert r["final_founder_ownership"] < 1.0
        assert len(r["rounds"]) == 2
        # Ownership decreases each round
        assert r["rounds"][1]["founder_ownership"] < r["rounds"][0]["founder_ownership"]


# ── Loan Amortization ────────────────────────────────────────────────────


class TestLoanAmort:
    def test_basic(self):
        r = loan_amortization(500000, 0.065, 30)
        assert r["monthly_payment"] > 0
        assert r["total_interest"] > 0
        assert r["total_cost"] == pytest.approx(r["principal"] + r["total_interest"])

    def test_extra_payment_saves(self):
        r1 = loan_amortization(500000, 0.065, 30)
        r2 = loan_amortization(500000, 0.065, 30, extra_payment=500)
        assert r2["total_interest"] < r1["total_interest"]
        assert r2["interest_saved"] > 0
        assert r2["months_saved"] > 0


# ── Market Maker ──────────────────────────────────────────────────────────


class TestMarketMaker:
    def test_zero_inventory(self):
        r = optimal_quotes(100, 0, 0.01, 0.02, 1.0, 1.5)
        # With zero inventory, reservation price should equal mid
        assert r["reservation_price"] == pytest.approx(100, abs=0.01)
        assert r["optimal_spread"] > 0
        assert r["bid_price"] < r["ask_price"]

    def test_long_inventory_lowers_reservation(self):
        r = optimal_quotes(100, 100, 0.1, 0.02, 1.0, 1.5)
        assert r["reservation_price"] < 100

    def test_short_inventory_raises_reservation(self):
        r = optimal_quotes(100, -100, 0.1, 0.02, 1.0, 1.5)
        assert r["reservation_price"] > 100
