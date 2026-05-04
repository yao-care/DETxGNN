---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: Repurposing Evaluation Incomplete — No Predictions Available

## One-Sentence Summary

Budesonide (DrugBank: DB01222) is a synthetic glucocorticoid with established anti-inflammatory properties.
This Evidence Pack contains **no TxGNN-predicted new indications**, and two critical data items — mechanism of action and TFDA package insert safety data — have not been successfully extracted.
A full repurposing evaluation cannot proceed until these gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None — TxGNN predictions not loaded |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | Not marketed (0 TFDA authorizations found) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why the Evaluation Cannot Proceed

Three structural issues prevent this report from being completed in standard format:

**1. No predicted indications**
The `predicted_indications` field is empty. TxGNN has not returned any candidate new indications for Budesonide in this Evidence Pack. Without a repurposing hypothesis, there is no clinical trial evidence to surface, no mechanism bridge to explain, and no benefit-risk ratio to weigh.

**2. Mechanism of action unavailable (DG002 — High severity)**
DrugBank was queried successfully and returned one record, but MOA data was not extracted into the pack. Without MOA, mechanistic plausibility cannot be assessed for any future predicted indication.

**3. TFDA safety data missing (DG001 — Blocking severity)**
The TFDA package insert query returned a result, but warnings and contraindications were not parsed into the safety fields. This is classified as Blocking — the safety pre-screening step is formally incomplete, and no candidate can advance to clinical feasibility review under this status.

> **Data quality note:** The query log shows both the DrugBank query (ID 3) and the TFDA package insert query (ID 4) as `success` with `result_count: 1`. The data gaps therefore reflect an extraction or parsing failure, not a source availability problem. Re-running the extraction pipeline should recover this information without needing to re-query upstream sources.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions are present in this Evidence Pack. Even if predictions were added, two blocking/high-severity data gaps — missing safety extractions and missing MOA — would prevent the evaluation from clearing mandatory pre-screening gates.

**To proceed, the following is needed:**

- **Re-run extraction pipeline** on the already-retrieved DrugBank record and TFDA package insert PDF to populate MOA and safety fields — the source documents are confirmed available
- **Load TxGNN prediction results** for Budesonide into the Evidence Pack (`predicted_indications` must be populated before any evaluation work begins)
- **Re-verify Taiwan market status**: TFDA licensing query returned 0 results, but Budesonide has internationally marketed branded products (e.g., Rhinocort®, Pulmicort®, Entocort®); a re-query using alternative trade names or ATC code R03BA02 / A07EA06 may surface existing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

