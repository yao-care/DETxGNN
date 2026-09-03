---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

> Pioglitazone is a thiazolidinedione (TZD)-class insulin sensitizer, traditionally used to improve glycemic control in type 2 diabetes mellitus.
> The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale notes no known biological link between the drug's mechanism and this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on known drug class; not explicitly recorded in this evidence pack) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, pioglitazone is a thiazolidinedione (PPAR-γ agonist) that improves peripheral insulin sensitivity and has demonstrated efficacy in type 2 diabetes mellitus, including protective effects on β-cell function and cardiovascular risk markers.

Opsismodysplasia, however, is a skeletal developmental disorder associated with INT complex genes (INTS8/RSPRY1), a pathway with no established interaction with PPAR-γ signaling. The evidence pack's own repurposing rationale explicitly states that this TxGNN score reflects a graph-embedding association rather than a biologically grounded hypothesis, and that no mechanistic rationale can currently be articulated for this drug-disease pair.

Given the absence of any mechanistic overlap, clinical trial data, or supporting literature, this prediction should be treated as a pure model output requiring independent biological validation before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Pioglitazone currently has no marketing authorizations on record in Germany (market status: **Not Marketed**, 0 total licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap — required before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (opsismodysplasia) is supported only by a model similarity score (L5, Evidence Level), with zero clinical trials, zero literature, and no plausible mechanistic link between PPAR-γ agonism and this INT-complex-related skeletal disorder — a limitation the model's own rationale explicitly acknowledges.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for pioglitazone (currently a data gap)
- TFDA/BfArM label warnings and contraindications (Blocking gap — required before S1 safety evaluation)
- Independent mechanistic or preclinical evidence connecting PPAR-γ signaling to INT-complex-associated skeletal pathology
- If pursuing repurposing research, consider prioritizing the pack's lower-ranked lipodystrophy-related predictions (ranks 5–8) instead, as these have a documented PPAR-γ/adipogenesis mechanistic rationale, even though they too currently lack clinical or trial evidence and remain at the "Research Question" stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

