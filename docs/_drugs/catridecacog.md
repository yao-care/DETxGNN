---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 3
---

# Catridecacog
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Catridecacog: From Congenital Factor XIII A-Subunit Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

> Catridecacog (DB09310) is a recombinant Factor XIIIA subunit used for the prophylactic treatment of congenital Factor XIII A-subunit deficiency.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but currently **no clinical trials** and **no published literature** support this direction — this is a model-only prediction (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital Factor XIII A-subunit deficiency *(not captured in evidence pack — original_indications field empty; based on known drug profile of catridecacog)* |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.29% (rank 7629) |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (MOA field flagged as Data Gap, severity High). Based on the repurposing rationale attached to the prediction itself, catridecacog is a recombinant Factor XIIIA subunit that acts far downstream in the coagulation cascade — it stabilizes fibrin cross-linking after a clot has already formed. It does not act on platelet granule release, platelet receptor function, or platelet aggregation pathways.

Primary release disorder of platelets (e.g., storage pool disease) is caused by defective δ/α-granule content release from platelets — a mechanism entirely upstream of, and independent from, fibrin stabilization. The evidence pack's own mechanistic assessment explicitly states there is **no direct mechanistic link**, and that this association is "purely data-driven" without biological plausibility support.

For completeness, two other candidates were predicted with similarly high TxGNN scores but equally weak mechanistic grounding: **pseudo-von Willebrand disease** (rank 2, score 99.29%, mismatch — pathology is a GPIbα receptor gain-of-function mutation) and **Glanzmann thrombasthenia** (rank 3, score 99.15%, mismatch — pathology is GPIIb/IIIa integrin deficiency). All three predictions share the same limitation: they are platelet-function disorders, while catridecacog's mechanism operates strictly at the fibrin cross-linking step, downstream of platelet involvement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Catridecacog currently has no market authorization in Germany (0 authorizations, market status: 未上市/Not marketed). No license records are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No warnings, contraindications, or drug interaction data currently available — TFDA/BfArM labeling data flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by no clinical trials, no literature, and the mechanistic rationale explicitly argues against biological plausibility — catridecacog's downstream fibrin-stabilizing action does not address the upstream platelet granule-release, receptor, or aggregation defects seen in any of the three predicted indications. This is an L5, model-score-only signal.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (DrugBank API query) — currently a High-severity data gap (DG002)
- Preclinical or case-level evidence directly linking Factor XIII supplementation to platelet-release disorders, pseudo-von Willebrand disease, or Glanzmann thrombasthenia, before advancing beyond S0
- Given the mechanistic mismatch identified above, re-evaluation of whether these candidates warrant further investment at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

