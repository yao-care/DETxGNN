---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mecasermin: From Unspecified Original Indication to Monosomy X (Turner Syndrome)

## One-Sentence Summary

> Mecasermin is a recombinant human insulin-like growth factor 1 (IGF-1) analogue; the current evidence pack does not contain data on its original approved indication or detailed mechanism of action.
> The TxGNN model predicts potential relevance to **Monosomy X (Turner Syndrome)**,
> but this is currently a **model-prediction-only** finding, with **0 clinical trials** and **0 publications** identified in support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license/indication data in evidence pack) |
| Predicted New Indication | Monosomy X (Turner Syndrome) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mecasermin is not available in this evidence pack. Based on information embedded in the related prediction rationale (see rank-3 candidate, "growth hormone insensitivity syndrome"), mecasermin is a recombinant human IGF-1 product, and its established pharmacological role is to supply IGF-1 directly downstream of the GH receptor — which is the mechanistic basis for its use in GH-resistant/insensitivity conditions.

For the top-ranked candidate, Monosomy X (Turner Syndrome), the rationale is indirect: patients with Turner syndrome commonly present with short stature and, in some cases, reduced responsiveness of the GH/IGF-1 axis. Theoretically, exogenous IGF-1 supplementation could support growth in this population, but this is an inferential link — there is no direct mechanistic or clinical evidence in the pack confirming mecasermin's efficacy specifically in monosomy X.

It is worth noting that the evidence pack itself flags this prediction as low-confidence: no clinical trials or literature were retrieved for monosomy X, and the rationale explicitly labels the connection as indirect. By contrast, the mechanistically stronger candidate (growth hormone insensitivity syndrome, rank 3) also lacks any supporting trials or publications, suggesting the current evidence base for all five candidates is prediction-only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Mecasermin is not currently marketed in Germany (market status: Not Marketed; total authorizations: 0). No license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The evidence pack flags TFDA/package-insert warnings and contraindications as a **Blocking** data gap (DG001), meaning this candidate cannot yet proceed to a formal safety (S1) evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for mecasermin — including the top-ranked Monosomy X — are at evidence level L5 (model prediction only), with no supporting clinical trials or literature identified, and decision stage remains S0. In addition, a blocking data gap exists for TFDA/package-insert safety information, preventing any preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA/package insert warnings and contraindications (blocking gap, DG001)
- Detailed mechanism of action (MOA) data via DrugBank API (DG002)
- Clinical trial or literature evidence specifically evaluating mecasermin in Turner syndrome (monosomy X) or GH insensitivity/Laron-like syndromes
- Confirmation of market/regulatory status in Germany, given the drug is currently not marketed
- Route of administration and dosage form compatibility data (currently marked "pending" for all candidates)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

