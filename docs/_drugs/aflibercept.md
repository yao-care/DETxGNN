---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Aflibercept
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

Using the drug-repurposing evaluation report template (v5) to produce this report directly from the supplied Evidence Pack — no additional tool calls are needed since all required fields are already in the JSON.

Note upfront: several fields the template expects (original indication license text, MOA, safety data, market authorizations) are empty or flagged as data gaps in this pack, so I've followed the "omit / state unavailable, never print the literal `[Data Gap]` token" rule throughout.

---

# Aflibercept: From Ophthalmic Vascular Disease to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF-trap fusion protein whose established clinical use is concentrated in ophthalmic vascular disorders (e.g., wet age-related macular degeneration, diabetic macular edema, retinopathy of prematurity), though no formal license or indication text is present in this evidence pack. The TxGNN model predicts a possible association with **Esotropia**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on the model's score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured license data; per known pharmacology, aflibercept is used in ophthalmic vascular disease (wet AMD, diabetic macular edema, ROP) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — DrugBank MOA query needed). Based on known pharmacological background, aflibercept is a VEGF-trap fusion protein that inhibits VEGF-A, VEGF-B, and PlGF; its clinical use has concentrated on angiogenic/vascular-proliferative eye diseases such as wet AMD, diabetic macular edema, and retinopathy of prematurity (ROP).

Esotropia, by contrast, is a neuromuscular/refractive eye-alignment disorder — its pathophysiology (extraocular muscle imbalance, accommodative refractive error, cranial nerve dysfunction) has no established connection to the VEGF signaling pathway. The only proposed link in this evidence pack is an indirect hypothesis: treating vascular retinopathies such as ROP might secondarily lower the risk of resulting strabismus. This is a plausible-sounding but **unverified, speculative connection** — it is not supported by any clinical trial or literature evidence, and should not be treated as mechanistic support.

Given the absence of both direct mechanistic rationale and confirmatory evidence, this prediction should be read as a hypothesis-generating signal from the model only, not as a clinically grounded repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No market authorizations are on record for aflibercept in this dataset (market status: not marketed, 0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA package-insert warnings/contraindications are flagged in this pack as a **Blocking** data gap — DG001 — and must be resolved before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5, decision stage S0) — there are zero clinical trials and zero publications linking aflibercept to esotropia, and the proposed mechanistic link is explicitly speculative with no established pharmacological basis connecting the VEGF pathway to esotropia's neuromuscular/refractive etiology.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): TFDA/regulatory package-insert warnings and contraindications, required before any safety pre-assessment
- Resolve DG002 (High): confirmed mechanism of action from DrugBank to properly assess mechanistic plausibility
- Confirmed original indication / license data (currently absent from regulatory records)
- Any preclinical, mechanistic, or observational literature specifically examining VEGF pathway involvement in strabismus/esotropia
- DDI data (currently "not found") before any co-prescription risk can be evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

