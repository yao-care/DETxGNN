---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Established Oncology Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor (camptothecin derivative) already used as a chemotherapy agent in oncology — per trial data in this evidence pack (e.g., NCT01931098), it is described as a drug "used to treat lung cancer."
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**,
> with **5 clinical trials** and **20 publications** currently identified as supporting evidence, though most are small, historical, or preclinical studies rather than confirmatory trials in this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in German license data (no BfArM authorization on file); per trial descriptions in this evidence pack, topotecan is an established chemotherapy for lung cancer and other solid tumors |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this candidate (flagged as a High-severity data gap, DG002). However, the repurposing rationale embedded in this evidence pack identifies topotecan as a **Topoisomerase I inhibitor**: it induces DNA double-strand breaks by trapping the Topo I–DNA cleavage complex, a mechanism confirmed repeatedly in the literature evidence (e.g., PMID 15836850 describes it as "a Camptothecin derivative [that] shows a large spectrum in anti-tumor activity... by inhibition of topoisomerase I activity resulting in double-strand DNA breaks").

Breast cancer cells — particularly triple-negative subtypes (MCF-7, MDA-MB-231) — have been shown in this evidence base to be Topo I-dependent and sensitive to this mechanism (PMID 40300683 identifies TFDP1 as a topotecan-responsive target in TNBC). Several older Phase II trials and pilot studies (PMID 10362325, PMID 11455218, PMID 9413954) already tested topotecan directly in advanced/metastatic breast cancer, including CNS-metastatic disease, suggesting the drug has real, if limited, clinical precedent in this population rather than being a purely computational prediction.

That said, breast cancer is not the drug's mainstream indication, current supporting trials for this specific TxGNN-predicted link are largely older, small, terminated, or of uncertain relevance (several trials in the pack are graded "C" relevance — e.g., ovarian cancer trials where topotecan's role is unclear), and no completed Phase 3 RCT specifically establishes efficacy in breast cancer. The mechanistic plausibility is reasonable, but clinical confirmation is thin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer; trial terminated |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-based high-throughput drug screening platform for refractory solid tumors; not a direct efficacy trial (relevance grade C) |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab/olaparib/cediranib triplet therapy in platinum-resistant ovarian cancer; topotecan's role in this trial is not explicit (relevance grade C) |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's choice single-agent chemotherapy in gBRCA-mutated relapsed ovarian cancer; topotecan may be a comparator arm, not confirmed (relevance grade C) |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with standard chemo/immunotherapy regimens in advanced malignancies; topotecan-specific relevance unclear (relevance grade C) |

**Note:** Only one trial (NCT00006032) directly and unambiguously involves topotecan in breast cancer; it was terminated. The remaining four are graded low relevance and warrant re-verification before being counted as supporting evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II clinical trial | American Journal of Clinical Oncology | CALGB Phase II trial of topotecan in advanced/pretreated breast cancer patients (n=47 eligible) |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Cohort/Pilot | Onkologie | Pilot study of topotecan as primary chemotherapy for breast cancer patients with brain metastases |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Cohort/Pilot (Phase II) | British Journal of Cancer | Infusional topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy vs. bolus dosing |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Mechanistic/Preclinical | International Journal of Biological Macromolecules | TFDP1 identified as a therapeutic target for topotecan in triple-negative breast cancer |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib shows potent efficacy in preclinical TNBC models |
| [27444351](https://pubmed.ncbi.nlm.nih.gov/27444351/) | 2016 | Preclinical | Phytomedicine | MHP-1 (Cordyceps-derived) restores topotecan sensitivity via EMT/TGF-β regulation in breast cancer cells |
| [15836850](https://pubmed.ncbi.nlm.nih.gov/15836850/) | 2005 | In vitro | Journal of Surgical Research | Quercetin combined with topotecan increases cytotoxicity in MCF-7 and MDA-MB-231 cells |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | In vitro | Pharmacological Research | Daidzein enhances topotecan efficacy and reverses BCRP-mediated drug resistance in breast cancer |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-Geburtshilfliche Rundschau | Review of new cytotoxic drugs, including topotecan, in breast carcinoma therapy |
| [7910993](https://pubmed.ncbi.nlm.nih.gov/7910993/) | 1994 | Review | World Journal of Surgery | General review of systemic management options for metastatic breast cancer |

---

## Germany Market Information

Topotecan currently has **no BfArM authorization records** in this evidence pack — the drug is marked as not marketed in Germany (0 licenses on file).

---

## Cytotoxicity

Topotecan is a conventional cytotoxic chemotherapy agent (camptothecin derivative, Topoisomerase I inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin class) |
| Myelosuppression Risk | High — literature in this pack (PMID 8617580) reports myelosuppression as the major toxicity, with severe nadir counts (leukocyte, neutrophil, hemoglobin, platelet all markedly reduced) |
| Emetogenicity Classification | Not specified in evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential (given documented severe myelosuppression), plus standard organ function monitoring per institutional oncology protocol |
| Handling Protection | Requires cytotoxic drug handling precautions per standard chemotherapy handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data for topotecan are not available in this evidence pack (flagged as Blocking data gap DG001 — TFDA/German label warnings and contraindications).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L3 — supporting data consist mainly of small pilot/Phase II studies, preclinical/in vitro work, and reviews, with no completed pivotal trial confirming efficacy of topotecan specifically in breast cancer, and several cited trials carry low relevance grades. The drug is also not currently marketed in Germany, and a Blocking-severity safety data gap (no label warnings/contraindications) prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/German label safety data (warnings, contraindications) — Blocking gap DG001
- Confirmed mechanism-of-action documentation from DrugBank — High-severity gap DG002
- Verification of the low-relevance ("grade C") trials to confirm whether topotecan is actually used in those regimens
- Completion of "pending" literature classifications (study type/tier) to properly assess evidence strength
- Clarification of topotecan's actual original/approved indication(s), since regulatory license data is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

