---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# INSULIN HUMAN: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin human is the standard replacement therapy for diabetes mellitus (endogenous insulin deficiency).
The TxGNN model's top-ranked new-indication prediction is **Autoimmune Oophoritis** (score 99.84%),
but this candidate has **no clinical trials, no supporting literature, and no mechanistic rationale for therapeutic benefit** —
the evidence assessment itself flags it as a likely knowledge-graph comorbidity artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (insulin replacement therapy) — not itemized in this evidence pack; Germany/regulatory license data unavailable |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack). Based on general pharmacological knowledge, insulin human replaces or supplements endogenous insulin to regulate glucose metabolism; its efficacy in diabetes mellitus is well established.

The proposed mechanistic link to autoimmune oophoritis is that both conditions can co-occur within autoimmune polyglandular syndrome (Type 1 diabetes plus autoimmune ovarian failure share an autoimmune predisposition). However, this is a **comorbidity association**, not evidence that insulin has any direct therapeutic effect on ovarian autoimmune tissue destruction. The evidence assessment explicitly characterizes this prediction as "knowledge-graph relational noise" rather than a plausible pharmacological hypothesis — insulin's glucose-lowering mechanism has no established pathway relevant to halting or reversing autoimmune oophoritis.

Reviewing the full set of 10 TxGNN predictions for this drug reinforces this conclusion: most (ranks 1, 2, 3, 5, 6, 7, 8, 10) are explicitly annotated by the evidence layer as comorbidity artifacts or even **direction-reversed associations** (e.g., insulin injection is a known *cause* of localized lipodystrophy, not a treatment for it). The two exceptions — thiamine-responsive dysfunction syndrome (rank 4) and pancreatic agenesis (rank 9) — reflect insulin's well-established role in managing *secondary diabetes* that arises from these genetic syndromes, which is existing standard clinical practice rather than a novel repurposing discovery.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No authorization records are available in this evidence pack. Market status is recorded as **未上市 (Not marketed)** with **0 total licenses**, so no product/dosage-form table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all unavailable in this evidence pack; TFDA label warnings/contraindications are flagged as a **Blocking** data gap that prevents formal S1 safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (autoimmune oophoritis) has no clinical, literature, or mechanistic support and is explicitly identified by the evidence assessment as a likely knowledge-graph artifact driven by shared autoimmune comorbidity rather than a genuine pharmacological signal. Combined with a Blocking-severity gap in TFDA safety labeling and a High-severity gap in mechanism-of-action data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/EMA package insert data (warnings, contraindications) to clear the Blocking data gap and enable S1 safety screening
- Confirmed mechanism-of-action documentation for insulin human (DrugBank API query)
- If autoimmune oophoritis is pursued further: dedicated mechanistic or preclinical studies evaluating insulin/insulin-signaling pathways in ovarian autoimmune tissue — none currently exist
- Re-evaluate whether ranks 4 (thiamine-responsive dysfunction syndrome) and 9 (pancreatic agenesis) should instead be reclassified as "existing standard-of-care" rather than novel repurposing candidates, since insulin is already used clinically for secondary diabetes in both syndromes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

