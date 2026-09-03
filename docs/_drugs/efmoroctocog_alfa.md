---
layout: default
title: Efmoroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Efmoroctocog alfa is a recombinant Factor VIII-Fc fusion protein whose core approved use is Hemophilia A (Factor VIII replacement therapy).
> The TxGNN model's top-ranked prediction is **Pseudo-von Willebrand Disease**, with a prediction score of **99.99%**,
> but this candidate currently has **no supporting clinical trials or literature**, and the underlying mechanistic rationale is assessed as weak — likely a knowledge-graph co-occurrence artifact rather than a genuine therapeutic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (Factor VIII deficiency) — noted in evidence rationale; not independently confirmed via Taiwan license data |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query pending — Data Gap DG002). Based on the information available in this evidence pack, efmoroctocog alfa is a recombinant Factor VIII-Fc fusion protein, and its core clinical role is Factor VIII replacement in Hemophilia A.

The top-ranked prediction, pseudo-von Willebrand disease, is mechanistically **not well supported**. This condition results from an abnormal platelet membrane GPIb receptor that causes excessive binding to von Willebrand factor (VWF) — it is a platelet functional defect, not a Factor VIII deficiency. Supplementing Factor VIII does not correct the underlying GPIb-VWF interaction abnormality. The evidence pack's own rationale flags this as a likely false-positive association, probably arising from the VWF-Factor VIII complex frequently co-occurring in the underlying knowledge graph rather than reflecting a real pharmacological relationship.

Among all ten predicted indications, the one with the strongest inherent mechanistic plausibility is actually rank 9, "hemophilia A with vascular abnormality" — this is essentially an extension of the drug's known, approved mechanism (Factor VIII replacement) rather than a novel repurposing hypothesis. However, it also currently has zero supporting clinical trials or literature. The remaining eight candidates (platelet release disorders, Glanzmann thrombasthenia, Scott syndrome, TTP, etc.) all involve platelet-function or non-Factor-VIII coagulation pathologies where Factor VIII replacement has no established mechanistic basis, and in the case of thrombotic thrombocytopenic purpura, the mechanism runs in the opposite direction (pro-thrombotic risk).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Efmoroctocog alfa currently has **no market authorization records in Taiwan** (0 licenses; market status: not marketed). No dosage form or approved indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications retrieval is an open, blocking data gap — see Conclusion and Next Steps below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are TxGNN model output only (Evidence Level L5), with zero supporting clinical trials or literature across the board. The top-ranked candidate's mechanistic rationale is explicitly assessed as weak/likely artifactual, and the drug is not currently marketed in Taiwan. Combined with a blocking safety data gap, there is insufficient evidence to advance any candidate at this time.

**To proceed, the following is needed:**
- Retrieve TFDA package insert (warnings, contraindications) — blocking gap (DG001)
- Retrieve DrugBank mechanism of action data — high-priority gap (DG002)
- If pursuing repurposing, prioritize rank 9 (hemophilia A with vascular abnormality) as the most mechanistically defensible candidate, and conduct a targeted literature/trial search rather than relying on the raw TxGNN ranking
- Reassess pseudo-von Willebrand disease (rank 1) as a likely false positive before any further investment of review effort
- Clarify Taiwan regulatory pathway status, given the drug is currently unmarketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

