---
layout: default
title: Eribulin
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From Soft Tissue Sarcoma/Liposarcoma to Fibroblastic Neoplasm (Solitary Fibrous Tumor / Fibrosarcoma Spectrum)

## One-Sentence Summary

Eribulin is a microtubule-dynamics inhibitor already used against soft tissue sarcoma, including liposarcoma. Among 10 TxGNN-predicted indications, the strongest evidence-backed signal points to **Fibroblastic Neoplasm** (covering solitary fibrous tumor and fibrosarcoma/myxofibrosarcoma), supported by **1 completed Phase II trial** and **8 publications** — the only candidate in this set with real-world corroboration; the other 9 predictions remain model-prediction-only (L5), with several explicitly flagged in the source rationale as likely graph-linkage noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Germany licensing data (drug unmarketed); evidence-pack rationale confirms eribulin already has an approved indication in soft tissue sarcoma / liposarcoma via microtubule-dynamics inhibition |
| Predicted New Indication | Fibroblastic Neoplasm (Solitary Fibrous Tumor / Fibrosarcoma spectrum) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L3 (1 completed, non-randomized Phase II trial + multiple preclinical studies) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data (DrugBank field) is currently a data gap. However, the repurposing rationale embedded across multiple predicted indications in this evidence pack consistently describes eribulin as a **microtubule-dynamics inhibitor / anti-mitotic agent**, with efficacy already established in soft tissue sarcoma, including an approved liposarcoma indication (noted explicitly for the myxoid liposarcoma prediction, rank 5).

Fibroblastic neoplasms — solitary fibrous tumor (SFT), fibrosarcoma, and myxofibrosarcoma — belong to the same broad soft-tissue sarcoma family as liposarcoma. They share highly proliferative, mesenchymal-origin biology that is mechanistically dependent on microtubule function, making them a biologically plausible extension of eribulin's known antitumor activity rather than an unrelated disease area.

This mechanistic plausibility is reinforced by actual data: a completed Phase II trial (ERASING, NCT03840772) specifically tested eribulin in advanced SFT, and multiple independent preclinical studies (2021–2025) demonstrate eribulin activity — including synergy with recombinant methioninase — in fibrosarcoma and myxofibrosarcoma cell lines and patient-derived xenografts. This combination of a completed clinical trial plus a consistent, growing preclinical literature is unique among the 10 candidates in this pack; nine other predictions (e.g., familial Mediterranean fever, mesothelioma subtypes, adenomatoid tumor) have zero supporting trials or literature and are explicitly annotated in the source rationale as low mechanistic plausibility or likely TxGNN graph noise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | Italian Sarcoma Group study (ERASING) evaluating eribulin in advanced Solitary Fibrous Tumor |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | Diagnostics and treatment landscape of extrameningeal SFT; discusses chemotherapy including microtubule-targeting agents |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical (PDX) | Eur J Cancer | Patient-derived SFT xenografts predict sensitivity to doxorubicin/dacarbazine, and highlight eribulin/trabectedin as potentially effective |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical (in vitro) | Anticancer Research | Recombinant methioninase synergizes with eribulin against fibrosarcoma cells but spares normal fibroblasts |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical (in vitro) | Anticancer Research | Recombinant methioninase increases eribulin efficacy 16-fold in eribulin-resistant HT1080 fibrosarcoma cells |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical (in vivo) | In Vivo | Super-eribulin-resistant fibrosarcoma cells become more malignant but are synergistically controlled by eribulin + methionine restriction in mice |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Preclinical (cell line) | Human Cell | Establishment of novel myxofibrosarcoma cell line (SMU-MFS) for future drug testing, including microtubule-targeting agents |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Preclinical (cell line) | Human Cell | Establishment of patient-derived myxofibrosarcoma cell line (NCC-MFS4-C1) as a model for treatment development |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Case report | Genes Chromosomes Cancer | Response to entrectinib (not eribulin) in NTRK-fusion malignant peripheral nerve sheath tumor; included via disease-class linkage, not eribulin-specific — weak relevance |

---

## Germany Market Information

Eribulin currently holds **no marketing authorization in Germany** (0 licenses on file); no product/dosage-form data is available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule-dynamics inhibitor / anti-mitotic agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data in this dataset) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Antineoplastic agent — cytotoxic drug handling precautions apply per institutional protocol |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack (flagged as a Blocking data gap pending TFDA label acquisition).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fibroblastic neoplasm is the only one of 10 TxGNN-predicted indications backed by a completed clinical trial and a consistent body of preclinical literature; however, the trial is small (n=16), non-randomized, and no comparator or survival endpoints are reported in this pack, so evidence remains preliminary (L3).

**To proceed, the following is needed:**
- TFDA/German label data (warnings, contraindications) — currently a Blocking data gap preventing full S1 safety review
- Structured MOA data from DrugBank to formally confirm the microtubule-inhibition mechanism
- Efficacy/safety results (not just trial registration) from NCT03840772
- A larger, ideally randomized trial in SFT/fibrosarcoma to move beyond L3
- DDI and contraindication profile before advancing past current review stage
- Regulatory/access pathway assessment given eribulin is not currently marketed in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

