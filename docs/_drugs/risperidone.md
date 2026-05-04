---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 6
---

# Risperidone
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

# Risperidone: Evaluation Pending — No Repurposing Prediction Available

## One-Sentence Summary

Risperidone (DB00734) is a well-known atypical antipsychotic commonly used for schizophrenia and related conditions. However, the current Evidence Pack contains **no TxGNN-predicted repurposing indications**, no mechanism of action data, and no safety records — making a substantive repurposing evaluation impossible at this stage. **Immediate data remediation is required before this candidate can advance.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | N/A — No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — currently not even reached) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Evaluation Can Be Performed

The TxGNN prediction pipeline returned **zero predicted indications** for Risperidone in this Evidence Pack version (v4, data cutoff 2026-04-20). This is an upstream pipeline issue rather than a reflection of Risperidone's clinical potential.

Two blocking data gaps have been formally identified:

| Gap ID | Category | Missing Item | Severity | Impact |
|--------|----------|--------------|----------|--------|
| DG001 | Drug Level | Package insert warnings / contraindications | **Blocking** | Cannot perform S1 safety screening |
| DG002 | Drug Level | Mechanism of action (MOA) | High | Cannot perform mechanistic relevance analysis |

Until the TxGNN pipeline produces at least one predicted indication, and until DG001 is resolved, no downstream evaluation (mechanism analysis, clinical trial mapping, or safety profiling) can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this candidate.

*(Prerequisite: TxGNN predicted indication must be available before trial mapping is performed.)*

---

## Literature Evidence

Currently no related literature available.

*(Prerequisite: TxGNN predicted indication must be available before literature search is performed.)*

---

## Taiwan Market Information

Risperidone has **no registered licenses** in the Taiwan market according to the current TFDA query (queried 2026-03-29, result count: 0).

> Note: The TFDA package insert query (query ID 4) returned 1 result — this may indicate a package insert exists for reference purposes even without an active marketing authorization. The package insert should be retrieved and parsed to resolve DG001.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields — key warnings, contraindications, and drug-drug interactions — returned no data in the current Evidence Pack. DDI query status: not found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Risperidone (v4) is structurally incomplete — no TxGNN repurposing predictions were generated, and two high-severity data gaps (DG001, DG002) block safety screening and mechanistic analysis. There is no evaluable repurposing hypothesis at this time.

**To proceed, the following is needed:**

1. **Re-run TxGNN prediction pipeline** for DB00734 and confirm at least one predicted indication is returned
2. **Resolve DG001** — Download and parse the TFDA package insert PDF (1 document found in query log) to extract warnings and contraindications
3. **Resolve DG002** — Query DrugBank API for Risperidone's full mechanism of action, pharmacological class, and targets
4. **Re-run DDI query** — Current status is `not_found`; verify query parameters and retry
5. **Re-generate Evidence Pack** (v5+) once the above data is available, then re-submit for evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

