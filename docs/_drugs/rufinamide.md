---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

> Rufinamide is an anticonvulsant historically associated with Lennox-Gastaut Syndrome (LGS), referenced within this evidence pack's mechanistic rationale, though formal original-indication and MOA fields are currently data gaps.
> The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
> but **no clinical trials** and **no literature** are currently available to support this direction — this is a model-prediction-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lennox-Gastaut Syndrome (LGS) — inferred from mechanistic rationale text; formal `original_indications`/`original_moa` fields are data gaps |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for rufinamide is not available (data gap). Based on information embedded elsewhere in this evidence pack's mechanistic rationale fields, rufinamide is described as a broad-spectrum sodium-channel modulating anticonvulsant, with an approved indication in Lennox-Gastaut Syndrome (LGS).

FIRES is a severe, treatment-refractory epileptic encephalopathy that, like LGS, involves diffuse cortical hyperexcitability and is often managed with broad-spectrum antiepileptic agents when standard therapy fails. This provides a plausible mechanistic rationale for extending sodium-channel-targeted anticonvulsants such as rufinamide to FIRES. However, no repurposing rationale text, clinical trial, or literature evidence was provided for this specific top-ranked indication (rank 1), so this remains a theoretical extrapolation rather than an evidence-backed hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Rufinamide currently has no marketing authorizations in Taiwan (0 licenses on record); no product/dosage form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug-drug interaction data are marked as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN similarity score (L5) with zero clinical trials and zero literature evidence, and the drug is not currently marketed in Taiwan. A Blocking safety data gap (missing TFDA label/contraindication data) also prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA label (warnings, contraindications, DDI) via label PDF parsing
- Resolve DG002: obtain confirmed MOA via DrugBank API query
- Confirm formal original indication(s) for rufinamide (currently empty in source data)
- Generate or source clinical trial / literature evidence specific to FIRES before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

