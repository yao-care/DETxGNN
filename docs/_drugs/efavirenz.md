---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed for HIV-1 infection (based on general pharmacological knowledge; no verified BfArM label is present in this Evidence Pack).
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
but this signal is supported by only **1 clinical trial (unrelated drug, withdrawn)** and **14 publications, all preclinical macaque-model studies** — evidence is weak and largely does not describe a human clinical indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack — no BfArM authorization on file (0 licenses); efavirenz is generally known as an HIV-1 NNRTI, but this is not confirmed by regulatory data here |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as Data Gap DG002, High severity). Based on general pharmacological knowledge, efavirenz is an NNRTI that blocks HIV-1 reverse transcriptase; its efficacy in HIV-1 infection is well established in the literature, though this could not be verified against structured DrugBank data in this pack.

The predicted "new indication" — SIV infection — is not a naturally occurring human disease. It refers to a laboratory model: researchers have engineered a chimeric virus (RT-SHIV) by replacing the SIV reverse transcriptase gene with the HIV-1 reverse transcriptase gene, making it susceptible to NNRTIs like efavirenz in rhesus macaques. This allows efavirenz to suppress viral load in RT-SHIV-infected macaques (e.g., PMID 15919889, 19889213), which is almost certainly the source of the TxGNN association. Natural, non-engineered SIV is intrinsically resistant to efavirenz because wild-type SIV reverse transcriptase differs structurally from HIV-1 RT.

This means the mechanistic link is real but narrow: it applies only to an engineered laboratory tool used to study HIV pharmacokinetics and drug resistance in nonhuman primates, not to a genuine new human (or animal) therapeutic indication. Rank 2 (feline AIDS) has a similar limitation — FIV reverse transcriptase differs substantially from HIV-1 RT, and human NNRTIs including efavirenz show weak activity against wild-type FIV. Rank 3 (a rare pediatric neurodevelopmental disorder) has no mechanistic rationale and no supporting evidence at all, while efavirenz carries known CNS-related risks (dizziness, abnormal dreams, suicidal ideation) that would raise concern in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Studied HIV viral decay kinetics with **raltegravir** (an integrase inhibitor), not efavirenz; comparison referenced SIV-infected macaque decay kinetics as background only. Trial was withdrawn (enrollment 0) and is graded **C (low relevance)** — drug and study population do not match this candidate. |

*No trials directly evaluating efavirenz in SIV infection were identified.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Cohort (preclinical) | Antimicrob Agents Chemother | First demonstration that efavirenz suppresses RT-SHIV (chimeric SIV carrying HIV-1 RT) replication in rhesus macaques |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Cohort (preclinical) | J Virol | Efavirenz + lamivudine + tenofovir combination suppressed RT-SHIV viral load in macaques, modeling human HAART |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Cohort (preclinical) | Retrovirology | Short-course efavirenz monotherapy followed by combination ART in RT-SHIV-infected macaques; tracked viral subpopulation dynamics |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Review/Cohort | J Virol | Efavirenz monotherapy in pigtail macaques prior to combination ART; genetic diversity of RT-SHIV persisted despite treatment |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Cohort (preclinical) | Antimicrob Agents Chemother | Enhanced 4–5 drug ART regimens (context includes efavirenz-based models) improved RT-SHIV decay kinetics in macaques |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Preclinical | PLoS One | Characterized viral decay kinetics in HAART-treated RT-SHIV macaque model of AIDS |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | Preclinical | Retrovirology | Plasma/tissue viral population analysis in RT-SHIV macaques on ART suggests no residual tissue replication |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Preclinical | J Virol | Identified viral sanctuaries persisting during HAART in the RT-SHIV nonhuman primate AIDS model |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | In vitro | J Virol | Ultrasensitive PCR detected rare pre-existing drug-resistant RT-SHIV variants in macaques prior to ART |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | In vitro/Imaging | Antimicrob Agents Chemother | Mass spectrometry imaging mapped antiretroviral drug distribution and residual RT-SHIV RNA in macaque spleen tissue |

**Note:** All identified literature describes the engineered RT-SHIV macaque research model used to study human HIV-1 pharmacology and resistance — none describes treatment of naturally occurring SIV infection as a disease target.

---

## Germany Market Information

Efavirenz currently holds **no marketing authorization on record** in this Evidence Pack (0 licenses; market status: not marketed). BfArM label content (warnings, contraindications, approved indications) could not be retrieved and is tracked as **Data Gap DG001 (Blocking)**.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warning, contraindication, and drug-interaction data (TFDA/BfArM label) are not yet available for efavirenz in this Evidence Pack — retrieval of the official label PDF is tracked as Data Gap DG001 (Blocking), which currently prevents a full S1 safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (SIV infection) reflects an engineered laboratory research model (RT-SHIV in macaques) rather than a genuine treatable disease target; the only associated clinical trial is unrelated and withdrawn; and both regulatory safety data (DG001, Blocking) and mechanism-of-action data (DG002, High) are missing, preventing progression past S0.

**To proceed, the following is needed:**
- Retrieve and parse the official TFDA/BfArM label PDF for warnings and contraindications (DG001)
- Query DrugBank (or equivalent) to confirm and document efavirenz's mechanism of action (DG002)
- Clarify with the TxGNN/evidence pipeline whether "simian immunodeficiency virus infection" should be excluded as a non-human, model-only node, since it does not represent an actionable repurposing target
- Re-screen ranks 2 (feline AIDS — veterinary, not human) and 3 (ultra-rare neurodevelopmental disorder — no evidence, potential CNS safety conflict) before considering any further evaluation of this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

