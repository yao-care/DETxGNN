---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: From Undocumented Original Indication to Bacteroidaceae Infectious Disease

## One-Sentence Summary

> Oritavancin is a lipoglycopeptide antibiotic; its original indication is not documented in this evidence pack, and it is not currently marketed in this jurisdiction.
> The TxGNN model predicts it may be effective for **Bacteroidaceae infectious disease**,
> but **no clinical trials** and **no literature** currently support this direction, and the drug's own mechanism of action argues against it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication data provided (drug not marketed) |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed MOA data is flagged as a data gap, but the evidence pack's own mechanistic rationale is informative: oritavancin is a **lipoglycopeptide** antibiotic that binds the D-Ala-D-Ala terminus of peptidoglycan precursors, inhibiting bacterial cell wall synthesis. This mechanism is only active against **Gram-positive** organisms.

**Bacteroidaceae** are Gram-negative anaerobes whose outer membrane blocks penetration of large glycopeptide molecules — mechanistically, oritavancin should not be active against this pathogen family. The rationale text explicitly labels this a likely **TxGNN false positive**, arising from the drug and disease being graph-adjacent "infectious disease" nodes rather than sharing a real pharmacological mechanism.

The other two candidates in this evidence pack (ophthalmic herpes zoster — a viral infection, and *Mycoplasma pneumoniae* pneumonia — a cell-wall-deficient bacterium) show the same pattern: high TxGNN scores paired with mechanistic incompatibility and zero clinical/literature support. This is not a case of a plausible signal awaiting evidence — the mechanism itself argues against the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Oritavancin is not marketed in this jurisdiction — no authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Bacteroidaceae infectious disease) is mechanistically incompatible with oritavancin's Gram-positive-only spectrum, is unsupported by any clinical trial or literature evidence, and reflects TxGNN's L5 (prediction-only) tier. The two other candidates in this pack show the same pattern of mechanistic implausibility, suggesting a systematic false-positive cluster rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Confirmed MOA and original indication data from DrugBank/regulatory sources (currently marked as data gaps)
- TFDA/regulatory label warnings and contraindications (blocking gap — required before any S1 safety screening)
- Independent microbiological or in-vitro evidence of activity against Bacteroidaceae, if this candidate is to be pursued further
- Given the mechanistic red flags, recommend deprioritizing this candidate in favor of higher-evidence-level predictions elsewhere in the pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

