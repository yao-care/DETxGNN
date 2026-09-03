---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: Data-Gap-Driven Confirmation of Obstructive Lung Disease (COPD/Asthma) Use

## One-Sentence Summary

> This evidence pack shows no recorded original indication or mechanism of action for Vilanterol — both are flagged as data gaps in the source database, and the drug is not currently marketed in Taiwan.
> The TxGNN model's top prediction is **Obstructive Lung Disease**, and the supporting evidence — **80+ clinical trials (many completed Phase 3) and 20 publications**, including the landmark IMPACT and FULFIL trials — shows this is not a novel repurposing signal but Vilanterol's already well-established, globally approved role as a long-acting β2-agonist (LABA) in COPD/asthma combination inhalers (e.g., Breo/Relvar Ellipta, Anoro Ellipta, Trelegy Ellipta).
> This case should be read as **data-gap remediation and confirmation**, not discovery of a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on file (drug not marketed in Taiwan; original_indications field empty in source data) |
| Predicted New Indication | Obstructive Lung Disease (COPD / Asthma) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The evidence pack's structured `original_moa` field is a data gap, but the underlying trial and literature evidence consistently describes Vilanterol's pharmacology: it is a selective long-acting β2-adrenergic receptor agonist (LABA) that activates β2 receptors on bronchial smooth muscle, increasing intracellular cAMP and producing sustained bronchodilation (~24-hour duration). This is a direct, mechanism-based pharmacological effect on airway obstruction — not a speculative network-inferred association.

Critically, "obstructive lung disease" is not a new therapeutic direction for Vilanterol — it is the drug's core, already-marketed indication internationally, delivered as a component of fixed-dose combination inhalers with fluticasone furoate (Breo/Relvar Ellipta), umeclidinium (Anoro Ellipta), or both (Trelegy Ellipta, triple ICS/LAMA/LABA therapy). The empty `original_indications` and `original_moa: [Data Gap]` fields in this evidence pack should be understood as a **database population gap**, not evidence that the drug lacks an established indication.

Because the mechanism-to-disease link is direct rather than inferred, and because the evidence base includes large, high-quality confirmatory trials (e.g., the 10,355-patient IMPACT trial and the FULFIL trial), this candidate scores at the highest evidence tier (L1) despite the underlying data gaps in the drug-level metadata.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02164513](https://clinicaltrials.gov/study/NCT02164513) | Phase 3 | Completed | 10,355 | IMPACT trial — FF/UMEC/VI triple therapy reduces annual exacerbation rate vs. FF/VI or UMEC/VI dual therapy in COPD |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4,233 | 12-month effectiveness of FF/VI once-daily vs. usual asthma maintenance therapy |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Phase 3 | Completed | 1,538 | Pivotal 24-week efficacy/safety study of UMEC/VI and individual components vs. placebo in COPD |
| [NCT02467452](https://clinicaltrials.gov/study/NCT02467452) | Phase 3 | Completed | 1,479 | Non-inferiority of triple pMDI therapy vs. FF/VI plus tiotropium in COPD |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | Completed | 1,055 | Closed triple therapy (FF/UMEC/VI) vs. open triple (FF/VI + UMEC) — lung function comparison in COPD |
| [NCT03248128](https://clinicaltrials.gov/study/NCT03248128) | Phase 3 | Completed | 906 | FF/VI vs. FF alone in pediatric/adolescent asthma (5–17y) uncontrolled on ICS |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Phase 3 | Completed | 717 | UMEC/VI vs. fluticasone/salmeterol over 12 weeks in COPD (Grade A relevance) |
| [NCT01817764](https://clinicaltrials.gov/study/NCT01817764) | Phase 3 | Completed | 707 | UMEC/VI vs. fluticasone/salmeterol over 12 weeks in COPD (Grade A relevance) |
| [NCT05757102](https://clinicaltrials.gov/study/NCT05757102) | Phase 3 | Recruiting | 292 | FF/UMEC/VI vs. FF/VI in adolescents (12–17y) with inadequately controlled asthma; Bayesian dynamic borrowing design |
| [NCT03378648](https://clinicaltrials.gov/study/NCT03378648) | Phase 1/2 | Completed | 118 | First-in-human safety/PK/PD study of a bifunctional muscarinic antagonist/β2-agonist (MABA) bronchodilator compound |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | NEJM | IMPACT trial — triple ICS/LAMA/LABA therapy vs. dual therapy in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (mortality analysis) | Am J Respir Crit Care Med | FF/UMEC/VI significantly reduces all-cause mortality vs. UMEC/VI in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL trial — once-daily triple therapy superior to ICS/LABA dual therapy in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT (Phase 3A) | Lancet Respir Med | CAPTAIN trial — FF/UMEC/VI vs. FF/VI in inadequately controlled asthma |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT subgroup analysis | Eur Respir J | IMPACT trial — effect of exacerbation history on treatment outcomes |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | FF/UMEC/VI vs. other COPD therapies — comparative efficacy |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review & meta-analysis | BMC Pulm Med | UMEC/VI vs. other bronchodilators in COPD management |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic review | Clin Respir J | Fixed-dose UMEC/VI combination for COPD — systematic review |
| [30463451](https://pubmed.ncbi.nlm.nih.gov/30463451/) | 2018 | Review | Expert Rev Respir Med | FF/UMEC/VI combination therapy for COPD |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Rev Respir Med | Fluticasone furoate and vilanterol for COPD treatment |

---

## Taiwan Market Information

No authorizations on file. Vilanterol-containing products are not currently marketed in Taiwan according to this evidence pack (`total_licenses: 0`, `licenses: []`).

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack contains no key warnings, contraindications, or drug interaction data (all flagged as data gaps; DDI query returned no results), and this is recorded as a Blocking data gap (DG001) preventing formal safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The link between Vilanterol and obstructive lung disease is supported by L1-level evidence — multiple completed Phase 3 RCTs including the large-scale IMPACT and FULFIL trials — and reflects a direct, established pharmacological mechanism (LABA bronchodilation) rather than a speculative prediction. However, this evidence pack's drug-level metadata (original indication, MOA) and all safety/regulatory data (TFDA label, contraindications, DDI) are missing, and the drug is not currently marketed in Taiwan, so it cannot yet proceed past initial safety screening (S1/S3 gate).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA label warnings/contraindications, or confirm via original manufacturer labeling (Breo/Anoro/Trelegy Ellipta) if Vilanterol is imported as a combination product
- Resolve DG002 (High): populate MOA and original indication fields from DrugBank to correct the apparent "data gap" that is driving this candidate to appear as a novel prediction rather than a confirmed existing use
- Confirm Taiwan regulatory/import status for Vilanterol-containing combination products
- Reclassify this candidate internally as **data confirmation**, not new indication discovery, to avoid misrepresenting an already-approved global indication as a repurposing finding

**Note on other predicted indications (ranks 2–10):** the remaining candidates in this evidence pack (hyperlucent lung, interstitial emphysema, compensatory emphysema, tracheal stenosis, tracheal calcification, laryngotracheitis, congenital lobar emphysema, bronchial neoplasm, respiratory malformation) are either pure TxGNN model scores with no supporting clinical trial or literature evidence (L5, Hold), or show evidence/topic mismatches where the underlying trials and papers are generic COPD/asthma studies unrelated to the specific predicted disease (likely ontology label mismatch). None of these are ready for further evaluation without additional targeted evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

