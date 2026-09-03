---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Linaclotide: From Undocumented Original Indication to Predicted Cauda Equina Syndrome

## One-Sentence Summary

> Linaclotide's original approved indication is not documented in the current evidence pack, though its known mechanism (a guanylate cyclase-C agonist acting locally on intestinal epithelium) points to a gastrointestinal secretory context rather than a neurological one.
> The TxGNN model predicts a possible link to **Cauda Equina Syndrome** with a very high score (**99.96%**),
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the association as likely a data artifact rather than a genuine treatment mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap — `original_indications` empty, `original_moa` = [Data Gap]) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% (rank 766) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is formally marked as a data gap in this evidence pack. However, the model's own repurposing rationale describes linaclotide as a **guanylate cyclase-C (GC-C) agonist** that acts exclusively on receptors on the intestinal epithelial surface, with systemic absorption below 0.1% and no capacity to cross the blood-brain barrier or act on spinal/cauda equina neural structures.

Cauda equina syndrome is a surgical emergency caused by mechanical compression of the cauda equina nerve roots, requiring urgent decompression — it has no established pharmacological relationship with intestinal secretory function. According to the evidence pack's own rationale, the high TxGNN score most likely reflects **confounding by symptom overlap** in the knowledge graph: "constipation" as a symptom node is frequently co-associated with the bowel/bladder dysfunction commonly seen in cauda equina syndrome patients, rather than reflecting any disease-modifying mechanism.

In short, the mechanistic link presented in this evidence pack is explicitly assessed as **not treatment-relevant** — it is a plausible explanation for *why the model scored this pairing highly*, not evidence that the pairing is clinically meaningful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Linaclotide is not marketed in Germany (`market_status: 未上市`), and no authorization records are present in the evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: the evidence pack flags TFDA label warnings/contraindications (DG001) as a **Blocking** data gap — this prevents any safety pre-assessment (S1 stage) for this candidate regardless of predicted indication.

---

## Additional Context: Pattern Across Predicted Indications

This evidence pack includes two further high-scoring predictions for linaclotide — **obsolete neurogenic bladder** (99.89%, rank 1766) and **insomnia** (99.51%, rank 5775) — both of which carry the same profile: no clinical trials, no literature, evidence level L5, and rationale text explicitly identifying the score as likely driven by symptom co-occurrence in the knowledge graph (e.g., neurogenic bowel/bladder co-morbidity, IBS-C/insomnia co-morbidity) rather than a genuine pharmacological mechanism. This consistent pattern across all three ranked candidates reinforces that none of the current predictions for linaclotide meet the bar for further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trial or literature evidence (L5, model-only), and the mechanistic rationale itself identifies the association as a likely knowledge-graph artifact (symptom co-occurrence) rather than a plausible treatment mechanism. A Blocking data gap on TFDA safety labeling also prevents entry into any formal safety pre-assessment.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data for linaclotide (currently missing from evidence pack)
- TFDA label warnings/contraindications (DG001 — Blocking) to enable S1 safety pre-assessment
- Independent mechanistic or preclinical evidence directly linking GC-C agonism to cauda equina pathophysiology, if such a hypothesis is to be pursued further
- Given the absence of any biological rationale, this candidate is not recommended for further development unless new primary evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

