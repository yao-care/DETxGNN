---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection (NNRTI-Class) to Congenital HIV Infection (Perinatal Transmission Prevention)

## One-Sentence Summary

> Etravirine is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) used for HIV-1 infection, particularly in NNRTI-experienced adults. Among the 10 TxGNN-predicted indications in this evidence pack, most (including the top-ranked "feline acquired immunodeficiency syndrome") show no credible mechanistic support and are flagged as likely model noise. The one candidate with real evidentiary weight — **Congenital HIV Infection / perinatal transmission prevention** — is supported by **13 clinical trials** (including Phase 3 regimen studies and pregnancy-specific pharmacokinetic trials) and **1 publication**, reflecting a natural life-cycle extension of etravirine's existing HIV-1 use rather than a truly novel mechanism.

> ⚠️ Note: The evidence pack's top-ranked prediction by raw TxGNN score is "feline acquired immunodeficiency syndrome" (a veterinary/cross-species entity) and "simian immunodeficiency virus infection," both scored L5/Hold with explicit rationale stating there is no mechanistic support. This report focuses instead on the highest-quality, evidence-backed candidate (rank 5, L2) rather than the raw top-score entry, to avoid presenting a misleading headline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection, NNRTI-resistance setting *(structured field is a data gap; drawn from repurposing_rationale text)* |
| Predicted New Indication | Congenital HIV Infection (perinatal/vertical transmission prevention) |
| TxGNN Prediction Score | 99.79% (rank 3016 of model output) |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for etravirine in this evidence pack (data gap DG002). Based on the information available, etravirine is a diarylpyrimidine NNRTI approved for HIV-1 infection, and its core indication — treatment of HIV-1 in patients with documented NNRTI resistance — is well established. Congenital/perinatal HIV infection is not a distinct disease mechanism but part of the same HIV-1 disease spectrum, transmitted from mother to child; preventing it relies on suppressing maternal HIV-1 viral load with the same class of antiretroviral agents used in adult treatment.

This is reflected directly in the evidence: several Phase 3 trials in this pack (e.g., NCT00855335, NCT00042289) specifically study antiretroviral pharmacokinetics — including etravirine — in HIV-1-infected pregnant women, and one Phase 1 trial (NCT04630002) directly evaluates etravirine drug-drug interactions in combination therapy. This indicates the "new indication" is less a mechanistic leap and more an extension of etravirine's known use into the perinatal population, which is why it is the only candidate in this pack reaching evidence level L2.

By contrast, the model's top three ranked predictions — feline AIDS, simian immunodeficiency virus infection, and a rare neurodevelopmental disorder — lack any plausible biological link to etravirine's NNRTI mechanism, as explicitly stated in the pack's own rationale text (cross-species/cross-family enzyme mismatch, or no known pathway overlap at all). These are treated as likely model artifacts rather than genuine repurposing signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | PK of darunavir, ritonavir, etravirine, and rilpivirine specifically in HIV-1-infected pregnant women |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1578 | IMPAACT P1026s — PK of antiretrovirals (incl. etravirine-class agents) during pregnancy/postpartum |
| [NCT04630002](https://clinicaltrials.gov/study/NCT04630002) | Phase 1 | Completed | 54 | Drug-drug interaction study of darunavir/ritonavir and/or etravirine with GSK3640254 |
| [NCT01199731](https://clinicaltrials.gov/study/NCT01199731) | Phase 2b | Terminated | 30 | GSK2248761 dose-selection study using open-label etravirine 200mg BID as control arm |
| [NCT07412977](https://clinicaltrials.gov/study/NCT07412977) | N/A | Not yet recruiting | 5160 | VIROPREG — French cohort on viral infections (incl. HIV) and antiviral treatment impact on pregnancy/mother-to-child transmission |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS — switching virologically suppressed HIV-1 adults to long-acting cabotegravir + rilpivirine |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Switching to dolutegravir + rilpivirine from INI-/NNRTI-/PI-based regimen in suppressed HIV-1 adults |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | Same design as above, second cohort |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3b | Active, not recruiting | 1049 | ATLAS-2M — long-acting cabotegravir + rilpivirine dosed Q8W vs Q4W |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | FLAIR — long-acting IM cabotegravir/rilpivirine maintenance after switch from INI regimen |

*Excluded from this table: NCT04273165 (Friedreich Ataxia trial — confirmed database mismatch, unrelated to HIV) and NCT01458132 (GSK drug-exposure registry, etravirine involvement unconfirmed).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Cohort/Case series | Antiviral Therapy | Two case reports on use of darunavir and etravirine (± raltegravir) in pregnancy for highly treatment-experienced HIV patients |

---

## Other TxGNN Predictions (Screened Out)

For transparency, the remaining 9 predicted indications in this evidence pack are summarized below. All were assessed as insufficiently supported for further action:

| Rank | Disease | Evidence Level | Decision | Reason |
|------|---------|----------------|----------|--------|
| 1 | Feline acquired immunodeficiency syndrome | L5 | Hold | Cross-species mismatch; FIV reverse transcriptase not a designed target |
| 2 | Simian immunodeficiency virus infection | L4 | Hold | Only indirect in vitro nanoparticle-delivery literature; no direct SIV-RT inhibition data |
| 3 | Rare neurodevelopmental disorder (ataxic gait/absent speech) | L5 | Hold | No mechanistic link; likely model noise |
| 4 | AIDS related complex | L3 | Research Question | Within core HIV-1 disease spectrum; evidence indirect (PROTEKT trial relevance unconfirmed) |
| 6 | Fibroma of prostate | L5 | Hold | No mechanistic link |
| 7 | Brenner tumor | L5 | Hold | No mechanistic link |
| 8 | Benign reproductive system neoplasm | L5 | Hold | Non-specific disease category, no biological hypothesis |
| 9 | Benign prostate phyllodes tumor | L5 | Hold | No mechanistic link |
| 10 | Obsolete familial combined hyperlipidemia | L5 | Hold | Reflects a known NNRTI side effect (dyslipidemia), not a treatment use; disease class is obsolete |

---

## Germany Market Information

Etravirine currently has **no marketing authorization records** in the German dataset (`taiwan_regulatory.total_licenses = 0`). No product, dosage form, or approved indication text is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (flagged as Blocking data gap DG001 — TFDA label warnings/contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The most credible predicted indication — congenital/perinatal HIV infection — is mechanistically coherent (same virus, same drug class, extension into pregnancy) and supported by Phase 3 and pregnancy-specific PK trials, reaching evidence level L2. However, the drug currently has zero marketing authorizations in Germany, and a **Blocking** data gap (missing TFDA label warnings/contraindications) prevents completion of the S1 safety screen. The remaining 9 predicted indications lack credible mechanistic or clinical support and should not be pursued.

**To proceed, the following is needed:**
- TFDA product label (warnings, contraindications) — currently a Blocking gap (DG001)
- Original mechanism of action documentation from DrugBank — currently a High-severity gap (DG002)
- Confirmation of etravirine's original approved indication(s), which are currently unpopulated in this record
- If pursuing the perinatal-transmission indication: a dedicated efficacy/safety study of etravirine specifically for prevention of vertical HIV transmission, since existing trials (PK studies, regimen-switch trials) do not directly test this endpoint
- Clarification of German/EU market access pathway, given the drug is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

