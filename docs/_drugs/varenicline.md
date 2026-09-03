---
layout: default
title: Varenicline
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotinic acetylcholine receptor (nAChR) partial agonist used as an aid for smoking cessation. The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a pure model output with no mechanistic or clinical validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation aid (inferred from literature; official regulatory indication text not available) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the surrounding literature in this evidence pack, varenicline is described as "a partial agonist/antagonist with affinity and selectivity for alpha4 beta2 nicotinic acetylcholine receptors," used clinically as a first-line smoking cessation therapy by reducing nicotine craving and withdrawal symptoms.

There is no literature or clinical trial in this evidence pack that connects α4β2 nAChR partial agonism to migraine pathophysiology. The only migraine-adjacent evidence found under a related candidate indication ("headache disorder," rank 9) consists exclusively of smoking-cessation trials where headache appears as an incidental adverse-event term — including one case report ("Bath-related headache induced by varenicline," PMID 23175211) describing varenicline **causing** headache, i.e., evidence pointing in the opposite direction of the hypothesis. No positive mechanistic or clinical signal for migraine treatment exists in the available data.

Given the complete absence of disease-specific trials, publications, or mechanistic rationale, this prediction should be treated as an unvalidated model output rather than a pharmacologically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

Varenicline is currently **not marketed** in Germany (0 authorizations on record), so no product/authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (migraine disorder) has no supporting clinical trials or literature, and the only tangentially related evidence in this evidence pack (under "headache disorder") actually suggests varenicline may *induce* rather than treat headache. Combined with two blocking/high-severity data gaps — missing TFDA label data (warnings/contraindications) and missing MOA confirmation — this candidate does not meet the minimum bar to advance past S0.

**To proceed, the following is needed:**
- TFDA-approved label (warnings, contraindications) to unblock S1 safety screening (DG001, Blocking)
- Confirmed mechanism of action from DrugBank/primary pharmacology sources (DG002, High)
- Disease-specific preclinical or clinical evidence directly evaluating varenicline in migraine (not smoking-cessation trials with headache as an incidental term)
- Clarification of official original indication and regulatory approval status, since `original_indications` is currently empty
- If pursuing lower-ranked candidates (e.g., glaucoma, alopecia), equivalent trial/literature evidence must first be identified — none currently exists for any of the 10 candidates in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

