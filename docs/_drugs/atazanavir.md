---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atazanavir: From HIV-1 Infection to Congenital/Perinatal HIV Exposure & AIDS-Related Complex

## One-Sentence Summary

> Atazanavir (DrugBank DB01072) is an HIV-1 protease inhibitor originally developed for HIV-1 infection (marketed as Reyataz).
> The TxGNN model's best-supported prediction extends this to **congenital/perinatal HIV exposure** and **AIDS-related complex** —
> not a novel mechanism, but a formal consolidation of the drug's existing antiretroviral use, backed by **30+ clinical trials**
> and **10 publications**. The model's top four raw-ranked predictions (feline AIDS, SIV infection, a rare neurodevelopmental
> disorder, and hyperlipidemia) show no credible mechanistic or evidentiary support and have been excluded from this report as
> likely knowledge-graph artifacts (see note below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy, brand Reyataz) — inferred from trial/rationale data; not present in Evidence Pack license fields (drug not marketed in Germany) |
| Predicted New Indication | Congenital/Perinatal HIV Exposure & AIDS-Related Complex (indication consolidation, not a novel mechanism) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable (Data Gap DG002). Based on the trial and literature
evidence available, atazanavir is an HIV-1 aspartyl protease inhibitor: it blocks cleavage of the Gag-Pol polyprotein
precursor, preventing maturation of infectious virions and halting viral replication.

The two indications with real supporting evidence — "AIDS-related complex" and "congenital human immunodeficiency virus" —
are not mechanistically distinct from atazanavir's original HIV-1 indication. AIDS-related complex is simply an earlier/broader
clinical staging term for HIV disease, and congenital HIV exposure concerns the same virus and the same protease target in a
perinatal/pediatric population. Extensive Phase 3 trial history (including two dedicated pediatric programs, PRINCE I and
PRINCE II) and multiple pregnancy pharmacokinetic and safety cohort studies (e.g., PHACS SMARTT, IMPAACT P1026s) support use
across these populations. This should be read as **label/population extension of an already-approved use**, not a genuine
drug-repurposing discovery.

### Note: Lower-Confidence Predictions Excluded from This Report

The Evidence Pack's top four ranked candidates were not carried forward as headline findings, because the pack's own
rationale flags each as implausible or unsupported:

| Rank | Disease | Score | Issue |
|------|---------|-------|-------|
| 1 | Feline acquired immunodeficiency syndrome | 99.98% | Veterinary indication (FIV); HIV-1 protease specificity does not cross-react; likely embedding-similarity false positive ("immunodeficiency virus" text overlap) |
| 2 | Simian immunodeficiency virus infection | 99.98% | Non-human-primate animal model only; no clinical trials, single animal-study citation |
| 3 | Rare neurodevelopmental disorder (ataxic gait, absent speech, decreased white matter) | 99.98% | No known mechanistic relationship to protease inhibition; no evidence at all |
| 4 | (Obsolete) familial combined hyperlipidemia | 99.82% | Evidence points the *opposite* direction — atazanavir is comparatively lipid-neutral versus other PIs; disease term itself is deprecated |

These should not be pursued as repurposing candidates without independent validation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | PK of antiretroviral & anti-TB drugs during pregnancy and postpartum |
| [NCT00326716](https://clinicaltrials.gov/study/NCT00326716) | Phase 1 | Completed | 69 | ATV/RTV dosing and PK in HIV-1 infected pregnant women |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4/N/A | Completed | 1578 | IMPAACT P1026s: large PK study of ARV/TB drugs in pregnant women and infants |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | Safety of ATV capsule + RTV in HIV-infected pediatric patients (6–18y) |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: ATV powder + RTV safety/efficacy/PK in pediatric patients (3mo–6y) |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II: ATV powder + RTV in pediatric patients (3mo–11y) |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS: switch to long-acting cabotegravir + rilpivirine vs. continuing ART (incl. PI-based regimens) |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1149 | Switch to D/C/F/TAF vs. continuing boosted-PI regimen in virologically suppressed HIV-1 patients |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | DTG/ABC/3TC vs. ATV+RTV+TDF/FTC in ART-naive **women** (relevant to childbearing-age population) |
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1057 | 96-week ATV/RTV vs. LPV/RTV + TDF/FTC efficacy and safety in treatment-naive HIV-1 patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohort (PHACS SMARTT) | Frontiers in Immunology | Large (3,500+) HIV-exposed-uninfected infant/child cohort assessing safety of in-utero ARV exposure |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Congenital anomalies and in-utero ARV exposure in HIV-exposed uninfected infants |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/non-case study | Eur J Clin Pharmacol | European registry study of congenital anomaly risk after fetal ARV exposure |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort | Antiviral Therapy | Atazanavir exposure remains effective during pregnancy regardless of tenofovir co-administration |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance database analysis | Clin Infect Dis | Comparator safety-signal analysis for ARVs in pregnancy (dolutegravir focus) |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cohort | J AIDS Immune Res | Newborn hearing screening outcomes in HIV-exposed uninfected infants |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In vitro mechanistic study | Reproductive Toxicology | ATV/RTV interactions with placental ABC transporters affecting transplacental disposition |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | GI adverse event risk factors in HIV-treated vs. untreated patients (protease-inhibitor context) |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohort | J Acquir Immune Defic Syndr | ART regimen choice and incidence of AIDS-defining neurological conditions |

## Safety Considerations

Please refer to the package insert for safety information. No drug-specific warnings, contraindications, or drug-interaction
data were retrievable in this Evidence Pack (DDI query returned no results; TFDA/BfArM label data marked as a **Blocking**
data gap — DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although congenital/perinatal HIV exposure and AIDS-related complex are backed by strong (L1) trial and cohort evidence, this
represents consolidation of atazanavir's *existing* HIV/AIDS indication rather than a genuine new repurposing opportunity. More
importantly, a **Blocking**-severity data gap (missing TFDA/BfArM label warnings and contraindications) prevents any safety
evaluation (S1), and the drug currently holds zero marketing authorizations in Germany. The model's top four raw-ranked
predictions were separately assessed and rejected as low-credibility artifacts.

**To proceed, the following is needed:**
- TFDA/BfArM label PDF retrieval and parsing for warnings/contraindications (resolves DG001, currently blocking)
- DrugBank MOA confirmation (resolves DG002)
- A regulatory determination of whether "congenital HIV" / "AIDS-related complex" require a distinct submission or fall under the existing HIV-1 indication scope
- If a genuine repurposing signal is desired, re-run TxGNN scoring excluding the four flagged artifact predictions and review any remaining mid-ranked candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

