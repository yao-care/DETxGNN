---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: Drug Repurposing Evaluation — Evidence Pack Incomplete

## One-Sentence Summary

Ravulizumab (DrugBank ID: DB11580) is a drug for which this Evidence Pack contains insufficient data to support a standard repurposing evaluation. The TxGNN model has returned **no predicted indications** for this candidate, and both original indication data and mechanism of action information are absent. A complete evaluation cannot proceed until the data gaps identified below are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No TxGNN prediction returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model returned no output; no supporting studies |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Evaluation Cannot Proceed

This Evidence Pack is missing three components that are each independently required before a repurposing evaluation can be written:

**1. No predicted indication.** The `predicted_indications` field is empty. The TxGNN model did not return a candidate disease for this drug. Without a predicted target indication, there is no repurposing hypothesis to evaluate — the core question of "effective for what new condition?" has no answer.

**2. No original indication on record.** The `original_indications` field is also empty. This prevents establishing the mechanistic baseline — the "from" in the standard repurposing narrative. Without knowing what disease the drug was developed for, relatedness to any new indication cannot be assessed.

**3. Mechanism of action unavailable.** The `original_moa` field returned no data. Mechanistic plausibility — typically the strongest argument for or against repurposing — cannot be evaluated.

Currently, detailed mechanism of action data is not available. Based on known registry information, Ravulizumab is classified under DrugBank ID DB11580, but the specific pharmacological target and pathway data required for this evaluation have not been retrieved.

---

## Taiwan Market Information

Ravulizumab is **not currently approved or marketed in Taiwan**. There are no TFDA-issued drug licenses on record.

| Item | Status |
|------|--------|
| TFDA Market Status | Not marketed |
| Number of Licenses | 0 |
| Dosage Forms Approved | None |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Ravulizumab is missing all three elements required for a repurposing evaluation: a predicted target indication, an original indication baseline, and mechanism of action data. Issuing any recommendation under these conditions would be speculative.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for DB11580 — confirm why `predicted_indications` returned empty (model coverage gap, data pipeline error, or genuine no-prediction result)
- **Retrieve MOA from DrugBank API** (DG002, High severity) — query DrugBank for pharmacological target, mechanism, and drug category for Ravulizumab
- **Download and parse TFDA package insert PDF** (DG001, Blocking severity) — extract approved indications, key warnings, and contraindications for the Taiwan label
- **Clarify original indication** — confirm from DrugBank or EMA/FDA labeling what disease Ravulizumab is currently approved to treat; this anchors the repurposing narrative
- **Re-submit Evidence Pack** once all four items above are resolved; a full L1–L5 evidence evaluation can then be generated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

