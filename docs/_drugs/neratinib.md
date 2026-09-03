---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 4
---

# Neratinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Neratinib is an irreversible pan-HER (HER1/HER2/HER4) tyrosine kinase inhibitor originally developed for HER2-positive breast cancer.
> The TxGNN model predicts it may also be effective for **progesterone-receptor positive breast cancer**,
> with **5 clinical trials** and **9 publications** currently supporting this direction — though most of this evidence comes from overlapping HER2-positive/HR-positive populations rather than a distinctly defined PR-positive cohort.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (per known drug class; not captured in this evidence pack — see Germany market status below) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured MOA field was not available in this evidence pack (data gap DG002). However, literature evidence included in this pack (ExteNET trial, PMID 26874901) describes neratinib as an **irreversible tyrosine-kinase inhibitor of HER1, HER2, and HER4**, originally used to reduce recurrence risk in HER2-positive breast cancer following trastuzumab-based adjuvant therapy.

Progesterone-receptor (PR) status and HER2 status are not mutually exclusive in breast cancer — many patients are HR-positive (ER and/or PR-positive) **and** HER2-positive simultaneously. Several of the retrieved trials directly enroll this overlapping population, for example NCT04886531 ("ER-Positive, HER-2 Positive Cancers") and NCT04901299 ("HR-Positive, HER2-Negative Metastatic Breast Cancer"). This suggests the TxGNN model is likely detecting a real biological relationship — neratinib's HER-pathway blockade combined with endocrine therapy in hormone-receptor-driven, HER2-altered tumors — rather than an entirely novel mechanism.

That said, none of the identified trials or publications specifically define "progesterone-receptor positive breast cancer" as an isolated primary endpoint independent of HER2 status. The prediction should therefore be interpreted as an extension within an already-related disease space (breast cancer, HER-pathway biology) rather than a genuinely new therapeutic area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective multicenter study on HER2-low prevalence, treatment patterns and outcomes in HER2-negative metastatic breast cancer |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib + endocrine therapy + trastuzumab in ER-positive, HER2-positive breast cancer |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Withdrawn | 0 | Neratinib + fulvestrant in previously treated HR-positive, HER2-negative metastatic breast cancer |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A | Completed | 111 | Retrospective observational study of neratinib as extended adjuvant therapy in early-stage HER2+ breast cancer (European EAP) |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Phase 2 | Terminated | 12 | Neratinib targeting EGFR/ERBB2 in HR-positive/HER2-negative, HER2-enriched advanced/metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | Phase 3 RCT | Lancet Oncology | ExteNET trial: neratinib after trastuzumab-based adjuvant therapy reduces recurrence in early-stage HER2+ breast cancer |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | Adaptive Phase 2 Trial | NEJM | I-SPY 2 trial: neratinib added to neoadjuvant chemotherapy in high-risk stage II/III breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Guideline | JNCCN | NCCN Breast Cancer guideline update, covering HER2/endocrine treatment sequencing |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Observational | Breast Cancer Res Treat | Real-world adjuvant neratinib use in HR+/HER2+ early-stage breast cancer; GI toxicity limits continuation |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Expert Roundtable/Review | Clin Breast Cancer | Practice guidance on HER2-positive breast cancer, including neratinib and lapatinib |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Current treatment trends in HR+/HER2+ breast cancer |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Retrospective In Silico Analysis | Breast Cancer Res | ERBB2 mutation status as prognostic marker in ER+, ERBB2 non-amplified lobular breast carcinoma |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Report | Frontiers in Oncology | HER2+ breast cancer with leptomeningeal disease treated with pyrotinib + metronomic vinorelbine |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Review | Clin Adv Hematol Oncol | Overview of metastatic breast cancer subtypes and treatment integration |

---

## Germany Market Information

Neratinib currently holds **no marketing authorization in Germany** (market status: not marketed; 0 authorizations on record). No product-level dosage form or approved indication text is available for this market.

---

## Cytotoxicity

Neratinib is an antineoplastic agent (pan-HER tyrosine kinase inhibitor used in breast cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (irreversible pan-HER1/HER2/HER4 tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not reported as a primary toxicity in the retrieved evidence; per PMID 39153126, the main dose-limiting toxicity in real-world adjuvant use is significant gastrointestinal (diarrhea) rather than hematologic |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | GI symptom monitoring (diarrhea, often requiring prophylaxis/dose reduction per PMID 39153126); liver function; other parameters per package insert |
| Handling Protection | Please refer to institutional guidelines for handling oral antineoplastic/targeted agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is biologically plausible and moderately substantial — it draws on overlapping HER2-positive/HR-positive breast cancer trial populations, including a completed Phase 3 RCT (ExteNET) — but it does not directly address "progesterone-receptor positive breast cancer" as a distinct indication. More critically, TFDA/BfArM safety labeling data is a **Blocking** data gap (DG001), which prevents this candidate from entering the S1 safety pre-assessment stage regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications, DDI) to unblock S1 safety review
- Confirmed structured MOA data from DrugBank (DG002)
- Clarification of whether "progesterone-receptor positive breast cancer" should be treated as a distinct indication or merged with the existing HER2-positive breast cancer evidence base, given substantial population overlap in the cited trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

