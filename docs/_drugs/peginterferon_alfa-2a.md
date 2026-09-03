---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Viral Hepatitis to Confirmed Efficacy in Hepatitis B Virus Infection

## One-Sentence Summary

> Peginterferon Alfa-2a (a pegylated interferon best known by the brand Pegasys) has a long history of antiviral/immunomodulatory use in chronic viral hepatitis, though this dataset does not carry a documented original indication record.
> The TxGNN model's top prediction — **Hepatitis B Virus Infection** — is supported by **50 clinical trials** and **20 publications**, including a landmark NEJM randomized trial.
> Importantly, the underlying rationale notes this is less a "new" indication and more a **confirmation of an already-established use** that is simply missing from the structured regulatory record — a distinction that matters for how this candidate should be prioritized.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current regulatory dataset (trial history strongly indicates established use in chronic viral hepatitis B/C) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacological class information, Peginterferon Alfa-2a is a pegylated recombinant interferon-alfa — a cytokine-class agent with broad antiviral and immunomodulatory activity. Its efficacy in chronic viral hepatitis has been extensively documented through decades of clinical use, and mechanistically this same immune-activating, antiviral pathway is directly applicable to Hepatitis B Virus Infection.

Unlike a typical "new use" candidate, the evidence pack's own repurposing rationale for this prediction states that Peginterferon Alfa-2a is **already an established antiviral/immunomodulatory therapy for chronic hepatitis B** (used to drive HBeAg seroconversion), and that this is "not strictly a new indication in the repurposing sense" — rather, it reflects a gap in this dataset's original-indication documentation rather than a genuine novel signal. This distinction is important: the strength of the evidence below primarily *validates* an existing, well-characterized use rather than uncovering a new one.

That said, the sheer depth of Phase 3/4 randomized and real-world evidence — including landmark trials establishing PEG-IFN alfa-2a's role in both HBeAg-positive and HBeAg-negative chronic hepatitis B — makes this one of the most robustly supported entries in the prediction set, and a useful benchmark for interpreting the model's other (genuinely exploratory) hepatitis-related predictions in this dataset, such as Hepatitis E virus infection (rank 2, L3 evidence, largely case-report/systematic-review based).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00291616](https://clinicaltrials.gov/study/NCT00291616) | Phase 4 | Completed | 52 | RCT combining Thymosin Alpha 1 with PEG-IFN alfa-2a vs PEG-IFN alone in HBeAg-positive CHB; optimal treatment duration assessment |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Phase 2 | Completed | 76 | Add-on PEG-IFN to NA therapy in HBeAg-negative genotype D CHB with stable DNA suppression; evaluated HBsAg decline |
| [NCT01237496](https://clinicaltrials.gov/study/NCT01237496) | Phase 3 | Completed | 17 | Immunology sub-study of HBV-specific T-cell responses in HBeAg-negative CHB patients treated with Pegasys |
| [NCT02604823](https://clinicaltrials.gov/study/NCT02604823) | Phase 4 | Completed | 307 | Efficacy/safety of Pegasys in naïve, interferon- or lamivudine-pretreated HBeAg-positive CHB patients |
| [NCT02570191](https://clinicaltrials.gov/study/NCT02570191) | Phase 4 | Completed | 60 | Efficacy, safety, tolerability of PEGASYS in HBeAg-negative CHB patients |
| [NCT02598063](https://clinicaltrials.gov/study/NCT02598063) | Phase 4 | Completed | 255 | PEG-IFN alfa-2a vs adefovir dipivoxil in lamivudine-resistant HBeAg-positive CHB |
| [NCT01095835](https://clinicaltrials.gov/study/NCT01095835) | Phase 3 | Completed | 131 | 48 vs 96 weeks of PEG-IFN alfa-2a, alone or with lamivudine, in HBeAg-negative CHB |
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | PARC study — PEG-IFN + ribavirin vs PEG-IFN monotherapy in HBeAg-negative CHB |
| [NCT01519921](https://clinicaltrials.gov/study/NCT01519921) | Phase 4 | Completed | 150 | Efficacy/safety of PEGASYS in treatment-naïve and YMDD-mutant HBeAg-positive CHB |
| [NCT01373684](https://clinicaltrials.gov/study/NCT01373684) | Phase 4 | Completed | 90 | Add-on PEG-IFN alfa-2a to NA therapy to enhance HBsAg decline in HBeAg-negative CHB |

*(50 clinical trials total are referenced in the evidence pack for this indication; the 10 above represent the largest, most directly HBV-relevant completed Phase 3/4 studies.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | New England Journal of Medicine | Landmark trial: PEG-IFN alfa-2a ± lamivudine vs lamivudine alone for HBeAg-positive CHB — established PEG-IFN's role in modern CHB therapy |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + PEG-IFN alfa-2a in HBeAg-positive immune-tolerant CHB adults |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review/Meta-analysis | Antiviral Therapy | Individual participant data meta-analysis defining PEG-IFN alfa-2a stopping rules in CHB |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Comprehensive review of chronic HBV infection, treatment landscape including PEG-IFN |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Overview of hepatitis B therapy goals and treatment response monitoring |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | Clinical Trial | Hepatology | Entecavir/PEG-IFN alfa-2a combination in children with HBeAg-positive immune-tolerant CHB |
| [33339708](https://pubmed.ncbi.nlm.nih.gov/33339708/) | 2021 | Cohort | Journal of the Formosan Medical Association (Taiwan) | Virological/immunological predictors of long-term outcomes of PEG-IFN therapy in HBeAg-negative CHB |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | RCT | Virology Journal | Long-term effects of PEG-IFN alfa-2a in Japanese CHB patients |
| [18220290](https://pubmed.ncbi.nlm.nih.gov/18220290/) | 2008 | Clinical Trial (Phase 3 registration) | Hepatology | HBeAg and HBV DNA as outcome predictors during PEG-IFN alfa-2a therapy |
| [16013986](https://pubmed.ncbi.nlm.nih.gov/16013986/) | 2005 | Expert Review | Expert Opinion on Pharmacotherapy | Review of PEG-IFN alfa-2a approval and clinical trial evidence in hepatitis B |

---

## Germany Market Information

No marketing authorizations are currently on record for Peginterferon Alfa-2a in the Germany regulatory dataset (`market_status: 未上市 / Not Marketed`, 0 total licenses). This is inconsistent with the drug's well-documented clinical trial history and likely reflects a data completeness gap in the regulatory source rather than an actual absence from the German market — this should be verified directly against BfArM records before finalizing any decision.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) is not currently available in this dataset. Notably, this is flagged as a **Blocking-severity data gap (DG001: TFDA/BfArM label warnings and contraindications)** — meaning this candidate cannot formally enter the S1 safety initial-review stage until label data is obtained (e.g., by downloading and parsing the official product label PDF).

Please refer to the official package insert for complete safety information in the interim.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical evidence base for Peginterferon Alfa-2a in Hepatitis B Virus Infection is exceptionally strong (L1, including a landmark Phase 3 NEJM RCT and dozens of completed Phase 3/4 trials), but the rationale itself indicates this largely confirms an already-established use rather than a novel repurposing opportunity. Combined with a Blocking safety data gap and an apparently incomplete German market record, the candidate should proceed only with guardrails until foundational regulatory data is filled in.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official TFDA/BfArM product label for warnings, contraindications, and DDI data
- Resolve DG002 (High): confirm mechanism of action via DrugBank API query
- Verify actual German market/authorization status against BfArM records (current "0 licenses" appears to be a data gap, not a true absence)
- Confirm and document the drug's actual original approved indication(s) to correctly classify this as label-confirmation vs. true repurposing
- Consider Hepatitis E virus infection (rank 2, L3 evidence: humanized-mouse model + case reports + one systematic review) as a separate, genuinely exploratory research question worth independent follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

