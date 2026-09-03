---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
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

# Trastuzumab Emtansine: From HER2-Positive Breast Cancer to Progesterone-Receptor-Positive Breast Cancer

## One-Sentence Summary

Trastuzumab emtansine (T-DM1) is an antibody-drug conjugate combining the anti-HER2 antibody trastuzumab with the cytotoxic microtubule inhibitor DM1, historically used in HER2-positive breast cancer. The TxGNN model predicts additional benefit in **progesterone-receptor (PR) positive breast cancer**, supported by **4 clinical trials** and **15 publications** — though as detailed below, this largely reflects an existing HER2+ subgroup rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (formal `original_indications` field is empty — a data gap, not a true clinical blank; internal rationale text identifies HER2-positive breast cancer as the established use) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (0 licenses on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is a flagged data gap (DG002). Based on what is available in this evidence pack's own analysis, trastuzumab emtansine is an antibody-drug conjugate: the trastuzumab antibody component binds HER2-overexpressing tumor cells, delivering the conjugated payload DM1 (mertansine), a maytansinoid microtubule inhibitor, directly into the cell to induce cytotoxicity.

Critically, the evidence pack's own rationale flags an important caveat: PR status is a commonly co-existing biomarker in breast cancer, not an independent pharmacological target of T-DM1. The drug's activity is driven by HER2 expression, not PR status. This means the "PR-positive breast cancer" prediction substantially overlaps with the population already captured under the existing HER2-positive breast cancer indication — this is best understood as a biomarker-refined subgroup of an existing use, not a true novel repurposing signal.

Mechanistically, T-DM1 remains applicable wherever HER2 overexpression coexists with PR positivity (e.g., HR+/HER2+ disease), since PR status only informs whether concurrent endocrine therapy should be added — it does not change the drug's target engagement. Clinical selection should therefore continue to be anchored on HER2 status, with PR status used only as an adjunct for endocrine-therapy sequencing decisions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab or placebo + neoadjuvant ddAC-paclitaxel-trastuzumab-pertuzumab in early HER2-positive breast cancer; strongest RCT-level evidence in this set (Grade A) |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab in preoperative HER2-positive breast cancer, examining impact of HER2 heterogeneity on response |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective, non-interventional study on HER2-low prevalence/characteristics in metastatic breast cancer; weak direct relevance (Grade C) |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | De-escalation of adjuvant chemotherapy in ER-negative, node-negative HER2+ early breast cancer after pCR; population is ER-negative, not PR-stratified (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline | J Clin Oncol | ASCO clinical practice guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Review/Guideline | J Clin Oncol | Earlier ASCO practice guideline for HER2-positive advanced breast cancer systemic therapy |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline/Review | Eur J Cancer | EGTM biomarker guideline noting HER2 (not PR alone) determines eligibility for anti-HER2 agents including T-DM1 |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncol | Reviews HR+/HER2+ breast cancer treatment trends, including T-DM1 in hormone-receptor co-positive disease |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Overview of targeted/cytotoxic breast cancer inhibitors, discussing HER2/HR/ER/PR-based treatment selection |
| [35140078](https://pubmed.ncbi.nlm.nih.gov/35140078/) | 2022 | Case Report | BMJ Case Rep | Receptor conversion (biomarker status change) in breast cancer, illustrating limits of static PR/HER2 classification |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Report | Front Oncol | Leptomeningeal metastasis case in HER2-positive, PR-negative breast cancer treated with alternative anti-HER2 regimen |
| [40642740](https://pubmed.ncbi.nlm.nih.gov/40642740/) | 2025 | Case Report | J Med Cases | Case of HER2-mutated triple-negative breast cancer responding to a related anti-HER2 ADC |
| [37445276](https://pubmed.ncbi.nlm.nih.gov/37445276/) | 2023 | Preclinical | J Clin Med | In vitro study of an aminosteroid compound across breast cancer molecular subtypes, including PR-stratified subtypes |

---

## Taiwan Regulatory & Market Status

Trastuzumab emtansine is **not currently marketed** in this dataset — 0 authorizations on file, no license records available. No approved-indication text, product names, or dosage forms could be extracted.

---

## Cytotoxicity

*(Included because T-DM1 is an antibody-drug conjugate carrying a cytotoxic microtubule-inhibitor payload.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC); anti-HER2 antibody conjugated to DM1 (mertansine), a maytansinoid microtubule inhibitor cytotoxic payload |
| Myelosuppression Risk | Not available in this evidence pack — please refer to the package insert (blocked by data gap DG001) |
| Emetogenicity Classification | Not available in this evidence pack — please refer to the package insert (blocked by data gap DG001) |
| Monitoring Items | Not available in this evidence pack — please refer to the package insert (blocked by data gap DG001) |
| Handling Protection | Given the cytotoxic ADC payload, cytotoxic-drug handling precautions are likely warranted, but a formal handling protocol is not available in this evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information. All key warnings, contraindications, and drug-drug interaction data in this evidence pack are marked as unresolved data gaps (DG001, Blocking severity) — a TFDA package-insert review is required before any safety-related conclusions can be drawn.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The PR-positive breast cancer prediction is supported by one completed Phase 3 RCT (IMpassion050) and a body of ASCO/EGTM guideline literature, meeting L1 evidence criteria per the evidence pack's own scoring. However, this predicted indication substantially overlaps with the drug's already-established HER2-positive breast cancer use — PR status is a co-existing biomarker, not an independent target — so the "new indication" value here is limited, and safety data remain entirely unresolved.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA package insert for warnings/contraindications before any safety sign-off
- Resolve DG002: obtain a formal, structured MOA record from DrugBank rather than relying on rationale-text mentions
- Clarify the true original approved indication, since `original_indications` is empty despite this being a globally marketed drug — this gap should be closed before finalizing any "original → new indication" narrative
- Confirm whether the PR+ subgroup adds any clinical decision-making value beyond existing HER2-status-based selection, or whether this prediction should be reclassified as confirmatory rather than novel
- If Taiwan market entry is being considered, a full registration pathway assessment is required given 0 current licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

