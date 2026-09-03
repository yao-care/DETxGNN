---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
---

# Dolutegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Dolutegravir is an integrase strand transfer inhibitor (INSTI) used in combination antiretroviral therapy for HIV-1 infection in humans.
> The TxGNN model predicts it may be effective against **Feline Acquired Immunodeficiency Syndrome** (feline immunodeficiency virus, FIV — the feline lentiviral analogue of HIV),
> with **5 human HIV-1 clinical trials** supporting the parent compound's antiviral mechanism and **1 direct preclinical study** in FIV-infected cats.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (not recorded as a formal regulatory indication in this evidence pack — drug holds no marketing authorization in Germany; inferred from clinical trial descriptions) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 for the parent HIV-1 indication (≥2 completed Phase 3 RCTs); direct translational evidence for feline AIDS itself is limited to a single preclinical animal study (L4-equivalent) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dolutegravir is not available in this evidence pack. Based on the associated clinical trial descriptions, dolutegravir is an integrase strand transfer inhibitor (INSTI), dosed once daily and typically combined with dual NRTI backbones (e.g., abacavir/lamivudine, tenofovir/emtricitabine) for treatment of HIV-1 infection; its efficacy has been established in this setting across multiple completed Phase 2/3 trials.

Feline immunodeficiency virus (FIV) is a lentivirus closely related to HIV that causes a progressive, AIDS-like immunodeficiency syndrome in domestic cats. Because retroviral integrase enzymes are functionally conserved across lentiviruses, an INSTI mechanism developed against HIV-1 integrase is mechanistically plausible against FIV integrase as well — which is precisely the rationale tested in the one directly relevant publication in this pack (Kim et al., 2023), where a dolutegravir-containing combination antiretroviral regimen was evaluated pharmacokinetically and clinically in FIV-infected cats.

It is important to note that the five clinical trials listed under this predicted indication were all conducted in human HIV-1 populations, not in FIV-infected cats. They establish confidence in dolutegravir's core antiviral mechanism and human safety/PK profile, but they do not constitute direct efficacy evidence for feline AIDS. Direct translational support currently rests on a single small preclinical/veterinary study.

---

## Clinical Trial Evidence

*(Trials below evaluate dolutegravir in human HIV-1 infection — the mechanistic basis for the FIV prediction — not FIV itself.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Single-arm study of dolutegravir 50mg QD + abacavir/lamivudine in ART-naïve HIV-1 subjects; evaluated CNS/plasma PK over 96 weeks |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla in ART-naïve HIV-1 subjects; non-inferiority over 96 weeks |
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir vs. raltegravir (integrase-naïve, ART-experienced HIV-1 subjects), both with background regimen, over 48 weeks |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of dolutegravir with ABC/3TC or TDF/FTC in ART-naïve HIV-1 subjects |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. raltegravir, both with dual-NRTI backbone, in ART-naïve HIV-1 subjects over 96 weeks |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical (animal study) | Viruses | Combination ART (dolutegravir 2.5 mg/kg + tenofovir + emtricitabine) evaluated in FIV-infected domestic cats; assessed pharmacokinetics and immunophenotype/clinical outcomes, directly supporting the repurposing hypothesis |

---

## Germany Market Information

Dolutegravir is currently **not marketed** in Germany under this evidence pack (0 authorizations on record). No product-level licensing data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although dolutegravir's parent HIV-1 indication is backed by multiple completed Phase 3 RCTs, direct evidence for the predicted feline AIDS indication is limited to a single small preclinical study, the drug has no marketing authorization in Germany, and the required safety/labeling data (TFDA warnings and contraindications) are currently a **Blocking** data gap that prevents a formal S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — resolves DG001 (Blocking)
- Confirmed mechanism-of-action data via DrugBank API — resolves DG002 (High)
- Additional efficacy/safety studies in FIV-infected cats beyond the single pilot PK/immunophenotype study
- Clarification of intended use context (veterinary vs. human), as this affects the applicable regulatory and safety pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

