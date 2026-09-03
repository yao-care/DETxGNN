---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: From Psoriasis to Dermatitis (Atopic Dermatitis)

## One-Sentence Summary

Ustekinumab is an IL-12/IL-23 p40 antagonist monoclonal antibody; per literature evidence in this pack it is already approved for psoriasis, psoriatic arthritis, Crohn's disease and ulcerative colitis, though no formal German (BfArM) licensing data is available in this evidence pack.
The TxGNN model predicts it may be effective for **Dermatitis (Atopic Dermatitis)**, supported by **7 clinical trials** (including 2 completed Phase 2 RCTs) and **20 publications**.
However, a **Blocking** data gap on TFDA/BfArM safety labeling means this candidate cannot yet complete a safety pre-assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Germany regulatory data provided (0 licenses on file). Per literature evidence (PMID 36208443), ustekinumab is elsewhere approved for psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis |
| Predicted New Indication | Dermatitis (Atopic Dermatitis) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this evidence pack (data gap). However, the literature evidence collected here consistently describes ustekinumab as a fully human IgG1 monoclonal antibody that binds the shared p40 subunit of interleukin (IL)-12 and IL-23, thereby suppressing Th1, Th17 and Th22 pathway activation (PMID 27304428, PMID 36208443). This class of biologic is already used to treat inflammatory diseases with a strong Th17/Th22 signature, most notably psoriasis and psoriatic arthritis.

Atopic dermatitis shares overlapping Th17/Th22-driven inflammatory pathology with psoriasis, even though the two conditions are clinically distinct (Th2-dominant in AD vs. Th17-dominant in psoriasis). Several groups have therefore tested whether blocking IL-12/23 with ustekinumab also benefits AD patients, reasoning that Th22 suppression in particular could reduce epidermal hyperplasia and barrier dysfunction seen in chronic AD lesions (PMID 27745907 demonstrated measurable down-regulation of Th2/Th22 markers with ustekinumab in severe AD).

Results across the identified studies are mixed — some placebo-controlled trials (e.g., the Japanese Phase 2 study, PMID 28338223) showed only modest separation from placebo, and systematic reviews/meta-analyses (PMID 33074565, PMID 29098604) conclude that evidence for biologics targeting IL-12/23 in AD is still inconsistent compared with IL-4/IL-13-targeted agents. This tempers, but does not eliminate, the mechanistic plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Completed | 32 | Randomized pilot study of ustekinumab in chronic atopic dermatitis patients with sub-optimal response to prior therapy |
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Completed | 79 | Randomized, double-blind, placebo-controlled study of two ustekinumab doses in Japanese adults with severe atopic dermatitis |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Completed | 676 | CLEAR trial — secukinumab vs. ustekinumab in moderate-to-severe plaque psoriasis (original indication comparator study, not AD) |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completed | 126 | Cardiovascular risk assessment in severe psoriasis patients treated with biologic agents including ustekinumab |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective pharmacogenetic cohort study on 10-year survival of biologic therapies (including ustekinumab) in cutaneous psoriasis/PsA |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Recruiting | 45 | Suction-blistering contact dermatitis model to study how biologics modulate skin inflammation |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice delivering FDA-approved AD/psoriasis drugs (including ustekinumab) directly into skin for comparative efficacy testing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase 2) | Experimental Dermatology | Double-blind, placebo-controlled trial in 33 moderate-to-severe AD patients assessing ustekinumab efficacy/safety |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase 2) | British Journal of Dermatology | Randomized, double-blind, placebo-controlled study of ustekinumab in Japanese patients with severe AD |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic Review/Meta-analysis | Allergy | EAACI evidence base review of systemic treatments (including ustekinumab) for moderate-to-severe AD |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Systematic Review | J Dermatolog Treat | Systematic review of ustekinumab efficacy and safety specifically in AD treatment |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Systematic Review/Meta-analysis | Am J Clin Dermatol | Meta-analysis asking whether biologics (incl. ustekinumab) are efficacious in AD |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatologic Therapy | Review of off-label uses of ustekinumab, describing its IL-12/23 mechanism and approved indications |
| [30850043](https://pubmed.ncbi.nlm.nih.gov/30850043/) | 2019 | Review | Dermatologic Clinics | Review of emerging AD treatments, contextualizing ustekinumab among newer targeted agents |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Real-world/Observational | J Dermatolog Treat | Real-world evidence analysis of ustekinumab effectiveness in AD patients |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | Real-world Safety (FAERS) | Int Immunopharmacology | FDA adverse event reporting system analysis of ustekinumab safety in psoriasis/PsA |
| [27745907](https://pubmed.ncbi.nlm.nih.gov/27745907/) | 2017 | Clinical Study | J Am Acad Dermatol | Ustekinumab in severe AD associated with down-regulation of Th2/Th22 gene expression |

---

## Germany Market Information

Ustekinumab is currently **not marketed in Germany** according to this evidence pack (0 authorizations on file). No BfArM license records, product names, dosage forms, or approved indication texts are available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Key warnings, contraindications, and drug-interaction data for ustekinumab are flagged as a **Blocking** data gap (DG001 — missing TFDA/BfArM label) in this evidence pack, meaning a formal safety pre-assessment (S1) cannot yet be performed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for ustekinumab in dermatitis/atopic dermatitis is moderate (L2: two completed Phase 2 RCTs plus supportive systematic reviews), but a **Blocking** data gap on official safety labeling (DG001) prevents completion of the S1 safety pre-assessment, and the drug currently has no marketing authorization in Germany.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — required to clear the Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank API (DG002)
- Formal drug-drug interaction (DDI) data
- Clarification of German regulatory pathway, since the drug is not currently marketed there
- Reconciliation of mixed efficacy signals across the AD trials/reviews (some show only modest benefit vs. placebo) before advancing to later decision stages
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

