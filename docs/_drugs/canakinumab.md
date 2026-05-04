---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: Evaluation Incomplete — No TxGNN Prediction Available

## One-Sentence Summary

Canakinumab (DB06168, brand: Ilaris) is a fully human anti–interleukin-1β (IL-1β) monoclonal antibody widely used in autoinflammatory conditions.
The current Evidence Pack contains **no TxGNN predicted indications** and multiple blocking data gaps, making a complete repurposing evaluation impossible at this stage.
**Immediate data remediation is required before this candidate can advance.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None — TxGNN results not loaded |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions available |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

The Evidence Pack for Canakinumab (DB06168) is missing inputs at two levels:

**1. No repurposing target identified**
The `predicted_indications` array is empty. Without a TxGNN-predicted indication, there is no repurposing hypothesis to evaluate, and the core structure of this report — mechanistic plausibility, clinical trial evidence, and literature support — cannot be assembled.

**2. Drug-level data gaps block safety and mechanism review**

| Gap ID | Item | Severity | Impact |
|--------|------|----------|--------|
| DG001 | TFDA package insert (warnings / contraindications) | **Blocking** | Safety pre-screening (S1) cannot be completed |
| DG002 | Mechanism of action (MOA) | High | Mechanistic plausibility analysis blocked |

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, Canakinumab is an anti-IL-1β biologic; its efficacy in autoinflammatory diseases has been established, and its anti-inflammatory mechanism is mechanistically relevant to a broad range of inflammatory and metabolic conditions. However, a formal MOA-to-new-indication mapping cannot be generated without confirmed DrugBank data in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No repurposing candidate has been identified by TxGNN, and two blocking/high-severity data gaps prevent both safety and mechanistic evaluation. The candidate cannot advance until the Evidence Pack is completed and re-run.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** for DB06168 to generate `predicted_indications` entries with scores, clinical trials, and literature
- **Retrieve MOA from DrugBank API** (DG002 remediation) — query `/drugs/DB06168` for `mechanism-of-action`, `pharmacodynamics`, and `targets`
- **Download and parse TFDA package insert PDF** (DG001 remediation) — extract warnings, contraindications, and special population restrictions
- **Re-generate Evidence Pack** with all inputs confirmed before initiating the next evaluation cycle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

