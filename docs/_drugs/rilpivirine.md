---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 5
---

# Rilpivirine
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

# Rilpivirine: Drug Repurposing Evaluation — Insufficient Evidence Pack

## One-Sentence Summary

Rilpivirine (DrugBank: DB08864) is an antiretroviral agent belonging to the NNRTI class, used in the treatment of HIV-1 infection.
This Evidence Pack does not contain any TxGNN-predicted repurposing indications, and the drug carries no regulatory authorizations in Taiwan.
A **Hold** decision is recommended until prediction outputs and safety documentation are obtained.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in regulatory data |
| Predicted New Indication | No predictions available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No supporting studies; model output absent |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Taiwan Market Information

No authorized products found for Rilpivirine in the Taiwan regulatory database. Zero licenses are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The TFDA package insert query returned a record (see query log ID 4), but warning and contraindication content has not been parsed into this Evidence Pack. Drug interaction data was not found (query log ID 2).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The `predicted_indications` array is empty — there are no TxGNN repurposing candidates to evaluate for this compound. Without a target indication, neither mechanistic relevance, clinical evidence, nor a benefit-risk assessment can be conducted.

**To proceed, the following is needed:**

- **TxGNN output**: Re-run TxGNN inference for Rilpivirine (DB08864) and confirm whether any indication scores meet the reporting threshold
- **MOA data** (DG002 – High severity): Retrieve mechanism of action from DrugBank API to enable mechanistic plausibility analysis
- **Safety documentation** (DG001 – Blocking): Parse the TFDA package insert PDF already retrieved (query log ID 4) to extract key warnings, contraindications, and special population restrictions before any S1 safety screening
- **Target market review**: Confirm whether Germany (BfArM) or Taiwan (TFDA) is the intended regulatory jurisdiction for this candidate, and align the Evidence Pack accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

