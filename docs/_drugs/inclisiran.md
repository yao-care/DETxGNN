---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Original Indication Not on Record → Predicted Use in Potassium Deficiency Disease

## One-Sentence Summary

> Inclisiran's original approved indication and mechanism of action are not available in the current evidence pack (flagged as data gaps). The TxGNN model's top-ranked prediction for this drug is **Potassium Deficiency Disease**, but this prediction is currently backed by **0 clinical trials** and **0 publications** — it is a pure model score with no real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on record; regulatory license list is empty) |
| Predicted New Indication | Potassium Deficiency Disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Inclisiran is not available in this evidence pack — it is flagged as a **High-severity data gap** requiring a DrugBank API lookup. The original approved indication is also empty in this dataset, and the drug currently has **zero regulatory authorizations** in Germany (未上市).

Because both the original indication and MOA are undocumented here, mechanistic plausibility cannot be assessed from first principles. The evidence pack's own rationale field for this specific candidate is explicit and unambiguous:

> "No known PCSK9/siRNA mechanism relates to potassium ion homeostasis; this is purely a high TxGNN score with no supporting evidence."

For context, other entries in this same evidence pack describe Inclisiran as a **PCSK9-targeted siRNA** primarily used to lower LDL-cholesterol — but this pharmacological class has no established or hypothesized link to potassium balance. In other words, the embedding model produced a high similarity score, but there is no biological hypothesis, clinical trial, or literature connecting Inclisiran's known pharmacology to this predicted indication.

Given the complete absence of mechanistic rationale or clinical/literature support, this top-ranked prediction should be treated as a **low-confidence, exploratory signal only**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Inclisiran is currently **not marketed** in Germany under this evidence pack — there are 0 registered authorizations and no license records to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Potassium Deficiency Disease) has zero clinical trials and zero literature support (L5 — model prediction only), and the drug itself lacks basic reference data (original indication, MOA, safety labeling) needed to even begin a mechanistic plausibility assessment. There is currently no actionable evidence to justify moving this candidate forward.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Retrieve confirmed MOA via DrugBank API — currently a **High**-severity data gap (DG002)
- Establish Inclisiran's actual approved indication(s), since this evidence pack has none on record
- **Data-quality flag for this pack**: a separate candidate in the same dataset (rank 8, "aortic malformation," L2/S1) cites two Phase 3 trials (NCT06597019, NCT06597006) — but both trials actually study **pediatric familial hypercholesterolemia**, not aortic malformation. This suggests an indication-linkage mismatch in the evidence pipeline that should be corrected before that candidate (or any other in this pack) is cited as having "L2" support
- If a genuinely evidence-backed repurposing direction is needed for Inclisiran, the familial-hypercholesterolemia-related trials noted above are a more promising starting point than the current top-ranked, zero-evidence prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

