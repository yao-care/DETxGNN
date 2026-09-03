---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From Thrombopoietin Receptor Agonist Therapy to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

> Lusutrombopag's original approved indication is not documented in the current evidence pack, though its known mechanism is thrombopoietin (TPO) receptor agonism, a class typically used for thrombocytopenia management.
> The TxGNN model's top prediction is **Hereditary Thrombocytopenia with Normal Platelets**,
> but this direction is currently supported by **0 clinical trials** and **0 publications**, and the disease label itself is noted as internally contradictory in the model's own rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no approved indication text available; drug not marketed in Germany) |
| Predicted New Indication | Hereditary Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for Lusutrombopag is currently a data gap (DG002). However, the evidence pack's own rationale identifies Lusutrombopag as a **TPO receptor agonist**, a class that stimulates megakaryocyte production in bone marrow to increase platelet counts — this is consistent with its established pharmacological class (TPO-RAs such as eltrombopag, avatrombopag).

The top-ranked prediction, "hereditary thrombocytopenia with normal platelets," has a name that is semantically contradictory (a thrombocytopenia diagnosis paired with "normal platelets"), which the model's own rationale flags as a likely disease-ontology naming or classification artifact rather than a coherent clinical phenotype. This makes the biological interpretability of the #1 prediction weak despite its high similarity score.

Among the remaining nine predictions, only ranks 2–5 (macrothrombocytopenia with mitral valve insufficiency, transient neonatal thrombocytopenia, dense granule disease, platelet storage pool deficiency) have any plausible mechanistic link to platelet biology, and even these are described in the rationale as indirect or mechanistically mismatched (e.g., TPO-RAs increase platelet *quantity*, not *function*, so they are unlikely to correct storage pool or granule defects). Ranks 6–10 (ALS, lower motor neuron syndrome, polymicrogyria, spondylometaphyseal dysplasia) have no known biological pathway connecting TPO receptor signaling to their pathology, and the rationale explicitly attributes these to graph-proximity artifacts in the knowledge graph rather than genuine mechanistic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No marketing authorizations are currently recorded (total_licenses = 0; market status: not marketed). No product, dosage form, or approved indication data is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/BfArM-level labeling data (warnings, contraindications) is currently a **Blocking** data gap (DG001), meaning this candidate cannot yet proceed to a formal safety (S1) evaluation stage until label data is obtained and reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are at evidence level L5 (model score only, zero supporting trials or literature), the top prediction's disease label is internally inconsistent per the model's own rationale, and foundational drug-level data (original indication, MOA, Germany market status, safety label) are largely unavailable. There is no basis to advance beyond a research hypothesis at this time.

**To proceed, the following is needed:**
- TFDA/BfArM label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank — currently High priority gap (DG002)
- Clarification of disease ontology for "hereditary thrombocytopenia with normal platelets" before further evaluation
- Preclinical or case-level evidence for any of the top 5 platelet-related predictions before considering trial-stage advancement
- Re-screening of ranks 6–10 for possible knowledge-graph noise before inclusion in any future prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

