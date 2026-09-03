---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Undocumented Original Indication to Pseudo-von Willebrand Disease

## One-Sentence Summary

Defibrotide's original approved indication and mechanism of action are not documented in this evidence pack, and the drug is not currently marketed. The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, but this prediction is currently supported by **no clinical trials and no literature** — it is a purely computational inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license/indication text available) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for defibrotide is not available in this evidence pack, and no original indication is on file. Based on general pharmacological knowledge, defibrotide is a polydeoxyribonucleotide-derived agent with antithrombotic, profibrinolytic, and endothelial-protective properties — properties that are documented later in this report for the related "thrombotic thrombocytopenic purpura" prediction (rank 4).

For pseudo-von Willebrand disease specifically, the repurposing rationale explicitly states that this connection is **not** based on any verifiable mechanistic literature. The model's high score (0.999) is presumed to arise from graph-level similarity between this disease and other platelet-function disorders in the knowledge graph, rather than any known pharmacological or clinical relationship. No mechanistic argument for this pairing can currently be substantiated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No authorization records are available — defibrotide is not currently marketed (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: safety warnings, contraindications, and drug-interaction data are all currently missing from the evidence pack. TFDA label warnings/contraindications are flagged as a **blocking** data gap for safety pre-screening.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (evidence level L5) — the prediction rests solely on the TxGNN model score, with no mechanistic or empirical corroboration. It cannot proceed past the initial screening stage (S0) as-is.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action data (currently blocking mechanistic-relevance analysis)
- TFDA/official label warnings and contraindications (blocking — required before any safety pre-screening, S1)
- Targeted literature/trial search specific to pseudo-von Willebrand disease and defibrotide, since none currently exist
- Consider re-evaluating lower-ranked but better-evidenced candidates in this same evidence pack: **thrombotic thrombocytopenic purpura** (rank 4) and **thrombocytopenic purpura** (rank 10) both reached evidence level L3 / decision stage S1 ("Research Question") with multiple case series and a 2023 in-vitro mechanistic study, though one adverse-event case report (PMID 7896218) also describes defibrotide-associated TTP and should be weighed as a safety signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

