---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Unspecified Original Indications to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate (DrugBank DB00563) is a long-established antifolate agent, but this evidence pack does not contain a documented original indication, mechanism of action, or German marketing record for the drug. The TxGNN model predicts a possible new application in **Pulmonary Blastoma**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational prediction with no corroborating clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on record (drug currently not marketed in Germany) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for methotrexate is not available in this evidence pack (`original_moa: Data Gap`). Contextual information drawn from other candidate indications in this same dataset indicates that methotrexate acts as a **dihydrofolate reductase (DHFR) inhibitor**, blocking purine and thymidylate synthesis — a mechanism widely used in hematologic and CNS malignancies (e.g., CNS lymphoma, non-Hodgkin lymphoma, rhabdomyosarcoma) documented elsewhere in this dataset.

For the specific candidate indication evaluated here, **pulmonary blastoma**, no mechanistic rationale, clinical trial, or literature evidence was identified. The evidence pack's own rationale states: *"Only a TxGNN model prediction score is available; there is no clinical trial or literature evidence supporting a mechanistic link or clinical use of methotrexate for this rare pulmonary blastoma."* This means the prediction currently rests entirely on the graph-neural-network signal (Evidence Level L5), with no disease-specific scientific or clinical basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Methotrexate currently holds **no marketing authorization in Germany** in this dataset (0 licenses on record; market status: Not Marketed).

---

## Cytotoxicity

Methotrexate is classified as an antineoplastic/cytotoxic agent (antimetabolite class), based on its established use in multiple chemotherapy regimens referenced throughout this evidence pack (e.g., CNS lymphoma, non-Hodgkin lymphoma, rhabdomyosarcoma, small cell lung carcinoma).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite / Antifolate, DHFR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow standard cytotoxic drug handling regulations (antimetabolite chemotherapy agent) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for pulmonary blastoma is high, but there is no clinical trial or literature evidence specific to this rare tumor type, and drug-level data (MOA, TFDA/BfArM label warnings, contraindications, market status) are all unavailable, blocking any safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/BfArM label warnings and contraindications
- Resolve DG002 (High): confirm methotrexate's mechanism of action via DrugBank or equivalent source
- Conduct a targeted literature/trial search specific to methotrexate in pulmonary blastoma
- Confirm German marketing/licensing status, since 0 authorizations are currently on record

**Note:** This evidence pack also contains other candidate indications for methotrexate with substantially stronger evidence — notably **Hodgkin lymphoma** (Evidence Level L2, "Proceed with Guardrails," multiple historical Phase 2/3 regimens) and **rhabdomyosarcoma** (Evidence Level L2, "Research Question," Phase 2 trial evidence). These may warrant prioritized evaluation over the pulmonary blastoma signal assessed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

