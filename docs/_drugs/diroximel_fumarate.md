---
layout: default
title: Diroximel Fumarate
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# DIROXIMEL FUMARATE: From Unknown Original Indication to Diabetic Cataract

## One-Sentence Summary

Diroximel fumarate is a fumarate ester prodrug whose original indication and mechanism of action are currently undocumented in this Evidence Pack (data gap). TxGNN predicts a possible association with **Diabetic Cataract**, but this prediction is supported by **0 clinical trials** and **0 publications**, making it a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licensed indication on record) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.9993% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diroximel fumarate belongs to the fumarate ester class of prodrugs, but its original indication and pharmacological rationale are not recorded in this Evidence Pack, so no mechanistic link to diabetic cataract can be established.

Notably, the top 10 predicted indications for this drug are all diabetes-related ocular conditions (diabetic cataract, diabetic retinopathy, various cataract subtypes) with nearly identical TxGNN scores (0.999990–0.999992). This pattern of homogeneous, non-differentiated scores across an entire disease cluster is a known signature of models linking predictions through a shared node (e.g., "diabetes" or "cataract") rather than producing drug-specific signals. Absent any independent clinical or literature evidence, this pattern should be treated as a flag for potential model over-generalization rather than a genuine repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Diroximel fumarate is not currently marketed in Germany (未上市), and no authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are all marked as data gaps in the current Evidence Pack. Per DG001, TFDA/BfArM label warnings and contraindications must be obtained before any safety pre-assessment (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero clinical trials, zero literature support, and no mechanism-of-action data — combined with a suspicious pattern of near-identical TxGNN scores across all 10 predicted diabetes/ocular indications, suggesting the prediction may reflect shared-node clustering rather than a specific drug-disease signal. There is no evidentiary basis to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/official label warnings and contraindications before any safety evaluation can begin
- Resolve DG002 (High): retrieve MOA from DrugBank to enable mechanistic plausibility assessment
- Confirm original approved indication(s) for diroximel fumarate, since none are currently on record
- Independent literature/clinical trial search specific to diabetic cataract and diroximel fumarate (or its parent compound monomethyl fumarate) to distinguish genuine signal from model artifact
- Manual review of TxGNN's disease-embedding structure for this drug to assess whether the diabetes/cataract cluster reflects a training-data or overfitting issue, before any indication in this cluster is progressed further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

