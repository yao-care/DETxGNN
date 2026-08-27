---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Entacapone
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

Using the drug-repurposing evaluation report template you supplied. This evidence pack is structured with 10 ranked predicted indications, but the requested report format is scoped to `predicted_indications[0]` (rank 1: PLA2G6-associated neurodegeneration). I've generated that report faithfully, and appended a short supplementary note on the other ranked candidates since two of them (rank 4, 7, 10) carry materially stronger mechanistic rationale and actual evidence — omitting that context would understate what this evidence pack actually shows.

---

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT (catechol-O-methyltransferase) inhibitor used as adjunct therapy to levodopa in Parkinson's disease.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only prediction with no real-world evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease, adjunct to levodopa/carbidopa (COMT inhibitor) — based on known drug class background; not confirmed by license data in this evidence pack |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known background information, entacapone is a peripheral COMT inhibitor that blocks the enzymatic breakdown of levodopa, prolonging its central nervous system availability. Its proven efficacy is in reducing motor fluctuations ("wearing-off") in Parkinson's disease when co-administered with levodopa.

PLA2G6-associated neurodegeneration (PLAN, including infantile neuroaxonal dystrophy and its atypical late-onset forms) is a distinct disease driven by loss of PLA2G6 phospholipase A2 function and iron accumulation in the brain. Some atypical, late-onset PLAN subtypes can present with parkinsonism-like rigidity and dystonia, which is the only point of clinical overlap with entacapone's approved use — if such patients were treated with levodopa, entacapone could theoretically play an adjunctive role.

However, this is an indirect, inferential connection. The core pathology of PLA2G6 deficiency (phospholipase dysfunction, iron deposition) does not overlap mechanistically with the COMT/dopamine metabolism pathway that entacapone targets. The high TxGNN score more likely reflects proximity between "neurodegeneration" and "movement disorder" nodes in the underlying knowledge graph rather than a genuine pharmacological relationship. No clinical trials or literature currently support this specific drug-disease pairing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/BfArM label warnings and contraindications are marked as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety pre-assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) — there are no clinical trials, no publications, and no direct molecular mechanism connecting entacapone's COMT-inhibition activity to PLA2G6-associated neurodegeneration's core pathology. The evidence pack's own rationale flags this as a likely knowledge-graph embedding artifact rather than a true pharmacological signal.

**To proceed, the following is needed:**
- Resolution of DG001 (TFDA/BfArM package insert warnings and contraindications) — currently blocking any safety pre-assessment
- Resolution of DG002 (confirmed mechanism of action data from DrugBank) to properly assess mechanistic plausibility
- Preclinical/mechanistic studies specifically testing entacapone in PLA2G6-deficiency disease models
- Confirmation of whether atypical late-onset PLAN patients with parkinsonism-like features are a clinically meaningful subgroup worth targeting

---

### Supplementary Note: Other Candidates in This Evidence Pack

This report is scoped to the rank-1 prediction as specified by the report format, but the evidence pack ranks 10 candidate indications for entacapone, and the strongest mechanistic and evidentiary signals are **not** at rank 1. Three other candidates were scored at decision-stage S1 ("Research Question") rather than Hold, and may warrant independent evaluation:

| Rank | Disease | TxGNN Score | Evidence Level | Notes |
|------|---------|-------------|-----------------|-------|
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L4 | Historical name for early-onset Parkinson's/Parkinson-plus syndrome — direct mechanistic overlap with entacapone's approved use, but no trials/literature target this specific early-onset subgroup. |
| 7 | Lewy body dementia | 99.25% | L4 | Same α-synucleinopathy family as Parkinson's disease; 1 Phase 1 imaging trial ([NCT04246437](https://clinicaltrials.gov/study/NCT04246437)) and 3 literature records exist, though none directly test entacapone. |
| 10 | Progressive supranuclear palsy–corticobasal syndrome | 99.04% | L4 | Atypical parkinsonism (tau-driven, not synuclein); 1 observational gait-analysis trial ([NCT02994719](https://clinicaltrials.gov/study/NCT02994719)) exists but is non-interventional. |

All ten candidates remain at S0/S1 (Hold or Research Question) — none currently justify a "Go" or "Proceed with Guardrails" decision. If further investment is warranted, ranks 4, 7, and 10 are better starting points than rank 1, given their stronger mechanistic proximity to entacapone's established dopaminergic pathway.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

