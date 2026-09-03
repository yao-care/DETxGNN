---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an antifibrotic agent whose established clinical use — per literature citation (PMID 29702057) — is idiopathic pulmonary fibrosis (IPF); no official regulatory indication text is available in this dataset. The TxGNN model's top prediction is **Extracutaneous Mastocytoma**, but this candidate is currently supported by **zero clinical trials and zero publications** — the score reflects a pure knowledge-graph prediction with no external validation.

> ⚠️ Note: All 10 predicted indications in this evidence pack are rated **L5 (model prediction only)** except rank 9 (fibroblastic neoplasm), which reached L4 — driven mainly by **negative safety signals** (case reports of sarcoma occurrence and dermatofibroma aggravation), not positive efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) — *sourced from literature citation only; official regulatory indication text not available (data gap)* |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on external literature embedded in this evidence pack, pirfenidone is known to inhibit TGF-β1–mediated signalling (including non-SMAD pathways), reduce fibroblast proliferation, and decrease collagen deposition — a mechanism well-documented for fibrotic disorders such as IPF and Dupuytren's disease.

For the top-ranked candidate, **extracutaneous mastocytoma**, this mechanism does not map cleanly onto the disease biology. Mastocytoma is driven by mast cell proliferation (often KIT-pathway related), not by fibroblast/TGF-β–mediated fibrosis. The evidence pack's own rationale explicitly flags this as a "weak, purely inferential" link, likely reflecting graph-embedding proximity between fibrosis-related and mast-cell-related nodes rather than a genuine pharmacological relationship.

Notably, among the ten predictions, most (mastocytoma, fibrosarcoma subtypes, dermatofibrosarcoma protuberans) cluster around a "TGF-β/anti-fibroblast" hypothesis for soft-tissue neoplasms. However, the only prediction with actual literature support (rank 9, fibroblastic neoplasm) surfaces a **safety concern in the opposite direction** — case reports of pirfenidone-associated undifferentiated pleomorphic sarcoma and aggravated dermatofibroma — which undermines the "anti-fibrotic = anti-tumour" assumption underlying several of these predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (Extracutaneous Mastocytoma).

*(Note: literature evidence exists only for rank 9 — Fibroblastic Neoplasm — see Safety Considerations below.)*

---

## Germany Market Information

Pirfenidone currently has **no marketing authorizations** on record in this dataset (total_licenses: 0). No product/dosage-form information is available.

---

## Safety Considerations

All primary safety fields (key warnings, contraindications, DDI) are marked as data gaps in this dataset:

> Please refer to the package insert for safety information.

**Notable literature-derived safety signal** (from evidence tied to a lower-ranked prediction, not from formal safety data):
- A case report describes **undifferentiated pleomorphic sarcoma** occurring after pirfenidone use (PMID 29702057).
- A separate case report describes **aggravation of multiple eruptive dermatofibromas** in a patient on pirfenidone + mycophenolate mofetil (PMID 32572469).

These are isolated case reports, not causally established, but they warrant caution before pursuing any fibroblastic/soft-tissue-neoplasm-related repurposing hypothesis for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this evidence pack is either unsupported by any clinical trial or literature (L5), or supported only by literature that raises a safety concern rather than efficacy evidence (L4, rank 9). Combined with missing MOA data, missing regulatory/safety documentation, and zero market authorizations, there is currently no basis to advance any candidate beyond model-prediction stage.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed MOA from DrugBank API — currently high-severity gap (DG002)
- Confirmed original indication and regulatory approval text (currently absent from `taiwan_regulatory.licenses`)
- Preclinical or clinical evidence specifically for extracutaneous mastocytoma before any further evaluation
- Clarification of the sarcoma-occurrence/dermatofibroma-aggravation safety signal before pursuing any fibroblastic-neoplasm-family indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

