---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metformin: From Type 2 Diabetes to Five Rare-Disease Candidates (Model-Only Signal)

## One-Sentence Summary

Metformin is a widely used biguanide antidiabetic agent, though this specific evidence pack does not capture its original indication or mechanism (drug not currently marketed in this jurisdiction). The TxGNN model surfaces five candidate indications — led by **Focal Stiff Limb Syndrome** and **Classic Stiff Person Syndrome** — but **none are supported by any clinical trials or literature**, and the accompanying mechanistic rationales are explicitly flagged as weak or absent. This is a pure model-signal (L5) candidate set requiring full evidence build-out before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (drug not marketed locally; `original_indications` field empty) |
| Predicted New Indication | Focal Stiff Limb Syndrome (top rank; 4 additional candidates below) |
| TxGNN Prediction Score | 99.45% (rank 1); range 99.06%–99.45% across all 5 candidates |
| Evidence Level | L5 (model prediction only — no trials, no literature, for all 5 candidates) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

### All Predicted Indications

| Rank | Disease | TxGNN Score | Model Rank | Evidence Level | Recommendation |
|------|---------|-------------|-----------|-----------------|-----------------|
| 1 | Focal Stiff Limb Syndrome | 99.45% | 6338 | L5 | Hold |
| 2 | Classic Stiff Person Syndrome | 99.45% | 6339 | L5 | Hold |
| 3 | Opsismodysplasia | 99.40% | 6707 | L5 | Hold |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 99.40% | 6765 | L5 | Hold |
| 5 | Drug-Induced Localized Lipodystrophy | 99.06% | 9580 | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack. Metformin is generally known as a biguanide that activates AMPK and suppresses hepatic gluconeogenesis, an action commonly associated with type 2 diabetes management — but this evidence pack does not itself document an original indication, so this context should be treated as background rather than verified source data.

Across all five predicted indications, the model's rationale acknowledges only tenuous or absent biological links:

- **Stiff Limb / Stiff Person Syndrome** (ranks 1–2): autoimmune, anti-GAD65-mediated GABAergic disorders. No known mechanistic overlap with AMPK/glucose metabolism pathways — the rationale explicitly states there is "no known intersection" and attributes the score to graph-based association only.
- **Opsismodysplasia** (rank 3): caused by *INPPL1 (SHIP2)* mutations, a protein in the insulin-signaling pathway that has a distant topological relationship to metformin's target pathway — but no animal or human evidence supports any effect on skeletal phenotype.
- **Thiamine-Responsive Dysfunction Syndrome** (rank 4): the only plausible link is symptomatic glycemic management in TRMA-associated diabetes, not correction of the underlying thiamine-transport defect.
- **Drug-Induced Localized Lipodystrophy** (rank 5): metformin's AMPK-mediated effects on adipocyte metabolism offer a theoretical but directionally ambiguous connection; no evidence indicates it prevents or reverses lipodystrophic lesions.

In summary, all five signals originate from graph-embedding similarity in TxGNN rather than an identifiable, evidence-backed biological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the five predicted indications (Focal Stiff Limb Syndrome, Classic Stiff Person Syndrome, Opsismodysplasia, Thiamine-Responsive Dysfunction Syndrome, Drug-Induced Localized Lipodystrophy).

---

## Literature Evidence

Currently no related literature available for any of the five predicted indications.

---

## Germany Market Information

Metformin holds no current market authorizations in this jurisdiction (`market_status`: not marketed; `total_licenses`: 0). No product listings are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. Note: this evidence pack could not retrieve label warnings, contraindications, or drug–drug interaction data (source: TFDA/BfArM label PDF), which is flagged as a **Blocking** gap preventing preliminary safety screening (S1) for any of these candidates.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications rest solely on TxGNN model output (L5) with zero supporting clinical trials or literature, and the model's own mechanistic rationales describe the biological links as weak, indirect, or entirely absent. Combined with missing MOA and safety label data, there is no basis to advance any candidate beyond model-signal stage.

**To proceed, the following is needed:**
- Retrieve and parse TFDA/BfArM label (warnings, contraindications, DDI) — currently Blocking (DG001)
- Confirm metformin's mechanism of action via DrugBank API — currently High priority gap (DG002)
- Targeted literature and clinical trial searches for each of the five candidate indications (autoimmune neurology, skeletal dysplasia, thiamine metabolism disorders, lipodystrophy) to establish whether any move beyond L5
- Independent mechanistic/pharmacological review before any candidate is considered for S1 entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

