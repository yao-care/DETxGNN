---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema Prophylaxis to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab is a fully human monoclonal antibody that inhibits plasma kallikrein, already approved and marketed in multiple countries (e.g., Japan, South Korea, China, Argentina — as documented in the trial records below) for long-term prophylaxis of hereditary angioedema (HAE) attacks. The TxGNN model's top prediction, **C1 inhibitor deficiency**, is supported by **24 clinical trials** and **20 publications**. Note, however, that C1 inhibitor deficiency is the underlying genetic defect that *causes* HAE — the disease lanadelumab already treats — so this result largely **confirms the model's accuracy** rather than identifying a genuinely novel repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE) prophylaxis (per trial records; formal MOA/original-indication fields in this evidence pack are marked as data gaps) |
| Predicted New Indication | C1 inhibitor deficiency |
| TxGNN Prediction Score | 99.9955% |
| Evidence Level | L2 (1 completed Phase 3 RCT — HELP Study; remaining Phase 3 trials are open-label/expanded-access/observational) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `original_moa` field in this evidence pack is marked as a data gap. However, based on literature evidence collected in this pack (PMID 30267321), lanadelumab is documented as a fully human monoclonal antibody that inhibits plasma kallikrein, reducing bradykinin generation within the kallikrein-kinin pathway.

C1 inhibitor (encoded by *SERPING1*) is the physiological regulator of plasma kallikrein. When C1-INH is deficient or dysfunctional (HAE Type I/II), kallikrein activity becomes unregulated, driving excess bradykinin production and the vascular permeability that causes HAE attacks. Lanadelumab does not replace C1-INH itself, but inhibits the same downstream enzyme (kallikrein) that C1-INH normally regulates — which is why it is already an approved, first-line long-term prophylactic therapy for HAE due to C1-INH deficiency in numerous markets referenced in the trial data below (Japan, South Korea, China, Argentina, UK, Poland, Saudi Arabia).

Because "C1 inhibitor deficiency" is essentially synonymous with the disease population lanadelumab already treats, this TxGNN prediction should be interpreted as a **validation signal** for the model rather than a new therapeutic hypothesis requiring independent proof-of-concept.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study — pivotal randomized, double-blind, placebo-controlled trial demonstrating efficacy of lanadelumab (DX-2930) in preventing HAE attacks (Type I/II) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension — open-label long-term safety and efficacy follow-up |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Safety, PK, and efficacy of lanadelumab in Chinese HAE patients over 26 weeks |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Efficacy and safety of lanadelumab in Japanese HAE Type I/II patients |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study — PK/PD and efficacy of lanadelumab in pediatric patients (2–<12 years) |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in non-histaminergic angioedema with normal C1-INH |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Phase 3 | Completed | 12 | Japan expanded access program for HAE Type I/II |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Phase 1 | Completed | 32 | First-in-human single ascending dose safety/PK study (healthy subjects) |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1 | Completed | 38 | Multiple ascending dose safety/tolerability/PK study in HAE subjects |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER Study — real-world observational attack-rate comparison (US/Canada) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab significantly reduced HAE attack frequency vs. placebo (HELP Study primary publication) |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | Overview of HAE pathophysiology, C1-INH deficiency, and treatment landscape |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clin Rev Allergy Immunol | Breakthrough attacks in HAE patients on long-term prophylaxis, including lanadelumab |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Current and emerging therapies for C1-INH-HAE, including kallikrein inhibition |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | "Lanadelumab: First Global Approval" — MOA and regulatory approval summary |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-Label Extension | Allergy | HELP OLE Study — long-term effectiveness/safety data (NCT02741596) |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Real-World/Observational | J Allergy Clin Immunol Pract | Multicountry INTEGRATED study on real-world effectiveness of lanadelumab |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs R D | Comparative efficacy/safety of HAE long-term prophylaxis agents (lanadelumab, garadacimab, berotralstat, C1-INH) |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Disease burden of C1-INH deficiency in the Asia-Pacific region |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Preclinical and Phase I data review of lanadelumab for C1-INH-HAE prophylaxis |

---

## Germany Market Information

Lanadelumab currently has **no marketing authorization on record in this evidence pack** (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license table can be generated.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug-drug interactions) are flagged as data gaps in this evidence pack (DG001, severity: **Blocking**) and could not be retrieved from a formal source (e.g., BfArM/EMA label). This gap specifically **blocks progression to the S1 safety pre-assessment stage**.

> Please refer to the official package insert / EMA SmPC for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for lanadelumab in HAE/C1-INH-deficiency-related indications is strong (1 completed Phase 3 RCT plus extensive supporting Phase 3 and real-world data), but this largely reflects the drug's **already-established** indication rather than a novel repurposing candidate.
- A **Blocking**-severity data gap (DG001: missing formal warnings/contraindications) prevents this candidate from proceeding to the S1 safety pre-assessment, per the evidence pack's own gap classification.

**To proceed, the following is needed:**
- Retrieve official label/SmPC data (warnings, contraindications, DDI) from BfArM/EMA to close DG001 before any safety pre-assessment.
- Confirm and document the original MOA (DG002) from a primary regulatory source rather than secondary literature.
- Clarify scope: since "C1 inhibitor deficiency" overlaps with lanadelumab's known approved use, determine whether this candidate should instead be tracked as a **market-entry assessment** for Germany rather than a repurposing candidate.
- If genuine repurposing value is sought, evaluate lower-ranked candidates (e.g., non-histaminergic angioedema with normal C1-INH, supported by NCT04444895/PMID 37780787) which represent more distinct indications from the approved label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

