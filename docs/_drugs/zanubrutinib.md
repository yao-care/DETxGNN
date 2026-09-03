---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Zanubrutinib: From B-Cell Malignancies to Myeloid Leukemia

## One-Sentence Summary

> Zanubrutinib is a Bruton tyrosine kinase (BTK) inhibitor whose established evidence base (per the literature in this pack) centers on B-cell malignancies such as CLL/SLL and Waldenström macroglobulinemia.
> The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with a prediction score of **99.65%**,
> but **none of the cited clinical trials or publications directly study zanubrutinib in myeloid leukemia** — the trials involve different investigational drugs, and the literature supports only its known lymphoid-malignancy indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this pack (no BfArM license data; literature indicates zanubrutinib is an established BTK-inhibitor therapy for CLL/SLL and other B-cell malignancies) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 (model prediction only — cited trials involve unrelated drugs; cited literature does not address myeloid leukemia) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable (blocking data gap, DG002). Based on the information available in this evidence pack, zanubrutinib is a next-generation, highly selective BTK inhibitor that blocks B-cell receptor signaling — a pathway central to B-cell malignancies. Its clinical evidence (SEQUOIA, ALPINE and related studies) is concentrated almost entirely in CLL/SLL and Waldenström macroglobulinemia.

Myeloid leukemia arises from a different hematopoietic lineage than CLL/SLL, and BTK is not established as a key driver in myeloid malignancies the way it is in B-cell lymphoid disease. The two clinical trials retrieved under this predicted indication (NCT04477291, NCT05665530) do not actually test zanubrutinib for myeloid leukemia — they involve different investigational agents (luxeptinib/CG-806 and PRT2527) that happen to co-occur in the same trial registry search, or use zanubrutinib only as a combination comparator in unrelated hematologic malignancies. Taken together, this prediction most likely reflects an over-generalization of the TxGNN embedding for the broad "leukemia" disease category, rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Terminated | 45 | Tests **luxeptinib (CG-806)**, not zanubrutinib, in relapsed/refractory AML/MDS; trial terminated — not usable as supporting evidence |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Tests **PRT2527 (CDK9 inhibitor)** monotherapy and in combination with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies; zanubrutinib is a combination arm comparator, not the study drug for myeloid leukemia specifically |

**Note:** Neither trial provides direct evidence for zanubrutinib monotherapy efficacy in myeloid leukemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 5-year follow-up: zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Zanubrutinib well tolerated/effective in CLL/SLL patients intolerant of ibrutinib/acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Review | Blood Advances | Pooled analysis of zanubrutinib in del(17p)/TP53-mutated CLL/SLL across SEQUOIA and ALPINE |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study of zanubrutinib in BTK-inhibitor-intolerant B-cell malignancies |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | TKI-era review of CML and CLL, general context on tyrosine kinase pathways |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK inhibitors, including zanubrutinib, in Waldenström macroglobulinemia |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case Report | Front Immunol | Case report of coexisting WM and B-ALL, unrelated to zanubrutinib treatment outcomes |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | HBV reactivation risk in patients receiving BTK inhibitors, including zanubrutinib |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | General synthetic-chemistry review of FDA-approved anticancer drugs (2018–2021), not disease-specific |

**Important:** None of the above publications specifically study zanubrutinib in myeloid leukemia. They represent the drug's established evidence base for B-cell malignancies (CLL/SLL, Waldenström) plus general safety/chemistry reviews. **No direct literature evidence for the predicted myeloid leukemia indication was found.**

---

## Germany Market Information

Zanubrutinib is currently **not marketed in Germany** (0 BfArM authorizations on record in this pack).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor; oral small-molecule kinase inhibitor, not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no quantitative toxicity data in this pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; hepatitis B serology/viral load — HBV reactivation has been reported with BTK inhibitors including zanubrutinib (PMID [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/)) |
| Handling Protection | Please refer to the package insert and institutional hazardous drug handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this pack — DG001, blocking).

**Signal from literature (not formal safety labeling):** BTK inhibitors as a class, including zanubrutinib, have been associated with hepatitis B virus reactivation (PMID [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/)); HBV screening should be considered before initiating therapy pending confirmation from official labeling.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is not substantive — the two retrieved clinical trials involve different investigational drugs, and all retrieved literature supports zanubrutinib's *established* B-cell malignancy indications rather than myeloid leukemia. Combined with a blocking data gap on approved-label warnings/contraindications (DG001) and the fact that the drug is not currently marketed in Germany, this candidate cannot advance past S0.

**To proceed, the following is needed:**
- Resolve DG001: BfArM/manufacturer label warnings and contraindications, required before any S1 safety screening
- Resolve DG002: Confirmed mechanism-of-action data from DrugBank
- Any dedicated preclinical, mechanistic, or clinical evidence linking BTK signaling to myeloid leukemia pathogenesis (currently absent)
- Correction of the clinical-trial matching pipeline, since both retrieved trials are drug-mismatched and should not have been attributed to this candidate

**Additional note:** Ranks 2–6 (vertebral anomalies syndrome, ganglioneuroblastoma, retroperitoneal neoplasm, Ewing sarcoma, neuroblastoma) are all Evidence Level L5 with zero or near-zero supporting trials/literature and no plausible mechanistic link to BTK inhibition. These should be deprioritized unless new external evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

