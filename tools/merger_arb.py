#!/usr/bin/env python3
"""Merger arbitrage spread calculator.

Usage:
    python merger_arb.py --current 45 --offer 50 --days 90 --type cash
    python merger_arb.py --current 45 --offer-ratio 0.5 --acquirer-price 110 --days 120 --type stock
"""

import argparse


def merger_arb(
    current_price: float,
    offer_price: float,
    days_to_close: int,
    risk_free: float = 0.05,
    downside_price: float | None = None,
    cvr_value: float = 0.0,
    cvr_prob: float = 0.0,
) -> dict:
    """Calculate merger arbitrage spread and implied probabilities.

    Args:
        current_price: Current target stock price.
        offer_price: Offer price (cash deal) or implied offer (stock deal).
        days_to_close: Expected days to deal close.
        risk_free: Annual risk-free rate for annualization.
        downside_price: Estimated price if deal breaks (default: 80% of current).
        cvr_value: Contingent value right face value (default: 0).
        cvr_prob: Probability CVR pays out (default: 0).

    Returns:
        Dict with gross/annualized spread, implied probability, and break-even.
    """
    if downside_price is None:
        downside_price = current_price * 0.80

    # Adjust offer for CVR expected value
    cvr_expected = cvr_value * cvr_prob
    effective_offer = offer_price + cvr_expected

    # Gross spread (using effective offer including CVR)
    gross_spread = (effective_offer - current_price) / current_price
    ann_factor = 365 / days_to_close if days_to_close > 0 else 1

    # Annualized spread
    annualized_spread = (1 + gross_spread) ** ann_factor - 1

    # Implied deal probability (given a required return)
    # E[return] = P(close) * upside + P(break) * downside
    upside = (effective_offer - current_price) / current_price
    downside = (downside_price - current_price) / current_price

    # Solve: required_return = p * upside + (1-p) * downside
    # => p = (required_return - downside) / (upside - downside)
    required_return = (1 + risk_free) ** (days_to_close / 365) - 1
    spread_range = upside - downside
    if abs(spread_range) < 1e-10:
        implied_probability = None
        breakeven_probability = None
    else:
        implied_probability = (required_return - downside) / spread_range
        implied_probability = max(0, min(1, implied_probability))
        # Break-even probability (where E[return] = 0)
        breakeven_probability = -downside / spread_range
        breakeven_probability = max(0, min(1, breakeven_probability))

    # Risk-reward ratio
    risk_reward = abs(upside / downside) if downside != 0 else float("inf")

    return {
        "gross_spread": gross_spread,
        "annualized_spread": annualized_spread,
        "implied_probability": implied_probability,
        "breakeven_probability": breakeven_probability,
        "upside_per_share": effective_offer - current_price,
        "downside_per_share": downside_price - current_price,
        "risk_reward": risk_reward,
        "days_to_close": days_to_close,
        "cvr_expected_value": cvr_expected,
        "effective_offer": effective_offer,
    }


def main():
    parser = argparse.ArgumentParser(description="Merger Arb Spread Calculator")
    parser.add_argument("--current", type=float, required=True, help="Current target price")
    parser.add_argument("--offer", type=float, default=None, help="Cash offer price")
    parser.add_argument("--offer-ratio", type=float, default=None, help="Stock exchange ratio")
    parser.add_argument("--acquirer-price", type=float, default=None, help="Acquirer price (stock deals)")
    parser.add_argument("--days", type=int, required=True, help="Expected days to close")
    parser.add_argument("--type", dest="deal_type", required=True, choices=["cash", "stock"])
    parser.add_argument("--rf", type=float, default=0.05, help="Risk-free rate (default: 0.05)")
    parser.add_argument("--downside", type=float, default=None, help="Break price (default: 80%% of current)")
    parser.add_argument("--collar-low", type=float, default=None, help="Collar floor price (stock deals)")
    parser.add_argument("--collar-high", type=float, default=None, help="Collar cap price (stock deals)")
    parser.add_argument("--cvr", type=float, default=0, help="CVR face value (default: 0)")
    parser.add_argument("--cvr-prob", type=float, default=0, help="CVR payout probability (default: 0)")
    args = parser.parse_args()

    if args.deal_type == "cash":
        if args.offer is None:
            parser.error("Cash deals require --offer")
        offer_price = args.offer
    else:
        if args.offer_ratio is None or args.acquirer_price is None:
            parser.error("Stock deals require --offer-ratio and --acquirer-price")
        # Collar adjustment: clamp effective exchange ratio
        acq = args.acquirer_price
        if args.collar_low is not None and acq < args.collar_low:
            offer_price = args.offer_ratio * args.collar_low
        elif args.collar_high is not None and acq > args.collar_high:
            offer_price = args.offer_ratio * args.collar_high
        else:
            offer_price = args.offer_ratio * acq

    r = merger_arb(args.current, offer_price, args.days, args.rf, args.downside, args.cvr, args.cvr_prob)

    print(f"\n{'=' * 50}")
    print(f"  Merger Arb Analysis ({args.deal_type.upper()} deal)")
    print(f"{'=' * 50}")
    print(f"  Current Price:       ${args.current:>10.2f}")
    print(f"  Offer Price:         ${offer_price:>10.2f}")
    if args.deal_type == "stock":
        print(f"  Exchange Ratio:      {args.offer_ratio:>10.4f}")
        print(f"  Acquirer Price:      ${args.acquirer_price:>10.2f}")
        if args.collar_low is not None:
            print(f"  Collar Floor:        ${args.collar_low:>10.2f}")
        if args.collar_high is not None:
            print(f"  Collar Cap:          ${args.collar_high:>10.2f}")
    if r["cvr_expected_value"] > 0:
        print(f"  CVR Expected Value:  ${r['cvr_expected_value']:>10.2f}")
        print(f"  Effective Offer:     ${r['effective_offer']:>10.2f}")
    print(f"  Days to Close:       {r['days_to_close']:>10d}")
    print(f"{'─' * 50}")
    print(f"  Gross Spread:        {r['gross_spread'] * 100:>+10.2f}%")
    print(f"  Annualized Spread:   {r['annualized_spread'] * 100:>+10.2f}%")
    print(f"{'─' * 50}")
    print(f"  Upside (if close):   ${r['upside_per_share']:>+10.2f}")
    print(f"  Downside (if break): ${r['downside_per_share']:>+10.2f}")
    print(f"  Risk/Reward:         {r['risk_reward']:>10.2f}x")
    print(f"{'─' * 50}")
    if r["implied_probability"] is not None:
        print(f"  Implied Deal Prob:   {r['implied_probability'] * 100:>10.1f}%")
        print(f"  Break-Even Prob:     {r['breakeven_probability'] * 100:>10.1f}%")
    else:
        print(f"  Implied Deal Prob:   {'N/A':>10}  (upside = downside)")
        print(f"  Break-Even Prob:     {'N/A':>10}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
