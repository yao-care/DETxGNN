---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid; the original approved indication text and detailed mechanism-of-action data were not available in this evidence pack. The TxGNN model predicts it may be effective for **Alopecia Areata**, and while the 13 retrieved clinical trials are largely unrelated oncology combination-therapy studies, **20 publications** — including one RCT and several systematic reviews/cohort studies — directly support dexamethasone (oral/IV pulse therapy) as an existing off-label treatment for alopecia areata.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no license text or original_indications data available; MOA marked as data gap) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on known pharmacological class information, dexamethasone is a high-potency synthetic glucocorticoid with broad systemic anti-inflammatory and immunosuppressive activity — this is not part of the structured evidence but is well-established background knowledge that contextualizes the prediction below.

Alopecia areata is an autoimmune disease in which cytotoxic T-cells attack the hair follicle, collapsing its normal immune-privileged state and triggering non-scarring hair loss. Systemic corticosteroids — including dexamethasone oral or IV pulse regimens — are already an established standard/second-line clinical treatment for moderate-to-severe alopecia areata, particularly in patients who are ineligible for or lack access to JAK inhibitors. This means the mechanistic link is not a purely theoretical model extrapolation: it is corroborated by real-world clinical practice and published pulse-therapy protocols identified in the literature evidence below.

By contrast, most of the clinical trials returned by the evidence search (e.g., dexamethasone used as a chemotherapy combination partner in multiple myeloma, NSCLC, or mesothelioma regimens) are not relevant to alopecia areata and reflect dexamethasone's routine use as an oncology-supportive medication rather than evidence for this specific repurposing hypothesis.

---

## Clinical Trial Evidence

None of the retrieved trials directly investigate dexamethasone for alopecia areata; they largely reflect dexamethasone's role as a combination/supportive agent in oncology regimens and were graded as low relevance (C) where reviewed. They are listed below for transparency.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00282087](https://clinicaltrials.gov/study/NCT00282087) | Phase 2 | Completed | 47 | Adjuvant gemcitabine/docetaxel + doxorubicin in uterine leiomyosarcoma; not AA-related |
| [NCT02004275](https://clinicaltrials.gov/study/NCT02004275) | Phase 1/2 | Unknown | 118 | Pomalidomide + dexamethasone ± ixazomib in relapsed multiple myeloma; dexamethasone as standard chemo co-agent, unrelated to AA |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Unknown | 74 | Prophylactic oral dexamethasone for regorafenib-induced fatigue/malaise in mCRC; unrelated to AA |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Dexamethasone suppression test in mild autonomous cortisol secretion and bone strength; diagnostic use, not AA treatment |
| [NCT01215916](https://clinicaltrials.gov/study/NCT01215916) | Phase 1 | Completed | 39 | LY573636 + pemetrexed in solid tumors; dexamethasone likely premedication only |
| [NCT01126736](https://clinicaltrials.gov/study/NCT01126736) | Phase 1/2 | Completed | 98 | Eribulin + pemetrexed in NSCLC; unrelated to AA |
| [NCT01607554](https://clinicaltrials.gov/study/NCT01607554) | Phase 1/2 | Terminated | 2 | Irinotecan in ISG15-high NSCLC; unrelated to AA |
| [NCT01055496](https://clinicaltrials.gov/study/NCT01055496) | Phase 1 | Completed | 103 | R-CVP/R-GDP + inotuzumab in CD22+ NHL; dexamethasone as part of standard chemo backbone |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | Completed | 24 | Cabazitaxel in temozolomide-refractory GBM; dexamethasone used for cerebral edema control, unrelated to AA |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | Completed | 56 | Durvalumab + lenalidomide ± dexamethasone in newly diagnosed multiple myeloma; unrelated to AA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomized trial: low-dose dexamethasone oral mini-pulse vs. DPCP contact sensitization in severe pediatric alopecia areata |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / NMA | Archives of Dermatological Research | Network meta-analysis comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | Compares efficacy, relapse rate, and side effects across three systemic corticosteroid modalities for AA |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Review of pulse-dose corticosteroid dosing/administration regimens for AA in children |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Multicentric Study/Review | Dermatologic Therapy | Multicentric study of mini-pulse oral dexamethasone for moderate-to-severe AA |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world cohort assessing effectiveness/safety of dexamethasone mini-pulse therapy in AA, plus response predictors |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Cohort | European Journal of Dermatology | Stepwise topical corticosteroid + dexamethasone rescue strategy enhances baricitinib outcomes in severe AA (n=19) |
| [17656876](https://pubmed.ncbi.nlm.nih.gov/17656876/) | 2002 | Review/Commentary | Indian J Dermatol Venereol Leprol | Discussion of dexamethasone pulse therapy utility for extensive AA |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Case Series | Dermatologic Therapy | Combined IV pulse + topical corticosteroid for severe pediatric AA; comparison of 1-day vs. 3-day dexamethasone pulse regimens (n=73) |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Case Series | Journal of Dermatology | Twice-weekly 5mg dexamethasone oral pulse in extensive AA (n=30), early foundational protocol |

---

## Germany Market Information

Dexamethasone currently has no registered marketing authorization in the evidence pack (market status: Not Marketed, 0 authorizations). No license records were available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (see Data Gap DG001, classified as **Blocking** for safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexamethasone pulse therapy for alopecia areata is supported by an existing evidence base beyond the TxGNN score alone — including one RCT, a systematic review/network meta-analysis, and multiple cohort/case-series studies — indicating this is an established off-label practice rather than a purely model-generated hypothesis. However, the underlying evidence pack lacks the original indication text, MOA detail, and TFDA/BfArM safety labeling needed for a full safety assessment, so progression must be gated on closing these gaps.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (Blocking gap DG001) — required before S1 safety pre-assessment can proceed
- Mechanism of action detail via DrugBank query (High-priority gap DG002)
- Confirmed original indication list and formal drug classification (currently absent from the evidence pack)
- Drug-drug interaction data (current DDI query status: not found)
- Given the trial evidence is oncology-combination based and not AA-specific, no further AA-specific trial evidence is expected from ClinicalTrials.gov; reliance should remain on the published literature base above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

