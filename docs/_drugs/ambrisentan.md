---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Idiopathic Pulmonary Arterial Hypertension to Connective Tissue Disease-Associated Pulmonary Arterial Hypertension

## One-Sentence Summary

Ambrisentan is a selective endothelin type A (ETA) receptor antagonist originally developed for idiopathic/heritable pulmonary arterial hypertension (PAH). The TxGNN model — together with corroborating clinical and literature evidence — predicts it may also be effective for **Pulmonary Arterial Hypertension Associated with Connective Tissue Disease (CTD-PAH)**, with **3 clinical trials** (including the pivotal AMBITION combination-therapy program) and **20 publications**, including a systematic review and meta-analysis, currently supporting this direction.

> **Note on indication selection:** This Evidence Pack contains 10 TxGNN-predicted indications for ambrisentan. The single highest-scoring prediction by raw TxGNN score (`pulmonary arteriovenous malformation`, 99.41%) is supported by only one case report and is scored **L4/Hold** by the pipeline's own evidence engine. This report instead focuses on **CTD-PAH**, which carries the strongest, most clinically actionable evidence body among the ten candidates (**L1, decision stage S3, "Proceed with Guardrails"**). A full screening summary of all 10 candidates is provided at the end of this report for transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic / Heritable Pulmonary Arterial Hypertension (WHO Group 1 PAH) — inferred from cross-referenced literature and mechanistic rationale, since Germany license records returned zero entries |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Connective Tissue Disease (CTD-PAH) |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data was not returned by the DrugBank query (flagged as a High-severity data gap). However, the mechanistic rationale is consistently documented across the Evidence Pack's repurposing analyses: **Ambrisentan is a selective endothelin type A (ETA) receptor antagonist**. By blocking endothelin-1-mediated vasoconstriction and vascular smooth muscle proliferation, it reduces pulmonary vascular resistance and reverses pathological pulmonary vascular remodeling — the shared final pathway of all WHO Group 1 PAH subtypes.

Connective tissue disease-associated PAH (most commonly seen in systemic sclerosis/scleroderma, and also lupus and mixed connective tissue disease) is classified as WHO Group 1.4.1 — a molecularly indistinguishable process from idiopathic PAH, differing only in the upstream autoimmune trigger that initiates endothelial injury and endothelin-1 overexpression. Because the terminal vascular pathology and drug target are identical, ETA-receptor blockade is mechanistically as applicable in CTD-PAH as in idiopathic PAH.

This mechanistic plausibility is strongly reinforced by real clinical precedent already present in the literature: a 2017 review (PMID 28425346) explicitly states that ambrisentan is "approved for the treatment of idiopathic, heritable PAH **and connective tissue disease-associated PAH**." Multiple post-hoc/subgroup analyses of the AMBITION trial — ambrisentan's own pivotal registration study, combined with tadalafil — specifically evaluated the CTD-PAH subpopulation and reported meaningful benefit, further supporting that the TxGNN prediction reflects an indication already partially validated in real-world regulatory and clinical practice elsewhere, rather than a purely speculative extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | Open-label study of ambrisentan + tadalafil combination therapy in PAH associated with systemic sclerosis spectrum disease (PAH-SSD); assessed 6MWD, NYHA class, and hemodynamics. |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA proof-of-concept RCT: early ambrisentan treatment in borderline/early elevated pulmonary artery pressure associated with systemic sclerosis. |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | Phase 4 | Terminated (n=3) | 3 | Switch study from bosentan/macitentan to ambrisentan in CTD-PAH; terminated early due to low enrollment, safety-observation value only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review & Meta-analysis | Internal and Emergency Medicine | Pooled RCT evidence for CTD-PAH treatment outcomes (functional class, survival, 6MWD, NT-proBNP). |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials establishing efficacy signal for PAH-targeted therapy, including ambrisentan, in CTD-PAH. |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | RCT (AMBITION subgroup) | American Journal of Respiratory and Critical Care Medicine | Up-front ambrisentan + tadalafil combination therapy in scleroderma-associated PAH (SSc-PAH). |
| [31655622](https://pubmed.ncbi.nlm.nih.gov/31655622/) | 2019 | RCT (EDITA study) | Arthritis Research & Therapy | Randomized, double-blind, placebo-controlled trial of early ambrisentan in mildly elevated mPAP associated with systemic sclerosis. |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Cohort (AMBITION post-hoc) | Annals of the Rheumatic Diseases | Post-hoc analysis of initial ambrisentan + tadalafil combination therapy in CTD-PAH within the AMBITION modified ITT population. |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Cohort (AMBITION subgroup) | Annals of the Rheumatic Diseases | Subgroup analysis of AMBITION trial confirming benefit of initial combination therapy in CTD-PAH, including systemic sclerosis. |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Cohort (ARIES-E subgroup) | Respiratory Medicine | 3-year efficacy and safety of ambrisentan specifically in CTD-PAH patients from the ARIES-E extension study. |
| [29282676](https://pubmed.ncbi.nlm.nih.gov/29282676/) | 2018 | Post-marketing Surveillance | Clinical Drug Investigation | Real-world safety and efficacy surveillance of ambrisentan (Volibris) in 702 PAH patients, including CTD-associated cases. |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Therapeutic Advances in Respiratory Disease | States ambrisentan is approved for idiopathic/heritable PAH and CTD-PAH; summarizes efficacy on exercise capacity and hemodynamics. |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of PAH associated with connective tissue disease, contextualizing ERA therapy including ambrisentan. |

---

## Germany Market Information

No marketing authorizations are currently on record — ambrisentan is **not marketed** in this jurisdiction per the available regulatory data (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack's German regulatory warnings/contraindications and drug-drug interaction (DDI) database queries did not return usable data (DDI query status: *not found*; package insert data flagged as a **Blocking** data gap, DG001), so no drug-specific warnings can be cited here beyond the general PAH-therapy class considerations (e.g., hepatic monitoring, teratogenicity, fluid retention typical of endothelin receptor antagonists) — none of which are sourced from this Evidence Pack and should not be treated as a substitute for the official label.

---

## Other TxGNN-Predicted Indications (Screening Summary)

For transparency, given this Evidence Pack evaluated 10 candidate indications for ambrisentan, the table below summarizes how each was scored so the choice of CTD-PAH as the lead indication in this report can be cross-checked:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Pulmonary arteriovenous malformation | 99.41% | L4 | Hold — mechanistically distinct (structural shunt vs. endothelin-driven vasculopathy); only 1 case report |
| 2 | PAH associated with congenital heart disease | 99.37% | L1 | Proceed with Guardrails — 9 trials incl. a completed Phase 3b (134 pts); strong mechanistic overlap (WHO Group 1.4.4) |
| 3 | PAH associated with schistosomiasis | 99.30% | L5 | Hold — no trials or literature; pure mechanistic extrapolation |
| 4 | PAH associated with HIV infection | 99.30% | L1 | Proceed with Guardrails — 1 completed Phase 3 RCT (64 pts) + 4 supporting papers; requires antiretroviral DDI guardrails |
| **5** | **PAH associated with connective tissue disease (this report)** | **99.30%** | **L1** | **Proceed with Guardrails — strongest evidence body (AMBITION subgroup, meta-analysis, systematic review); precedent of approval elsewhere** |
| 6 | PAH associated with chronic hemolytic anemia | 99.30% | L5 | Hold — no trials or literature; theoretical mechanistic link only |
| 7 | Malformation syndrome with odontal/periodontal component | 99.19% | L5 | Hold — retrieved literature is unrelated periodontitis research; likely embedding-similarity false positive |
| 8 | Hypotrichosis simplex of the scalp | 99.15% | L5 | Hold — no mechanistic basis, no evidence; model noise |
| 9 | Hypertrichosis | 99.14% | L5 | Hold — no mechanistic basis (ETA antagonism ≠ minoxidil-type mechanism); model noise |
| 10 | Syndrome with Dandy-Walker malformation as major feature | 99.12% | L5 | Hold — no mechanistic basis; likely keyword ("malformation") similarity artifact |

This confirms that ambrisentan's genuinely repurposable candidates cluster tightly around **other PAH etiological subtypes** (ranks 2, 4, 5), consistent with its known ETA-antagonist mechanism, while the remaining candidates are either single-case anecdotal signals or apparent embedding-similarity noise unrelated to the drug's pharmacology.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CTD-PAH is supported by L1-level evidence — including subgroup analyses from ambrisentan's own pivotal AMBITION trial, a dedicated meta-analysis, and a systematic review — and the mechanism (ETA-receptor antagonism against endothelin-driven vascular remodeling) is pathophysiologically identical to the drug's original PAH indication. Literature further indicates ambrisentan is already approved for CTD-PAH in other markets. However, the drug currently has zero marketing authorizations in this jurisdiction and critical safety documentation (package insert warnings/contraindications, DDI data) is missing, which prevents this from being a clean "Go."

**To proceed, the following is needed:**
- Obtain the official German/local package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Formally resolve the detailed mechanism-of-action documentation via DrugBank API rather than relying on inferred rationale text (High-severity gap, DG002)
- Conduct a dedicated DDI database review, since the current query returned no results
- Clarify local regulatory pathway/status, given the drug is currently unlicensed and unmarketed here (0 authorizations)
- Consider parallel evaluation of PAH-associated congenital heart disease and PAH-associated HIV infection (ranks 2 and 4), which also scored L1/"Proceed with Guardrails" and may support a broader repurposing label strategy across PAH subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

