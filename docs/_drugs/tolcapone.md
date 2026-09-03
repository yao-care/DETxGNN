---
layout: default
title: Tolcapone
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone: From Parkinson's Disease (COMT Inhibition) to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a COMT (catechol-O-methyltransferase) inhibitor; per the evidence pack's own rationale notes, its established pharmacology relates to catecholamine metabolism in Parkinson's disease as an adjunct to levodopa (no formal Taiwan/Germany regulatory record is available in this dataset).
The TxGNN model's top prediction is **Rasmussen Subacute Encephalitis**, but this is a pure model-driven association with **0 clinical trials** and **0 publications**, and the evidence pack explicitly states no known mechanistic overlap between COMT inhibition and this disease's T-cell–mediated neuronal injury.
Evidence strength for this specific prediction is minimal (L5) and does not currently support further development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Taiwan/Germany regulatory data (per evidence pack rationale, tolcapone is a COMT inhibitor classically used as adjunct therapy in Parkinson's disease) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap (DG002) in this evidence pack. Based on the mechanistic notes accompanying the predictions, tolcapone acts as a COMT inhibitor, altering catecholamine (dopamine) metabolism — a mechanism whose established clinical relevance is in dopaminergic disorders such as Parkinson's disease.

Rasmussen subacute encephalitis, in contrast, is an autoimmune epilepsy syndrome whose core pathology is T-cell–mediated neuronal destruction. The evidence pack's own repurposing rationale states there is **no known intersection** between the dopamine/catecholamine metabolic pathway and this disease's immunological mechanism, and characterizes this top-ranked prediction as a "data-driven association rather than a biological hypothesis."

It is worth noting that lower-ranked predictions in this same evidence pack show comparatively stronger (though still limited) mechanistic plausibility — for example, Lewy body dementia (rank 6, L4) is linked via DOPAL/α-synuclein biochemistry, and juvenile parkinsonism (rank 10, L4) is linked via tolcapone's established dopaminergic pharmacology. These may warrant separate evaluation, but per the reporting scope the top-ranked candidate (Rasmussen subacute encephalitis) does not currently have a defensible mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

No German market authorizations found in this evidence pack (total_licenses = 0; market_status = Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM label warnings and contraindications are flagged in this evidence pack as a Blocking data gap (DG001) — safety data could not be verified for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) has no supporting clinical trials, no literature, and an explicitly stated absence of mechanistic plausibility in the evidence pack itself — this is a model-score-only association (L5) and does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/BfArM label warnings and contraindications before any safety-stage evaluation can begin
- Resolve DG002 (High): obtain confirmed drug MOA data from DrugBank to properly assess mechanistic linkage
- Confirmed original indication and regulatory history for tolcapone (currently absent from this evidence pack)
- If pursuing repurposing signals from this dataset, consider re-scoping evaluation toward the higher-plausibility candidates identified within the same pack (Lewy body dementia, juvenile parkinsonism) rather than the top TxGNN-ranked but mechanistically unsupported candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

