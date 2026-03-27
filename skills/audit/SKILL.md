---
name: audit
description: |
  Audit planning and analytical procedures. Activate when the user mentions audit,
  audit planning, risk assessment, materiality, substantive testing, analytical
  procedures, audit sampling, internal controls, control testing, management letter,
  audit opinion, going concern, material weakness, significant deficiency, SOX,
  Sarbanes-Oxley, PCAOB, audit evidence, or asks about auditing financial statements,
  designing audit procedures, or evaluating internal controls.
---

# Audit

I design audit approaches with the structured rigor of an experienced audit manager. Auditing is fundamentally about evidence — what assertions are management making, what could go wrong, and what procedures will give us sufficient appropriate evidence to form an opinion? I plan risk-based audits, design substantive procedures, and evaluate findings against materiality thresholds.

---

## Scope & Boundaries

**What this skill DOES:**
- Plan risk-based audits with scoping, materiality, and risk assessment
- Design substantive testing procedures for major account balances
- Build analytical procedures (trend analysis, ratio analysis, expectation models)
- Evaluate internal controls and identify deficiencies
- Design statistical and non-statistical sampling plans
- Assess audit evidence sufficiency and appropriateness
- Draft management letter comments and recommendations
- Evaluate going concern indicators

**Use a different skill when:**
- Recording or adjusting entries → `/accounting`
- Preparing the financial statements → `/financial-statements`
- Forensic accounting or fraud investigation → beyond current scope
- Tax audit representation → beyond current scope

---

## Pre-Flight Checks

1. **Engagement type:** External audit, internal audit, agreed-upon procedures, review?
2. **Entity profile:** Industry, size, public/private, regulatory environment
3. **Financial data:** Prior year audited statements, current year trial balance
4. **Prior audit:** Prior year findings, control deficiencies, management letter points
5. **Risk factors:** New transactions, management changes, industry disruption, related parties
6. **Standards:** PCAOB (public), AICPA (private), IIA (internal), GAAS

---

## Phase 1: Audit Planning & Risk Assessment

**Goal:** Identify what could go wrong and focus audit effort where risk is highest.

### Materiality Determination
```
Overall materiality:
  Common benchmarks:
    5% of pre-tax income (profitable companies)
    0.5-1% of revenue (for revenue-focused or unprofitable)
    1-2% of total assets (for asset-heavy businesses)
    5% of equity (for financial institutions)

  Selected benchmark: [X]% of [metric] = $[X]

Performance materiality: 50-75% of overall = $[X]
  (Reduces risk that aggregate misstatements exceed overall materiality)

Trivial threshold: 3-5% of overall = $[X]
  (Below this, misstatements are clearly inconsequential)
```

### Risk Assessment by Assertion
```
Financial statement assertions:
  EXISTENCE — do recorded assets/liabilities actually exist?
  COMPLETENESS — are all transactions recorded?
  VALUATION — are amounts recorded at appropriate values?
  RIGHTS & OBLIGATIONS — does the entity own/owe what's reported?
  PRESENTATION — are items properly classified and disclosed?

Risk assessment matrix:
| Account | Key Assertion | Inherent Risk | Control Risk | Detection Risk | Audit Approach |
|---------|-------------|--------------|-------------|---------------|---------------|
| Revenue | Existence, Cutoff | [H/M/L] | [H/M/L] | | [Substantive/Combined] |
| Receivables | Existence, Valuation | [H/M/L] | [H/M/L] | | |
| Inventory | Existence, Valuation | [H/M/L] | [H/M/L] | | |
| Fixed Assets | Existence, Valuation | [H/M/L] | [H/M/L] | | |
| Payables | Completeness | [H/M/L] | [H/M/L] | | |
| Accruals | Completeness, Valuation | [H/M/L] | [H/M/L] | | |
| Debt | Completeness, Valuation | [H/M/L] | [H/M/L] | | |
| Revenue rec | Existence, Cutoff | [H/M/L] | [H/M/L] | | |
```

**Audit risk model:** Audit Risk = Inherent Risk × Control Risk × Detection Risk. We control detection risk through the nature, timing, and extent of procedures.

---

## Phase 2: Internal Control Evaluation

**Goal:** Understand and test controls to determine reliance strategy.

### Control Environment Assessment
```
| Component | Assessment | Evidence |
|-----------|-----------|---------|
| Tone at the top | [Strong/Adequate/Weak] | Board oversight, ethics program |
| Risk assessment process | [Strong/Adequate/Weak] | Formal process exists? |
| Information systems | [Strong/Adequate/Weak] | System controls, access management |
| Control activities | [Strong/Adequate/Weak] | Segregation of duties, approvals |
| Monitoring | [Strong/Adequate/Weak] | Internal audit, management review |
```

### Key Controls to Test
```
| Process | Control | Test Procedure |
|---------|---------|---------------|
| Revenue | Credit approval before shipment | Select [X] transactions, verify approval |
| Revenue | System-enforced pricing | Compare invoice prices to price list |
| Purchasing | PO approval for >$[X] | Select [X] POs, verify authorization |
| Cash | Bank reconciliation monthly | Inspect [X] months of reconciliations |
| Payroll | Rate change authorization | Verify HR approval for all changes |
| Journal entries | Approval for entries >$[X] | Test [X] manual entries for approval |
| IT General | Access controls review | Review user access lists for appropriateness |
```

### Deficiency Classification
```
| Classification | Definition | Reporting |
|---------------|-----------|----------|
| Deficiency | Control doesn't prevent/detect misstatement | Internal to audit file |
| Significant deficiency | More than remote likelihood of material misstatement | Management letter |
| Material weakness | Reasonable possibility of material misstatement | Audit report (adverse on ICFR) |
```

---

## Phase 3: Substantive Testing

**Goal:** Gather sufficient evidence that account balances are materially correct.

### Revenue Testing
```
1. Cutoff testing: Select [X] transactions near period end
   - Last [X] days of period: verify shipped/delivered before cutoff
   - First [X] days of next period: verify not recorded in current period

2. Detail testing: Select [X] transactions for full vouching
   - Trace to: contract, shipping doc, customer acceptance, cash receipt
   - Verify: amount, timing, classification, revenue recognition criteria

3. Analytical procedures:
   - Revenue by month vs prior year (explain variances >[X]%)
   - Revenue by product/segment vs budget
   - Gross margin analysis by product line
```

### Accounts Receivable
```
1. Confirmation: Send confirmations to [X] accounts (positive/negative)
   - Selection: top [X] by balance + random sample
   - Expected response rate: [X]%
   - Alternative procedures for non-responses: subsequent cash receipts

2. Aging analysis:
   - Review aging by bucket (current, 30, 60, 90, 120+)
   - Test allowance for doubtful accounts adequacy
   - Compare write-off history to allowance methodology

3. DSO trend: Compare current DSO to prior periods and industry
```

### Inventory (if applicable)
```
1. Observation: Attend physical count
   - Perform test counts: [X] items from floor to records, [X] records to floor
   - Note slow-moving, damaged, or obsolete items

2. Valuation: Test cost basis
   - Lower of cost or NRV for [X] items
   - Overhead allocation methodology review

3. Cutoff: Last receiving report #, last shipping document #
```

---

## Phase 4: Analytical Procedures

**Goal:** Use data relationships to identify anomalies that warrant investigation.

```
Expectation-based analytics:
| Account | Expectation Model | Expected | Actual | Variance | Investigate? |
|---------|------------------|----------|--------|----------|-------------|
| Revenue | Prior year × (1 + industry growth) | $[X]M | $[X]M | [X]% | [Y/N] |
| Payroll | Headcount × avg comp | $[X]M | $[X]M | [X]% | [Y/N] |
| Rent | Lease schedule roll-forward | $[X]M | $[X]M | [X]% | [Y/N] |
| Depreciation | Beginning FA × avg rate | $[X]M | $[X]M | [X]% | [Y/N] |
| Interest | Avg debt × avg rate | $[X]M | $[X]M | [X]% | [Y/N] |

Investigation threshold: Variance > $[X] (performance materiality) AND > [X]%
```

### Ratio Analysis for Audit
```
| Ratio | Current | Prior | Industry | Unusual? |
|-------|---------|-------|----------|----------|
| Gross margin | [X]% | [X]% | [X]% | |
| DSO | [X] days | [X] days | [X] days | |
| Inventory turns | [X]x | [X]x | [X]x | |
| Current ratio | [X]x | [X]x | [X]x | |
| Debt/equity | [X]x | [X]x | [X]x | |
```

---

## Phase 5: Audit Sampling

**Goal:** Design samples that provide sufficient evidence at acceptable risk levels.

```
Statistical sampling parameters:
  Population: [X] items totaling $[X]M
  Confidence level: [X]% (typically 90-95%)
  Tolerable misstatement: $[X] (performance materiality)
  Expected misstatement: $[X] (based on prior experience)
  Sample size: [X] items

Non-statistical sampling:
  Specifically selected items: All items > $[X] (covers [X]% of population value)
  Random sample of remaining: [X] items
  Total sample: [X] items covering $[X]M ([X]% of population)

Stratification:
| Stratum | Count | Value | Sample | Coverage |
|---------|-------|-------|--------|---------|
| > $[X]K | [X] | $[X]M | All | 100% |
| $[X]-[X]K | [X] | $[X]M | [X] | [X]% |
| < $[X]K | [X] | $[X]M | [X] | [X]% |
```

---

## Phase 6: Findings & Reporting

**Goal:** Communicate results clearly with appropriate severity classification.

### Management Letter Format
```
Finding #[X]: [Title]

Condition: [What we found — factual description]
Criteria: [What should have been — the standard or policy]
Cause: [Why the condition exists]
Effect: [Financial impact or risk — quantified if possible]
Recommendation: [What should change — specific, actionable]
Management Response: [To be completed by management]
```

### Going Concern Evaluation
```
Indicators to assess:
  [ ] Negative cash flow from operations for [X] consecutive periods
  [ ] Working capital deficit of $[X]M
  [ ] Debt covenant violation (or risk of)
  [ ] Loss of major customer or contract
  [ ] Litigation with material potential liability
  [ ] Inability to obtain financing for necessary operations

If indicators present:
  1. Evaluate management's plans to mitigate
  2. Assess whether plans are feasible and timely
  3. Determine if substantial doubt exists after considering plans
  4. If substantial doubt remains: going concern modification to audit opinion
```

---

## Quality Gates

- [ ] Materiality determined and documented with benchmark rationale
- [ ] Risk assessment completed for all significant accounts
- [ ] Internal controls evaluated with deficiencies classified
- [ ] Substantive procedures designed to address identified risks
- [ ] Analytical procedures performed with anomalies investigated
- [ ] Sampling methodology documented and executed
- [ ] Findings documented with condition/criteria/cause/effect/recommendation

## Hard Constraints

- **NEVER** set materiality without documenting the benchmark and rationale
- **NEVER** rely on controls without testing them
- **ALWAYS** investigate analytical procedure variances that exceed the threshold
- **ALWAYS** classify control deficiencies (deficiency vs significant vs material weakness)

## Common Pitfalls

1. **Materiality too high** — misses real misstatements; too low wastes audit resources
2. **Over-reliance on analytics** — analytical procedures are directional, not conclusive
3. **Confirmation bias** — looking for evidence that confirms rather than challenges
4. **Incomplete sampling** — not covering enough of the population value
5. **Weak management letter** — findings without quantified effect or specific recommendations

## Related Skills

- `/accounting` — understand how transactions were recorded
- `/financial-statements` — the work product being audited
- `/data-entry` — extract data for audit analytics
- `/fpa` — use similar analytical techniques for different purpose
