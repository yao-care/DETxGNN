---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Complement-Mediated Disease to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5-inhibiting monoclonal antibody, historically established for hemolytic/complement-driven disorders such as PNH and aHUS (per background literature in this evidence pack, though formal indication and label data are not provided here). The TxGNN model's top prediction is **Cyclic Hematopoiesis**, a genetic (ELANE-driven) neutropenia disorder — but this prediction is currently supported by **zero clinical trials** and **zero publications**, making it a pure model-generated hypothesis with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally provided in this evidence pack (drug is a known anti-C5 complement inhibitor; literature within this pack references PNH, aHUS, and refractory generalized myasthenia gravis as established uses — not independently confirmed as official label data) |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa: [Data Gap]`). Based on information embedded in the accompanying literature, eculizumab is a monoclonal antibody that binds complement protein C5, blocking its cleavage and preventing formation of the terminal membrane attack complex (MAC) — a mechanism established in complement-mediated hemolytic and thrombotic microangiopathy diseases (e.g., PNH, aHUS).

Cyclic hematopoiesis, however, is caused by *ELANE* gene mutations that disrupt neutrophil elastase processing and cyclic regulation of granulopoiesis — a cell-intrinsic myeloid maturation defect with no established link to complement activation. As explicitly noted in the rationale accompanying this prediction, "no known intersection" exists between the terminal complement pathway and cyclic granulopoiesis regulation.

This prediction therefore represents a graph-embedding proximity signal (TxGNN network similarity) rather than a mechanistically grounded hypothesis. The same pattern holds across ranks 2–9 of the candidate list (JAGN1 deficiency, X-linked SCN, CXCR2 deficiency, CSF3R deficiency, etc.) — all are congenital neutropenia/immunodeficiency syndromes driven by distinct, non-complement pathways, and none have any supporting trials or literature. For ranks 4 and 10, literature *was* retrieved, but on review it consists entirely of eculizumab's already-known indications (PNH, aHUS, TMA, myasthenia gravis) and unrelated CD59-mutation case reports — a keyword-matching artifact rather than direct evidence for the predicted disease itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: two lower-ranked candidates in this evidence pack — congenital neutropenia-myelofibrosis-nephromegaly syndrome, rank 4; and primary release disorder of platelets, rank 10 — did return literature hits, but all were confirmed mismatches referencing eculizumab's existing approved indications rather than the candidate diseases themselves, and are therefore not counted as supporting evidence for the top prediction.)*

---

## Germany Market Information

Eculizumab is currently **not marketed** in Germany under this evidence pack's regulatory data, with no authorization records available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are flagged as a **Blocking** data gap in this evidence pack — TFDA/label data has not yet been retrieved, which prevents progression to the S1 safety screening stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (cyclic hematopoiesis) has no mechanistic rationale, no clinical trials, and no literature support — meeting only the lowest evidence tier (L5, model prediction only). Combined with missing MOA data and a **Blocking** safety data gap (no label/contraindication data), this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Retrieve formal drug label / TFDA warnings and contraindications to clear the Blocking data gap (DG001)
- Retrieve structured MOA data from DrugBank to enable proper mechanistic-link analysis (DG002)
- Independent biological plausibility study (in vitro/in vivo) connecting complement C5 inhibition to ELANE-driven granulopoiesis, if this hypothesis is to be pursued further
- Re-run literature/trial search with disease-specific synonyms to rule out further keyword-mismatch artifacts before any candidate in this batch is escalated beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

