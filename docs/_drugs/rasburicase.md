---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# RASBURICASE: From Hyperuricemia to — No TxGNN Prediction Available

## One-Sentence Summary

Rasburicase is a recombinant urate-oxidase enzyme used to prevent and treat hyperuricemia associated with tumor lysis syndrome in patients undergoing chemotherapy for hematologic and solid tumor malignancies. The TxGNN model returned **no predicted new indications** for this drug in the current evidence pack, preventing a standard repurposing evaluation. With **zero clinical trials** and **zero publications** linked to a repurposing target, and the drug not marketed in Taiwan, this candidate requires substantial data remediation before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperuricemia in cancer patients undergoing chemotherapy (tumor lysis syndrome prevention) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — no prediction generated) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No repurposing prediction is available for evaluation at this time.

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Rasburicase is a recombinant form of urate oxidase — an enzyme naturally absent in humans — that catalyzes the oxidation of uric acid into allantoin, a far more water-soluble and renally excretable metabolite. This mechanism is entirely metabolic, not cytotoxic, which distinguishes it sharply from antineoplastic agents.

Because the predicted indications array is empty, it is not possible to reason about mechanistic applicability to a new disease target. The absence of a TxGNN output may reflect missing drug–graph linkages, insufficient knowledge graph coverage for this molecule, or upstream data pipeline issues that prevented the model from generating candidates. Resolving the root cause of the missing prediction is the first required remediation step.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a repurposing target.

---

## Literature Evidence

Currently no related literature available for a repurposing target.

---

## Taiwan Market Information

Rasburicase currently holds **no marketing authorizations** in Taiwan. The drug is approved in other major markets under the brand names **Fasturtec** (EU/EMA) and **Elitek** (US/FDA), primarily for hyperuricemia prophylaxis and treatment in adult and pediatric oncology patients.

---

## Safety Considerations

All safety fields in the current evidence pack (key warnings, contraindications, drug interactions) contain no usable data. Based on established pharmacological literature, the following safety signals are known to be clinically significant and **must** be incorporated once formal safety data is retrieved:

- **Hemolysis / Methemoglobinemia**: Rasburicase is absolutely contraindicated in patients with glucose-6-phosphate dehydrogenase (G6PD) deficiency due to the hydrogen peroxide generated during uric acid oxidation, which can trigger severe hemolytic anemia and methemoglobinemia.
- **Anaphylaxis**: As a foreign protein, Rasburicase carries a risk of hypersensitivity reactions including anaphylaxis; pre-treatment testing and emergency management readiness are required.
- **Uric acid sample handling**: Blood samples from patients receiving Rasburicase must be placed immediately on ice to prevent ex-vivo degradation of uric acid, which would falsely lower measured levels.

> Please refer to the package insert (EU SmPC / US Prescribing Information) for full warnings and precautions pending TFDA package insert retrieval.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack for Rasburicase (DB00049) is critically incomplete — it lacks original indication mapping, mechanism of action data, safety data, and most importantly, any TxGNN-predicted new indication — making it impossible to conduct a meaningful repurposing evaluation at this stage.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve TFDA package insert PDF and extract approved indications, key warnings, and contraindications to unblock the safety screening (S1) gate
- **[High — DG002]** Query DrugBank API for full MOA, pharmacodynamics, and drug categories to enable mechanism-based reasoning
- **[Critical]** Investigate why `predicted_indications` is empty — confirm whether the TxGNN knowledge graph contains the Rasburicase node (DB00049) and re-run the prediction pipeline; check for missing drug–disease edges in the KG
- **[High]** Conduct G6PD-deficiency interaction review as a mandatory safety prerequisite for any potential new indication in populations at elevated G6PD-deficiency prevalence
- **[Medium]** Confirm EU/US approval status and indication text from Fasturtec/Elitek SmPC as a reference anchor for the original indication field, which is currently empty
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

