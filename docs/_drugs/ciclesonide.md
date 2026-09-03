---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

> Ciclesonide is an inhaled corticosteroid (ICS) prodrug, best known as the active ingredient in **Alvesco** for asthma control.
> The TxGNN model predicts it may be effective for **Atopic Eczema**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — a prediction based purely on the knowledge graph, with no empirical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (inhaled corticosteroid; confirmed only via the drug's own known ICS classification, not a formal regulatory record) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for ciclesonide is not available from the regulatory data source used to build this evidence pack (data gap). However, the evidence pack's own repurposing rationale for a related candidate confirms that ciclesonide is an inhaled corticosteroid (ICS) prodrug, activated by pulmonary esterases into its active metabolite des-ciclesonide, which binds the glucocorticoid receptor and suppresses airway inflammation. This is ciclesonide's well-established, already-approved mode of action for asthma (e.g., Alvesco) — not a new use.

Atopic eczema and asthma both belong to the atopic/Th2-driven inflammatory disease spectrum, and topical corticosteroids are indeed a mainstay of eczema treatment, so a glucocorticoid mechanism is not inherently implausible for skin inflammation. This gives the prediction a superficial theoretical basis.

However, the practical case is weak: ciclesonide is currently formulated only for inhalation, with no pharmacokinetic or safety data for cutaneous/topical administration. The evidence pack itself explicitly flags this mechanistic link as "weak" (機轉關聯薄弱) due to the route-of-administration mismatch. Without a topical formulation and dermatologic PK/safety package, this prediction cannot be translated into a testable clinical hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Ciclesonide is **not currently marketed in Taiwan** — no product authorizations are on record (0 licenses). No approved indication text, dosage form, or authorization number data is available for this drug in this market.

---

## Safety Considerations

Please refer to the package insert for safety information (no structured warnings, contraindications, or DDI data are available for this drug in the current dataset, and it is not marketed in Taiwan).

**Notable safety signal from literature (not specific to the eczema prediction):** A case report (PMID [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/), *Contact Dermatitis*, 2012) describes systemic allergic dermatitis caused by inhaled **budesonide**, with patch testing showing **cross-reactivity to ciclesonide** as a structurally related ICS. This is an adverse-reaction signal, not evidence of therapeutic benefit, and should be treated as a caution flag — particularly relevant given any future dermatologic repurposing exploration for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The atopic eczema prediction is supported only by a TxGNN model score (L5), with zero clinical trials and zero publications, and the drug currently has no topical/dermatologic formulation or route-compatible safety data — the mechanistic link is explicitly assessed as weak even within the evidence pack itself.

**To proceed, the following is needed:**
- Formal TFDA/manufacturer labeling data (warnings, contraindications, DDI) — currently a blocking data gap
- Confirmed original indication and MOA sourced directly from DrugBank/regulatory filings (currently inferred only from secondary rationale text)
- Feasibility assessment and PK/safety data for a topical/dermatologic formulation of ciclesonide, since no cutaneous route currently exists
- At minimum, preclinical or early-phase dermatologic efficacy data before this candidate can move beyond S0

**For context:** two other candidates in this evidence pack carry stronger, actionable signals and may warrant separate tracking — *bronchitis* (L4, decision stage S1, literature support via COPD guideline) and *asthma-related traits susceptibility* (L1, decision stage S3), the latter of which essentially reflects ciclesonide's already-approved asthma indication rather than a genuine new use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

