---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 2
---

# Interferon Beta-1B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Interferon Beta-1b: From Multiple Sclerosis to Hairy Cell Leukemia

## One-Sentence Summary

> Interferon beta-1b (marketed elsewhere as Betaferon®/Betaseron®) is a recombinant type I interferon approved for the treatment of relapsing forms of multiple sclerosis.
> The TxGNN model predicts it may also be effective for **Hairy Cell Leukemia**,
> with **0 registered clinical trials** but **4 historical publications** (1987–1990) supporting early exploratory activity in this disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Sclerosis (inferred from literature/known use; not confirmed by German regulatory data — data gap) |
| Predicted New Indication | Hairy Cell Leukemia |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for interferon beta-1b is not available in this evidence pack. Based on known pharmacology, interferon beta-1b is a recombinant, cysteine-to-serine-substituted type I interferon with potent antiproliferative and immunomodulatory activity, approved for relapsing forms of multiple sclerosis (an autoimmune demyelinating disease of the CNS — see the second predicted indication in this dataset, which the model itself flags as the drug's original approved use rather than a new one).

Type I interferons as a class (including interferon alfa) have long served as an effective, guideline-supported therapy for hairy cell leukemia, a rare B-cell lymphoproliferative disorder that is highly sensitive to interferon-mediated antiproliferative and differentiation-inducing signaling. Because interferon beta-1b binds the same type I interferon receptor and activates overlapping downstream signaling pathways as interferon alfa, it is mechanistically plausible that it could exert similar antileukemic activity — a hypothesis that was in fact tested prospectively in the late 1980s.

However, development of interferon beta-1b in hairy cell leukemia was not pursued further: interferon alfa became the interferon of choice, and purine analogs (cladribine, pentostatin) subsequently displaced interferons altogether as first-line therapy. No modern clinical trials have evaluated interferon beta-1b in this indication since ~1990, so the mechanistic rationale, while sound, rests on dated and small-scale clinical experience rather than contemporary validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Cohort | Leukemia | UCLA experience: 51 patients across type I interferons; ~71% hematologic improvement in initial beta-serine-interferon cohort |
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Cohort | Cancer | 10 patients treated with rIFN-beta ser (90×10⁶ U SC TIW); 63% normalized peripheral counts, 25% partial hematologic improvement |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Cohort | American Journal of Hematology | 12 patients (10 previously treated) given IV beta-ser interferon 90×10⁶ U TIW; bone marrow involvement 90–100% hairy cells at baseline |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Case Report | American Journal of Clinical Oncology | Patient who failed beta-ser-interferon subsequently achieved complete response with 2'-deoxycoformycin (pentostatin) |

---

## Germany Market Information

No German market authorization records are available for interferon beta-1b in this dataset — the drug's market status is recorded as **Not Marketed** with **0 licenses**.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for hairy cell leukemia is limited to four small, older (1987–1990) cohort/case-report studies (evidence level L3) with no registered modern clinical trials, and the drug currently has no market authorization in Germany. The mechanistic rationale (shared type I interferon receptor pathway with interferon alfa, a historically effective HCL therapy) is plausible but has not been re-tested against current standard-of-care agents (cladribine, pentostatin).

**To proceed, the following is needed:**
- TFDA/BfArM label data — key warnings and contraindications (currently blocking, DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A modern comparative or translational study of interferon beta-1b against current HCL standard-of-care (purine analogs) to justify renewed clinical interest
- Clarification of original indication/regulatory status, since `original_indications` and German license records are both empty in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

