---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Recurrent Intracerebral Hemorrhage Prevention

## One-Sentence Summary

> Amlodipine is a long-acting dihydropyridine calcium channel blocker (CCB) conventionally used for blood pressure control. TxGNN generated 10 candidate new indications for this drug; among them, **secondary prevention of recurrent intracerebral hemorrhage (ICH)** via intensive triple-pill blood pressure control stands out as the only candidate backed by real clinical evidence — **6 clinical trials** (including one completed Phase 3 RCT, n=1,671) and **8 publications**. The other 9 predicted indications range from weak (case-report level) to essentially unsupported (TxGNN score only, no trials or literature) and are not recommended for further action at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (CCB class use — no formal TFDA-approved indication text is available in this dataset) |
| Predicted New Indication | Recurrent Intracerebral Hemorrhage (secondary prevention, intensive BP control) |
| TxGNN Prediction Score | 99.79% (this candidate ranked 10th of 10 by raw TxGNN score, but has the strongest actual evidence) |
| Evidence Level | L1 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for amlodipine is not available in this evidence pack. Based on information embedded in the trial/literature rationale, amlodipine is a dihydropyridine calcium channel blocker that lowers blood pressure by reducing peripheral vascular resistance and cardiac afterload. This is a well-established antihypertensive mechanism rather than a novel one.

The link to ICH is not a mechanistic leap but a direct extension of standard-of-care blood pressure management: intensive BP control is the primary modifiable risk factor for ICH recurrence. The TRIDENT trial (NCT02699645, Phase 3, completed, n=1,671) specifically tested a fixed-dose "Triple Pill" combination (including an amlodipine-class CCB) against standard care in patients with prior ICH, evaluating time to recurrent stroke. A follow-on trial (NCT07458880, actively recruiting, n=140) is now testing a TRICH-score-guided triple antihypertensive strategy in the same population.

This is best understood as a **repositioning within the same pharmacological class and mechanism** (BP lowering) rather than a mechanistically novel indication — amlodipine's role here is as a component of combination therapy, not a standalone new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: fixed-dose triple-pill BP-lowering strategy (incl. amlodipine-class CCB) vs. standard care for preventing recurrent stroke after ICH — directly relevant, largest and most rigorous trial in this set |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Recruiting | 140 | TRICH-score-guided triple antihypertensive medication for BP control after ICH |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | High-normal BP intervention in type 2 diabetics — cardiovascular/cerebrovascular risk factor modification, not ICH-specific |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | High-dose ARB monotherapy vs. ARB+CCB combination therapy in elderly hypertensive Japanese patients at high CV risk |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study — terminated, negligible enrollment |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study — terminated, negligible enrollment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | RCT (trial design/protocol) | Int J Stroke | Rationale and design of the TRIDENT trial evaluating single-pill combination BP-lowering (incl. amlodipine) for ICH secondary prevention |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT (CASE-J) | Hypertens Res | Rationale/design of a large RCT comparing ARB vs. CCB-based regimens for cardiovascular event reduction in high-risk hypertensives |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Review | Neurol Sci | Role of β-blockers vs. other antihypertensives (context for BP agent selection) in acute hypertensive ICH outcomes |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Cohort | Biol Pharm Bull | Long-acting dihydropyridine CCB (benidipine) improves cerebral blood flow autoregulation in hypertensive rats — supportive mechanistic context |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Overview of CCB antihypertensive mechanism and use in severe hypertension |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with hemorrhagic stroke — safety signal |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Rep | PRES after rapid antihypertensive withdrawal in a patient with prior ICH |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Curr Drug Saf | Tizanidine-induced hypotension in stroke patients on antihypertensives — general polypharmacy caution, not amlodipine-specific |

---

## Germany Market Information

Amlodipine is currently **not marketed** in Germany and no marketing authorizations are recorded in this dataset (0 licenses). No approved indication text is therefore available to cite.

---

## Safety Considerations

Formal safety fields (key warnings, contraindications, drug-drug interaction database) contain no data in this evidence pack.

- **Signal identified in literature review**: A case report ([PMID 19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/)) describes probable amlodipine-induced angioedema in a patient with hemorrhagic stroke — relevant given the proposed post-ICH population and warrants monitoring.
- Beyond this, please refer to the package insert for safety information once available.

---

## Additional TxGNN Predictions (Lower Evidence — Not Prioritized)

For completeness, the other 9 candidates from this evidence pack are summarized below. None currently meet the bar for further action (evidence level L3–L5, mostly "Hold").

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 1 | Brain stem infarction | 99.94% | L5 | Hold | No trials or literature; pure model inference |
| 2 | Pulmonary hypertension (lung disease/hypoxia) | 99.91% | L5 | Hold | Literature is generic hypoxia biology, not amlodipine-specific; CCBs may theoretically worsen hypoxic pulmonary vasoconstriction |
| 3 | Pulmonary hypertension (unclear mechanism) | 99.91% | L5 | Hold | No evidence at all |
| 4 | Malignant renovascular hypertension | 99.90% | L4 | Research Question | Only 2 pediatric case reports; mechanistically plausible (standard CCB use in severe hypertension) |
| 5 | Malignant hypertensive renal disease | 99.90% | L5 | Hold | No evidence |
| 6 | Cerebral artery occlusion | 99.89% | L3 | Research Question | Preclinical (rodent MCAO) neuroprotection data; human trials are BP-management context, not disease-specific |
| 7 | Braddock syndrome | 99.88% | L5 | Hold | No known CCB-related pathophysiology; likely false positive |
| 8 | MRI-defined brain infarct | 99.86% | L4 | Hold | Single trial, status Unknown, not amlodipine-specific |
| 9 | ABri amyloidosis | 99.84% | L5 | Hold | No known mechanistic link; likely false positive |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The recurrent intracerebral hemorrhage indication is supported by a completed Phase 3 RCT (TRIDENT, n=1,671) directly testing an amlodipine-containing triple-pill regimen, plus an actively recruiting confirmatory trial (NCT07458880). This is real, class-appropriate evidence — but it reflects amlodipine's established antihypertensive role within a combination strategy, not a standalone novel mechanism, and a safety signal (angioedema in stroke patients) needs monitoring.

**To proceed, the following is needed:**
- TFDA/German product label data (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Formal mechanism-of-action documentation (DG002)
- Formal confirmation of amlodipine's originally approved indication text, given the absence of Germany licensing records
- Monitoring plan for angioedema risk in post-ICH patients
- The 9 lower-evidence candidates should not advance without new trial or literature data; re-screen periodically for updates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

