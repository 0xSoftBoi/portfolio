# Research article template

> Use this before promoting a draft from **note** to **research**. A section may be short, but it may not be silently omitted.

## Metadata

- Status: draft / research note / research report
- Version:
- Last updated:
- Decision question:
- One-sentence claim:
- Evidence classes present: observed / derived / estimated / target
- Reproducibility artifact:

## Executive finding

State the result in 2–4 sentences. Lead with what changed your view, not the setup.

## Key findings

1. Finding with denominator / units / comparison set.
2. Finding with uncertainty or sensitivity where relevant.
3. Negative result, boundary, or null finding.

## Method

- Data / system / sample
- Time window
- Inclusion and exclusion rules
- Measurement procedure
- Baseline / counterfactual
- Parameters and assumptions
- Known sources of bias

## Evidence ledger

| Claim | Evidence class | Primary source / artifact | Reproducible? | Notes |
|---|---|---|---|---|
| | Observed / Derived / Estimated / Target | | Yes / Partial / No | |

## Results

Use tables or figures when the evidence is quantitative. Every figure needs a takeaway, source/provenance, units, and enough context to avoid misleading scale or denominator choices.

## Strongest counterargument

Write the best rival explanation as if its author will review the piece. State what observation would distinguish it from the preferred thesis.

## Sensitivity / robustness

Show how the conclusion changes under plausible alternative assumptions, subsets, parameters, baselines, or evaluators. If no sensitivity analysis is possible, state why.

## Limitations

Say what the evidence does **not** establish. Do not hide a material limitation in a footnote.

## What would change my mind?

List concrete observations that would downgrade, overturn, or materially revise the conclusion.

## Reproducibility

Link code, data, configs, queries, prompts, calculations, hardware logs, or exact commands where practical.

## Sources

Primary sources first. A citation must support the exact adjacent claim; secondary sources may provide context but should not be used to launder unsupported claims.

## Revision log

- v1.0 — initial publication

---

## Publication gates

- [ ] Gate A — every consequential factual claim has provenance.
- [ ] Gate B — quantitative claims expose denominator, units, assumptions, and uncertainty/sensitivity where material.
- [ ] Gate C — strongest rival explanation is stated and tested or explicitly unresolved.
- [ ] Gate D — citations support the exact claims they sit beside; facts, derivations, estimates, and targets are distinguished.
- [ ] Gate E — reproduction artifacts are linked, or the reason reproduction is impossible is explicit.
- [ ] Editorial — headline/dek do not overstate the body; the conclusion is no stronger than the evidence.
