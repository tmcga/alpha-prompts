#!/usr/bin/env python3
"""Market data fetcher — free, no-auth public sources (Treasury.gov, FRED).

Usage: python fetch.py --treasury | python fetch.py --fred DGS10,FEDFUNDS
"""

import argparse
import urllib.request
from datetime import datetime


def treasury_rates() -> dict:
    """Fetch the latest US Treasury yield curve from treasury.gov.

    Returns:
        Dict with tenor names as keys and yields (as decimals) as values,
        plus metadata (date, source).
    """
    try:
        yc_url = (
            "https://home.treasury.gov/resource-center/data-chart-center/"
            "interest-rates/daily-treasury-rates.csv/all/2025"
            "?type=daily_treasury_yield_curve&field_tdr_date_value=2025&page&_format=csv"
        )
        req = urllib.request.Request(yc_url, headers={"User-Agent": "AlphaStack/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            lines = resp.read().decode().strip().split("\n")

        if len(lines) < 2:
            raise ValueError("No yield curve data returned")

        header = [h.strip().strip('"') for h in lines[0].split(",")]
        latest = [v.strip().strip('"') for v in lines[-1].split(",")]
        row = dict(zip(header, latest))

        tenor_map = {
            "1 Mo": "1M",
            "2 Mo": "2M",
            "3 Mo": "3M",
            "4 Mo": "4M",
            "6 Mo": "6M",
            "1 Yr": "1Y",
            "2 Yr": "2Y",
            "3 Yr": "3Y",
            "5 Yr": "5Y",
            "7 Yr": "7Y",
            "10 Yr": "10Y",
            "20 Yr": "20Y",
            "30 Yr": "30Y",
        }
        rates = {}
        for csv_name, short_name in tenor_map.items():
            val = row.get(csv_name, "")
            if val and val != "N/A":
                rates[short_name] = round(float(val) / 100, 6)

        date_str = row.get("Date", "unknown")
        return {
            "date": date_str,
            "source": "US Treasury Daily Yield Curve",
            "rates": rates,
            "unit": "decimal (e.g., 0.045 = 4.5%)",
        }
    except Exception as e:
        return {"error": f"Treasury fetch failed: {type(e).__name__}: {e}"}


def fred_series(series_ids: list[str]) -> dict:
    """Fetch latest values from FRED (Federal Reserve Economic Data).

    Uses the FRED public observations endpoint. No API key required for
    the HTML scraping fallback; primary path uses the public JSON API
    which requires a key. Falls back to a no-auth approach.

    Args:
        series_ids: List of FRED series IDs (e.g., ['DGS10', 'FEDFUNDS']).

    Returns:
        Dict with series IDs as keys and their latest values + metadata.
    """
    results = {}
    for sid in series_ids:
        sid = sid.strip().upper()
        try:
            url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd=2024-01-01"
            req = urllib.request.Request(url, headers={"User-Agent": "AlphaStack/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                lines = resp.read().decode().strip().split("\n")

            if len(lines) < 2:
                results[sid] = {"error": "No data returned"}
                continue

            # Walk backwards to find last non-empty value
            for line in reversed(lines[1:]):
                parts = line.split(",")
                if len(parts) >= 2 and parts[1].strip() not in ("", "."):
                    results[sid] = {
                        "date": parts[0].strip(),
                        "value": float(parts[1].strip()),
                        "source": "FRED (fred.stlouisfed.org)",
                    }
                    break
            else:
                results[sid] = {"error": "All values empty"}

        except Exception as e:
            results[sid] = {"error": f"{type(e).__name__}: {e}"}

    return {"series": results, "retrieved_at": datetime.now().isoformat()}


COMMON_FRED = {
    "fed_funds": "FEDFUNDS",
    "10y": "DGS10",
    "2y": "DGS2",
    "30y": "DGS30",
    "3m_tbill": "DTB3",
    "cpi": "CPIAUCSL",
    "core_pce": "PCEPILFE",
    "unemployment": "UNRATE",
    "vix": "VIXCLS",
    "baa_spread": "BAAFFM",
}


def main():
    parser = argparse.ArgumentParser(description="Market Data Fetcher")
    parser.add_argument("--treasury", action="store_true", help="Fetch US Treasury yield curve")
    parser.add_argument(
        "--tenor",
        type=str,
        default=None,
        help="Specific tenor to display (e.g., 10, 2Y, 30Y)",
    )
    parser.add_argument(
        "--fred",
        type=str,
        default=None,
        help="Comma-separated FRED series IDs (e.g., DGS10,FEDFUNDS)",
    )
    parser.add_argument(
        "--list-fred",
        action="store_true",
        help="List common FRED series IDs",
    )
    args = parser.parse_args()

    if args.list_fred:
        print(f"\n{'=' * 55}")
        print("  Common FRED Series")
        print(f"{'=' * 55}")
        for name, sid in COMMON_FRED.items():
            print(f"  {name:<20s} {sid}")
        print(f"{'=' * 55}")
        print("  Usage: python fetch.py --fred DGS10,FEDFUNDS")
        print()
        return

    if not args.treasury and not args.fred:
        parser.error("Provide --treasury, --fred SERIES, or --list-fred")

    if args.treasury:
        result = treasury_rates()
        if "error" in result:
            print(f"\nError: {result['error']}\n")
            return
        print(f"\n{'=' * 50}")
        print(f"  US Treasury Yield Curve ({result['date']})")
        print(f"{'=' * 50}")
        for tenor, rate in result["rates"].items():
            if args.tenor:
                t = args.tenor.upper().replace("Y", "").replace("M", "")
                if t not in tenor.upper().replace("Y", "").replace("M", ""):
                    continue
            print(f"  {tenor:>5s}:  {rate * 100:6.3f}%")
        print(f"{'=' * 50}")
        print(f"  Source: {result['source']}")
        print()

    if args.fred:
        ids = [s.strip() for s in args.fred.split(",")]
        result = fred_series(ids)
        print(f"\n{'=' * 55}")
        print("  FRED Economic Data")
        print(f"{'=' * 55}")
        for sid, data in result["series"].items():
            if "error" in data:
                print(f"  {sid:<12s}  Error: {data['error']}")
            else:
                print(f"  {sid:<12s}  {data['value']:>10.4f}  ({data['date']})")
        print(f"{'=' * 55}")
        print("  Source: FRED (fred.stlouisfed.org)")
        print()


if __name__ == "__main__":
    main()
