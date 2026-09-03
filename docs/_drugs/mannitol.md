---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Mannitol is a long-established osmotic diuretic agent; formal original-indication and MOA records are currently unavailable in this Evidence Pack, though it is widely known clinically for use in raised intracranial/intraocular pressure and oliguric states.
> The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
> but this prediction is currently supported by **0 clinical trials** and only **1 loosely related publication**, and should be treated as a hypothesis-generating signal rather than actionable evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory data (0 licenses on file); based on known pharmacology, mannitol is historically used as an osmotic diuretic for cerebral/ocular edema and acute oliguric states |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the Evidence Pack (`original_moa: [Data Gap]`). Based on known pharmacological information, mannitol is a sugar-alcohol osmotic agent that draws free water into the vascular compartment and promotes renal free-water excretion; it has long been used clinically to reduce intracranial and intraocular pressure and to maintain urine output in acute oliguric states.

The mechanistic rationale offered for NSIAD is that an osmotic diuretic could theoretically increase free-water clearance and thereby correct the dilutional hyponatremia characteristic of NSIAD. However, the single literature item retrieved for this pairing (PMID 26706473) is a general review on pitfalls in evaluating hyponatremia — it does **not** mention mannitol or NSIAD specifically, and provides no direct experimental or clinical support for this drug-disease pairing.

It should also be noted that a lower-ranked prediction in this same evidence pack (rank 9, nephrogenic diabetes insipidus) flags mannitol/osmotic agents as agents that can **induce** a diabetes-insipidus-like excessive free-water loss rather than treat it — the opposite physiological direction. This raises a plausibility concern about the NSIAD prediction that should be resolved before further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European journal of internal medicine | General review of common diagnostic pitfalls in evaluating hyponatremic patients; does not specifically address mannitol or NSIAD |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN's algorithmic score (L5, no trials, one indirectly-related review); there is no direct mechanistic or clinical evidence linking mannitol to NSIAD, and a plausible opposite-direction safety signal (osmotic-agent-induced free-water loss) exists elsewhere in this evidence pack that has not been reconciled.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data for mannitol (currently flagged as Blocking/High data gaps, DG001–DG002)
- TFDA/BfArM label review to resolve the apparent contradiction between "treats NSIAD" and "can induce NDI-like free-water loss"
- Preclinical or case-level evidence directly testing mannitol in NSIAD/SIADH-related hyponatremia before advancing past S0

**Additional note:** Among the 10 TxGNN-predicted indications in this pack, most (ranks 1, 3, 5–10) are L5/Hold with little or no supporting evidence. The only candidate with a documented, established clinical rationale — mannitol's adjunctive osmotic-diuresis role to mitigate rhabdomyolysis-related renal injury during malignant hyperthermia crises (rank 4, L4/S1, "Research Question") — may be a more productive line to pursue if further repurposing work on this drug is planned.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

