---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: From Glioblastoma/Anaplastic Astrocytoma to Adult Astrocytic Tumour

## One-Sentence Summary

> Temozolomide is an oral alkylating agent whose established therapeutic role is glioblastoma and anaplastic astrocytoma, delivered as concomitant and adjuvant chemotherapy with radiotherapy (the Stupp protocol).
> The TxGNN model's top prediction — **Adult Astrocytic Tumour** — largely restates this already-established standard of care rather than pointing to a genuinely new indication.
> The evidence base is unusually strong for a "prediction": **2 clinical trials** (including a Phase 3 RCT with 500 patients) and **20 publications**, several of them practice-defining RCTs (NEJM, Lancet, JAMA).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the regulatory data provided (licenses list is empty). Per the literature and repurposing rationale in this pack, temozolomide's established indication is glioblastoma / anaplastic astrocytoma. |
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug (data gap DG002). However, the evidence pack's repurposing rationale describes temozolomide as an oral alkylating agent that crosses the blood–brain barrier and is converted to MTIC, which methylates DNA at the O6 position of guanine. This DNA damage triggers apoptosis and is particularly cytotoxic to rapidly proliferating glial tumour cells — the mechanistic basis for its activity in CNS malignancies.

Importantly, "adult astrocytic tumour" is not a distant or unexpected new indication for temozolomide — it sits within the drug's known therapeutic category (glioblastoma/anaplastic astrocytoma). The evidence pack itself flags this as "not a typical repurposing case, but rather an extension of existing clinical standard-of-care evidence (Stupp protocol)." In other words, TxGNN's top-ranked prediction here largely reconstructs a well-established indication rather than surfacing a novel therapeutic hypothesis. This should be factored into how the prediction is used: it is strong validation of the model's ability to recover known drug–disease links, but it should not be marketed internally as a "new" discovery.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | RCT comparing temozolomide vs. PCV (procarbazine, lomustine, vincristine) in recurrent WHO grade III/IV astrocytic tumours; directly supports temozolomide's efficacy in this population. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) combined with temozolomide + radiotherapy in newly diagnosed glioblastoma; provides combination safety/PK data rather than temozolomide monotherapy evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark EORTC-NCIC trial establishing concomitant + adjuvant temozolomide plus radiotherapy as the new standard of care for newly diagnosed glioblastoma. |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | 5-year follow-up of the EORTC-NCIC trial confirming durable survival benefit of temozolomide + radiotherapy over radiotherapy alone. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 Phase 3 trial: temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | RCT adding bevacizumab to standard temozolomide + radiotherapy in newly diagnosed glioblastoma; confirms temozolomide + radiotherapy as the standard-of-care backbone. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | EF-14 trial: Tumor Treating Fields plus maintenance temozolomide vs. temozolomide alone, showing significantly improved overall survival with the combination. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3 trial: lomustine-temozolomide combination superior to temozolomide monotherapy in MGMT-methylated newly diagnosed glioblastoma. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG Oncology BN007 Phase II/III trial of dual immune checkpoint blockade in MGMT-unmethylated glioblastoma, with temozolomide-based standard therapy as background/comparator. |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Review | J Neurooncol | Exploratory cohort analysis of radiotherapy plus temozolomide in anaplastic astrocytic gliomas. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of glioblastoma and other primary adult brain malignancies, including temozolomide-based standard of care. |
| [39516198](https://pubmed.ncbi.nlm.nih.gov/39516198/) | 2024 | Review | Nat Commun | Methodological review of regulatory programs underlying neural cancer plasticity; tangential relevance to temozolomide's clinical indication. |

---

## Cytotoxicity

Temozolomide is a conventional cytotoxic chemotherapeutic agent (alkylating agent, imidazotetrazine class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (TFDA label data currently unavailable — see DG001) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting temozolomide in adult astrocytic tumour is exceptionally strong (L1: multiple Phase 3 RCTs including landmark NEJM/Lancet/JAMA trials), but this largely confirms an already-established standard-of-care indication rather than a novel repurposing signal — it should be framed internally as validation, not discovery. Regulatory and safety data are currently missing, which blocks a full risk assessment.

**To proceed, the following is needed:**
- TFDA/BfArM package insert with warnings, contraindications, and drug interaction data (DG001, blocking)
- Structured mechanism-of-action record from DrugBank (DG002)
- Confirmation of Taiwan/Germany marketing and licensing status before positioning this as an actionable repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

