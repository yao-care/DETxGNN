---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost: From Pulmonary Arterial Hypertension to PAH Associated with HIV Infection

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (PGI2) analog established for treatment of pulmonary arterial hypertension (PAH), acting via IP-receptor-mediated vasodilation and antiplatelet/antiproliferative effects.
The TxGNN model predicts it may be effective for **Pulmonary Arterial Hypertension Associated with HIV Infection**,
a specific etiological subtype of PAH, supported by **1 completed Phase 3 randomized controlled trial** and **4 supporting publications**.

> Note: This evidence pack scored 9 candidate indications for iloprost, most within the broader PAH disease family (congenital heart disease-PAH, connective tissue disease-PAH, HIV-PAH, schistosomiasis-PAH, hemolytic anemia-PAH) plus two unrelated hair-disorder predictions with no supporting evidence. Of these, the HIV-PAH indication carries by far the strongest evidence (L1, Phase 3 RCT) and is the subject of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a structured field in this evidence pack (data gap); mechanistically, iloprost is an established PGI2 analog used for pulmonary arterial hypertension (per repurposing rationale notes in the source data) |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with HIV Infection |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed original-indication and mechanism-of-action data are not available as structured fields (flagged as data gaps DG001/DG002 in this evidence pack). Based on the mechanistic notes embedded in the evidence pack, iloprost is a synthetic prostacyclin (PGI2) analog that activates the IP receptor, producing pulmonary vascular smooth-muscle relaxation, inhibition of platelet aggregation, and suppression of smooth-muscle proliferation — the core pharmacologic pathway underlying PAH treatment.

HIV-associated PAH shares the same downstream pathology (pulmonary vascular remodeling and endothelial dysfunction) as other PAH etiologies, even though the upstream trigger (HIV-related endothelial injury) differs. Because iloprost's therapeutic effect operates on the shared vascular remodeling pathway rather than on the disease-specific trigger, this represents an **on-class, label-adjacent expansion** rather than a mechanistically novel repurposing hypothesis — analogous to the established use of another prostacyclin analog, epoprostenol, in HIV-PAH.

This is further supported by the fact that a completed Phase 3, double-blind, randomized, placebo-controlled, crossover trial (PROWESS 15) explicitly enrolled HIV-associated PAH patients alongside idiopathic/familial PAH patients, indicating this population is already considered part of the standard iloprost/prostanoid treatment paradigm in clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Double-blind, randomized, placebo-controlled crossover study of single-dose inhaled Iloprost Power 15 on exercise capacity in symptomatic PAH patients, including those with HIV-associated PAH, NYHA class II–IV, either treatment-naive or on stable background bosentan/ambrisentan/sildenafil |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | The Mount Sinai Journal of Medicine | Overview of HIV-related pulmonary hypertension; estimated incidence ~0.5% of HIV-infected individuals, pathogenesis still unclear |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | American Journal of Respiratory Medicine | Reviews prostanoid therapy across PAH etiologies, including HIV infection, noting shared obstructive pulmonary microvascular pathology |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort (Registry) | Terapevticheskii Arkhiv | Six-year National Registry analysis of PAH prevalence, clinical course, therapy, and mortality |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Reviews controlled trials of prostacyclin and synthetic analogues across PAH subtypes including HIV infection |

---

## Germany Market Information

No marketing authorizations were found for iloprost in the current dataset (0 authorizations, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT directly enrolled HIV-associated PAH patients, and the mechanistic rationale is an on-class, label-adjacent extension of iloprost's established PGI2 pathway rather than a novel mechanism — this is the strongest-evidence candidate among the nine indications scored in this pack (L1/S3, versus L2–L5 for the others).

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: TFDA/BfArM package insert warnings and contraindications, required before any S1 safety assessment can proceed
- Resolve high-priority data gap DG002: formal DrugBank MOA confirmation
- Structured original-indication data (currently absent from the drug record)
- HIV-antiretroviral drug–drug interaction data, given this population's near-universal concomitant ART use
- A German market-entry/regulatory pathway assessment, since iloprost currently has zero marketing authorizations on file
- Subgroup-level efficacy/safety data specific to the HIV-PAH arm of NCT00709956, rather than the pooled PAH population result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

