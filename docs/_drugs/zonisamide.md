---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Zonisamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

> Zonisamide is an antiepileptic drug used as adjunctive therapy for refractory partial seizures, acting through sodium/calcium channel modulation.
> The TxGNN model predicts it may be effective for **Tourette Syndrome**,
> but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a mechanistic hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — adjunctive treatment of partial seizures (inferred from literature evidence in this pack; no formal license text available) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap, DrugBank query pending). Based on information embedded in the evidence pack's own literature (e.g., PMID 16341290, 8831258), zonisamide is a broad-spectrum antiepileptic drug (1,2-benzisoxazole-3-methanesulfonamide) with multiple proposed mechanisms — sodium/T-type calcium channel blockade and modulation of dopamine/serotonin release — used mainly as adjunctive therapy for partial and generalized seizures.

The rationale for a Tourette syndrome connection is purely mechanistic: zonisamide's mild anti-dopaminergic activity and effect on monoamine release could theoretically reduce tic frequency, since dopaminergic dysregulation is implicated in tic disorders. However, this link has not been tested — there are no registered clinical trials and no published literature specifically evaluating zonisamide in Tourette syndrome. This places the prediction at the earliest possible evidence stage (L5 — model prediction only), and it should be treated as a research hypothesis rather than a repurposing signal ready for clinical evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorization records are available — zonisamide is currently listed as **not marketed** in Germany within this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug-drug interaction data are currently marked as a blocking data gap (DG001), which prevents a full S1 safety assessment for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for Tourette syndrome is high, but it is unsupported by any clinical trial or literature evidence — the mechanistic link (dopamine/serotonin modulation) is speculative. Combined with the missing TFDA safety data (blocking gap) and the drug's current unmarketed status in Germany, there is insufficient basis to advance this specific indication beyond a research hypothesis.

**To proceed, the following is needed:**
- Formal MOA confirmation from DrugBank (DG002)
- TFDA label warnings/contraindications to clear the S1 safety gate (DG001)
- At minimum, preclinical or case-series evidence directly evaluating zonisamide in tic disorders
- Consider re-prioritizing: this same evidence pack contains two candidates with substantially stronger evidence — **absence epilepsy** (rank 8, evidence level L1, "Proceed with Guardrails", supported by a completed Phase 3 RCT n=583 and multiple cohort studies) and **manic/mixed bipolar disorder** (rank 7, evidence level L2, "Research Question", supported by a placebo-controlled RCT). These may represent more actionable near-term repurposing opportunities than Tourette syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

