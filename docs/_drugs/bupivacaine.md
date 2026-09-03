---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 4
---

# Bupivacaine
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

# Bupivacaine: Local Anesthetic Agent — No Repurposing Predictions Available

## One-Sentence Summary

Bupivacaine is a long-acting amide-type local anesthetic widely used for regional and neuraxial anesthesia. The current Evidence Pack contains **no TxGNN-predicted new indications** for this drug, and the drug is **not registered in Taiwan**. Without predicted indications or regulatory authorization data, a formal repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local/regional anesthesia (from general pharmacological knowledge; not present in Evidence Pack) |
| Predicted New Indication | — No prediction available |
| TxGNN Prediction Score | — |
| Evidence Level | — (No predictions to evaluate) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available in this Evidence Pack, so a mechanistic rationale for a new indication cannot be evaluated at this time.

For reference, bupivacaine is a voltage-gated sodium channel blocker (Nav1.x). It inhibits membrane depolarization in sensory and motor neurons, producing reversible conduction blockade. This mechanism is pharmacologically relevant to several non-anesthetic applications (e.g., chronic pain, anti-arrhythmic effects at low doses), but without a specific TxGNN-predicted disease target, no claim can be made.

The Evidence Pack also records two data gaps: mechanism of action (MOA) data is absent from the structured drug record, and no Taiwan package insert warnings were parsed into the safety fields. These gaps should be resolved before any repurposing pathway is assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposing indication (predicted_indications is empty).

---

## Literature Evidence

Currently no related literature available for a repurposing indication (predicted_indications is empty).

---

## Taiwan Market Information

Bupivacaine is **not currently registered** with the Taiwan Food and Drug Administration (TFDA). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The TFDA package insert query (query_log ID 4) returned a result but the structured safety fields were not populated. A manual review of the package insert PDF is required to extract warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications, no structured safety data, and no Taiwan regulatory authorizations. There is no repurposing candidate to evaluate at this stage.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for DB00297 (Bupivacaine) to obtain disease-level scores and candidate indications
- **Resolve DG001** — Parse the TFDA package insert PDF to extract key warnings, contraindications, and dosing limits
- **Resolve DG002** — Query DrugBank API for structured MOA and pharmacological category data
- **Verify DDI data** — DDI query returned `not_found`; cross-check against alternative interaction databases (e.g., DrugBank interactions, Taiwan NHI formulary)
- Once predicted indications are available, re-issue a full evaluation report with clinical trial and literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

