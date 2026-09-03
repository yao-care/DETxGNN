---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 6
---

# Iron
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

# Iron (DB01592): From an Undocumented Original Indication to Iron-Deficiency-Related Disorders

## One-Sentence Summary

This evidence pack contains no confirmed original indication, mechanism of action, or German market authorization for Iron (DrugBank ID DB01592) — it is currently **not marketed** in Germany with 0 authorizations on file. TxGNN generated **six** candidate indications; after evidence review, only two are clinically coherent extensions of iron's known role in correcting iron deficiency — **Vitamin/Mineral Deficiency Disorder** (L2 evidence, multiple completed Phase 2–4 RCTs) and **Plummer-Vinson syndrome** (L4 evidence, 20 supporting publications) — while the remaining four candidates lack mechanistic plausibility and are flagged as likely prediction noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Data Gap) |
| Predicted New Indication (primary) | Vitamin/Mineral Deficiency Disorder (i.e., iron deficiency correction) |
| Predicted New Indication (secondary) | Plummer-Vinson Syndrome |
| TxGNN Prediction Score (primary) | 99.68% |
| TxGNN Prediction Score (secondary) | 99.89% |
| Evidence Level (primary) | L2 |
| Evidence Level (secondary) | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (iron-deficiency-related indications only) |

### All Six Candidates at a Glance

| Rank | Predicted Indication | Score | Evidence Level | Decision Stage | Recommendation | Note |
|---|---|---|---|---|---|---|
| 1 | Vitamin B12/folate-independent megaloblastic anemia | 99.89% | L5 | S0 | Hold | No trials or literature; TxGNN rationale flags this as a likely spurious "anemia" semantic association — iron has no known mechanism to correct this genetic condition |
| 2 | **Plummer-Vinson syndrome** | 99.89% | L4 | S2 | **Proceed with Guardrails** | 20 supporting publications; iron deficiency is the established etiology of this syndrome |
| 3 | Non-syndromic esophageal malformation | 99.86% | L5 | S0 | Hold | Structural congenital defect; no evidence, no plausible mechanism |
| 4 | Biotin metabolic disease | 99.74% | L4 | S0 | Hold | Cited trials are generic multi-micronutrient studies (mostly graded C relevance), not biotin-disease-specific |
| 5 | **Vitamin deficiency disorder** | 99.68% | L2 | S2 | **Proceed with Guardrails** | Strongest evidence base of all six candidates; note the disease label is an ontology mismatch (iron is a mineral, not a vitamin) |
| 6 | Esophageal disease | 99.42% | L4 | S1 | Research Question | Mixed evidence; only iron-deficiency-linked esophageal subtypes (e.g., webs) are relevant |

---

## Why Are These Predictions Reasonable?

Currently, detailed mechanism of action data for this drug entry is not available. Based on known information, Iron (DB01592) is an essential trace mineral used across many pharmaceutical formulations for the correction of iron deficiency and iron deficiency anemia; its central role is in hemoglobin synthesis, oxygen transport, and mitochondrial/enzymatic cofactor function.

The two evidence-supported candidates are not truly "novel" indications but rather **direct extensions of iron's already-established therapeutic role**:

- **Vitamin/Mineral Deficiency Disorder**: The clinical trial evidence base (pregnancy, heart failure with reduced ejection fraction, post-bariatric surgery, pediatric growth, unexplained anemia of the elderly) consistently tests iron supplementation for correcting measurable iron deficiency. The "vitamin" label is a taxonomic artifact of the disease ontology used by TxGNN — iron deficiency is a mineral deficiency, not a vitamin deficiency — but the underlying clinical signal is real and mechanistically direct.

- **Plummer-Vinson syndrome**: This rare condition's core pathophysiology (dysphagia, esophageal web, iron-deficiency anemia) is *caused by* chronic iron deficiency, and iron repletion is already standard-of-care treatment reported to resolve symptoms and webs in the cited case series and reviews. This is less a "new hypothesis" than a confirmation that TxGNN correctly recovered a well-established clinical relationship.

By contrast, candidates such as megaloblastic anemia (B12/folate-independent, i.e., not caused by iron deficiency), non-syndromic esophageal malformation (a structural congenital defect), and biotin metabolic disease show no mechanistic overlap with iron metabolism, and their supporting "evidence" consists of generically related multi-micronutrient studies rather than disease-specific data — consistent with the scoring engine's own assessment that these are likely artifacts of semantic similarity in the underlying knowledge graph rather than genuine biological signal.

---

## Clinical Trial Evidence (Primary Candidate: Vitamin/Mineral Deficiency Disorder)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01953107](https://clinicaltrials.gov/study/NCT01953107) | Phase 4 | Completed | 200 | Preoperative ferrous fumarate 300mg vs. placebo in newly diagnosed gynecologic oncology patients |
| [NCT01904864](https://clinicaltrials.gov/study/NCT01904864) | Phase 4 | Completed | 80 | NovaFerrum® vs. ferrous sulfate for treatment of nutritional iron deficiency anemia in infants/young children |
| [NCT04764955](https://clinicaltrials.gov/study/NCT04764955) | Phase 3 | Completed | 1,300 | Effect of maternal vitamin D3 supplementation on iron status during pregnancy and early infancy |
| [NCT03079518](https://clinicaltrials.gov/study/NCT03079518) | Phase 2 | Completed | 23 | Ferric carboxymaltose single high-dose infusion effects on FGF23/phosphate metabolism in HFrEF with iron deficiency |
| [NCT05185024](https://clinicaltrials.gov/study/NCT05185024) | N/A | Completed | 152 | Efficacy/safety of three oral iron-containing supplements for correcting hematological indices in iron-deficient adults |
| [NCT01609387](https://clinicaltrials.gov/study/NCT01609387) | Phase 4 | Completed | 300 | Double-blind RCT of postoperative vitamin/mineral supplementation in morbidly obese patients |
| [NCT03247816](https://clinicaltrials.gov/study/NCT03247816) | N/A | Completed | 59 | Real-world effectiveness of ferric maltol (Feraccru®) for iron deficiency anemia in IBD patients |
| [NCT01572506](https://clinicaltrials.gov/study/NCT01572506) | Phase 1 | Completed | 58 | Mechanistic study of unexplained anemia in the elderly (red cell lifespan, iron-related) |
| [NCT04561635](https://clinicaltrials.gov/study/NCT04561635) | N/A | Completed | 98 | Cluster RCT of multi-micronutrient supplementation on growth and iron status in indigenous children (Malaysia) |
| [NCT03762148](https://clinicaltrials.gov/study/NCT03762148) | N/A | Completed | 46 | Dose-dependent effect of galacto-oligosaccharides (GOS) on iron absorption in women with low iron stores |

*Note: The rank-1 (megaloblastic anemia), rank-3 (esophageal malformation), and rank-2 (Plummer-Vinson syndrome) candidates currently have no registered clinical trials in this evidence pack.*

---

## Literature Evidence (Primary Candidate: Vitamin/Mineral Deficiency Disorder)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28034892](https://pubmed.ncbi.nlm.nih.gov/28034892/) | 2017 | Review (Tier 1) | Blood | Clinical management framework for anemia in pregnancy covering iron, cobalamin, and folate deficiencies |
| [34534708](https://pubmed.ncbi.nlm.nih.gov/34534708/) | 2022 | Review (Tier 2) | Bone | Comprehensive review of hypophosphatemia following IV iron therapy and management recommendations |
| [10595751](https://pubmed.ncbi.nlm.nih.gov/10595751/) | 1999 | Review (Tier 2) | Seminars in Hematology | Overview of nutritional anemias with focus on folate, B12, and iron metabolism |
| [1596590](https://pubmed.ncbi.nlm.nih.gov/1596590/) | 1992 | Review (Tier 2) | Bailliere's Clinical Haematology | Global public health perspective on nutritional anaemia, iron deficiency as leading cause |
| [7603852](https://pubmed.ncbi.nlm.nih.gov/7603852/) | 1995 | Review (Tier 2) | Nursing Times | Clinical deficiency testing protocols for iron, B12, and folate |
| [39667365](https://pubmed.ncbi.nlm.nih.gov/39667365/) | 2025 | Review | Nutrition Reviews | Historical and mechanistic review of vitamin A deficiency's impact on iron metabolism |
| [35163110](https://pubmed.ncbi.nlm.nih.gov/35163110/) | 2022 | Systems Review | Int J Mol Sci | Systems-biology analysis of interrelations between iron and vitamin A status |
| [31256475](https://pubmed.ncbi.nlm.nih.gov/31256475/) | 2019 | Review | Australian Journal of General Practice | Primary care management guidance for anaemia in pregnancy |
| [35807896](https://pubmed.ncbi.nlm.nih.gov/35807896/) | 2022 | Narrative Review | Nutrients | Combined roles of vitamin D and iron status on skeletal muscle mass, strength, and function |
| [24998947](https://pubmed.ncbi.nlm.nih.gov/24998947/) | 2014 | Basic Research | J Nutr Biochem | Animal study showing vitamin A deficiency modulates iron metabolism via ineffective erythropoiesis |

---

## Additional Evidence: Plummer-Vinson Syndrome (Secondary Candidate, L4)

No clinical trials are registered for this indication, but the literature base is substantial (20 publications) and clinically well-established. Representative citations:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Review | Journal of Blood Medicine | Current insights on iron deficiency anemia and Plummer-Vinson syndrome (PVS); iron deficiency is central to pathogenesis |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet Journal of Rare Diseases | Classical triad of dysphagia, iron-deficiency anemia, and esophageal webs |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Review | Diseases of the Esophagus | Two PVS cases successfully treated with iron supplementation resulting in symptom elimination |
| [26502163](https://pubmed.ncbi.nlm.nih.gov/26502163/) | 2015 | Review | J Pediatr Gastroenterol Nutr | PVS in children, associated with frequent iron deficiency |
| [37013208](https://pubmed.ncbi.nlm.nih.gov/37013208/) | 2023 | Case Series | Pan African Medical Journal | 23-patient Tunisian case series describing epidemiology and therapeutic outcomes of PVS |

---

## Lower-Confidence Candidates (Not Recommended to Advance)

The following three candidates were reviewed and are **not** recommended for further action based on this evidence pack:

- **Vitamin B12/folate-independent megaloblastic anemia (Rank 1)**: No clinical trials or literature; this is a genetic disorder of DNA synthesis unrelated to iron status. TxGNN's own rationale flags this as likely a spurious "anemia" keyword association.
- **Non-syndromic esophageal malformation (Rank 3)**: A structural congenital defect with no evidence and no plausible biological connection to iron.
- **Biotin metabolic disease (Rank 4)**: Cited trials are generic pediatric/nutritional micronutrient studies (mostly graded C relevance), not biotin-disease-specific; literature is dominated by tangential mitochondrial-metabolism connections.
- **Esophageal disease (Rank 6, broad category)**: Evidence quality is mixed — only the iron-deficiency-linked subtypes (e.g., esophageal webs) are actually supported; most cited trials concern gastric/esophageal cancer or bariatric surgery, unrelated to iron.

---

## Germany Market Information

No German market authorizations are recorded for this drug entry — market status is **Not Marketed**, with **0** total licenses on file in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (limited to Vitamin/Mineral Deficiency Disorder and Plummer-Vinson syndrome only) **/ Hold** (for the remaining four candidates)

**Rationale:**
Two of the six TxGNN-predicted indications (iron/vitamin deficiency correction, and Plummer-Vinson syndrome) are mechanistically coherent and evidence-supported, but they represent confirmation of iron's already-known therapeutic role rather than a genuinely novel repurposing opportunity. The other four candidates lack mechanistic plausibility, clinical trial support, or disease-specific literature, and are more likely artifacts of semantic similarity in the underlying knowledge graph.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank (currently a Blocking/High-severity data gap — DG002)
- Official TFDA/German product label warnings and contraindications (Blocking data gap — DG001), required before any S1 safety pre-screening can occur
- Clarification of the original approved indication(s) for this specific drug entry, which are currently undocumented
- If pursuing Plummer-Vinson syndrome as a formal indication: confirmation of whether this would constitute a genuinely new regulatory indication or simply document an already-standard off-label practice
- If pursuing the "Vitamin deficiency disorder" candidate: reconciliation of the disease-ontology mismatch (iron is a mineral) with regulatory nomenclature before drafting any indication statement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

