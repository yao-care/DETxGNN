---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# RISANKIZUMAB: Evidence Pack Incomplete — Evaluation Pending

## One-Sentence Summary

Risankizumab is a humanized monoclonal antibody targeting the IL-23 pathway, with established use in immune-mediated inflammatory conditions such as plaque psoriasis and inflammatory bowel disease.
However, this Evidence Pack (v4, data cutoff 2026-04-20) contains **no TxGNN predicted indications**, **no mechanism of action data**, and **no safety profile data** — the report cannot proceed to a full repurposing evaluation in its current state.
Three critical data gaps have been identified, two of which are rated **Blocking** or **High** severity, preventing standard scoring and decision-making.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current Evidence Pack |
| Predicted New Indication | No predictions generated — see Data Gap section |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (Model prediction only — not yet available) |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** — insufficient data to evaluate |

---

## Why This Report Cannot Proceed to Full Evaluation

The Evidence Pack for RISANKIZUMAB is currently missing the two foundational inputs required for a drug repurposing report:

**1. TxGNN Predicted Indications (Empty)**
The `predicted_indications` array is empty. Without a predicted target indication, it is not possible to identify relevant clinical trials, literature, or a mechanistic rationale to evaluate. This may indicate the TxGNN pipeline has not yet been run for this candidate, or that predictions were filtered out upstream.

**2. Mechanism of Action (Data Gap DG002 — High Severity)**
The `original_moa` field is marked as a data gap. The MOA is required to assess whether the drug's pharmacological mechanism is plausibly applicable to any new indication. Remediation: query DrugBank API for DB14762.

**3. Safety Warnings and Contraindications (Data Gap DG001 — Blocking Severity)**
Both `key_warnings` and `contraindications` contain only `[Data Gap]`. This is classified as **Blocking** severity — the evaluation cannot pass the S1 safety screening without this information. Remediation: download and parse the TFDA package insert PDF.

---

## Taiwan Market Information

No authorizations found for RISANKIZUMAB in the Taiwan TFDA database as of 2026-04-20. No product entries to display.

> **Note for context:** Risankizumab (brand name Skyrizi®, AbbVie) is approved in multiple major markets (FDA, EMA, PMDA) for plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis, but this information is not reflected in the current Evidence Pack and therefore cannot be used as the basis for a formal evaluation under this pipeline.

---

## Safety Considerations

All safety fields in the current Evidence Pack are marked as data gaps. Please refer to the official package insert and the TFDA drug information database for warnings, contraindications, and drug interactions before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for RISANKIZUMAB (DB14762) is structurally incomplete — both the TxGNN prediction output and the core safety/MOA data are absent, making it impossible to perform a meaningful repurposing evaluation or evidence scoring at this time.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN pipeline** for DB14762 to generate predicted indications with scores; verify the prediction output was not silently filtered
- [ ] **Resolve DG002 (Blocking):** Download and parse the TFDA package insert PDF to extract key warnings and contraindications — required to pass S1 safety screening
- [ ] **Resolve DG001 (High):** Query DrugBank API for `DB14762` to retrieve the mechanism of action (p19/IL-23 subunit inhibition) and pharmacological categories
- [ ] **Confirm pipeline inputs:** The `meta.inputs_received` field lists only `"drugbank"` — verify whether TFDA, clinical trial (ClinicalTrials.gov), and literature (PubMed) sources were queried and returned empty, or were never invoked
- [ ] **Re-submit Evidence Pack** once the above items are resolved; this report should be regenerated at v5 or later
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

