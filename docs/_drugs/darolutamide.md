---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 3
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Darolutamide is a second-generation androgen receptor (AR) antagonist originally used for prostate cancer.
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
> but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis finds no known pharmacological basis for this link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (inferred from AR-antagonist mechanism described in evidence pack; not present as a structured field — see Data Gap DG002) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for darolutamide is flagged as a data gap (DG002) in this evidence pack. Based on the mechanistic rationale text supplied alongside the predictions, darolutamide is described as a second-generation androgen receptor (AR) antagonist that acts on the AR signaling pathway in prostate cancer.

For the top-ranked prediction, Homozygous Familial Hypercholesterolemia, the core pathology is a defect in the LDL receptor (LDLR) gene causing impaired LDL clearance — a lipid-metabolism pathway with no established mechanistic overlap with AR signaling. The evidence pack itself states that this high TxGNN score likely reflects an indirect or noisy connection in the knowledge graph (e.g., a shared metabolic-enzyme node) rather than a genuine pharmacological rationale.

The two lower-ranked candidates show a similar pattern: multiple endocrine neoplasia is driven by MEN1/RET mutations unrelated to AR signaling, and HIV-associated wasting syndrome is more plausibly linked to AR *agonists* (e.g., testosterone, oxandrolone) rather than an AR antagonist like darolutamide, whose pharmacological direction runs counter to the therapeutic need. None of the three predictions currently have a defensible mechanistic basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM label warnings and contraindications are flagged as a Blocking data gap — DG001 — meaning this candidate cannot yet advance to a formal S1 safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications lack a coherent mechanistic rationale, and the top-ranked candidate (HoFH) has zero supporting clinical trials or literature. Combined with a Blocking data gap on TFDA label safety information (DG001), there is currently no basis to advance this candidate past preliminary screening.

**To proceed, the following is needed:**
- Confirmed darolutamide MOA and DrugBank categorization (resolve DG002)
- TFDA/BfArM label warnings and contraindications (resolve DG001, required before any S1 safety review)
- Independent literature or preclinical search specifically for AR-pathway involvement in HoFH, MEN, or HIV-wasting pathophysiology to validate or refute the TxGNN signal
- If no supporting mechanistic or clinical evidence emerges, treat these predictions as knowledge-graph noise and deprioritize
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

