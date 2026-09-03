---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: From Chronic Myeloid Leukaemia/GIST to Fibroblastic Neoplasm (Dermatofibrosarcoma Protuberans)

## One-Sentence Summary

Imatinib is a BCR-ABL/KIT/PDGFR tyrosine kinase inhibitor historically developed for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST); detailed original indication text and MOA documentation are not present in this evidence pack (see Data Gaps DG001/DG002). Among 10 TxGNN-predicted indications screened for this drug, **Fibroblastic Neoplasm** — which the evidence maps clinically to **Dermatofibrosarcoma Protuberans (DFSP)** — has by far the strongest support, with **1 completed Phase 2 trial** and **20 related publications**, including a 2025 European interdisciplinary treatment guideline. Note that the single highest TxGNN score in this pack ("heart fibrosarcoma") has almost no corroborating evidence and is flagged Hold; it is discussed separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (drug.original_indications is empty; regulatory license text unavailable — DG001) |
| Predicted New Indication | Fibroblastic Neoplasm (clinically corresponds to Dermatofibrosarcoma Protuberans, DFSP) |
| TxGNN Prediction Score | 99.94% (rank 1108 among all TxGNN candidate diseases; rank 2 of 10 in this evidence pack) |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for imatinib in this evidence pack (Data Gap DG002). Based on generally known pharmacology, imatinib is a small-molecule inhibitor of BCR-ABL, KIT and PDGFR tyrosine kinases, and its efficacy in CML and GIST is well established.

For the "Fibroblastic Neoplasm" prediction, the evidence pack's own mechanistic rationale is clear and specific: this disease category corresponds substantially to **DFSP**, which carries a characteristic **t(17;22)(q22;q13) COL1A1–PDGFB translocation** leading to constitutive PDGFRB activation. This is a textbook molecular target for imatinib, and the mechanism-to-indication link is direct rather than inferred — DFSP with fibrosarcomatous transformation has in fact already been treated with imatinib in real-world oncology practice.

By contrast, the top-scored candidate by raw TxGNN score alone, "heart fibrosarcoma," has only a single 2008 drug-bulletin commentary as support, whose title explicitly states the evidence is "not robust." This illustrates why TxGNN score rank and evidence strength must be evaluated separately — see the full candidate screening table at the end of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Completed | 17 | Imatinib in locally advanced/metastatic DFSP and giant cell fibroblastoma harboring the COL1A1/PDGFB fusion; trial directly enrolled molecularly-confirmed patients (Evidence Grade A). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Review/Guideline | Eur J Cancer | European interdisciplinary (EADO/EDF/UEMS/EADV) updated guideline on DFSP diagnosis and treatment. |
| [41236573](https://pubmed.ncbi.nlm.nih.gov/41236573/) | 2025 | Preclinical | Human Cell | Establishment of an imatinib-resistant DFSP cell line (DFSP-DPH1) for resistance research. |
| [37610680](https://pubmed.ncbi.nlm.nih.gov/37610680/) | 2023 | Preclinical | Human Cell | Multi-omic profiling and ex vivo modeling of imatinib-resistant DFSP with fibrosarcomatous transformation. |
| [36630365](https://pubmed.ncbi.nlm.nih.gov/36630365/) | 2023 | Review | Clin Exp Dermatol | Overview of DFSP clinical features, histology, and PDGFB-COL1A1 fusion (>90% of cases). |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Review | J Surg Oncol | Surgical management of DFSP; notes imatinib use in advanced/unresectable disease. |
| [33993132](https://pubmed.ncbi.nlm.nih.gov/33993132/) | 2021 | Review | Curr Opin Otolaryngol Head Neck Surg | Diagnosis, workup, and treatment strategies for DFSP. |
| [30297237](https://pubmed.ncbi.nlm.nih.gov/30297237/) | 2018 | Review | Bull Cancer | DFSP management; identifies t(17;22)(q22;q13) COL1A1/PDGFB as specific diagnostic marker. |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Review | Dermatol Clin | DFSP clinical/histologic characterization; radiation and systemic therapy in unresectable cases. |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Review | Curr Treat Options Oncol | Multidisciplinary treatment approach to DFSP. |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Review | Expert Rev Anticancer Ther | Current treatment options for DFSP; PDGF autocrine/paracrine mechanism. |

---

## Germany Market Information

Imatinib is currently **not marketed** in this jurisdiction (`market_status: 未上市`), and no product authorization records are present in this evidence pack (`total_licenses: 0`). Regulatory approval and product listing data will need to be sourced separately if repurposing is pursued.

---

## Cytotoxicity

Imatinib's original indications (CML, Ph+ ALL, GIST) place it within the antineoplastic drug category, though it acts as a targeted therapy rather than a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BCR-ABL/KIT/PDGFR tyrosine kinase inhibitor) — based on known drug class; not derived from evidence-pack toxicity data |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug–drug interaction data were available in this evidence pack (flagged as Data Gap DG001, severity: Blocking, currently preventing S1 safety evaluation).

---

## Full Screening Summary of All Predicted Indications

For completeness, all 10 TxGNN candidates in this evidence pack are ranked below by evidence quality rather than raw score, since the two frequently diverge:

| Rank (by score) | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|---|---|---|---|---|---|---|
| 2 | Fibroblastic Neoplasm (≈DFSP) | 99.94% | L2 | S3 | Proceed with Guardrails | Strongest signal; PDGFB fusion, direct Phase 2 trial |
| 3 | Conventional Fibrosarcoma | 99.93% | L2 | S2 | Proceed with Guardrails | Evidence largely overlaps with DFSP; true "conventional" fibrosarcoma lacks PDGFR/KIT driver data — needs molecular subtyping before use |
| 6 | Liposarcoma | 99.88% | L2 | S2 | Research Question | Mixed Phase 2 evidence; unselected populations show limited response; needs PDGFR/KIT-enriched subgroup |
| 1 | Heart Fibrosarcoma | 99.94% | L4 | S0 | Hold | Highest raw score but only 1 non-robust 2008 commentary |
| 4 | Kidney Fibrosarcoma | 99.93% | L4 | S1 | Research Question | Basket trial only; literature match appears to be a keyword mismatch (FSGS, unrelated renal disease) |
| 5 | Low Grade Fibromyxoid Sarcoma | 99.93% | L5 | S0 | Hold | Wrong driver gene (FUS-CREB3L2); literature is an unrelated case series |
| 7 | Liver Fibrosarcoma | 99.86% | L5 | S0 | Hold | No trials or literature at all |
| 8 | Familial Mediterranean Fever | 99.86% | L5 | S0 | Hold | No plausible mechanistic link; likely knowledge-graph false positive |
| 9 | Ovarian Myxoid Liposarcoma | 99.85% | L5 | S0 | Hold | No supporting data |
| 10 | Familial Rhabdoid Tumor | 99.83% | L5 | S0 | Hold | Driven by SMARCB1 loss, unrelated to kinase inhibition |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The single well-supported signal in this evidence pack is Fibroblastic Neoplasm/DFSP, backed by a completed Phase 2 trial with a molecularly-defined population (COL1A1-PDGFB fusion) and a 2025 clinical guideline. All other 9 candidates are either weakly supported (L4) or effectively unsupported model artifacts (L5) and should be held pending stronger evidence.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a **Blocking** gap (DG001) preventing initial safety screening (S1)
- Formal MOA documentation from DrugBank (DG002)
- Molecular confirmation protocol (COL1A1-PDGFB testing) to define the target subpopulation for Fibroblastic Neoplasm/Conventional Fibrosarcoma indications
- For Liposarcoma: PDGFR/KIT expression-based patient enrichment strategy before further evaluation
- Regulatory pathway assessment, since the drug is not currently marketed in this jurisdiction (0 authorizations)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

