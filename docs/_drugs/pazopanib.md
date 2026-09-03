---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma / Soft Tissue Sarcoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

> Pazopanib is a multi-target tyrosine kinase inhibitor whose established use — as documented in the retrieved literature — is advanced/metastatic clear-cell renal cell carcinoma (ccRCC) and non-adipocytic soft tissue sarcoma.
> The TxGNN model predicts it may also be effective for **Unclassified Renal Cell Carcinoma**,
> with **1 completed Phase 3 clinical trial** and **6 publications** currently supporting this direction.
> Note: the drug is not currently marketed in Germany, and TFDA-level warning/contraindication data is a **blocking** gap for safety pre-assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in the evidence pack (`taiwan_regulatory.licenses` and `drug.original_indications` are both empty). Based on retrieved literature within this pack, pazopanib is a registered/standard therapy for advanced/metastatic clear-cell RCC and non-adipocytic soft tissue sarcoma. |
| Predicted New Indication | Unclassified Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L2 (1 completed Phase 3 trial + multiple retrospective/real-world cohorts) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the retrieved literature itself, pazopanib is a multi-target tyrosine kinase inhibitor with anti-angiogenic activity; multiple abstracts in the evidence pack describe it as a "standard first-line treatment for metastatic clear-cell renal cell carcinoma (ccRCC)" (PMID 28108284) and note it is "registered" for advanced RCC (NCT01613846 summary).

Unclassified RCC is a rare, non-clear-cell histologic subtype within the same organ/tumor family as pazopanib's established indication. Because treatment approaches for non-clear-cell RCC (nccRCC) are "frequently extrapolated from data of clear cell renal cell carcinoma" (PMID 31921344), and pazopanib's anti-angiogenic mechanism is not histology-restricted, the mechanistic rationale for extending use into unclassified/non-clear-cell RCC is plausible and is echoed across several retrospective cohorts (PANORAMA study, PMID 28108284; MD Anderson cohort, PMID 27568124; IMDC consortium analysis, PMID 41558869).

However, "unclassified RCC" is a distinct and rarer diagnostic category than the nccRCC populations actually studied in these papers, and no trial or publication in this pack specifically isolates the "unclassified" subtype. This introduces residual uncertainty about direct applicability.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Completed | 544 | Randomized sequential trial evaluating sorafenib→pazopanib vs. pazopanib→sorafenib in advanced/metastatic RCC; both agents were registered/effective in RCC but no prior comparative sequencing data existed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase II, single-arm | Cancer Research and Treatment | Prospective phase II study assessing efficacy/safety of pazopanib specifically in non-clear-cell RCC (nccRCC). |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world/Retrospective | Ecancermedicalscience | Compares first-line sunitinib vs. pazopanib in non-clear-cell and sarcomatoid histology mRCC; asks whether the two are interchangeable. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective multicenter | Clinical Genitourinary Cancer | Italian PANORAMA study: retrospective efficacy/toxicity analysis of first-line pazopanib in nccRCC. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clinical Genitourinary Cancer | Outcomes of metastatic non-clear-cell RCC patients treated with pazopanib. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospective/Case series | Clinical Genitourinary Cancer | Histologic/immunohistochemical characterization and targeted-therapy outcomes in carcinoma-of-unknown-primary presenting with mRCC features (CUP-mRCC). |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospective database cohort | European Urology Oncology | IMDC consortium analysis comparing contemporary vs. traditional first-line therapies across nccRCC histologic subtypes, including unclassified RCC. |

---

## Germany Market Information

Pazopanib currently holds no marketing authorization in Germany (market status: Not marketed; 0 authorizations on file).

---

## Cytotoxicity

Pazopanib's established indications (renal cell carcinoma, soft tissue sarcoma) are antineoplastic, and it is a multi-target tyrosine kinase inhibitor — classifying it under this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor; anti-angiogenic, VEGFR/PDGFR/c-KIT-directed) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not specifically documented in this evidence pack; TKIs of this class are generally associated with lower myelosuppression risk than conventional cytotoxics — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI query all returned no data — DDI query status: `not_found`.)

**Note:** This is flagged in the evidence pack as a **Blocking** data gap (DG001 — TFDA warning/contraindication labeling not yet retrieved), meaning this candidate cannot yet pass S1 safety pre-assessment.

---

## Other Predicted Indications (Summary)

For context, the same evidence pack scored 9 additional candidate indications for pazopanib. Most have weak or no direct evidence and are held; two related sarcoma indications show notably stronger, disease-specific support:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 2 | Renal cell carcinoma (Xp11.2/TFE3 fusion) | 99.63% | L5 | Hold — no trial/literature support |
| 3 | Renal cell carcinoma with neuroblastoma | 99.63% | L5 | Hold — no trial/literature support |
| 4 | Liposarcoma | 99.59% | L2 | **Proceed with Guardrails** — 2 disease-specific Phase II trials (NCT01506596, NCT01692496) + randomized Phase II combo trial (NCT01532687); PDGFRA-amplification mechanistic rationale |
| 5 | Childhood kidney cell carcinoma | 99.54% | L4 | Hold — only trial listed is an adult mRCC study, likely ontology mismatch; no pediatric PK/safety data |
| 6 | Ovarian myxoid liposarcoma | 99.51% | L5 | Hold — no trial/literature support |
| 7 | Heart fibrosarcoma | 99.37% | L4 | Hold — only broad STS trials, no cardiac-specific data; cardiotoxicity risk needs evaluation |
| 8 | Fibroblastic neoplasm | 99.35% | L3 (est.) | Hold — rich literature on desmoid tumor/solitary fibrous tumor subtypes (incl. single-arm Phase II, PMID 30578023) but "fibroblastic neoplasm" as a category is too broad/heterogeneous for a single recommendation |
| 9 | Kidney fibrosarcoma | 99.33% | L5 | Hold — no trial/literature support |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | L2 (est.) | Proceed with Guardrails (cautious) — disease-specific Phase II trial (NCT01059656, terminated) + multicenter Phase II publication (PMID 32956651); strong mechanistic rationale via COL1A1-PDGFB fusion |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for the top prediction (unclassified RCC) is moderate (L2) and mechanistically plausible, and two other candidates (liposarcoma, dermatofibrosarcoma protuberans) show even stronger disease-specific trial evidence. However, this candidate cannot advance because (1) TFDA-level warnings/contraindications are a **Blocking** data gap that prevents safety pre-assessment (S1), and (2) the drug currently has zero marketing authorizations in Germany, so regulatory pathway and local labeling are undefined.

**To proceed, the following is needed:**
- Retrieve TFDA/BfArM package insert (warnings, contraindications, DDI) to resolve DG001 before any safety pre-assessment
- Obtain formal DrugBank/MOA data to resolve DG002 and support mechanistic-link scoring
- Confirm regulatory pathway given 0 current marketing authorizations in Germany
- If pursuing liposarcoma or dermatofibrosarcoma protuberans in parallel, prioritize these given stronger disease-specific Phase II evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

