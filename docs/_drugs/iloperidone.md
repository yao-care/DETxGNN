---
layout: default
title: Iloperidone
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Iloperidone
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

# Iloperidone: From Schizophrenia to Bipolar Mania

## One-Sentence Summary

Iloperidone (Fanapt) is a D2/5-HT2A dual antagonist originally developed and marketed for the treatment of schizophrenia. The TxGNN model's most credible signal among its top predictions points to **manic episodes of Bipolar I Disorder**, an indication that is supported by **1 completed Phase 4 trial**, **1 completed Phase 3 RCT**, and **19 related publications**, including confirmation that this indication received formal regulatory approval in 2024. Nine other very high-scoring TxGNN predictions for this drug are also reported, but none of them have any corroborating clinical trial or literature evidence and are assessed as likely false positives.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per literature evidence, e.g. PMID 22849428, 21446639) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Market Status | ✗ Not marketed (0 authorizations on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Iloperidone is a serotonin/dopamine antagonist (5-HT2A/D2), the same pharmacological class as several atypical antipsychotics already approved for bipolar mania — olanzapine, risperidone, quetiapine, aripiprazole, asenapine, and cariprazine. This shared receptor-binding profile gives strong mechanistic plausibility for extending iloperidone's use from schizophrenia to acute manic/mixed episodes of Bipolar I Disorder.

This is not purely a model-generated hypothesis: PMID 39008105 (*The Medical Letter*, 2024) documents that iloperidone received a **new FDA-approved indication for bipolar disorder in 2024**, and PMID 38236020 reports the pivotal Phase 3, randomized, double-blind, placebo-controlled trial (27 sites, US and international, 2021–2022) that demonstrated significant reduction in Young Mania Rating Scale (YMRS) scores versus placebo. A completed Phase 4 trial (NCT02413918) further examined iloperidone as adjunctive therapy in mixed-state bipolar disorder. Taken together, the TxGNN prediction here aligns with real-world regulatory and clinical outcomes rather than an unvalidated model artifact.

### Other TxGNN High-Score Predictions Without Supporting Evidence

The evidence pack also contains nine other candidate indications with near-identical, extremely high TxGNN scores (~99.999%, ranks 24–39): retinal dystrophy, congenital disorder of glycosylation with defective fucosylation, hydranencephaly, Charcot-Marie-Tooth disease type 1G, perisylvian polymicrogyria syndrome, three forms of syndromic/hereditary myopia, and atypical glycine encephalopathy. None of these have any associated clinical trials, and where literature was retrieved (retinal dystrophy), the papers are unrelated general ophthalmology/genetics topics with no mention of iloperidone or antipsychotic mechanisms. These are judged to be **likely false positives arising from knowledge-graph embedding similarity rather than genuine biological association**, and all carry a "Hold" recommendation. They are not developed further in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02413918](https://clinicaltrials.gov/study/NCT02413918) | Phase 4 | Completed | 41 | Open-label study of iloperidone as adjunctive treatment (with lithium, divalproex, and/or lamotrigine) in mixed states of bipolar disorder; assessed acute and long-term bimodal efficacy and predictors of treatment response. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38236020](https://pubmed.ncbi.nlm.nih.gov/38236020/) | 2024 | RCT (Phase 3) | J Clin Psychiatry | Randomized, double-blind, placebo-controlled trial (27 sites); iloperidone up to 24 mg/day significantly reduced YMRS scores at 4 weeks vs. placebo in adults with bipolar mania. |
| [39008105](https://pubmed.ncbi.nlm.nih.gov/39008105/) | 2024 | Regulatory Update | The Medical Letter | Reports FDA approval of a new bipolar disorder indication for iloperidone (Fanapt). |
| [39800949](https://pubmed.ncbi.nlm.nih.gov/39800949/) | 2025 | Review | Ann Pharmacother | Evaluates efficacy of iloperidone for bipolar I mania and discusses safety profile (QTc prolongation, orthostatic hypotension, metabolic effects). |
| [28817490](https://pubmed.ncbi.nlm.nih.gov/28817490/) | 2017 | Open-label Trial | J Clin Psychopharmacol | Open trial of iloperidone in mixed episodes of bipolar disorder; notes difficulty of treating mixed states and gaps in depression-response reporting for FDA-approved agents. |
| [22900950](https://pubmed.ncbi.nlm.nih.gov/22900950/) | 2012 | Systematic Review/Meta-analysis | CNS Drugs | Compares body weight and metabolic adverse effects of asenapine, iloperidone, lurasidone, and paliperidone in schizophrenia and bipolar disorder. |
| [33177350](https://pubmed.ncbi.nlm.nih.gov/33177350/) | 2021 | Comparative Study | J Clin Psychopharmacol | Compares metabolic characteristics of newer second-generation antipsychotics (including iloperidone) against olanzapine. |
| [41826282](https://pubmed.ncbi.nlm.nih.gov/41826282/) | 2026 | Pharmacogenomic Analysis | Pharmacogenomics J | Secondary analysis of the Phase 3 bipolar mania trial; SLC2A9 variant associated with iloperidone-related uric acid increase. |
| [39126643](https://pubmed.ncbi.nlm.nih.gov/39126643/) | 2024 | Review (Safety/QTc) | Expert Opin Drug Saf | Updated safety review of atypical antipsychotics and QTc/Torsades de Pointes risk, relevant to iloperidone's known cardiac signal. |
| [22849428](https://pubmed.ncbi.nlm.nih.gov/22849428/) | 2012 | Review | Expert Opin Pharmacother | Primer on iloperidone, asenapine, and lurasidone; confirms iloperidone's original schizophrenia indication and shared receptor mechanism relevant to bipolar disorder. |
| [18095919](https://pubmed.ncbi.nlm.nih.gov/18095919/) | 2008 | Review | Expert Opin Investig Drugs | Early profile of iloperidone as a 5-HT2A/D2 antagonist under development for schizophrenia and bipolar disorder. |

---

## Market Information

The drug is currently **not marketed** and holds **no marketing authorizations** on file (0 licenses recorded). No dosage form or approved-indication data are available for local review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted bipolar mania indication is supported by a completed Phase 3 RCT, a completed Phase 4 trial, and confirmed 2024 regulatory approval in at least one market, giving it L1-level evidence — substantially stronger than iloperidone's other nine TxGNN predictions, which lack any clinical or mechanistic support and should be held. However, the complete absence of local marketing authorization, package-insert warnings/contraindications, and MOA documentation (both flagged as Blocking/High severity data gaps) means the candidate cannot yet clear initial safety screening (S1).

**To proceed, the following is needed:**
- Obtain the official package insert (warnings, contraindications, DDI) from the relevant regulatory authority to close data gap DG001 (Blocking)
- Retrieve formal mechanism-of-action documentation from DrugBank to close data gap DG002 (High)
- Confirm local marketing authorization status and pathway if repurposing submission is pursued
- Monitor known class-wide risks identified in the literature (QTc prolongation, orthostatic hypotension, metabolic/weight effects, akathisia) as part of any safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

