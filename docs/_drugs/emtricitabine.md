---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI), originally developed for HIV-1 infection as part of combination antiretroviral regimens (e.g. Truvada, Atripla). The TxGNN model's top prediction points to **feline acquired immunodeficiency syndrome (FIV)** — a veterinary, not human, disease — but the supporting evidence consists of **4 clinical trials** (all in human HIV-1 patients, mostly using drugs other than emtricitabine) and **1 publication** (a small cohort study directly testing emtricitabine-containing therapy in FIV-infected cats). The evidence is therefore preclinical/mechanistic in strength, not clinical.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (antiretroviral combination therapy) — no BfArM/German license record exists in this dataset; inferred from the combination regimens (Atripla, Truvada) referenced in the trial evidence |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for emtricitabine in this evidence pack (flagged as a High-severity data gap). Based on what is known, emtricitabine is a cytidine-analogue NRTI and a core component of fixed-dose combination antiretroviral regimens (e.g. Truvada [with tenofovir], Atripla [with efavirenz + tenofovir]), where it blocks HIV-1 reverse transcriptase and halts viral DNA synthesis. Its efficacy in HIV-1 infection is well established through numerous completed Phase 3 trials.

The mechanistic rationale for extending this to FIV is that Feline Immunodeficiency Virus, like HIV, is a lentivirus that depends on reverse transcriptase for replication, and the two enzymes are structurally conserved across species. In principle, an NRTI effective against HIV reverse transcriptase could inhibit FIV reverse transcriptase as well.

However, this prediction needs to be read with an important caveat: **three of the four clinical trials returned as "evidence" do not involve emtricitabine at all** (they test dolutegravir, darunavir, or raltegravir combinations) and **all four are human HIV-1 trials, not feline studies** — the evidence pack itself flags this as a likely knowledge-graph ontology mismatch, where trials matched on the generic term "immunodeficiency" rather than true relevance to FIV. The one genuinely relevant data point is a 2023 cohort study that directly evaluated a combination antiretroviral regimen containing emtricitabine in FIV-infected domestic cats — a real but small, non-clinical (veterinary pharmacokinetic/outcome) study. For context, a closely related TxGNN prediction in this same evidence pack (rank 2, Simian Immunodeficiency Virus infection) is supported by substantially stronger translational evidence — 20 publications, many of them macaque challenge studies directly dosing emtricitabine — and carries a higher evidence grade (L3, Proceed with Guardrails), though SIV itself is a primate research model rather than a licensed human indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla (efavirenz/emtricitabine/tenofovir) in ART-naive HIV-1 adults. Human trial; graded low relevance (C) — not an FIV study, drug not the primary comparator. |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in naive HIV-1 patients. Human trial; graded low relevance (C). |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. raltegravir, both with dual NRTI backbone (ABC/3TC or TDF/FTC), in ART-naive HIV-1 adults. Human trial; graded low relevance (C) — primary comparator not emtricitabine. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of dolutegravir with abacavir/lamivudine or tenofovir/emtricitabine in ART-naive HIV-1 adults. Human trial; graded low relevance (C). |

**Note:** All four trials are graded "C" (low relevance) — they are human HIV-1 studies, not FIV studies, and in most cases emtricitabine is not the drug under primary investigation.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Cohort (animal immunophenotyping) | Viruses | Evaluated combination antiretroviral therapy (dolutegravir 2.5 mg/kg, tenofovir 20 mg/kg, emtricitabine 40 mg/kg) in FIV-infected domestic cats — the only evidence item directly testing emtricitabine in the predicted feline indication. |

---

## Germany Market Information

Emtricitabine currently has **no BfArM market authorization on record** in this dataset (0 licenses, market status: Not Marketed). It may exist only as part of fixed-dose combination products (e.g. Truvada, Atripla) not captured under this drug entity in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/BfArM warnings, contraindications, and drug-interaction data could not be retrieved for this drug — retrieval of the official package insert is flagged as a **blocking** data gap that must be resolved before any Stage-1 safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (FIV) rests on a single small animal cohort study and four clinical trials that are, on inspection, human HIV-1 studies largely unrelated to emtricitabine or to the feline indication — consistent with the evidence pack's own assessment that this match likely reflects a knowledge-graph ontology overlap ("immunodeficiency") rather than genuine translational evidence. Combined with the unresolved blocking gap on TFDA/BfArM safety labeling, there is not enough evidence to proceed past S0.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — currently a blocking data gap
- Confirmed DrugBank mechanism-of-action detail for emtricitabine
- Additional preclinical or clinical data evaluating emtricitabine specifically (not other NRTIs) in FIV-infected cats
- Consideration of the related rank-2 prediction (Simian Immunodeficiency Virus infection), which is supported by substantially more literature (20 publications, including direct macaque dosing studies) and a higher evidence grade (L3), as a potentially more defensible research direction — while noting SIV itself is an animal research model, not a licensed human indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

