---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a well-established amide local anesthetic, used clinically to numb tissue for surgical/procedural pain control (and, in certain formulations, as a Class Ib antiarrhythmic). The TxGNN model predicts a possible new indication for **Punctate Epithelial Keratoconjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal with no external validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (official approved-indication text unavailable — no license records in dataset) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lidocaine is not available in the current DrugBank extract (flagged as Data Gap DG002, High severity). Based on general pharmacological knowledge, lidocaine is an amide-class local anesthetic that blocks voltage-gated sodium channels to reversibly inhibit nerve conduction; it produces analgesia/anesthesia but has no established anti-inflammatory, antiviral, or immunomodulatory activity.

Punctate epithelial keratoconjunctivitis is an inflammatory/erosive condition of the corneal and conjunctival epithelium, typically driven by viral infection, chemical/UV injury, or immune-mediated processes. Sodium-channel blockade can mask ocular surface pain but does not address any of these underlying disease mechanisms — there is no known pathway by which lidocaine would modify the course of this condition.

The model-generated rationale for this prediction itself concludes that the high TxGNN score most likely reflects a **semantic clustering artifact**: lidocaine appears frequently in the knowledge graph alongside "topical ophthalmic drug" contexts (e.g., as a procedural anesthetic used during eye surgery and injections), rather than reflecting a genuine disease-modifying mechanistic relationship. No literature or trial evidence currently exists to test this hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No marketing authorizations are present in the current dataset — lidocaine is recorded as **not marketed** (0 licenses on file). Authorization details cannot be summarized until license records are added.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — Data Gap DG001, Blocking severity, requires TFDA/BfArM label retrieval before any safety pre-screen can be completed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has Evidence Level L5 — a TxGNN score with no supporting clinical trials or literature — and the model's own rationale identifies it as a likely false-positive driven by semantic clustering rather than a real mechanistic link. In addition, the Blocking-severity label data gap (DG001) means the candidate cannot even enter S1 safety pre-screening yet.

**To proceed, the following is needed:**
- Retrieve official TFDA/BfArM package insert (warnings, contraindications) to resolve DG001
- Retrieve full DrugBank MOA data to resolve DG002
- Independent literature/mechanistic search specific to lidocaine and corneal/conjunctival epithelial repair, since none currently exists
- Note: among this candidate's top-10 predicted indications, **atopic conjunctivitis (rank 5)** is the only one that reached decision stage S1 with a "Research Question" recommendation (L4, based on a plausible neuro-immune mechanism — nasal/topical anesthesia suppressing reflex-mediated allergic conjunctival responses). If pursuing further work on this drug, that candidate is a substantially stronger starting point than punctate epithelial keratoconjunctivitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

