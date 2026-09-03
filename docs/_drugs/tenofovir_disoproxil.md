---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tenofovir Disoproxil: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor (NRTI) prodrug originally developed for the treatment of HIV-1 infection and chronic hepatitis B.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **2 clinical trials** and **~20 publications** currently associated with this direction — however, the underlying evidence is almost entirely preclinical macaque pre-exposure prophylaxis (PrEP) research rather than treatment of SIV disease itself, and the two clinical trials identified are graded as low relevance (Grade C).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap); clinically known to be HIV-1 infection / chronic hepatitis B |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 (per evidence pack scoring; underlying studies are largely preclinical animal models — see caveat below) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tenofovir disoproxil in this evidence pack (data gap DG002). Based on known pharmacology, tenofovir disoproxil is a prodrug of tenofovir, an acyclic nucleotide analog that inhibits the reverse transcriptase enzyme shared across lentiviruses. This enzyme is highly conserved between HIV and SIV, which is the biological basis for the TxGNN association.

However, a close reading of the supporting evidence reveals an important mismatch: nearly all literature and trial evidence retrieved for "SIV infection" actually documents tenofovir's use as **pre-exposure prophylaxis (PrEP) against HIV/SHIV transmission in macaque models**, not treatment of an established SIV infection as a disease entity. In other words, the real-world therapeutic application this evidence supports (HIV PrEP) is **already an approved use of tenofovir disoproxil-based regimens**, not a genuinely novel indication. This label/evidence mismatch is explicitly flagged in the repurposing rationale and should be treated as a data-mapping artifact rather than a new repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Studied raltegravir (not tenofovir) HIV decay kinetics referencing SIV-macaque comparators; **Grade C relevance** — withdrawn, zero enrollment, wrong drug |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + ART for HIV virological remission; **Grade C relevance** — tenofovir not the primary intervention, unknown status, very small sample |

Both identified trials were assessed as low relevance to the SIV infection indication specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT | Pharmacotherapy | Systemic pre-exposure prophylaxis for HIV infection — foundational PrEP evidence base |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Review | J Virol | SIVagm dynamics in African green monkeys treated with tenofovir + emtricitabine ART |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Cohort (macaque) | J Infect Dis | TAF + FTC protects macaques from rectal SHIV infection (PrEP model) |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Cohort (macaque) | JCI Insight | Hypo-osmolar rectal tenofovir douche prevents SHIV acquisition |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Cohort (macaque) | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 protect infant macaques against oral SIV challenge |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Cohort (macaque) | J Infect Dis | TDF chemoprophylaxis gives partial protection against SHIV with multiple challenges |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Cohort (macaque) | J Virol | Vaginal 1% tenofovir gel provides durable protection from SHIV infection |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Cohort (macaque) | J Infect Dis | FTC/TDF prevents vaginal SHIV infection even with concurrent STIs |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Cohort (macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts give extended postexposure SHIV protection |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Cohort (macaque) | J Infect Dis | FTC/TDF prevents transmission of tenofovir-resistant (K65R) SHIV |

**Note:** All except the two entries above are animal-model PrEP/prophylaxis studies, not treatment studies of established SIV disease.

---

## Germany Market Information

Tenofovir disoproxil is currently **not marketed** under this dataset (`total_licenses = 0`), so no authorization records are available to list.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) is currently unavailable in this evidence pack. This is tracked internally as data gap **DG001 (Blocking severity)** — the absence of TFDA/regulatory label information (warnings and contraindications) prevents this candidate from progressing to Stage 1 (S1) safety review. This gap must be closed via TFDA/EMA label retrieval before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication label ("SIV infection") does not match the substance of its supporting evidence, which almost entirely documents tenofovir's established HIV PrEP mechanism in animal models rather than a genuinely novel therapeutic application. Combined with a Blocking-severity safety data gap (DG001) and the drug's current unmarketed status, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/EMA package insert data (warnings, contraindications) to enable S1 safety review
- Resolve DG002: confirm mechanism of action via DrugBank to properly assess mechanistic plausibility
- Clarify with the modeling/evidence pipeline whether "SIV infection" should be re-mapped to the already-approved human HIV PrEP indication, since current evidence does not support it as a distinct new indication
- Note: lower-ranked predictions (feline AIDS — veterinary-only evidence; two neurological/metabolic disease predictions with zero supporting evidence, L5) should remain on **Hold** and are not recommended for further evaluation at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

