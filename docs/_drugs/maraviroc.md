---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Maraviroc is a CCR5 co-receptor antagonist originally developed for CCR5-tropic HIV-1 infection.
> The TxGNN model's top-ranked prediction suggests possible relevance to **Multiple Endocrine Neoplasia**,
> but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5-tropic), used as part of combination antiretroviral therapy — not documented in this evidence pack's `taiwan_regulatory` data (drug not marketed in Germany) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% (rank 2613) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a High-severity data gap). Based on general clinical knowledge, maraviroc is a small-molecule CCR5 antagonist that blocks viral entry by preventing gp120 from binding the CCR5 co-receptor; its efficacy in CCR5-tropic HIV-1 infection is well established.

For the top-ranked prediction, however, the evidence pack's own mechanistic assessment is explicit and unfavorable: *"There is no known link between CCR5 antagonism and the pathogenesis of endocrine neoplasia; this is a pure TxGNN algorithmic score with no supporting literature or trials."* In other words, TxGNN identified a statistical association in its knowledge graph embedding space, but no biological rationale currently connects CCR5 blockade to multiple endocrine neoplasia.

It is worth noting that among the 10 predictions in this pack, several lower-ranked candidates have more coherent mechanistic support — notably **HER2-positive breast carcinoma** (rank 10), where a preclinical study shows the CCL5–CCR5 autocrine axis drives trastuzumab resistance via ERK activation, giving a concrete rationale for CCR5 blockade as a resistance-reversal strategy. This candidate reached decision stage S1, unlike the top-ranked prediction, and may merit closer follow-up despite its lower TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Maraviroc is **not currently marketed in Germany** under this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available for this candidate; obtaining official labeling is flagged as a **Blocking** data gap (DG001) that must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (multiple endocrine neoplasia) has no clinical trial or literature support and the evidence pack explicitly states there is no known mechanistic link — this is a pure model artifact (L5) and does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official TFDA/EMA prescribing information to complete S1 safety pre-assessment
- Resolve DG002 (High): obtain confirmed MOA data from DrugBank/label to support or refute mechanistic linkage claims
- If pursuing repurposing further, consider redirecting focus toward the pack's stronger secondary signals — particularly **HER2-positive breast carcinoma** (S1 stage, in vitro mechanistic evidence on CCL5-CCR5/ERK-mediated trastuzumab resistance) and, at lower priority, the cutaneous T-cell lymphoma and CMV infection hypotheses (L4, Research Question stage) — rather than the top-ranked but mechanistically unsupported multiple endocrine neoplasia prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

