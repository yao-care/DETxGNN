---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 3
---

# Pitolisant
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

# Pitolisant: From Narcolepsy to Insomnia (Signal Requires Verification)

## One-Sentence Summary

> Pitolisant is a histamine H3-receptor inverse agonist known from the literature for narcolepsy and OSA-related excessive daytime sleepiness — i.e., a **wake-promoting** drug.
> The TxGNN model predicts it may be effective for **Insomnia**, but this is supported by only **1 withdrawn trial** (for an unrelated indication) and **8 publications**, most of which actually describe the opposite clinical effect.
> This prediction shows a direct mechanistic contradiction and should be treated as a research question, not an actionable signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with/without cataplexy (per literature evidence only; no formal regulatory record in this dataset) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal drugbank MOA data is not available for this drug (data gap). Based on the literature evidence attached to this candidate, pitolisant is a **selective histamine H3-receptor inverse agonist/antagonist**. By blocking H3 autoreceptors, it increases histaminergic, noradrenergic, and dopaminergic tone in the brain, producing a **wake-promoting** effect. This mechanism is the basis for its approved use in narcolepsy (with or without cataplexy) and its investigational use for residual excessive daytime sleepiness (EDS) in OSA patients on CPAP.

This is precisely why the "insomnia" prediction is mechanistically counter-intuitive: a drug designed to increase wakefulness would be expected to *worsen*, not treat, insomnia. Seven of the eight literature citations attached to this indication actually describe pitolisant's use for **narcolepsy or EDS in OSA** — the clinical opposite of insomnia — and the single associated clinical trial (also withdrawn, zero enrollment) targeted alcohol use disorder, not sleep initiation/maintenance problems.

The most plausible explanation, consistent with the rationale already flagged in this evidence pack, is that the TxGNN knowledge graph node labeled "insomnia (disease)" may be embedding-adjacent to narcolepsy/hypersomnia/EDS disease nodes, producing a **false-positive association** rather than a genuine therapeutic hypothesis. This needs to be manually verified against the KG's disease ontology before any further evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Designed to evaluate pitolisant for **alcohol use disorder** (heavy drinking days as primary endpoint), not insomnia. Withdrawn with zero enrollment — no efficacy or safety data generated, and the target indication does not match the predicted one. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | Lancet Neurology | Phase 3 RCT of pitolisant in pediatric narcolepsy with/without cataplexy — confirms wake-promoting efficacy, not an insomnia indication. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | RCT in OSA patients with residual excessive daytime sleepiness despite CPAP — pitolisant used to *increase* wakefulness. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | RCT for daytime sleepiness in OSA patients refusing CPAP — again a wake-promoting use, clinically opposite to insomnia treatment. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de Neurología | Real-world study of pitolisant in treatment-refractory type 1 narcolepsy with cataplexy. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | General review of histamine receptor pharmacology (H1–H4); mechanistic background only, not indication-specific. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Review of pitolisant's development and place in therapy for narcolepsy. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Reviews histaminergic system changes in neuropsychiatric disease; notes pitolisant is used for EDS in narcolepsy, contrasted with H1-antagonist doxepin being the drug actually used for insomnia. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review/Mechanistic | Clinical Neuropharmacology | Early mechanistic review of pitolisant as a stimulant for narcolepsy-cataplexy in teenagers. |

**Note:** No publication in this evidence set actually studies pitolisant for insomnia treatment. Several sources explicitly describe the opposite pharmacological effect (wake-promotion).

---

## Germany Market Information

Pitolisant is currently **not marketed** in this jurisdiction, and no marketing authorization records are available in the dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (insomnia) is mechanistically implausible given pitolisant's well-documented wake-promoting pharmacology, and the only attached clinical trial is unrelated and withdrawn. The bulk of the literature evidence actually supports the opposite clinical use (EDS/narcolepsy), suggesting the TxGNN signal is likely a knowledge-graph artifact rather than a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Manual verification of the "insomnia (disease)" node definition and its graph neighbors in the TxGNN knowledge graph, to rule out confusion with narcolepsy/hypersomnia/EDS nodes
- Formal DrugBank MOA confirmation (currently a data gap, DG002)
- TFDA/BfArM label warnings and contraindications (currently a blocking data gap, DG001) before any safety-relevant evaluation
- If the KG node is confirmed as true insomnia (not a mislabeled hypersomnia-adjacent node), dedicated preclinical or clinical insomnia data would be required before this candidate could be reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

