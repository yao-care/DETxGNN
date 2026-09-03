---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Erdafitinib: From Unspecified Original Indication to Pulmonary Hypertension

## One-Sentence Summary

> Erdafitinib is a pan-FGFR (FGFR1-4) kinase inhibitor; however, its original approved indication is not recorded in the current evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-level hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no original indications recorded in evidence pack (see DG001/DG002) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data for erdafitinib is not available (`original_moa`: Data Gap), and no original indications are recorded in this evidence pack. Based on the mechanistic rationale accompanying the TxGNN prediction, erdafitinib is understood to be a **pan-FGFR (FGFR1-4) inhibitor**. FGF2/FGFR1 signaling has a known role in pulmonary vascular smooth muscle proliferation and vascular remodeling, which is the biological basis the model draws on to link erdafitinib to pulmonary hypertension.

This link, however, is explicitly flagged by the source rationale itself as inferred from **in vitro/animal-model level mechanistic reasoning only** — there is no clinical trial, no observational study, and no published case data connecting erdafitinib to pulmonary hypertension in humans. The high TxGNN score reflects strong embedding-space similarity in the model's knowledge graph, not validated pharmacological evidence.

Without confirmed data on erdafitinib's original approved indication(s), it is also not possible to assess mechanistic continuity between the original and predicted use — this remains a genuine evidence gap rather than a supported hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Erdafitinib currently holds **no market authorization** in this jurisdiction (`market_status`: Not Marketed, `total_licenses`: 0). No product/license records are available to summarize.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug-drug interactions) is currently available for erdafitinib in this evidence pack, and the corresponding local prescribing information could not be sourced (DG001, Blocking severity). Since the drug is not yet marketed in this jurisdiction, safety assessment should rely on internationally published prescribing information (e.g., FDA label) pending confirmation of local regulatory data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pulmonary hypertension) is supported only by theoretical mechanistic reasoning with zero clinical trials and zero literature — this is an L5, S0-stage prediction. Combined with a Blocking-severity gap in local safety/label data (DG001) and a High-severity gap in MOA data (DG002), the candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA/BfArM label data — package insert warnings, contraindications, and DDI profile (resolves DG001)
- Structured MOA and original-indication reference data (resolves DG002)
- Preclinical (animal model) or observational evidence specifically linking erdafitinib to pulmonary vascular remodeling/pulmonary hypertension
- DrugBank category/classification data to determine antineoplastic/cytotoxicity risk profile, which is currently indeterminate from available data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

