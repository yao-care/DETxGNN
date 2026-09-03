---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Analgesic/Anti-inflammatory Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used NSAID (mechanism of action data not provided in this Evidence Pack); no original indication text was supplied either. TxGNN's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare autosomal recessive skeletal dysplasia, but this is supported by **zero clinical trials** and **zero publications**, and the model's own rationale flags the link as likely a knowledge-graph co-occurrence artifact rather than a genuine mechanistic relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no `original_indications` or license data provided) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no clinical/literature support) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ibuprofen in this Evidence Pack (flagged as a High-severity data gap, DG002). Without this, no credible pharmacological bridge can be established between Ibuprofen's known COX-inhibition/anti-inflammatory activity and the predicted indication.

Acromesomelic Dysplasia, Hunter-Thompson Type is caused by *NPR2* gene mutations that disrupt CNP (C-type natriuretic peptide) signaling in growth-plate chondrocytes — a developmental/genetic disorder, not an inflammatory condition. The rationale provided alongside this prediction explicitly states there is no direct causal relationship to Ibuprofen's COX-inhibitory mechanism, and attributes the high TxGNN score to co-occurrence of "skeletal/joint symptom" nodes in the knowledge graph rather than a real disease-modifying effect.

This pattern repeats across all seven ranked predictions in this Evidence Pack (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) — all are rare structural/genetic skeletal or developmental disorders with no inflammatory pathophysiology, no supporting trials, and no supporting literature. The one partial exception is pseudoachondroplasia, where NSAIDs could plausibly offer *symptomatic* pain relief for associated early-onset osteoarthritis-like joint pain, but this would be symptom management, not a disease-modifying repurposing indication, and remains entirely unstudied in this population.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No market authorization data available — Ibuprofen is recorded as **not marketed** in this dataset, with 0 total licenses.

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are all marked as data gaps in this Evidence Pack; TFDA/BfArM label review is separately flagged as a Blocking data gap — DG001 — required before any S1 safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate lacks the three pillars needed to advance: no MOA data to support mechanistic plausibility, no clinical or literature evidence for any of the seven predicted indications, and no German market presence. The prediction's own rationale explicitly identifies the top-ranked indication as a probable knowledge-graph co-occurrence artifact rather than a real signal.

**To proceed, the following is needed:**
- Ibuprofen mechanism of action (MOA) data (DG002)
- TFDA/BfArM label — warnings and contraindications (DG001, Blocking)
- Independent mechanistic review of why TxGNN assigns high scores to genetically-driven skeletal dysplasias with no inflammatory component (possible model calibration issue)
- If pursuing the pseudoachondroplasia signal specifically: literature/case evidence on NSAID use for joint pain in COMP-related skeletal dysplasias, since this is the only prediction with a plausible (symptomatic) rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

