---
layout: default
title: Parathyroid Hormone
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Parathyroid Hormone
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

# Parathyroid Hormone: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

> The original indication and mechanism of action of Parathyroid Hormone (DrugBank DB05829) are not available in the current evidence pack.
> The TxGNN model predicts potential efficacy for **Migraine Disorder**, with a prediction score of **99.98%**,
> but the supporting evidence — **1 clinical trial** (unrelated to PTH) and **6 publications** (mostly indirect/associative) — is weak and largely tangential.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no approved indication text or original_indications data available) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% (rank 523) |
| Evidence Level | L4 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Parathyroid Hormone is not available (data gap DG002, severity: High). Based on the evidence provided, the repurposing signal for migraine rests on a single 2025 genetic association study proposing PTHrP (parathyroid hormone-related peptide) receptors as a potential genetic driver of migraine susceptibility, plus a 1986 mechanistic animal study on central effects of calcitonin and parathormone.

It is important to note the distinction between **PTHrP** (a related but distinct peptide, often studied in genetic/oncologic contexts) and **PTH itself** (the drug substance under evaluation) — the cited literature largely concerns PTHrP receptor genetics rather than a demonstrated pharmacological effect of exogenous PTH on migraine pathophysiology. The single clinical trial linked to this indication (foot reflexology massage for migraine) has no pharmacological relationship to PTH and was flagged by the underlying evidence pipeline as an unrelated database-matching artifact (relevance grade C).

Overall, the mechanistic rationale is indirect and speculative: a genetic association between a related peptide's receptor and migraine susceptibility does not constitute evidence that administering PTH would be therapeutically effective for migraine. This is reflected in the L4 evidence level (preclinical/mechanistic only) and the "Hold" recommendation already assigned in the scoring.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07028684](https://clinicaltrials.gov/study/NCT07028684) | N/A | Completed | 22 | Studied foot reflexology massage for pain/sleep/quality of life in women with migraine — **not related to PTH pharmacology**; included only as a database co-mention, not mechanistic support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40297711](https://pubmed.ncbi.nlm.nih.gov/40297711/) | 2025 | Genetic/Review | Brain Communications | Proposes PTHrP receptors as a candidate genetic driver of migraine susceptibility in a Portuguese cohort. |
| [29429076](https://pubmed.ncbi.nlm.nih.gov/29429076/) | 2018 | Review | Neuromolecular Medicine | Reviews cardiovascular autonomic dysfunction linking MS, osteoporosis and neurodegeneration; PTH mentioned only as part of bone-remodeling context, not migraine-specific. |
| [31261815](https://pubmed.ncbi.nlm.nih.gov/31261815/) | 2019 | Cohort | Medicina (Kaunas) | Evaluates vitamin D levels and treatment response in pediatric migraine; no direct PTH intervention. |
| [24714817](https://pubmed.ncbi.nlm.nih.gov/24714817/) | 2014 | Cohort | Braz J Med Biol Res | Vitamin D add-on to amitriptyline in pediatric migraine attacks; PTH not administered as treatment. |
| [11425281](https://pubmed.ncbi.nlm.nih.gov/11425281/) | 2001 | Review | Medical Hypotheses | Broad review of magnesium deficiency pathology; PTH mentioned only within mineral-metabolism context. |
| [3739765](https://pubmed.ncbi.nlm.nih.gov/3739765/) | 1986 | Mechanistic (animal) | Acta Neurologica | Early animal study on central effects of calcitonin and parathormone; no abstract available, dated mechanistic data only. |

---

## Germany Market Information

Currently not marketed in Germany — no BfArM authorization records are available for this drug (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/BfArM label warnings and contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack — safety review (S1 stage) cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (migraine disorder) is supported only by L4-level evidence — a single genetic association study on a related peptide (PTHrP, not PTH) and one decades-old mechanistic animal study — with no clinical trial actually testing PTH for migraine. The mechanistic link is speculative and does not meet the threshold for advancing beyond S0.

**To proceed, the following is needed:**
- Original indication and confirmed mechanism of action data (DG002, High severity)
- TFDA/BfArM label warnings and contraindications, required to unblock safety review S1 (DG001, Blocking severity)
- A study or trial directly testing exogenous PTH administration in migraine patients, rather than PTHrP genetic-association or unrelated non-pharmacological trials
- Clarification of the PTH vs. PTHrP mechanistic distinction before any further evidence synthesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

