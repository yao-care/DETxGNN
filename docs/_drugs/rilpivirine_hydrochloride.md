---
layout: default
title: Rilpivirine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 0
---

# Rilpivirine Hydrochloride
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

# Rilpivirine Hydrochloride: Drug Repurposing Evaluation — Predictions Not Yet Available

## One-Sentence Summary

Rilpivirine Hydrochloride is a non-nucleoside reverse transcriptase inhibitor (NNRTI) belonging to the antiretroviral drug class, with established use in HIV-1 infection treatment in global markets. The current Evidence Pack contains **no TxGNN-predicted new indications**, and the drug is **not marketed in Taiwan** with zero TFDA authorizations on record. Due to critical data gaps in mechanism of action, safety data, and model output, a complete repurposing evaluation cannot be generated at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not listed in Evidence Pack (NNRTI class; globally indicated for HIV-1 infection) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | — |
| Evidence Level | L5 — No model output available |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indications were returned by the TxGNN pipeline for this drug in the current Evidence Pack. A mechanistic rationale for a repurposing hypothesis therefore cannot be presented.

Detailed mechanism of action data is not available in this evidence pack. Based on pharmacological class, Rilpivirine Hydrochloride is known globally as an NNRTI that selectively inhibits HIV-1 reverse transcriptase by binding to an allosteric site, blocking viral RNA-dependent and DNA-dependent DNA polymerase activity. Its established clinical role is in HIV-1 infection — typically as part of complete regimens (e.g., combined with emtricitabine/tenofovir). However, since neither `original_moa` nor `original_indications` fields were populated in this Evidence Pack, this background cannot be formally confirmed from supplied data.

Repurposing hypotheses for NNRTIs have appeared in oncology and immunology literature (e.g., reverse transcriptase inhibition of endogenous retroelements in cancer), but without a TxGNN prediction score to anchor the analysis, any further discussion would be speculative and is therefore omitted.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing all components required for a repurposing evaluation: no TxGNN-predicted indications, no mechanism of action, no safety or contraindication data, and no Taiwan regulatory approvals. Proceeding to any clinical or regulatory assessment is not possible in this state.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** — the predicted_indications array is empty; confirm whether the model was run and returned no results, or whether the pipeline failed upstream
- **Extract MOA from DrugBank** — the query log shows DrugBank returned 1 result (`result_count: 1`); this data was not propagated into the `drug.original_moa` field and should be retrieved
- **Extract safety warnings from TFDA package insert** — the query log shows `tfda_package_insert` returned 1 result (`result_count: 1`); key_warnings and contraindications should be populated from this source
- **Populate original_indications** — the field is empty despite DrugBank and package insert data being available; align with retrieved regulatory text
- **Confirm Taiwan market status** — the drug is marketed globally under brand names (e.g., Edurant, Odefsey, Juluca); investigate whether it is registered in Taiwan under a combination product or different INN spelling
- **Address DG001 (Blocking)** — TFDA package insert warnings/contraindications must be resolved before any safety tier assessment can begin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

