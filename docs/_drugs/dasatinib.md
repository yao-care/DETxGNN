---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib is a multi-target tyrosine kinase inhibitor (BCR-ABL, SRC family kinases, c-KIT, PDGFR); the evidence pack's own annotations indicate it is currently approved for chronic myeloid leukemia (CML) and Ph+ acute lymphoblastic leukemia, though this original-indication field is blank in the source data and should be independently verified. The TxGNN model's top new-indication prediction is **Ewing sarcoma**, supported by **3 clinical trials** and **9 publications**, with the strongest clinical trial (Phase 2, n=366) already completed but showing limited single-agent activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not provided in evidence pack (`drug.original_indications` is empty). Contextual notes in the pack's own rationale text describe dasatinib as a BCR-ABL kinase inhibitor used for CML/Ph+ ALL — **this needs independent verification against TFDA/DrugBank before use**, since it is inconsistent with the "not marketed" status below (see Data Quality Note) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% (score 0.9990, global rank 1,687) |
| Evidence Level | L2 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is not available in this evidence pack (`original_moa`: Data Gap). However, the supporting literature and the pack's own repurposing rationale describe dasatinib as a multi-kinase inhibitor that blocks Src-family kinases (SRC/LCK/YES/FYN) in addition to BCR-ABL, c-KIT, and PDGFR.

Ewing sarcoma tumor cells depend heavily on Src signaling — downstream of the disease-defining EWS-FLI1 fusion — for invasion, migration, and invadopodia formation. In vitro studies (PMID 17363602, PMID 18202781) demonstrate that dasatinib inhibits proliferation and migration in bone-sarcoma cell lines through this pathway, giving a plausible mechanistic bridge from dasatinib's known kinase-inhibitory activity to Ewing sarcoma biology.

Clinically, this mechanistic rationale has already been tested: a completed Phase 2 trial in advanced sarcomas (NCT00464620, n=366) included an Ewing sarcoma cohort, but single-agent dasatinib showed **limited activity and did not reach the expected response rate**. This tempers the otherwise strong mechanistic case and is the main reason the evidence level is capped at L2 rather than higher.

**Data Quality Note:** The rank-2 prediction (myeloid leukemia) in this same evidence pack flags an internal inconsistency — `original_indications` is empty and `market_status` is "not marketed," which does not match dasatinib's well-established approval history for CML. This suggests a possible field-mapping gap in the source database for this drug record. This should be resolved before the "Original Indication" field above is finalized.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Response rate and 6-month PFS of dasatinib in advanced sarcomas, including an Ewing sarcoma cohort; single-agent activity was limited and did not meet the expected response rate. |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib combined with ifosfamide/carboplatin/etoposide; terminated with only 7 patients enrolled, limited evidentiary value. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | Tests B7-H3 CAR-T cell therapy in relapsed/refractory solid tumors (including Ewing sarcoma population); not a dasatinib trial, only population-level overlap. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical/In vitro | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in neuroblastoma and Ewing sarcoma cell lines, consistent with c-KIT/PDGFR/Src involvement. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical/In vitro | Cancer Research | Dasatinib inhibits migration/invasion across diverse sarcoma cell lines and induces apoptosis in Src-dependent bone sarcoma cells. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical/Mechanistic | Sarcoma | Reviews FAK-Src complex targeting in DSRCT, Ewing sarcoma, and rhabdomyosarcoma; notes dasatinib failed as monotherapy in a Phase 2 study of these subtypes, motivating combination strategies. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical/Mechanistic | Neoplasia | Tenascin C and Src cooperate to drive invadopodia formation and invasion in Ewing sarcoma cells under microenvironmental stress. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical/Mechanistic | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and migration in Ewing sarcoma. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | General review of Src signaling's role in sarcoma biology and its feasibility as a drug target. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Review (indirect — chondrosarcoma) | Current Treatment Options in Oncology | Systemic therapy review for chondrosarcoma, not Ewing sarcoma specifically; included for background only, low direct relevance. |

*Note: 2 additional literature hits returned by the search (PMID 29776413 — plerixafor, not dasatinib; PMID 32999666 — unrelated CML case report) were excluded from this table as not substantively relevant to the dasatinib–Ewing sarcoma question.*

---

## Germany Market Information

Dasatinib is currently **not marketed in Germany** under this evidence pack (0 authorizations on record; `market_status`: "未上市"). No license records are available to summarize.

---

## Cytotoxicity

Dasatinib is an oncology/antineoplastic agent (tyrosine kinase inhibitor class, referenced in this pack's own rationale as a treatment for CML/Ph+ ALL), so this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL / Src-family kinase inhibitor, tyrosine kinase inhibitor class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI data are all unavailable in this evidence pack — DG001, labeled "Blocking" severity, explicitly prevents proceeding to the S1 safety assessment stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (Src-dependent invasion in Ewing sarcoma) is credible and supported by in vitro data, but the only relevant clinical trial (Phase 2, n=366) already showed limited single-agent efficacy, and no dedicated Ewing sarcoma trial data exists. Combined with a **Blocking** data gap on TFDA labeling/safety information (DG001), the candidate cannot proceed past S1.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the S1 safety gate (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Resolution of the `original_indications`/`market_status` data inconsistency flagged above, so the true original indication and current authorization status can be confirmed
- If pursued further, evaluation should focus on combination regimens (e.g., with chemotherapy or FAK inhibitors) rather than dasatinib monotherapy, given the negative single-agent signal in NCT00464620
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

