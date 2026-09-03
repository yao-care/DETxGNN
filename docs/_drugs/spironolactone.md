---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From Aldosterone-Related Fluid Retention to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Spironolactone is a mineralocorticoid (aldosterone) receptor antagonist historically used for conditions such as edema and hypertension, and off-label for androgenetic alopecia due to its anti-androgenic activity.
> The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, a hereditary hair-loss disorder,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap); spironolactone is generally known as an aldosterone antagonist used for edema/fluid retention and hypertension |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on generally known pharmacology, spironolactone is a mineralocorticoid receptor antagonist that also exhibits anti-androgenic activity, which is why it is used off-label for androgenetic alopecia (a hormone/androgen-driven hair loss condition).

However, hypotrichosis simplex of the scalp is a hereditary, autosomal condition most often linked to **APCDD1** mutations that disrupt the **Wnt signaling pathway** required for normal hair follicle development. This mechanism is unrelated to androgen or mineralocorticoid signaling. As a result, there is no established biological pathway connecting spironolactone's known pharmacology to this specific genetic disorder — the high TxGNN score (0.99) most likely reflects embedding similarity between "hair loss" phenotypes in the model's knowledge graph rather than a genuine causal or mechanistic link.

A second candidate in this evidence pack, **congenital hypotrichosis with milia** (score 0.99, rank 9732), shows the same pattern: it is a rare ectodermal dysplasia driven by keratinocyte differentiation/follicle development genes, with no known relationship to mineralocorticoid or androgen pathways. Both predictions should be treated as hypothesis-generating only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Spironolactone is currently **not marketed** in Germany under this evidence pack (0 authorizations on file), so no license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/label-level warnings, contraindications, and drug-drug interaction data are currently unavailable — this is a blocking data gap (DG001) that must be resolved before any safety evaluation (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial or literature support (L5, decision stage S0), and the proposed mechanistic link between spironolactone's known pharmacology and this hereditary Wnt-pathway hair disorder is not biologically supported. In addition, safety labeling data (warnings/contraindications) is missing, which blocks any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (DG001, blocking — required before S1 safety screening)
- Verified original indication and mechanism of action data from DrugBank (DG002)
- Any preclinical or genetic evidence linking mineralocorticoid/anti-androgen activity to APCDD1/Wnt-pathway hair follicle disorders
- If no such mechanistic or empirical evidence can be found, this candidate should remain at S0/Hold indefinitely rather than advance on TxGNN score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

