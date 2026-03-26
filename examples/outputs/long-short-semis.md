# Example Output: Long/Short Equity — Semiconductor Equipment

> This is an annotated example of what a `/long-short` analysis produces. All data is fictional.

---

## Thesis Summary

| Field | Value |
|-------|-------|
| Company | PrecisionFab Technologies |
| Side | Long |
| Price | $178 |
| Target | $225-240 (26-35% upside) |
| Time Horizon | 12-18 months |
| Conviction | High |
| Position Size | 3.2% of NAV (half Kelly) |

**The variant perception:** Street models PrecisionFab as a cyclical bounce normalizing to 5-8% growth. We think the AI capex supercycle is structurally different — advanced packaging revenue (45% gross margin) is going from 28% to 40% of mix, which drives both top-line and margin expansion the market isn't pricing.

---

## Position Sizing (Kelly Criterion)

```
$ python3 tools/kelly.py --win-prob 0.60 --win-loss-ratio 1.8 --fraction 0.5

==================================================
  Kelly Criterion: Position Sizing
==================================================
  Win Probability:          60.0%
  Win/Loss Ratio:           1.80x
  Edge:                   +68.00%
──────────────────────────────────────────────────
  Full Kelly:               37.8%
  Half Kelly:               18.9%
  Exp Return/Bet:         +68.00%
  Geo Growth Rate:        9.1862%
──────────────────────────────────────────────────
  Drawdown Risk (at full Kelly):
    P(50% drawdown):        31.9%
    P(75% drawdown):        62.3%
==================================================
```

> **Sizing decision:** Full Kelly says 37.8% — way too aggressive for a single-stock position. Half Kelly is 18.9%, but our fund has a 5% single-position cap. We size at **3.2% of NAV** — well below Kelly, reflecting portfolio-level constraints and the high vol of semi equipment names (beta 1.3x).

---

## Variant Perception Detail

| Metric | Consensus | Our View | Evidence |
|--------|-----------|----------|---------|
| FY+1 Revenue Growth | 8% | 14% | TSMC/Samsung capex guides, advanced packaging pipeline |
| FY+1 EBITDA Margin | 29% | 32% | Mix shift to 35% advanced packaging (45% GM vs 32% corp) |
| NTM EPS | $8.20 | $9.50-10.00 | Higher revenue × higher margin = ~$1.50 EPS gap |
| Sustainable Growth | 5-8% (cycle peak) | 10-12% (structural) | AI capex is replacing traditional capex, not supplementing it |

> **Why consensus is wrong:** Analysts are using the 2018-2019 semi cycle as the template. That cycle was inventory-driven and mean-reverted. This cycle is capex-driven by hyperscalers building AI infrastructure — it has a multi-year runway that looks more like the cloud build-out of 2015-2020 than a traditional semi cycle.

---

## Catalyst Calendar

| # | Catalyst | Timeline | Probability | Impact |
|---|---------|----------|------------|--------|
| 1 | Q2 earnings — backlog update to $15B+ | 6 weeks | 75% | High — validates structural demand |
| 2 | TSMC Arizona fab Phase 2 order | 3 months | 60% | Medium — $400M+ equipment order |
| 3 | Margin inflection as software mix crosses 30% | H2 | 80% | High — proves mix shift thesis |
| 4 | Sell-side upgrades post Q2 beat | 2 months | 65% | Medium — broadens the shareholder base |
| 5 | Intel foundry services ramp | 6-9 months | 40% | Medium — optional upside not in base case |

---

## Risk Matrix

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| AI capex cycle peaks sooner than expected | 20% | High | Monitor hyperscaler capex guides quarterly |
| Customer concentration (top 3 = 62%) | Ongoing | Medium | Diversification into Intel, Samsung offsets |
| Short squeeze unwind (8.2% SI) | 15% | Low (positive) | Actually helps our long thesis |
| China export controls tighten | 25% | Medium | <10% China exposure, mostly non-restricted |
| Sector rotation out of tech | 30% | Medium | 3.2% position size limits drawdown |

---

## Monitoring Framework

**Thesis-confirming signals:**
- Backlog growth >10% QoQ
- Advanced packaging revenue mix trending toward 35%+
- Gross margin expansion >100bps QoQ

**Thesis-killing signals (sell triggers):**
- Two consecutive quarters of backlog decline
- TSMC/Samsung push out capex timelines by >6 months
- Gross margin contraction despite favorable mix

**Position management:**
- Add at $165 or below (5% position cap)
- Trim at $225 (take 30% off)
- Full exit at $240 or on thesis-kill signal

---

*This analysis was produced using Alpha Stack's `/long-short` skill with Kelly criterion sizing.*
