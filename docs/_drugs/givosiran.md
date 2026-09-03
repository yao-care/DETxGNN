---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Primitive Portal Vein Thrombosis

## One-Sentence Summary

> Givosiran is a GalNAc-conjugated siRNA therapeutic; the Evidence Pack does not contain a confirmed original indication or approved product information (the drug is not marketed in this jurisdiction), though it is externally known as a treatment for acute hepatic porphyria.
> The TxGNN model's top-ranked prediction is **Primitive Portal Vein Thrombosis**, but this candidate currently has **0 clinical trials** and **0 supporting publications**, and the accompanying rationale explicitly states there is no known mechanistic link.
> Evidence for this specific candidate is therefore model-output only (L5), and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/approved-indication text in Evidence Pack (drug not marketed in this jurisdiction) |
| Predicted New Indication | Primitive Portal Vein Thrombosis |
| TxGNN Prediction Score | 99.9986% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). External background knowledge indicates givosiran is a small interfering RNA (siRNA) that is taken up by hepatocytes via GalNAc conjugation and suppresses translation of hepatic ALAS1 mRNA, thereby reducing accumulation of the neurotoxic heme precursors ALA and PBG — this MOA is corroborated by the rationale text attached to a lower-ranked candidate in this same Evidence Pack (rank 9, ALA dehydratase deficiency porphyria), though it is not confirmed for the top-ranked candidate itself.

For the top prediction, **Primitive Portal Vein Thrombosis**, the Evidence Pack's own rationale is explicit: *"No known mechanistic link. Givosiran acts on the ALAS1/heme biosynthesis pathway, which has no direct connection to the coagulation/vascular pathology underlying portal vein thrombosis. The high TxGNN score likely reflects representational similarity among 'liver disease' nodes in the knowledge graph rather than a genuine biological pathway."* Ranks 2–5, 7, 8, and 10 in this same batch carry an identical or near-identical TxGNN score (~0.99999) and the same caveat, suggesting a score-clustering artifact around hepatic-disease nodes rather than independently validated signals.

By contrast, one candidate in this batch — porphyria due to ALA dehydratase deficiency (rank 9) — does have a coherent mechanistic rationale (shared ALAS1/heme pathway with the drug's known clinical use in acute hepatic porphyria) and 8 supporting publications, including a Phase 3 post-hoc analysis. This candidate scored lower than the top-ranked prediction, which further supports treating the rank-1 candidate's high score with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorizations were found for this drug in the current dataset (market status: not marketed; total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: a Blocking-severity data gap (DG001) means TFDA/label warnings and contraindications could not be retrieved, so this drug cannot yet undergo initial safety screening (S1) for any indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Primitive Portal Vein Thrombosis) has no clinical trials, no literature, and an explicitly stated lack of mechanistic plausibility — this is a pure model-score artifact, not an actionable repurposing signal. Combined with the Blocking-severity gap in label/safety data, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/EMA label data (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed original indication and DrugBank MOA data (DG002)
- Independent mechanistic or preclinical evidence connecting ALAS1/heme biosynthesis inhibition to portal vein thrombosis pathology, if this candidate is to be pursued further

**Separate note for the research team:** within this same batch, rank 9 (*porphyria due to ALA dehydratase deficiency*) has a materially stronger evidence profile — coherent shared-pathway mechanism, 8 literature citations including a Phase 3 post-hoc analysis (L3, Research Question stage) — and may warrant its own evaluation track rather than being deprioritized simply because of its lower raw TxGNN rank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

