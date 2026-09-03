---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 4
---

# Ezetimibe
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

> Ezetimibe is a cholesterol-absorption inhibitor whose established clinical use is lowering LDL-cholesterol in hypercholesterolemia and mixed dyslipidemia, typically as an add-on to statin therapy.
> The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**,
> with **50 clinical trials** and **19 publications** currently supporting this direction.
> ⚠️ Note: this evidence pack itself flags a data-quality issue — see "Why is This Prediction Reasonable?" below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (licenses list is empty) — clinically known as hypercholesterolemia/dyslipidemia; treated as a **blocking data gap (DG001)**, not a true "no original indication" |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed *(per this dataset — see data-quality note below)* |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ezetimibe inhibits the intestinal Niemann-Pick C1-Like 1 (NPC1L1) transporter, reducing dietary and biliary cholesterol absorption in the small intestine. This lowers the delivery of cholesterol to the liver, upregulates hepatic LDL receptor expression, and produces a clinically meaningful reduction in LDL-cholesterol, typically used in combination with statins for an additive lowering effect.

Hyperlipoproteinemia is a broad umbrella term encompassing elevated LDL-C/mixed lipid disorders — mechanistically and clinically this overlaps directly with ezetimibe's already-established use in hypercholesterolemia and mixed hyperlipidemia (as reflected in dozens of completed Phase 3 trials, including combinations with fenofibrate, statins, bempedoic acid, and obicetrapib).

**Data-quality caveat:** The evidence pack's own `repurposing_rationale` explicitly flags an internal inconsistency: this dataset records `market_status = "未上市" (not marketed)` and an empty `original_indications` list, which contradicts the well-known fact that ezetimibe (Zetia®/Ezetrol®) is a globally approved lipid-lowering agent. The evidence pack itself concludes this is **not a genuine drug-repurposing candidate**, but rather a case of missing/incomplete regulatory source data (BfArM label not yet ingested — DG001, Blocking) combined with a missing MOA field (DG002, High). The clinical trial and literature evidence below is real and substantial, but it largely supports an **already-recognized indication** rather than a novel repositioning hypothesis. This must be resolved before any downstream decision is finalized.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg + atorvastatin/simvastatin in homozygous familial hypercholesterolemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Phase 1 | Completed | 18 | PK interaction study: Vytorin (ezetimibe/simvastatin) + Niaspan (niacin ER) |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Phase 3 | Completed | 450 | "Inclisiran first" strategy vs usual care in ASCVD with elevated LDL-C on maximal statin ± ezetimibe |
| [NCT05255094](https://clinicaltrials.gov/study/NCT05255094) | Phase 3 | Completed | 464 | AK102 (PCSK9 inhibitor) in primary hypercholesterolemia/mixed hyperlipidemia; ezetimibe-relevant population overlap |
| [NCT00552097 (ENHANCE)](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | Ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT03337308](https://clinicaltrials.gov/study/NCT03337308) | Phase 3 | Completed | 382 | Bempedoic acid 180mg + ezetimibe 10mg FDC vs components/placebo on top of maximal statin therapy |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib 10mg + ezetimibe 10mg FDC in HeFH and/or ASCVD/high-risk patients |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Completed | 135 | Long-term safety/tolerability of ezetimibe + rosuvastatin FDC in Japanese hypercholesterolemia patients |
| [NCT01043380 (PRECISE-IVUS)](https://clinicaltrials.gov/study/NCT01043380) | Phase 4 | Completed | 245 | IVUS-measured coronary plaque regression: cholesterol absorption inhibitor (ezetimibe) vs synthesis inhibitor |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM trial: obicetrapib + ezetimibe FDC significantly reduces LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in HeFH patients not achieving LDL-C goals on existing therapy incl. ezetimibe |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Editorial/Commentary | N Engl J Med | Editorial on cholesterol lowering and ezetimibe (ENHANCE trial controversy) |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug and Therapeutics Bulletin | Ezetimibe update: efficacy/safety review, no proven CV mortality/morbidity benefit at time of writing |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Familial hypercholesterolemia treatment overview including statins, ezetimibe, and other LDL-lowering agents |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | FH epidemiology, underdiagnosis, and treatment landscape |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Postprandial hyperlipidemia pathophysiology, diagnosis, and treatment |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Emerging LDL-C/ApoB-lowering therapies incl. ezetimibe-based combinations |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors, statin-intolerant/FH populations |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circulation Research | Overview of cholesterol-lowering agent classes including ezetimibe |

---

## Germany Market Information

No BfArM authorization records are present in this evidence pack (`total_licenses = 0`, `licenses = []`). This is inconsistent with ezetimibe's known long-standing market presence in Germany/EU (e.g., Ezetrol®, Inegy®/Vytorin® combination products) and has been logged as **data gap DG001 (Blocking)** — the regulatory label/authorization data has not yet been ingested from the BfArM source. This gap must be closed before any safety or authorization claims can be made about this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. *(All safety fields in this dataset — key warnings, contraindications, and drug interactions — are currently unavailable; DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical trial and literature base for ezetimibe in LDL-C/hyperlipoproteinemia-type indications is extensive and high-quality (L1 evidence, multiple completed Phase 3 RCTs including the pivotal ENHANCE trial and modern FDC studies). However, this dataset's own regulatory and MOA fields are incomplete and internally inconsistent with ezetimibe's known real-world approval status, so this should be treated as evidence consolidation for a plausible/likely-already-approved use rather than a validated novel repurposing signal until the data gaps are resolved.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the actual BfArM/TFDA label PDF to confirm true market status, licenses, and approved indication text
- Resolve DG002 (High): query DrugBank API for confirmed MOA to replace the current placeholder
- Reconcile the `market_status = "未上市"` / empty `original_indications` fields against ezetimibe's known approved indications, to determine whether "Hyperlipoproteinemia" is a genuinely new label extension or an existing on-label use
- Obtain safety/contraindication data (key warnings, DDI) once the label source is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

