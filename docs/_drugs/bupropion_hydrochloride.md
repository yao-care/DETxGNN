---
layout: default
title: Bupropion Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Bupropion Hydrochloride
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

# Bupropion Hydrochloride: Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Bupropion Hydrochloride is a drug with no approved indications on record in Taiwan and no TxGNN repurposing predictions available in this Evidence Pack. A complete repurposing evaluation cannot be conducted at this stage — essential data including mechanism of action, original indications, and model output are all absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no Taiwan licenses found |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (model prediction absent; no supporting studies retrievable) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

The Evidence Pack for this candidate is structurally incomplete in two critical areas:

**No TxGNN predictions were returned.** The `predicted_indications` array is empty, meaning either the TxGNN pipeline has not been run for this drug, or no above-threshold indications were identified. Without at least one predicted indication, the core sections of a repurposing report — mechanistic rationale, clinical trial linkage, literature mapping — cannot be populated.

**Drug-level metadata is missing.** Although the query log records a successful DrugBank lookup (1 result) and a successful TFDA package insert retrieval (1 result), neither the mechanism of action nor the original approved indications have been integrated into the Evidence Pack fields. The `original_moa` field remains `[Data Gap]` and `original_indications` is an empty array. This prevents any mechanistic analysis.

---

## Taiwan Market Information

No authorizations on record. The TFDA query returned 0 results, and market status is confirmed as **Not marketed** in Taiwan.

---

## Safety Considerations

Please refer to the package insert for safety information.

(Safety warnings and contraindications were not populated despite a successful TFDA package insert query being logged. DDI data was not found.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline has not produced any repurposing predictions for this candidate, and the minimum data requirements for a Level 5 evaluation are not met. Proceeding without predictions or baseline drug characterization would produce a report with no actionable content.

**To proceed, the following is needed:**

- **[Critical]** Run TxGNN prediction pipeline for Bupropion Hydrochloride and confirm at least one ranked indication is returned
- **[Critical]** Integrate DrugBank results into the `drug.original_moa` and `drug.drugbank_id` fields — the query log confirms 1 record was retrieved but not parsed into the pack
- **[Critical]** Integrate TFDA package insert results into `drug.original_indications`, `safety.key_warnings`, and `safety.contraindications` — query log confirms 1 record retrieved but not parsed
- **[High]** Assign a `drugbank_id` to enable cross-referencing with clinical trial and literature evidence sources
- **[Medium]** Re-run DDI query after DrugBank ID is confirmed, as the current `not_found` result may be due to a name-matching failure rather than a true absence of interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

