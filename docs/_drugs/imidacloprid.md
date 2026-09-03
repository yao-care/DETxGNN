---
layout: default
title: Imidacloprid
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 9
---

# Imidacloprid
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

# Imidacloprid: From Insecticide to Cauda Equina Syndrome

## One-Sentence Summary

> Imidacloprid is a neonicotinoid insecticide with no approved human indication; it is not a marketed pharmaceutical product.
> The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the drug's own mechanism of action (insect-selective nicotinic receptor agonism with minimal vertebrate affinity) provides no biological rationale for this or any of the other candidate indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — Imidacloprid is a neonicotinoid insecticide, not an approved human pharmaceutical |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% (rank 208 of all candidate diseases) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

It is not. Imidacloprid is an insect-selective nicotinic acetylcholine receptor (nAChR) agonist. Its selectivity for insect-type nAChR subunits over vertebrate nAChR — combined with very low affinity for the vertebrate receptor — is precisely the pharmacological basis for its safety profile as an insecticide. This is the opposite of a property one would look for when repurposing a compound for a human neurological condition.

Cauda equina syndrome is a mechanical/compressive neurological emergency (nerve root compression at the lumbosacral spinal canal), typically caused by disc herniation, tumor, trauma, or infection. There is no plausible pharmacological pathway by which a vertebrate-nAChR-sparing insecticide would address nerve root compression. The TxGNN score most likely reflects graph topology similarity (shared metadata or indirect network paths) rather than any underlying biological signal — this interpretation is consistent with the evidence pack's own assessment.

The same conclusion applies to the other eight ranked predictions in this evidence pack (obsolete neurogenic bladder, irritable bowel syndrome, esophageal disorders, mitral valve prolapse and its subtypes, neurocirculatory asthenia): all are scored L5, all carry "Hold" recommendations, and none have a documented mechanistic link to imidacloprid's known pharmacology. Where clinical trials or literature were retrieved for lower-ranked candidates (e.g., IBS, esophageal disease), reviewer notes confirm these are false-positive matches — the retrieved studies involve unrelated interventions (osteopathic manipulation, radiotherapy, endoscopy techniques) that were pulled in solely because of disease-name overlap, not because they studied imidacloprid. The one genuine imidacloprid-related record (PMID 29506575) is a veterinary study of a topical imidacloprid-moxidectin antiparasitic product in dogs with esophageal spirocercosis — a parasitic infection, not a human esophageal disease, and not relevant to human repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Imidacloprid holds no marketing authorizations in Germany (0 licenses on file). It is registered and used exclusively as an agricultural/veterinary insecticide (e.g., flea/tick topical products, crop protection), not as a human pharmaceutical product.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: The evidence pack flags TFDA-equivalent labeling/warnings and contraindication data as a Blocking data gap — this must be resolved from regulatory sources such as veterinary product SmPCs and pesticide safety data sheets before any further evaluation, since no human-use labeling exists.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Imidacloprid is not a human pharmaceutical, has no marketing authorization in Germany, and none of the nine TxGNN-predicted indications (including the top-ranked Cauda Equina Syndrome) are supported by clinical trials, literature, or a plausible mechanistic rationale. The drug's core pharmacological property — sparing vertebrate nAChR — argues against, rather than for, human therapeutic repurposing. This candidate does not meet the minimum evidentiary bar to advance past S0.

**To proceed, the following is needed:**
- Confirmation of human safety/toxicology data (currently a Blocking data gap) — critical given imidacloprid's use as a pesticide
- Independent mechanistic validation explaining why a vertebrate-nAChR-sparing insecticide would have any activity in the predicted indications
- Re-evaluation of the TxGNN prediction itself, given the high likelihood these are graph-topology artifacts rather than biologically grounded signals
- If none of the above can be established, this candidate should be deprioritized/closed rather than held indefinitely
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

