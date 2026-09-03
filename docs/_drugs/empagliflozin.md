---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is a well-known SGLT2 (sodium-glucose cotransporter-2) inhibitor whose original indication (type 2 diabetes mellitus and related cardiorenal use) is not captured in this evidence pack. The TxGNN model predicts possible efficacy in **Classic Stiff Person Syndrome**, but the prediction is currently supported by **0 clinical trials** and **0 publications** — this is a model-only signal (Evidence Level L5) with a "Hold" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap — `original_indications` is empty). Empagliflozin is publicly known as an SGLT2 inhibitor for type 2 diabetes mellitus. |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | ✗ 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged in this evidence pack as data gap **DG002**, severity: High). Based on known information, Empagliflozin acts as an SGLT2 inhibitor, reducing renal glucose reabsorption; its established action is confined to renal glucose transport physiology and downstream metabolic/cardiorenal effects.

Classic Stiff Person Syndrome (SPS) is an autoimmune neurological disorder driven primarily by anti-GAD65 antibodies that impair GABAergic neurotransmission. There is no established mechanistic overlap between SGLT2 inhibition and GABAergic signaling or autoimmune neuro-modulation. Because `original_moa` is a data gap, we cannot cross-validate whether an indirect (e.g., metabolic–neuroimmune) pathway underlies this prediction.

Two observations weaken confidence in this specific signal: (1) the near-identical TxGNN scores between rank 1 (classic stiff person syndrome, 99.06%) and rank 2 (focal stiff limb syndrome, 99.06%) suggest the model is scoring an entire disease cluster rather than generating an indication-specific signal; and (2) no clinical trials, registry entries, or literature exist to corroborate the prediction. The score most likely reflects knowledge-graph node-embedding proximity (e.g., topological closeness to other neuromuscular or metabolic-comorbidity nodes) rather than a validated pharmacological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No Taiwan market authorization records are currently available for Empagliflozin in this evidence pack (`total_licenses = 0`, market status: 未上市 / Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: this evidence pack flags **DG001** (TFDA package insert warnings/contraindications — severity: **Blocking**), meaning key warnings, contraindications, and drug-drug interaction data could not be retrieved. This blocks progression to the S1 safety pre-screening stage and must be resolved before any further evaluation.

---

## Additional Predicted Indications (Same Evidence Pack)

Two further TxGNN predictions were returned alongside the primary candidate. Both share the same evidentiary profile — no clinical trials, no literature, Evidence Level L5, decision stage S0, recommendation Hold — and are noted here for completeness:

| Rank | Disease | TxGNN Score | Note |
|------|---------|-------------|------|
| 2 | Focal Stiff Limb Syndrome | 99.06% | Near-identical score to rank 1; likely reflects the same disease-cluster embedding, not a distinct signal |
| 3 | Opsismodysplasia | 99.03% | Rare pediatric skeletal dysplasia (INPPL1/SHIP2-driven); any link to SGLT2 inhibition is speculative and unsupported by data |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (Evidence Level L5) with zero corroborating clinical trials or literature, and the drug's own mechanism of action data is unavailable. A Blocking-severity data gap (TFDA warnings/contraindications) also prevents even a preliminary safety assessment, so this candidate cannot advance past S0.

**To proceed, the following is needed:**
- Resolve DG001: retrieve TFDA package insert (warnings, contraindications, DDI) to enable S1 safety pre-screening
- Resolve DG002: obtain confirmed original MOA from DrugBank/product label to assess mechanistic plausibility
- Establish original indication and Taiwan/international licensing status to support the "original vs. predicted indication" comparison
- Conduct a targeted literature/preclinical search for any SGLT2i–GABAergic or SGLT2i–autoimmune neurological mechanism, given none currently exists
- Given the clustering pattern across ranks 1–2, consider re-examining whether the underlying knowledge graph node structure is driving a shared false-positive signal across the stiff-person-syndrome spectrum before committing further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

