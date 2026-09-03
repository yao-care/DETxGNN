---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Pegfilgrastim: From Chemotherapy-Induced Neutropenia to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Pegfilgrastim is a G-CSF (granulocyte colony-stimulating factor) analogue, clinically used to stimulate bone marrow granulocyte production and prevent chemotherapy-induced neutropenia.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but currently **no clinical trials** and **no publications** support this direction — the prediction rests solely on the model's internal knowledge graph.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced neutropenia (based on known mechanism of action; formal Taiwan/Germany license data not available) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pegfilgrastim is a G-CSF analogue whose established clinical role is stimulating bone marrow granulocyte production to prevent chemotherapy-induced neutropenia. No published data currently describe a direct link between this mechanism and diabetic retinopathy pathology (e.g., VEGF signaling, retinal microvascular injury, or inflammatory pathways).

The high TxGNN score may reflect an indirect graph association between G-CSF-mediated bone marrow stem cell mobilization (CD34+ cells) and vascular repair processes, which are conceptually relevant to ischemic retinal disease. However, this is a hypothesis derived from graph structure, not from experimental or clinical evidence. Notably, G-CSF agents have a theoretical **dual-direction risk**: while endothelial progenitor cell mobilization could theoretically support ischemic retinal repair, G-CSF has also been raised as a potential contributor to pathological neovascularization, which would be undesirable in proliferative diabetic retinopathy. A second, closely related prediction — "diabetic retinopathy" (score 99.73%, rank 3759) — shows the same pattern of unresolved mechanistic direction and complete absence of supporting evidence.

Given the original indication and MOA are themselves marked as data gaps in this evidence pack, this mechanistic rationale cannot be independently verified and should be treated as speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No license records are currently available — pegfilgrastim is not marketed in this jurisdiction according to the regulatory dataset (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Key warnings, contraindications, and drug-drug interaction data are currently unavailable in this evidence pack (flagged as a **Blocking** data gap — TFDA/label warnings and contraindications, DG001). This gap alone is sufficient to prevent progression to safety pre-screening (S1) regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by the TxGNN model score (L5 evidence) with zero clinical trials and zero publications. The proposed mechanism is speculative and carries an unresolved, potentially opposing risk direction (retinal vascular repair vs. pathological neovascularization). Combined with a Blocking-severity gap in safety/label data, this candidate does not meet the threshold for further evaluation at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for pegfilgrastim (DG002)
- TFDA/official label warnings and contraindications (DG001, Blocking — required before any S1 safety pre-screening)
- Preclinical or observational evidence specifically evaluating G-CSF agents in diabetic retinopathy, given the theoretical risk of exacerbating pathological retinal neovascularization
- Formal regulatory/license data if market entry is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

