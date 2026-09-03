---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm to Pre-Malignant Myeloid Neoplasm

## One-Sentence Summary

Tagraxofusp is a CD123-targeted diphtheria-toxin fusion protein; per its own trial documentation it is used to treat CD123-expressing hematologic malignancies (established blastic plasmacytoid dendritic cell neoplasm and AML).
Of TxGNN's top-10 predictions, 9 (including the #1-ranked "esotropia") were flagged by the evidence pipeline itself as **mechanistic noise with zero supporting evidence**. The only prediction with real supporting data is **Pre-Malignant Myeloid Neoplasm** (rank #2), backed by **5 clinical trials** (all trials of tagraxofusp or closely related CD123-targeted agents) but **no dedicated literature**, and the trial populations largely target *established* AML/BPDCN rather than a strict pre-malignant population — so the link remains inferential.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Blastic plasmacytoid dendritic cell neoplasm (BPDCN) — stated in trial documentation (NCT05476770); not yet confirmed via DrugBank/regulatory data, see Data Gap DG002 |
| Predicted New Indication | Pre-Malignant Myeloid Neoplasm (e.g., MDS/CMML precursor states) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> Note: The nominal #1-ranked prediction, "esotropia" (99.73% score), was excluded from this report — the evidence pipeline's own annotation states it has no mechanistic connection to CD123-targeted toxin therapy and no supporting trials/literature (classified as TxGNN similarity noise). The same applies to 8 of the remaining 9 top predictions (inner ear neoplasm, benign tongue neoplasm, non-seminomatous lesion, chondroid hamartoma, childhood bronchial carcinoid, ductal/ductular proliferation, cystic neoplasm, thyroglossal duct cyst) — all L5/S0/Hold with no biological rationale.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002 — High severity). Based on trial documentation, tagraxofusp is a CD123-targeted diphtheria toxin fusion protein ("protein-drug conjugate consisting of a diphtheria toxin redirected to target CD123"), and it is already used clinically against CD123-expressing hematologic malignancies (BPDCN, AML, high-risk MDS).

The proposed link to "pre-malignant myeloid neoplasm" rests on the biological premise that CD123 (IL-3Rα) is over-expressed not only on established leukemic blasts but also on abnormal stem/progenitor clones in pre-malignant myeloid conditions (e.g., MDS, CMML), meaning tagraxofusp could theoretically eliminate these clones before progression to overt malignancy.

However, this connection is explicitly flagged as **inferential** in the source data: none of the 5 supporting trials enroll a strictly-defined pre-malignant population. Most target established AML, BPDCN, or high-risk MDS (NCT03113643), or measurable residual disease in AML (NCT07148180) — a state closer to sub-clinical relapse than to a true pre-malignant lesion. Only NCT06414681 (tagraxofusp + pacritinib in myelofibrosis) touches an MDS/MPN-overlap population, and it has not yet begun recruiting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06414681](https://clinicaltrials.gov/study/NCT06414681) | Early Phase 1 | Not yet recruiting | 20 | Tagraxofusp + pacritinib in intermediate-1+ myelofibrosis after/instead of JAK inhibitor therapy; Grade B relevance (MDS/MPN-overlap population, but not yet recruiting) |
| [NCT05476770](https://clinicaltrials.gov/study/NCT05476770) | Phase 1 | Recruiting | 54 | Tagraxofusp ± chemotherapy in pediatric relapsed/refractory CD123+ hematologic malignancies; confirms tagraxofusp's approved use in BPDCN; Grade B relevance (established malignancy, not pre-malignant) |
| [NCT07148180](https://clinicaltrials.gov/study/NCT07148180) | Phase 1/2 | Recruiting | 31 | Tagraxofusp + azacitidine + venetoclax targeting measurable residual disease (MRD) in AML; Grade B relevance (MRD-positive state partially overlaps with "pre-malignant" concept) |
| [NCT03113643](https://clinicaltrials.gov/study/NCT03113643) | Phase 1 | Recruiting | 72 | SL-401 (= tagraxofusp) + azacitidine/venetoclax in relapsed/refractory AML, treatment-naive AML, BPDCN, and high-risk MDS; Grade B relevance (drug's own trial, but population is established malignancy) |
| [NCT03386513](https://clinicaltrials.gov/study/NCT03386513) | Phase 1/2 | Active, not recruiting | 179 | IMGN632 (pivekimab sunirine, a *different* CD123-targeted agent) in CD123+ AML and hematologic malignancies; Grade C relevance (mechanism analogy only, not the same drug) |

---

## Literature Evidence

Currently no related literature available for this indication (the 20 literature records retrieved for a different predicted indication — "ductal or ductular proliferation" — concern hepatic ductular reaction/fibrosis pathways unrelated to CD123 biology and were excluded as apparent text-matching noise).

---

## Germany Market Information

Tagraxofusp is currently **not marketed** in Germany (0 authorizations on record), so no product/authorization table is available.

---

## Cytotoxicity

Tagraxofusp is a CD123-targeted immunotoxin (protein-drug conjugate incorporating a diphtheria toxin payload) used against CD123-expressing hematologic malignancies, meeting the antineoplastic criteria for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CD123-directed protein-toxin conjugate; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — see Data Gap DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only prediction with any supporting evidence (pre-malignant myeloid neoplasm) is backed solely by trials in *established* AML/BPDCN/high-risk MDS rather than a genuine pre-malignant population, and the mechanistic link is explicitly labeled inferential in the source data. Combined with a Blocking-severity data gap on TFDA/German label warnings and contraindications (DG001), the evidence does not clear the bar for S1 safety pre-screening, let alone a Go decision. All other top-10 TxGNN predictions for this drug were independently confirmed as biological noise with no clinical trial or literature support.

**To proceed, the following is needed:**
- Package insert (warnings, contraindications, DDI) to clear the S1 safety pre-screen (DG001)
- Confirmed mechanism of action data via DrugBank API (DG002)
- A trial or cohort study specifically enrolling a pre-malignant (e.g., low/intermediate-risk MDS, CMML) population rather than established AML/BPDCN, to directly test the CD123-clearance hypothesis
- Results from NCT06414681 (myelofibrosis combination trial) once recruitment begins, as the closest available population match
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

