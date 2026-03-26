# Example Output: Sell-Side M&A — Specialty Chemical Company

> This is an annotated example of what a `/sell-side` analysis produces. All data is fictional.

---

## Assumptions

| Assumption | Value | Confidence | Source |
|-----------|-------|-----------|--------|
| Revenue growth | 7% organic | High | 3-year trend |
| EBITDA margin trajectory | 28% → 30% | Medium | Management guidance + peer comps |
| Capex normalization | $13M/year (from $20M) | High | Growth capex winding down |
| Terminal growth rate | 2.5% | Medium | GDP + specialty chemical premium |
| WACC | 9.5% | Medium | CAPM build-up (see below) |
| Buyer universe multiple range | 9-12x EBITDA | High | Precedent transactions |

> **Why this matters:** Every number below flows from these assumptions. Change the EBITDA margin assumption by 100bps and the valuation range shifts by ~$50M.

---

## Valuation: DCF

```
$ python3 tools/dcf.py --fcf 62,68,75,82,90 --wacc 0.095 --terminal-growth 0.025 --net-debt 145 --shares 100

==================================================
  DCF Valuation (Gordon Growth)
==================================================
  PV of FCFs (explicit):  $      284.67
  PV of Terminal Value:   $      837.14
  Enterprise Value:       $    1,121.80
  Less: Net Debt:         $      145.00
  Equity Value:           $      976.80
  Price per Share:        $        9.77
  Terminal Value % of EV:         74.6%
==================================================

  Sensitivity: Price per Share (WACC vs Terminal Growth)
──────────────────────────────────────────────────
WACC \ TG   0.021   0.023   0.025   0.027   0.029
    0.087  $10.63  $10.94  $11.26  $11.61  $11.98
    0.091   $9.92  $10.19  $10.47  $10.77  $11.09
    0.095   $9.28   $9.52   $9.77  $10.03  $10.31
    0.099   $8.71   $8.92   $9.14   $9.37   $9.62
    0.103   $8.20   $8.38   $8.58   $8.78   $9.00
```

> **Reading this output:** Enterprise value of ~$1.1B. Terminal value is 74.6% of EV — high but typical for a stable grower. The sensitivity table shows the price is most sensitive to WACC (vertical axis): a 40bps change in WACC moves value by ~$0.60/share.

---

## Valuation: LBO Floor

```
$ python3 tools/lbo.py --ebitda 62 --entry-multiple 10 --leverage 5.0 --rate 0.06 --growth 0.07 --years 5 --exit-multiple 10

  Entry EV:        $     620.0  (10.0x EBITDA)
  Entry Equity:    $     310.0
  Exit EBITDA:     $      86.9  (7.0% CAGR)
  Exit EV:         $     869.3  (10.0x EBITDA)
  MOIC:                  2.08x
  IRR:                   15.8%
```

> **What this tells us:** A PE buyer paying 10x with no multiple expansion generates a ~16% IRR. This sets the **floor** — strategic buyers should pay more because of synergies. The 10-12x range in our buyer universe is well-supported.

---

## Valuation Summary

| Method | Low | Base | High |
|--------|-----|------|------|
| DCF (Gordon Growth) | $920M | $1,120M | $1,380M |
| DCF (Exit Multiple, 10-12x) | $880M | $1,050M | $1,220M |
| Precedent Transactions (9-12x) | $558M | $744M | $930M |
| LBO Floor (15-20% IRR) | $620M | $720M | $810M |
| **Recommended Range** | **$850M** | **$1,000M** | **$1,150M** |

> **The range tells the story:** DCF points to $1.1B+, but precedent transactions and LBO analysis anchor the floor at $850M. A competitive auction with 3+ serious bidders should push toward $1B+.

---

## Buyer Universe (Top 8)

| Buyer | Type | Rationale | Est. Willingness | Risk |
|-------|------|-----------|-----------------|------|
| ChemGlobal AG | Strategic | Adjacent product line, distribution overlap | 11-12x | EU regulatory |
| Adhesive Corp | Strategic | Direct competitor, cost synergies | 10-11x | Antitrust review |
| Summit Capital | PE | Bolt-on to portfolio company | 9-10x | Lower ceiling |
| Vertex Partners | PE | Standalone platform | 9-10x | Leverage constrained |
| NipponChem | Strategic | US market entry | 11-13x | CFIUS risk |
| PolymerTech Inc | Strategic | Technology acquisition | 10-11x | Integration complexity |
| Atlas PE | PE | Specialty chemical thesis | 9.5-10.5x | Commodity cycle concern |
| IndustriGroup | Strategic | Vertical integration play | 10-12x | Board approval lag |

---

## Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Customer concentration (28% in top 2) | Medium | High | Long-term contracts, diversified pipeline |
| Environmental remediation ($4M reserve) | Low | Medium | Indemnity cap in purchase agreement |
| EBITDA margin reversion to 26% | Low | High | Show structural drivers, not just cycle |
| Process leak (identity revealed) | Medium | Medium | Staged teaser distribution, clean team |
| No bid above 10x | Low | High | Expand buyer universe, adjust timing |

---

## What Kills This Thesis

1. **Margin compression:** If raw material costs spike and SpecChem can't pass through, EBITDA could drop 20%. At $50M EBITDA, the valuation range compresses to $650-750M.
2. **Customer loss:** If either of the two 14% customers switches suppliers during the process, the story breaks.
3. **Rate environment:** If financing costs rise 200bps, PE buyers' willingness to pay drops by 0.5-1.0x EBITDA.

---

*This analysis was produced using Alpha Stack's `/sell-side` skill with DCF, LBO, and WACC tools.*
