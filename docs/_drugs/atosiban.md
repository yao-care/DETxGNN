---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Preterm Labor (Tocolysis) to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is a competitive oxytocin/vasopressin V1A receptor antagonist used clinically for tocolysis in threatened preterm labor. The TxGNN model's top prediction is **Primary Hereditary Glaucoma**, but this direction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own rationale flags it as a likely knowledge-graph artifact rather than a biologically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Preterm labor / tocolysis (per drug rationale text; no formal indication record or MOA field is available in this data set) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on what can be inferred from the drug-level rationale text, atosiban acts as a competitive oxytocin/vasopressin V1A receptor antagonist and is clinically used for tocolysis (delaying preterm labor).

There is no known or plausible mechanistic link between oxytocin/V1A receptor antagonism and the pathophysiology of primary hereditary glaucoma, which is governed by aqueous humor dynamics and intraocular pressure regulation. The evidence pack's own repurposing rationale explicitly states this connection is judged to be a **TxGNN graph-association artifact with no biological basis**, and no clinical trial or literature evidence was found to support it.

For context, among the 10 TxGNN-predicted indications provided, only one (rank 6, "vascular disease") has any supporting literature — and even there, the cited studies concern oxytocin **agonism** producing cardioprotective/vasoconstrictive effects, which is mechanistically the *opposite* direction of atosiban's antagonist action. No candidate in this list currently has a coherent, evidence-backed repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Atosiban is not currently marketed in Germany, and no authorization records are available in this data set.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA package insert warnings/contraindications are flagged as a **Blocking** data gap (DG001) — safety pre-assessment (S1) cannot proceed without this data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Primary Hereditary Glaucoma) has no supporting clinical trials or literature (L5, decision stage S0), and its own mechanistic rationale identifies it as a likely model artifact rather than a genuine biological hypothesis. Combined with the absence of core safety data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/package insert warnings and contraindications (DG001, Blocking — required before any S1 safety assessment)
- Detailed mechanism of action data from DrugBank (DG002)
- Independent biological or preclinical evidence directly linking V1A receptor antagonism to intraocular pressure or aqueous humor regulation (none currently exists)
- If exploring alternative candidates from this prediction set, note that "vascular disease" (rank 6) has the most literature support (L4) but requires resolving the agonist-vs-antagonist mechanistic contradiction before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

