---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
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

Using the drug-repurposing report template to produce this report directly from the evidence pack (no additional tool calls needed — all fields are present or explicitly marked as gaps).

---

# Tenofovir Alafenamide (TAF): From Antiretroviral Therapy to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Tenofovir alafenamide is a nucleotide reverse transcriptase inhibitor (NRTI) used to treat HIV-1 infection and chronic hepatitis B (based on the mechanism described in the model's own rationale text; no formal Taiwan label data is available).
> The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome** — a veterinary (cat) disease — with **zero clinical trials and zero literature** currently supporting it.
> A second candidate, **simian immunodeficiency virus (SIV) infection**, has 1 low-relevance trial and 9 preclinical macaque studies, but these substantiate TAF's *already-known* HIV pre-exposure prophylaxis (PrEP) mechanism rather than a genuinely new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan license data (0 licenses on file); based on the evidence pack's own rationale text, TAF is a known NRTI used for HIV-1 / chronic hepatitis B |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (rank 1) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature attached to this candidate) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap (DG002) in this pack. Based on the rationale text attached to the other two candidates in this same evidence pack, TAF is understood to act as an NRTI that inhibits retroviral (and HBV) reverse transcriptase/polymerase — this is standard, well-established pharmacology, not new information generated for this report.

The rank-1 prediction, **feline acquired immunodeficiency syndrome**, is caused by Feline Immunodeficiency Virus (FIV) — a lentivirus related to, but distinct from, HIV/SIV. A shared lentivirus family could plausibly explain why the knowledge graph linked TAF to this disease (reverse transcriptase inhibitors have shown some cross-lentivirus activity in vitro in the literature generally). However, **this evidence pack contains no clinical trials, no literature, and no completed scoring** (`decision_stage: pending`) for this candidate — the mechanistic plausibility above is inference, not evidence provided in this pack.

The better-documented candidate is rank 2, **SIV infection**: SIV and HIV-1 are both lentiviruses with highly homologous reverse transcriptase, and TAF/tenofovir diphosphate directly inhibits SIV RT — this is the actual non-human-primate model used during TAF's own HIV PrEP development program, reproduced across 9 independent macaque studies. The evidence pack's own rationale is explicit, though, that **SIV infection itself is not a human disease** and this evidence really substantiates TAF's *existing* HIV-PrEP indication rather than a new indication. Rank 3 (a rare monogenic neurodevelopmental disorder) is flagged directly in the pack as mechanistically implausible and possibly contradicted by TAF's known mitochondrial toxicity profile — it should be treated as noise, not a lead.

---

## Clinical Trial Evidence

**For the top-ranked prediction (feline acquired immunodeficiency syndrome):** Currently no related clinical trials registered.

*Supplementary context — trial linked to the rank-2 candidate (SIV infection), included for transparency but graded low-relevance:*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Studies vedolizumab + ART for HIV virological remission; TAF is not the study drug and this is a human HIV (not SIV) trial. Relevance grade **C** — flagged as a likely mis-linked trial. |

---

## Literature Evidence

**For the top-ranked prediction (feline acquired immunodeficiency syndrome):** Currently no related literature available.

*Supplementary context — preclinical literature linked to the rank-2 candidate (SIV infection); all are macaque/mouse animal-model studies (Tier 3), not human clinical data:*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (macaque) | Nature Communications | Oral FTC/TAF + long-acting cabotegravir/rilpivirine achieves SHIV remission in early-treated macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical (macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts give extended post-exposure protection against SHIV |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical (humanized mouse) | Frontiers in Immunology | Dual-purpose mouse model for testing antiviral strategies against SIV and HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Preclinical (macaque, device) | J Antimicrob Chemother | Biodegradable TAF-releasing implant protects macaques from vaginal SHIV |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical (macaque PrEP) | J Infect Dis | Oral TAF/FTC or TAF alone prevents vaginal SHIV infection in macaques |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Preclinical (methodology) | PLoS One | Protocol for daily oral ARV dosing compliance in macaque SIV/SHIV models |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical (macaque PrEP) | J Infect Dis | Oral FTC/TAF chemoprophylaxis protects macaques from rectal SHIV infection |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Preclinical (macaque) | J Infect Dis | Oral PrEP reduces inflammation/CD4 loss in breakthrough acute SHIV infection |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Preclinical (infant macaque) | J Acquir Immune Defic Syndr | Oral tenofovir DF / topical GS-7340 protect infant macaques from oral SIV challenge |

---

## Taiwan Market Information

Not marketed in Taiwan (`market_status: 未上市`, 0 authorizations on file). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this evidence pack — DDI query returned no results.)

**Note:** DG001 (TFDA label warnings/contraindications) is flagged as a **Blocking** data gap — its absence means this candidate cannot yet enter a formal S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline AIDS) has a high TxGNN score but zero supporting trials or literature and incomplete scoring (L5, model-prediction-only). The best-evidenced candidate (SIV infection) is explicitly an animal model reproducing TAF's *already-approved* HIV-PrEP mechanism rather than a new human indication, and its own rationale recommends Hold. The third candidate is flagged by the model's own reasoning as mechanistically implausible. In addition, a **Blocking** data gap (TFDA label unavailable) prevents formal safety pre-assessment, and TAF is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA label (warnings/contraindications) before any S1 safety review
- Resolve DG002: obtain DrugBank MOA data to properly assess mechanistic plausibility
- Request re-ranking/filtering from TxGNN to exclude non-human-disease ontology terms (e.g., feline/veterinary MONDO or animal-model-only entries) from the candidate list
- If SIV/PrEP-related repurposing is of interest, reframe the candidate as "TAF for human HIV PrEP" (an already-established indication) rather than "SIV infection" as a novel target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

