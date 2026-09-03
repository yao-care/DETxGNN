---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 1
---

# Lapatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Lapatinib: From HER2-Overexpressing Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

> Lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor originally used for HER2-overexpressing breast cancer.
> The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-overexpressing breast cancer *(derived from repurposing rationale text; not confirmed by formal regulatory/label data)* |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (MOA) is not available in structured form. Based on the evidence pack's rationale text, lapatinib is a dual EGFR/HER2 (ErbB1/ErbB2) tyrosine kinase inhibitor, primarily used for HER2-overexpressing breast cancer.

However, the biological link between this MOA and DFSP is weak. DFSP is driven predominantly by the **COL1A1-PDGFB fusion gene**, which causes constitutive activation of PDGFRB — a pathway targeted by imatinib (a PDGFR inhibitor), not by EGFR/HER2 inhibitors. There is currently no known literature demonstrating clinically meaningful EGFR or HER2 overexpression or driver mutations in DFSP tumor cells.

This prediction should therefore be interpreted as a **TxGNN knowledge-graph association only**, lacking independent biological plausibility support at this stage, and should be treated with a high degree of skepticism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

Lapatinib is currently **not marketed** in Germany under this evidence pack (0 authorizations found); no product/dosage form/indication data is available.

## Cytotoxicity

Lapatinib is an antineoplastic agent (breast cancer indication), classified as a targeted therapy rather than a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (dual EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM label warnings and contraindications are currently unavailable — this is flagged as a Blocking data gap and must be resolved before any safety review can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials or literature), the proposed mechanism does not align with the known driver pathway of DFSP (COL1A1-PDGFB/PDGFRB, not EGFR/HER2), and the drug is not currently marketed in Germany. In addition, TFDA label safety data (warnings/contraindications) is missing, which is a blocking gap for any safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap, required before S1 safety review
- Confirmed original MOA and indication data from DrugBank/regulatory source
- Preclinical evidence of EGFR/HER2 relevance in DFSP tumor biology, if any exists
- Clinical trial or case-report evidence specifically evaluating lapatinib in DFSP or PDGFR-driven sarcomas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

