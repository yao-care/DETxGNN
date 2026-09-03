---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Undocumented Original Indication to Acute Lymphoblastic Leukemia

## One-Sentence Summary

> This evidence pack contains no confirmed original indication or mechanism-of-action data for sotatercept (DrugBank ID DB12118).
> The TxGNN model's top prediction is **Acute Lymphoblastic Leukemia**, with a score of **99.78%**,
> but this is supported by **zero clinical trials** and **zero publications** — the prediction is model-output only (L5), and the drug's own rationale text flags it as a low-plausibility, database-link-type inference rather than a mechanistically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not marketed, no license records) |
| Predicted New Indication | Acute Lymphoblastic Leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sotatercept is not available in this evidence pack (`original_moa` is empty). Based on the rationale text accompanying the predictions, sotatercept is described as an **activin receptor IIA-Fc fusion protein (ligand trap)** that inhibits activin/GDF/BMP signaling within the TGF-β superfamily. This pathway has known roles in hematopoietic differentiation and the bone marrow microenvironment — but the rationale for the top-ranked prediction (Acute Lymphoblastic Leukemia) explicitly states there is **no known direct mechanistic link** to leukemic cell proliferation, and characterizes the high TxGNN score as a database-connectivity artifact rather than a biologically grounded signal.

Because both the original indication and the mechanism of action are undocumented here, the relationship between "what sotatercept currently treats" and "what it is predicted to treat" cannot be evaluated. Among the ten ranked predictions, the model's own annotations note that **drug-induced osteoporosis** (rank 4) has comparatively stronger mechanistic plausibility, since activin receptor IIA ligand traps (a class that includes luspatercept) are known to affect bone metabolism — but even this indication has no clinical trial or literature support and would require preclinical validation before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Sotatercept is currently **not marketed** in this jurisdiction (`market_status: 未上市`), with **0 authorizations** on file. No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM package insert warnings and contraindications are flagged as a Blocking data gap (DG001) — this is required before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN predictions for sotatercept are Evidence Level L5 (model prediction only, no clinical trials or literature), and the system's own scoring recommends "Hold" across the board. The top-ranked indication (Acute Lymphoblastic Leukemia) is explicitly flagged in its own rationale as lacking biological plausibility and being a database-link-type inference rather than a supported hypothesis.

**To proceed, the following is needed:**
- Confirmed original indication(s) and regulatory history for sotatercept (currently blank)
- Mechanism-of-action data via DrugBank API (DG002, High severity)
- TFDA/BfArM package insert (warnings, contraindications) to unblock S1 safety pre-assessment (DG001, Blocking)
- If pursuing the osteoporosis signal (rank 4, comparatively stronger mechanistic rationale via the activin-receptor/bone-metabolism pathway): preclinical bone-density data before any clinical evaluation
- At minimum, preliminary literature or preclinical evidence for any candidate indication before moving past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

