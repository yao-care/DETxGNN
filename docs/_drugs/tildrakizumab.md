---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tildrakizumab: From Unconfirmed Original Indication to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> The original indication for Tildrakizumab could not be confirmed from the current Evidence Pack — the drug is not yet marketed in Germany and no license records exist.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but currently **0 clinical trials** and **0 publications** support this direction — the prediction is based purely on knowledge-graph inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license records; original_indications field is empty) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is flagged as a data gap in this Evidence Pack). Based on information embedded in the repurposing rationale, Tildrakizumab is identified as an **anti-IL-23p19 monoclonal antibody**. This mechanism class is well established in dermatology (IL-23/Th17 pathway inhibition), though the confirmed original indication itself is not documented in this data pack.

The theoretical link to diabetic retinopathy rests on the hypothesis that the IL-23/Th17 axis contributes to chronic retinal inflammation and pathological neovascularization, so IL-23 blockade might theoretically reduce inflammation-driven retinal damage. However, this is a **mechanistic hypothesis only** — there is no animal or human data in the current evidence base connecting IL-23 inhibition to diabetic eye disease outcomes.

Overall, the high TxGNN score reflects structural similarity within the knowledge graph rather than validated biological or clinical evidence. This candidate should be treated as an early-stage hypothesis requiring substantial additional data before any clinical consideration.

### Other Predicted Indications (Not Yet Prioritized)

The same Evidence Pack also flagged three additional candidates, all at the same evidence stage:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 2 | Diabetic Retinopathy | 99.53% | L5 | Hold |
| 3 | Diabetic Cataract | 99.21% | L5 | Hold |
| 4 | Drug-induced Osteoporosis | 99.20% | L5 | Hold |

Of these, drug-induced osteoporosis has the relatively strongest mechanistic plausibility (IL-23/IL-17/Th17 signaling is known to regulate osteoclast activation via RANKL), while diabetic cataract has the weakest mechanistic link, as its pathology is primarily driven by hyperglycemia-induced lens protein glycation rather than inflammation. All four candidates currently have zero supporting clinical trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Tildrakizumab is not currently marketed in Germany, and no authorization records are available in this Evidence Pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this Evidence Pack. Notably, the meta section marks "TFDA label warnings/contraindications" as a **Blocking** data gap, meaning this candidate cannot yet enter Stage S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications are supported only by TxGNN model scores (L5, S0 stage) with zero clinical trials or literature evidence. In addition, a Blocking-severity data gap (missing TFDA label warnings/contraindications) currently prevents this candidate from proceeding to any safety evaluation stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): Obtain TFDA/official label warnings and contraindications
- Resolve DG002 (High): Confirm mechanism of action via DrugBank API query
- Confirm the drug's original approved indication(s), currently undocumented in this pack
- Identify at least preclinical or observational evidence connecting IL-23 inhibition to any of the four candidate indications before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

