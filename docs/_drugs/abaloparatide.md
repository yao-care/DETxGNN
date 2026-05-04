---
layout: default
title: Abaloparatide
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 4
---

# Abaloparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# ABALOPARATIDE: Drug Repurposing Evaluation Report

## One-Sentence Summary

Abaloparatide is a synthetic peptide analog of parathyroid hormone-related protein (PTHrP), approved internationally for the treatment of postmenopausal osteoporosis (marketed as Tymlos® in the US). The TxGNN model has **not generated any predicted new indications** for this drug, and the evidence pack contains significant data gaps across regulatory, safety, and mechanistic domains.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in Taiwan (no TFDA licenses); internationally approved for postmenopausal osteoporosis |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | — |
| Evidence Level | N/A — No predictions to evaluate |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There are currently **no TxGNN-predicted indications** for Abaloparatide, so a mechanistic plausibility assessment cannot be performed at this time.

For background: Abaloparatide is a 34-amino-acid synthetic peptide analog of human parathyroid hormone-related protein (PTHrP). It selectively activates the PTH1 receptor in its RG conformation, promoting osteoblast-mediated bone formation while producing a more transient calcemic response compared to teriparatide (PTH 1-34). This anabolic mechanism increases bone mineral density and reduces fracture risk.

Detailed mechanism of action data was not available in this evidence pack (listed as a High-severity data gap). Should TxGNN predictions become available in future iterations, the PTHrP agonist mechanism — with its effects on calcium homeostasis, bone remodeling, and mesenchymal cell signaling — could potentially be relevant to indications beyond osteoporosis.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indications exist; therefore, no indication-specific clinical trial search was performed.

---

## Literature Evidence

Currently no TxGNN-predicted indications exist; therefore, no indication-specific literature search was performed.

---

## Taiwan Market Information

Abaloparatide has **no TFDA-approved licenses** and is **not marketed in Taiwan**. No authorization records are available.

---

## Safety Considerations

> Please refer to the package insert for safety information.
>
> Note: TFDA package insert warnings/contraindications were identified as a **Blocking-severity data gap** (DG001). Drug interaction data was queried but returned no results. Complete safety evaluation cannot proceed until package insert data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no TxGNN-predicted new indications for Abaloparatide at this time, and significant data gaps exist across mechanism of action, regulatory, and safety domains. Without a predicted indication, drug repurposing evaluation cannot proceed.

**To proceed, the following is needed:**
- **TxGNN prediction results**: Re-run or verify the TxGNN model to determine whether any new indications are predicted for Abaloparatide (DB05084)
- **Mechanism of action data (DG002)**: Query DrugBank API for complete MOA, pharmacodynamic targets, and pathway information
- **TFDA package insert (DG001)**: Obtain and parse the package insert for warnings, contraindications, and prescribing information (if applicable from reference country)
- **Regulatory pathway assessment**: Since the drug is not marketed in Taiwan, evaluate whether an international reference (e.g., FDA, EMA) approval dossier can be leveraged for any future repurposing application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

