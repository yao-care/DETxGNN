---
layout: default
title: Cholic Acid
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Cholic Acid
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

# Cholic Acid: From Bile Acid Physiology to Predicted HIV Infectious Disease

## One-Sentence Summary

> Cholic acid is a naturally occurring primary bile acid; this evidence pack does not document a formally established original indication, though cholic acid is known outside this dataset for bile acid replacement therapy.
> The TxGNN model's top-ranked prediction is **HIV infectious disease**, but the supporting evidence is weak and partially **contradictory** — the associated literature describes spermicidal/virucidal use in contraceptive sponges and blood-product viral inactivation, and one study reports that cholic acid derivatives actually *enhance* HIV-1 replication.
> With **0 clinical trials** and **9 publications**, none of which demonstrate an antiretroviral therapeutic effect, the evidence does not currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (`original_indications` is empty; cholic acid is generally known as a natural primary bile acid used in bile acid replacement therapy, but this is not captured in the evidence pack) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for cholic acid in this evidence pack (marked as a Blocking-priority data gap, DG002). Without MOA data, there is no pharmacological basis provided in this pack to link cholic acid to antiretroviral activity.

The literature retrieved for this prediction does not describe a mechanism consistent with treating HIV infection. Most papers concern the use of sodium cholate as a **spermicidal/virucidal agent in vaginal contraceptive sponges** (e.g., Protectaid) or as an agent for **viral inactivation of blood products** (tri-n-butyl phosphate/sodium cholate treatment of plasma-derived factor concentrates) — these are barrier/disinfection contexts, not systemic antiretroviral therapy. More concerning, one study (PMID 16610808) found that amino-functionalized cholic acid derivatives **induced HIV-1 replication and syncytia formation** in T cells, i.e., the opposite of a therapeutic effect.

Given the absence of MOA data, the absence of any clinical trial, and the presence of a directly contradictory in-vitro finding, this specific TxGNN-predicted association currently lacks mechanistic plausibility and should not be advanced without independent confirmatory pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | Clinical/microbicide study | Human Reproduction | Sodium cholate (in the Protectaid sponge, F-5 Gel) shows dose-dependent in-vitro spermicidal and anti-HIV-1 reverse transcriptase inhibitory activity; a barrier-contraceptive/microbicide effect, not systemic antiviral therapy |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | In vitro virucidal study | Lancet | Tri(n-butyl)phosphate/sodium cholate treatment inactivates HBV and HTLV-III (HIV precursor virus) in blood-product manufacturing; a viral-inactivation/disinfection process, not a therapeutic mechanism |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro (contradictory finding) | Journal of Medicinal Chemistry | Amino-functionalized cholic acid derivatives **induced** HIV-1 replication and syncytia formation in T cells — directly contradicts the hypothesis that cholic acid is protective against HIV |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Review | Hepatology | Discusses NASH drug development in people living with HIV; bile acids are mentioned only in the context of drug-drug interaction concerns with antiretrovirals, not as HIV therapy |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Contraceptive device study | Ann NY Acad Sci | Discusses anti-STD vaginal contraceptive sponges containing cholic acid derivatives as a barrier method |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust NZ J Obstet Gynaecol | General review of future contraceptive methods offering STD/HIV protection; cholic acid not specifically evaluated as antiretroviral |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | Reviews barrier contraception methods (condoms, spermicides) for STD/HIV prevention |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Observational study | Pharmacotherapy | Evaluates plasma bile acid concentrations in HIV patients on protease inhibitors as a marker for hepatotoxicity risk — an association/monitoring study, not a treatment study |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | In vitro methodology | ChemMedChem | Methodological paper on detergent assay artifacts affecting HIV-1 protease inhibitor binding assays; not related to cholic acid's therapeutic effect |

---

## Germany Market Information

Currently no marketing authorizations recorded for cholic acid in Germany (`total_licenses: 0`, `market_status: 未上市`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings`, `contraindications`, and `ddi` are all marked as data gaps in this pack; TFDA label warnings/contraindications are flagged as a Blocking data gap (DG001) that must be resolved before any S1 safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support cholic acid for HIV infectious disease, the mechanism of action is undocumented (Blocking data gap), and one in-vitro study directly contradicts the predicted therapeutic direction. Evidence level is L5 — model prediction only, without supportive actual studies.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/BfArM label warnings and contraindications) — currently blocking any S1 safety assessment
- Resolve DG002 (mechanism of action data via DrugBank) — needed for mechanistic plausibility review
- Independent pharmacological studies clarifying why the TxGNN model links cholic acid to HIV infectious disease, given the contradictory in-vitro signal (PMID 16610808)
- Consider re-evaluating lower-ranked candidates in this pack (e.g., "vitamin deficiency disorder," rank 5) which show stronger, mechanistically coherent evidence (an active Cholbam patient registry, NCT03115086, and multiple case series on bile acid synthesis disorders) more consistent with cholic acid's known biology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

