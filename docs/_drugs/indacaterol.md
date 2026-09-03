---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From Bronchial Disease (COPD/Asthma) to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Indacaterol is a long-acting β2-adrenergic agonist (LABA) bronchodilator, presumed by drug class to have been developed for COPD/asthma-related bronchial disease — formal original-indication data is a confirmed gap, as the drug is not currently marketed in Germany.
> The TxGNN model's top-ranked prediction suggests possible efficacy in **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
> but this is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review flags the prediction as lacking biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered — drug is not marketed in Germany; pharmacologically presumed to be COPD/asthma-related bronchial disease based on drug class (LABA) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only, no supporting clinical trials or literature) |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is currently a confirmed data gap (DG002). Based on known pharmacological class information referenced elsewhere in this evidence pack, indacaterol is a selective long-acting β2-adrenergic receptor agonist (LABA) that relaxes bronchial smooth muscle — a mechanism associated with COPD/asthma-type bronchial disease.

NSIAD, in contrast, is driven by persistent, ligand-independent activation of the vasopressin V2 receptor in the renal collecting duct, causing inappropriate water retention independent of ADH levels. There is no established pharmacological pathway connecting β2-adrenergic agonism to V2 receptor activity.

The evidence pack's own repurposing rationale explicitly notes this: *"與腎性抗利尿激素不當分泌症候群(NSIAD)之V2受體persistent activation機轉無已知關聯。TxGNN高分推測缺乏生物學合理性支持"* — i.e., despite the high computational similarity score, the model's top prediction is not backed by a plausible biological mechanism. This should be treated as a caution flag rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorizations are currently on record for Indacaterol in Germany (total_licenses = 0; market status: 未上市). This drug-level gap (see DG001) also blocks formal safety/indication-label review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (NSIAD) has no clinical trial or literature support (Evidence Level L5) and the mechanistic rationale in this same evidence pack states the connection lacks biological plausibility. Combined with blocking data gaps on TFDA/BfArM label warnings (DG001) and mechanism of action (DG002), there is insufficient basis to advance this indication.

**To proceed, the following is needed:**
- Resolve DG001 (BfArM label warnings/contraindications) via label PDF retrieval
- Resolve DG002 (confirmed MOA) via DrugBank API
- If a repurposing signal is still desired for this drug, note that **"bronchial disease"** (rank 7 in this pack) carries strong evidence (L1, 30+ trials, 20+ publications, decision stage S3, "Proceed with Guardrails") — however, the pack's own rationale flags this as confirmation of the drug's *existing* known pharmacology (COPD/asthma) rather than a novel repurposing candidate, so it should be evaluated separately from a true new-indication standpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

