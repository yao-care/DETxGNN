---
layout: default
title: Binimetinib
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 0
---

# Binimetinib
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

# Binimetinib: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Binimetinib (Mektovi) is a selective MEK1/2 inhibitor approved internationally for BRAF V600E/K-mutant unresectable or metastatic melanoma in combination with encorafenib. The current Evidence Pack contains **no TxGNN predicted indications** and critical data gaps in mechanism of action and safety fields, making a complete repurposing assessment impossible at this stage. **Recommended action: Hold — resolve data gaps before proceeding.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600E/K-mutant unresectable or metastatic melanoma (international; no Taiwan license) |
| Predicted New Indication | — (No TxGNN predictions returned) |
| TxGNN Prediction Score | — |
| Evidence Level | — |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Repurposing Prediction is Available

The TxGNN pipeline did not return any predicted indications for binimetinib (DB11967) in this Evidence Pack. Without at least one candidate indication, the core repurposing rationale, clinical trial evidence, and literature evidence sections cannot be populated.

For context: binimetinib is a well-characterised small-molecule that blocks the RAS→RAF→MEK→ERK signalling axis (MAPK pathway). MEK inhibition has been studied in multiple solid tumour types beyond melanoma — including NSCLC, colorectal cancer, pancreatic cancer, and several haematological malignancies — suggesting that valid repurposing candidates likely exist. The absence of predictions most likely reflects a pipeline execution issue rather than a genuine lack of biological signal. Re-running the TxGNN pipeline is the immediate priority.

---

## Taiwan Market Information

Binimetinib is **not marketed in Taiwan**. No TFDA-licensed products, approved indications, or dosage form records are available.

> Note: The query log confirms a TFDA package insert record was retrieved (query ID 4, status: success), but the warning and contraindication fields were not parsed into the Evidence Pack. This data must be extracted before safety screening can proceed.

---

## Cytotoxicity

Binimetinib is an antineoplastic targeted therapy. The following table reflects known pharmacological class properties.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — MEK1/2 kinase inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low to Moderate |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST), CPK, ECG (QTc interval), ophthalmological evaluation (retinal events), blood pressure |
| Handling Protection | Standard oral antineoplastic handling precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

The TFDA package insert query returned a result but key warnings and contraindications were not parsed into this Evidence Pack (Data Gap DG001, severity: Blocking). Drug interaction data was also not found in the DDI database query. These gaps must be resolved before the drug can pass safety screening.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete on two dimensions: the TxGNN model returned zero predicted indications, and both the mechanism of action and safety data fields are unfilled. A responsible repurposing evaluation requires at minimum one candidate indication and a cleared safety profile — neither condition is met here.

**To proceed, the following is needed:**

- **\[Priority 1\]** Re-execute the TxGNN prediction pipeline for binimetinib (DB11967) and confirm the model receives a valid drug embedding
- **\[Priority 2\]** Parse TFDA package insert PDF to extract key warnings, contraindications, and precautions (resolves DG001 — currently Blocking)
- **\[Priority 3\]** Query DrugBank API for full mechanism of action data (resolves DG002)
- **\[Priority 4\]** Supplement with international approval status (FDA/EMA) to provide a complete regulatory context, given the absence of any Taiwan authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

