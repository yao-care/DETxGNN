---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Plerixafor: From Hematopoietic Stem Cell Mobilization to Myeloid Leukemia (Chemosensitization)

## One-Sentence Summary

> Plerixafor is a CXCR4 antagonist historically used with G-CSF to mobilize hematopoietic stem cells for transplantation.
> Among the seven indications the TxGNN model surfaced for this drug, only **Myeloid Leukemia** is backed by real-world evidence —
> the other six top-ranked predictions (including a non-disease genetic locus and a likely false positive for bronchitis) have **zero supporting trials or literature**.
> For Myeloid Leukemia, the evidence pack contains **30 registered clinical trials** and **21 publications**, making it the credible repurposing candidate in this dataset despite a comparatively lower raw TxGNN rank (#9976 vs. #600 for the top-scored but evidence-free prediction).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hematopoietic stem cell (HSC) mobilization, in combination with G-CSF, prior to autologous transplantation (derived from clinical-trial context; not present in a formal registry record — data gap DG002) |
| Predicted New Indication | Myeloid Leukemia (acute myeloid leukemia, AML) — as a chemosensitizing adjunct to induction/consolidation chemotherapy |
| TxGNN Prediction Score | 99.02% (raw model rank #9976 of all candidates — notably lower than the top-scored but unsupported predictions) |
| Evidence Level | L2 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on candidate selection:** The top TxGNN-ranked predictions (indolent plasma cell myeloma, CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, bronchitis, vulvar melanoma) all carry **zero clinical trials and zero literature** in this evidence pack, and are flagged in the source rationale as speculative or, in the case of CMM7, not a valid disease entity. This report therefore focuses on Myeloid Leukemia, the one prediction with substantive corroborating evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Plerixafor in this evidence pack (data gap DG002). Based on information embedded in the clinical trial records themselves, Plerixafor is a CXCR4 antagonist that is FDA-approved for mobilizing hematopoietic stem cells from the bone marrow into peripheral blood, typically in combination with G-CSF, to support autologous or allogeneic transplantation.

The proposed new indication — myeloid leukemia — is mechanistically adjacent to this original use. Acute myeloid leukemia (AML) blasts rely on the same CXCR4–CXCL12 axis to adhere to bone marrow stromal niches, where they are protected from chemotherapy. By blocking CXCR4, Plerixafor can mobilize leukemic blasts out of this protective niche and into circulation, where they become more sensitive to cytotoxic therapy — essentially the same "mobilization" pharmacology repurposed from healthy stem cells to leukemic cells.

This mechanistic hypothesis is not merely theoretical: it has been tested in over two dozen Phase 1/2 trials combining Plerixafor with standard induction/consolidation regimens (FLAG-Ida, mitoxantrone-etoposide-cytarabine, decitabine, sorafenib for FLT3-mutated AML) in both relapsed/refractory and newly diagnosed AML patients, and is the subject of a dedicated systematic review and meta-analysis (PMID 32877869). The landmark proof-of-concept study (Uy et al., *Blood* 2012, PMID 22308295) first established that Plerixafor-induced blast mobilization correlates with improved chemotherapy response in relapsed/refractory AML.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Completed | 55 | Fludarabine + idarubicin + cytarabine + G-CSF + Plerixafor induction in relapsed/refractory AML patients ≤65 years |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF chemosensitization in relapsed/refractory AML |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | Completed | 33 | Sorafenib + G-CSF + Plerixafor combination dose-finding in FLT3-mutated AML |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | Completed | 47 | G-CSF + Plerixafor + busulfan/fludarabine conditioning for allogeneic transplant in AML/MDS/CML |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 (Plerixafor) + mitoxantrone/etoposide/cytarabine (MEC) in relapsed/refractory AML — landmark chemosensitization study |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Decitabine + Plerixafor priming as induction/postremission therapy in AML patients ≥60 years |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Plerixafor as chemosensitizing agent with cytarabine/etoposide in pediatric relapsed acute leukemia/MDS |
| [NCT01455025](https://clinicaltrials.gov/study/NCT01455025) | Phase 1 | Terminated | 11 | Dose-escalation of Plerixafor with induction/consolidation chemotherapy in relapsed AML |
| [NCT02605460](https://clinicaltrials.gov/study/NCT02605460) | Phase 2 | Unknown | 20 | CXCR4 antagonist chemosensitization before autologous/allogeneic HSCT in acute leukemia in remission |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | Unknown | 28 | Plerixafor + donor lymphocyte infusion for relapsed acute leukemia after allogeneic HSCT |

*20 additional trials (mobilization studies, transplant-conditioning regimens, and further AML chemosensitization protocols) are available in the underlying data but omitted here for brevity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1/2 | Annals of Hematology | PLERIFLAG regimen (FLAG-Ida + high-dose IV Plerixafor) in first early-relapsed/refractory AML |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 | Blood | Landmark chemosensitization study: CXCR4 antagonism with Plerixafor in 52 relapsed/refractory AML patients |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 | American Journal of Hematology | Sorafenib + G-CSF + Plerixafor in relapsed/refractory FLT3-ITD-mutated AML |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | Comprehensive review of CXCR4 as a therapeutic target in AML |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic Review/Meta-analysis | Leukemia Research | Plerixafor + chemotherapy and/or HSCT in acute leukemia — pooled preclinical/clinical evidence |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Review | Biology | CXCR4 antagonists as stem cell mobilizers and therapy sensitizers in AML and glioblastoma |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Cohort | Biology of Blood and Marrow Transplantation | Safety/tolerability of Plerixafor within myeloablative conditioning for AML allografting |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 | Haematologica | Decitabine + Plerixafor in newly diagnosed older AML patients, with leukemia stem cell effect analysis |
| [30150522](https://pubmed.ncbi.nlm.nih.gov/30150522/) | 2018 | Case Report | Cancers | Complete remission in refractory pediatric AML (monosomy 7) using Plerixafor + cytarabine + melphalan conditioning |
| [38024589](https://pubmed.ncbi.nlm.nih.gov/38024589/) | 2023 | Case Report/Cohort | EJHaem | Concomitant multiple myeloma and CML case, contextualizing CXCR4-related stem cell biology |

---

## Germany Market Information

Plerixafor is currently **not marketed** in the covered jurisdiction (0 authorizations on record), so no authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA/regulatory warnings, contraindications, and drug interaction data were not available in this evidence pack (data gap DG001, marked as **Blocking** severity — this gap currently prevents entry into the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Myeloid leukemia is the only prediction in this evidence pack supported by substantial clinical and mechanistic evidence — 30 registered trials (several completed Phase 1/2 studies) and a systematic review — establishing CXCR4 blockade as a validated chemosensitization strategy in AML. However, the drug is not currently marketed in the covered jurisdiction, and a **blocking** data gap on formal safety labeling (warnings/contraindications) prevents formal safety pre-assessment (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label / regulatory safety documentation (warnings, contraindications, DDI) before advancing past preliminary screening
- Resolve DG002 (High): obtain formal mechanism-of-action documentation (e.g., via DrugBank API) to strengthen the mechanistic linkage analysis
- Confirm original approved indication and formal regulatory history, since the current record shows no registered original indication
- Given multiple terminated/unknown-status trials in the dataset, assess feasibility and reasons for discontinuation before committing further evaluation resources
- Deprioritize the other six TxGNN-predicted indications (indolent plasma cell myeloma, CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, bronchitis, vulvar melanoma) pending any future emergence of clinical or literature evidence — none currently warrant investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

