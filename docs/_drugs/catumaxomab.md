---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 3
---

# Catumaxomab
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

Using no additional skill — this is a direct report-drafting task with explicit formatting rules already given in the prompt.

# Catumaxomab: From Malignant Ascites to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Catumaxomab is a trifunctional bispecific antibody (anti-EpCAM × anti-CD3) originally used for malignant ascites in EpCAM-positive carcinomas, but was withdrawn from the market in 2017 for commercial reasons.
> The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence is at the algorithmic-prediction stage only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not officially approved in Taiwan; per drug background, originally indicated for malignant ascites (withdrawn from market in 2017 for commercial reasons) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the available background information, catumaxomab is a trifunctional bispecific antibody that simultaneously binds tumor-cell surface EpCAM, T-cell CD3, and Fcγ receptors on accessory immune cells, thereby triggering immune-mediated killing of EpCAM-positive tumor cells. Its proven efficacy is limited to intraperitoneal use in malignant ascites, an oncology/tumor-immunology application.

Diabetic retinopathy is driven by chronic hyperglycemia-induced microvascular damage and VEGF-mediated neovascularization — a pathophysiology with no known mechanistic overlap with EpCAM/CD3-directed T-cell engagement. No VEGF, inflammatory, or angiogenesis pathway overlap has been identified for catumaxomab.

Given this, the mechanistic plausibility of applying catumaxomab to diabetic retinopathy is very low. The prediction reflects a TxGNN algorithmic association without biological rationale, clinical evidence, or practical feasibility — a systemically administered immune-activating antibody with known toxicity risk (originally given intraperitoneally for a terminal oncologic indication) is not a plausible candidate for a chronic ophthalmic condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Catumaxomab is not currently marketed in Taiwan and has no authorization records (`total_licenses = 0`). Per drug background information, it was withdrawn from the global market in 2017 for commercial reasons after prior approval for malignant ascites.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Catumaxomab's original indication (malignant ascites in EpCAM-positive carcinomas) qualifies it as an antineoplastic/immuno-oncology agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (trifunctional bispecific T-cell engaging antibody, anti-EpCAM × anti-CD3) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings/contraindications data is currently unavailable and is flagged as a **Blocking** data gap (DG001), meaning this candidate cannot yet proceed to the S1 safety review stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has evidence level L5 (algorithmic prediction only) with zero supporting clinical trials or literature, and the proposed mechanism (EpCAM/CD3-directed T-cell engagement) shows no known relevance to diabetic retinopathy's vascular/metabolic pathology. The drug is also not marketed anywhere and was previously withdrawn for commercial reasons, further limiting practical feasibility.

**To proceed, the following is needed:**
- TFDA/original manufacturer label data on warnings and contraindications (DG001, blocking — required before any S1 safety evaluation)
- Confirmed mechanism of action data (DG002)
- Preclinical or mechanistic evidence linking EpCAM/CD3-directed immunotherapy to diabetic retinopathy pathology
- Assessment of feasibility of reintroducing a discontinued biologic for a new, unrelated chronic indication

*Note: The two lower-ranked predictions in this evidence pack — drug-induced osteoporosis (rank 2, L5) and diabetic retinopathy (rank 3, L5) — show similarly weak mechanistic rationale, no supporting trials/literature, and are also recommended Hold.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

