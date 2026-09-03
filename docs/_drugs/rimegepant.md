---
layout: default
title: Rimegepant
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 6
---

# Rimegepant
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

# RIMEGEPANT: Repurposing Evaluation — Insufficient Data to Complete Assessment

## Summary

RIMEGEPANT (DrugBank: DB12457) is a small-molecule drug queried through the TxGNN repurposing pipeline on 2026-03-29.
The current Evidence Pack contains **no TxGNN predicted indications**, no confirmed original indication, and no mechanism of action data.
A full repurposing evaluation cannot be completed at this stage; this report documents the current data state and defines the minimum requirements to proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | No predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions to evaluate |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold — Critical data missing** |

---

## Taiwan Market Information

RIMEGEPANT currently has **no drug licenses registered in Taiwan**. There are no approved products, dosage forms, or indications on record with the TFDA as of the data cutoff (2026-04-20).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack returned zero TxGNN predictions and is missing both original indication data and mechanism of action information, making it impossible to assess repurposing rationale, evidence strength, or safety relevance at this time.

**To proceed, the following is needed:**

- **TxGNN predictions** — Re-run the TxGNN pipeline for DB12457 and confirm that `predicted_indications` is populated before generating a full report
- **Original indication** — Retrieve approved indication(s) from DrugBank or the FDA/EMA label (RIMEGEPANT is commercially available outside Taiwan under brand names including Nurtec ODT and Vydura)
- **Mechanism of action** — Query DrugBank API for MOA; RIMEGEPANT is a CGRP receptor antagonist — this should be confirmable from the public DrugBank record
- **Safety data** — Download and parse the TFDA package insert PDF to extract key warnings and contraindications (Data Gap DG001, severity: Blocking)
- **DDI profile** — Re-query the DDI database; the current query returned `not_found`, which may reflect a data source gap rather than an absence of interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

