---
layout: default
title: Brimonidine Tartrate
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Brimonidine Tartrate
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

# Brimonidine Tartrate: Repurposing Evaluation — TxGNN Prediction Data Unavailable

## One-Sentence Summary

Brimonidine Tartrate is an alpha-2 adrenergic agonist clinically established for reducing intraocular pressure in glaucoma and ocular hypertension.
The current Evidence Pack contains **no TxGNN-predicted new indications**, and critical data fields — including MOA detail, safety warnings, and contraindications — are missing.
A full repurposing evaluation **cannot be completed** at this stage; the report below documents what was retrieved and maps the remaining gaps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular Hypertension (established pharmacological class; not captured in this Evidence Pack) |
| Predicted New Indication | Not available — TxGNN prediction list is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction absent; no supporting studies identified |
| Taiwan Market Status | Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Prediction Cannot Yet Be Assessed

Brimonidine Tartrate belongs to the alpha-2 adrenergic agonist class. Its primary mechanism — selective stimulation of presynaptic and postsynaptic α₂-receptors — reduces aqueous humour production and increases uveoscleral outflow, thereby lowering intraocular pressure. Secondary mechanisms relevant to repurposing (neuroprotection via Bcl-2 upregulation, anti-inflammatory activity, vasoconstriction for dermatological applications such as rosacea) are documented in the literature but are absent from this Evidence Pack's `original_moa` field.

Without a populated `predicted_indications` array from TxGNN, it is not possible to assess mechanistic plausibility for any candidate new indication, nor to select supporting trials or publications. The pipeline appears to have retrieved a DrugBank record (query_log ID 3, status: success) and a TFDA package insert (query_log ID 4, status: success), but neither fed structured data into the Evidence Pack fields. This suggests a downstream parsing or mapping failure rather than a genuine absence of drug information.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available to scope a trial search. No clinical trial evidence can be presented.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available to scope a literature search. No publication evidence can be presented.

---

## Taiwan Market Information

Brimonidine Tartrate holds **zero TFDA authorizations**. The drug is **not marketed in Taiwan**. No license table can be generated.

> Note: Brimonidine is marketed under trade names such as Alphagan® and Mirvaso® in the US, EU, and multiple Asian markets. The TFDA query returned 0 results (query_log ID 1), which may reflect a formulation-specific or brand-name discrepancy rather than global non-approval. A cross-check against alternative spellings (e.g., "Brimonidine," "酒石酸溴莫尼定") is recommended.

---

## Safety Considerations

All safety fields in this Evidence Pack are missing:

- Key warnings: not retrieved
- Contraindications: not retrieved
- Drug-drug interactions: query returned no results (query_log ID 2, status: not_found)

Please refer to the package insert (successfully retrieved per query_log ID 4) and DrugBank record (query_log ID 3) for warnings, contraindications, and interactions. These sources must be parsed and re-ingested before any safety evaluation can proceed.

Known class-level cautions for alpha-2 agonists include: cardiovascular depression, CNS sedation, rebound hypertension on abrupt withdrawal, and risk of severe hypotension when combined with antihypertensives or CNS depressants.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — TxGNN predictions are absent and two blocking data gaps (DG001: safety/warnings, DG002: MOA) remain unresolved. No repurposing hypothesis can be evaluated, and no safety review can be initiated, until these are resolved.

**To proceed, the following is needed:**

1. **Re-run TxGNN inference** for Brimonidine Tartrate and populate `predicted_indications` — confirm that the DrugBank entity ID is correctly mapped (DrugBank ID field is currently null).
2. **Parse the TFDA package insert** (already retrieved, query_log ID 4) to extract structured warnings and contraindications into `safety.key_warnings` and `safety.contraindications`.
3. **Parse the DrugBank record** (already retrieved, query_log ID 3) to extract `original_moa`, categories, and toxicity data.
4. **Verify TFDA search coverage** — re-query with simplified drug name ("Brimonidine") and Chinese INN ("溴莫尼定") to rule out zero-result artifacts.
5. **Re-run DDI query** once DrugBank ID is confirmed, as the current not_found status may stem from a missing identifier.
6. Once the above are resolved, regenerate the Evidence Pack and re-submit for a complete evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

