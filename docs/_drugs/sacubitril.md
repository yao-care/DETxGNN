---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 5
---

# Sacubitril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

## One-Sentence Summary

Sacubitril is a neprilysin inhibitor that is only used clinically in fixed combination with valsartan (sacubitril/valsartan, LCZ696/Entresto) for heart failure with reduced ejection fraction (HFrEF). The TxGNN model predicts the combination may also benefit **Diabetic Nephropathy**, supported by **2 clinical trials** (including one dedicated Phase 4 RCT) and **20 publications**, including a secondary analysis of the pivotal PARADIGM-HF trial.

> **Note:** This evidence pack contains 5 TxGNN-predicted indications for sacubitril. Diabetic nephropathy (rank 3) is the only one with any supporting clinical or mechanistic evidence — the other four (brain small vessel disease, HANAC syndrome, rheumatoid arthritis, hemoglobinopathy) have no clinical trials, no relevant literature, and no plausible mechanistic link, and are explicitly scored **L5 / Hold**. This report therefore focuses on diabetic nephropathy as the only actionable candidate; the remaining four are summarized briefly at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure with reduced ejection fraction (HFrEF), as part of the sacubitril/valsartan combination — *inferred from trial/literature context; not present as structured data in this evidence pack* |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (flagged internally as "Research Question") |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa: [Data Gap]`). Based on the trial and literature context in this pack, sacubitril is a prodrug that inhibits neprilysin, raising circulating levels of natriuretic peptides (ANP, BNP), and is co-administered with valsartan (an ARB) to simultaneously block the renin-angiotensin-aldosterone system (RAAS) — the combination is marketed as LCZ696/Entresto for HFrEF.

Heart failure and diabetic nephropathy share substantial pathophysiological overlap: both involve RAAS activation, glomerular/systemic hemodynamic stress, and chronic low-grade inflammation, and the two patient populations frequently overlap clinically (diabetic patients with HFrEF are a common comorbid group). Multiple preclinical studies (rat and mouse models of diabetic kidney disease) show sacubitril/valsartan reduces glomerular hypertension, oxidative stress, and NF-κB/NLRP3-mediated inflammation, and a secondary analysis of the PARADIGM-HF trial (PMID 29661699) found neprilysin inhibition was associated with slower renal function decline in patients with type 2 diabetes already on maximal RAAS blockade — providing translational, human-level support for the mechanistic hypothesis.

Importantly, sacubitril has never been studied or approved as a monotherapy for kidney disease — all supporting evidence relates to the fixed-dose combination with valsartan, not sacubitril alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | Randomized, controlled, multicenter "Hyper-Save" study comparing sacubitril/valsartan vs. valsartan alone in patients with mild-to-moderate essential hypertension and type 2 diabetic nephropathy over 12 weeks; primary purpose-designed for this indication, but no results yet. |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Real-world retrospective EMR study of sacubitril/valsartan prescribing in HFrEF patients in India; not designed for diabetic nephropathy specifically, but the HFrEF population likely includes diabetic nephropathy comorbidity — indirect evidence only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | RCT (secondary analysis) | Lancet Diabetes Endocrinol | Secondary analysis of PARADIGM-HF: neprilysin inhibition slowed renal function decline in type 2 diabetic HF patients already on maximal RAAS blockade. |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical study | Int Immunopharmacol | 112 diabetic nephropathy + hypertension patients; nifedipine + sacubitril/valsartan improved renal function vs. nifedipine + valsartan alone. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical study | Diabetes Metab Syndr Obes | BOLD-MRI study evaluating renal protective effects of sacubitril/valsartan in type 2 diabetics. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on pharmacological pillars slowing diabetic kidney disease progression, including RAAS/neprilysin pathways. |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Revue Médicale Suisse | Discusses potential role of sacubitril/valsartan in type 2 diabetes, including glycemic and renal effects. |
| [30909895](https://pubmed.ncbi.nlm.nih.gov/30909895/) | 2019 | Preclinical (Zucker Obese rat) | Cardiovasc Diabetol | Sacubitril + valsartan combination reduced glomerular and tubular injury more effectively than valsartan alone. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preclinical (rat) | Diabetes Metab Syndr Obes | Sacubitril/valsartan improved early diabetic nephropathy via inhibition of the NLRP3 inflammasome pathway. |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preclinical (rat) | PeerJ | LCZ696 mitigated diabetic nephropathy via reduced oxidative stress, NF-κB inflammation, and glomerulosclerosis. |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Preclinical (db/db & KKAy mice) | Am J Physiol Renal Physiol | Sacubitril/valsartan showed differential renoprotective effects vs. valsartan alone in two diabetic mouse models. |
| [27129187](https://pubmed.ncbi.nlm.nih.gov/27129187/) | 2016 | Preclinical (diabetic rat) | Clin Sci (Lond) | AT1 receptor-neprilysin inhibition produced blood-pressure-independent renoprotection vs. ARB alone. |

---

## Germany / Taiwan Market Information

Sacubitril is **not currently marketed** in this jurisdiction (`market_status: 未上市`), and no drug licenses are on file (0 authorizations). No product/authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug-drug interaction data are currently available for sacubitril in this evidence pack (all fields returned `[Data Gap]` or `not_found`).

---

## Other TxGNN Predictions (Screened, Not Pursued)

The remaining 4 predictions in this evidence pack (all rank 5000+, score ~99–99.6%) have **no clinical trials, no relevant literature, and no plausible mechanistic link** to sacubitril's pharmacology. All are scored **L5 / Hold**:

| Rank | Predicted Indication | Score | Reason for Hold |
|------|----------------------|-------|------------------|
| 1 | Brain small vessel disease 1 with ocular anomalies | 99.58% | COL4A1-related genetic disorder; no known link to neprilysin/natriuretic peptide pathway |
| 2 | HANAC syndrome (familial hematuria-retinal arteriolar tortuosity) | 99.57% | COL4A1 mutation disorder; no supporting trials or literature |
| 4 | Rheumatoid arthritis | 99.35% | No supporting trials or literature despite theoretical anti-inflammatory rationale |
| 5 | Hemoglobinopathy | 99.18% | No supporting trials, literature, or mechanistic rationale |

These are model artifacts of a high-recall prediction system and should not be pursued without independent mechanistic or clinical signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Diabetic nephropathy has the strongest evidentiary support among all TxGNN predictions for sacubitril, including a purpose-built Phase 4 RCT (not yet recruiting) and a positive secondary analysis of PARADIGM-HF. However, no completed trial has yet demonstrated efficacy for this indication in humans, and sacubitril itself is not marketed in this jurisdiction — this remains a research question, not a near-term repurposing opportunity.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formal MOA and original indication documentation from DrugBank — currently a **High** severity data gap (DG002)
- Results from NCT06501651 (Hyper-Save study) once recruitment completes
- Confirmation that any future indication claim applies to the sacubitril/valsartan combination, not sacubitril monotherapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

