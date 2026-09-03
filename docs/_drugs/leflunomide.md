---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 2
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

> Leflunomide is a DHODH inhibitor conventionally used to treat rheumatoid arthritis and other inflammatory/autoimmune conditions.
> The TxGNN model predicts a possible association with **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal malformation,
> but this prediction is currently supported by **no clinical trials and no published literature** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / other inflammatory diseases (based on known clinical use; not derivable from structured license data — none available) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for leflunomide is not available in this Evidence Pack (`[Data Gap]`). Based on known information, leflunomide inhibits dihydroorotate dehydrogenase (DHODH), blocking de novo pyrimidine synthesis in activated lymphocytes, which produces an immunomodulatory effect used clinically in inflammatory diseases such as rheumatoid arthritis.

Brachydactyly-syndactyly syndrome, however, is a congenital skeletal malformation disorder typically linked to developmental gene abnormalities (e.g., HOXD gene cluster), driven by embryonic limb patterning defects rather than inflammatory or autoimmune processes. There is no established biological pathway connecting DHODH inhibition or pyrimidine synthesis blockade to congenital limb development.

The repurposing rationale attached to this candidate explicitly notes that **no mechanistic connection can currently be established**, and the missing original MOA data further weakens confidence in this link. This prediction should be treated as an algorithmic signal only (TxGNN score 0.9993, rank 1209), not as a mechanistically grounded hypothesis.

A second, closely related candidate — **colobomatous microphthalmia-rhizomelic dysplasia syndrome** (score 0.9993, rank 1235) — shows the same pattern: a rare congenital eye/skeletal developmental disorder with no plausible link to leflunomide's known immunomodulatory mechanism, and no supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Leflunomide is currently **not marketed** in Germany under this record (`market_status: 未上市`), and no authorization entries are available (`total_licenses: 0`). No product/license table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM warnings and contraindications are flagged as a **Blocking** data gap — DG001 — preventing entry into the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a raw TxGNN prediction score, with no clinical trials, no literature, and no plausible mechanistic link between leflunomide's known immunomodulatory action and a congenital skeletal malformation syndrome. Combined with a Blocking-severity safety data gap (missing warnings/contraindications), this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- Leflunomide's original MOA and confirmed original indication(s) from DrugBank/authoritative labeling
- TFDA/BfArM package insert warnings and contraindications (resolves DG001, currently blocking)
- Preclinical or genetic evidence establishing a biological pathway between pyrimidine synthesis/DHODH inhibition and skeletal/limb developmental disorders
- Any case reports, registries, or mechanistic studies for either predicted indication before advancing beyond model-prediction-only status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

