---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa is a recombinant Factor Xa decoy protein originally developed to reverse life-threatening bleeding in patients on oral Factor Xa inhibitors (e.g., rivaroxaban, apixaban). The TxGNN model predicts a possible link to **Glanzmann thrombasthenia**, but this prediction currently has **zero clinical trials** and **zero supporting publications** — it rests entirely on model-level similarity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of anticoagulant effect of Factor Xa inhibitors in patients with major/life-threatening bleeding (derived from literature context in this pack; not present in structured regulatory data) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured record (flagged as a data gap). Based on the literature captured in this evidence pack, andexanet alfa acts as a modified, catalytically inactive Factor Xa decoy — it binds and sequesters oral Factor Xa inhibitors, thereby restoring endogenous Xa activity. It does not supply clotting factors, and it does not act on platelet aggregation pathways.

Glanzmann thrombasthenia, by contrast, is a congenital platelet disorder caused by GPIIb/IIIa receptor deficiency, which impairs platelet-to-platelet aggregation independent of the coagulation cascade. There is no shared molecular target or pathway between neutralizing a Factor Xa inhibitor and correcting a GPIIb/IIIa defect.

The evidence pack's own mechanistic rationale is explicit on this point: the high TxGNN score most likely reflects the model's semantic proximity between "bleeding/coagulation disorder" concepts in the knowledge graph, rather than a genuine pharmacological relationship. The same disconnect applies to the two other top-ranked candidates (primary platelet release disorder, pseudo-von Willebrand disease), and even to hemophilia (rank 4), where literature exists but describes andexanet's role in *interfering with* factor assays and *reversing* anticoagulation — not treating factor deficiency itself. All four candidates were scored **Hold** for this reason.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

### Additional Predicted Candidates Considered (Not Primary Focus)

| Rank | Disease | TxGNN Score | Evidence Level | Literature | Recommendation |
|------|---------|-------------|-----------------|------------|-----------------|
| 2 | Primary release disorder of platelets | 99.76% | L5 | None | Hold |
| 3 | Pseudo-von Willebrand disease | 99.65% | L5 | None | Hold |
| 4 | Hemophilia | 99.10% | L4 | 11 papers (mostly on DOAC reversal / lab interference, none supporting therapeutic use in hemophilia) | Hold |

## Germany Market Information

Andexanet alfa is not currently marketed in Germany (market status: not marketed), and no marketing authorization records are present in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/BfArM label warnings and contraindications are flagged in this evidence pack as a **blocking data gap**, meaning a safety pre-screen (S1) cannot be completed until this is resolved.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications for andexanet alfa show no clinical trial or literature support, and the evidence pack's own mechanistic analysis concludes the top-ranked prediction (Glanzmann thrombasthenia) is very likely a knowledge-graph artifact rather than a genuine pharmacological signal. Combined with a blocking safety data gap, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Confirmed mechanism of action from DrugBank/primary sources (currently a data gap)
- TFDA/BfArM package insert (warnings, contraindications) — blocking gap, required before any S1 safety pre-screen
- Any preclinical or mechanistic studies specifically linking Factor Xa decoy activity to platelet-function disorders, if such evidence emerges
- Re-evaluation if new clinical trials or publications on any of the four candidate indications are registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

