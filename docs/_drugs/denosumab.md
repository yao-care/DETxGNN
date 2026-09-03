---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 2
---

# Denosumab
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

# Denosumab: Original Indication Unconfirmed → Predicted Application in Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Denosumab's original approved indication cannot be confirmed from the current evidence pack (no license or indication text on file), though it is broadly known as a RANKL-targeting monoclonal antibody used in bone-related conditions.
> The TxGNN model predicts a possible role in **Severe Nonproliferative Diabetic Retinopathy**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure algorithmic extrapolation with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` and `taiwan_regulatory.licenses` are both empty in this evidence pack |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% (rank 4724) |
| Evidence Level | **L5** (model prediction only) |
| Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, DrugBank query pending). The predicted-indication rationale supplied with this pack states the working hypothesis directly: the prediction extends a **RANKL/OPG axis hypothesis** — already flagged as relevant to diabetic retinopathy in general — to a specific disease subtype (severe nonproliferative disease). However, the rationale explicitly notes this is "a pure knowledge-graph node-similarity extrapolation by the TxGNN algorithm, lacking any subtype-specific biological argumentation," and is unsupported by any direct or indirect clinical data.

Some indirect support exists for the **broader** diabetic retinopathy category (TxGNN rank 2, score 99.23%, evidence level L4), which is the presumed biological basis this severe-subtype prediction is extrapolated from:

- **OPG–RANKL correlation**: Osteoprotegerin (OPG), the decoy receptor for RANKL, has been reported elevated in patients with diabetic retinopathy and correlated with disease severity — suggesting the RANKL/OPG axis may participate in retinal vascular pathology (inflammation, vascular remodeling). This is a correlative biomarker association, not an established causal treatment mechanism, and the direction of effect (denosumab *inhibits* RANKL, whereas the association is with *elevated* OPG) is not fully consistent with a straightforward causal story.
- A 2024 real-world cohort study (PMID [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/), Henney et al., *Diabetes Obes Metab*) found denosumab use was associated with reduced incidence of type 2 diabetes and lower rates of microvascular complications (including retinopathy) compared with bisphosphonates — an observational signal, not an interventional efficacy result for retinopathy itself.

No evidence in this pack specifically addresses the **severe nonproliferative** subtype rank 1 is predicting for; all available signal pertains to diabetic retinopathy as a broad category.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

*Context: one Phase 3 trial exists for the broader diabetic retinopathy/denosumab space — [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) (completed, n=769) — but it evaluated lens opacification (cataract) safety in prostate cancer patients on denosumab for bone loss, not retinopathy efficacy. It was graded **C/low relevance** by evidence review and provides ocular safety context only, not efficacy evidence.*

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy specifically.

*Context: two publications support the broader diabetic retinopathy category (cited in the mechanism discussion above) — a 2024 real-world cohort/meta-analysis (PMID 38899553) and a 2023 fracture-risk cohort (PMID 36960265) with lower relevance. Neither addresses the severe subtype or provides interventional efficacy data.*

---

## Market Information

No marketing authorizations currently on file (product status: Not Marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: local (TFDA-equivalent) label warnings and contraindications could not be retrieved for this evidence pack (DG001, **Blocking** severity) — this alone prevents any S1 safety pre-assessment for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (severe nonproliferative diabetic retinopathy) has zero direct clinical trial or literature support and an L5 evidence level — this is an unvalidated knowledge-graph extrapolation from a broader, itself only weakly-supported (L4, correlative) disease association. Combined with a blocking data gap on local label warnings/contraindications, the candidate cannot yet enter safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/local package insert warnings and contraindications (DG001, blocking — required before any S1 safety review)
- Denosumab mechanism-of-action data from DrugBank (DG002)
- Original indication and licensing data (currently entirely absent from this pack)
- Preclinical or translational evidence linking the RANKL/OPG axis causally (not just correlatively) to diabetic retinopathy, and specifically to the severe nonproliferative subtype
- If pursuing the broader diabetic retinopathy signal (rank 2) instead, prospective mechanistic or interventional studies to move beyond the current cohort-level, correlative evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

