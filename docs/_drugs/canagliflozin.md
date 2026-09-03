---
layout: default
title: Canagliflozin
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 0
---

# Canagliflozin
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

# Canagliflozin: Drug Repurposing Evaluation — No TxGNN Prediction Data Available

## One-Sentence Summary

Canagliflozin is a sodium-glucose co-transporter 2 (SGLT2) inhibitor widely used internationally for Type 2 diabetes, heart failure, and chronic kidney disease.
However, **this Evidence Pack contains no TxGNN predicted indications**, and the drug has **no Taiwan regulatory approvals** on record.
A complete repurposing evaluation cannot be generated until prediction data and mechanism of action information are retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan approval on record |
| Predicted New Indication | No prediction data available |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — no predictions, no supporting studies retrieved |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

This Evidence Pack is missing two foundational data elements required for a repurposing evaluation:

1. **No TxGNN predictions** — The `predicted_indications` array is empty. Without a model prediction, there is no candidate indication to evaluate, and no direction for evidence search.

2. **MOA data absent** — The mechanism of action field was not successfully retrieved from DrugBank despite the query returning a result. Without MOA, the biological plausibility of any repurposing hypothesis cannot be assessed.

Canagliflozin is a well-characterised drug internationally (SGLT2 inhibition, renal glucose excretion, haemodynamic and cardioprotective effects), but these facts cannot substitute for the structured pipeline output required to proceed with this workflow.

---

## Clinical Trial Evidence

Currently no related clinical trials are listed in this Evidence Pack.

---

## Literature Evidence

Currently no related literature is listed in this Evidence Pack.

---

## Taiwan Market Information

Canagliflozin has no registered drug authorizations in Taiwan as of this Evidence Pack's data cutoff (2026-04-20).

---

## Safety Considerations

Please refer to the package insert for safety information.

> No warnings, contraindications, or drug interaction data are present in this Evidence Pack. All safety fields returned no data or were not queryable.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack lacks TxGNN prediction output and MOA data — the two inputs that drive every downstream section of a repurposing report. Proceeding without them would require fabricating analytical content, which is not acceptable.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN pipeline** — Confirm whether Canagliflozin was processed through the model; retrieve `predicted_indications` with scores, clinical trial links, and literature PMIDs
- [ ] **Retrieve MOA from DrugBank** — DrugBank query returned a result (query log entry #3) but MOA was not extracted; re-parse the DrugBank record for mechanism, pharmacodynamics, and categories
- [ ] **Download Taiwan package insert** — TFDA query returned a result (query log entry #4); extract warnings, contraindications, and approved indications from the PDF
- [ ] **Re-run DDI query** — Drug interaction query returned `not_found`; verify if this reflects true absence or a query parameter issue
- [ ] **Clarify market scope** — If the target market is Germany (BfArM) rather than Taiwan (TFDA), switch the regulatory query source accordingly; Canagliflozin (Invokana®) is authorised in the EU
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

