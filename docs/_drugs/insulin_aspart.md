---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart is a rapid-acting insulin analogue originally developed for glycaemic control in diabetes mellitus. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus** specifically, with **60 clinical trials** and **20 publications** currently supporting this direction — though this is best read as a **confirmatory signal** rather than a novel repurposing, since insulin aspart is already an established mealtime insulin for type 1 diabetes in multiple jurisdictions. A blocking data gap on drug label safety information means this candidate cannot yet clear safety pre-screening.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (rapid-acting mealtime insulin) — precise approved indication text not available in this Evidence Pack |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known clinical information, insulin aspart is a rapid-acting recombinant human insulin analogue engineered for faster onset and shorter duration of action than regular human insulin, making it suitable for mealtime (bolus) glycaemic control.

The predicted indication — type 1 diabetes mellitus — sits within the same core pharmacological use case as insulin aspart's general diabetes indication: exogenous insulin replacement for glucose regulation. In type 1 diabetes specifically, patients are absolutely insulin-deficient due to autoimmune beta-cell destruction, and rapid-acting analogues like aspart are a standard component of basal-bolus and pump-based regimens.

Because this candidate largely reconfirms an already well-established clinical use rather than identifying a mechanistically distant new indication, the "prediction" should be interpreted as validation of TxGNN's ability to recover known drug-disease relationships, rather than a genuine repurposing opportunity. The very large trial and literature base (60 trials, spanning Phase 1–4, including multiple completed Phase 3 RCTs) is consistent with this being a mature, guideline-supported use rather than an exploratory one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | Completed | 50 | Once vs twice-daily detemir with aspart as mealtime insulin in children/adolescents with T1D |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Detemir+aspart vs NPH+aspart: hypoglycaemia frequency in basal-bolus T1D regimen |
| [NCT01109316](https://clinicaltrials.gov/study/NCT01109316) | Phase 3 | Completed | 132 | CSII pump comparison: insulin lispro vs insulin aspart in T1D |
| [NCT00097071](https://clinicaltrials.gov/study/NCT00097071) | Phase 3 | Completed | 299 | Safety/efficacy of aspart vs lispro in insulin pumps, children and adolescents with T1D |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Terminated | 596 | Inhaled mealtime insulin vs subcutaneous aspart (+detemir) in T1D, 104-week RCT |
| [NCT03143816](https://clinicaltrials.gov/study/NCT03143816) | Phase 4 | Completed | 60 | Prandial insulin aspart vs Technosphere inhaled insulin in T1D on multiple daily injections |
| [NCT00593255](https://clinicaltrials.gov/study/NCT00593255) | Phase 4 | Completed | 220 | Aspart vs human soluble insulin as mealtime insulin in Chinese T1D/T2D patients |
| [NCT03565666](https://clinicaltrials.gov/study/NCT03565666) | Phase 2/3 | Completed | 36 | Insulin-only bionic pancreas (aspart-based) closed-loop bridging study |
| [NCT02871089](https://clinicaltrials.gov/study/NCT02871089) | NA | Active, not recruiting | 96 | Closed-loop insulin delivery from T1D onset on residual beta-cell function |
| [NCT05653050](https://clinicaltrials.gov/study/NCT05653050) | NA | Completed | 26 | Closed-loop glucose control vs standard pump+CGM in adolescents with T1D |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Overview of T1D pathophysiology, epidemiology, and complications |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (Phase 3a) | Lancet | ONWARDS 6: once-weekly icodec vs daily degludec, both with aspart bolus, in T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: degludec vs detemir, both + aspart, in pregnant women with T1D |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster aspart vs aspart on fetal growth in T1D/T2D pregnancy |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT (crossover) | Diabetes Obes Metab | Faster aspart vs aspart with non-automated pump + CGM in adults with T1D |
| [37404205](https://pubmed.ncbi.nlm.nih.gov/37404205/) | 2023 | RCT (crossover) | Diabetes Technol Ther | Faster vs standard aspart with hybrid closed-loop in active children/adolescents with T1D |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic Review | Diabetes Metab | Efficacy/safety of aspart vs regular human insulin in T1D and T2D |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Meta-analysis | Diabetes Metab J | FIAsp vs aspart with insulin pump in T1D: pooled efficacy/safety |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Observational | Acta Diabetol | Glulisine vs lispro vs aspart during CSII in T1D: HbA1c, hypo/hyperglycaemia, DKA rates |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Spotlight review on insulin aspart in T1D and T2D management |

---

## Germany Market Information

Insulin aspart currently has **no marketing authorization on record** in this jurisdiction (`market_status: 未上市`, `total_licenses: 0`). No license entries are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a Blocking data gap — DG001, missing TFDA/regulatory label warnings and contraindications — currently prevents completion of the initial safety screen (S1) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is strong and mature (L1, multiple completed Phase 3 RCTs plus 60 trials and a broad literature base), but this largely reflects insulin aspart's already-established role in type 1 diabetes rather than a novel repurposing opportunity. More importantly, a **Blocking** data gap on drug label safety information (warnings/contraindications) means the candidate cannot yet pass initial safety screening (S1), and there is currently no market authorization in this jurisdiction to anchor a regulatory pathway.

**To proceed, the following is needed:**
- Retrieve and parse official package insert (warnings, contraindications) to close DG001 (Blocking)
- Obtain DrugBank/mechanism-of-action detail to close DG002 (High) and support formal mechanistic rationale
- Confirm actual local regulatory/licensing status, given `market_status: 未上市` conflicts with insulin aspart's approval status in most other markets
- Clarify with stakeholders whether this candidate should be tracked as "confirmatory validation" rather than a new repurposing opportunity, given original and predicted indications largely overlap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

