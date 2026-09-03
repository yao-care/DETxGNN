---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity to Diabetic Cataract

## One-Sentence Summary

Glucarpidase (DrugBank DB08898) is a recombinant bacterial enzyme (carboxypeptidase G2) used as an emergency antidote to inactivate toxic methotrexate levels. The TxGNN model predicts a possible effect on **Diabetic Cataract** and nine other cataract/retinopathy-related conditions, but **no clinical trials or literature currently support any of these predictions**, and the mechanistic rationale provided is explicitly assessed as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methotrexate (MTX) toxicity — emergency detoxification (derived from evidence pack rationale; no formal indication text on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on the information present in this evidence pack, glucarpidase's only well-established biological activity is hydrolyzing the terminal glutamate residue of methotrexate, which inactivates the drug and is used clinically for MTX overdose rescue. This is a highly specific, single-substrate enzymatic function with no known involvement in lens metabolism, advanced glycation end-product (AGE) accumulation, oxidative stress, retinal microvascular pathology, or calcium/parathyroid pathways — the mechanisms typically implicated in cataract and diabetic retinopathy.

The evidence pack's own repurposing rationale for every one of the top 10 predicted indications (all cataract subtypes and diabetic retinopathy) states there is **no known mechanistic link** between glucarpidase and these conditions, and attributes the high TxGNN scores to sparse indirect graph connections (e.g., co-occurrence of "enzyme-class drug" and "metabolic eye disease" nodes) rather than genuine pharmacological plausibility.

Given that the original indication (acute MTX toxicity, a single-dose IV rescue therapy) has no logical or mechanistic relationship to chronic ophthalmic conditions like cataract, this prediction cluster should be treated as a low-confidence graph-topology artifact rather than a credible repurposing hypothesis.

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
All 10 predicted indications (diabetic cataract, diabetic retinopathy, and 8 other cataract subtypes) carry Evidence Level L5 with zero supporting clinical trials or literature, and the evidence pack's own mechanistic analysis explicitly concludes there is no biological plausibility linking glucarpidase's known enzymatic activity to any of these ophthalmic conditions.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for glucarpidase (currently Data Gap, DG002)
- TFDA/manufacturer package insert warnings and contraindications (currently Data Gap, DG001 — Blocking)
- Independent preclinical or mechanistic studies establishing a plausible pathway between carboxypeptidase G2 activity and lens/retinal pathology before any further evaluation is warranted
- Re-evaluation should only be triggered if new literature or trial data emerges; no active investment is recommended at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

