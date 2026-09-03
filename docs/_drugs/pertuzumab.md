---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Pertuzumab (Perjeta) is a HER2-targeted monoclonal antibody originally developed and used for HER2-positive breast cancer.
> The TxGNN model predicts it may also be effective in **progesterone-receptor (PR) positive breast cancer**,
> with **10 clinical trials** and **20 publications** currently supporting this direction — though this largely reflects a biomarker-subgroup extension of an existing indication rather than a novel mechanistic repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (inferred from trial/evidence context; no formal indication text available in this data pack) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism of action (MOA) data is not available in this evidence pack. However, based on the repurposing rationale accompanying the prediction, pertuzumab is known to inhibit HER2/HER3 heterodimerization, blocking downstream signaling that drives proliferation in HER2-overexpressing tumors. Its pharmacological target is HER2 overexpression itself, not the progesterone receptor.

PR-positive status is a commonly co-occurring biomarker in HER2-positive breast cancer, rather than an independent therapeutic target for pertuzumab. As a result, this prediction is **not a classic drug repurposing case** in the sense of finding a new disease mechanism — it reflects an established indication (HER2+ breast cancer) being extended into a biomarker-defined subgroup (HER2+/PR+ disease). This is further supported by real-world data (e.g., PMID 37723497) suggesting PR status may actually be a more decisive factor than ER status in determining benefit from adding pertuzumab to neoadjuvant therapy in HER2+/node-positive patients.

Because the underlying mechanism (HER2 blockade) is unchanged and the trial evidence base overlaps substantially with the approved HER2+ indication, the applicability of the mechanism to this population is well-supported — but reviewers should treat this as **indication refinement**, not a de novo repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant trial comparing Herceptin + docetaxel ± pertuzumab combinations in locally advanced/early HER2+ breast cancer; foundational pCR evidence. |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) (IMpassion050) | Phase 3 | Completed | 454 | Placebo-controlled trial of atezolizumab added to neoadjuvant anthracycline/paclitaxel + trastuzumab + pertuzumab in early HER2+ breast cancer. |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Randomized, double-blind trial evaluating a pertuzumab biosimilar (QL1209) vs. pertuzumab + docetaxel in early/locally advanced HER2+, ER/PR-negative breast cancer. |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Double-blind biosimilar (BCD-178) vs. Perjeta comparison as neoadjuvant therapy in HER2+ (ER/PR-negative) breast cancer. |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) (NEOADAPT) | Phase 2 | Unknown | 7 | Single-arm, chemotherapy-free neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab in HR+ (ER+/PR+), HER2+ early breast cancer. |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Multicenter retrospective study characterizing HER2-low prevalence, treatment patterns, and outcomes in HER2-negative metastatic breast cancer. |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) (TBCRC 023) | Phase 2 | Active, not recruiting | 128 | Randomized neoadjuvant trial of lapatinib + trastuzumab ± endocrine therapy for 12 vs. 24 weeks in HER2-overexpressing breast cancer. |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Studies HER2 heterogeneity impact using T-DM1 + pertuzumab preoperatively in early-stage HER2+ breast cancer. |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) (DECRESCENDO) | Phase 2 | Terminated | 139 | De-escalation of adjuvant chemotherapy after pCR to neoadjuvant taxane + pertuzumab/trastuzumab in HER2+/ER-negative, node-negative disease. |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) (ARETTA) | Phase 2 | Withdrawn | 0 | Withdrawn single-arm study of neoadjuvant weekly paclitaxel in Nigerian women with breast cancer; no data generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Annals of Oncology | WSG-ADAPT HER2+/HR- Phase II trial: assessed 12-week de-escalated neoadjuvant dual HER2 blockade ± chemotherapy, with predictive markers for pCR. |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II trial: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer. |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review/Guideline | J Clin Oncol | ASCO Guideline Update on systemic therapy for advanced HER2-positive breast cancer. |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort (long-term follow-up) | Lancet Oncology | NeoSphere 5-year follow-up: neoadjuvant pertuzumab + trastuzumab improved pCR and long-term outcomes in HER2+ breast cancer. |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase II, PERTAIN) | J Clin Oncol | First-line trastuzumab + aromatase inhibitor ± pertuzumab in HER2+/HR+ metastatic or locally advanced breast cancer. |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (biosimilar equivalence) | British Journal of Cancer | QL1209 (pertuzumab biosimilar) vs. reference pertuzumab in HER2+, ER/PR-negative neoadjuvant treatment. |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | Trial protocol/analysis | Future Oncology | DECRESCENDO trial: de-escalating chemotherapy in HER2+, ER-negative, node-negative early breast cancer with dual HER2 blockade. |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Review | Southern Medical Journal | Overview of neoadjuvant/adjuvant breast cancer therapy across molecular subtypes, including HER2-enriched disease. |
| [33902424](https://pubmed.ncbi.nlm.nih.gov/33902424/) | 2022 | Review | Endocrine Metab Immune Disord Drug Targets | Review of immunotherapy and targeted approaches (including trastuzumab/pertuzumab) in breast cancer treatment. |
| [40282499](https://pubmed.ncbi.nlm.nih.gov/40282499/) | 2025 | Review/Proposal | Cancers | Operational proposal for adjuvant metronomic chemotherapy plus targeted/anti-hormonal therapy in HER2+/ER-PR+ early breast cancer. |

---

## Germany Market Information

Pertuzumab is currently **not marketed** in Germany according to this data pack (0 authorizations on record). No product license or approved indication text is available for extraction.

---

## Cytotoxicity

Pertuzumab is an anti-HER2 monoclonal antibody and is antineoplastic by original indication (HER2-positive breast cancer), though it is not a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; blocks HER2/HER3 heterodimerization) |
| Myelosuppression Risk | Low as monotherapy; risk increases when combined with taxanes/other chemotherapy (as in most trial regimens, e.g., docetaxel combinations) |
| Emetogenicity Classification | Low (minimal intrinsic emetogenic potential; combination regimens follow the emetogenicity of the chemotherapy partner) |
| Monitoring Items | Left ventricular ejection fraction (LVEF)/cardiac function, infusion-related reactions, CBC when combined with cytotoxic chemotherapy |
| Handling Protection | Standard biologic infusion precautions; not subject to cytotoxic drug handling regulations as monotherapy — please refer to the package insert for combination-regimen specifics |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence meets L1 criteria with two completed Phase 3 RCTs (NCT04629846, NCT03726879) and multiple tier-1 literature sources (WSG-ADAPT, WSG-TP-II, PERTAIN, ASCO Guideline) supporting pertuzumab use in HER2+/PR-status-defined breast cancer subgroups. However, since HER2 status — not PR status — is the actual pharmacological target, this should be framed as a biomarker-subgroup indication refinement within the existing HER2+ breast cancer indication rather than a novel repurposing hypothesis.

**To proceed, the following is needed:**
- Formal MOA and TFDA/BfArM label data (currently flagged as Blocking/High data gaps in this evidence pack)
- Confirmation of German market entry strategy, given zero current authorizations
- Clarification of the regulatory pathway: whether this represents a label refinement (biomarker subgroup) vs. a genuinely new indication claim
- Safety monitoring plan specific to HER2+/PR+ populations, particularly cardiac monitoring given anti-HER2 class effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

