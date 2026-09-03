---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fluticasone Furoate: From Undocumented Original Indication to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is a corticosteroid whose original approved indication and mechanism of action are not documented in the current evidence pack, and it is currently **not marketed in Germany** (0 licenses on record). The TxGNN model predicts it may be effective for **atopic eczema**, but the supporting evidence base (**9 clinical trials, 2 publications**) tests the related compound fluticasone *propionate* rather than furoate itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no license records available) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa: Data Gap). Based on the information that is available, fluticasone furoate belongs to the corticosteroid (glucocorticoid) class and is described as a second-generation inhaled/intranasal corticosteroid, mechanistically related to fluticasone propionate. Both compounds act via glucocorticoid receptor activation, suppressing inflammatory mediators (IL-4, IL-13, TNF-α) — a pathway plausibly relevant to the skin-barrier inflammation seen in atopic eczema.

This pack does not record fluticasone furoate's currently approved indication or any German marketing history, so a direct "original → new indication" comparison cannot be made from the available data. Critically, essentially all of the supporting clinical evidence below tests topical **fluticasone propionate** cream/ointment formulations, not furoate. Furoate is currently only known to exist in nasal-spray and dry-powder inhaler formulations; no topical dermatologic formulation of furoate exists in the evidence provided. The prediction is therefore best characterized as a **class-level (propionate-derived) inference**, not molecule-specific evidence — and would additionally require new formulation development before any topical use in eczema could be considered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Compared EpiCeram (non-steroidal barrier cream) vs. fluticasone propionate 0.05% cream in pediatric moderate-to-severe AD |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Twice-weekly fluticasone propionate 0.05% cream maintenance therapy to reduce AD relapse in children |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone propionate) lotion 0.05% and effect on HPA axis in pediatric AD |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Intermittent fluticasone propionate 0.05% cream (2x/week) + moisturizer vs. moisturizer alone to reduce relapse in stabilized pediatric AD |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Tacrolimus 0.03% vs. fluticasone 0.005% ointment in children ≥2y with moderate-severe AD |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | Proactive skin-barrier care plus proactive fluticasone propionate cream vs. reactive therapy to prevent AD progression and food allergy |
| [NCT07537751](https://clinicaltrials.gov/study/NCT07537751) | N/A | Completed | 40 | Crisaborole 2% vs. fluticasone propionate 0.05% in children (1–12y) with mild-moderate AD |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Tacrolimus 0.1% vs. fluticasone 0.005% ointment in adults with facial ("red face") AD |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Pimecrolimus 1% + fluticasone (Cutivate) 0.05% combination vs. vehicle in severe AD lesions |

**Note:** All trials above use fluticasone **propionate** formulations; none directly test fluticasone furoate in atopic eczema/dermatitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review/Cohort | Neuroimmunomodulation | Reviews HPA-axis suppression risk from intranasal corticosteroids in allergic disease, noting frequent comorbidity with atopic dermatitis |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case Study | Indian J Otolaryngol Head Neck Surg | Case report on allergen immunotherapy, mentioning atopic dermatitis as one of its emerging applications (background context only) |

---

## Germany Market Information

No marketing authorization is currently registered for fluticasone furoate in Germany (0 licenses on record; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the atopic eczema prediction is class-level only (derived from fluticasone propionate trials, not furoate itself), furoate has no known topical dermatologic formulation, and the drug is not currently marketed in Germany. Combined with a blocking gap in safety/label data, there is insufficient basis to advance beyond a research question at this time.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official German label warnings/contraindications before any S1 safety assessment
- Resolve DG002: obtain documented mechanism of action and confirmed original approved indication(s) for fluticasone furoate
- Furoate-specific (not propionate) clinical evidence in an eczema/dermatitis population
- Formulation feasibility assessment — furoate currently exists only as nasal/inhaled products; a topical form would need to be developed
- Consider evaluating the higher-evidence candidate identified elsewhere in this evidence pack: **bronchitis** (rank 2, L2, "Proceed with Guardrails"), which has direct furoate trial support (e.g., NCT02989935, RELVAR/fluticasone furoate-vilanterol in COPD/bronchitis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

