---
layout: default
title: Bictegravir
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 3
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome (Feline AIDS)

## One-Sentence Summary

Bictegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), used clinically as part of antiretroviral therapy in people living with HIV. The TxGNN model predicts it may be effective against **feline acquired immunodeficiency syndrome** (a lentiviral disease in cats caused by FIV), with a very high prediction score but **no clinical trials or literature currently supporting this specific indication**. A closely related, identically-scored prediction — **simian immunodeficiency virus (SIV) infection** — is supported by 3 mechanistic/preclinical publications and is discussed below as corroborating evidence for the same biological hypothesis (lentiviral integrase inhibition).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from literature evidence in this pack; TFDA-approved indication text not yet available — see Data Gap DG001) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (Feline AIDS) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature specific to this indication) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for bictegravir is not yet available in this evidence pack (Data Gap DG002). Based on the literature evidence retrieved, bictegravir is a second-generation **integrase strand transfer inhibitor (INSTI)** used in combination antiretroviral therapy for HIV-1, and it imparts a high genetic barrier to resistance compared to earlier INSTIs such as raltegravir and elvitegravir.

Feline AIDS is caused by **feline immunodeficiency virus (FIV)**, a lentivirus in the same retroviral family as HIV, sharing a homologous integrase enzyme mechanism. This provides a plausible mechanistic rationale for TxGNN's prediction — an integrase inhibitor effective against one lentivirus may plausibly inhibit integration of a related lentivirus. However, **no clinical trials, ICTRP trials, or published literature directly evaluate bictegravir in FIV/feline AIDS**, so this remains a mechanism-only hypothesis (Evidence Level L5).

Notably, TxGNN assigned an **identical score (99.82%)** to a second, closely related prediction: **simian immunodeficiency virus (SIV) infection**. Unlike feline AIDS, this prediction is supported by 3 publications describing bictegravir's antiviral activity against SIV and SIV/HIV intasome structural biology, effectively corroborating the underlying mechanistic hypothesis (cross-lentivirus integrase inhibition) even though the pack does not provide feline-AIDS-specific data. This supporting literature is presented below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome (or for the related SIV infection prediction).

---

## Literature Evidence

No literature is directly indexed against feline AIDS in this pack. The following 3 publications support the closely related, identically-scored prediction (SIV infection), and are included here as mechanistic corroboration for the cross-lentivirus integrase-inhibition hypothesis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Preclinical/Mechanism | Antimicrobial Agents and Chemotherapy | Bictegravir shows antiviral activity against integrase-inhibitor-resistant SIVmac239 and HIV-1, with a higher genetic barrier to resistance than raltegravir/elvitegravir |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Review/Structural biology | The FEBS Journal | Structural analysis of HIV/SIV intasome complexes explains bictegravir binding and viral escape mechanisms |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical (animal model) | Frontiers in Immunology | Humanized mouse model developed for testing antiretroviral strategies against both SIV and HIV |

---

## Germany Market Information

Bictegravir currently has **no marketing authorizations** on record (market status: Not Marketed, 0 licenses). No authorization table can be generated.

---

## Safety Considerations

Safety data (key warnings, contraindications, drug interactions) are not yet available for this candidate. This is flagged as a **Blocking** data gap (DG001 — TFDA labeling warnings/contraindications), which currently prevents entry into S1 safety pre-assessment. Please refer to the package insert for safety information once available.

---

## Note: Screened-Out Prediction (Not Pursued)

A third TxGNN prediction in this pack — a rare neurodevelopmental disorder (ataxic gait, absent speech, decreased cortical white matter) — was already scored by the pipeline as **L5 / S0 / Hold**, with the rationale that this genetic neurodevelopmental condition has no known pathological link to viral integrase inhibition and no supporting trials or literature. It is treated as a likely false-positive TxGNN output and is excluded from further consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The feline AIDS prediction is mechanistically plausible (lentivirus integrase homology) and reinforced by literature on the closely related SIV prediction, but it has zero indication-specific clinical or literature evidence, no confirmed original-indication regulatory text, and no German market authorization. Most critically, the **Blocking** safety data gap (DG001) prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/BfArM label warnings and contraindications (resolve DG001, currently Blocking)
- Confirmed mechanism-of-action documentation from DrugBank (resolve DG002)
- Confirmation of original approved indication text (HIV-1 infection) from a regulatory source
- Any veterinary or preclinical efficacy data specific to FIV/feline AIDS, if this candidate is to be pursued as a veterinary repurposing case rather than purely as a human-medicine hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

