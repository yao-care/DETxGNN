---
layout: default
title: Tivozanib
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: From Undetermined Original Indication to Endocervical Carcinoma (Predicted)

## One-Sentence Summary

Tivozanib is described in this evidence pack as a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor, but its originally approved indication is not documented here — the drug is unregistered in Germany (0 authorizations) and both formal MOA and regulatory safety data are flagged as gaps (DG001/DG002). The TxGNN model predicts possible efficacy in **Endocervical Carcinoma**, but this is currently supported by **0 clinical trials** and **0 publications** — a purely computational (L5) prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license records, `original_indications` empty) |
| Predicted New Indication | Endocervical carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The formal `original_moa` field is marked as a data gap (DG002). However, the evidence pack's repurposing rationale describes tivozanib as a highly selective VEGFR-1/2/3 tyrosine kinase inhibitor, acting mechanistically by suppressing tumor angiogenesis.

Because no approved indication or license record exists in this evidence pack, the relationship between tivozanib's original (real-world) indication and the predicted new indication cannot be established from the data provided here — this gap should be resolved before further scoring.

The mechanistic argument for endocervical carcinoma is purely analogical: anti-angiogenic agents (e.g., bevacizumab) are already used in cervical cancer, so VEGFR blockade is plausible in principle. Notably, all top-10 TxGNN predictions for this drug are rare gynecologic (cervical/uterine ligament) carcinoma subtypes, each scored L5/Hold with no supporting trials or literature — suggesting the model has captured a broad "VEGF-dependent gynecologic tumor" association rather than indication-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

Tivozanib is not currently marketed in Germany; there are no authorization records in this evidence pack (0 licenses).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR-1/2/3 tyrosine kinase inhibitor / anti-angiogenic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications for this drug are Evidence Level L5 (model prediction only, no supporting trials or literature), and a Blocking data gap (DG001 — TFDA warnings/contraindications) currently prevents S1 safety screening.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/regulatory label warnings and contraindications (blocking)
- Resolve DG002: confirm mechanism of action via DrugBank API
- Identify tivozanib's actual approved indication(s), since no license/indication record exists in this evidence pack
- Targeted literature and clinical trial search for VEGFR inhibitors in gynecologic (cervical/uterine ligament) carcinoma subtypes
- Re-score once evidence level advances beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

