---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 0
---

# Bortezomib
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

# Bortezomib: Drug Repurposing Evaluation — Data Collection Pending

## One-Sentence Summary

Bortezomib (DB00188) is a known antineoplastic proteasome inhibitor currently not registered in Taiwan.
The TxGNN prediction pipeline returned **no predicted indications** in this evaluation run,
and critical data — including original indication records, mechanism of action, and safety profile — remain outstanding and must be collected before repurposing analysis can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| TxGNN Predicted Indication | No prediction returned |
| Evidence Level | L5 — pipeline output pending; no actual studies available for evaluation |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on pharmacological class recognition, Bortezomib is a proteasome inhibitor in the antineoplastic category, but the Evidence Pack contains no original indication records and no MOA data. Without these inputs, the TxGNN knowledge graph cannot anchor the drug node to any disease trajectory, which likely explains the empty prediction output.

No mechanistic or indication-level analysis can be conducted at this stage. Once the original indication and MOA are retrieved from DrugBank and the TFDA package insert, the prediction pipeline should be re-run to generate a valid candidate indication list.

---

## Cytotoxicity

Bortezomib is a known antineoplastic agent (proteasome inhibitor). This section is included accordingly.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Proteasome inhibitor |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications, and all three critical data layers — original indication, mechanism of action, and safety profile — are currently unavailable. No repurposing evaluation can be completed in this state.

**To proceed, the following is needed:**

- **Original indication**: Download and parse TFDA package insert PDF to extract approved indications
- **Mechanism of action**: Query DrugBank API (DB00188) to obtain MOA, pharmacodynamics, and drug categories
- **Safety data**: Extract key warnings and contraindications from TFDA package insert
- **TxGNN re-run**: Once drug metadata is complete, re-execute the prediction pipeline to generate candidate indications
- **DDI analysis**: Run drug–drug interaction query after base drug profile is established
- **Taiwan registration**: Verify whether any import or hospital-use exemption pathways apply, given zero current authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

