---
layout: default
title: Dibotermin Alfa
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 9
---

# Dibotermin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dibotermin Alfa: From Bone Regeneration to Esotropia

## One-Sentence Summary

> Dibotermin alfa (recombinant human BMP-2) is a bone-inductive growth factor used for spinal fusion and open tibial fracture repair.
> The TxGNN model's top prediction is **Esotropia**, but this candidate is supported by **zero clinical trials** and **zero publications**,
> and the drug's own evidence pack explicitly notes there is no known biological link between BMP-2 signaling and extraocular muscle disorders.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bone regeneration (spinal fusion / open tibial fracture) — inferred from mechanistic rationale; not separately confirmed in this evidence pack |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa = Data Gap). Based on other information in the pack, dibotermin alfa is recombinant human BMP-2 (rhBMP-2), a growth factor whose known biology is to induce osteogenic differentiation; it is used clinically for spinal fusion and open tibial fracture bone regeneration.

Esotropia is a neuromuscular control disorder of the extraocular muscles. There is no known mechanistic pathway connecting BMP-2 osteoinductive signaling to extraocular muscle alignment or neuromuscular control. The evidence pack's own rationale explicitly states this candidate has "no biological plausibility support" and represents a pure network-association artifact of the TxGNN model rather than a grounded repurposing hypothesis.

Because there is no mechanistic bridge, no completed or ongoing clinical trials, and no literature, this prediction should be treated as a **low-confidence signal requiring independent biological validation**, not as an actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Dibotermin alfa currently holds no marketing authorization in Germany (0 licenses on record); the drug is not marketed in this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Additional Note: Other Predicted Indications Reviewed

Eight additional TxGNN-predicted indications were reviewed alongside esotropia (ranks 2–9), all scored L5 / Hold, with no supporting clinical trials. Two points are worth flagging to decision-makers:

- **HER2-positive breast carcinoma and related breast cancer subtypes (ranks 2, 3, 4, 6)**: Literature on BMP-2 signaling in breast tumor biology generally points toward tumor promotion (proliferation, EMT, bone metastasis) rather than a therapeutic effect. These should be read as a **potential safety signal**, not a repurposing opportunity.
- **"Breast tumor luminal A or B" (rank 5)**: The 19 literature records attached to this candidate are a **data-quality artifact** — they concern B-cell immunology and Hepatitis B vaccines, evidently mismatched via the keyword "B" and unrelated to breast cancer or BMP-2. This should be excluded from any evidence count.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (esotropia) has no clinical, literature, or mechanistic support, and the pack's own analysis states there is no biological plausibility. No candidate across the full prediction set reaches even L3 evidence, and two candidates carry a potential safety signal (pro-tumorigenic BMP-2 activity in breast cancer) rather than a therapeutic rationale.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/BfArM label warnings and contraindications) before any S1 safety screening can occur
- Resolve DG002 (confirmed mechanism of action) to properly assess mechanistic plausibility
- Independent, targeted literature search for BMP-2 and extraocular muscle/strabismus biology (current literature pull returned no relevant hits)
- If breast cancer signal is pursued further, prioritize it as a **risk assessment** (does BMP-2 exposure worsen breast cancer outcomes) rather than a repurposing opportunity
- Given the drug is not marketed in Germany and no clinical evidence exists for any candidate, no further action is recommended at this time beyond monitoring for new literature/trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

