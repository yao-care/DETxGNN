---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Antiplatelet Therapy (ACS/PCI) to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine-class P2Y12 receptor inhibitor, an antiplatelet drug clinically established for acute coronary syndrome (ACS) and percutaneous coronary intervention (PCI) settings. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but currently only **2 clinical trials** and **2 publications** are available, and none of them directly study prasugrel in pulmonary hypertension patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack; clinically known as an antiplatelet agent for ACS/PCI (thienopyridine class) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, prasugrel belongs to the thienopyridine class of P2Y12 platelet receptor inhibitors, and its efficacy in reducing thrombotic events following ACS/PCI is well established.

The theoretical link to pulmonary hypertension rests on the pathophysiology of chronic thromboembolic pulmonary hypertension (CTEPH), a subtype in which recurrent pulmonary thrombus formation contributes to disease progression — a process where antiplatelet mechanisms could plausibly play a role. However, this connection is inferential rather than evidence-based: the two retrieved trials concern cancer-associated venous thromboembolism eligibility and NOAC use in atrial fibrillation, neither involving prasugrel or pulmonary hypertension directly (both graded "C" relevance — background topical overlap only). The two retrieved publications likewise discuss COVID-19 comorbidity therapy and clopidogrel/prasugrel adherence after PCI, again without addressing pulmonary hypertension.

Given the absence of any drug-specific or indication-specific study, this prediction should be regarded as a model-generated hypothesis (L5) rather than an evidence-supported repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility of cancer-associated thrombosis patients for trials like CARAVAGGIO; does not involve prasugrel or pulmonary hypertension (low relevance — background thrombosis field only). |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational study of NOAC (oral anticoagulant, not antiplatelet) management in elderly atrial fibrillation patients in Spain; drug class and indication both mismatched (low relevance). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Examines clopidogrel/prasugrel use and adherence after PCI in ACS patients; relevant to prasugrel's established antiplatelet use, not to pulmonary hypertension. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | ACTIV COVID-19 registry analysis of background cardiovascular therapy on infection outcomes; no direct connection to prasugrel or pulmonary hypertension. |

---

## Germany Market Information

No marketing authorization records are currently available for this drug (market status: not marketed, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary hypertension) is supported only by the TxGNN model score, with no drug-specific or indication-specific clinical trials or literature (Evidence Level L5). The retrieved trials and publications are only tangentially related to antiplatelet/anticoagulant therapy in general cardiovascular contexts and do not address prasugrel's use in pulmonary hypertension.

**To proceed, the following is needed:**
- TFDA/BfArM label warnings and contraindications (DG001, blocking) — required before any S1 safety assessment can begin
- Structured mechanism-of-action data from DrugBank (DG002)
- Preclinical or mechanistic studies specifically linking P2Y12 inhibition to pulmonary vascular remodeling or CTEPH pathophysiology
- Consider re-evaluating **migraine disorder** (rank 2 in this evidence pack, Evidence Level L3, decision stage S1 "Research Question") as an alternative candidate, given its comparatively stronger literature signal (thienopyridine-class effect on PFO-related migraine)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

