---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
---

# Risdiplam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# RISDIPLAM: Evaluation Pending — Critical Data Gaps Prevent Full Assessment

## One-Sentence Summary

Risdiplam (DrugBank ID: DB15305) is currently not marketed in Taiwan, and the TxGNN model returned **no predicted indications** in this Evidence Pack.
Original indications, mechanism of action, and safety data are all absent, making it impossible to conduct a meaningful repurposing evaluation at this stage.
This report documents the current state and specifies the data required to proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in this Evidence Pack |
| Predicted New Indication | No TxGNN predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (no actual studies linked) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The `predicted_indications` array in this Evidence Pack is empty. Without a TxGNN-predicted target indication, the standard repurposing pipeline cannot proceed.

In addition, the `original_indications` field is also empty and the mechanism of action is flagged as a data gap. Two upstream data gaps (DG001: package insert warnings/contraindications; DG002: MOA) were identified at the time of Evidence Pack generation, both rated **Blocking** or **High** severity. These gaps must be resolved before any mechanistic similarity analysis can be written.

Based on general knowledge, Risdiplam is a well-characterised oral small-molecule SMN2 pre-mRNA splicing modifier approved in multiple markets for Spinal Muscular Atrophy (SMA). However, this information is **not present in the submitted Evidence Pack** and therefore cannot be used as the basis for an evaluation recommendation. The data pipeline needs to be re-run with the remediation steps below completed first.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The minimum required data to perform a drug repurposing evaluation is absent — `predicted_indications` is empty and the two upstream blocking data gaps (DG001, DG002) were not resolved before this Evidence Pack was finalised.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse the TFDA package insert PDF to extract key warnings and contraindications; re-run the safety module
- **[DG002 — High]** Query the DrugBank API for Risdiplam (DB15305) to retrieve MOA, drug categories, and toxicity data; populate `original_moa`
- **Re-run TxGNN inference** after `original_indications` and `original_moa` are populated so that `predicted_indications` returns at least one candidate
- **Verify original indication list** — confirm the approved indication(s) (e.g., SMA) are correctly loaded into the pipeline before re-scoring
- Once the above are complete, regenerate the Evidence Pack and re-submit for a full evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

