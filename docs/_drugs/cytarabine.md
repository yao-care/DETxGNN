---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

> Cytarabine is a pyrimidine antimetabolite classically used in the treatment of acute leukemia (AML/ALL).
> The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma**,
> with **3 clinical trials** and **20 publications** currently supporting this direction — though most of this evidence originates from historical (1980s–1990s) chemotherapy regimens rather than the current standard of care for SCLC.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from license/regulatory records (no German market authorization on file); classical literature-documented indication is acute leukemia (AML) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, cytarabine is a cytidine analog that is intracellularly phosphorylated to Ara-CTP, which is incorporated into DNA and inhibits DNA polymerase, blocking DNA synthesis in the S-phase of the cell cycle. This S-phase specificity makes it broadly cytotoxic to rapidly dividing malignant cells, which historically supported its use against leukemias.

Small cell lung carcinoma is one of the most rapidly proliferating solid tumors, sharing the high-growth-fraction biology that made cytarabine effective in leukemia. This mechanistic overlap was explored clinically in the 1980s, when cytarabine (Ara-C) was combined with cisplatin, vindesine, or cyclophosphamide/doxorubicin/vincristine (CAV) regimens for both SCLC and NSCLC.

However, the current standard of care for SCLC (etoposide plus platinum) has since superseded cytarabine-containing regimens, and no contemporary registered trial tests cytarabine specifically in SCLC. The mechanistic rationale is biologically plausible but reflects a clinical role that has already been replaced by newer agents — supporting a research/hypothesis-generating framing rather than a near-term repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal **pemetrexed** (not cytarabine) combined with radiotherapy for leptomeningeal metastasis from solid tumors; low direct relevance to cytarabine/SCLC |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; cytarabine mentioned only as a historical comparator drug, not tested |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine/cisplatin/docetaxel/gemcitabine/pemetrexed) vs. observation in early-stage NSCLC; cytarabine not part of the tested regimens, disease is NSCLC not SCLC |

**Note:** None of the currently registered trials directly test cytarabine in small cell lung carcinoma; all three are low-relevance (Grade C).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Clinical trial (historic) | Medical and Pediatric Oncology | Cyclophosphamide + Adriamycin + cytosine arabinoside plus radiotherapy in 20 previously untreated SCLC patients |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical study | American Journal of Clinical Oncology | Continuous-infusion Ara-C alone showed no responses with severe toxicity in relapsed SCLC; Ara-C added to CAV in extensive-stage disease |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical study | American Journal of Clinical Oncology | Etoposide (VP-16) + infusional Ara-C in 17 patients with combination-refractory relapsed SCLC |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II trial (NSCLC) | Tumori | Cisplatin + vindesine + cytarabine in 32 advanced NSCLC patients; 18% response rate |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II trial (NSCLC) | Cancer | High-dose cytarabine (3 g/m²) + cisplatin in chemo-naive NSCLC; 14% response rate, but Grade IV myelosuppression in 32% of patients |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot study (NSCLC) | European Journal of Cancer & Clinical Oncology | Cisplatin + cytarabine combination pilot study in advanced NSCLC |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case series | American Journal of Medicine | Intensive chemotherapy (historically including cytarabine) for meningeal carcinomatosis in SCLC; 78% response rate |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case report | Gan to Kagaku Ryoho | Multidisciplinary treatment of meningeal carcinomatosis in a SCLC patient |
| [75105](https://pubmed.ncbi.nlm.nih.gov/75105/) | 1978 | Phase II trial (EORTC) | European Journal of Cancer | Phase II study of anhydro-ara-5-fluorocytidine (an Ara-C analog) across several tumor types including SCLC |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics and Chemotherapy | Review of Ara-C analogs (cyclocytidine, AAFC, N4-acyl derivatives) developed to overcome cytidine deaminase inactivation |

---

## Germany Market Information

Cytarabine currently has **no marketing authorization on file** in Germany (`total_licenses = 0`). No authorization number, product name, dosage form, or approved indication data is available for this dataset.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (pyrimidine antimetabolite / nucleoside analog) |
| Myelosuppression Risk | High — literature-documented Grade III/IV myelosuppression in up to 46% of patients with high-dose regimens (PMID 2156598) |
| Emetogenicity Classification | Moderate to High (dose-dependent; high-dose regimens are classified as highly emetogenic) |
| Monitoring Items | CBC with differential and platelets, liver and renal function, neurologic exam (cerebellar toxicity risk with high-dose therapy), ocular exam (conjunctivitis risk with high-dose therapy) |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. (Detailed German/EU label warnings, contraindications, and drug interaction data are not yet available for this candidate — see Data Gap DG001, flagged as Blocking for safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for cytarabine in small cell lung carcinoma is limited to historical (1980s) chemotherapy regimens that have since been superseded by platinum/etoposide as standard of care, no currently registered trial tests cytarabine specifically in SCLC, and a Blocking data gap (missing label warnings/contraindications) prevents this candidate from formally entering the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Resolve DG001: obtain German/EU-approved label safety data (warnings, contraindications) from BfArM
- Resolve DG002: obtain detailed mechanism of action data from DrugBank
- Identify whether any contemporary (post-2000) trials or real-world evidence support cytarabine's role in SCLC, given the field has moved to newer regimens
- Confirm route compatibility, since `route_compatibility.status` is currently unresolved for this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

