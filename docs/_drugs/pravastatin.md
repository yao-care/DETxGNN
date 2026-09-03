---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pravastatin: From Hypercholesterolemia to HIV-Related Dyslipidemia and Cardiovascular Risk Management

## One-Sentence Summary

> Pravastatin is an HMG-CoA reductase inhibitor (statin); the evidence base consistently describes it as a treatment for hypercholesterolemia/dyslipidemia, though formal original-indication and MOA records are flagged as data gaps in this pack.
> Of **9 TxGNN-predicted indications** screened for this candidate, **HIV-related dyslipidemia / cardiovascular risk management** emerged as the most clinically credible, supported by **16 clinical trials** (including dedicated Phase 2–4 RCTs of pravastatin in HIV-infected patients) and **20 publications**.
> This is risk-factor management in HIV patients on antiretroviral therapy, not an antiviral effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (`taiwan_regulatory.licenses` is empty). Trial/literature descriptions in this evidence base consistently identify pravastatin as an HMG-CoA reductase inhibitor for hypercholesterolemia/dyslipidemia. |
| Predicted New Indication | HIV infectious disease (ART-related dyslipidemia / cardiovascular risk management) |
| TxGNN Prediction Score | 99.74% (rank 3562) |
| Evidence Level | L2 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

### All Predicted Indications Screened (for transparency)

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Note |
|---|---|---|---|---|---|
| 1 | Homozygous familial hypercholesterolemia | 99.95% | L4 | Hold | Statin efficacy limited by non-functional LDLR in HoFH |
| 2 | **HIV infectious disease** | 99.74% | **L2** | **Proceed with Guardrails** | Selected as primary candidate (see below) |
| 3 | Neurodevelopmental disorder (ataxic gait/absent speech) | 99.62% | L5 | Hold | No trials, no literature, no mechanistic rationale |
| 4 | Feline acquired immunodeficiency syndrome | 99.55% | L5 | Hold | Veterinary disease; graph spill-over via HIV homology |
| 5 | Simian immunodeficiency virus infection | 99.55% | L5 | Hold | Primate model virus; no human evidence |
| 6 | Familial hypercholesterolemia | 99.34% | L1 | Proceed with Guardrails | Already an established statin indication, not a novel repurposing candidate |
| 7 | Hypoalphalipoproteinemia | 99.21% | L4 | Hold | No dedicated trials; statin effect on HDL is modest/off-target |
| 8 | Hypercholesterolemia due to CYP7A1 deficiency | 99.07% | L5 | Hold | Ultra-rare disease; mechanistic speculation only |
| 9 | Cholesterol-ester transfer protein deficiency | 99.04% | L5 | Hold | No mechanistic or clinical link to statin pathway |

---

## Why is This Prediction Reasonable?

The `original_moa` field itself is marked as a data gap, but the underlying evidence base repeatedly and consistently identifies pravastatin as a competitive HMG-CoA reductase inhibitor that lowers hepatic cholesterol synthesis and upregulates LDL receptor expression (e.g., PMID 1658544, NCT00227500). This mechanism is the pharmacological basis for its use in hypercholesterolemia/dyslipidemia.

HIV infection and its antiretroviral therapy (ART), particularly protease-inhibitor-based regimens, are well documented in this evidence base to cause dyslipidemia, chronic immune activation, and accelerated atherosclerosis, substantially raising cardiovascular risk in people living with HIV. Statins are therefore a rational adjunct in this population — not as antiviral agents, but as lipid-lowering and potentially anti-inflammatory/immunomodulatory therapy addressing a major ART-related comorbidity.

Pravastatin specifically stands out among statins for this population because it is not extensively metabolized via CYP3A4, unlike atorvastatin or simvastatin, reducing the risk of clinically significant drug-drug interactions with protease inhibitors and other ART agents that are strong CYP3A4 inhibitors. This DDI advantage is explicitly the rationale behind multiple dedicated trials in this evidence pack (e.g., NCT00000941, NCT00630734, NCT00117494) that established pravastatin as a preferred statin choice for HIV-infected, PI-treated patients with dyslipidemia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Phase 3 | Completed | 630 | Fenofibrate vs. pravastatin in HIV-infected subjects with lipid abnormalities |
| [NCT00117494](https://clinicaltrials.gov/study/NCT00117494) | Phase 4 | Completed | 86 | Rosuvastatin vs. pravastatin in ART-treated dyslipidemic HIV patients (ANRS 126) |
| [NCT00221754](https://clinicaltrials.gov/study/NCT00221754) | Phase 2 | Completed | 21 | RCT of pravastatin in hypercholesterolemic HIV patients on protease inhibitors |
| [NCT00147797](https://clinicaltrials.gov/study/NCT00147797) | N/A | Completed | 84 | Pravastatin effect on carotid artery structure/function in HIV patients on ART |
| [NCT00227500](https://clinicaltrials.gov/study/NCT00227500) | Phase 4 | Completed | 40 | Randomized, double-blind, placebo-controlled pravastatin trial in HIV hyperlipidaemia |
| [NCT00000941](https://clinicaltrials.gov/study/NCT00000941) | Phase 1 | Completed | 56 | PK interactions between protease inhibitors and statins (pravastatin, simvastatin, atorvastatin) |
| [NCT02841774](https://clinicaltrials.gov/study/NCT02841774) | Phase 2 | Completed | 10 | HILLCLIMBER: moderate-dose pravastatin vs. high-dose rosuvastatin in HIV patients with CHD |
| [NCT00630734](https://clinicaltrials.gov/study/NCT00630734) | Phase 4 | Completed | 32 | SLCO1B1 genetic predictors of darunavir/ritonavir–pravastatin DDI |
| [NCT00982189](https://clinicaltrials.gov/study/NCT00982189) | N/A | Completed | 37 | Cardiovascular risk-reduction polypill pilot in HIV-infected persons |
| [NCT00843661](https://clinicaltrials.gov/study/NCT00843661) | Phase 4 | Unknown | 60 | Ezetimibe+fenofibrate vs. pravastatin monotherapy in HIV patients on protease inhibitors |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | RCT (Phase 4) | The Lancet HIV | INTREPID trial: pitavastatin vs. pravastatin in HIV-1 patients with dyslipidaemia, avoiding CYP450-dependent metabolism |
| [25574964](https://pubmed.ncbi.nlm.nih.gov/25574964/) | 2014 | RCT | AIDS | Atorvastatin reduced T-cell activation; pravastatin had no significant immune-activation effect |
| [26148680](https://pubmed.ncbi.nlm.nih.gov/26148680/) | 2015 | RCT, cross-over | BMC Research Notes | Pravastatin, phytosterols, and combination therapy compared for lipid-lowering in HIV |
| [28252528](https://pubmed.ncbi.nlm.nih.gov/28252528/) | 2017 | Cohort/RCT | AIDS | Pitavastatin and pravastatin compared on immune activation and arterial inflammation markers in HIV |
| [16603852](https://pubmed.ncbi.nlm.nih.gov/16603852/) | 2006 | RCT (placebo-controlled) | AIDS | Pravastatin effect on body composition and cardiovascular markers in HIV-infected men |
| [17117030](https://pubmed.ncbi.nlm.nih.gov/17117030/) | 2006 | Cohort | AIDS | Pravastatin had no significant influence on carotid intima-media thickness or aortic stiffness in HIV patients |
| [16218799](https://pubmed.ncbi.nlm.nih.gov/16218799/) | 2005 | RCT | AIDS Research and Human Retroviruses | ACTG 5087: fenofibrate vs. pravastatin for combined dyslipidemia in HIV |
| [18991624](https://pubmed.ncbi.nlm.nih.gov/18991624/) | 2008 | Review | Current HIV Research | Comparative review of rosuvastatin, pravastatin, and atorvastatin for PI-associated hypercholesterolaemia |
| [28364370](https://pubmed.ncbi.nlm.nih.gov/28364370/) | 2017 | Review/Guideline | American Journal of Cardiovascular Drugs | Recommendations for managing statin–HIV medication drug-drug interactions |
| [25907504](https://pubmed.ncbi.nlm.nih.gov/25907504/) | 2015 | Systematic Review | The American Journal of Cardiology | Systematic review of statin therapy usefulness in HIV-infected patients |

---

## Germany Market Information

No marketing authorizations are currently on file for this candidate (`total_licenses: 0`, market status: Not Marketed). No product/dosage-form/indication details are available to summarize.

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, DDI database) are all empty or data gaps in this pack, and no TFDA/BfArM label has been retrieved yet (see DG001, Blocking).

**Drug interactions noted in trial evidence (not from a formal DDI database):**
- Pravastatin is repeatedly used as a low-CYP3A4-dependency statin in probe-substrate DDI studies (NCT04425902, NCT02578277), and its PK is affected by OATP1B1/SLCO1B1 transporter variants when co-administered with darunavir/ritonavir (NCT00630734) and raltegravir (NCT00665717) — relevant specifically to the HIV indication under review.

> For all other safety information, please refer to the package insert once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple dedicated Phase 2–4 RCTs (including a 630-patient Phase 3 trial) establish pravastatin's efficacy and DDI-favorable profile for managing ART-related dyslipidemia and cardiovascular risk in HIV-infected patients — a genuine, evidence-supported repurposing signal distinct from pravastatin's already-established statin indications (e.g., familial hypercholesterolemia, rank 6, which is not novel). The remaining 7 of 9 TxGNN predictions (L4–L5) lack sufficient clinical or mechanistic support and are held.

**To proceed, the following is needed:**
- Official product label / warnings and contraindications (DG001, Blocking — TFDA/BfArM PDF retrieval)
- Confirmed mechanism-of-action documentation (DG002 — DrugBank query)
- Formal DDI database query specific to ART regimens (protease inhibitors, integrase inhibitors)
- Clarification of target population and endpoint (ART-associated dyslipidemia/CV risk reduction, not antiviral effect)
- Assessment of German/EU marketing-authorization pathway, given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

