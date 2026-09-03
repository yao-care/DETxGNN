---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy to Migraine Prevention

## One-Sentence Summary

Lacosamide is a third-generation antiepileptic drug (AED), used clinically for partial-onset seizures via sodium-channel modulation. Among 10 candidate indications flagged by the TxGNN model, **migraine disorder** stands out as the most evidence-backed repurposing candidate — not the top TxGNN score, but the only one supported by a **completed head-to-head Phase 3 RCT with published positive results**, **7 total clinical trials**, and **17 supporting publications**, including direct mechanistic (CGRP/cortical spreading depolarization) and clinical efficacy data.

> Note: This evidence pack contains 10 TxGNN-predicted indications for lacosamide, each independently scored. Rank 1 by raw TxGNN score ("manic bipolar affective disorder," 99.96%) currently has only a single recruiting trial and unclassified/tangential literature — its evidence base is far weaker than migraine's. This report focuses on **migraine disorder**, the indication with the strongest actual clinical evidence in the pack (evidence level L1, decision stage S3).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures) — inferred from supporting literature ("FDA-approved for treating partial seizures," third-generation AED); formal label/indication text is not available in this evidence pack |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this evidence pack (flagged as data gap DG002). Based on the supporting literature, lacosamide selectively enhances the **slow inactivation of voltage-gated sodium (Nav) channels**, stabilizing hyperexcitable neuronal membranes — the same mechanistic class as other AEDs (topiramate, valproate) already approved for migraine prophylaxis.

Beyond this shared Nav-channel mechanism, lacosamide has a more specific proposed pathway for migraine: it interacts with **collapsin response mediator protein 2 (CRMP2)**, inhibiting its phosphorylation and thereby reducing **CGRP (calcitonin gene-related peptide) release** in the trigeminal system — the central pathophysiological driver of migraine attacks (PMID 27917413). This is corroborated by an animal model showing lacosamide suppresses **cortical spreading depolarization** (PMID 40670944), and by clinical biomarker data showing reduced serum CGRP after lacosamide treatment in episodic migraine patients (PMID 38502425).

The epilepsy-to-migraine link is also clinically precedented: several AEDs (topiramate, valproate) are established first-line migraine preventives, and epilepsy/migraine share overlapping channelopathy biology (e.g., SCN1A-related phenotypes span both conditions, PMID 35696452). This convergence of a plausible shared mechanism, a specific CGRP-related pathway, and completed head-to-head clinical trials makes the migraine prediction considerably more defensible than the model's raw ranking alone would suggest.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | Completed | 600 | Lacosamide vs propranolol for episodic migraine prevention; direct head-to-head comparison with published positive results (see PMID 41863672) |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | Completed | 218 | Multicenter, randomized, double-blind, placebo-controlled trial of 100mg/day and 300mg/day lacosamide for migraine prophylaxis |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 | Completed | 200 | Randomized pilot study: lacosamide 50mg BID add-on vs ibuprofen alone; assessed serum CGRP changes in episodic migraine |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | Recruiting (Unknown) | 600 | Lacosamide vs topiramate; monthly migraine days reduction and ≥50% responder rate; completion/results status unconfirmed |
| [NCT06347497](https://clinicaltrials.gov/study/NCT06347497) | Phase 3 | Recruiting | 600 | Zonisamide vs topiramate — same-class (AED) comparator trial, does not test lacosamide directly |
| [NCT06361446](https://clinicaltrials.gov/study/NCT06361446) | Phase 3 | Recruiting | 600 | Zonisamide vs propranolol — same-class comparator trial, does not test lacosamide directly |
| [NCT06485726](https://clinicaltrials.gov/study/NCT06485726) | Phase 4 | Recruiting | 600 | Valproate vs propranolol — same-class comparator trial, does not test lacosamide directly |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | RCT | Molecular Neurobiology | Published results of the lacosamide vs propranolol Phase 3 RCT; lacosamide effective as alternative preventive for patients intolerant of propranolol/standard AEDs |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | RCT (biomarker) | Acta Neurologica Belgica | Lacosamide add-on reduced serum CGRP levels in episodic migraine patients, supporting a CGRP-mediated mechanism |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Systematic Review/Meta-analysis | Epilepsia | Pooled safety/tolerability profile of lacosamide across RCTs; relevant to migraine-population risk-benefit assessment |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Animal/Mechanistic | The Journal of Headache and Pain | Lacosamide suppresses cortical spreading depolarization in mice, a core migraine pathophysiology model |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Preclinical | Pain Reports | (S)-Lacosamide inhibits CGRP release via CRMP2 in preclinical cephalic pain models |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Network meta-analysis of AED monotherapy efficacy in epilepsy; background context for AED class effect |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Review | Expert Opinion on Emerging Drugs | Overview of emerging treatments for chronic/refractory migraine |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on third-generation anticonvulsants in trigeminal neuralgia/headache pharmacotherapy (tangential context) |
| [25196459](https://pubmed.ncbi.nlm.nih.gov/25196459/) | 2014 | Review | Expert Opinion on Drug Metabolism & Toxicology | PK/PD interactions between antiepileptics and antidepressants; relevant to comorbid migraine-psychiatric prescribing |
| [21565431](https://pubmed.ncbi.nlm.nih.gov/21565431/) | 2011 | Review | Neurología | General overview of lacosamide as a new AED with broad therapeutic perspectives |

---

## Germany Market Information

Lacosamide is currently **not marketed** under this evidence pack's regulatory data — 0 marketing authorizations are on record, and no licensed products/dosage forms are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in this evidence pack; DG001 flags TFDA/BfArM label data as a blocking gap for full safety assessment.)

---

## Other Screened Indications (Same Drug, Not Prioritized)

For context, the same evidence pack screened 9 additional TxGNN-predicted indications for lacosamide. All were assessed as **Hold** or exploratory-only due to weak/absent direct evidence, mismatched trial data, or mechanistically opposing signals:

| Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Manic bipolar affective disorder | 99.96% | pending | pending | 1 recruiting Phase 3 trial; literature mostly unclassified |
| Myofascial pain syndrome | 99.81% | L2 | Research Question | 1 completed Phase 2 fibromyalgia trial (n=159) |
| Insomnia | 99.83% | L3 | Research Question | Sleep-effect data from an epilepsy trial, not primary-insomnia designed |
| Migraine with brainstem aura | 99.82% | L4 | Hold | Channelopathy mechanism only, no direct treatment data |
| Tourette syndrome | 99.95% | L5 | Hold | Literature suggests AEDs may *induce* tics — opposing direction |
| Nephrogenic SIAD | 99.91% | L5 | Hold | AEDs associated with SIADH risk — safety signal, not efficacy |
| Trichotillomania | 99.92% | L5 | Hold | No supporting evidence |
| Obsessive-compulsive disorder | 99.78% | L5 | Hold | Only trial found is about alcohol craving, data mismatch |
| Papillary conjunctivitis | 99.72% | L5 | Hold | No pharmacological rationale |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine disorder is supported by a completed, published Phase 3 head-to-head RCT (lacosamide vs. propranolol) plus converging mechanistic evidence (CGRP suppression, cortical spreading depolarization inhibition), meeting an L1 evidence threshold. However, the drug is not currently marketed in Germany, and core safety/label data are missing, warranting cautious, guardrailed progression rather than unrestricted advancement.

**To proceed, the following is needed:**
- TFDA/BfArM official label data — warnings, contraindications, and drug interactions (DG001, blocking)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Outcome/results retrieval for NCT06243692 (status currently "Unknown" — lacosamide vs. topiramate)
- A germany-specific regulatory pathway assessment, given the drug currently has zero local marketing authorizations
- A safety monitoring plan reflecting known AED-class risks (e.g., mood/behavioral effects, cardiac conduction), pending full label confirmation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

