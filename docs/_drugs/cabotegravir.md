---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 5
---

# Cabotegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cabotegravir: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), approved internationally for HIV-1 treatment (in combination with rilpivirine) and HIV pre-exposure prophylaxis (PrEP).
The current Evidence Pack contains **no TxGNN-predicted new indications**, and critical data fields — including mechanism of action, safety warnings, and contraindications — are unavailable.
A complete repurposing evaluation **cannot be completed** until these gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (treatment & PrEP) — based on international approvals; not reflected in Evidence Pack |
| Predicted New Indication | No prediction available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction only; no repurposing evidence provided |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why a Full Evaluation Cannot Be Completed

The Evidence Pack for Cabotegravir (DB11751) is missing two categories of blocking data:

**1. No TxGNN-predicted indications**
The `predicted_indications` array is empty. Without a candidate target disease from the model, there is no repurposing hypothesis to evaluate. It is unclear whether this reflects a model output with no high-confidence predictions, or a data pipeline gap where predictions were not retrieved.

**2. Missing mechanism of action (MOA)**
The `original_moa` field is marked as a data gap. From publicly available sources, Cabotegravir is known to act as an INSTI — it blocks the HIV integrase enzyme from inserting viral DNA into the host genome. However, since this has not been confirmed through the designated data source (DrugBank API), it cannot be formally cited in this evaluation per the protocol rules.

**3. No safety data**
Key warnings and contraindications are both listed as data gaps. Drug–drug interaction queries returned no results. Without safety information, even a preliminary safety screen (S1 assessment) cannot proceed.

---

## Taiwan Market Information

Cabotegravir currently holds **no regulatory authorizations** in Taiwan. There are no licensed products, no approved dosage forms, and no approved indications on record.

> **Note:** Internationally, Cabotegravir is marketed as **Cabenuva** (with rilpivirine, long-acting injectable for HIV-1 treatment) and **Apretude** (long-acting injectable for PrEP). These are not reflected in the Taiwanese regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in the current Evidence Pack — including key warnings, contraindications, and drug interactions — are unavailable.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack lacks the minimum required data to support any repurposing recommendation — there are no TxGNN predictions, no MOA data, and no safety information. Proceeding to evaluation without these inputs would produce unreliable conclusions.

**To proceed, the following is needed:**

1. **Re-run TxGNN prediction pipeline** — confirm whether the empty `predicted_indications` is a true model output (no confident hits) or a retrieval failure; retrieve and load results
2. **Retrieve MOA from DrugBank API** (DB11751) — confirm integrase inhibitor mechanism and target pathways
3. **Download and parse TFDA package insert PDF** — extract key warnings and contraindications to enable S1 safety screening
4. **Re-query DDI database** — current result is `not_found`; verify whether this is due to drug name formatting (try "cabotegravir", "CAB", "GSK1265744") or a genuine absence of interaction data
5. **Clarify scope** — if TxGNN returns no predictions after re-run, determine whether this candidate should be retired from the repurposing pipeline or flagged for manual literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

