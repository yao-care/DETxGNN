---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine: From (Original Indication Not Yet Documented) to Hypertrichosis

## One-Sentence Summary

> Ivabradine (DB09083) currently has no original indication or mechanism-of-action data captured in this evidence pack, and it is not marketed in Germany (0 authorizations).
> The TxGNN model predicts potential relevance to **Hypertrichosis (disease)** with a score of **99.79%**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license or indication text in evidence pack (data gap) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ivabradine in this evidence pack, and no original indication was recorded either. Without this baseline, no pharmacological bridge between the original use and hypertrichosis can be established from the supplied data alone.

It is also worth noting that among the six diseases TxGNN surfaced for this drug, all fall in a very low-confidence score band (rank 3008–9476 out of the full prediction space) and cluster around rare congenital/genetic syndromes — hypertrichosis, Ambras type congenital hypertrichosis, a malformation syndrome with dental/periodontal features, Dandy-Walker malformation syndrome, an isolated genetic hair shaft abnormality, and nephrogenic SIAD. For rank 2 (Ambras syndrome), the evidence pack itself already documents the mechanistic assessment explicitly: this is a monogenic disorder linked to the 8q24.3 region near *TRPS1*, with **no relationship to HCN/If channel pharmacology**, and the reviewer rationale already recommends **Hold** with no mechanistic support. This pattern across the batch — rare genetic syndromes with no drug-target linkage evident — suggests the hypertrichosis prediction likely shares the same weakness rather than reflecting a genuine repurposing signal.

Given the absence of MOA, original indication, and any corroborating trial or literature evidence, this prediction should be treated as an unvalidated model output rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

*(Note: literature returned elsewhere in this evidence pack, e.g. under "malformation syndrome with odontal/periodontal component," relates to periodontitis and dental microbiology, not to hypertrichosis, and is not applicable here.)*

---

## Germany Market Information

Ivabradine currently holds no German market authorization in this evidence pack (0 licenses, market status "not marketed"). No product name, dosage form, or approved indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack. TFDA label warnings/contraindications retrieval is flagged as a **Blocking** data gap (DG001), meaning a formal safety (S1) evaluation cannot proceed until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanism-of-action data, no original indication on record, no supporting clinical trials or literature for the predicted indication, and the drug is not currently marketed in Germany. Combined with the fact that a sibling prediction in the same batch (Ambras syndrome) has already been assessed as mechanistically implausible, this candidate does not meet the threshold to advance beyond an L5, model-only signal.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/German label warnings and contraindications) — currently blocking any safety (S1) evaluation
- Resolve DG002 (mechanism of action from DrugBank) to assess biological plausibility for hypertrichosis
- Confirm original approved indication(s) for ivabradine from regulatory sources
- Targeted literature search specifically on HCN/If channel involvement in hair follicle biology, if any exists, since none was returned in this pull
- Re-run evidence collection once MOA and indication data gaps are closed before re-scoring this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

