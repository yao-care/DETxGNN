---
layout: default
title: Reteplase
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: Drug Repurposing Assessment — Insufficient Evidence for Evaluation

## One-Sentence Summary

Reteplase (DB00015) is a recombinant tissue plasminogen activator (tPA) used in thrombolytic therapy. The current Evidence Pack contains **no TxGNN predicted indications**, combined with blocking data gaps in safety information and mechanism of action, meaning a meaningful repurposing evaluation **cannot be completed at this stage**. A Hold decision is warranted until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in current Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no predictions, no supporting studies identified) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The TxGNN model returned zero predicted indications for Reteplase in this Evidence Pack. This typically occurs for one of the following reasons:

1. **Knowledge graph coverage gap**: Reteplase may not be sufficiently represented as a node in the TxGNN heterogeneous knowledge graph, limiting the model's ability to propagate disease associations.
2. **Narrow mechanism profile**: As a thrombolytic agent acting specifically on fibrin clots via plasminogen activation, Reteplase's pharmacological footprint may not overlap with non-cardiovascular disease nodes in the graph at the current prediction threshold.
3. **Data input incompleteness**: The Evidence Pack lists `original_indications` as empty and `original_moa` as unavailable. Without these anchors, the model cannot seed association traversal.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological class, Reteplase is a recombinant deletion mutant of human tissue-type plasminogen activator; its thrombolytic efficacy in acute myocardial infarction has been established clinically, and any mechanistic applicability to new indications would depend on resolving the MOA data gap first.

---

## Germany Market Information

Reteplase holds **no marketing authorizations** in Germany at the time of this report. There are no licensed products, dosage forms, or approved indications on record in the current Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were returned in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Reteplase is critically incomplete — TxGNN produced no predicted indications, mechanism of action data is absent, all safety fields are empty, and the drug has no German market authorization. There is no evaluable repurposing signal at this time.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve full package insert (TFDA / BfArM / SmPC) to populate warnings, contraindications, and approved indications — this is a prerequisite for any safety screening
- **[High]** Obtain MOA data from DrugBank API (query returned 1 result but MOA was not extracted) — required for mechanistic plausibility analysis
- **[High]** Re-run TxGNN prediction pipeline after confirming Reteplase is correctly represented as a knowledge graph node; verify node ID mapping between DrugBank DB00015 and the KG entity
- **[Medium]** Confirm whether Reteplase has regulatory approvals outside Germany (e.g., EMA, FDA) that could anchor the original indication field and support cross-market repurposing analysis
- **[Medium]** Check TxGNN prediction threshold settings — if the score cutoff is set high, lowering it may surface sub-threshold candidate indications for exploratory review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

