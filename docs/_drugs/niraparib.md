---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Niraparib is a PARP1/2 inhibitor internationally approved for maintenance treatment of recurrent epithelial ovarian, fallopian tube, and primary peritoneal cancer (not currently marketed in Taiwan). The TxGNN model's top-ranked prediction for this drug is **Epiglottis Neoplasm**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational output with no biological plausibility identified in the evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Taiwan; internationally approved for maintenance treatment of recurrent epithelial ovarian, fallopian tube, or primary peritoneal cancer |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.99% (model rank #289) |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. Based on the repurposing rationale provided for related candidate indications in this evidence pack, niraparib is known to act as a PARP1/2 inhibitor that exploits synthetic lethality in tumors with homologous recombination deficiency (HRD), including BRCA1/2-mutated cancers — this is the basis for its established use in ovarian cancer maintenance therapy.

For epiglottis neoplasm specifically, the evidence pack's own mechanistic annotation states that this tumor type is predominantly a head-and-neck squamous cell carcinoma with very low HRD/BRCA mutation prevalence, meaning **there is no established molecular rationale for PARP inhibitor activity** in this disease. The annotation explicitly characterizes this as "purely a model prediction, with no clinical or literature support."

This prediction should be treated as a low-confidence computational hypothesis only, not as a mechanistically or clinically substantiated repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information (Taiwan)

Niraparib is not currently marketed in Taiwan — 0 authorizations on record.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | High — niraparib is well documented to cause significant thrombocytopenia, anemia, and neutropenia; regular hematologic monitoring is required in all approved indications |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC (weekly for the first month, then monthly), blood pressure, renal and hepatic function |
| Handling Protection | Oral small-molecule targeted agent; handling per institutional hazardous drug protocols (PARP inhibitors are commonly classified as hazardous due to genotoxic potential) |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting niraparib use in epiglottis neoplasm, and the underlying tumor biology (low HRD/BRCA prevalence in head-and-neck squamous cell carcinoma) does not align with the drug's PARP-inhibition mechanism. This is an L5 (model-only) prediction with no supporting real-world data.

**To proceed, the following is needed:**
- Preclinical/biomarker data confirming HRD or BRCA pathway alterations in epiglottis/laryngeal squamous cell carcinoma subpopulations
- Mechanistic studies evaluating PARP inhibitor sensitivity in this tumor type
- Independent validation that the "epiglottis neoplasm" TxGNN label reflects a clinically coherent disease entity rather than an ontology-mapping artifact

**Additional note:** This evidence pack also contains a substantially stronger-supported prediction — **"cystic neoplasm"** (TxGNN rank #292, L2, *Proceed with Guardrails*) — corresponding to high-grade serous ovarian/endometrial carcinoma, backed by 3 clinical trials and 9 publications directly relevant to niraparib's established mechanism. This candidate may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

