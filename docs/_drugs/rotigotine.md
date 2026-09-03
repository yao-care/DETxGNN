---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Rotigotine
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

# Rotigotine: From Parkinson's Disease/Restless Legs Syndrome to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

> Rotigotine is a dopamine D1/D2/D3 receptor agonist established for **Parkinson's Disease** and **Restless Legs Syndrome (RLS)**.
> The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**,
> but currently **no clinical trials** and only **3 indirect publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease / Restless Legs Syndrome (per PMID 37221270; not derivable from Taiwan/Germany license data, which is empty) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently a **[High-severity data gap]** and was not available for this evaluation (DG002). Based on the evidence pack's literature, Rotigotine is known as a non-ergot **D1/D2/D3 dopamine receptor full agonist**, used clinically for Parkinson's Disease and RLS (PMID 37221270).

The mechanistic link to ADHD is indirect. ADHD pathophysiology does involve dopaminergic dysregulation, but the standard-of-care drugs (methylphenidate, amphetamine) act by **increasing synaptic dopamine/norepinephrine concentrations**, not by direct receptor agonism. The literature retrieved for this candidate does not address ADHD directly — one paper covers RLS (a condition with known ADHD comorbidity), and another is basic receptor pharmacology on D4 receptor heterodimerization implicated in ADHD genetics, not a Rotigotine efficacy study.

Notably, a second predicted indication in this evidence pack — **schizophrenia** (rank 2, TxGNN score 99.996%) — has comparatively stronger support: a systematic review/meta-analysis (PMID 31688399) on prodopaminergic drugs for negative symptoms of schizophrenia, plus a structural biology paper (PMID 37221270) directly showing Rotigotine bound to all five dopamine receptor subtypes. This suggests the schizophrenia hypothesis may merit prioritized follow-up over ADHD, though neither has a Rotigotine-specific clinical trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current Pharmaceutical Design | Reviews pharmacological options for RLS in children; RLS and ADHD frequently co-occur, but does not evaluate Rotigotine for ADHD directly |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclinical/Receptor pharmacology | Pharmacological Research | Shows α2A adrenoceptor–D4 receptor heteromerization affects impulsive-control disorder pharmacology, relevant to ADHD biology but not to Rotigotine specifically |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | General review of RLS pathophysiology and treatment; no ADHD-specific data |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are currently flagged as Blocking/High-severity data gaps — TFDA label not yet retrieved, DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD indication is supported only by mechanistic/preclinical inference (L4) with zero clinical trials and no ADHD-specific efficacy literature — the retrieved papers address RLS comorbidity and receptor biology, not Rotigotine's clinical effect in ADHD. Combined with a Blocking data gap on TFDA safety labeling, this candidate is not ready to advance past S0.

**To proceed, the following is needed:**
- DrugBank MOA confirmation (DG002) to formally establish receptor-binding profile relevant to ADHD
- TFDA/German product label retrieval for safety and contraindication review (DG001, currently Blocking)
- Rotigotine-specific preclinical or clinical data in ADHD populations (current literature is indirect/comorbidity-based only)
- Consider parallel evaluation of the schizophrenia candidate (rank 2, L3, "Research Question" stage), which has stronger systematic-review-level evidence and may be a more efficient path forward
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

