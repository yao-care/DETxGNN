---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase Alfa: From CLN2 Disease (Batten Disease) to Scheie Syndrome

## One-Sentence Summary

> Cerliponase alfa is a recombinant TPP1 (tripeptidyl peptidase 1) enzyme replacement therapy, originally developed for **CLN2 disease** (a form of neuronal ceroid lipofuscinosis / Batten disease).
> The TxGNN model's top prediction is **Scheie Syndrome** (a subtype of Mucopolysaccharidosis I) with a **99.98%** prediction score,
> but there are currently **0 clinical trials** and **0 publications** supporting this specific link, and the mechanistic rationale suggests the signal is likely a model artifact rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLN2 disease (Neuronal Ceroid Lipofuscinosis Type 2 / Batten disease) — inferred from repurposing rationale text; not independently confirmed via German license data as the product is not marketed there |
| Predicted New Indication | Scheie Syndrome |
| TxGNN Prediction Score | 99.98% (rank 468 in overall model output) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data (`original_moa`) is marked as a data gap in this Evidence Pack. Based on the repurposing rationale notes attached to each predicted indication, cerliponase alfa is understood to be a recombinant enzyme replacement therapy that supplies **TPP1**, targeting CLN2 disease, a lysosomal storage disorder caused by TPP1 deficiency.

Scheie syndrome, by contrast, is a lysosomal storage disease caused by deficiency of **alpha-L-iduronidase** (MPS I), an entirely different enzyme and metabolic pathway. There is no shared substrate, no shared enzyme target, and no overlapping treatment mechanism between the two conditions.

The rationale text explicitly flags this: the high TxGNN score is most likely explained by the model's embedding space clustering diseases under the broad semantic category "lysosomal storage disease," rather than by any genuine pharmacological connection. This pattern repeats across nearly all top-10 predictions for this drug — Hurler syndrome, cholesteryl ester storage disease, Wolman disease, and Gaucher disease are all lysosomal storage disorders driven by *different* enzyme deficiencies (alpha-L-iduronidase, lysosomal acid lipase, glucocerebrosidase respectively), none of which involve TPP1. On the current evidence, this candidate should be treated as a likely **false positive** rather than a promising repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Cerliponase alfa currently has no German market authorization on file (`market_status`: 未上市 / Not marketed; `total_licenses`: 0). No product table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent labeling/warnings and contraindication data are flagged as Blocking data gaps in this Evidence Pack — see `DG001`. This must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Scheie syndrome) and essentially all other top-10 candidates lack both clinical trial and literature support (evidence level L5), and the drug's known enzyme-replacement mechanism (TPP1 for CLN2 disease) does not mechanistically overlap with the enzyme deficiencies underlying the predicted indications (alpha-L-iduronidase, lysosomal acid lipase, glucocerebrosidase, etc.). The pattern strongly suggests the TxGNN scores reflect semantic clustering of "lysosomal storage disease" labels rather than true repurposing signal.

**To proceed, the following is needed:**
- Confirmed MOA and original indication data from DrugBank/regulatory source (currently `[Data Gap]`)
- TFDA/EMA-equivalent labeling, warnings, and contraindications (Blocking gap `DG001`)
- If pursued further, independent mechanistic review of why TPP1 replacement could plausibly affect non-TPP1 lysosomal pathways, since no such rationale currently exists
- Given the absence of any supporting trial or literature evidence across all 10 candidates, recommend deprioritizing this drug for active repurposing evaluation unless new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

