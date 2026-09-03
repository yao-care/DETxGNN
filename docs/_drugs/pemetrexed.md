---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Malignant Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

> Pemetrexed is a multitargeted antifolate chemotherapy agent whose established use — in combination with cisplatin — is the treatment of malignant pleural mesothelioma and non-squamous NSCLC.
> The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, a rarer mesothelial-lining cancer,
> with **10 clinical trials** and **10 curated publications** currently supporting this direction — though no dedicated Phase 3 RCT exists for this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant Pleural Mesothelioma (in combination with cisplatin) — pemetrexed's established, guideline-recognised standard-of-care indication |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data was not available in this evidence pack (DrugBank MOA field is a data gap). However, the underlying evidence base consistently describes pemetrexed as a multitargeted antifolate that inhibits **thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT)** — enzymes essential to folate-dependent DNA and RNA precursor synthesis. This cytotoxic mechanism is well validated in malignant pleural mesothelioma, where pemetrexed plus cisplatin became the standard first-line regimen following the pivotal Phase 3 trial (Vogelzang et al., 2003).

Malignant peritoneal mesothelioma and malignant pleural mesothelioma both arise from mesothelial cells — one lining the pleural cavity, the other the peritoneal cavity — and share overlapping histology, asbestos-related pathogenesis, and antifolate drug sensitivity. Because no dedicated, guideline-endorsed systemic regimen exists for the peritoneal subtype, oncologists have empirically extrapolated the pleural mesothelioma regimen (pemetrexed + cisplatin) to peritoneal disease.

This extrapolation is supported by real-world and retrospective clinical experience: Fujimoto et al. (2017) and Nagata et al. (2019) both report on first-line pemetrexed-cisplatin specifically in malignant peritoneal mesothelioma cohorts, and multiple case series (e.g., rechallenge with cisplatin-pemetrexed, Gilani et al. 2013) describe meaningful responses. This gives the TxGNN prediction plausible mechanistic and clinical-practice grounding, even though a confirmatory randomized trial specific to the peritoneal subtype is still lacking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial comparing carboplatin/pemetrexed/bevacizumab ± atezolizumab as neoadjuvant or palliative therapy for peritoneal mesothelioma |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized comparison of intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC in malignant peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed plus gemcitabine as front-line therapy for pleural or peritoneal mesothelioma; assessed safety, tumor response, and survival |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm study of sintilimab + bevacizumab combined with pemetrexed/cisplatin in unresectable malignant peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | Randomized trial of PIPAC + systemic chemotherapy (cisplatin/pemetrexed) vs. systemic chemotherapy alone as first-line treatment |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Three-cohort trial of maintenance talazoparib after first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | Methoxyamine (TRC102) + cisplatin/pemetrexed in solid tumors/mesothelioma refractory to pemetrexed-cisplatin or -carboplatin |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib mesylate in unresectable/metastatic malignant mesothelioma; determined maximum tolerated dose |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 + pemetrexed + cisplatin in arginine-dependent tumors, including an advanced peritoneal mesothelioma dose-escalation cohort |
| [NCT03564691](https://clinicaltrials.gov/study/NCT03564691) | Phase 1 | Completed | 470 | MK-4830 monotherapy/combination with pembrolizumab in a broad advanced solid tumor basket study, including mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Review of Anticancer Therapy | First-line pemetrexed + cisplatin efficacy specifically evaluated in malignant peritoneal mesothelioma (MPeM) patients |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Japanese Journal of Clinical Oncology | Efficacy and safety of pemetrexed + cisplatin as first-line therapy in advanced MPeM; efficacy previously unclear, now characterized |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospective study | Clinical Medicine Insights: Oncology | Comparison of first-line pemetrexed-platinum vs. gemcitabine-platinum regimens in MPeM |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective study | BMC Cancer | Efficacy of second-line treatment and prognostic factors in advanced MPeM following first-line pemetrexed-based therapy |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center cohort | Annals of Surgical Oncology | Treatment strategies and outcomes across a multi-center MPeM cohort |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | MPeM patient responding to rechallenge with cisplatin + pemetrexed, with literature review |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and Peritoneum | Bidirectional chemotherapy (including pemetrexed-based regimens) enabling surgery + HIPEC for initially unresectable MPeM |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | Journal of Clinical Medicine | Comprehensive review of treatment approaches for malignant peritoneal mesothelioma |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | Journal of Gastrointestinal Oncology | Diagnosis and management of MPeM, including systemic chemotherapy options |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Translational Lung Cancer Research | General review of malignant peritoneal mesothelioma biology and treatment |

---

## Cytotoxicity

Pemetrexed is a conventional cytotoxic antineoplastic agent (antifolate/antimetabolite class), which triggers this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate/antimetabolite) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anemia are well-documented, particularly when combined with platinum agents (e.g., cisplatin) |
| Emetogenicity Classification | Moderate as monotherapy; High when combined with cisplatin |
| Monitoring Items | CBC with differential before each cycle, renal function (creatinine clearance), liver function tests; folic acid and vitamin B12 supplementation is required to reduce toxicity |
| Handling Protection | Must be handled under standard cytotoxic/hazardous drug handling protocols (closed-system transfer, PPE, controlled disposal) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Peritoneal mesothelioma shares mechanistic and histologic biology with pemetrexed's core approved indication (pleural mesothelioma), and multiple retrospective/cohort studies plus several active Phase 2 trials support pemetrexed-cisplatin activity in this subtype. However, no dedicated Phase 3 RCT has confirmed efficacy specifically in peritoneal disease, and the drug currently holds no market authorization in this jurisdiction (0 licenses, not marketed).

**To proceed, the following is needed:**
- Official product label warnings and contraindications (currently a blocking data gap — required before S1 safety screening can be completed)
- Structured DrugBank mechanism-of-action data to formally document the target pathway rationale
- Confirmation of local market authorization pathway, given current "not marketed" status with zero licenses
- A dedicated prospective/randomized trial (or mature real-world outcomes data) specific to malignant peritoneal mesothelioma to upgrade evidence beyond L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

