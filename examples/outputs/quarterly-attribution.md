# Example Output: Quarterly Performance Attribution

> This is an annotated example of what an `/attribution` analysis produces. All data is fictional.

---

## Summary

| Metric | Value |
|--------|-------|
| Fund | Growth Equity Fund |
| Period | Q4 |
| Benchmark | S&P 500 |
| Portfolio Return | +4.77% |
| Benchmark Return | +4.43% |
| Active Return | +0.34% |

---

## Brinson-Fachler Attribution

```
$ python3 tools/brinson.py --sectors "Tech,Healthcare,Financials,ConsDisc,Industrials,Energy,CommSvcs,Staples,Materials,RealEstate" \
  --port-weights 0.32,0.18,0.12,0.10,0.09,0.05,0.06,0.03,0.03,0.02 \
  --port-returns 0.085,0.032,0.051,-0.021,0.048,0.072,0.025,0.018,0.035,-0.015 \
  --bench-weights 0.28,0.14,0.13,0.11,0.09,0.05,0.08,0.06,0.03,0.03 \
  --bench-returns 0.062,0.048,0.045,0.013,0.039,0.068,0.051,0.022,0.029,-0.008

======================================================================
  Brinson-Fachler Performance Attribution
======================================================================
  Portfolio Return:      +4.77%
  Benchmark Return:      +4.43%
  Active Return:         +0.34%
──────────────────────────────────────────────────────────────────────
  Sector        Wt(P)  Wt(B)  Ret(P)  Ret(B)   Alloc  Select   Inter   Total
  ──────────── ────── ────── ─────── ─────── ─────── ─────── ─────── ───────
  Tech          32.0%  28.0%   +8.5%   +6.2%  +0.07%  +0.64%  +0.09%  +0.81%
  Healthcare    18.0%  14.0%   +3.2%   +4.8%  +0.01%  -0.22%  -0.06%  -0.27%
  Financials    12.0%  13.0%   +5.1%   +4.5%  -0.00%  +0.08%  -0.01%  +0.07%
  ConsDisc      10.0%  11.0%   -2.1%   +1.3%  +0.03%  -0.37%  +0.03%  -0.31%
  Industrials    9.0%   9.0%   +4.8%   +3.9%  -0.00%  +0.08%  +0.00%  +0.08%
  Energy         5.0%   5.0%   +7.2%   +6.8%  +0.00%  +0.02%  +0.00%  +0.02%
  CommSvcs       6.0%   8.0%   +2.5%   +5.1%  -0.01%  -0.21%  +0.05%  -0.17%
  Staples        3.0%   6.0%   +1.8%   +2.2%  +0.07%  -0.02%  +0.01%  +0.05%
  Materials      3.0%   3.0%   +3.5%   +2.9%  -0.00%  +0.02%  +0.00%  +0.02%
  RealEstate     2.0%   3.0%   -1.5%   -0.8%  +0.05%  -0.02%  +0.01%  +0.04%
  ──────────── ────── ────── ─────── ─────── ─────── ─────── ─────── ───────
  TOTAL                                       +0.22%  -0.01%  +0.13%  +0.34%
======================================================================
```

---

## Analysis: Where Did the Alpha Come From?

### Decomposition

| Source | Contribution | % of Active Return |
|--------|-------------|-------------------|
| **Allocation Effect** | +0.22% | 65% |
| **Selection Effect** | -0.01% | -3% |
| **Interaction Effect** | +0.13% | 38% |
| **Total Active Return** | **+0.34%** | **100%** |

> **Key insight:** The outperformance was almost entirely from **sector allocation bets**, not stock picking. The PM's decision to overweight Tech (+4%) and underweight Staples (-3%) drove 65% of active return. Stock selection was actually slightly negative — the PM picked worse stocks within sectors on a net basis.

### Top Contributors

| # | Sector | Effect | Driver |
|---|--------|--------|--------|
| 1 | **Tech (+0.81%)** | Selection | PM's tech stocks returned 8.5% vs benchmark 6.2% — strong stock picking in AI/cloud |
| 2 | **Staples (+0.05%)** | Allocation | Intentional underweight in an underperforming sector |
| 3 | **Industrials (+0.08%)** | Selection | Correct stock picks within a market-weight sector |

### Top Detractors

| # | Sector | Effect | Driver |
|---|--------|--------|--------|
| 1 | **Consumer Disc (-0.31%)** | Selection | PM's consumer stocks returned -2.1% vs benchmark +1.3% — specific to a retail short that reversed |
| 2 | **Healthcare (-0.27%)** | Selection | Overweight position underperformed benchmark by 160bps — biotech holdings lagged large pharma |
| 3 | **Comm Services (-0.17%)** | Selection | Underweight + poor stock picks — missed the streaming recovery trade |

---

## Intentionality Check

| Bet | Intended? | Outcome | Notes |
|-----|-----------|---------|-------|
| Tech overweight (+4%) | Yes | +0.81% | Core thesis — AI infrastructure play |
| Healthcare overweight (+4%) | Yes | -0.27% | Biotech thesis hasn't played out yet |
| Staples underweight (-3%) | Yes | +0.05% | Correct call — defensive rotation faded |
| Consumer Disc negative return | Partially | -0.31% | Retail short was intended, magnitude was not |
| Comm Services underweight (-2%) | No | -0.17% | Unintended — result of position sizing, not active decision |

> **CIO takeaway:** Tech selection was the standout — the PM's AI/cloud picks generated +230bps of alpha within that sector. Healthcare is the concern: the 4% overweight delivered -160bps of underperformance. If the biotech thesis doesn't inflect next quarter, consider trimming the overweight. The consumer discretionary loss (-0.31%) was a specific event (short squeeze on a retail name) — not systematic.

---

## Recommendations for Next Quarter

1. **Maintain Tech overweight** — thesis intact, selection quality proven
2. **Reduce Healthcare overweight** by 2% — rotate from biotech to large pharma (better risk/reward)
3. **Close Consumer Disc underperformer** — the retail short has moved against us; re-evaluate thesis
4. **Review Comm Services positioning** — the -2% underweight was unintended and cost us 17bps

---

*This analysis was produced using Alpha Stack's `/attribution` skill with the Brinson attribution tool.*
