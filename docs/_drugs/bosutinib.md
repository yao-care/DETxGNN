---
layout: default
title: Bosutinib
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 0
---

# Bosutinib
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

# BOSUTINIB: Drug Repurposing Evaluation — No Predictions Available

## One-Sentence Summary

BOSUTINIB (DB06616) is a Bcr-Abl/Src tyrosine kinase inhibitor, currently not marketed in Taiwan and with no TxGNN predicted indications present in this Evidence Pack.
Critical data items — including mechanism of action, safety warnings, and contraindications — are all flagged as gaps, making a complete repurposing evaluation impossible at this stage.
This report documents the current data status and outlines remediation steps before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in Evidence Pack |
| Predicted New Indication | None available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction data absent |
| Taiwan Market Status | Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predicted indication is present in this Evidence Pack (`predicted_indications: []`). Therefore, a mechanistic rationale linking BOSUTINIB to a new disease target cannot be constructed from the available data.

Currently, detailed mechanism of action data is not available (`original_moa: "[Data Gap]"`). Although BOSUTINIB is publicly known as a Bcr-Abl/Src dual kinase inhibitor used in Philadelphia chromosome-positive chronic myelogenous leukemia (CML), this information was not captured in the structured Evidence Pack and cannot be used as a formal input for this evaluation without verification.

The DrugBank query returned one result (query log ID 3, status: success), and the TFDA package insert query also returned one result (query log ID 4, status: success). Both data sources exist but their content was not parsed into the structured fields. Completing the data extraction from these two sources is the highest-priority remediation step before this evaluation can advance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any predicted indication (no TxGNN prediction available).

---

## Literature Evidence

Currently no related literature available for any predicted indication (no TxGNN prediction available).

---

## Taiwan Market Information

BOSUTINIB has **0 authorizations** in Taiwan. There are no licensed products to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The TFDA package insert query returned a result (query log ID 4), but safety data was not parsed into the structured fields. Key warnings, contraindications, and drug interaction data are all currently marked as gaps. No drug interactions were found via the DDI query source (query log ID 2, status: not_found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN predicted indications and no structured safety or mechanism data, making it impossible to perform a meaningful repurposing evaluation at this time. All three critical evaluation components — target indication, mechanistic rationale, and safety profile — are absent.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Extract and parse TFDA package insert warnings and contraindications from the already-retrieved PDF (query log ID 4 confirms the document exists)
- **[High — DG002]** Extract mechanism of action (MOA) from the DrugBank record already retrieved (query log ID 3 confirms result_count = 1)
- **[Critical]** Re-run TxGNN prediction pipeline for BOSUTINIB to generate `predicted_indications`; current empty array suggests the drug may not have been included in the prediction run or results were not mapped correctly
- Confirm whether "not marketed in Taiwan" reflects a regulatory decision or simply that no application has been submitted, as this affects the eventual market entry pathway assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

