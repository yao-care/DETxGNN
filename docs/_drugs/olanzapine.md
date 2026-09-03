---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 3
---

# Olanzapine
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

Using the drug-repurposing evaluation report format directly, since the Evidence Pack is fully self-contained (all data already supplied — no additional lookups needed). One structural note before the report: this Evidence Pack is a **multi-indication candidate** (`candidate_id: TW-DB00334-multi`) with three TxGNN-predicted indications of very different evidence quality. I've adapted the template to cover all three transparently rather than silently dropping two of them, and I have not filled in the two flagged data gaps (original MOA, original indication text) with outside knowledge — per the evidence pack's own governance rules (DG001/DG002), these remain flagged.

---

# Olanzapine: From Antipsychotic Therapy to Anxiety and Mood Disorder Augmentation

## One-Sentence Summary

Olanzapine's formal original-indication text and mechanism of action are not populated in this evidence pack (flagged as data gaps DG001/DG002); its supporting literature identifies it as a second-generation (atypical) antipsychotic used across schizophrenia, bipolar disorder, and treatment-resistant mood/anxiety augmentation. TxGNN predicts three new indications — **Agoraphobia**, **Dysthymic Disorder**, and **Benign Paroxysmal Torticollis of Infancy** — but only the first two are backed by actual literature (7 and 5 publications respectively, no RCTs); the third has a very high TxGNN score but zero supporting evidence and an implausible mechanistic link, and is recommended for **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Data Gap DG001/DG002). Literature context indicates second-generation (atypical) antipsychotic, used in schizophrenia/bipolar disorder and as augmentation therapy |
| Predicted New Indications | 1) Agoraphobia (score 99.47%, rank 6078) — L3, Research Question<br/>2) Dysthymic Disorder (score 99.28%, rank 7787) — L3, Research Question<br/>3) Benign Paroxysmal Torticollis of Infancy (score 99.54%, rank 5562) — L5, Hold |
| Evidence Level (overall) | L3 for Agoraphobia / Dysthymic Disorder; L5 for Infantile Torticollis |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (safety data gap is Blocking) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Olanzapine is not available in this evidence pack (Data Gap DG002). Based on the supporting literature retrieved for the two credible predicted indications, Olanzapine is used clinically as a second-generation (atypical) antipsychotic with 5-HT2A antagonism and modest H1-mediated sedation, properties that have been explored as augmentation therapy in mood and anxiety disorders.

**Agoraphobia** is most commonly comorbid with panic disorder. The literature shows Olanzapine has been studied — and used in case reports — as an SSRI-augmentation agent in treatment-resistant panic disorder (with or without agoraphobia), including a 12-week open-label fixed-dose trial (5 mg/day) showing efficacy on panic and anticipatory anxiety scales (PMID 16415705). However, the evidence is concentrated on "treatment-resistant panic disorder" rather than agoraphobia as a standalone diagnosis, making this an indirect extension rather than a disorder-specific study population.

**Dysthymic Disorder** (persistent depressive disorder) shares neurobiological overlap with major depressive disorder, where second-generation antipsychotics — including Olanzapine — have documented augmentation use (Cochrane review, PMID 21154393). Case-level and open-label evidence exists in populations with comorbid borderline personality disorder and dysthymia (PMID 10578457) and in bipolar disorder with comorbid anxiety/OCD (PMID 25012437), but no study targets dysthymia as an isolated primary indication.

**Benign Paroxysmal Torticollis of Infancy**, by contrast, has a TxGNN score higher than the other two predictions but no clinical trial or literature evidence at all, and the proposed rationale (CACNA1A/migraine-variant/vestibular pathophysiology) has no established biological connection to Olanzapine's D2/5-HT2A antagonism. This is very likely a knowledge-graph artifact (sedative/antipsychotic nodes linking indirectly to an unexplained pediatric movement disorder) rather than a real pharmacological signal, and pediatric/infant safety data for Olanzapine is essentially absent — the mechanistic plausibility here is very low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications (Agoraphobia, Dysthymic Disorder, or Benign Paroxysmal Torticollis of Infancy).

---

## Literature Evidence

### Agoraphobia

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label Trial (12-week, fixed-dose) | Journal of Clinical Psychopharmacology | Olanzapine 5 mg/d as SSRI augmentation in 31 treatment-resistant panic disorder patients (with/without agoraphobia); improved panic and anticipatory anxiety scores |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Review | Psychotherapy and Psychosomatics | Integrative review of pharmacological, psychotherapeutic, and neurostimulatory options for treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Review | Expert Opinion on Pharmacotherapy | Systematic review of treatment-resistant panic disorder, noting ~1/3 of patients have persistent symptoms after standard treatment |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | Journal of Affective Disorders | 24-month outcomes: comorbid agoraphobia/panic/SAD/GAD/OCD impact bipolar I disorder course |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case Report | Pharmacopsychiatry | Remission of chronic panic disorder with Olanzapine + paroxetine combination |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case Report | Psychiatria Danubina | CBT case of panic disorder with agoraphobia comorbid with psychosis |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case Report | American Journal of Psychiatry | Early case report on Olanzapine and panic attacks |

### Dysthymic Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Second-generation antipsychotics, including Olanzapine, as augmentation in major depressive disorder and dysthymia |
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Open-label Trial | Biological Psychiatry | Olanzapine safety/efficacy in borderline personality disorder with comorbid dysthymia |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review | Bipolar Disorders | Evidence-based options for treatment-resistant bipolar disorder, incl. antipsychotic augmentation |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review | Molecular Psychiatry | Mechanistic review of substituted benzamides in dysthymia and schizophrenia negative symptoms (not Olanzapine-specific) |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Systematic Review / Meta-analysis | Human Psychopharmacology | Efficacy of amisulpride (a different second-generation antipsychotic) for depressive symptoms — indirect comparator evidence, not Olanzapine-specific |

### Benign Paroxysmal Torticollis of Infancy

Currently no related literature available.

---

## Germany Market Information

Olanzapine is currently **not marketed** in Germany under this evidence pack (0 authorizations on record). No product license entries are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack flags the TFDA package insert warnings/contraindications (DG001) as a **Blocking** data gap — its stated impact is that the candidate **cannot proceed to the S1 safety pre-assessment stage** until this data is obtained. No drug-drug interaction records were found in the current DDI query (`not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The candidate cannot proceed past initial screening because the TFDA package insert (warnings/contraindications) data gap is explicitly marked **Blocking** — mechanism of action is also unverified (High severity gap). Without this, no responsible S1 safety pre-assessment is possible for any of the three predicted indications.
- Of the three TxGNN predictions, only Agoraphobia and Dysthymic Disorder have real (if indirect, low-tier: open-label/case-report/review-level) supporting literature and warrant tracking as **Research Questions**; Benign Paroxysmal Torticollis of Infancy has no supporting evidence, an implausible mechanistic link, and involves an infant population with no pediatric safety data — it should be deprioritized/dropped rather than advanced.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — required to clear the Blocking gap (DG001) before any safety assessment
- Confirmed mechanism of action from DrugBank or equivalent primary source (DG002)
- For Agoraphobia / Dysthymic Disorder: prospective or controlled trial data specific to these diagnoses (current evidence is comorbidity-adjacent, not disorder-specific)
- Formal original-indication and Germany market history documentation, if this candidate is to be pursued further
- Re-evaluation (or removal) of the Benign Paroxysmal Torticollis of Infancy signal, given its lack of biological plausibility and absent evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

