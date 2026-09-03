---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# ARIPIPRAZOLE: From Antipsychotic Use to Major Affective Disorder (Adjunctive Treatment)

## One-Sentence Summary

> Aripiprazole is a dopamine D2/D3 partial agonist antipsychotic; this evidence pack does not record its original approved indication (data gap), though real-world monographs list schizophrenia and bipolar I disorder.
> The TxGNN model predicts it may be effective for **Major Affective Disorder** (adjunctive treatment of major depressive disorder),
> with **60+ clinical trials** and **20 publications** currently supporting this direction, including a completed Phase 3 RCT already establishing this use in real-world practice.

> ⚠️ **Data note**: `drug.original_indications` and `taiwan_regulatory.licenses` are both empty in this evidence pack, and `market_status` reads "Not marketed." This conflicts with aripiprazole's well-documented global approval history (Abilify®) and should be verified against source data before this report is used for regulatory decisions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | **[Data Gap]** — not populated in evidence pack (`original_indications` empty) |
| Predicted New Indication | Major Affective Disorder (adjunctive to antidepressant therapy in MDD) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Market Status (this dataset) | Not marketed / 0 authorizations recorded |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` = [Data Gap]). Based on known pharmacology cited within the repurposing rationale, aripiprazole is a **dopamine D2/D3 partial agonist**, with additional **5-HT1A partial agonist** and **5-HT2A antagonist** activity. This receptor profile is the established pharmacological basis for its use as an antidepressant augmentation agent.

The predicted new indication — major affective disorder / major depressive disorder (MDD) — is mechanistically continuous with aripiprazole's known antipsychotic activity: partial dopaminergic and serotonergic modulation is theorized to correct monoaminergic dysregulation implicated in treatment-resistant depression. In fact, aripiprazole augmentation of antidepressants has already received regulatory approval and extensive clinical validation outside of this dataset (e.g., FDA approval as an adjunct for MDD), which is consistent with — and substantially strengthens — the TxGNN prediction.

The evidence pack itself flags an important caveat: because `original_indications` and `licenses` are empty, the internal consistency between "original indication" and "predicted indication" cannot be verified from this dataset alone. The mechanistic rationale should therefore be read as corroborated by external knowledge, not by this evidence pack's regulatory fields.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Completed | 225 | Pivotal double-blind, placebo-controlled trial of reduced-dose aripiprazole adjunctive to antidepressant therapy in MDD with inadequate response to prior treatment |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Placebo-controlled, parallel-group study of aripiprazole adjunctive to SSRI/SNRI in MDD |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | Completed | 349 | 14-week randomized, double-blind, placebo-controlled adjunctive trial in MDD with incomplete response to open-label antidepressant |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (aripiprazole/sertraline combination) vs sertraline monotherapy in MDD with incomplete response |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Completed | 731 | 52-week placebo-controlled study of IM depot aripiprazole as maintenance therapy in bipolar I disorder |
| [NCT01284218](https://clinicaltrials.gov/study/NCT01284218) | N/A | Completed | 23,514 | Retrospective real-world database study of health care utilization/costs with adjunctive aripiprazole vs other augmentation therapies in MDD |
| [NCT01429831](https://clinicaltrials.gov/study/NCT01429831) | Phase 4 | Completed | 300 | Taiwan real-world observational study of aripiprazole augmentation effectiveness/tolerability in MDD inadequate responders |
| [NCT00953745](https://clinicaltrials.gov/study/NCT00953745) | N/A | Completed | 43 | PET/fMRI mechanistic study testing dopaminergic pathway hypothesis for aripiprazole augmentation in treatment-resistant depression |
| [NCT00873795](https://clinicaltrials.gov/study/NCT00873795) | N/A | Completed | 41 | Small comparative trial of low-dose aripiprazole + sertraline vs sertraline alone in fresh MDD |
| [NCT05473741](https://clinicaltrials.gov/study/NCT05473741) | N/A | Completed | 51 | Longitudinal cohort on breakthrough symptom risk in remitted patients on long-acting antipsychotic maintenance therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | RCT meta-analysis | PLoS One | Largest systematic review/meta-analysis of RCTs on aripiprazole or bupropion augmentation and switching in treatment-resistant depression/MDD |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Network meta-analysis | J Affect Disord | Compares efficacy and discontinuation of augmentation agents (incl. aripiprazole) in treatment-resistant depression |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT | CNS Drugs | Pivotal safety/tolerability/PK study of aripiprazole 2-month long-acting injectable in schizophrenia and bipolar I disorder |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic review | Neuropsychopharmacol Rep | Network meta-analysis comparing brexpiprazole, aripiprazole, and placebo for MDD in Japanese patients |
| [36239033](https://pubmed.ncbi.nlm.nih.gov/36239033/) | 2023 | RCT | J Psychopharmacol | Randomized, double-blind, placebo-controlled trial of aripiprazole adjunctive therapy in MDD with somatic symptoms (with EEG evidence) |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic review/meta-analysis | Prim Care Companion CNS Disord | Long-term efficacy and tolerability of adjunctive aripiprazole for MDD |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic review/meta-analysis | Psychol Med | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in adult MDD |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | Review of pharmacotherapy for treatment-resistant depression: antidepressants and atypical antipsychotics, including aripiprazole |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | Review of antipsychotic pharmacotherapies for treatment-resistant depression within the evolving therapeutic landscape |
| [21254788](https://pubmed.ncbi.nlm.nih.gov/21254788/) | 2011 | Review | CNS Drugs | Overview and clinical trial data implications for aripiprazole as adjunctive therapy in MDD |

---

## Germany Market Information

No marketing authorizations were found in this evidence pack (`taiwan_regulatory.total_licenses = 0`, `licenses = []`, `market_status = "Not marketed"`). This is inconsistent with aripiprazole's known global regulatory history and should be treated as a data gap requiring source verification rather than a factual statement about market absence.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and `ddi` are all unpopulated / [Data Gap] in this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by L1-level evidence — a completed Phase 3 RCT (NCT00683852) plus multiple additional completed Phase 3 trials, a large real-world database study (n=23,514), and several RCT-level meta-analyses — and is directionally consistent with aripiprazole's well-established real-world use as antidepressant augmentation. However, critical drug-level fields (MOA, safety warnings, contraindications, DDI, market authorizations, original indication) are all data gaps in this pack, which blocks a full S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/regulatory label (仿單) warnings and contraindications (currently Blocking data gap, DG001)
- Verified drug-level MOA from DrugBank (DG002)
- Reconciliation of `original_indications` / `market_status` / `licenses` fields against known real-world approval status for aripiprazole
- Drug interaction (DDI) profile, particularly for antidepressant/antipsychotic combination use in MDD augmentation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

