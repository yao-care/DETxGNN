---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lonoctocog Alfa: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Lonoctocog alfa is a recombinant factor VIII (rFVIII) replacement therapy used for the treatment of **Haemophilia A**.
> The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
> but currently **no clinical trials** and **no publications** support this direction — the prediction is model-only and the evidence pack's own mechanistic review flags it as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (inferred from known rFVIII pharmacology; not confirmed in the current dataset — `original_indications` is empty and TFDA label data is a blocking data gap) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, lonoctocog alfa is a recombinant Factor VIII product that replaces deficient or dysfunctional coagulation Factor VIII, and its efficacy in Haemophilia A is well established.

However, the top four TxGNN-predicted indications — pseudo-von Willebrand disease, primary platelet release disorder, Glanzmann thrombasthenia, and Scott syndrome — are all **platelet-function or platelet-receptor disorders**, not coagulation-factor deficiencies. Per the evidence pack's own mechanistic analysis, the model's high similarity scores likely arise from an indirect knowledge-graph association between FVIII and von Willebrand factor (the two normally circulate as a complex and are often measured together diagnostically), rather than a genuine shared therapeutic mechanism.

None of the four candidate diseases have a pathophysiology that FVIII replacement would be expected to correct (GPIbα gain-of-function, platelet storage-pool defect, GPIIb/IIIa deficiency, and TMEM16F scramblase deficiency, respectively). The evidence pack explicitly characterizes these associations as mechanistically implausible and unsupported by any clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Additional Predicted Candidates (Not Further Assessed)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Concern |
|------|---------|-------------|-----------------|-----------------|-------------|
| 2 | Primary release disorder of platelets | 99.84% | L5 | Hold | Platelet granule-release defect; no known FVIII mechanism, no supporting evidence |
| 3 | Glanzmann thrombasthenia | 99.76% | L5 | Hold | GPIIb/IIIa deficiency; unrelated to FVIII pathway |
| 4 | Scott syndrome | 99.44% | L5 | Hold | Membrane scramblase (TMEM16F) defect; not correctable by FVIII replacement |

## Germany Market Information

Lonoctocog alfa is **not yet marketed in Taiwan** — there are no authorization records (`total_licenses = 0`, `licenses = []`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications are supported only by model score (Evidence Level L5), with zero clinical trials and zero publications. The evidence pack's own mechanistic rationale argues these are likely false-positive associations driven by the FVIII–vWF diagnostic complex relationship rather than a real repurposing hypothesis. Combined with a blocking data gap on TFDA label warnings/contraindications, this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank/authoritative source (DG002)
- Confirmed original indication and regulatory status (current dataset has empty `original_indications` and 0 Taiwan licenses)
- Independent mechanistic review to confirm/refute the "false positive via vWF-FVIII complex" hypothesis before any further evidence collection is commissioned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

