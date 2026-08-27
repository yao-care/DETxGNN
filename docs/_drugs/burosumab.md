---
layout: default
title: Burosumab
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
---

# Burosumab
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

# BUROSUMAB: Repurposing Candidate — No TxGNN Predictions Available

## One-Sentence Summary

BUROSUMAB (DrugBank ID: DB14012) is a biological drug with no TFDA marketing authorization records in Taiwan.
The current Evidence Pack contains **no TxGNN-predicted indications**, making a formal repurposing evaluation impossible at this stage.
Two blocking data gaps — mechanism of action and package insert safety data — must be resolved before this candidate can advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no TFDA authorization records) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the TxGNN pipeline generated no predicted indications for this candidate. Without a target indication, mechanistic plausibility analysis cannot be conducted. The sections below document the two blocking gaps preventing this evaluation from moving forward.

**Gap 1 — Mechanism of Action (MOA) · Severity: High**
Without MOA data, it is not possible to assess whether BUROSUMAB's pharmacological activity is relevant to any candidate new indication. Remediation: query DrugBank API for DB14012 and extract the mechanism of action field.

**Gap 2 — Package Insert Safety Data · Severity: Blocking**
Without TFDA-sourced warnings and contraindications, the candidate cannot pass initial safety screening, which is a prerequisite for all downstream evaluation steps. Remediation: download and parse the TFDA package insert PDF for BUROSUMAB.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication available to search against.

---

## Literature Evidence

Currently no related literature available — no predicted indication available to search against.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for BUROSUMAB is structurally incomplete: the TxGNN pipeline produced no predicted indications, and two data gaps classified as Blocking and High severity prevent the evaluation from proceeding at any stage.

**To proceed, the following is needed:**
- Re-run the TxGNN prediction pipeline for BUROSUMAB (DB14012) to generate candidate disease indications
- Retrieve mechanism of action data via the DrugBank API (DB14012)
- Download and parse the TFDA package insert PDF to extract warnings, contraindications, and dosing safety information
- Conduct drug-drug interaction screening once basic safety data is confirmed
- Re-issue the Evidence Pack and re-trigger report generation after the above gaps are resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

