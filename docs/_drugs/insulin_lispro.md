---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog used for glycemic control in diabetes mellitus.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**,
but currently **0 clinical trials** and **0 publications** support this direction, and the underlying rationale flags this prediction as likely graph-level noise rather than a genuine mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (glycemic control; detailed regulatory indication text not available in this evidence pack) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on general pharmacological knowledge, insulin lispro is a rapid-acting insulin analog that binds the insulin receptor to promote cellular glucose uptake; its efficacy in diabetes mellitus is well established.

For the top-ranked prediction, autoimmune oophoritis, the evidence pack's own mechanistic assessment is explicitly negative: there is **no known biological relationship** between autoimmune oophoritis and the insulin receptor/glucose metabolism pathway. The high TxGNN score most likely arises because both conditions are tagged as "autoimmune disease" and co-occur with Type 1 diabetes in the training knowledge graph — a semantic co-occurrence artifact rather than a genuine mechanistic link. The evidence pack itself classifies this as "database noise without mechanistic support."

Several lower-ranked candidates in this pack show comparatively more plausible (though still weak) rationale — for example, pancreatic agenesis (rank 7) and thiamine-responsive dysfunction syndrome (rank 2) both involve genuine diabetes-related comorbidity where insulin is used as supportive therapy. These are still extensions of the known diabetes indication rather than true novel indications, but they merit more consideration than the top-ranked candidate. Several other candidates (drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy) are flagged as likely representing insulin's known **adverse effect** (injection-site lipodystrophy) being mis-encoded as a treatment relationship, and should be treated as safety signals, not therapeutic opportunities.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

No marketing authorizations are currently on record for insulin lispro in this evidence pack (market status: Not Marketed; total authorizations: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (autoimmune oophoritis) has L5 evidence with zero supporting clinical trials or literature, and the evidence pack's own mechanistic review concludes it is most likely a semantic co-occurrence artifact in the training graph rather than a real biological association. No other candidate in this pack reaches beyond L4/S1 "Research Question" status, and those (pancreatic agenesis, thiamine-responsive dysfunction syndrome) are essentially restatements of the existing diabetes indication in rare genetic subtypes, not true new indications.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — currently blocking (DG001)
- Detailed mechanism of action data from DrugBank — currently high-priority gap (DG002)
- If pursuing pancreatic agenesis or thiamine-responsive dysfunction syndrome as research questions, case-series or registry data on insulin use in these rare genetic diabetes subtypes
- Re-run TxGNN scoring with lipodystrophy-related candidates reclassified as adverse-effect signals rather than candidate indications, to avoid future false positives from this same graph pattern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

