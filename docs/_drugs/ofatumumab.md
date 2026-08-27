---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody whose established use — per the literature captured in this evidence pack — is chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL). The TxGNN model's most clinically actionable new-indication prediction is **Follicular Lymphoma (FL)**, a related CD20-positive B-cell lymphoma, supported by **15 clinical trials** and **20 publications**, including at least one completed randomized Phase 2 trial. Several other TxGNN-ranked predictions (molecular CLL/SLL subtypes, "metastatic neoplasm," malignant spiradenoma, Langerhans cell histiocytosis) carry little to no supporting evidence and are not considered viable candidates at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia/Small Lymphocytic Lymphoma (CLL/SLL) — reconstructed from literature within this evidence pack (e.g., PMID 22830942, PMID 20068404); not separately confirmed in the structured `drug.original_indications` field, which is empty |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% (rank #4073) |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured record (`original_moa`: Data Gap). Based on the literature retrieved in this evidence pack, ofatumumab is a second-generation, fully human IgG1κ **anti-CD20 monoclonal antibody**. It binds a distinct, membrane-proximal small-loop epitope on the CD20 antigen (distinguishing it from rituximab) and clears CD20-positive B cells primarily through complement-dependent cytotoxicity (CDC), with additional antibody-dependent cellular cytotoxicity (ADCC) and induction of apoptosis (PMID 20068404, PMID 23850806, PMID 32482755).

CLL/SLL and follicular lymphoma are both mature B-cell neoplasms that near-universally express CD20 on the malignant clone. Anti-CD20 antibodies (rituximab, ofatumumab, obinutuzumab) are already standard-of-care building blocks across this entire disease family — CLL/SLL, FL, diffuse large B-cell lymphoma, and other indolent B-NHL subtypes are frequently studied together in the same trials and reviews (PMID 28983798, PMID 29934061, PMID 25736010). Several trials in this evidence pack directly enrolled combined "indolent B-cell lymphoma" populations spanning both CLL/SLL and FL (e.g., NCT01239394, NCT01294579), reinforcing that the mechanistic rationale for extending ofatumumab into FL is not speculative — it mirrors how the drug class is already used clinically.

It is worth noting that TxGNN's rank #5453 prediction ("chronic lymphocytic leukemia/small lymphocytic lymphoma," L1, 34 trials including two completed Phase 3 RCTs — RESONATE/NCT01578707 and DUO/NCT02004522) is effectively **re-predicting the drug's own established indication** rather than a genuinely new one. We treat this as a positive sanity check on the model rather than a repurposing candidate. Similarly, the two top-ranked predictions (pregerminal-center and IGHV-mutated CLL/SLL molecular subtypes) are narrow biomarker-defined sub-populations of the *same* disease with zero trial or literature evidence (L5) and are not actionable. Follicular lymphoma is therefore the strongest genuine repurposing signal in this pack: mechanistically coherent, biologically adjacent to the original indication, and — unlike the CLL/SLL entry — actually represents a distinct disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminated | 346 | Randomized ofatumumab + bendamustine vs. bendamustine alone in indolent B-cell NHL (incl. FL) refractory to rituximab; largest FL-relevant RCT in the pack but stopped before completion |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Completed | 135 | Randomized ofatumumab + bendamustine ± bortezomib in untreated follicular lymphoma |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | Single-arm, international trial of ofatumumab in rituximab-refractory FL |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | Stage I/II FL treated with radiotherapy with/without ofatumumab, stratified by molecular (Bcl-2) status |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Randomized two-dose ofatumumab + CHOP in previously untreated FL |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | CALGB trial of ofatumumab in previously untreated Stage II–IV follicular NHL |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab + bendamustine, then ofatumumab maintenance, in indolent B-NHL (incl. FL) relapsed after rituximab |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma (includes FL) |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Japanese safety/PK study of ofatumumab monotherapy in FL and CLL patients |

*Additional Phase 2 trials (e.g., NCT01263418, NCT00092274, NCT01119794, NCT01397591) were withdrawn or terminated with minimal/no enrollment and are omitted from this table as low-information.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904 (Alliance): randomized Phase 2 comparing ofatumumab+bendamustine vs. triplet with bortezomib in untreated high-risk FL |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Cohort (Phase 2) | The Lancet Haematology | FIL MIRO final results: MRD-driven radiotherapy ± ofatumumab in early-stage FL |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 (single-arm) | British Journal of Haematology | CALGB 50901 (Alliance): single-agent ofatumumab in untreated, low/intermediate-risk FL |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 1–2 | British Journal of Haematology | Ofatumumab + CHOP (O-CHOP) as frontline therapy for FL; two dose levels compared |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Cohort | Blood | Ofatumumab monotherapy in rituximab-refractory FL; overall response rate 13% |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | PK study | Journal of Clinical Pharmacology | Population PK of ofatumumab across CLL, FL, and rheumatoid arthritis populations |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Review of Hematology | Emerging therapeutic strategies in follicular lymphoma, including anti-CD20 agents |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Evidence review | Clinical Lymphoma, Myeloma & Leukemia | Evidence-based review of anti-CD20 antibody regimens across CLL, DLBCL, and FL |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 20-year clinical experience with anti-CD20 therapy (rituximab) in B-cell malignancies, contextualizing ofatumumab's role |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 | Blood | First clinical use of ofatumumab in relapsed/refractory FL |

---

## Germany Market Information

Per the current regulatory dataset, ofatumumab has **no active marketing authorization in Germany** (`total_licenses = 0`, `market_status = 未上市`/Not Marketed, `licenses = []`). No product records are available to tabulate. This status should be verified directly against BfArM/EMA registries, since global regulatory history for this molecule is not captured by this dataset.

---

## Cytotoxicity

Ofatumumab targets CD20-expressing B-cell malignancies and is used in the treatment of cancer (CLL/SLL, FL), meeting the antineoplastic criteria for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody; CDC/ADCC-mediated B-cell depletion, not a conventional DNA-damaging cytotoxic agent) |
| Myelosuppression Risk | Not available in this evidence pack — please refer to the package insert warnings and precautions (neutropenia has been reported with anti-CD20 antibody class agents in general) |
| Emetogenicity Classification | Low (monoclonal antibodies typically carry minimal emetogenic potential; infusion-related reactions, rather than nausea/vomiting, are the predominant acute administration concern) |
| Monitoring Items | Complete blood count with differential; hepatitis B serology prior to therapy (anti-CD20 class carries reactivation risk); immunoglobulin levels; infusion-related reaction monitoring during administration |
| Handling Protection | Not classified as a conventional cytotoxic hazardous drug; standard biologic/monoclonal antibody infusion handling precautions apply rather than cytotoxic drug handling protocols — confirm against institutional policy |

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack does not contain populated key warnings, contraindications, or drug interaction data for ofatumumab — this is flagged as a **Blocking-severity data gap (DG001)**, meaning a formal safety pre-assessment (S1) cannot be completed until TFDA/package-insert warnings and contraindications are obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Follicular lymphoma has a mechanistically coherent, moderately well-supported evidence base (L2: 15 trials including a completed randomized Phase 2 and one terminated Phase 3, plus 20 publications), making it the most credible genuine repurposing signal in this pack. However, a Blocking-severity safety data gap (missing warnings/contraindications) prevents completion of the initial safety screening stage, and the drug currently holds no marketing authorization in Germany — both must be resolved before progressing beyond a research question.

**To proceed, the following is needed:**
- TFDA/package-insert warnings and contraindications (resolves DG001, Blocking)
- Confirmed mechanism of action and original-indication regulatory history from DrugBank (resolves DG002)
- Drug-drug interaction data (currently `not_found`)
- Direct confirmation of current marketing authorization status with BfArM/EMA
- If advancing, prioritize completion or replication of a Phase 3 RCT specifically in FL, since current best evidence is Phase 2 (e.g., CALGB 50904) supplemented by one terminated Phase 3 trial (NCT01077518)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

