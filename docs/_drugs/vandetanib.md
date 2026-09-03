---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor (VEGFR2/VEGFR3/EGFR/RET) originally developed and approved (EU/US) for advanced medullary thyroid cancer. TxGNN predicts it may also be effective for **renal cell carcinoma**, particularly VHL-associated and clear cell subtypes, with **4 clinical trials** and **6 publications** currently supporting this direction — though key safety documentation is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the structured regulatory field (drug not marketed in Germany, 0 authorizations); literature in this evidence pack confirms vandetanib's approved use is **medullary thyroid cancer (MTC)**, driven by RET kinase inhibition |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data (`original_moa`) is flagged as a data gap. However, the literature evidence in this pack consistently describes vandetanib as an orally bioavailable multi-kinase inhibitor targeting **VEGFR2, VEGFR3, EGFR, and RET** (e.g. PMID 24451769, 28477875, 30860683). Its approved indication — medullary thyroid cancer — is driven by constitutively activated RET signalling, and its EU authorization (Caprelsa, AstraZeneca) for this setting is explicitly referenced in PMID 23185843 and PMID 32691271.

Renal cell carcinoma, particularly the clear cell and VHL-associated subtypes, is a classically angiogenesis-driven tumour: loss of VHL function stabilizes HIF and drives VEGF pathway activation. This is mechanistically the same pathway already targeted by several approved RCC therapies (sunitinib, pazopanib, axitinib), all of which are VEGFR-TKIs. Vandetanib's VEGFR2/VEGFR3-inhibitory activity therefore has a plausible mechanistic rationale for RCC, and this is reinforced by direct preclinical evidence (PMID 15886878, murine RCC model showing anti-angiogenic and microvascular effects of ZD6474/vandetanib) and dedicated clinical testing in VHL-related renal tumors (NCT00566995) and advanced clear cell RCC (NCT01372813).

That said, the strongest clinical signal comes specifically from VHL-disease-associated and clear-cell RCC populations rather than RCC broadly; several other TxGNN-predicted renal subtypes in this pack (TFE3-fusion RCC, neuroblastoma-associated RCC, unclassified RCC) lack any supporting trial or literature evidence and rely on VHL/HIF-independent driver pathways, which weakens the generalizability of the mechanistic argument across all RCC subtypes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Evaluated vandetanib (ZD6474) in patients with Von Hippel-Lindau disease and renal tumors; most direct and best-powered evidence in this evidence pack. |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized trial of carboplatin/gemcitabine ± vandetanib in advanced urothelial cell cancer (cisplatin-ineligible patients); relevance to RCC specifically needs confirmation. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC; terminated early, small sample, mechanistic feasibility signal only. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell RCC; most mechanistically targeted trial design but terminated with only 3 patients enrolled — underpowered. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | RCT (different drug) | Clin Cancer Res | Phase II trial of guadecitabine in SDH-deficient tumors including HLRCC-associated RCC — supports targeting hereditary RCC driver pathways, though not vandetanib itself. |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Reviews targeted therapy strategies in metastatic fumarate hydratase-deficient RCC, a molecularly defined RCC subtype with no established regimen. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Reviews antiangiogenic TKIs (including vandetanib) approved across solid tumor types, situating it among established VEGFR-targeted RCC agents. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bull Cancer | Describes cabozantinib's VEGFR2/MET/RET mechanism as comparator for multi-kinase RCC therapy, contextualizing vandetanib's shared target profile. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | Confirms vandetanib's RET-kinase inhibitory mechanism and its FDA approval basis in thyroid cancer, supporting the RET/VEGFR mechanistic rationale. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | Characterizes TFE3-Xp11.2 translocation RCC biology and novel therapeutic targets — relevant to a separate, mechanistically distinct RCC subtype (not directly supportive of the vandetanib/RCC link). |

---

## Germany Market Information

Vandetanib is currently **not marketed in Germany** (market status: 未上市, 0 authorizations on file). No German marketing authorization records are available in this evidence pack.

---

## Cytotoxicity

Vandetanib is a small-molecule multi-kinase inhibitor used as an antineoplastic agent (approved for medullary thyroid cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2/VEGFR3/EGFR/RET) |
| Myelosuppression Risk | Low — myelosuppression is not the dominant toxicity for this drug class; class-level meta-analyses in this evidence pack instead highlight hepatotoxicity (PMID 23981115) and proteinuria (PMID 32105149) as more prominent risks |
| Emetogenicity Classification | Low (typical of oral VEGFR-TKIs) |
| Monitoring Items | Liver function tests, urine protein/proteinuria monitoring, skin reactions (phototoxicity reported for this drug class, PMID 30519172); overall treatment-related mortality has been characterized for VEGFR-TKIs as a class (PMID 22651902) |
| Handling Protection | Oral targeted antineoplastic agent — follow institutional hazardous-drug handling policy for oral oncolytics; does not require conventional cytotoxic chemotherapy handling precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Structured warnings, contraindications, and drug-interaction data are currently unavailable (flagged as a **Blocking** data gap — TFDA label warnings/contraindications, DG001), which prevents completion of the S1 safety initial evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and clinical evidence for VHL-associated/clear cell RCC are reasonably solid (L2, two completed Phase 2 trials with Grade A/B relevance), but a **Blocking** data gap in official safety labeling (TFDA warnings/contraindications) prevents the mandatory S1 safety evaluation from proceeding, and the drug is not currently marketed in Germany.

**To proceed, the following is needed:**
- TFDA/official label safety data — download and parse the package insert for warnings and contraindications (DG001, Blocking)
- DrugBank-sourced mechanism of action confirmation (DG002, High)
- Completed DDI database query (currently `not_found`)
- Subgroup clarification: prioritize VHL-disease/clear cell RCC populations over general "renal cell carcinoma" given the mechanistic and trial-design specificity
- Larger, non-terminated confirmatory trial, since both directly-targeted RCC trials (NCT01372813, NCT02495103) were terminated early with very small enrollment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

