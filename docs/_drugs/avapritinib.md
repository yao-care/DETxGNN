---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: From Undocumented Original Indication to Axial Spondylometaphyseal Dysplasia (Low-Confidence Signal)

## One-Sentence Summary

> The evidence pack for Avapritinib does not contain its original approved indication or mechanism of action (both marked as data gaps).
> The TxGNN model's top prediction is **Axial Spondylometaphyseal Dysplasia**, but this is one of 10 top-ranked predictions,
> **none of which are supported by any clinical trials or literature** — all 10 fall into evidence level L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (DrugBank `original_indications` and `original_moa` are both empty/data-gap) |
| Predicted New Indication | Axial Spondylometaphyseal Dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for avapritinib in this evidence pack (data gap DG002, severity High). Based on the repurposing rationale attached to each of the 10 predictions, avapritinib is understood to be a **KIT/PDGFRA tyrosine kinase inhibitor**. However, the rationale text for every single one of the top 10 predictions explicitly states that **no known mechanistic or pathway link** exists between KIT/PDGFRA inhibition and the predicted disease.

Looking across all 10 predictions, a clear pattern emerges: they cluster into two disease groups — rare skeletal/neurodevelopmental syndromes (ranks 1, 2, 4, 8) and the amyotrophic lateral sclerosis (ALS) spectrum of motor neuron diseases (ranks 3, 5, 6, 7, 9, 10). The rank-10 rationale directly notes this pattern, suggesting the TxGNN model is grouping these diseases by **phenotypic/graph-topological similarity to each other**, not by a genuine pharmacological relationship to avapritinib. Without original indication or MOA data to anchor a repurposing hypothesis, and without any external corroborating evidence, these predictions should be treated as exploratory signals only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Avapritinib currently holds no marketing authorization in Germany (0 licenses on record); no dosage form or approved-indication data is available.

---

## Cytotoxicity

Avapritinib is understood to be a KIT/PDGFRA tyrosine kinase inhibitor, a class of targeted antineoplastic therapy typically used in oncology. Detailed cytotoxicity classification, myelosuppression risk, emetogenicity, and monitoring data are not available in the current evidence pack. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked predicted indications are evidence level L5 (model prediction only) with zero supporting clinical trials or literature, and the repurposing rationale itself flags a likely lack of genuine mechanistic relevance. In addition, drug-level safety data (warnings, contraindications, MOA) is entirely missing, including a Blocking-severity gap (DG001) that prevents even an initial S1 safety review.

**To proceed, the following is needed:**
- TFDA/BfArM package insert with warnings and contraindications (DG001, Blocking — required before any safety pre-screening)
- Mechanism of action data from DrugBank (DG002)
- Confirmation of avapritinib's original approved indication(s) to establish a repurposing baseline
- Independent literature/clinical trial search for the top-ranked predicted indications, since the current zero-hit result may reflect either a genuinely novel signal or a coverage limitation of the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

