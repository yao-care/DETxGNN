---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine is a rapid-acting insulin analogue already used for glycaemic control in diabetes mellitus. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**, supported by **75+ clinical trials** and **20 publications** — but this indication substantially overlaps with the drug's existing, well-established clinical use rather than representing a novel repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (glycaemic control) — detailed approved indication text not on file (data gap) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known pharmacology, insulin glulisine is a recombinant rapid-acting human insulin analogue that binds the insulin receptor to lower blood glucose, and it is already used clinically for mealtime (bolus) glycaemic control in both type 1 and type 2 diabetes.

Because type 1 diabetes mellitus is characterised by absolute insulin deficiency, insulin replacement — including rapid-acting analogues like glulisine — is the established standard of care rather than a new therapeutic hypothesis. The evidence pack itself flags this explicitly: the mechanistic link here is "the drug's own original indication rather than a repurposing inference," meaning the TxGNN prediction largely recovers existing, well-documented clinical knowledge instead of surfacing a novel use.

It is also worth noting that among the ten TxGNN predictions supplied in this evidence pack, only rank 1 (Type 1 Diabetes Mellitus) is backed by direct trial/literature evidence (L1). Ranks 2–10 (e.g., thiamine-responsive dysfunction syndrome, opsismodysplasia, stiff person syndrome, lipodystrophy variants) all scored L4–L5 with no supporting trials or literature, and several appear to reflect knowledge-graph artefacts — including at least two cases where the "predicted indication" is actually a known adverse effect of insulin injection (localized lipodystrophy/lipoatrophy) rather than a treatable target, i.e., a possible reversed-causality signal. These should not be advanced without independent mechanistic review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Phase 3 | Completed | 224 | Non-inferior immunogenicity, efficacy and safety of biosimilar GP40321 vs Apidra® in T1DM |
| [NCT01194258](https://clinicaltrials.gov/study/NCT01194258) | Phase 2 | Completed | 132 | Double-blind crossover comparing rHuPH20-formulated prandial insulins to insulin lispro |
| [NCT02509429](https://clinicaltrials.gov/study/NCT02509429) | Phase 2 | Completed | 24 | Closed-loop artificial pancreas reduces nocturnal hypoglycaemia in children with T1DM |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week efficacy/safety of insulin glulisine + glargine in T1DM (HbA1c, hypoglycaemia) |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Glulisine vs lispro (with glargine) in T1/T2DM: efficacy, safety, hypoglycaemia frequency |
| [NCT01159353](https://clinicaltrials.gov/study/NCT01159353) | Phase 1 | Completed | 37 | PK/PD comparison of glulisine vs aspart post-prandial glucose control |
| [NCT02871089](https://clinicaltrials.gov/study/NCT02871089) | N/A | Active, not recruiting | 96 | Closed-loop insulin delivery from T1D onset; residual beta-cell function |
| [NCT02914886](https://clinicaltrials.gov/study/NCT02914886) | Phase 4 | Completed | 14 | Zinc-free insulin (glulisine) effect on lipoatrophy in T1D pump users |
| [NCT03495908](https://clinicaltrials.gov/study/NCT03495908) | N/A | Completed | 136 | Regular vs rapid-acting insulin via V-Go wearable delivery device |
| [NCT02814123](https://clinicaltrials.gov/study/NCT02814123) | Phase 2 | Completed | 28 | Closed-loop fast-acting insulin ± pramlintide co-administration in T1DM |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multinational RCT comparing efficacy/safety of glulisine vs lispro in adults with T1DM |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | RCT (Phase III) | Diabetes Obes Metab | Biosimilar insulin glulisine (T-Glu) non-inferior to originator (R-Glu) in T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | 3-way crossover: glulisine vs aspart vs lispro via CSII pump in T1DM |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 26-week trial: comparable efficacy/safety of glulisine vs lispro in pediatric T1DM |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes Obes Metab | Glulisine vs lispro efficacy/safety in Japanese patients with T1DM |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Cohort/Comparative | Acta Diabetol | Real-world comparison of glulisine vs lispro/aspart for CSII in T1DM |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort | Pediatr Int | Glulisine for CSII in pediatric T1DM: 1-year efficacy/safety data |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK Study | Diabetes Care | Pharmacokinetics and prandial glucose control of glulisine in children/adolescents with T1DM |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Overview of insulin glulisine's role in diabetes management |
| [35650058](https://pubmed.ncbi.nlm.nih.gov/35650058/) | 2022 | Case report | Nihon Ronen Igakkai Zasshi | Switching degludec→glulisine improved nocturnal hypoglycaemia/arrhythmia in elderly T1DM patient |

---

## Germany Market Information

Currently not marketed in Germany — no marketing authorizations are on file for this candidate (0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings/contraindications and DDI data are currently unavailable — flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence is strong (L1: multiple completed Phase 2/3 RCTs, including a 2026 Phase III biosimilar trial) for insulin glulisine's efficacy and safety in type 1 diabetes mellitus. However, this is confirmatory evidence for an already-known use rather than a novel repurposing signal, and two blocking/high-severity data gaps (TFDA labeling, MOA documentation) remain unresolved before any safety-relevant decision can be finalized.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (DG001, blocking — required before S1 safety review)
- Detailed mechanism of action documentation from DrugBank (DG002)
- Clarification of regulatory/commercial status given zero current marketing authorizations
- Reassessment of whether rank-1 "prediction" should be reclassified as label-confirmation rather than repurposing, and independent review of ranks 2–10 (all L4/L5, including two likely reversed-causality signals) before any further action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

