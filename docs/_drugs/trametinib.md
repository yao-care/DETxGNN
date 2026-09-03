---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From BRAF V600-Mutant Melanoma to Additional Melanoma Subtypes

## One-Sentence Summary

> Trametinib is a MEK1/2 inhibitor whose established use — evident throughout the clinical trial record in this evidence pack — is combination therapy with dabrafenib for BRAF V600 mutation-positive melanoma. TxGNN additionally flags several histological and anatomical melanoma subtypes (nodular, superficial spreading, non-cutaneous/mucosal-ocular) as candidates for the same mechanism, each supported to varying degrees by completed Phase 2/3 trials and case-level literature, while a subset of predictions (choroideremia, scrotal melanoma, CDK4-linked melanoma, balloon cell melanoma) have no clinical or mechanistic support at all. This is a **multi-indication candidate pack (10 predictions, evidence levels L1–L5)**, so each candidate below is assessed independently rather than as a single go/no-go decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan/Germany regulatory data (0 licenses on file). Based on clinical trial descriptions in this pack, trametinib's established use is combination therapy with dabrafenib for **BRAF V600E/K mutation-positive melanoma** (unresectable/metastatic and adjuvant settings) |
| Best-Supported New Indications | **Superficial spreading melanoma** and **Nodular malignant melanoma** (histological subtypes of cutaneous melanoma) |
| TxGNN Prediction Score (top pick) | 99.14% (both indications, tied) |
| Evidence Level | L2 (1 completed Phase 2 trial + supporting cohort/case literature) |
| Germany Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Proceed with Guardrails** (for melanoma-subtype extensions, conditional on BRAF V600 testing) — see full ranking below for other candidates |

### Full Predicted-Indication Ranking

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-----------|-----------|-----------|
| 1 | Choroideremia | 99.31% | L5 | Hold |
| 2 | Non-cutaneous melanoma | 99.30% | L1 | Research Question |
| 3 | Epithelioid cell melanoma | 99.28% | L4 | Research Question |
| 4 | Eyelid melanoma | 99.26% | L4 | Research Question |
| 5 | Scrotum melanoma | 99.21% | L5 | Hold |
| 6 | Nodular malignant melanoma | 99.14% | L2 | **Proceed with Guardrails** |
| 7 | Balloon cell malignant melanoma | 99.14% | L5 | Hold |
| 8 | Superficial spreading melanoma | 99.14% | L2 | **Proceed with Guardrails** |
| 9 | CDK4-linked melanoma | 99.14% | L5 | Hold |
| 10 | Amelanotic skin melanoma | 99.14% | L4 | Research Question |

*Note: Evidence level here does not track monotonically with TxGNN score — a high similarity score reflects embedding proximity in the knowledge graph, not clinical support. Rank 2 is labeled L1 in the source scoring but downgraded to "Research Question" because its listed trials are cutaneous-melanoma registration trials applied indirectly to a non-cutaneous population, not disease-specific RCTs.*

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this evidence pack (data gap DG002). However, every clinical trial record in the pack consistently describes trametinib as an oral **MEK1/2 inhibitor**, used in combination with the BRAF inhibitor dabrafenib to block the MAPK/ERK signaling cascade downstream of BRAF V600 mutations. This combination is the backbone of the pivotal registration trials present here (e.g., NCT01245062, NCT01584648, NCT01597908), which established efficacy in BRAF V600E/K-mutant unresectable or metastatic **cutaneous** melanoma.

The predictions in ranks 6 and 8 (nodular and superficial spreading melanoma) are histological *subtypes* of cutaneous melanoma rather than distinct diseases — they share the same BRAF V600 mutation biology as the already-treated population, so the mechanistic extrapolation is close to direct rather than novel. Rank 2 (non-cutaneous melanoma) and the ocular/mucosal predictions (ranks 3, 4, 10) are biologically more distant: BRAF V600 mutation prevalence in conjunctival, eyelid, and mucosal melanoma is substantially lower than in cutaneous melanoma, so response is plausible only in the BRAF-mutant-positive subset, as illustrated by isolated case reports of conjunctival melanoma responding to BRAF/MEK inhibition (PMID 27893585, 31361915).

Conversely, choroideremia (rank 1), scrotal melanoma (rank 5), balloon cell melanoma (rank 7), and CDK4-linked melanoma (rank 9) have no clinical trials, no literature, and no plausible mechanistic link to MEK inhibition (choroideremia is a CHM/REP1 retinal degeneration unrelated to MAPK signaling; CDK4-driven melanoma acts through cell-cycle rather than MAPK pathways). These should be treated as pure knowledge-graph artifacts.

---

## Clinical Trial Evidence

Trials below form the core evidence base underpinning trametinib's BRAF/MEK mechanism; they support the melanoma-subtype extensions (non-cutaneous, nodular, superficial spreading) as background mechanistic evidence rather than subtype-specific confirmatory trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01245062](https://clinicaltrials.gov/study/NCT01245062) | Phase 3 | Completed | 322 | Pivotal trial: trametinib monotherapy vs. chemotherapy in BRAF V600E/K-positive cutaneous melanoma |
| [NCT01584648](https://clinicaltrials.gov/study/NCT01584648) | Phase 3 | Completed | 423 | COMBI-d: dabrafenib+trametinib vs. dabrafenib alone, unresectable/metastatic BRAF V600E/K cutaneous melanoma |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Phase 3 | Completed | 704 | COMBI-v: dabrafenib+trametinib vs. vemurafenib, BRAF V600E/K cutaneous melanoma |
| [NCT03551626](https://clinicaltrials.gov/study/NCT03551626) | Phase 3b | Completed | 552 | COMBI-APlus: adjuvant dabrafenib+trametinib after complete resection, Stage III BRAF V600 melanoma; pyrexia AE-management algorithm |
| [NCT01072175](https://clinicaltrials.gov/study/NCT01072175) | Phase 1/2 | Completed | 430 | Original dose-escalation/combination trial of dabrafenib+trametinib in BRAF-mutant metastatic melanoma |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Phase 2 | Completed | 127 | Dabrafenib+trametinib in BRAF-mutant melanoma with brain metastases (4 mutation cohorts) |
| [NCT02645149](https://clinicaltrials.gov/study/NCT02645149) | Phase 2 | Completed | 216 | Molecular profiling with matched targeted therapy in BRAF/NRAS wild-type unresectable/metastatic melanoma progressing on immunotherapy |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | Triplet nivolumab+dabrafenib+trametinib (TRIDeNT) vs. encorafenib+binimetinib+nivolumab (TRIBECA), BRAF-mutant Stage III-IV melanoma |
| [NCT05171374](https://clinicaltrials.gov/study/NCT05171374) | N/A | Unknown | 500 | Prospective real-world outcomes of dabrafenib+trametinib in resectable/metastatic BRAF+ melanoma |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Phase 4 | Recruiting | 100 | Long-term safety roll-over study for patients continuing dabrafenib/trametinib after parent-study completion |

*No trials in this pack specifically enroll patients with choroideremia, scrotal melanoma, balloon cell melanoma, or CDK4-linked melanoma.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Review | JAMA | Overview of cutaneous melanoma epidemiology and treatment landscape, including BRAF/MEK-targeted therapy |
| [30376465](https://pubmed.ncbi.nlm.nih.gov/30376465/) | 2019 | Cohort | Melanoma Research | Multicenter real-life study of BRAF/MEK inhibitor combination in melanoma patients with active brain metastases (n=65) |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case Report/Review | Clin Exp Dermatol | BRAF-mutated bulbar conjunctival (epithelioid) melanoma treated with vemurafenib; literature review |
| [27893585](https://pubmed.ncbi.nlm.nih.gov/27893585/) | 2017 | Case Report | Ophthalmic Plast Reconstr Surg | Conjunctival melanoma with BRAF V600E responsive to systemic BRAF/MEK inhibitor combination |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case Report/Review | J Investig Med High Impact Case Rep | Lacrimal sac malignant melanoma (epithelioid type); review of 15 Japanese cases |
| [41310270](https://pubmed.ncbi.nlm.nih.gov/41310270/) | 2025 | Case Report | Child's Nervous System | Pediatric amelanotic CNS melanoma with systemic spread, associated with congenital melanocytic naevi |
| [41209431](https://pubmed.ncbi.nlm.nih.gov/41209431/) | 2026 | Case Report | Oncology Letters | Combined BRAF/MEK inhibition for BRAF-mutant brain metastases from superficial spreading melanoma during pregnancy |
| [37756677](https://pubmed.ncbi.nlm.nih.gov/37756677/) | 2025 | Case Report | Retinal Cases & Brief Reports | Rapid resolution of choroidal metastasis from cutaneous melanoma after combined targeted therapy |
| [24879511](https://pubmed.ncbi.nlm.nih.gov/24879511/) | 2014 | Case Series (safety) | Am J Dermatopathol | Panniculitis as an adverse effect of BRAF/MEK inhibitor therapy (dabrafenib, dabrafenib+trametinib) |
| [32614358](https://pubmed.ncbi.nlm.nih.gov/32614358/) | 2020 | Case Report | La Clinica Terapeutica | PET-guided switch from immunotherapy to BRAF/MEK targeted therapy in nodular melanoma with cutaneous/skeletal metastases |

*No literature was returned for choroideremia, scrotal melanoma, balloon cell melanoma, or CDK4-linked melanoma.*

---

## Germany Market Information

Trametinib is currently **not marketed** in Germany under this evidence pack's regulatory data source (market status: 未上市, 0 authorizations on file). No license table can be produced.

---

## Cytotoxicity

Trametinib is an antineoplastic agent (all trial populations in this pack are oncology/melanoma patients), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA/BfArM warning, contraindication, and drug-interaction data are not available in this evidence pack — flagged as a blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the melanoma-subtype extensions: nodular melanoma, superficial spreading melanoma, non-cutaneous melanoma) / **Hold** (for choroideremia, scrotal melanoma, balloon cell melanoma, CDK4-linked melanoma) / **Research Question** (for epithelioid cell melanoma, eyelid melanoma, amelanotic melanoma)

**Rationale:**
- Nodular and superficial spreading melanoma are histological subtypes already within the biological population (BRAF V600-mutant cutaneous melanoma) that the pivotal dabrafenib+trametinib trials enrolled — the mechanistic case is strong, but subtype-specific confirmatory trials are absent, so guardrails (mandatory BRAF V600 testing, subtype-stratified monitoring) are warranted.
- Non-cutaneous, ocular, and mucosal melanoma predictions rest only on case-level evidence in a population with lower BRAF mutation prevalence, and choroideremia/scrotal/balloon-cell/CDK4-linked melanoma predictions have zero clinical or mechanistic support — these should not proceed without new primary evidence.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- DrugBank-sourced mechanism of action and toxicity profile (DG002)
- BRAF V600 mutation-status stratification data for any subtype-specific trial design
- Confirmation of trametinib's approved label scope (cutaneous vs. all melanoma) from an authoritative regulatory source, since it is absent from the regulatory data provided here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

