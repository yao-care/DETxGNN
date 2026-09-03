---
layout: default
title: Grazoprevir
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Grazoprevir
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

# Grazoprevir: From Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Grazoprevir is an HCV NS3/4A protease inhibitor marketed as part of the fixed-dose combination Zepatier® (grazoprevir + elbasvir), used for chronic hepatitis C virus (HCV) genotype 1, 4, and 6 infection. TxGNN predicts a **99.73% score** for "HIV infectious disease," but on review, **all supporting clinical trials and literature describe treating HCV in patients who are co-infected with HIV — not treating HIV itself**. This is very likely a database co-occurrence artifact rather than a genuine pharmacological signal, and the evidence pack itself flags this rationale explicitly.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C virus (HCV) genotype 1, 4, 6 infection — as the protease-inhibitor component of Zepatier® (grazoprevir + elbasvir). (Not present in the structured `original_indications` field; derived from consistent evidence across trials/literature in this pack.) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 (model prediction only; no study directly treats HIV with grazoprevir) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Detailed formal MOA data for grazoprevir was flagged as a data gap in this evidence pack. However, the evidence itself (trial descriptions and literature abstracts) consistently identifies grazoprevir as an **HCV NS3/4A protease inhibitor**, co-formulated with the NS5A inhibitor elbasvir under the brand Zepatier®, used to achieve sustained virologic response (SVR) in chronic HCV infection.

Critically, **this mechanism has no known relevance to HIV**. HIV requires inhibition of its own protease, reverse transcriptase, or integrase enzymes — none of which are structurally related to HCV NS3/4A protease. Every single clinical trial and literature record returned for this candidate describes treating **HCV** in patients who happen to also carry HIV (HIV/HCV co-infection populations), evaluating HCV cure rates (SVR12), liver fibrosis, cardiovascular risk, or drug-drug interactions with antiretrovirals. None evaluate grazoprevir as a treatment for HIV itself, and no viral suppression or CD4/viral-load endpoint for HIV is reported anywhere in this evidence set.

**Conclusion of this section: the prediction is not mechanistically or clinically supported.** It most plausibly reflects a graph-embedding artifact caused by the frequent co-occurrence of "grazoprevir" and "HIV" in trial metadata for HCV/HIV co-infected cohorts, rather than a true repurposing signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Completed | 218 | C-EDGE CO-INFECTION: GZR+EBR for **HCV** GT1/4/6 in HIV/HCV co-infected, treatment-naïve subjects — evaluates HCV SVR12, not HIV outcomes. |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Completed | 573 | C-WORTHY: GZR+EBR±RBV for **HCV**; HIV/HCV co-infected arm included, primary endpoint is HCV SVR12. |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Completed | 159 | GZR+EBR for **HCV** GT1/4/6 in patients with inherited blood disorders, with/without HIV co-infection. |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Completed | 150 | Swiss HCVree Trial: "treat, counsel, cure" strategy for **HCV** in HIV-positive MSM; HIV itself not a treatment target. |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unknown | 1000 | HEPAVIR cohort: real-world efficacy/tolerability of DAA regimens for **HCV** in HIV/HCV co-infected patients. |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | DAHHS-2: GZR+EBR for **acute HCV** genotype 1/4 in HIV-positive individuals. |
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unknown | 62 | GZR/EBR for early chronic **HCV** GT1/4 in HIV co-infected patients (8 vs 12 weeks). |
| [NCT03037151](https://clinicaltrials.gov/study/NCT03037151) | Phase 4 | Unknown | 100 | Safety/fibrosis improvement with GZR+EBR for **HCV** GT1/6, cirrhotic, with or without HIV. |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Completed | 40 | GZR+EBR for **HCV** GT1 in PWID/MSM with HIV co-infection, prior peg-IFN/RBV experienced. |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after **HCV** eradication in HIV/HCV co-infected vs HIV mono-infected controls — not an HIV efficacy trial. |

**Every trial above treats HCV in an HIV-positive population; none treats HIV as the target disease.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | RCT | The Lancet HIV | C-EDGE CO-INFECTION: GZR+EBR efficacy/safety for **HCV** in HIV/HCV co-infected patients. |
| [25467560](https://pubmed.ncbi.nlm.nih.gov/25467560/) | 2015 | RCT (Phase 2) | Lancet | C-WORTHY: 8 vs 12 weeks GZR+EBR±RBV for **HCV** GT1 mono- and HIV/HCV co-infection. |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Review | Expert Opin Drug Metab Toxicol | Reviews drug-drug interactions between DAAs (incl. grazoprevir) and antiretrovirals in HIV patients being treated for HCV. |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | PK study | Antimicrob Agents Chemother | PK interactions of elbasvir/grazoprevir with HIV protease inhibitors (ritonavir, atazanavir, lopinavir, darunavir). |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | DDI study | J Antimicrob Chemother | Interaction assessment between elbasvir/grazoprevir and HIV integrase inhibitors (raltegravir, dolutegravir). |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Systematic review / meta-analysis | J Gastroenterol Hepatol | Network meta-analysis of DAA regimen efficacy/safety for **HCV** in HIV/HCV co-infected patients. |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Review | Drugs | Comprehensive review of elbasvir/grazoprevir for chronic **HCV** GT1/4. |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Review | Drug Des Devel Ther | Safety and efficacy evidence for elbasvir/grazoprevir in **HCV**. |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Review | Expert Rev Clin Pharmacol | MOA, PK/PD, efficacy and safety review of elbasvir/grazoprevir for **HCV** GT1/4. |
| [26849059](https://pubmed.ncbi.nlm.nih.gov/26849059/) | 2016 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics/pharmacokinetics of elbasvir and grazoprevir in **HCV** treatment. |

**None of the literature above evaluates grazoprevir as an anti-HIV agent** — the DDI/PK papers characterize how to safely combine grazoprevir with antiretrovirals when treating HCV in HIV-positive patients, not anti-HIV efficacy of grazoprevir itself.

## Taiwan Market Information

Grazoprevir (and the Zepatier® combination) is **not currently marketed in Taiwan** — 0 registered authorizations, no dosage forms recorded. This means no local regulatory or safety-label information is available to review.

## Safety Considerations

Structured safety data (key warnings, contraindications, DDI database) were not available for this candidate. However, the literature evidence pack does contain sourced pharmacokinetic interaction data relevant to any future HIV-related use:

- **Drug Interactions (from literature, not structured DDI data):** Elbasvir/grazoprevir shows clinically significant pharmacokinetic interactions with ritonavir-boosted HIV protease inhibitors (ritonavir, atazanavir, lopinavir, darunavir) and with HIV integrase inhibitors (raltegravir, dolutegravir) (PMID [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/), [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/)). These interactions matter for HIV/HCV co-infected patients receiving both drug classes concurrently, but do not indicate anti-HIV activity of grazoprevir.

For all other safety information, please refer to the package insert once formally reviewed by TFDA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score (99.73%) is not corroborated by any trial or literature evidence of grazoprevir treating HIV directly. All 10+ trials and 20 literature records identified are HCV-treatment studies conducted in HIV/HCV co-infected populations — a classic co-occurrence confound in knowledge-graph models. There is no known or plausible molecular mechanism (grazoprevir targets HCV NS3/4A protease; HIV depends on protease/reverse transcriptase/integrase from an unrelated retroviral family) supporting anti-HIV activity. Grazoprevir is also not currently marketed in Taiwan.

**To proceed, the following is needed (before this can be considered anything other than Hold):**
- In vitro assay data confirming (or refuting) grazoprevir activity against HIV protease, reverse transcriptase, or integrase
- Formal DrugBank/TFDA MOA and label documentation (currently a data gap)
- If in vitro signal is negative (expected), this candidate should be closed rather than advanced

**Note on other ranked predictions in this pack:** Ranks 2–10 (HBV, HEV, HAV, animal hepatitis, Omsk hemorrhagic fever, SIV, FIV, a rare neurodevelopmental disorder) were also reviewed and show the same or weaker pattern — all scored "Hold" (L5, no genuine mechanistic or clinical support), except rank 7 (Kyasanur forest disease), which was flagged as a low-priority **research question** based on one in-silico docking study (PMID 34662258) exploiting cross-genus Flaviviridae NS3 protease conservation — still requiring wet-lab validation before any further action.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

