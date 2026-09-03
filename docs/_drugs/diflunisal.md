---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: From NSAID Analgesic Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Diflunisal is a salicylic-acid-derivative NSAID; detailed original indication and mechanism-of-action data are not yet available in this evidence pack.
> The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare genetic skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, with no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available data (Diflunisal is pharmacologically classified as a salicylate-derivative NSAID) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Diflunisal in this evidence pack. Based on general pharmacological classification, Diflunisal is a salicylic-acid-derivative NSAID that inhibits cyclo-oxygenase (COX-1/COX-2), reducing prostaglandin synthesis to produce analgesic and anti-inflammatory effects — a mechanism class typically applied to musculoskeletal pain and inflammatory arthritic conditions.

The top-ranked predicted indication, Acromesomelic Dysplasia (Hunter-Thompson Type), is a structural genetic skeletal disorder caused by GDF5/CDMP1 mutations. There is no known inflammatory or prostaglandin-mediated pathophysiology in this condition, so an NSAID's anti-inflammatory mechanism has no plausible therapeutic rationale here. The evidence pack's own repurposing rationale confirms this: "structural genetic disease, no reasonable treatment basis for NSAID anti-inflammatory mechanism, no clinical evidence." This prediction likely reflects a TxGNN embedding-similarity artifact rather than a biologically grounded signal.

**Note:** A lower-ranked candidate in this same evidence pack — **ankylosing spondylitis** (rank 5) and its broader category **inflammatory spondylopathy** (rank 10) — shows a mechanistically coherent link (NSAID COX inhibition for inflammatory spondyloarthropathy) and is supported by an actual randomized controlled trial comparing diflunisal to phenylbutazone in AS patients (L2, "Proceed with Guardrails"). This may be a more clinically meaningful repurposing candidate than the top TxGNN-scored disease and could warrant separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Acromesomelic Dysplasia, Hunter-Thompson Type) is a rare genetic skeletal disorder with no plausible mechanistic link to NSAID pharmacology, and no clinical trial or literature evidence exists to support it. In addition, TFDA/BfArM package insert warnings and contraindications are currently missing (a blocking data gap), so this candidate cannot proceed to safety evaluation.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — currently a blocking data gap
- DrugBank-sourced mechanism of action (MOA) data
- Reconsider evaluation priority: the ankylosing spondylitis / inflammatory spondylopathy candidates in this same evidence pack have stronger mechanistic and clinical trial support and may merit a dedicated evaluation report instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

