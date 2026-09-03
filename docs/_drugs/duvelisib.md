---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

# Duvelisib: A PI3K-δ,γ Dual Inhibitor — TxGNN-Predicted Link to Hodgkin Lymphoma

## One-Sentence Summary

Duvelisib is an oral PI3K-δ,γ dual inhibitor; this evidence pack does not record an original approved indication for it in this market (drug is currently unmarketed here). TxGNN's top-ranked prediction is **Hodgkin's lymphoma**, but the **11 clinical trials** and **16 publications** retrieved as supporting evidence all concern non-Hodgkin lymphoma subtypes (CLL/SLL, follicular, mantle cell, peripheral T-cell lymphoma) — none study classical Hodgkin lymphoma directly, so the evidence level for this specific label is only **L4** with a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset — duvelisib is not currently marketed in this jurisdiction and no approved-indication text is available |
| Predicted New Indication | Hodgkin's lymphoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Duvelisib's official mechanism-of-action field is a data gap in this evidence pack. However, the literature retrieved as supporting evidence consistently and independently describes duvelisib as an **oral dual inhibitor of phosphoinositide 3-kinase δ and γ (PI3K-δ,γ)**, acting downstream of the B-cell receptor signaling pathway to suppress proliferation and survival of malignant B cells, while PI3K-γ inhibition additionally modulates the tumor microenvironment (macrophages/T-cells).

The automated relevance review embedded in this pack flags a significant mismatch for this rank-1 prediction: **none of the 11 clinical trials or 16 publications** retrieved under the "Hodgkin lymphoma" label actually enrolled or studied classical Hodgkin lymphoma (Reed-Sternberg cell biology). Every trial and paper instead concerns non-Hodgkin lymphoma subtypes — CLL/SLL, follicular lymphoma, mantle cell lymphoma, peripheral/cutaneous T-cell lymphoma — where duvelisib's mechanism is well established. This strongly suggests the TxGNN "Hodgkin lymphoma" score reflects an embedding-similarity artifact between lymphoma disease labels in the knowledge graph, rather than a genuine mechanistic signal specific to classical HL.

**Important context:** the same evidence pack contains a much stronger, differently-labeled signal — "B-cell neoplasm" (rank 9) — anchored by a completed pivotal Phase 3 trial (DUO, NCT02004522, n=319, duvelisib vs. ofatumumab in relapsed/refractory CLL/SLL) and rated L1/S3/"Proceed with Guardrails." The pack's own annotation for that entry, however, cautions that this largely reflects duvelisib's **already-established** therapeutic scope (CLL/SLL/FL) rather than a novel repurposing signal, and recommends resolving the drug-level data gaps (original indication, MOA) before that program is scored as "repurposing" versus "primary indication confirmation."

---

## Clinical Trial Evidence

*None of the following trials studied classical Hodgkin lymphoma specifically; all involve non-Hodgkin lymphoid malignancies retrieved under the "Hodgkin lymphoma" label.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Withdrawn | 0 | Duvelisib+bendamustine/rituximab vs. placebo in previously-treated indolent NHL — withdrawn, no data |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Duvelisib-CHOEP vs. standard regimens in untreated CD30-negative peripheral T-cell lymphoma |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | PI3K-class agent (YY-20394) monotherapy in relapsed/refractory follicular NHL |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Duvelisib monotherapy in rituximab/chemo-refractory indolent NHL (FL, marginal zone, SLL) |
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Intermittent vs. continuous duvelisib dosing schedules in indolent NHL |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | Duvelisib + rituximab or bendamustine/rituximab in NHL/CLL |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, not recruiting | 42 | Duvelisib after CAR T-cell therapy to enhance CAR T persistence via PI3K inhibition |
| [NCT02640833](https://clinicaltrials.gov/study/NCT02640833) | Phase 1 | Withdrawn | 0 | Duvelisib + venetoclax in R/R CLL/SLL/NHL — withdrawn |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Duvelisib + acalabrutinib in R/R indolent NHL — withdrawn |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Duvelisib + BMS-986345 combination in lymphoid malignancy, dose-finding |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic Review/Meta-analysis | Frontiers in Immunology | Safety/efficacy meta-analysis of duvelisib across R/R lymphoid neoplasm types |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Review | The Lancet Oncology | Overview of duvelisib in indolent non-Hodgkin lymphoma |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 Trial | Blood | Foundational Phase 1 study establishing MTD (75 mg BID) and activity of duvelisib in advanced hematologic malignancies |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Cohort/Phase 1 | American Journal of Hematology | Duvelisib + rituximab or bendamustine/rituximab in NHL/CLL |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Current Treatment Options in Oncology | PI3K inhibitors, including duvelisib, as targeted therapy in lymphoma |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Novel therapeutic approaches, including duvelisib, in follicular lymphoma |
| [27872741](https://pubmed.ncbi.nlm.nih.gov/27872741/) | 2016 | Review | Mediterranean Journal of Hematology and Infectious Diseases | Novel drugs, including duvelisib, in follicular lymphoma |
| [32658557](https://pubmed.ncbi.nlm.nih.gov/32658557/) | 2020 | Review | Future Oncology | PI3K inhibitor class review in non-Hodgkin lymphoma treatment landscape |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | American Journal of Health-System Pharmacy | Summary of regulatory-approved targeted therapies for B- and T-cell lymphomas |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical | Scientific Reports | PI3Kγ/δ roles in mantle cell lymphoma proliferation/migration and duvelisib efficacy |

---

## Germany Market Information

Duvelisib is currently **not marketed in Germany** — no BfArM authorization records exist in this evidence pack (0 licenses on file).

---

## Cytotoxicity

Duvelisib is an antineoplastic agent (oral small-molecule kinase inhibitor developed for hematologic malignancies).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3K-δ,γ dual inhibitor) — based on consistent description across retrieved literature; formal DrugBank category data not available in this evidence pack |
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
The rank-1 TxGNN prediction (Hodgkin lymphoma) is not supported by relevant evidence — every retrieved clinical trial and publication concerns non-Hodgkin lymphoma, indicating a likely disease-label embedding artifact rather than a genuine repurposing signal for classical HL. In parallel, this candidate's drug-level data gaps (missing BfArM label warnings/contraindications — Blocking; missing MOA — High) prevent it from clearing the S1 safety pre-assessment stage regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001: obtain BfArM/product label warnings and contraindications
- Resolve DG002: obtain confirmed MOA from DrugBank
- Establish and document duvelisib's original/approved indication(s), currently unrecorded in this dataset
- Disease-label-specific evidence re-review to confirm or rule out classical Hodgkin lymphoma relevance before advancing this specific candidate
- If redirecting toward the stronger "B-cell neoplasm" signal (rank 9, L1/S3), first clarify whether that reflects genuine repurposing potential or overlap with duvelisib's already-established indication scope, and re-screen adjacent low-evidence CLL/SLL subtype entries (ranks 5–6) for the same embedding-artifact pattern seen at rank 1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

