---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using no specialized skill here — this is a direct templated report-generation task with an explicit format already specified in the prompt.

# Selpercatinib: From RET-Altered Cancers to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor originally used for RET fusion/mutation-positive non-small cell lung cancer (NSCLC) and medullary thyroid carcinoma (MTC). The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but this direction is currently supported by **0 clinical trials** and **no literature directly addressing this indication** — the available publications concern the drug's original oncology use and safety profile only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RET fusion/mutation-positive NSCLC and medullary thyroid carcinoma (per repurposing rationale; not confirmed via formal license data) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is not available — this is a documented data gap (DG002, High severity). Based on the available repurposing rationale, selpercatinib is a highly selective RET kinase inhibitor, approved for RET fusion/mutation-positive tumours, and its efficacy in NSCLC and MTC is well established.

The link between RET signalling and pulmonary vascular remodeling is only loosely supported: scattered basic-science literature has noted RET expression in vascular smooth muscle cells, but there is no validated mechanistic pathway connecting RET kinase inhibition to therapeutic benefit in pulmonary hypertension. The high TxGNN score most likely reflects indirect graph-embedding proximity between RET–oncology–vascular endothelium nodes in the knowledge graph, rather than direct pathophysiological evidence.

Given the absence of any preclinical, clinical, or case-based support specific to pulmonary hypertension, this prediction should be treated as hypothesis-generating only, not as a clinically actionable signal at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Retrospective safety comparison | Frontiers in Pharmacology | Compared adverse event profiles between pralsetinib and selpercatinib using FDA FAERS data; not related to pulmonary hypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective analysis (RET+ NSCLC) | Therapeutic Advances in Medical Oncology | Real-world efficacy of selpercatinib in RET fusion-positive NSCLC patients treated through an access program |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report (MEN2B/MTC) | Cureus | Case of metastatic medullary thyroid carcinoma in MEN2B with RET M918T mutation, discussing long-term management and targeted therapy |

**Note:** None of the retrieved literature directly addresses pulmonary hypertension; all three publications relate to the drug's original oncology indications or its safety profile.

---

## Germany Market Information

No marketing authorizations found — selpercatinib is currently **not marketed** in Germany (0 authorizations on record).

---

## Cytotoxicity

Selpercatinib is a targeted RET kinase inhibitor used for RET-altered cancers (NSCLC, MTC), and is therefore reviewed under this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA/BfArM label data is flagged as a blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the evidence level is L5 — model prediction only, with no clinical trials and no literature specific to pulmonary hypertension. The mechanistic link between RET inhibition and pulmonary vascular disease is speculative and unvalidated, and the drug is not currently marketed in Germany, so no real-world safety or regulatory context exists to support further evaluation.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism of action data (DG002)
- Preclinical or mechanistic studies specifically examining RET signalling in pulmonary vascular remodeling
- At least one case report, observational study, or early-phase trial directly addressing selpercatinib in pulmonary hypertension before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

