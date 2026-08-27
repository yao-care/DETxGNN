---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Alpelisib: From Advanced Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib is a PI3Kα (PIK3CA)-selective inhibitor whose structured original-indication and mechanism-of-action fields are currently missing from the regulatory record, but the supporting literature in this evidence pack repeatedly references its use in advanced breast cancer. The TxGNN model predicts a possible new indication in **Pulmonary Hypertension** (score 99.03%), but this prediction is currently supported only by a mismatched clinical trial and two tier-3 publications — one of which reports a drug-induced lung toxicity signal that runs counter to the treatment hypothesis. Given the absence of direct efficacy evidence and an unresolved safety data gap, this candidate is not ready to advance past initial screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured regulatory data (see Data Gaps); literature context suggests advanced HR+/HER2- breast cancer |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for alpelisib is not populated in the current regulatory record (flagged as a High-severity data gap). Based on the evidence available in this pack, alpelisib is a PI3Kα (PIK3CA)-selective inhibitor, and the accompanying literature and trial records indicate it is used in advanced HR+/HER2-negative breast cancer.

The mechanistic rationale for the pulmonary hypertension prediction rests on the PI3K/Akt/mTOR pathway's known theoretical role in pulmonary vascular smooth muscle cell proliferation and vascular remodeling — a pathway explored preclinically as a potential therapeutic target in pulmonary arterial hypertension (PAH). This pathway-level association is the likely driver of the high TxGNN score.

However, this link remains purely mechanistic. There is no direct evidence of alpelisib efficacy in PAH models or patients. More importantly, the literature in this pack shows the opposite signal: alpelisib has been reported to induce interstitial lung disease (ILD), and PI3Kα pathway inhibition has been associated with biventricular cardiac atrophy and right ventricular dysfunction in preclinical models. Both findings represent potential mechanisms for **worsening** rather than treating pulmonary hypertension, so the current evidence should be read as a safety caution rather than a supportive signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Retrospective real-world study of ribociclib vs. **alpelisib** in HR+/HER2- advanced/metastatic breast cancer. **Not relevant to pulmonary hypertension** — the trial evaluates a different indication (breast cancer) and its primary comparator is ribociclib, not alpelisib; flagged as a data-mismatch (relevance grade C) and should not be treated as supporting evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Reports alpelisib-induced interstitial lung disease (ILD) in a patient with advanced breast cancer — a pulmonary toxicity signal, not evidence of benefit in pulmonary hypertension. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical/Experimental | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin caused biventricular cardiac atrophy and right ventricular dysfunction in an animal model — raises concern about right-heart effects rather than supporting a PAH treatment rationale. |

---

## Germany Market Information

Alpelisib currently has no marketing authorization registered in Germany (0 authorizations; market status: not marketed).

---

## Cytotoxicity

Available evidence (literature context referencing "advanced breast cancer" and a PI3Kα-selective mechanism) indicates alpelisib is an oncology drug used as a targeted therapy rather than a conventional cytotoxic agent. Structured DrugBank category and toxicity data are not present in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kα inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Pulmonary function/respiratory symptoms (given the ILD signal in the literature above); please refer to the package insert for the full monitoring panel |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data for alpelisib are not currently available in this evidence pack (this is flagged as a **Blocking** data gap — DG001 — that must be resolved before this candidate can proceed to initial safety screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No direct clinical or preclinical evidence supports alpelisib efficacy in pulmonary hypertension — the only registered clinical trial is a mismatched breast-cancer study, and the two available publications point to a pulmonary/cardiac toxicity signal rather than a therapeutic benefit. This is compounded by a Blocking data gap in TFDA/EU package insert safety data, which prevents the candidate from entering the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Package insert warnings/contraindications data (DG001, Blocking — required for S1 safety screening)
- Confirmed mechanism of action and original approved indication (DG002, High)
- DrugBank drug-category and toxicity classification data
- Drug-drug interaction (DDI) profile
- Direct preclinical or clinical evidence of alpelisib activity in pulmonary hypertension/PAH models, specifically addressing the ILD and right-ventricular-dysfunction safety signals identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

