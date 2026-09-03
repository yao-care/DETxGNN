---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine: From Alzheimer's Disease to Migraine Disorder

## One-Sentence Summary

> Memantine is a well-established NMDA receptor antagonist, globally known for treating moderate-to-severe Alzheimer's disease (this approved-indication detail is a data gap in the current evidence pack).
> The TxGNN model — together with independent literature — points to **Migraine Disorder (episodic migraine prophylaxis)** as its most credible new use,
> with **2 clinical trials** (including 1 completed Phase 3 RCT) and **9+ relevant publications** (including a meta-analysis, a systematic review, and a network meta-analysis) supporting this direction.
> Three other TxGNN-predicted indications (pulmonary hypertension, kyphoscoliotic heart disease, migraine with brainstem aura) were also reviewed but carry far weaker or no supporting evidence — see "Other Predicted Indications" below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe Alzheimer's disease (dementia) — widely established for memantine, but not captured in this Evidence Pack's structured fields (flagged as data gap DG001/DG002) |
| Predicted New Indication | Migraine Disorder (episodic migraine, prophylactic treatment) |
| TxGNN Prediction Score | 99.52% (score 0.9952, rank 5690) |
| Evidence Level | L2 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank's structured field (DG002, flagged High severity). Based on the literature contained in this evidence pack, memantine is consistently described as a moderate-affinity, uncompetitive **NMDA (N-methyl-D-aspartate) receptor antagonist** — the same glutamatergic mechanism underlying its established efficacy in Alzheimer's disease, where it reduces excitotoxic glutamate signaling.

Multiple independent reviews in the evidence pack (PMID 36869904, 29508147, 36983158) explain that elevated glutamate levels and NMDA receptor-mediated **cortical spreading depression** are central to migraine pathophysiology. This gives memantine a mechanistically coherent rationale as a migraine preventive — the same NMDA-blocking action that protects neurons in Alzheimer's disease may also dampen the cortical hyperexcitability that triggers migraine attacks.

Importantly, this is not a purely data-driven signal: it is corroborated by a completed Phase 3 head-to-head RCT (memantine vs. sodium valproate), a placebo-controlled RCT, a meta-analysis of RCTs, a systematic review, and a 2025 network meta-analysis of oral migraine preventives — a substantially stronger evidence base than the other three TxGNN-flagged indications in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Head-to-head comparison of memantine vs. sodium valproate for prophylactic treatment of episodic migraine; small active-comparator trial (Grade A relevance, but limited by sample size) |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Phase 4 | Enrolling by Invitation | 3300 | Pragmatic EMR-based practice research across 10 common neurological disorders; not a dedicated memantine efficacy trial, only indirectly relevant (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-Analysis (RCTs) | Clinical Neuropharmacology | Pooled RCT data on memantine vs. placebo for migraine; efficacy signal present but described as still controversial |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic Review | Headache | Assesses efficacy and safety of memantine for prophylactic treatment of episodic migraine |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network Meta-Analysis | Frontiers in Pharmacology | Compares oral preventive medications for migraine in adults 18–65, including memantine's relative efficacy/safety |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (placebo-controlled) | Headache | Randomized double-blind placebo-controlled study of memantine for prophylaxis of migraine without aura |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical Practice Guideline | Annals of Internal Medicine | 2023 VA/DoD guideline reviewing recommendations for migraine and tension-type headache management |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedeberg's Archives of Pharmacology | Presents memantine and ketamine as NMDA-receptor-antagonist anti-migraine agent candidates |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary/Review | Headache | Explicitly cautions "big promise but little evidence" for memantine in migraine — a useful counterweight |
| [19280698](https://pubmed.ncbi.nlm.nih.gov/19280698/) | 2009 | Review | Headache | Early review of memantine in preventive treatment of migraine and refractory migraine |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective Cohort | The Journal of Headache and Pain | Retrospective series of 60 cases characterizing memantine's preventive efficacy in frequent migraine |
| [19031499](https://pubmed.ncbi.nlm.nih.gov/19031499/) | 2008 | Clinical Study | Headache | Assesses efficacy and tolerability of memantine in preventive treatment of refractory migraine |

---

## Germany Market Information

Memantine is currently **not marketed** under this evidence pack's regulatory dataset (0 authorizations, `market_status: 未上市`), so no product license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were returned in this evidence pack (labeling data is flagged as a **Blocking** data gap, DG001 — TFDA label warnings/contraindications need to be sourced and parsed before any S1 safety assessment can proceed).

---

## Other Predicted Indications (Lower Priority, Not Pursued)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Reason |
|---|---|---|---|---|---|
| 1 | Pulmonary hypertension | 99.54% | L5 | Hold | No direct mechanistic or clinical evidence connecting NMDA antagonism to pulmonary vascular remodeling; supporting literature is either off-target (insulin/lipid metabolism) or concerns an unrelated compound (MN-08) |
| 3 | Kyphoscoliotic heart disease | 99.43% | L5 | Hold | No clinical trials, no literature, no plausible mechanistic link — a purely data-driven TxGNN artifact |
| 4 | Migraine with brainstem aura | 99.41% | L3 | Research Question | Shares NMDA/glutamate rationale with migraine generally, but the only relevant RCT (26638119) studied "migraine without aura," not the brainstem-aura subtype — mechanistic extrapolation only |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Among the four TxGNN-predicted indications, migraine disorder has by far the strongest evidence base (1 completed Phase 3 RCT, a placebo-controlled RCT, a meta-analysis, a systematic review, and a 2025 network meta-analysis), earning it "Research Question" status (L2/S2) rather than outright rejection. However, trial sizes remain small, at least one commentary explicitly flags the evidence as weak ("big promise but little evidence"), the drug currently has zero authorizations and is not marketed in this jurisdiction, and a Blocking safety data gap (TFDA/BfArM label warnings unavailable) prevents any S1 safety review. These combined factors mean the candidate cannot yet proceed to Go.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official package insert for warnings/contraindications
- Resolve DG002 (High): confirm memantine's formal MOA entry in DrugBank
- A larger, adequately powered confirmatory Phase 3 RCT specifically for migraine prevention (current completed trial N=33)
- Clarify local regulatory pathway, since memantine is currently unapproved/not marketed in this jurisdiction
- Re-evaluate pulmonary hypertension and kyphoscoliotic heart disease only if new mechanistic or clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

