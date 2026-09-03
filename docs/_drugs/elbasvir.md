---
layout: default
title: Elbasvir
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Elbasvir
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

# Elbasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Elbasvir is an NS5A replication-complex inhibitor developed as part of the fixed-dose combination grazoprevir/elbasvir (Zepatier), established for chronic **hepatitis C virus (HCV)** genotype 1, 4, and 6 infection — though this is inferred from trial and literature context, as no structured original-indication data was returned.
> The TxGNN model ranks **hepatitis B virus (HBV) infection** as its top new-indication prediction, with **13 clinical trials** and **18 publications** attached as supporting evidence.
> However, on review, every one of these studies is actually an HCV trial or HCV-focused publication — none involves HBV patients or HBV virologic endpoints — so the supporting evidence does not substantiate this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) genotype 1/4/6 infection (inferred from trial/literature context; not present in structured drug record) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no HBV-specific study) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this record. Based on established pharmacology, elbasvir is an inhibitor of the HCV NS5A protein, a non-structural protein unique to the *Hepacivirus* genus (family *Flaviviridae*). It is co-formulated with the NS3/4A protease inhibitor grazoprevir and used exclusively for chronic HCV genotype 1, 4, and 6 infection.

HBV, in contrast, is a hepadnavirus — a partially double-stranded DNA virus that replicates via reverse transcription of an RNA intermediate. It has no NS5A homolog and no known point of pharmacological overlap with HCV NS5A inhibitors. The two viruses share only the clinical label "viral hepatitis," not a common replication mechanism or drug target.

Consistent with this, the evidence pack's own mechanistic review concludes the HBV prediction is most likely a **TxGNN embedding artifact**: because HBV and HCV cluster closely in disease-embedding space (both being "viral hepatitis" entities), the model surfaces HCV-specific trial evidence under the HBV prediction even though none of it involves HBV patients or endpoints. This should be treated as a false positive pending any independent mechanistic or in vitro signal specific to HBV.

---

## Clinical Trial Evidence

All trials below were retrieved as "supporting evidence" for the HBV prediction. On inspection, every trial actually studies HCV (genotype 1/4/6, with or without HIV co-infection or hepatic/renal impairment) — none enrolled HBV patients or measured HBV outcomes.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | HCV eradication and cardiovascular risk in HIV/HCV co-infection — no HBV arm |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Phase 2/3 | Completed | 40 | Grazoprevir+elbasvir in HCV GT1/4/6 with Child-Pugh B hepatic insufficiency |
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Phase 2 | Completed | 15 | Pembrolizumab in HCV-positive/negative HCC — elbasvir not the study drug |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Completed | 573 | Grazoprevir+elbasvir ± ribavirin, chronic HCV, SVR12 endpoint |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | Grazoprevir+elbasvir for acute HCV genotype 1/4 |
| [NCT01932762](https://clinicaltrials.gov/study/NCT01932762) | Phase 2 | Completed | 98 | Grazoprevir ± elbasvir/ribavirin in HCV GT2/4/5/6, treatment-naive |
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Completed | 48 | Elbasvir monotherapy PK/PD in HCV-infected males |
| [NCT03797066](https://clinicaltrials.gov/study/NCT03797066) | Phase 4 | Terminated | 13 | Point-of-care HCV test-and-treat with grazoprevir/elbasvir in homeless population |
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Completed | 413 | Grazoprevir+uprifosbuvir with elbasvir or ruzasvir, HCV GT3/4/5/6 |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Completed | 301 | Grazoprevir/elbasvir in HCV GT1/4/6 patients on opiate substitution therapy |

*Note: 3 additional trials in the evidence set were pre-graded relevance "C" (i.e., judged not relevant to HBV) and are omitted here for brevity.*

---

## Literature Evidence

None of the 18 publications attached to this prediction report an HBV-specific study of elbasvir. Two (marked below) discuss HBV only in passing, as a contrast to HCV.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver International | "Towards eradication of HCV and a cure for HBV" — discusses the two viruses as distinct disease entities, not a shared drug mechanism |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional | Annals of Hepatology | Compares HBV vs. HCV antiviral drug pricing — economic, not mechanistic, comparison |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharmaceutica Sinica B | Overview of direct-acting anti-HCV agents; explicitly notes HCV is curable unlike HIV/HBV |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Phase 4 trial | Antimicrobial Agents and Chemotherapy | Grazoprevir/elbasvir in HCV GT1b liver/kidney transplant recipients |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Basic science | Hepatology | HCV protease inhibitor resistance-variant evolution |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Real-world study | Journal of Viral Hepatitis | Elbasvir/grazoprevir liver and renal safety in Taiwanese HCV patients |
| [29077864](https://pubmed.ncbi.nlm.nih.gov/29077864/) | 2018 | RCT | Clinical Infectious Diseases | Sofosbuvir+grazoprevir/elbasvir retreatment of HCV GT1/4 after prior DAA failure |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Review | Klinická Mikrobiologie a Infekční Lékařství | Antiviral treatment of chronic HBV **and** HCV in children — combined review, not HBV-specific elbasvir data |
| [32306039](https://pubmed.ncbi.nlm.nih.gov/32306039/) | 2020 | Cohort study | Journal of Antimicrobial Chemotherapy | Grazoprevir/elbasvir for recently acquired HCV GT1/4 in MSM |
| [30049677](https://pubmed.ncbi.nlm.nih.gov/30049677/) | 2018 | Case report | BMJ Case Reports | HCV-associated dermatomyositis case; unrelated to HBV |

---

## Germany Market Information

Elbasvir currently has **no marketing authorization in Germany** — the drug record shows 0 licenses and market status "Not marketed." No Germany product table can be generated from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Two structural data gaps were flagged in this evidence pack that block a full safety assessment:

- **TFDA/BfArM label warnings and contraindications** — not yet retrieved (Blocking severity; required before this candidate can enter safety pre-screening).
- **Mechanism of action detail** — not yet retrieved from DrugBank (High severity; needed to properly assess mechanistic plausibility for any new indication).

No drug-drug interaction data was found (query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HBV prediction carries the model's own L5 evidence rating (prediction-only, no supporting study), and manual review confirms all 13 attached trials and 18 publications are HCV-specific with no HBV patients or endpoints — indicating the signal is most likely a disease-embedding artifact rather than a genuine repurposing opportunity. Compounding this, elbasvir has no marketing authorization in Germany and a Blocking-severity data gap on label safety information, so it cannot proceed regardless of the indication question.

**To proceed, the following is needed:**
- Confirmed drug label (TFDA/BfArM) warnings, contraindications, and DDI profile
- DrugBank-sourced mechanism-of-action confirmation for elbasvir
- Any independent in vitro or in vivo evidence of elbasvir activity against HBV replication (currently none identified)
- If no HBV-specific mechanistic or preclinical signal emerges, this candidate should be deprioritized in favor of the pipeline's other predicted indications, none of which (HEV, HAV, animal hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, FIV, SIV, or the neurodevelopmental disorder) currently have supporting mechanistic rationale either — all carry the same "Hold" recommendation in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

