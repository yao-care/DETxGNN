---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 1
---

# Selinexor
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

# Selinexor: From Original Indication (Not Documented) to Drug-Induced Osteoporosis

## One-Sentence Summary

> The original indication and mechanism of action for Selinexor are **not available** in the current dataset (marked as Data Gap).
> The TxGNN model predicts a possible association with **Drug-Induced Osteoporosis**, but this comes with **zero supporting clinical trials** and **zero literature references**,
> and the semantic relationship itself is ambiguous — it is unclear whether this indicates a *treatment* effect or an *adverse-effect* risk.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as Data Gap in the source evidence pack). No original indication is recorded either, which means we cannot compare the drug's known pharmacology against the predicted new indication.

More importantly, the predicted indication itself — "drug-induced osteoporosis" — is semantically ambiguous in this context. It is not clear whether the TxGNN model is proposing that Selinexor could be **used to treat** drug-induced osteoporosis, or whether it is flagging that Selinexor **may itself induce** osteoporosis as an adverse effect. These two interpretations lead to opposite clinical conclusions (a therapeutic candidate vs. a safety signal), and the evidence pack explicitly notes this ambiguity has not been resolved.

Given the absence of MOA data, original indication data, and any supporting trials or literature, there is currently no mechanistic or clinical basis to judge the biological plausibility of this high prediction score (0.992). The score alone, without corroborating evidence, is insufficient to support advancing this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Selinexor is not currently marketed in Germany (0 authorizations on record); no license or approved-indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only, no clinical trials or literature), and two blocking/high-severity data gaps remain — TFDA warnings/contraindications and mechanism of action — in addition to an unresolved ambiguity about whether the predicted association represents a therapeutic opportunity or an adverse-effect risk.

**To proceed, the following is needed:**
- Original indication and mechanism of action (MOA) data from DrugBank
- TFDA/BfArM package insert data (warnings, contraindications) — currently blocking for safety review
- Clarification of whether "drug-induced osteoporosis" reflects a treatment target or a risk association for Selinexor
- Independent search for supporting clinical trials or literature before this candidate can move past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

