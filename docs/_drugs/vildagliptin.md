---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

> Vildagliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor originally developed for type 2 diabetes mellitus (T2DM), improving glycemic control by prolonging endogenous GLP-1/GIP activity.
> The TxGNN model's top-ranked prediction is **Focal Stiff Limb Syndrome**, with a prediction score of **99.88%**,
> but this candidate currently has **0 clinical trials** and **0 supporting publications**, and the evidence pack itself flags no plausible mechanistic link — this is a pure model-score hit, not a substantiated repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus *(derived from literature within the evidence pack; not formally recorded in regulatory data as the drug is unmarketed in Germany)* |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is officially marked as a data gap (DrugBank query pending). Based on information embedded in the accompanying literature and trial evidence, vildagliptin is known to inhibit DPP-4, thereby extending the half-life of endogenous GLP-1 and GIP, enhancing glucose-dependent insulin secretion, and suppressing inappropriate glucagon release — its efficacy in T2DM is well established in this class.

However, for the top-ranked candidate, **Focal Stiff Limb Syndrome**, no plausible mechanistic bridge exists. Stiff limb/stiff person syndrome is an autoimmune neurological disorder driven primarily by anti-GAD65 antibodies and impaired GABAergic inhibitory transmission — a pathophysiology entirely unrelated to incretin/glucose signaling. The evidence pack's own rationale explicitly states: *"無可辨識之機轉關聯...此為TxGNN純預測分數，缺乏任何生物學支持論述"* (no identifiable mechanistic link; this is a pure TxGNN prediction score without biological support). The same holds for TxGNN's other top-5 hits (classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia) — all are rare, structurally or genetically driven diseases with no known DPP-4 connection.

Given the very high raw score but complete absence of corroborating evidence, this prediction should be treated as a statistical artifact of the knowledge-graph embedding rather than a credible repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Vildagliptin is currently **not marketed** in Germany (未上市) under this evidence pack, with 0 registered authorizations. No product/license records are available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all currently marked as data gaps — TFDA label retrieval is a blocking item, see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Focal Stiff Limb Syndrome) has Evidence Level L5 — a model score with zero clinical trials, zero literature, and no identifiable mechanistic rationale. Combined with the drug's unmarketed status in Germany and missing MOA/label data (DG001 blocking, DG002 high severity), there is no basis to advance this indication beyond exploratory screening.

**To proceed, the following is needed:**
- TFDA/official label retrieval (warnings, contraindications) — currently blocking S1 safety screening
- Confirmed DrugBank MOA data
- Any preclinical or mechanistic rationale connecting DPP-4/incretin pathways to autoimmune stiff-person-spectrum disease, before further evaluation is justified

---

**Additional Note — Alternative Signal Worth Tracking:**
Among this drug's 10 TxGNN-predicted indications, **Type 1 Diabetes Mellitus** (rank 10, score 99.37%) stands out as the only candidate with substantive evidence: Evidence Level **L2**, including a completed Phase 2 RCT directly testing rapamycin + vildagliptin for β-cell function recovery in long-standing T1D (NCT02803892; concordant RCT publication PMID 33124663), plus mechanistic RCT evidence on glucagon counter-regulation in T1D (PMID 22855332). This is mechanistically coherent (incretin-mediated β-cell preservation as adjunct, not insulin replacement) and is a more defensible candidate for a "Research Question" stage evaluation than the top-ranked stiff-limb-syndrome hit, though most of its 40+ listed trials are T2DM noise and would need individual re-grading before use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

