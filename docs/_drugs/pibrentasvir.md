---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is an NS5A inhibitor marketed only as part of the fixed-dose combination glecaprevir/pibrentasvir (Mavyret), approved for chronic **Hepatitis C virus (HCV)** infection. The TxGNN model predicts a possible effect on **Hepatitis B virus (HBV) infection** (score 99.84%), but on review the supporting **14 clinical trials** and **20 publications** all study glecaprevir/pibrentasvir for HCV — none test the drug against HBV, and the evidence reviewers flagged this as a likely graph co-occurrence artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C virus (HCV) infection, as a component of the glecaprevir/pibrentasvir fixed-dose combination (Mavyret) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no direct supporting studies) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal, sourced mechanism-of-action record for pibrentasvir is not currently available in this evidence pack (data gap, high severity — see DG002). Based on information embedded in the trial and literature evidence, however, pibrentasvir is known to be an HCV NS5A protein dimerization inhibitor, always co-administered with glecaprevir (an NS3/4A protease inhibitor) as Mavyret. Its efficacy is well established for chronic HCV genotypes 1–6.

HCV (Flaviviridae, *Hepacivirus*) and HBV (Hepadnaviridae) are taxonomically and structurally unrelated viruses. HBV has no NS5A homolog, so there is no known target-level basis for cross-activity. Reviewing the 14 clinical trials and 20 publications linked to this prediction, all of them evaluate glecaprevir/pibrentasvir efficacy, safety, or pharmacokinetics **in HCV-infected patients**; a few touch on HBV only tangentially (e.g., HBV vaccination after HCV cure, or HBV/HCV co-screening populations), never as a treatment endpoint for HBV itself.

This pattern is consistent with the reviewers' assessment: the high TxGNN score likely reflects a graph co-occurrence signal (HBV and HCV are frequently screened, studied, and discussed together in the same clinical and literature contexts) rather than a real pharmacological relationship. Mechanistically, there is currently no basis to expect pibrentasvir to have anti-HBV activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected patients; not an HBV study. |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | Efficacy/safety of GLE/PIB in treatment-naïve Brazilian adults with chronic HCV GT1–6; no HBV endpoint. |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Completed | 304 | ENDURANCE-2: GLE/PIB efficacy/safety in HCV genotype 2 infection; graded C — not relevant to HBV. |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | SURVEYOR-II: GLE/PIB ± ribavirin in chronic HCV GT2–6; graded C — HBV co-infection possibly excluded/screened, not treated. |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | SURVEYOR-I: GLE/PIB ± ribavirin in HCV GT1,4,5,6 infection. |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Completed | 89 | Dose-ranging safety/antiviral activity of GLE/PIB components in HCV GT1 infection. |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Completed | 384 | Long-term follow-up of DAA resistance durability in prior HCV GLE/PIB trial participants. |
| [NCT02296905](https://clinicaltrials.gov/study/NCT02296905) | Phase 1 | Completed | 24 | Pharmacokinetics/safety of GLE/PIB in hepatic impairment (not HBV-specific). |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | G/P ± ribavirin in GT1 HCV patients previously treated with an NS5A inhibitor + sofosbuvir. |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | ENDURANCE-3: GLE/PIB vs. sofosbuvir+daclatasvir in HCV genotype 3 infection. |

**Note:** All 14 trials associated with this prediction study glecaprevir/pibrentasvir for HCV treatment. None enroll patients for an HBV treatment endpoint.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | Lancet Infect Dis | Discusses HBV vaccination after HCV treatment — a care-pathway topic, not anti-HBV drug efficacy. |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Review | Cancers | Reviews hepatocellular carcinoma risk in chronic kidney disease; mentions viral hepatitis as a risk factor context only. |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | Real-world GLE/PIB effectiveness/safety in HCV patients with severe renal impairment in Taiwan. |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | Overview of HCV infection management in children/adolescents. |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | — | Hepatology | Characterizes HCV protease-inhibitor resistance-associated substitutions. |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Reviews management advances for pediatric HBV and HCV, discussing both viruses separately (no combined therapy claim). |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | — | Eur J Gen Pract | Practical guide to chronic HCV diagnosis and treatment for primary care. |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | — | Semin Liver Dis | Reviews retreatment strategies for HCV patients who failed prior DAA regimens. |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | — | World J Gastroenterol | Real-world DAA effectiveness in HIV/HCV genotype 6 co-infected patients. |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | — | Ann Hepatol | Cross-country comparison of HBV and HCV antiviral drug pricing (health-economics topic, not efficacy data). |

**Note:** None of the reviewed literature reports pibrentasvir being tested for, or effective against, HBV.

---

## Germany Market Information

Pibrentasvir is currently **not marketed** in Germany, and no BfArM authorization records exist for this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A blocking data gap exists — official warnings/contraindications from the label are not yet available, which prevents a full S1 safety assessment. See remediation plan below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but every piece of supporting evidence (14 trials, 20 publications) concerns glecaprevir/pibrentasvir's established use against HCV, not HBV. There is no mechanistic basis (HBV lacks an NS5A homolog) and no direct experimental or clinical data suggesting anti-HBV activity. The evidence level is L5 — model prediction only — and the drug is unlicensed in this market. The same pattern holds across this drug's other top-10 TxGNN predictions (HIV, HEV, HAV, Omsk hemorrhagic fever, Kyasanur forest disease, and several animal/rare-disease indications), which the evidence reviewers likewise flagged as graph co-occurrence noise or taxonomic-homology artifacts with no supporting data. This candidate should not advance beyond Hold without new primary evidence.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action documentation (DG002 remediation via DrugBank API)
- TFDA/BfArM label warnings and contraindications (DG001 — blocking, required before any S1 safety review)
- In vitro anti-HBV screening data for pibrentasvir, if repurposing interest continues
- Reassessment against future TxGNN model versions with cleaner disease-similarity signal, given the apparent HCV/HBV co-occurrence bias observed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

