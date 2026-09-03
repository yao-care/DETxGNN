---
layout: default
title: Riociguat
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 0
---

# Riociguat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Riociguat: Evaluation Incomplete — Insufficient Data for Repurposing Analysis

## One-Sentence Summary

Riociguat (DrugBank ID: DB08931) has been identified as a candidate for drug repurposing evaluation.
However, the current Evidence Pack contains **no TxGNN-predicted indications**, **no original indication records**, and **no safety data**,
making it impossible to conduct a meaningful mechanistic or clinical evidence assessment at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not assessable |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Assessment Is Possible

The Evidence Pack for Riociguat is missing three critical data categories:

**1. No original indication data**
The `original_indications` field is empty, and no approved product label (package insert) data has been parsed into structured form. Without knowing the drug's approved therapeutic context, mechanistic bridging to a new indication cannot be attempted.

**2. No mechanism of action (MOA)**
MOA data is flagged as a high-severity gap (`DG002`). Without knowing how Riociguat exerts its pharmacological effect, it is not possible to reason about mechanistic applicability to other diseases.

**3. No TxGNN predictions**
The `predicted_indications` array is empty. This means the TxGNN knowledge-graph model either has not yet processed this drug, or the drug did not pass the minimum score threshold to generate candidate indications. Until predictions are generated, no evidence review can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A package insert query (`tfda_package_insert`) was executed on 2026-03-29 with status `success`, indicating source material exists. However, structured safety fields (warnings, contraindications, DDI) have not been parsed from this source into the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are currently no TxGNN-predicted indications and no structured drug-level data available; proceeding to any stage of repurposing analysis would be premature and methodologically unsound.

**To proceed, the following is needed:**

1. **Parse the package insert** — The `tfda_package_insert` query returned one result (2026-03-29). Extract and structure the approved indications, warnings, and contraindications from this document into the Evidence Pack.
2. **Retrieve MOA from DrugBank** — DrugBank query returned one result (`result_count: 1`). Extract the mechanism of action, pharmacological class, and drug categories to populate `original_moa`.
3. **Re-run TxGNN prediction pipeline** — Once drug-level metadata is populated, re-submit Riociguat to the TxGNN model to generate scored indication candidates.
4. **Re-run DDI query** — The current DDI query returned `not_found`. After MOA and drug class are confirmed, re-query the DDI database with enriched drug profile parameters.
5. **Generate updated Evidence Pack (v5)** — Only after steps 1–4 are complete should a full evaluation report be generated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

