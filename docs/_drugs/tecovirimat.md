---
layout: default
title: Tecovirimat
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: From Smallpox/Orthopoxvirus Infection to Hordeolum

## One-Sentence Summary

Tecovirimat is a VP37 envelope protein inhibitor originally developed and FDA-authorized for smallpox and orthopoxvirus infections (including mpox), acting through a mechanism specific to the *Orthopoxvirus* genus. TxGNN's top-ranked prediction is **Hordeolum**, but the model's own mechanistic review flags this as a **high embedding score with no biological plausibility**, since hordeolum is a bacterial (typically staphylococcal) eyelid gland infection unrelated to poxvirus replication or budding. **No clinical trials or literature support this specific pairing.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smallpox / Orthopoxvirus infection (incl. mpox), per literature context in evidence pack |
| Predicted New Indication | Hordeolum |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Tecovirimat inhibits the VP37 envelope-wrapping protein, a mechanism specific to the *Orthopoxvirus* genus (variola/smallpox, mpox, vaccinia). This mechanism has no known relevance to eyelid gland infections such as hordeolum, which are caused by bacteria (typically *Staphylococcus aureus*) infecting the meibomian or Zeis glands — an entirely different pathogen class and disease process.

The evidence pack's own mechanistic review explicitly rejects this prediction: **"TxGNN's high score reflects an embedding-space coincidence, with no biological plausibility."** The same pattern repeats across ranks 2–10 (vibrio infection, Klebsiella infection, noma, arbovirus infection, equine infectious anemia, idiopathic herpes, Astroviridae infection, Arterivirus infection) — all are bacterial infections, unrelated RNA/DNA virus families, or veterinary-only pathogens with no mechanistic link to VP37 inhibition.

The one exception in this candidate set is **rank 5, "coinfection"** (L3, S1, evidence includes 20 real publications). However, on closer reading, this cluster of literature does not represent a genuine new-indication signal — it consists of case reports and reviews describing tecovirimat's **existing, already-approved use for mpox** in patients with HIV or other coinfections (e.g., neurosyphilis, VZV). This appears to be a **data-labeling artifact**: the correct disease label should be "mpox in immunocompromised/coinfected patients," not a novel repurposing target. It should not be counted as new-indication evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Hordeolum.

*Note: 20 publications exist for rank 5 ("coinfection"), but these describe tecovirimat's already-approved mpox indication in HIV/coinfected populations rather than a novel repurposing hypothesis — see rationale above.*

---

## Germany Market Information

Tecovirimat is **not currently marketed in Germany** (0 authorizations on record), so no authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not yet available in this evidence pack (flagged as a **Blocking** data gap, DG001 — TFDA/BfArM label warnings and contraindications must be retrieved before any S1 safety screening can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN top-ranked predictions for tecovirimat lack mechanistic plausibility or supporting clinical/literature evidence. Nine of ten (hordeolum, vibrio infection, Klebsiella infection, noma, arbovirus infection, equine infectious anemia, idiopathic herpes, Astroviridae infection, Arterivirus infection) are bacterial, unrelated-virus, or veterinary conditions with no link to the VP37 orthopoxvirus mechanism. The one candidate with literature support ("coinfection") is most likely a mislabeled instance of tecovirimat's existing mpox indication in HIV-coinfected patients, not a true repurposing signal.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain TFDA/BfArM label warnings and contraindications before any safety-stage (S1) review
- Resolve **DG002 (High)**: obtain formal DrugBank/FDA-label MOA documentation to properly ground future mechanistic assessments
- Relabel "coinfection" in the TxGNN indication ontology as "mpox in HIV/immunocompromised patients" to avoid conflating existing-indication evidence with novel repurposing signals
- Re-run TxGNN scoring excluding known off-target embedding clusters (bacterial/veterinary diseases) if this pattern recurs for other orthopoxvirus-specific antivirals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

