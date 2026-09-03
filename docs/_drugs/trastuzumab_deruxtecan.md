---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From HER2-Expressing Tumours to Drug-Induced Osteoporosis

## One-Sentence Summary

Trastuzumab deruxtecan is a HER2-targeted antibody-drug conjugate (ADC) that delivers a cytotoxic topoisomerase I inhibitor (DXd) to HER2-expressing tumour cells. The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the underlying rationale suggests the signal is likely a knowledge-graph artifact rather than a genuine treatment effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no formal indication text is on file (data gap) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is a data gap). Based on the mechanistic notes attached to this candidate, trastuzumab deruxtecan is known to function as a HER2-targeted ADC that delivers a cytotoxic topoisomerase I inhibitor payload to HER2-expressing tumour cells — a mechanism relevant to oncology, not bone metabolism.

There is no known or literature-supported mechanism by which this drug would modulate osteoclast/osteoblast activity or bone-remodeling pathways such as RANKL/OPG. Clinically, cytotoxic chemotherapies and ADCs are far more commonly associated with drug-induced osteoporosis as a **cause** (a treatment side effect) rather than as a **treatment** for it.

Given the high TxGNN score (0.993) combined with the complete absence of clinical trials or literature, the most plausible explanation is that the knowledge graph is picking up a co-occurrence relationship between "cancer therapy drug" nodes and "chemotherapy-associated bone loss" nodes, rather than a true therapeutic signal. This prediction should be treated as biologically implausible until contradicted by new evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Trastuzumab deruxtecan currently has no German market authorization on file (`total_licenses = 0`, `market_status = 未上市 / Not marketed`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC) delivering a cytotoxic topoisomerase I inhibitor payload |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic/ADC drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: A blocking data gap exists — TFDA label warnings and contraindications (DG001) have not been retrieved. This prevents any formal S1 safety pre-assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by no clinical trials, no literature, and no plausible mechanistic link — the drug's known cytotoxic ADC mechanism is more consistent with *causing* bone loss than treating it. Combined with a blocking data gap on TFDA safety labeling, this candidate is not ready to advance beyond stage S0.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) to resolve DG001
- Confirmed original indication and mechanism of action (DG002)
- Preclinical or mechanistic evidence linking HER2-ADC/topoisomerase I inhibition to bone metabolism pathways, if this signal is to be pursued further
- Independent review to rule out knowledge-graph co-occurrence artifact before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

