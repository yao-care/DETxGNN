---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

> Lurasidone (development code SM-13496) is a second-generation atypical antipsychotic originally used to treat schizophrenia.
> The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder (Bipolar Disorder)**,
> with **15 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per literature evidence; no German market authorization data available to confirm approved label indication) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, structured mechanism-of-action data is not available in the regulatory record (marked as Data Gap). However, the evidence pack's repurposing rationale confirms that Lurasidone (development code SM-13496) is a second-generation atypical antipsychotic that primarily antagonizes D2 and 5-HT2A/5-HT7 receptors — a receptor profile shared by other agents used in bipolar disorder management.

Schizophrenia and bipolar affective disorder are both severe psychiatric conditions that respond to dopaminergic/serotonergic modulation, and atypical antipsychotics as a class are commonly repurposed across these two indications. Clinically, Lurasidone has already received regulatory approval in multiple countries (including the US) for bipolar I depression, both as monotherapy and as adjunctive therapy with lithium or divalproex — this is independently confirmed in the literature evidence (e.g., PMID 31957501, PMID 24170243), not merely a model-generated hypothesis. This real-world precedent strongly supports the plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Lurasidone adjunctive to lithium/divalproex for prevention of recurrence in bipolar I disorder |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | SM-13496 (lurasidone) vs. placebo, pivotal trial in bipolar I depression |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | Completed | 702 | 104-week open-label extension evaluating long-term safety/effectiveness in pediatric bipolar patients |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety of SM-13496 (lurasidone) in bipolar I disorder |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | Open-label extension of lurasidone adjunctive to lithium/divalproex in bipolar I disorder |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | Randomized, double-blind, placebo-controlled trial of lurasidone in children/adolescents with bipolar I depression |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | Large SMART trial comparing lurasidone, cariprazine, quetiapine, and aripiprazole/escitalopram for bipolar depression |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | Randomized, placebo-controlled flexible-dose study of lurasidone for bipolar I depression (terminated early) |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | Lurasidone adjunctive therapy for cognitive functioning in euthymic bipolar I/II patients (ELICE-BD) |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | Lurasidone vs. treatment-as-usual for cognitive functioning in euthymic bipolar patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Review (Meta-analysis) | BMJ Mental Health | Systematic review and dose-response meta-analysis of lurasidone efficacy/acceptability in bipolar depression |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Review (Network Meta-analysis) | Lancet Psychiatry | Comparative efficacy/tolerability of pharmacological interventions (incl. lurasidone) for acute bipolar depression |
| [31957501](https://pubmed.ncbi.nlm.nih.gov/31957501/) | 2020 | Review | Expert Opinion on Pharmacotherapy | Evaluates lurasidone as a treatment option for bipolar I depression, monotherapy and adjunct use |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Review (Guideline) | Bipolar Disorders | CANMAT/ISBD 2018 guidelines for management of bipolar disorder |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Review (Guideline) | Bipolar Disorders | CANMAT/ISBD recommendations for bipolar disorder with mixed presentations |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Diagnosis and treatment overview of bipolar disorder |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | American Journal of Psychiatry | Commentary confirming lurasidone's approved use in bipolar disorder |
| [25963405](https://pubmed.ncbi.nlm.nih.gov/25963405/) | 2016 | Review | Asia-Pacific Psychiatry | Discusses lurasidone (with quetiapine) as FDA-approved for bipolar depression |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Review (Network Meta-analysis) | Molecular Psychiatry | Antipsychotics/mood stabilizers for bipolar disorder maintenance phase |
| [40808269](https://pubmed.ncbi.nlm.nih.gov/40808269/) | 2025 | Review (Consensus) | Bipolar Disorders | ISBD Task Force consensus recommendations on treatment-resistant bipolar depression |

---

## Germany Market Information

Lurasidone currently has **no market authorization on record in Germany** (market status: Not Marketed, 0 authorizations). No BfArM license entries are available in this evidence pack to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is strong (L1) — multiple completed Phase 3 RCTs specifically on Lurasidone in bipolar I depression (e.g., NCT01986101, n=525; NCT01358357, n=965; NCT02046369, n=350) plus consistent literature support, and Lurasidone is already approved for bipolar depression in other markets. However, the drug is not currently marketed in Germany and key safety/regulatory data (TFDA/BfArM label warnings, contraindications, MOA confirmation) remain unresolved data gaps that block full safety evaluation (S1).

**To proceed, the following is needed:**
- Official German (BfArM) package insert — warnings, contraindications, and precautions (DG001, blocking)
- Confirmed mechanism-of-action documentation from DrugBank or manufacturer (DG002)
- Assessment of German market authorization pathway, since the drug is not currently marketed
- Drug-drug interaction (DDI) data, as none is currently available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

