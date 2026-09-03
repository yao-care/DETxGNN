---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From Unrecorded Original Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> The evidence pack does not record Tadalafil's original approved indication or mechanism of action (both marked as data gaps), and the drug is currently **not marketed** in Germany.
> The TxGNN model's top prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth disorder,
> but this is supported by **0 clinical trials** and **0 publications** — and the evidence pack's own rationale flags it as a likely network artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no approved indications or licenses on file) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% (rank 438) |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (original_moa: Data Gap). Based on the pharmacological background cited within the evidence pack itself, tadalafil is a phosphodiesterase type 5 (PDE5) inhibitor acting via the cGMP/NO pathway.

However, there is **no established biological link** between PDE5/cGMP signaling and Ambras type hypertrichosis universalis congenita, which is a rare congenital disorder of hair follicle overgrowth with a distinct genetic etiology. The evidence pack's own repurposing rationale explicitly states this prediction "lacks any mechanistic hypothesis" and is "suspected to be network noise" — i.e., an indirect, spurious graph connection between the drug node and a rare-disease genotype node, rather than a genuine pharmacological signal.

Given the complete absence of original indication data, MOA data, clinical trials, and literature, this top-ranked prediction should be treated as a high TxGNN score without corroborating evidence, not as a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

No marketing authorizations are currently recorded in Germany (Market status: Not marketed; total_licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Important note:** The evidence pack flags **TFDA label warnings/contraindications** as a **Blocking** data gap (DG001) — without this data, this candidate cannot advance to safety pre-screening (S1) regardless of predicted indication. Mechanism of action data is also flagged as a High-severity gap (DG002).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis universalis congenita) has no supporting clinical trials, literature, or mechanistic plausibility — the evidence pack itself identifies it as likely graph noise. Combined with missing original indication, MOA, and TFDA safety data, this candidate does not meet the minimum evidence bar to proceed.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001, blocking — required before any S1 safety pre-screening)
- Tadalafil mechanism of action and original approved indications (DG002)
- Independent review of whether the TxGNN score for this specific candidate reflects a real signal or a graph artifact, given the rationale text's own noise flag

**Note on other candidates in this pack:** Two lower-ranked predictions merit separate attention rather than dismissal alongside rank 1:
- **Rank 7 — Kyphoscoliotic heart disease** (Research Question stage): PDE5 inhibitors are an established drug class for pulmonary arterial hypertension (PAH), and kyphoscoliosis-associated restrictive lung disease can lead to secondary PAH. This is a plausible class-effect hypothesis worth checking against whether tadalafil's known PAH indication (e.g., Adcirca) was simply omitted from this evidence pack's original_indications field.
- **Rank 8 — Migraine with brainstem aura**: The single supporting citation is a case report of tadalafil-*induced* migraine aura (an adverse event), not a treatment-efficacy signal. This should be read as a safety signal, not a repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

