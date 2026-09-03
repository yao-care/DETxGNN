---
layout: default
title: Temoporfin
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Temoporfin
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

# Temoporfin: From Head and Neck Squamous Cell Carcinoma (PDT) to Tongue Neoplasm

## One-Sentence Summary

> Temoporfin (mTHPC) is a photosensitizer used in photodynamic therapy (PDT), with its strongest established evidence base in squamous cell tumors of the oral cavity, tongue base, and upper aerodigestive tract.
> Among the 10 candidate indications in this evidence pack, TxGNN's top-scoring prediction (**nasopharyngeal teratoma**) has **no supporting mechanism or literature**, while **Benign/Malignant Neoplasm of Tongue** — despite a slightly lower model score — is backed by **12 publications** including cohort studies, salvage-surgery case series, and pharmacokinetic localization studies. This report therefore focuses on the tongue indication as the most credible repurposing candidate in the pack.
> A **blocking data gap** (no local safety label/warnings available) currently prevents this candidate from advancing past a basic safety review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured regulatory data; per repeated evidence-pack rationale, temoporfin's validated use is **PDT for head & neck mucosal squamous cell tumors** |
| Predicted New Indication | Benign Neoplasm of Tongue (evidence base is predominantly tongue/tongue-base squamous cell carcinoma) |
| TxGNN Prediction Score | 99.76% (rank #3323 of candidate list) |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on TxGNN top rank:** The single highest-scoring prediction in this pack, *nasopharyngeal teratoma* (99.78%), is explicitly flagged in its own rationale as having "no mechanistic support" and is scored L5/Hold. It is not featured as the headline indication for that reason.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on information embedded in the evidence pack, temoporfin (mTHPC) is a photosensitizer: upon local light activation it generates singlet oxygen, causing selective tumor cell destruction. Its efficacy has been most extensively validated in squamous epithelial tumors of the head and neck mucosa — the oral cavity, tongue, tongue base, and upper aerodigestive tract.

The tongue is the anatomical site with the richest cluster of supporting literature in this dataset: pharmacokinetic localization studies of mTHPC in healthy versus malignant tongue/upper-aerodigestive tissue, interstitial PDT dosimetry/treatment-planning studies, and multiple cohort/case-series reports of PDT (including postoperative adjuvant use after robot-assisted salvage surgery) for tongue base carcinoma. This gives strong mechanistic and empirical continuity between temoporfin's established PDT use and this candidate indication.

One important caveat: nearly all cited literature concerns **malignant** squamous cell carcinoma of the tongue/tongue base, not strictly "benign neoplasm" as the TxGNN-labeled indication states. The evidence pack itself flags this naming mismatch and suggests the indication would be more accurately framed as "head and neck squamous epithelial neoplasm (including tongue)." This distinction should be preserved in any downstream clinical use case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9612194](https://pubmed.ncbi.nlm.nih.gov/9612194/) | 1996 | Clinical Cohort | J Clin Laser Med Surg | Early clinical evaluation of mTHPC-PDT in 27 patients with upper aerodigestive tract cancer |
| [9334805](https://pubmed.ncbi.nlm.nih.gov/9334805/) | 1997 | Cohort | Int J Cancer | mTHPC-PDT in 19 patients with oral cavity malignancy, including field cancerization |
| [9788423](https://pubmed.ncbi.nlm.nih.gov/9788423/) | 1998 | Clinical/Preclinical Correlation | Int J Radiat Oncol Biol Phys | Interstitial mTHPC-PDT dosing conditions that maximize tumor damage while sparing striated muscle |
| [11485842](https://pubmed.ncbi.nlm.nih.gov/11485842/) | 2001 | Pharmacokinetic Study | J Photochem Photobiol B | Fluorescence microscopy mapping of mTHPC (Foscan) distribution in healthy vs. malignant upper aerodigestive/tongue tissue |
| [20706842](https://pubmed.ncbi.nlm.nih.gov/20706842/) | 2011 | Cohort | Eur Arch Otorhinolaryngol | Outcome analysis of PDT in 170 patients (226 lesions) with early-stage oral cavity/oropharynx neoplasms |
| [21412802](https://pubmed.ncbi.nlm.nih.gov/21412802/) | 2011 | Cohort | Lasers Surg Med | PDT outcomes for oral dysplasia (premalignant lesions) |
| [22152039](https://pubmed.ncbi.nlm.nih.gov/22152039/) | 2011 | Case Series | Head Neck Oncol | mTHPC-PDT in end-stage/recurrent tongue base carcinoma; significant symptom reduction, favorable morbidity/mortality |
| [23775429](https://pubmed.ncbi.nlm.nih.gov/23775429/) | 2013 | Review/Technical | Lasers Surg Med | Airway management strategies for head & neck PDT; highlights post-PDT swelling risk at tongue base |
| [24037957](https://pubmed.ncbi.nlm.nih.gov/24037957/) | 2013 | Technical/Planning Study | Lasers Surg Med | MR/CT-based treatment planning method for mTHPC interstitial PDT in deep-seated head & neck cancer |
| [26179387](https://pubmed.ncbi.nlm.nih.gov/26179387/) | 2015 | Cohort | World J Surg Oncol | Postoperative temoporfin-PDT as adjuvant therapy after robot-assisted salvage surgery for recurrent tongue base SCC |

---

## Germany Market Information

No marketing authorizations are currently listed in the available regulatory dataset (`total_licenses: 0`, `market_status: 未上市/Not Marketed`). This may reflect withdrawal, non-renewal, or absence of a local filing rather than a fundamental efficacy/safety failure — original centralized EU approval history should be verified separately before drawing conclusions.

---

## Cytotoxicity

Temoporfin is classified here as antineoplastic based on its established use in treating malignant squamous cell tumors via photodynamic therapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted phototherapy agent (photosensitizer / PDT) — not a conventional systemic cytotoxic chemotherapeutic |
| Myelosuppression Risk | Not established in this dataset. Mechanistically (local, light-activated cytotoxicity rather than systemic exposure), myelosuppression risk is expected to be low, but this is inferred, not confirmed by toxicity data |
| Emetogenicity Classification | Not established; localized PDT agents are not typically classified under standard systemic emetogenicity scales |
| Monitoring Items | Skin/eye photosensitivity (prolonged light avoidance post-dose), airway patency and local tissue swelling post-treatment (per PMID 23775429), local wound/tissue healing |
| Handling Protection | Photosensitizing agent — requires light-controlled handling and patient light-avoidance protocols; standard cytotoxic drug handling regulations may not directly apply, but should be confirmed against the (currently unavailable) product label |

Please refer to the package insert warnings and precautions once available, as detailed toxicity data could not be retrieved for this evaluation (see Blocking data gap DG001 below).

---

## Safety Considerations

Please refer to the package insert for safety information. All key warnings, contraindications, and drug interaction fields in this evidence pack are currently unavailable (`[Data Gap]` / `not_found`).

**⚠ Blocking gap:** Local product label / TFDA-equivalent warnings and contraindications (DG001) have not yet been retrieved. Per the evidence pack, this blocks entry into the S1 safety pre-assessment stage and must be resolved before any clinical or regulatory next step.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tongue/tongue-base squamous neoplasm has the strongest and most consistent evidence base (L3, 10+ cohort/case-series/PK studies) among all candidates in this pack, and is mechanistically well-aligned with temoporfin's established PDT use. However, the drug has zero current marketing authorizations in the Germany dataset and a blocking safety-data gap, so progression must be conditional on resolving those gaps first.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label / warnings & contraindications (e.g., original EU/Foscan SmPC or TFDA-equivalent source) to complete S1 safety pre-assessment
- Resolve DG002 (High): confirm detailed MOA and DrugBank pharmacology data to strengthen the mechanistic rationale section
- Clarify the indication-naming mismatch: reframe "benign neoplasm of tongue" as "head & neck squamous epithelial neoplasm (tongue/tongue base)" to match the actual evidence base before advancing to protocol design
- Verify current German/EU marketing/authorization status (why `total_licenses = 0`) — determine if this reflects withdrawal, lapsed registration, or a data collection gap
- Given photosensitizer-class risk, prioritize confirmation of light-avoidance protocol and airway-monitoring requirements before any clinical guardrail design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

