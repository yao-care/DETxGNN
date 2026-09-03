---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

> Valsartan is a well-established angiotensin II receptor blocker (ARB); this evidence pack does not include structured data on its originally approved indications, but ARBs are broadly used for hypertension and heart failure.
> The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
> but currently only **0 clinical trials** and **1 indirect publication** (studying a different drug, avosentan) support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (Valsartan is a class-recognized ARB commonly indicated for hypertension/heart failure; no structured `original_indications` or license text was provided) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record (`original_moa: [Data Gap]`). Based on known pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker that suppresses the renin-angiotensin-aldosterone system (RAAS), lowering glomerular capillary pressure and reducing proteinuria — a mechanism broadly associated with renal protection in hypertensive nephropathy.

Malignant hypertension with renal involvement is characterized by markedly elevated angiotensin II activity and RAAS-driven vascular/glomerular injury, making RAAS blockade mechanistically plausible. However, malignant hypertension is a hypertensive emergency requiring rapid blood pressure control; oral ARBs have a slow onset of action and are not first-line for the acute phase, limiting direct applicability.

Importantly, the single literature citation supporting this prediction (PMID 24368192) studies **avosentan**, an endothelin receptor antagonist, not valsartan — it only indirectly supports the general concept that blocking vasoactive/pressor pathways can protect against hypertensive nephropathy in an animal model. No valsartan-specific clinical or preclinical data were retrieved for this indication, so the mechanistic link should be regarded as a class-level hypothesis rather than drug-specific evidence.

*Note: This evidence pack contains 7 TxGNN-predicted indications for valsartan. Two are flagged at "Research Question" stage — this one (rank 1, L4, driven mainly by TxGNN score) and "chronic pulmonary heart disease" (rank 6, L2, supported by multiple completed Phase 3/4 RCTs of sacubitril/valsartan in HFrEF with right-ventricular/pulmonary comorbidity). The rank 6 candidate has a materially stronger clinical evidence base and may warrant separate evaluation.*

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical/Review | Pharmacological Research | Endothelin receptor antagonist (avosentan) — not valsartan — showed renal protection in a hypertensive nephropathy rat model (double transgenic rats overexpressing renin/angiotensinogen) at doses avoiding fluid retention. Supports the general RAAS/vasoactive-pathway nephroprotection concept but provides no direct valsartan data. |

---

## Germany Market Information

Valsartan currently has no recorded marketing authorization in this dataset (market status: **Not marketed**, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A blocking data gap exists — TFDA-equivalent product label warnings/contraindications for valsartan could not be retrieved (DG001), which currently prevents a formal S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a TxGNN score with no clinical trials and a single piece of indirect, non-valsartan-specific literature (L4 evidence). Combined with the drug's "Not marketed" status and a blocking gap in label-level safety data, there is insufficient evidence to proceed toward a safety review at this time.

**To proceed, the following is needed:**
- Product label / official safety warnings and contraindications for valsartan (DG001, Blocking — required before S1 safety evaluation)
- Detailed mechanism of action documentation (DG002)
- Direct preclinical or clinical evidence using valsartan itself (not endothelin antagonists) for hypertensive nephropathy or malignant hypertension
- Consider a separate evaluation track for the "chronic pulmonary heart disease" candidate (rank 6), which has notably stronger evidence (L2, multiple completed Phase 3/4 RCTs of sacubitril/valsartan)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

