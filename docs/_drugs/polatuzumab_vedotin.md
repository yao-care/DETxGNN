---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 1
---

# Polatuzumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Polatuzumab Vedotin: From Diffuse Large B-Cell Lymphoma to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) approved for diffuse large B-cell lymphoma (DLBCL).
> The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph association without mechanistic or empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diffuse Large B-Cell Lymphoma (DLBCL) *(noted from mechanism description; official TFDA/German approved-label text unavailable — blocking data gap DG001)* |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is not available for this drug (data gap). Based on the repurposing rationale provided, polatuzumab vedotin is an antibody-drug conjugate (ADC) that targets CD79b, a B-cell surface antigen, and delivers the cytotoxic payload MMAE (monomethyl auristatin E) directly to CD79b-expressing cells. Its approved use is in DLBCL, where CD79b is highly expressed on malignant B cells.

CD79b is **not** expressed on breast cancer cells, including the HER2-positive subtype. HER2 and CD79b belong to entirely separate signaling/surface-marker systems, and there is currently no known biological pathway connecting the two. In other words, the drug's cytotoxic delivery mechanism has no target to bind to in HER2-positive breast carcinoma.

The high TxGNN score (0.99) therefore reflects a strong statistical association within the knowledge graph rather than a mechanism-driven hypothesis. Without a plausible target-expression rationale, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

*This drug is a cytotoxic antibody-drug conjugate approved for a hematologic malignancy (DLBCL), meeting the criteria for inclusion of this section.*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-drug conjugate (ADC) with cytotoxic payload (MMAE, a tubulin polymerization inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | ADCs are typically subject to cytotoxic/hazardous drug handling precautions; please refer to institutional handling protocol |

---

## Safety Considerations

Please refer to the package insert for safety information. *(Note: TFDA label/warnings data is a blocking data gap — DG001 — and must be resolved before any S1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at Evidence Level L5 — no clinical trials, no literature, and no plausible target-expression rationale (CD79b is not expressed in HER2-positive breast carcinoma). Combined with the blocking data gap on TFDA/German labeling and the drug's current "not marketed" status in Germany, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Preclinical evidence of CD79b expression or an alternative target-engagement mechanism in HER2-positive breast cancer models
- Resolution of blocking data gap DG001 (TFDA/German approved label, warnings, contraindications)
- Confirmed mechanism of action data (DG002)
- Clarification of German market/regulatory status before any further clinical development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

