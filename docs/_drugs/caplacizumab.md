---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: Repurposing Evaluation Halted — Critical Data Gaps

## One-Sentence Summary

Caplacizumab (DrugBank ID: DB06081) was successfully retrieved from DrugBank, but the current Evidence Pack contains no original indication data, no mechanism of action, and no TxGNN-predicted new indications. The repurposing evaluation cannot be completed until the identified critical data gaps are resolved — a **Hold** decision is recommended at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | Insufficient data |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism-to-indication analysis cannot be completed at this stage.

The DrugBank query for Caplacizumab (DB06081) returned a successful hit, and a TFDA package insert query also returned one result — however, neither mechanism of action nor original approved indication was extracted into the structured Evidence Pack. Without a baseline indication, the conceptual bridge between the drug's existing clinical role and any repurposing hypothesis cannot be established.

No TxGNN-predicted new indications are present in the current data (`predicted_indications: []`). This means there is no candidate disease target to evaluate, and no clinical trial or literature evidence can be assessed. Until the TxGNN pipeline is executed for DB06081 and the prediction results are returned, the core question — "what new indication might this drug treat?" — remains unanswered.

---

## Germany Market Information

Caplacizumab is currently not approved in Germany. No product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Caplacizumab is missing its original indication, TxGNN-predicted new indications, and mechanism of action — the three minimum inputs required to generate a meaningful repurposing evaluation report.

**To proceed, the following is needed:**

- **Extract original indication** from the TFDA package insert query result (query ID 4 already returned 1 result; data extraction is the pending step)
- **Extract MOA** from the DrugBank query result (query ID 3 already returned 1 result; structured parsing is the pending step)
- **Run TxGNN prediction pipeline** for DB06081 to generate candidate new indication targets
- **Extract safety data** (warnings, contraindications) from the TFDA package insert (same source as above)
- **Re-run DDI query** once drug class is confirmed; current `not_found` status may reflect an incomplete query term
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

