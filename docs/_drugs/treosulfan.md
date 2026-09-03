---
layout: default
title: Treosulfan
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 1
---

# Treosulfan
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

# Treosulfan: From Hematopoietic Stem Cell Transplant Conditioning to Diabetic Cataract

## One-Sentence Summary

> Treosulfan is a bifunctional alkylating agent clinically used as conditioning chemotherapy prior to hematopoietic stem cell transplantation.
> The TxGNN model predicts it may be effective for **Diabetic Cataract**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from German license data (drug is not marketed); known clinical use is conditioning chemotherapy before hematopoietic stem cell transplant |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, treosulfan is a bifunctional epoxide-type alkylating agent, whose activity is tied to DNA cross-linking and cytotoxic cell kill — the basis for its use as conditioning chemotherapy before hematopoietic stem cell transplantation.

There is no established mechanistic link between this cytotoxic/DNA-damaging action and the pathology of diabetic cataract, which is driven by lens osmotic stress, oxidative stress, and the polyol pathway. No shared pharmacological pathway connects an alkylating conditioning agent to cataract prevention or treatment.

Notably, this direction carries a plausible mechanistic **red flag rather than support**: alkylating agents are more commonly reported in the literature as being *associated with* cataract formation (as a long-term toxicity of conditioning regimens) rather than as a treatment for cataract. Given the drug is not marketed and the prediction has zero corroborating trial or literature evidence, this candidate should be treated as a pure model output requiring independent mechanistic and safety validation before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Treosulfan is currently not marketed in Germany; no license information is available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (bifunctional epoxide alkylating agent) |
| Myelosuppression Risk | High — alkylating conditioning regimens are typically associated with profound, dose-dependent myelosuppression |
| Emetogenicity Classification | Moderate to high, consistent with alkylator-based conditioning regimens |
| Monitoring Items | CBC with differential, renal function, hepatic function |
| Handling Protection | Standard cytotoxic drug handling precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support (L5, prediction-only), the drug is not currently marketed in Germany, and the proposed mechanism runs counter to known alkylator toxicity (cataract as an adverse effect, not a treatment target).

**To proceed, the following is needed:**
- TFDA/manufacturer package insert warnings and contraindications (blocking data gap — required before any S1 safety review)
- Detailed mechanism of action data to properly assess mechanistic plausibility
- Preclinical or mechanistic evidence specifically linking alkylating activity to diabetic cataract pathology, given the conflicting signal noted above
- Clarification of German/EU marketing status or an alternative regulatory pathway, since the drug is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

