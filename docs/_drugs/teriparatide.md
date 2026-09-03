---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Pregnancy and Lactation-Associated Osteoporosis (PLO)

## One-Sentence Summary

Teriparatide (recombinant human PTH 1-34) is originally used to treat osteoporosis by stimulating new bone formation. Among the TxGNN candidate indications, **Pregnancy and Lactation-Associated Osteoporosis (PLO)** is the one supported by real mechanistic and clinical rationale — it is essentially an osteoporosis subtype, not a novel disease target — and is backed by **2 clinical trials** and **19 publications**, several specifically studying teriparatide in this exact patient population.

> **Note on ranking**: TxGNN's top-scored candidates (duodenal ulcer, esophageal malformation, duodenal obstruction, duodenogastric reflux, Worth syndrome, autosomal dominant vitreoretinopathy, SCOT deficiency) have no plausible mechanistic link to PTH/bone metabolism and no supporting evidence — these are flagged as model noise (`Hold`, L5) and are not carried forward in this report. PLO (rank 8) is the only candidate with genuine mechanistic plausibility and clinical evidence, so it is used as the headline prediction here.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (per clinical trial description in evidence pack: "approved for the treatment of osteoporosis as FORTEO"; not independently verified via German market authorization, as the product is not currently marketed in Germany) |
| Predicted New Indication | Pregnancy and Lactation-Associated Osteoporosis (PLO) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record itself (flagged as a High-severity data gap). However, the evidence pack's own clinical trial descriptions confirm that teriparatide, as PTH(1-34), "has potent bone-building actions and has been approved for the treatment of osteoporosis as FORTEO," working by stimulating osteoblast activity and increasing bone mineral density.

PLO is not a mechanistically distinct new disease — it is a rare subtype of osteoporosis that occurs specifically during late pregnancy or the postpartum/lactation period, presenting with vertebral fragility fractures. The underlying pathology (bone loss, low bone mineral density, fracture risk) is the same skeletal fragility process that teriparatide is already approved to treat; PLO simply represents a distinct patient subgroup and etiological context (pregnancy-related calcium/bone physiology) rather than a new pharmacological target.

Because the anabolic bone-forming mechanism is identical, teriparatide's applicability to PLO is mechanistically well-supported, and this is corroborated by multiple published case series and cohort studies (below) specifically evaluating teriparatide in PLO patients — this is not a case of a prediction with no clinical grounding, but rather a plausible expansion of an existing, well-established mechanism into an underserved patient population lacking dedicated RCTs.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Studied PTH(1-34)'s impact on oral bone regeneration in periodontal surgery patients; not a PLO population, but supports PTH's general bone-forming mechanism (relevance grade: C, indirect) |
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Studied renal osteodystrophy and CKD-associated bone loss; not PLO-specific, low direct relevance (relevance grade: C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic Review/Meta-analysis | J Clin Endocrinol Metab | Comparative effectiveness review of therapeutic interventions for PLO; optimal management still not fully established |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Cohort/Case Series | Calcif Tissue Int | Multicenter retrospective study: 19 PLO patients treated with teriparatide (20 μg/day) vs. conventional management, assessing BMD and trabecular bone score outcomes |
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review/Meta-analysis | Osteoporos Int | 35 studies, 943 patients with pregnancy-associated osteoporosis; vertebral fractures and back pain common; treatment response data still limited |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Case Series | Geburtshilfe Frauenheilkd | 47 women with PLO and vertebral fractures treated with teriparatide; assessed impact on subsequent fracture risk and BMD |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Reviews treatment strategies for PLO with specific focus on teriparatide use, given the lack of dedicated clinical trials |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Case Series | Calcif Tissue Int | Examined BMD outcomes after teriparatide discontinuation, with or without sequential antiresorptive therapy, in PLO patients |
| [36764958](https://pubmed.ncbi.nlm.nih.gov/36764958/) | 2023 | Case Report | Calcif Tissue Int | Documented bone microarchitecture and strength improvements during combined teriparatide + zoledronic acid treatment in a PLO patient with multiple vertebral fractures |
| [28084543](https://pubmed.ncbi.nlm.nih.gov/28084543/) | 2017 | Review | Z Rheumatol | Reviews ~100 published PLO cases; concludes teriparatide and bisphosphonates appear to be the best treatment options |
| [39156353](https://pubmed.ncbi.nlm.nih.gov/39156353/) | 2024 | Case Report | Cureus | PLO patient treated aggressively with teriparatide subsequently had a healthy second pregnancy without recurrence |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | Calcif Tissue Int | General overview of PLO pathophysiology, presentation, and treatment approaches including teriparatide |

---

## Germany Market Information

Teriparatide is **not currently marketed in Germany** — the regulatory dataset shows 0 authorizations on file. No product license, dosage form, or approved indication text is available from the German registry for comparison.

---

## Safety Considerations

Formal package-insert-level safety data (key warnings, contraindications, DDI) is marked as a **Blocking data gap** (DG001) — TFDA/regulatory-sourced warnings have not yet been retrieved and this must be resolved before any Stage 1 safety assessment.

That said, the evidence pack's own literature review (collected under a separate branch of the prediction set) surfaces known teriparatide safety signals worth carrying forward into any guardrail plan:
- **Osteosarcoma risk** and **atypical fractures** — cited as recognized long-term risks in osteoporosis treatment reviews
- **Osteonecrosis of the jaw (ONJ)** and **atrial fibrillation** — reported as potential adverse events in osteoporosis drug safety reviews
- **Worsening of calcinosis cutis** — reported in two case reports involving patients with underlying autoimmune disease (dermatomyositis, CREST syndrome) treated with teriparatide

These signals are risk-related, not efficacy findings, and should be incorporated into any monitoring plan pending formal package insert retrieval.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple cohort/case-series studies and systematic reviews directly support teriparatide's use in PLO, and the underlying mechanism (PTH-driven bone anabolism) is identical to its approved osteoporosis indication — this is a mechanistically coherent extension to a specific patient subgroup rather than a speculative new indication. However, no Phase 3 RCT exists specifically for PLO, and pregnancy-specific safety data remains limited.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA package insert warnings and contraindications (currently a Blocking data gap, DG001)
- Obtain formal DrugBank/FDA-label MOA confirmation (High-severity data gap, DG002)
- Define pregnancy/lactation-specific safety monitoring protocol, given absence of controlled pregnancy safety data
- Recommend co-management pathway with endocrinology/obstetrics for any real-world use in PLO patients
- Deprioritize (Hold) all other TxGNN-predicted indications in this pack pending independent mechanistic or literature support — none currently meet even L4 evidence with therapeutic (as opposed to safety-signal) literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

