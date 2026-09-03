---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using no additional skill — this is a direct report-drafting task per the supplied template; proceeding with the Evidence Pack for PHENYLEPHRINE (DB00388).

---

# Phenylephrine: From Established Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is a topical α1-adrenergic agonist whose original indication record is not captured in this evidence pack (drug currently not marketed under this registry, 0 licenses). The TxGNN model assigns very high confidence (**99.97%**) to **Nasal Cavity Disease**, and the evidence pack's own rationale notes this largely reflects an *already-established* clinical use (nasal decongestion) rather than a truly novel hypothesis — supported by **8 clinical trials** and **8 publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no license/indication data recorded (drug not marketed) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation (DrugBank field) was not retrieved for this record (flagged as data gap DG002). However, the evidence pack's own repurposing rationale supplies the pharmacological basis: phenylephrine is a **selective α1-adrenergic receptor agonist** that acts directly on nasal mucosal vascular smooth muscle, producing vasoconstriction and reducing mucosal swelling and congestion — a mechanism that maps directly onto the "nasal cavity disease" prediction.

Importantly, this is **not a novel repurposing hypothesis** in the usual sense. As explicitly noted in the evidence pack, the empty `original_indications` field reflects a data-collection gap rather than a true absence of this indication — phenylephrine's decongestant role is long-established clinically (e.g., in co-phenylcaine nasal spray). The TxGNN prediction here functions more as a **confirmation of known pharmacology** than a discovery of new therapeutic potential.

The supporting evidence is a mix of direct (Grade A: co-phenylcaine nasal spray trials) and class-analogous (Grade B: oxymetazoline, another α-agonist decongestant, used comparably in sinus surgery) data, which together are mechanistically coherent even though several retrieved trials (e.g., esmolol/lidocaine, cocaine/xylometazoline comparisons) do not actually involve phenylephrine and were graded C as low-relevance noise from the retrieval process.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | NA | Completed | 106 | Co-phenylcaine (contains phenylephrine) nasal spray vs nebulization for decongestion/local anesthesia prior to nasoendoscopy — directly relevant (Grade A) |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Topical oxymetazoline vs epinephrine (same-class α-agonists) compared for bleeding control/surgical visualization in sinus surgery — class-level evidence (Grade B) |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Four-way crossover RCT on nasal congestion after allergen challenge; whether phenylephrine was the actual study drug is unconfirmed from public data (Grade B) |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | IV esmolol vs lidocaine for recovery quality after sinus surgery — no phenylephrine used (Grade C) |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Kovanaze (tetracaine/oxymetazoline) nasal mist vs articaine for dental anesthesia — no phenylephrine (Grade C) |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Withdrawn duplicate of the Kovanaze vs articaine trial — no data contribution (Grade C) |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | NA | Unknown | 120 | Endoscopic vs external dacryocystorhinostomy technique comparison — no confirmed phenylephrine use (Grade C) |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Cocaine vs lidocaine/xylometazoline vs saline for intranasal analgesia before nasotracheal intubation — no phenylephrine (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind RCT: cophenylcaine spray vs placebo before flexible nasendoscopy — minimal pain/discomfort in both arms, no significant difference found |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | Triple-blind RCT of topical tranexamic acid on bleeding/surgical field quality during FESS in chronic rhinosinusitis |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | Acoustic rhinometry of nasal cavity/nasopharynx geometry before and after adenotonsillectomy |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Cohort | Vestnik Otorinolaringologii | Safety/efficacy evaluation of Polydexa spray with phenylephrine in acute rhinosinusitis |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik Otorinolaringologii | Differential diagnosis of chronic nasal cavity disease after surgery and topical antibiotic therapy (incl. phenylephrine-containing Polydexa) |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik Otorinolaringologii | Pathogenetic approach to treatment of inflammatory diseases of the nose and paranasal sinuses |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case Report | Arch Ophthalmol | Case report: cocaine toxicity during dacryocystorhinostomy, with one patient also reacting to intranasal phenylephrine |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In-vitro | Clin Otolaryngol Allied Sci | In-vitro study of drug effects (including nasal-active agents) on ciliary beat frequency |

---

## Germany Market Information

No marketing authorization records are available in this evidence pack — `market_status` is **未上市 (Not marketed)** with **0 licenses** on file for this drug entity.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data were not retrievable for this record — flagged as blocking data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by one directly relevant Grade A trial/RCT (co-phenylcaine nasal spray) plus consistent class-level evidence from comparator α1-agonists, but this largely confirms an *already-established* decongestant use rather than a novel indication, and critical safety/regulatory documentation is entirely missing.

**To proceed, the following is needed:**
- TFDA/BfArM package insert — warnings, contraindications, DDI data (DG001, **Blocking**)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, **High**)
- Clarification of true original indication/license status, given the drug shows 0 current market authorizations
- Verification of the actual study drug in NCT00562120, as public materials do not confirm phenylephrine was the intervention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

