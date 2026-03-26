# Example Output: LBO — Enterprise Cloud Security

> This is an annotated example of what a `/lbo` analysis produces. All data is fictional.

---

## Deal Summary

| Parameter | Value |
|-----------|-------|
| Target | CyberVault Systems |
| Enterprise Value | $2.0B (12.0x LTM EBITDA) |
| LTM EBITDA | $167M |
| Total Leverage | 5.5x ($918M) |
| Equity Check | $1,086M |
| Exit Multiple | 13.0x (Year 5) |
| EBITDA Growth | 8% CAGR |

---

## Returns Analysis

```
$ python3 tools/lbo.py --ebitda 167 --entry-multiple 12 --leverage 5.5 --rate 0.055 --growth 0.08 --years 5 --exit-multiple 13

==================================================
  LBO Returns Analysis
==================================================
  Entry EV:        $   2,004.0  (12.0x EBITDA)
  Entry Debt:      $     918.5  (5.5x EBITDA)
  Entry Equity:    $   1,085.5
──────────────────────────────────────────────────
  Exit EBITDA:     $     245.4  (8.0% CAGR)
  Exit EV:         $   3,189.9  (13.0x EBITDA)
  Exit Debt:       $     563.5
  Exit Equity:     $   2,626.4
──────────────────────────────────────────────────
  MOIC:                  2.42x
  IRR:                   19.3%
  Debt Paydown:    $     355.0
──────────────────────────────────────────────────
  Returns Attribution:
    EBITDA Growth        0.01x  (  0.9%)
    Multiple Change      0.23x  ( 40.5%)
    Deleveraging         0.33x  ( 58.6%)
==================================================
```

> **Reading returns attribution:** 59% of returns come from deleveraging (paying down $355M of debt from cash flow), 40% from multiple expansion (12x → 13x), and only 1% from EBITDA growth contribution to equity value. This tells us the deal is **leveraged bet on margin expansion and debt paydown**, not a growth story.

---

## Sensitivity Analysis

### IRR Sensitivity: Entry Multiple vs. Exit Multiple

| Entry \ Exit | 11.0x | 12.0x | 13.0x | 14.0x | 15.0x |
|-------------|-------|-------|-------|-------|-------|
| **10.0x** | 20.5% | 24.8% | 28.6% | 32.0% | 35.1% |
| **11.0x** | 16.2% | 20.1% | 23.6% | 26.8% | 29.7% |
| **12.0x** | 12.5% | 16.1% | **19.3%** | 22.3% | 25.0% |
| **13.0x** | 9.4% | 12.7% | 15.7% | 18.4% | 21.0% |
| **14.0x** | 6.7% | 9.7% | 12.5% | 15.1% | 17.5% |

> **Key insight:** The deal works (>15% IRR) as long as exit multiple is at or above entry (12x). If exit compresses to 11x, returns drop to 12.5% — below hurdle. **Multiple expansion is doing heavy lifting here.**

### IRR Sensitivity: EBITDA Growth vs. Leverage

| Growth \ Leverage | 4.5x | 5.0x | 5.5x | 6.0x | 6.5x |
|------------------|------|------|------|------|------|
| **6%** | 14.8% | 16.0% | 17.1% | 18.1% | 19.0% |
| **7%** | 15.8% | 17.1% | 18.2% | 19.2% | 20.2% |
| **8%** | 16.9% | 18.1% | **19.3%** | 20.4% | 21.4% |
| **9%** | 17.9% | 19.2% | 20.4% | 21.5% | 22.5% |
| **10%** | 18.9% | 20.3% | 21.5% | 22.7% | 23.7% |

---

## Debt Schedule

| Year | Beginning Debt | Interest | Mandatory Amort | Cash Sweep | Ending Debt | Leverage |
|------|---------------|----------|----------------|-----------|-------------|---------|
| 0 | — | — | — | — | $918M | 5.5x |
| 1 | $918M | $50M | $7M | $28M | $883M | 4.9x |
| 2 | $883M | $49M | $7M | $35M | $842M | 4.3x |
| 3 | $842M | $46M | $7M | $42M | $793M | 3.8x |
| 4 | $793M | $44M | $7M | $50M | $736M | 3.3x |
| 5 | $736M | $40M | $7M | $166M | $564M | 2.3x |

> **Deleveraging profile:** Leverage drops from 5.5x to 2.3x over 5 years. The 50% cash sweep accelerates paydown in later years as FCF grows. By Year 3, the company is solidly investment-grade leverage territory.

---

## What Kills This Thesis

1. **Multiple compression to 10x:** IRR drops to ~10%. If the cybersecurity market cools or a large competitor emerges, exit multiples could revert to pre-boom levels.
2. **Revenue growth stalls at 5%:** EBITDA growth slows, FCF drops, debt paydown decelerates. IRR falls below 15%.
3. **Margin pressure from AI competition:** If AI-native security platforms commoditize CyberVault's offerings, margins compress rather than expand.
4. **Interest rate spike (+200bps):** Floating rate debt costs increase by ~$18M/year, consuming cash flow earmarked for debt paydown.

---

*This analysis was produced using Alpha Stack's `/lbo` skill with the LBO returns tool.*
