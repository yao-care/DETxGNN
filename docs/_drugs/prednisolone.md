---
layout: default
title: Prednisolone
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone: From Original Indication (Not Specified in Evidence Pack) to Alopecia Areata

## One-Sentence Summary

> The evidence pack does not record prednisolone's original approved indication, and no German (BfArM) marketing authorization currently exists for this product.
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **19 clinical trials retrieved** (several directly relevant) and **20 publications**, including one placebo-controlled RCT, currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified — no `original_indications` data available in the evidence pack |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for prednisolone is not available in the evidence pack, and no original indication is recorded in this dataset. This is flagged as a High-severity data gap (DG002) that limits formal mechanistic-linkage analysis.

Based on the repurposing rationale associated with this prediction, prednisolone is a systemic corticosteroid. Alopecia areata is understood to be a CD8⁺ T-cell-mediated autoimmune attack on the hair follicle, and systemic corticosteroids — particularly given as pulse therapy — are already an established treatment option for moderate-to-severe or treatment-resistant AA in real-world dermatology practice. This gives the prediction a plausible mechanistic basis (immunosuppression of the autoimmune follicular attack) even without a documented original indication.

Supporting this, a completed Phase 4 trial (NCT01167946) directly tested oral pulse methylprednisolone (a closely related glucocorticoid) in severe therapy-resistant AA, and a placebo-controlled RCT (PMID 15692475) specifically evaluated oral pulse **prednisolone** in AA. Several additional cohort studies and reviews on corticosteroid pulse therapy in AA reinforce that this class of drug already has an established clinical role in this indication, which is consistent with — and independently corroborates — the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone (same corticosteroid class) evaluated in severe therapy-resistant alopecia areata, including totalis/universalis/ophiasic types; investigated whether higher/more frequent pulse dosing improves response. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completed | 296 | Observational safety/effectiveness study of tofacitinib in alopecia, with participants receiving treatment with or without adjuvant prednisolone. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared two delivery methods (DERMOJET vs. standard syringe) for local/intralesional steroid injection in alopecia areata; conventional AA treatment involves topical, intralesional, or oral steroids. |
| [NCT01972217](https://clinicaltrials.gov/study/NCT01972217) | Phase 2 | Completed | 158 | Immune-modulating combination therapy trial in an autoimmune/oncology setting; graded as background reference only — not a direct prednisolone-AA trial. |
| [NCT03616912](https://clinicaltrials.gov/study/NCT03616912) | Phase 3 | Terminated | 830 | Baricitinib (JAK inhibitor, non-corticosteroid mechanism) trial in SLE; included only as landscape reference for autoimmune disease treatment, not direct AA/prednisolone evidence. |

*Note: The evidence pool also returned numerous Phase 2/3 SLE trials of unrelated biologics (efavaleukin alfa, acazicolcept, anifrolumab, sirolimus, enpatoran, etc.). These were excluded from the table above as they are not directly relevant to prednisolone or alopecia areata.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | First placebo-controlled RCT of oral pulse prednisolone therapy in alopecia areata. |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Review (Network Meta-analysis) | Cochrane Database Syst Rev | Compares immunosuppressants, hair growth stimulants, and contact immunotherapy across AA treatments. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, side effects, and prognostic factors of corticosteroid pulse therapy in AA. |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic Review | Australas J Dermatol | Systematic review of systemic treatments (including corticosteroids) for AA, totalis, and universalis. |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohort (Retrospective) | Dermatol Ther | Methylprednisolone alone vs. methylprednisolone + methotrexate in extensive AA. |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Clinical Study | Dermato-endocrinology | Medium-dose prednisolone pulse therapy evaluated in AA; notes efficacy in early-stage disease with potential dose-limiting side effects. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Cohort | Pediatr Dermatol | Reviews pulse dose corticosteroid therapy dosing/administration regimens and side effects in pediatric AA. |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohort | J Dtsch Dermatol Ges | Sequential high- and low-dose systemic corticosteroid therapy for severe childhood AA. |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Mechanistic Study | J Cosmet Dermatol | TNF-α level changes proposed as a mechanism of action for oral pulse steroids in AA. |
| [36681881](https://pubmed.ncbi.nlm.nih.gov/36681881/) | 2023 | Cohort (Retrospective) | J Eur Acad Dermatol Venereol | Long-term patient-reported experience with methylprednisolone pulse (± methotrexate) in AA. |

---

## Germany Market Information

No German (BfArM) marketing authorizations for prednisolone were found in the evidence pack (`total_licenses: 0`, market status: **未上市 / Not Marketed**). No product- or license-level detail is available to populate this section.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in the evidence pack — DDI query status: not found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Corticosteroid pulse therapy already has an established clinical role in alopecia areata, supported by a placebo-controlled RCT of prednisolone itself, a completed Phase 4 trial of the closely related methylprednisolone, and multiple cohort studies/reviews (Evidence Level L2). However, formal indication approval, MOA documentation, and safety/label data are missing, so this cannot yet proceed without additional guardrails.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (DG001 — **Blocking**: required before S1 safety pre-assessment can proceed)
- Confirmed mechanism of action data from DrugBank (DG002 — High priority, needed for formal mechanistic-linkage analysis)
- Confirmation of the original approved indication(s) for prednisolone, currently missing from the evidence pack
- Drug-drug interaction (DDI) data, since the current query returned no results
- Clarification of dose-equivalence between prednisolone and methylprednisolone (the drug most directly studied in the AA trial/RCT evidence above)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

