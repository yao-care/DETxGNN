---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine (DB01101): Drug Repurposing Evaluation — Insufficient Data to Proceed

## One-Sentence Summary

Capecitabine (DB01101) is a fluoropyrimidine antineoplastic agent. However, this Evidence Pack contains no TxGNN predicted indications, no confirmed mechanism of action data, and no Taiwan regulatory records — making a complete repurposing evaluation impossible at this stage. **The pipeline must be re-run and data gaps resolved before a repurposing direction can be assessed.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (no predictions returned; no supporting studies retrievable) |
| Taiwan Market Status | Not marketed (0 TFDA authorizations found) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predicted indications were returned in this Evidence Pack. Without at least one candidate indication, it is not possible to assess mechanistic plausibility, retrieve targeted clinical trial evidence, or evaluate clinical feasibility. This section will be completed once the prediction pipeline returns valid output.

Additionally, detailed mechanism of action data is not available in the current Evidence Pack. Capecitabine is structurally classifiable as a fluoropyrimidine, but no DrugBank MOA record was successfully loaded into this pack, so mechanistic analysis cannot be formally grounded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. *(This section requires at least one predicted indication to define the search scope.)*

---

## Literature Evidence

Currently no related literature available. *(This section requires at least one predicted indication to define the search scope.)*

---

## Cytotoxicity

Capecitabine falls within the fluoropyrimidine class of conventional cytotoxic chemotherapy, satisfying criterion 3 of the antineoplastic determination rules. This section is therefore included.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic drug handling regulations |

> Note: Detailed toxicity parameters (myelosuppression grade, emetogenicity level) could not be populated because the DrugBank toxicity fields and TFDA package insert data were not successfully loaded into this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no TxGNN predicted indications, no MOA data, and no Taiwan regulatory safety data are available. There is no repurposing hypothesis to evaluate, and no safety baseline to assess against.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for DB01101 and confirm at least one predicted indication is returned before re-generating this report
- **Resolve DG002 (High severity):** Retrieve MOA from DrugBank API (`/drugs/DB01101`) to enable mechanistic plausibility analysis
- **Resolve DG001 (Blocking severity):** Download and parse the TFDA package insert PDF to populate key warnings and contraindications for the S1 safety screen
- **Verify TFDA query result:** The query returned 0 authorizations for Capecitabine — confirm whether this reflects a genuine absence of TFDA approval or a data pipeline issue (e.g., brand name alias not searched)
- **Re-check DDI source:** The DDI query returned `not_found`; confirm whether this is a database gap or a query parameter error
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

