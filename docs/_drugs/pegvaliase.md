---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Pegvaliase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Pegvaliase: From Phenylketonuria to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase (DB12839) is a PEGylated phenylalanine ammonia lyase (PAL) enzyme therapy, clinically used to lower blood phenylalanine levels in patients with phenylketonuria (PKU). The TxGNN model predicts a high association score for **diabetic retinopathy**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no mechanistic link between phenylalanine metabolism and diabetic retinopathy has been established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (PKU) *(inferred from known clinical use — no formal indication text or MOA record available in this evidence pack)* |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (flagged as a High-severity data gap). Based on the repurposing rationale accompanying the prediction, pegvaliase is a PEGylated phenylalanine ammonia lyase (PAL) enzyme that converts phenylalanine into trans-cinnamic acid and ammonia, and is used clinically to control blood phenylalanine levels in PKU patients.

There is no known biological relationship between phenylalanine metabolism and the pathophysiology of diabetic retinopathy, which is primarily driven by chronic hyperglycemia, VEGF-mediated angiogenesis, and vascular inflammation. The same lack of mechanistic connection applies to two closely related predictions also generated for this drug — **severe nonproliferative diabetic retinopathy** (score 99.16%) and **diabetic cataract** (score 99.11%, linked instead to the aldose reductase/polyol pathway, which is likewise unrelated to PAL activity).

The high TxGNN scores across all three diabetic-eye-disease predictions most likely reflect topological similarity within the knowledge graph (e.g., shared graph neighbors or embedding proximity) rather than an underlying pharmacological rationale. Without any clinical, preclinical, or literature evidence to corroborate the connection, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

No marketed products for pegvaliase are currently registered in Taiwan (0 authorizations, market status: Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap — required before any safety pre-assessment (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5, no clinical trials, no literature, no mechanistic plausibility). The drug is also not currently marketed in Taiwan, and core safety data (TFDA label, MOA) are missing, so this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (Blocking data gap, DG001)
- Confirmed mechanism of action from DrugBank or primary literature (High-priority data gap, DG002)
- Preclinical or mechanistic evidence linking PAL/phenylalanine metabolism to diabetic retinal or lenticular pathology
- At minimum, an observational study or case series before considering progression beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

