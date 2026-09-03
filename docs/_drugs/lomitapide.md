---
layout: default
title: Lomitapide
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapide: From Homozygous Familial Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

> Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor internationally used for homozygous familial hypercholesterolemia (HoFH), a severe genetic form of hyperlipoproteinemia.
> The TxGNN model predicts it may be effective for **Hyperlipoproteinemia** more broadly,
> with **10 clinical trials** and **17 publications** currently supporting this direction — largely because this candidate reflects the drug's already-established international use rather than a genuinely novel signal.
>
> *Note: TxGNN also flagged 8 higher-ranked candidates (rare platelet/thrombocytopenia disorders, e.g. Glanzmann thrombasthenia, pseudo-von Willebrand disease) with very high model scores but **zero supporting trials or literature**. These remain unvalidated model output (L5) and are not covered further in this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in local regulatory data (drug not marketed in this jurisdiction); internationally established for Homozygous Familial Hypercholesterolemia (HoFH) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not provided as a structured field (flagged as a data gap), but it can be reconstructed directly from the trial evidence in this pack: lomitapide (originally coded AEGR-733 / BMS-201038) is a **microsomal triglyceride transfer protein (MTP) inhibitor**. By blocking MTP in hepatocytes and enterocytes, it prevents assembly and secretion of apolipoprotein-B-containing lipoproteins (VLDL, chylomicrons), lowering LDL-cholesterol through an LDL-receptor-independent pathway.

The predicted new indication, "hyperlipoproteinemia," is not mechanistically distant from the drug's known use — it is the broader disease category that includes HoFH, the rare, severe subtype for which lomitapide already has an extensive clinical development program (visible in the 13 trials returned, all enrolling HoFH or hypercholesterolemia patients). In this sense, TxGNN has essentially **recovered a known indication** rather than surfaced a genuinely novel one. This is still clinically useful: it confirms the model correctly captures the MTP-inhibition → lipoprotein-lowering axis, and it highlights a jurisdiction (this market) where the drug is not currently registered despite strong global evidence — a market-access gap worth investigating rather than a scientific unknown.

Because HoFH is ultra-rare (worldwide prevalence ~1:160,000–1,000,000), the pivotal registration trials (e.g., NCT00730236) were conducted as single-arm, open-label studies rather than placebo-controlled RCTs — a recognized and regulator-accepted design for this population. Smaller placebo-controlled Phase 2 studies exist for adjacent hypercholesterolemia populations, providing additional randomized-controlled support.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Completed | 29 | Pivotal single-arm trial of lomitapide (AEGR-733) on LDL-C and lipid endpoints in HoFH patients on stable lipid-lowering therapy |
| [NCT00943306](https://clinicaltrials.gov/study/NCT00943306) | Phase 3 | Completed | 19 | Long-term open-label follow-on study confirming continued safety/efficacy of lomitapide in HoFH |
| [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) | Phase 3 | Completed | 46 | Single-arm study of efficacy/long-term safety of lomitapide in pediatric HoFH on stable lipid-lowering therapy |
| [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) | Phase 3 | Completed | 9 | Efficacy/safety of lomitapide in Japanese HoFH patients on concurrent lipid-lowering therapy |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Dose-escalation study establishing safety, tolerability, and LDL-C/TC/TG-lowering pharmacodynamics of lomitapide |
| [NCT00559962](https://clinicaltrials.gov/study/NCT00559962) | Phase 2 | Completed | 260 | Randomized, double-blind, placebo-controlled trial of low-dose lomitapide ± statin/ezetimibe/fenofibrate on hepatic fat accumulation |
| [NCT00690443](https://clinicaltrials.gov/study/NCT00690443) | Phase 2 | Completed | 44 | Randomized, double-blind, comparator-controlled trial of lomitapide + atorvastatin vs atorvastatin monotherapy in moderate hypercholesterolemia |
| [NCT02135705](https://clinicaltrials.gov/study/NCT02135705) | N/A | Recruiting | 300 | LOWER global product-exposure registry evaluating long-term real-world safety/effectiveness of lomitapide |
| [NCT06832371](https://clinicaltrials.gov/study/NCT06832371) | N/A | Active, not recruiting | 73 | Observational study of lomitapide's effect on major adverse cardiovascular events (MACE) in HoFH |
| [NCT02765841](https://clinicaltrials.gov/study/NCT02765841) | Phase 3 | Withdrawn | 0 | Planned pediatric HoFH efficacy/safety study (12-wk run-in, 24-wk efficacy, 80-wk safety phase); not conducted |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39426393](https://pubmed.ncbi.nlm.nih.gov/39426393/) | 2024 | Phase 3 Study (open-label) | Lancet Diabetes Endocrinol | APH-19: efficacy-phase results of lomitapide in pediatric HoFH patients on standard-of-care lipid-lowering therapy |
| [37130090](https://pubmed.ncbi.nlm.nih.gov/37130090/) | 2023 | Consensus Statement | European Heart Journal | 2023 EAS update on HoFH diagnosis and treatment, including lomitapide's role among new therapies |
| [36152419](https://pubmed.ncbi.nlm.nih.gov/36152419/) | 2022 | Study | Atherosclerosis | Efficacy and safety of lomitapide extended to familial chylomicronaemia syndrome (adjacent lipid disorder) |
| [35148370](https://pubmed.ncbi.nlm.nih.gov/35148370/) | 2022 | Review | Eur J Prev Cardiol | Review of efficacy and safety of lomitapide in HoFH |
| [31741187](https://pubmed.ncbi.nlm.nih.gov/31741187/) | 2019 | Review | Curr Atheroscler Rep | Mechanistic review of MTP inhibition (lomitapide) and apoB100-synthesis inhibition (mipomersen) |
| [28598687](https://pubmed.ncbi.nlm.nih.gov/28598687/) | 2017 | Review | Expert Opin Pharmacother | Review of lomitapide for treatment of hypercholesterolemia, including HoFH management context |
| [25936301](https://pubmed.ncbi.nlm.nih.gov/25936301/) | 2015 | Review | Atherosclerosis Suppl | Mipomersen and lomitapide as new drugs for HoFH treatment |
| [25702706](https://pubmed.ncbi.nlm.nih.gov/25702706/) | 2015 | Review | Br J Clin Pharmacol | Pharmacological profile review of lomitapide |
| [25053660](https://pubmed.ncbi.nlm.nih.gov/25053660/) | 2014 | Consensus Statement | European Heart Journal | EAS position paper on HoFH detection and clinical management |
| [21846156](https://pubmed.ncbi.nlm.nih.gov/21846156/) | 2011 | Review | Am J Cardiovasc Drugs | Early development review of lomitapide as MTP inhibitor for familial/primary hypercholesterolemia |

---

## Germany Market Information

Lomitapide currently holds **no marketing authorizations** in this jurisdiction (0 licenses recorded; market status: not marketed). No product listings, dosage forms, or authorization numbers are available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured key warnings, contraindications, and drug-interaction data were not available in this evidence pack (flagged as a **blocking** data gap — [DG001] — preventing entry into the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Lomitapide has a substantial body of clinical trial and literature support for lipid-lowering efficacy (largely reflecting its established international use in HoFH), but it is not currently authorized in this market and a **blocking data gap** exists for essential safety information (label warnings and contraindications), which prevents a safety pre-assessment from being completed.

**To proceed, the following is needed:**
- Obtain the approved product label / SmPC (warnings, contraindications, DDI) via the relevant regulatory authority to close [DG001]
- Confirm formal MOA documentation via DrugBank to close [DG002]
- Assess regulatory pathway/rationale for absence of local marketing authorization despite international approval
- Independently evaluate the 8 unscored platelet/thrombocytopenia-related predictions (ranks 1–8, 10), which currently have no clinical trial or literature support (L5) and require dedicated evidence retrieval before any decision can be made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

