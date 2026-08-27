---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

# Remdesivir: Drug Repurposing Evaluation (Data Insufficient)

## One-Sentence Summary

Remdesivir (DB14761) is a broad-spectrum antiviral agent recognized internationally for COVID-19 treatment.
This Evidence Pack, however, **contains no TxGNN predicted indications** and is missing critical data inputs — including mechanism of action, safety warnings, and Taiwan regulatory records.
A complete repurposing evaluation **cannot be rendered** at this stage; the report below reflects only what is currently available.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (model prediction pipeline incomplete) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are present in `predicted_indications`. Without a target indication, no mechanistic bridge or repurposing rationale can be constructed.

The mechanism of action field is listed as a data gap (DG002, High severity). Remdesivir is broadly understood to act as an RNA-dependent RNA polymerase (RdRp) inhibitor; however, this has **not been confirmed by the current data inputs** and should not be treated as verified for this report.

Until both TxGNN predictions and MOA data are available, the biological plausibility of any candidate new indication cannot be assessed.

---

## Taiwan Market Information

Remdesivir currently holds **no approved licenses in Taiwan** (TFDA query returned 0 results). There are no dosage forms or approved indications on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The TFDA package insert query (query_log ID 4) returned a result, but the safety fields — warnings, contraindications, and drug interactions — remain unpopulated in this Evidence Pack. This is identified as a Blocking data gap (DG001) that must be resolved before any safety pre-assessment can begin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline has not produced any candidate indications for Remdesivir, and two critical data gaps (MOA and TFDA safety data) remain unresolved. There is no repurposing signal to evaluate at this time.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve TFDA package insert PDF and parse warnings/contraindications before entering safety pre-assessment
- **[DG002 — High]** Query DrugBank API to obtain confirmed mechanism of action data; the current DrugBank query (query_log ID 3) returned 1 record but did not populate the MOA field — investigate extraction logic
- **Re-run TxGNN prediction pipeline** to generate `predicted_indications`; without predictions, no repurposing target exists
- Once a target indication is confirmed, collect clinical trial and literature evidence accordingly
- Conduct drug interaction profiling (DDI query returned 0 results; verify whether this reflects true absence or a query scope issue)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

