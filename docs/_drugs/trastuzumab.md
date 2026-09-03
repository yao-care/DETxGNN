---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Trastuzumab is an anti-HER2 monoclonal antibody whose standard use is in HER2-positive breast cancer.
> The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
> with **36 clinical trials** and **20 publications** currently supporting this direction.
> Note: this predicted indication largely represents a molecular-subtype refinement (PR status as a stratification factor) within the already-recognized HER2-positive breast cancer population, rather than a mechanistically novel disease target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (referenced in evidence rationale text; no formal license text available in this evidence pack) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available in this evidence pack (original_moa is a data gap). Based on the information embedded in the trial/literature rationale, trastuzumab is an anti-HER2 (human epidermal growth factor receptor 2) monoclonal antibody, and its efficacy in HER2-positive breast cancer is well established as the current standard indication.

The predicted new indication — PR-positive breast cancer — is not a distinct mechanistic target. As stated directly in the evidence pack's repurposing rationale: *"PR status is a stratification factor rather than a new mechanistic target; this represents a molecular-subtype extension of the existing indication."* In practice, PR positivity frequently co-occurs with HER2 positivity (so-called "triple-positive" breast cancer, ER+/PR+/HER2+), and trastuzumab's HER2-targeted mechanism remains the operative driver of efficacy in this subgroup.

This is why the prediction is mechanistically plausible: multiple completed trials specifically enrolled HER2-positive patients who were also hormone-receptor positive (ER and/or PR positive), e.g. letrozole + trastuzumab (NCT00134680) and abemaciclib + trastuzumab ± fulvestrant (monarcHER, PMID 32353342), demonstrating that HER2-targeted therapy retains activity when combined with endocrine-pathway-directed agents in PR+/HER2+ disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Randomized, double-blind trial of QL1209 (pertuzumab biosimilar) + trastuzumab + docetaxel vs. reference pertuzumab + trastuzumab + docetaxel in ER/PR-negative, HER2+ early/locally advanced breast cancer — direct biosimilar/efficacy evidence for trastuzumab-based regimens |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm randomized study of Herceptin (trastuzumab) + docetaxel ± pertuzumab in HER2-positive locally advanced/inflammatory/early breast cancer, evaluating pathological complete response |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Combination of letrozole + trastuzumab in ErbB2-positive AND estrogen/progesterone-receptor-positive metastatic breast cancer — directly relevant to the PR+/HER2+ subgroup |
| [NCT03095352](https://clinicaltrials.gov/study/NCT03095352) | Phase 2 | Completed | 76 | Pembrolizumab + carboplatin vs. carboplatin alone in breast cancer patients with chest wall disease, including hormone-resistant ER+/PR+/HER2- and triple-negative subsets |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3436 | Doxorubicin + cyclophosphamide followed by weekly paclitaxel with or without trastuzumab as adjuvant treatment for HER2-overexpressing node-positive or high-risk node-negative breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy alone vs. chemotherapy plus trastuzumab in node-positive or high-risk node-negative HER2-low invasive breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy plus lapatinib vs. plus trastuzumab as first-line therapy for HER2/neu-positive metastatic breast cancer |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | Recruiting | 1100 | Double-blind, randomized, placebo-controlled study of trastuzumab as short-duration preoperative therapy in HER2-neu-positive operable breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab or placebo combined with neoadjuvant doxorubicin+cyclophosphamide followed by paclitaxel+trastuzumab+pertuzumab in early HER2-positive breast cancer |
| [NCT02654119](https://clinicaltrials.gov/study/NCT02654119) | Phase 2 | Completed | 20 | Adjuvant cyclophosphamide, paclitaxel with trastuzumab in Stage I-II HER2/neu-positive breast cancer patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT (Tier 1) | The Lancet. Oncology | ExteNET phase 3 trial: neratinib after trastuzumab-based adjuvant therapy improved outcomes in HER2-positive early breast cancer |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: neoadjuvant endocrine therapy + trastuzumab + pertuzumab vs. de-escalated chemotherapy in HR-positive/HER2-positive early breast cancer |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | The Lancet. Oncology | monarcHER phase 2 trial: abemaciclib + trastuzumab ± fulvestrant vs. chemotherapy + trastuzumab in hormone receptor-positive, HER2-positive advanced breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | The Lancet. Oncology | NeoSphere 5-year analysis: neoadjuvant pertuzumab + trastuzumab in HER2-positive breast cancer, showing sustained pathological complete response benefit |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis (Tier 1) | Lancet | EBCTCG overview of chemotherapy and hormonal therapy effects on recurrence and 15-year survival in early breast cancer |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Cohort (Tier 2) | NEJM | 20-year risk of breast-cancer recurrence after stopping endocrine therapy at 5 years in ER-positive early breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohort | Theranostics | Molecular portraits and trastuzumab responsiveness specifically in ER-positive, PR-positive, and HER2-positive ("triple-positive") breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO Guideline Update: systemic therapy recommendations for advanced HER2-positive breast cancer |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective cohort | BMC Cancer | Trastuzumab and fulvestrant combination therapy in hormone receptor- and HER2-positive advanced breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 trial | Annals of Oncology | WSG-ADAPT HER2+/HR- trial: 12-week neoadjuvant dual HER2 blockade (trastuzumab + pertuzumab) ± paclitaxel, de-escalation strategy |

---

## Germany Market Information

This drug currently holds **no marketing authorizations in Germany** in this evidence pack (market status: Not Marketed; total authorizations: 0). No license records are available to summarize dosage forms or approved indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody); not a conventional cytotoxic chemotherapeutic per the evidence pack's rationale text |
| Myelosuppression Risk | Not directly characterized in this evidence pack. Trial evidence instead identifies cardiac toxicity, rather than myelosuppression, as the primary monitored risk specific to trastuzumab (see NCT01436604) |
| Emetogenicity Classification | Please refer to the package insert |
| Monitoring Items | Cardiac function (LVEF/echocardiogram), based on a dedicated cardiotoxicity-monitoring trial (NCT01436604); CBC and liver/renal function when trastuzumab is combined with cytotoxic chemotherapy partners |
| Handling Protection | Please refer to the package insert warnings and precautions; standard biologic/antibody handling applies to trastuzumab monotherapy, with cytotoxic-drug handling protocols relevant only when combined with conventional chemotherapy agents |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The PR-positive breast cancer indication is supported by evidence level L1 (multiple completed Phase 2/3 trastuzumab-based trials in HER2-positive/hormone-receptor-positive breast cancer), but it functions as a molecular-subtype extension of trastuzumab's existing HER2-positive breast cancer indication rather than a novel target — and a Blocking-severity safety data gap currently prevents formal safety pre-assessment.

**To proceed, the following is needed:**
- Resolve Blocking gap **DG001**: obtain TFDA/official label warnings and contraindications (label PDF retrieval and parsing) — this is required before the candidate can enter S1 safety pre-assessment
- Resolve High-severity gap **DG002**: obtain formal MOA documentation from DrugBank to support mechanistic-linkage analysis
- Confirm PR-positivity biomarker stratification protocols, since current evidence treats PR status as a stratification factor rather than an independent therapeutic target
- Clarify the drug's regulatory/market status in Germany, given 0 current authorizations and "Not Marketed" status
- Run a proper drug-drug interaction query, as the current DDI check returned "not_found"

---

**Additional note:** This evidence pack also scored several other candidate indications for trastuzumab (e.g., normal breast-like subtype [L3], PR-negative breast cancer [L2], luminal A/B breast tumor [L2], and five rare non-breast tumor types [all L5, no supporting trials/literature, recommendation: Hold]). These are substantially weaker than the PR-positive breast cancer prediction and are not recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

