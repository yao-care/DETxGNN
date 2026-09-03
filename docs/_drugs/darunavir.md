---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 4
---

# Darunavir
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Darunavir is a second-generation HIV-1 protease inhibitor. The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, an animal-model indication supported by **0 clinical trials** and **4 publications** (all non-human primate studies). This is a research-tool application, not a human therapeutic indication, and no marketing authorization exists in Germany.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licensed indication text in dataset; darunavir is a known HIV-1 protease inhibitor for HIV-1 infection) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a Blocking/High-severity data gap). Based on known pharmacology, darunavir is a second-generation HIV-1 protease inhibitor that blocks viral polyprotein cleavage, preventing maturation of infectious virions.

SIV and HIV-1 are both lentiviruses with highly homologous protease structures. This structural similarity provides a plausible mechanistic rationale for darunavir's use in SIV-infected non-human primate (NHP) models — not as a novel human therapeutic, but as a component of combination antiretroviral therapy (cART) regimens used in HIV/AIDS cure research (viral reservoir studies, eradication strategies). This is consistent with darunavir's known pharmacology and explains why the model assigns it a high prediction score for this "indication."

It should be noted that three other TxGNN-predicted indications in this evidence pack were assessed as **not reasonable** and are held at S0/L4-L5 with a "Hold" recommendation:
- **Feline AIDS (FIV)**: likely a knowledge-graph entity confusion (FIV ≠ HIV); the only linked trial is actually a human HIV study, unrelated to cats.
- **Neurodevelopmental disorder (white matter/ataxic gait)**: no mechanistic link, no evidence — pure model artifact.
- **Familial combined hyperlipidemia**: mechanistically backwards — protease inhibitors are known to *cause* dyslipidemia, not treat it; the disease label itself is also obsolete.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Simian Immunodeficiency Virus Infection.

*(Note: one Phase 4 trial, [NCT02770508](https://clinicaltrials.gov/study/NCT02770508), was linked to the "feline AIDS" prediction but was assessed as irrelevant — it studies human HIV-1 patients, not cats, and is excluded from this indication's evidence base.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (NHP) | AIDS Research and Human Retroviruses | Evaluated coformulated injectable cART regimens (including darunavir components) in SIV-infected rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Study (NHP) | PLoS One | Combination cART plus SAHA (HDAC inhibitor) in SIV-infected Chinese rhesus macaques; viral reservoir research |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Study (NHP) | PLoS Pathogens | Highly intensified ART regimen achieved long-term viral suppression and reservoir restriction in simian AIDS model |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Study (NHP) | AIDS (London) | Auranofin combined with ART restricted viral reservoir in monkey AIDS model |

---

## Germany Market Information

Not marketed in Germany — no authorization records available (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All evidence for the SIV indication comes from non-human primate research-model studies (L3, no RCTs, no human clinical trials), and this is fundamentally a laboratory/animal-model tool use rather than a human therapeutic repurposing candidate. Combined with the absence of German market authorization and unresolved Blocking-severity safety data gaps (TFDA label/warnings, MOA), the candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety evaluation
- Resolve DG002 (High): confirm mechanism of action via DrugBank API
- Clarify intended use case — this is an NHP research-model application, not a human indication; confirm whether "repurposing" scope should even include animal-model/research-tool uses
- If human application is intended, source primary human clinical evidence (none currently exists for SIV, which by definition does not infect humans)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

