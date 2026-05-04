---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: ALS Treatment — No TxGNN Repurposing Prediction Available

## One-Sentence Summary

Riluzole is an established treatment for Amyotrophic Lateral Sclerosis (ALS), acting as a glutamate release inhibitor with neuroprotective properties.
However, this Evidence Pack contains **no TxGNN prediction data** and **no predicted indications**, making it impossible to conduct a full repurposing evaluation at this time.
Multiple blocking data gaps — including missing original indication records, MOA data, and safety information — must be resolved before this assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in this Evidence Pack (general knowledge: ALS / Motor Neurone Disease) |
| Predicted New Indication | **Not available** — `predicted_indications` array is empty |
| TxGNN Prediction Score | N/A |
| Evidence Level | Cannot be determined |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Prediction Data Is Unavailable

The Evidence Pack for Riluzole (DrugBank: DB00740) was generated with significant data gaps. Specifically:

- `predicted_indications` is an **empty array** — the TxGNN pipeline either did not run for this candidate or returned zero predictions.
- `original_indications` is also an **empty array** — the TFDA query returned 0 results, which is consistent with the drug being **not marketed in Taiwan/Germany**.
- `original_moa` is flagged as `[Data Gap]` — the DrugBank query logged a successful retrieval (`result_count: 1`) but no MOA was mapped into the output schema.

From general pharmacological knowledge: Riluzole (Rilutek®) is approved in the EU and US for **ALS/MND**. Its mechanism involves inhibition of presynaptic glutamate release and blockade of voltage-gated sodium channels, reducing excitotoxic neuronal damage. This context is provided for background only and does **not** substitute for a properly populated Evidence Pack.

Currently, detailed mechanism of action data is not available in this pack. Based on known information, Riluzole belongs to the benzothiazole class and its efficacy in ALS has been proven clinically; a properly populated MOA field would be needed to assess mechanistic applicability to any new indication.

---

## Germany Market Information

No authorisations found. Riluzole has **0 registered licenses** in the queried market. This section cannot be populated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields — key warnings, contraindications, and DDI — returned `[Data Gap]` or `not_found`. The TFDA package insert query did log a success (`result_count: 1`), suggesting source data exists but was not parsed into the Evidence Pack schema.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no TxGNN predicted indications, no original indication records, no MOA, and no safety data — making any repurposing evaluation premature and potentially misleading.

**To proceed, the following is needed:**

| Priority | Gap ID | Item | Action Required |
|----------|--------|------|-----------------|
| 🔴 Blocking | DG001 | TFDA/BfArM package insert warnings & contraindications | Parse the already-retrieved PDF (query log ID 4, `result_count: 1`) into the safety schema |
| 🔴 Blocking | — | `predicted_indications` is empty | Re-run TxGNN prediction pipeline for DB00740; verify input node mapping |
| 🟠 High | DG002 | MOA (mechanism of action) | DrugBank returned a result (query log ID 3, `result_count: 1`); extract `mechanism_of_action` field from API response |
| 🟠 High | — | `original_indications` | Riluzole is not marketed in Taiwan/Germany — source EU SmPC from EMA or FDA label to populate this field |
| 🟡 Medium | — | DDI data | Expand DDI query to DrugBank or credible interaction database; current result is `not_found` |

Once these gaps are resolved and TxGNN produces at least one scored indication, this report should be regenerated using Evidence Pack v5+.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

