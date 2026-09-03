---
layout: default
title: Lurbinectedin
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: From Small Cell Lung Cancer to Multiple Endocrine Neoplasia

## One-Sentence Summary

Lurbinectedin is a cytotoxic chemotherapy agent, described in the evidence rationale as currently used for small cell lung cancer.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — score alone, with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small Cell Lung Cancer (SCLC) — mentioned in the model's rationale narrative; not confirmed via formal license/regulatory data (data gap) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only; no supporting trials or literature) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the formal drug record (data gap DG002, High severity). Based on the model's own rationale annotations, lurbinectedin is a DNA minor-groove binding transcriptional inhibitor that induces transcription-coupled DNA damage via RNA Pol II inhibition — a conventional cytotoxic chemotherapy mechanism, currently applied in small cell lung cancer.

For the top-ranked prediction, however, the evidence pack explicitly states there is **no known mechanistic relationship** between this transcription-inhibition/DNA-damage mechanism and multiple endocrine neoplasia (a germline RET/MEN1-driven endocrine tumor syndrome). The prediction rests solely on TxGNN graph-similarity inference, with no clinical or literature corroboration.

Given lurbinectedin's cytotoxic and immunosuppressive properties, extending it to a non-oncologic, genetically-driven endocrine syndrome lacks biological plausibility at this stage. The same caveat applies to all nine other ranked predictions in this evidence pack — several of which are not even human diseases (e.g., feline immunodeficiency syndrome, infectious bovine rhinotracheitis), suggesting cross-species noise in the underlying knowledge graph rather than genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Lurbinectedin currently holds no marketing authorization in Germany (0 licenses on record); market status is **Not Marketed**.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA minor-groove binding transcription inhibitor (per rationale narrative; not independently confirmed via DrugBank category data) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function (standard for cytotoxic chemotherapy; product-specific data not confirmed) |
| Handling Protection | Standard cytotoxic drug handling precautions apply, given its confirmed classification as a cytotoxic chemotherapy agent |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings and contraindications are currently a **Blocking data gap (DG001)**, which prevents any formal S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for lurbinectedin are Evidence Level L5 (prediction-only, zero clinical trials, zero literature). The top-ranked candidate — multiple endocrine neoplasia — is explicitly flagged in its own rationale as lacking mechanistic, clinical, or literature support, and several lower-ranked predictions are not even human diseases, indicating likely knowledge-graph noise rather than a credible repurposing signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety pre-assessment
- Confirmed mechanism of action via DrugBank or primary literature (DG002, High)
- Independent verification of original indication and regulatory approval history
- Preclinical or mechanistic evidence establishing biological plausibility for the multiple endocrine neoplasia link before further investment
- Re-screening of lower-ranked predictions to filter out non-human-disease entries (cross-species graph noise)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

