---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: From Multiple Myeloma / MDS(del5q) to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide (Revlimid®) is an immunomodulatory imide drug (IMiD) already established for multiple myeloma and transfusion-dependent anemia due to low-risk myelodysplastic syndrome (MDS) with del(5q). The TxGNN model predicts it may also be effective for **Myeloid Leukemia**, with **over 40 clinical trials** (including 2 completed Phase 3 RCTs) and **20 publications** currently supporting this direction — though a **blocking safety data gap** (no TFDA/BfArM label data available) means this cannot yet proceed past preliminary safety review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma (in combination with dexamethasone) and transfusion-dependent anemia due to low-risk MDS with del(5q) cytogenetic abnormality *(derived from literature evidence, PMID 23316859; no BfArM label data available)* |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs: NCT00179621, NCT01029262) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for lenalidomide is not available in this evidence pack. However, supporting literature (PMID 39881283) indicates lenalidomide acts by binding cereblon (CRBN), recruiting the transcription factors IKZF1/IKZF3, and promoting their ubiquitination and degradation — the pathway underlying both its antimyeloma and antileukemic activity. This is consistent with lenalidomide's classification as an immunomodulatory imide drug (IMiD) rather than a conventional cytotoxic chemotherapy.

Myeloid leukemia (AML) and MDS with del(5q) — lenalidomide's proven original indications — sit on the same disease continuum: low-risk MDS frequently progresses to AML, and both conditions share overlapping clonal myeloid pathobiology and cytogenetic abnormalities (notably chromosome 5 deletions). This biological continuity is the most plausible basis for the TxGNN prediction, and is directly reflected in the trial evidence below, where lenalidomide (often combined with azacitidine) has been repeatedly tested across the MDS–AML spectrum, including in relapsed/refractory AML, post-transplant maintenance, and elderly newly-diagnosed AML.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00179621](https://clinicaltrials.gov/study/NCT00179621) | Phase 3 | Completed | 205 | Double-blind, placebo-controlled RCT of lenalidomide (10 mg vs 5 mg) vs placebo in RBC transfusion-dependent low/int-1 risk MDS with del(5q) |
| [NCT01029262](https://clinicaltrials.gov/study/NCT01029262) | Phase 3 | Completed | 239 | Double-blind, placebo-controlled RCT of lenalidomide vs placebo in transfusion-dependent anemia, low/int-1 risk MDS without del(5q), ESA-refractory |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Randomized, open-label comparison of high-dose lenalidomide vs sequential azacitidine+lenalidomide vs azacitidine alone in newly diagnosed AML, age ≥65 |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Phase 3 | Unknown | 60 | Azacitidine + lenalidomide as MRD-monitored maintenance therapy in elderly/unfit AML |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | Completed | 37 | Sequential azacitidine + lenalidomide for relapsed/refractory AML and high-risk MDS; CR/CRi rate as primary endpoint |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML patients in remission |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | Completed | 48 | Lenalidomide safety/efficacy in untreated AML patients ≥60 years without chromosome 5q abnormalities |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | Lenalidomide + MEC (mitoxantrone/etoposide/cytarabine) chemotherapy for relapsed/refractory AML |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | Completed | 27 | Lenalidomide in relapsed/refractory AML or high-risk MDS with chromosome 5 abnormalities |
| [NCT00957385](https://clinicaltrials.gov/study/NCT00957385) | Phase 2 | Completed | 24 | Randomized lenalidomide maintenance in AML patients in CR1 (≥60y) or CR2 (<60y) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35277655](https://pubmed.ncbi.nlm.nih.gov/35277655/) | 2022 | Randomized Phase 2 RCT | Leukemia | Azacitidine ± lenalidomide in higher-risk MDS and AML with del(5q) karyotype |
| [30653424](https://pubmed.ncbi.nlm.nih.gov/30653424/) | 2019 | Prospective clinical trial | J Clin Oncol | Lenalidomide + azacitidine salvage therapy for AML/MDS relapse after allogeneic transplant |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic review / meta-analysis | Hematology (Amsterdam) | Efficacy and adverse events of azacitidine + lenalidomide across AML, MDS, and CMML |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospective trial (Azalena) | Haematologica | Azacitidine + lenalidomide + donor lymphocyte infusion for post-transplant relapse of MDS/AML/CMML |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib trial | J Geriatric Oncology | Lenalidomide as post-remission therapy in older AML adults; safety and geriatric function assessed |
| [40250191](https://pubmed.ncbi.nlm.nih.gov/40250191/) | 2025 | Phase 1 trial | Leukemia Research | Lenalidomide + bortezomib for AML/MDS relapsing after allogeneic stem cell transplant |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase 1 dose-escalation trial | Bone Marrow Transplantation | Lenalidomide maintenance safety/tolerability in post-transplant AML and high-risk MDS |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Overview of lenalidomide as a novel treatment for AML; confirms approved MDS del(5q) and multiple myeloma indications |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Comprehensive review of MDS pathophysiology and progression to AML |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Mechanistic study | Cell Mol Biol Lett | KDM5C stabilizes cereblon (CRBN), enhancing AML cell sensitivity to lenalidomide — mechanistic basis for antileukemic activity |

---

## Germany Market Information

Lenalidomide is currently **not marketed** in Germany (market status: 未上市). No BfArM authorization records are available in the evidence pack (`total_licenses: 0`).

---

## Cytotoxicity

Lenalidomide is included here because its established original indication (multiple myeloma) is a hematologic malignancy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — immunomodulatory imide drug (IMiD), non-conventional cytotoxic (per PMID 39881283, acts via CRBN-mediated protein degradation) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for the myeloid leukemia indication is strong (L1: 2 completed Phase 3 RCTs plus extensive Phase 1/2 trial history and a randomized Phase 2 RCT). However, TFDA/BfArM label data (warnings, contraindications) is marked as a **Blocking** data gap that explicitly prevents entry into the S1 safety pre-assessment, and the drug is currently not marketed in Germany. The recommendation cannot be upgraded to "Proceed with Guardrails" until baseline safety documentation exists.

**To proceed, the following is needed:**
- Official TFDA/BfArM package insert (warnings, contraindications, DDI) to unblock the S1 safety evaluation
- Confirmed mechanism-of-action data from DrugBank
- Clarification of route/dosage-form compatibility for the AML/MDS population
- Re-verification of literature/trial matching for lower-confidence predicted indications in this pack (e.g., rank 4 "aregenerative anemia," where cited literature appears mismatched to multiple myeloma/Waldenström studies rather than the stated indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

