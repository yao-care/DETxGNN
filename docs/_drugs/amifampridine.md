---
layout: default
title: Amifampridine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Amifampridine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Amifampridine: From Unspecified Original Indication to Glaucoma

## One-Sentence Summary

Amifampridine (DrugBank ID: DB11640) is currently **not marketed in Germany**, and this evidence pack does not yet contain verified data on its original approved indication or mechanism of action (flagged as blocking/high-severity data gaps).
The TxGNN model predicts it may be effective for **Glaucoma**, with a prediction score of **99.71%**, but currently **0 clinical trials** and **0 publications** support this direction — the evidence level is model-prediction-only (L5).
A second, lower-priority candidate indication, **Acute Intermittent Porphyria**, was also predicted (score 99.32%), similarly with no supporting trials or literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data sources (see Data Gaps below) |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for amifampridine is not available in this evidence pack (Data Gap DG002, severity High), and no original indication has been recorded either. This significantly limits how confidently the original-indication-to-new-indication rationale can be assessed.

Based on the TxGNN model's own generated rationale, amifampridine is understood as a broad-spectrum voltage-gated potassium (Kv) channel blocker, with its established pharmacology centered on enhancing presynaptic acetylcholine release at the neuromuscular junction. The proposed link to glaucoma is an indirect, cross-system extrapolation: aqueous humor secretion by the ciliary body epithelium and trabecular meshwork outflow also involve various K+ channels (e.g., Kir, KCa), so a potassium-channel modulator could theoretically influence intraocular pressure (IOP). However, this is **not** a direct mechanistic link to glaucoma pathology (e.g., trabecular meshwork degeneration, retinal ganglion cell apoptosis), and the directionality of K+ channel blockade vs. activation on IOP is inconsistent across the literature. There is no animal model or ex vivo ocular tissue data supporting this connection — the model itself characterizes this as "highly speculative."

For the second candidate, acute intermittent porphyria (AIP), the rationale draws an analogy to amifampridine's known neuromuscular junction mechanism (used in Lambert-Eaton myasthenic syndrome-type indications): AIP can cause autonomic dysfunction and axonal neuropathy with associated muscle weakness, and enhancing ACh release could theoretically provide symptomatic benefit. However, AIP's core pathology is a defect in heme biosynthesis (porphobilinogen deaminase deficiency) and axonal degeneration — not a presynaptic neurotransmitter release deficit — so this is again a speculative mechanistic analogy rather than a direct pathological match, with no preclinical or clinical data available.

Given both candidates lack any supporting trial or literature evidence and rely purely on indirect mechanistic reasoning, neither prediction currently rises above L5 (model-prediction-only) evidence strength.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Amifampridine currently holds **no marketing authorizations in Germany** (market status: 未上市 / Not Marketed; total licenses: 0). No product, dosage form, or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** This evidence pack flags the absence of TFDA package insert warnings/contraindications data as a **Blocking** data gap (DG001), which prevents this candidate from entering the S1 safety pre-assessment stage. No DDI records were found (query status: not_found).

---

## Other Predicted Indication (Reference Only)

| Item | Content |
|------|------|
| Disease | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| Clinical Trials / Literature | None found |
| Recommendation | Hold |

The mechanistic rationale for this candidate is an indirect analogy between amifampridine's neuromuscular junction pharmacology and AIP-associated neuropathic weakness, rather than a match to AIP's core heme-biosynthesis pathology. No clinical, preclinical, or literature evidence currently supports this direction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications (glaucoma and acute intermittent porphyria) are supported only by TxGNN model scores and speculative mechanistic reasoning, with zero clinical trials or literature identified for either. In addition, a **Blocking**-severity data gap (missing TFDA label/warnings, DG001) prevents this candidate from even entering the standard safety pre-assessment (S1) stage, and the drug is not currently marketed in Germany.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) to clear the S1 safety pre-assessment blocker (DG001)
- Verified mechanism of action and original approved indication data from DrugBank or another authoritative source (DG002)
- Preclinical or in vitro evidence connecting amifampridine's K+ channel activity to IOP regulation (for the glaucoma candidate)
- Any case reports, observational data, or mechanistic studies linking amifampridine to AIP-related neuropathy (for the secondary candidate)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

