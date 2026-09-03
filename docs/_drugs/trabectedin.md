---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 1
---

# Trabectedin
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

# Trabectedin: From Soft Tissue Sarcoma / Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin (DrugBank DB05109) is a marine-derived DNA-binding cytotoxic agent internationally approved for soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin, for platinum-sensitive recurrent ovarian cancer.
> The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**,
> with **2 clinical trials** and **20 publications** currently supporting this direction — though the drug is not yet marketed in this jurisdiction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not locally licensed; internationally approved for soft tissue sarcoma and platinum-sensitive recurrent ovarian cancer (per literature) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available for this drug directly (DrugBank MOA field: data gap). Based on the mechanistic evidence compiled from the literature pack, trabectedin is a marine-derived, alkylating-type DNA minor-groove binding agent that interferes with transcription-coupled nucleotide excision repair (TC-NER) and modulates the tumor microenvironment by depleting tumor-associated monocytes/macrophages. This mechanism offers a theoretical synthetic-lethality rationale in BRCA1/2-deficient (homologous recombination-deficient) breast cancers, and in vitro studies show it can induce apoptosis in both HER2+/ER- and HER2-/ER+ breast cancer cell lines, with additional evidence of synergy with IL-12-mediated immune activation in triple-negative breast cancer (TNBC).

Breast cancer is not currently a primary approved indication for trabectedin — its established uses are soft tissue sarcoma and platinum-sensitive ovarian cancer, both of which share a DNA-repair-deficiency-driven treatment rationale with a subset of BRCA1/2-mutated breast cancers. The mechanistic link to breast cancer is therefore a reasonable extrapolation supported by preclinical and early-phase clinical signal, rather than a directly validated indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled, sequential-design QT/QTc interval study of single-dose trabectedin in advanced solid tumor malignancies; directly evaluates trabectedin cardiac safety at therapeutic dose (Relevance grade A). |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after response to trabectedin + pegylated liposomal doxorubicin (PLD) induction in recurrent BRCA-mutated ovarian carcinoma; trabectedin-PLD serves as induction regimen, not the primary study arm (small n=9, Relevance grade B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | RCT | Clinical Breast Cancer | Multicenter, randomized Phase 2 study of single-agent trabectedin (2 dosing regimens) in advanced breast cancer after prior anthracycline and taxane treatment. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | RCT | Clinical Breast Cancer | Phase 2 study of trabectedin in HR+/HER2- advanced breast cancer, efficacy assessed by tumor XPG mRNA expression as predictive biomarker. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 Trial | Annals of Oncology | International first-in-class Phase 2 trial showing trabectedin activity in germline BRCA1/2-mutated metastatic breast cancer. |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 Trial | European Journal of Cancer | Phase I/PK study of trabectedin + doxorubicin combination in advanced soft tissue sarcoma and breast cancer, feasibility and antitumor activity assessed. |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews trabectedin's mechanism (transcription regulation, TAM reduction) and its investigational potential in breast cancer. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | Reviews trabectedin as a chemotherapy option in patients with BRCA deficiency, including breast cancer. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Trabectedin depletes immunosuppressive myeloid cells and enhances IL-12-driven NK-cell cytotoxicity in triple-negative breast cancer models. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Trabectedin induces apoptosis via death-receptor pathway in MCF-7 (HER2-/ER+) and MDA-MB-453 (HER2+/ER-) breast cancer cell lines. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical | European Cytokine Network | Demonstrates anti-angiogenic effects of trabectedin on HUVECs and breast cancer cell lines via angiogenic cytokine modulation. |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Review | Seminars in Oncology | Reviews emerging agents, including trabectedin, for anthracycline- and taxane-refractory metastatic breast cancer. |

---

## Germany Market Information

Trabectedin currently has no marketing authorization record in this jurisdiction (0 licenses on file); market status is **Not Marketed**.

---

## Cytotoxicity

Trabectedin is a conventional cytotoxic chemotherapeutic agent (marine-derived, DNA minor-groove-binding alkylating-type agent), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — DNA minor-groove binder / transcription-coupled repair inhibitor (marine-derived alkylating-type agent) |
| Myelosuppression Risk | High — literature reports grade 3–4 neutropenia in ~50% and grade 3–4 thrombocytopenia in ~20% of patients (Boudou et al., 2009) |
| Emetogenicity Classification | Moderate (based on known clinical profile; specific formal classification not provided in this evidence pack) |
| Monitoring Items | CBC with differential, liver function tests (hepatotoxicity reported), creatine kinase (rhabdomyolysis risk), renal function, and cardiac monitoring (QT/QTc, per NCT00786838) |
| Handling Protection | Requires handling per standard cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug is not currently marketed/licensed in this jurisdiction, and package-insert-level safety data (warnings, contraindications) is a **blocking data gap (DG001)**, preventing a full S1 safety pre-assessment. While evidence level L2 (one supportive comparative QT-safety trial plus multiple early-phase/preclinical breast cancer studies) is mechanistically plausible and biomarker-directed (BRCA1/2, XPG), it is not yet strong enough on its own to justify progression without safety substantiation.

**To proceed, the following is needed:**
- Local safety labeling data (TFDA/BfArM package insert: warnings, contraindications, DDI) to close DG001
- Confirmed structured MOA documentation from DrugBank to close DG002 (partially supported by literature mechanistic rationale above)
- Additional larger Phase 2/3 breast-cancer-specific RCT data (current dedicated breast cancer trials are small/early-phase)
- Formal drug-drug interaction (DDI) profile, currently returns no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

