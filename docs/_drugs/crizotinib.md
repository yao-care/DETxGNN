---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK/ROS1-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is an ALK/ROS1/MET tyrosine kinase inhibitor established for ALK/ROS1-rearranged non-small cell lung cancer (NSCLC).
The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but this candidate currently has **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a pure embedding-score signal with no known biological basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this jurisdiction (drug unlicensed here; internationally, crizotinib is indicated for ALK/ROS1-positive NSCLC per literature evidence in this pack) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action record is available for this drug in the evidence pack. Based on repeated descriptions across the predicted-indication rationales, crizotinib is known to act as an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases ALK, ROS1, and MET, with established clinical efficacy in ALK/ROS1-rearranged NSCLC.

For the top-ranked prediction, **gingival fibromatosis**, no mechanistic or biological link to the ALK/ROS1/MET pathway has been identified. The model's own repurposing rationale explicitly states this is "a pure TxGNN embedding high-score prediction, lacking any biological hypothesis support." There are no clinical trials or literature entries supporting this candidate.

It is worth noting that among the 10 predictions generated for this drug, several lower-ranked candidates show materially stronger and more biologically coherent signals — most notably **lung hilum carcinoma** (rank 4, evidence level L3, decision stage S2, "Research Question"), which reflects the drug's already-established ALK/ROS1-driven NSCLC mechanism rather than a genuinely novel indication. By contrast, the rank-1 candidate reported here (gingival fibromatosis) appears to be embedding noise and does not warrant further action at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

This drug currently has no marketing authorization in this market (0 licenses on record).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (gingival fibromatosis) has no clinical trial or literature support, and the model's own rationale identifies it as an unsupported embedding-score artifact. Combined with the absence of local market authorization and core drug-level data (MOA, original indication, safety), there is insufficient basis to advance this specific candidate.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA/BfArM label warnings and contraindications (required before any S1 safety pre-assessment)
- Resolve high-severity data gap DG002: formal mechanism-of-action record from DrugBank
- If repurposing interest continues, redirect evaluation toward the better-evidenced candidate identified in this dataset — **lung hilum carcinoma** (L3, decision stage S2) — rather than the current top-ranked prediction
- Manual ontology/mapping review, since several other predictions in this dataset (e.g., ranks 5, 8, 10) show literature sets that do not match the predicted disease label, suggesting systematic mapping noise that should be corrected before future scoring runs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

