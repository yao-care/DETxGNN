---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

Using the report as a literal extraction-and-synthesis task against the supplied Evidence Pack (no coding/debugging skill applies here) — below is the report.

---

# Glecaprevir: From Hepatitis C Virus Infection to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an HCV NS3/4A protease inhibitor, part of the glecaprevir/pibrentasvir (Mavyret) combination used to treat chronic hepatitis C. The TxGNN model predicts it may be effective for **HIV infectious disease**, but the **15 clinical trials** and **20 publications** retrieved all evaluate HCV treatment (including in HIV/HCV-coinfected populations) — none measure an HIV treatment endpoint, and the mechanistic evidence argues against this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C (HCV) infection, genotypes 1–6 (inferred from trial and mechanistic evidence; no formal regulatory indication text available in this dataset) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not. Glecaprevir is an NS3/4A serine protease inhibitor specific to hepatitis C virus. HIV's essential protease is an aspartyl protease from an entirely different structural family with no target homology to HCV NS3/4A — there is no known or plausible mechanism by which glecaprevir would inhibit HIV replication.

The apparent link is almost certainly a labeling/embedding artifact: nearly all of the supporting clinical trials and literature concern treating **HCV** in patients who happen to also have **HIV** (HIV/HCV coinfection), not treating HIV itself. TxGNN's high similarity score likely reflects proximity in a shared "viral infection" embedding space rather than a genuine pharmacological signal.

Because the drug is not marketed in Germany (0 authorizations) and core safety data (TFDA warnings/contraindications) are unavailable, there is currently no basis — mechanistic, clinical, or regulatory — to advance this candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Compares cardiovascular risk after HCV cure in HIV/HCV-coinfected vs. HIV-mono-infected patients — endpoint is HCV eradication, not HIV control (Grade C: not HIV-relevant) |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | 4-week G/P regimen for acute HCV, with or without HIV-1 coinfection — endpoint is HCV cure |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | Completed | 42 | Real-world G/P effectiveness in DAA-experienced chronic HCV genotype 1 patients (Russia) — HCV SVR endpoint only |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | Completed | 33 | G/P + sofosbuvir + ribavirin for HCV patients with prior virologic failure — HCV endpoint only |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | DAA regimens (incl. G/P) for recently acquired HCV, with/without HIV co-infection — HCV endpoint (Grade C) |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | NA | Completed | 17 | Telemedicine delivery of HIV PrEP, MOUD, and HCV treatment at needle exchanges — a service-access study, not a drug efficacy trial for HIV (Grade C) |
| [NCT02604017](https://clinicaltrials.gov/study/NCT02604017) | Phase 3 | Completed | 703 | ABT-493/ABT-530 (G/P) efficacy/safety in genotype 1 HCV — HCV endpoint (Grade C) |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | G/P in Asian HCV genotype 1-6 patients with compensated cirrhosis, with/without HIV co-infection — HCV endpoint |
| [NCT03868163](https://clinicaltrials.gov/study/NCT03868163) | N/A | Completed | 161 | Real-world G/P effectiveness in chronic HCV genotypes 1-6 (Russia) — HCV endpoint only |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not yet recruiting | 30 | PK/safety of G/P initiated during pregnancy in HCV patients with/without HIV — HCV endpoint |

**Across all 10 trials, the treatment endpoint is HCV virologic clearance (SVR), including in HIV-coinfected subgroups — none tests glecaprevir as an anti-HIV therapy.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Real-world G/P response in HIV/HCV-coinfected patients — assesses HCV cure rates, not HIV outcomes |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | PK/DDI study | J Infect Dis | Characterizes drug-drug interactions between G/P and HIV antiretrovirals — relevant for safe coadministration, not evidence of anti-HIV activity |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case report | Clin J Gastroenterol | HIV/HCV-coinfected hemophilia patient successfully treated with G/P for HCV genotype 4a |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Review of HCV protease inhibitor therapy, discusses HIV/HCV coinfection context |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infect Dis | Review of HCV protease inhibitors; notes 25–30% HIV/HCV coinfection prevalence in Europe/US |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV treatment landscape in children and adolescents |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Primary-care overview of chronic HCV diagnosis and treatment |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | Overview of glecaprevir/pibrentasvir for chronic HCV |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Review | Hepatol Int | G/P expands HCV treatment reach while reducing cost/duration |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Reviews | Viral hepatitis conference summary; HBV/HCV burden estimates |

**All 20 retrieved publications concern HCV treatment or HIV/HCV coinfection management. None reports anti-HIV activity for glecaprevir.**

## Safety Considerations

Please refer to the package insert for safety information. TFDA/BfArM warnings, contraindications, and drug-drug interaction data are not currently available for this compound (flagged as a **Blocking** data gap in this evidence pack).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HIV infectious disease) lacks any mechanistic basis — glecaprevir targets a viral protease family unrelated to HIV — and every retrieved trial and publication actually studies HCV treatment, not HIV treatment. This pattern also holds across ranks 2–10 (HBV, HAV, HEV, SIV, feline AIDS, Omsk hemorrhagic fever, Kyasanur forest disease, and an unrelated neurodevelopmental disorder), all scored L4/L5 evidence with "Hold" recommendations, suggesting the model's embedding for glecaprevir is dominated by a generic "viral infection" signal rather than target-specific pharmacology.

**To proceed, the following is needed:**
- TFDA/BfArM label data (warnings, contraindications) — currently a blocking gap
- Verified mechanism-of-action and DDI data from DrugBank or manufacturer labeling
- A re-scoped TxGNN query or manual mechanistic review to determine whether any of the 10 candidates reflect a genuine repurposing signal, versus viral-infection embedding conflation
- If pursuing HIV/HCV coinfection management (not de novo HIV treatment) as an indication, reframe the candidate accordingly and re-evaluate evidence under that framing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

