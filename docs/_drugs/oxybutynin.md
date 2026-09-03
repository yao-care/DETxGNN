---
layout: default
title: Oxybutynin
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: Original Indication Not on File → Restless Legs Syndrome (Predicted)

## One-Sentence Summary

The original approved indication for oxybutynin is not documented in this evidence pack (a flagged data gap), so the historical use case cannot yet be confirmed here.
The TxGNN model's top prediction is **Restless Legs Syndrome**, but this candidate currently has **0 clinical trials** and **0 publications** supporting it — evidence is model-only (L5).
Two other candidates were also screened (gastroduodenitis, peptic ulcer disease), neither with a strong mechanistic case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap — see DG001/DG002; no `original_indications` or license text captured) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for oxybutynin is not available in this evidence pack, and the original indication itself is also undocumented here, which limits any formal mechanistic-overlap comparison. Oxybutynin is broadly known in pharmacology as a muscarinic (M3) receptor antagonist with antispasmodic activity, primarily acting on smooth muscle tone — but this is external background, not confirmed within the pack.

For the top-ranked candidate, restless legs syndrome, the evidence pack's own repurposing rationale states there is **no plausible mechanistic connection**: RLS pathophysiology centers on dopaminergic system dysfunction and abnormal brain iron metabolism, neither of which is addressed by anticholinergic (M3-antagonist) activity. The high TxGNN score likely reflects an indirect knowledge-graph association — such as shared comorbidities or symptom overlap in the training data — rather than genuine pharmacological evidence.

Two other candidates were screened at the same S0 stage: **gastroduodenitis** (no mechanistic rationale — anticholinergics do not treat mucosal inflammation and may worsen gastric emptying) and **peptic ulcer disease** (a historical, pre-PPI-era rationale exists — anticholinergics were once used to reduce vagally-mediated acid secretion — but this approach has been fully superseded by PPI + eradication therapy, and is accompanied by a case report of oxybutynin-induced reflux esophagitis, a risk signal rather than supporting evidence).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Oxybutynin is not currently marketed in Germany, and no authorization records are available in this evidence pack.

---

## Safety Considerations

Safety data (key warnings, contraindications, drug interactions) has not yet been retrieved for this evidence pack — this is flagged as a **Blocking** data gap (DG001), meaning the candidate cannot proceed to formal safety (S1) evaluation until the official package insert is sourced and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (restless legs syndrome) lacks any clinical trial or literature support and, per the pack's own rationale, lacks mechanistic plausibility. Combined with the absence of confirmed original-indication data, missing MOA data, and a Blocking gap in safety/label information, this candidate set is not ready to advance.

**To proceed, the following is needed:**
- Retrieve official package insert / label warnings and contraindications (DG001, Blocking)
- Obtain verified mechanism of action data for oxybutynin (DG002, High)
- Confirm and document the drug's original approved indication(s), currently missing from this pack
- If revisiting peptic ulcer disease, weigh the outdated mechanistic rationale against modern standard-of-care and the reported reflux esophagitis risk before any further scoring
- No further action recommended on restless legs syndrome or gastroduodenitis absent new mechanistic or clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

