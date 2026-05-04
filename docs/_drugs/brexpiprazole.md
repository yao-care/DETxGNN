---
layout: default
title: Brexpiprazole
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 0
---

# Brexpiprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Brexpiprazole: Evaluation Incomplete — No Repurposing Predictions Available

## One-Sentence Summary

Brexpiprazole is an atypical antipsychotic (serotonin-dopamine activity modulator) approved in multiple jurisdictions for schizophrenia and adjunctive treatment of major depressive disorder.
The current Evidence Pack (v4) contains **no TxGNN repurposing predictions**, and two critical data gaps — MOA detail and package-insert safety information — have been flagged as Blocking/High severity, preventing a complete repurposing assessment.
A Hold decision is recommended until the data gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Major Depressive Disorder (adjunctive) |
| Predicted New Indication | Not available — no TxGNN predictions in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted new indication is present in this Evidence Pack, so a mechanistic repurposing rationale cannot be generated at this stage.

Detailed MOA data is not available in the Evidence Pack (DG002, High severity). Based on publicly available information, brexpiprazole is classified as a serotonin-dopamine activity modulator (SDAM). It acts as a partial agonist at dopamine D2/D3 and serotonin 5-HT1A receptors, and as an antagonist at 5-HT2A, adrenergic α1B, and α2C receptors — a receptor profile that distinguishes it from first-generation antipsychotics and underlies its lower extrapyramidal side-effect burden. Its efficacy in schizophrenia and MDD has been established in Phase 3 trials, and it received FDA approval for agitation associated with Alzheimer's dementia in 2023, suggesting emerging evidence for neurodegenerative indications.

To produce a meaningful repurposing rationale, TxGNN predictions must first be generated, after which mechanistic links between the confirmed MOA and candidate indications can be evaluated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Package-insert warnings and contraindications could not be extracted — flagged as DG001, Blocking severity. DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN predictions and two unresolved data gaps of Blocking/High severity; a repurposing assessment cannot be completed without remediating these gaps first.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse the TFDA (or EMA/BfArM) package insert to extract warnings and contraindications; this must be resolved before any safety screening can begin.
- **[DG002 — High]** Query the DrugBank API to retrieve the full MOA, pharmacodynamics, and toxicity data for DB09128.
- **TxGNN inference** Run the TxGNN pipeline for brexpiprazole to generate predicted indication candidates; without predictions, the repurposing evaluation cannot proceed past this stage.
- **DDI data** Re-query a drug–drug interaction database (e.g., DrugBank DDI, CREDIBLEMEDS) with the correct search parameters; the current query returned zero results.
- **Germany (BfArM) authorization** Confirm current EMA/BfArM approval status directly, as the regulatory field reflects zero licenses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

