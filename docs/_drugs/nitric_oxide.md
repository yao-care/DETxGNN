---
layout: default
title: Nitric Oxide
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Nitric Oxide
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

# Nitric Oxide: From Inhaled Pulmonary Vasodilator to Pulmonary Arterial Hypertension

## One-Sentence Summary

Nitric oxide (NO) is a gaseous signalling molecule whose established clinical role is as an inhaled, selective pulmonary vasodilator (e.g., for hypoxic respiratory failure with pulmonary hypertension in neonates). Among the ten indications the TxGNN model surfaced for this candidate, **Pulmonary Arterial Hypertension (PAH)** is the one with a genuinely supportable evidence base — **50 clinical trials** and **20 publications**, including a completed Phase 3 study of inhaled NO and an RCT — and is therefore selected as the focus of this report rather than the model's single highest-scoring (but evidentially empty) prediction.

> **Note on candidate selection:** TxGNN's top five scoring predictions for this drug (e.g., "malformation syndrome with odontal/periodontal component," "hypertrichosis," "Ambras syndrome," "Dandy-Walker malformation," "isolated genetic hair shaft abnormality") returned either zero clinical trials/literature or literature with no mention of nitric oxide's biology at all. The evidence pack itself flags rank 1 as a likely false positive. These have all been scored **L5 / Hold** and are not carried forward here. Pulmonary Arterial Hypertension (rank 7 by TxGNN score) is the first candidate in the list with a coherent, literature-supported mechanism and an **L1** evidence level, and is the appropriate subject for further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No marketing-authorization record available in this evidence pack (drug not currently marketed in this jurisdiction; NO's established clinical use as an inhaled pulmonary vasodilator is general pharmacological knowledge, not a licensed indication captured here) |
| Predicted New Indication | Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for nitric oxide in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacology, however, nitric oxide is an endogenous, gaseous signalling molecule that activates soluble guanylate cyclase (sGC) in vascular smooth muscle, raising intracellular cGMP and producing selective vasodilation. This NO–sGC–cGMP axis is one of the three core pathobiological pathways targeted by essentially all modern PAH therapies (alongside the endothelin and prostacyclin pathways), and drugs such as PDE5 inhibitors (sildenafil) and sGC stimulators (riociguat) work precisely by amplifying signalling through this same pathway.

The literature returned for this prediction is directly on-mechanism rather than incidental: PAH patients show demonstrable NO deficiency and endothelial dysfunction (PMID 23822809), and the NO pathway is explicitly described as a validated drug target with defined biomarkers (PMID 32442078). Inhaled NO is already used clinically as the reference agent for acute pulmonary vasoreactivity testing in PAH work-up, which is a strong real-world signal that the mechanism translates into measurable hemodynamic effect in this exact patient population.

This mechanistic plausibility is reinforced by closely related, adjacent TxGNN predictions in the same pack: PAH associated with congenital heart disease (L2, Proceed with Guardrails), PAH associated with HIV infection (L3), and PAH associated with chronic hemolytic anemia (L3) — all converge on NO-pathway dysregulation (via eNOS polymorphisms, ADMA elevation, or hemoglobin-mediated NO scavenging, respectively) as part of their pathophysiology. This cluster of internally consistent, mechanistically coherent predictions across PAH subtypes gives the core PAH prediction considerably more credibility than an isolated high score would on its own.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | Safety/efficacy of inhaled NO (IK-3001) in Japanese patients with peri-/post-operative pulmonary hypertension after cardiac surgery |
| [NCT01265888](https://clinicaltrials.gov/study/NCT01265888) | Phase 2 | Completed | 31 | Dose-escalation of inhaled NO (GeNOsyl system) vs placebo in PAH (WHO Group 1) and PH secondary to IPF |
| [NCT02734953](https://clinicaltrials.gov/study/NCT02734953) | Phase 2 | Completed | 10 | Effects of inhaled NO on invasively-derived pulmonary vascular resistance parameters in PAH |
| [NCT04231084](https://clinicaltrials.gov/study/NCT04231084) | Phase 4 | Completed | 115 | Acute hemodynamic comparison of inhaled NO vs inhaled epoprostenol across PH phenotypes |
| [NCT05721144](https://clinicaltrials.gov/study/NCT05721144) | Phase 2 | Completed | 660 | Large RCT: perioperative inhaled NO to reduce postoperative pulmonary complications in recent COVID-19 patients |
| [NCT00335244](https://clinicaltrials.gov/study/NCT00335244) | Phase 3 | Completed | 77 | Single-blind RCT of IV L-citrulline (NO-pathway precursor) vs placebo in children undergoing cardiopulmonary bypass |
| [NCT00005776](https://clinicaltrials.gov/study/NCT00005776) | Phase 3 | Terminated | 235 | NINOS landmark RCT: inhaled NO vs 100% oxygen in term/near-term infants with hypoxic respiratory failure |
| [NCT00005773](https://clinicaltrials.gov/study/NCT00005773) | Phase 3 | Terminated | 302 | RCT testing early vs standard-threshold inhaled NO therapy in term/near-term infants with respiratory failure |
| [NCT01717209](https://clinicaltrials.gov/study/NCT01717209) | Phase 4 | Completed | 14 | Combined inhaled NO + inhaled prostacyclin on right-heart function after heart transplant/LVAD surgery |
| [NCT00001963](https://clinicaltrials.gov/study/NCT00001963) | Phase 1 | Completed | 28 | Vascular effects of endothelium-derived vs hemoglobin-transported NO in healthy subjects (mechanistic support) |

*50 trials were returned in total for this indication; the 10 above were prioritized for direct relevance to NO administration and pulmonary vascular endpoints. Several additional Phase 2–4 trials (e.g., riociguat, sildenafil, L-citrulline studies) further corroborate the NO/cGMP pathway as an active PAH treatment target but were not included to avoid redundancy.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33773120](https://pubmed.ncbi.nlm.nih.gov/33773120/) | 2021 | RCT | Lancet Respiratory Medicine | REPLACE trial: switching to riociguat (sGC stimulator, same pathway as NO) vs continued PDE5 inhibitor therapy in PAH |
| [23822809](https://pubmed.ncbi.nlm.nih.gov/23822809/) | 2013 | Review | Am J Respir Crit Care Med | NO deficiency and endothelial dysfunction are core features of PAH pathogenesis |
| [32442078](https://pubmed.ncbi.nlm.nih.gov/32442078/) | 2020 | Review | Current Medicinal Chemistry | The NO pathway in PAH: pathomechanism, biomarkers, and drug targets |
| [38416633](https://pubmed.ncbi.nlm.nih.gov/38416633/) | 2024 | Network Meta-Analysis | European Heart Journal | Individual participant data network meta-analysis comparing PAH treatment pathways, including the NO pathway |
| [39580019](https://pubmed.ncbi.nlm.nih.gov/39580019/) | 2025 | Systematic Review/Meta-Analysis | Nitric Oxide (journal) | NOS3 gene polymorphism is associated with PAH risk |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | Diagnosis and treatment overview of PAH |
| [39209476](https://pubmed.ncbi.nlm.nih.gov/39209476/) | 2024 | Review | European Respiratory Journal | Treatment algorithm for PAH, covering NO/endothelin/prostacyclin/BMP pathways |
| [33836637](https://pubmed.ncbi.nlm.nih.gov/33836637/) | 2021 | Review | J Cardiovasc Pharmacol Ther | Combination PAH therapy targeting the NO and prostacyclin pathways |
| [38054614](https://pubmed.ncbi.nlm.nih.gov/38054614/) | 2024 | Review | Small (journal) | Inhalable NO delivery systems developed specifically for PAH treatment |
| [20051913](https://pubmed.ncbi.nlm.nih.gov/20051913/) | 2010 | Review | Journal of Hypertension | NO, oxidative stress, and inflammation in PAH pathogenesis |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data were queried but not found for this candidate — recorded as a Blocking data gap, DG001, requiring TFDA/BfArM package-insert retrieval before any S1 safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pulmonary Arterial Hypertension is supported by an L1 evidence level — a completed Phase 3 trial of inhaled NO, several additional completed Phase 2–4 trials directly testing NO administration in pulmonary hypertension populations, and 20 publications establishing the NO–cGMP pathway as a validated, already-drugged mechanism in PAH. This is a mechanistically coherent and clinically plausible repurposing candidate, distinct from the model's top-scoring but evidence-free predictions (ranks 1–5), which remain on Hold.

**To proceed, the following is needed:**
- Retrieve official package insert / regulatory safety data (warnings, contraindications) — currently a Blocking gap (DG001)
- Obtain detailed DrugBank mechanism-of-action documentation (DG002)
- Confirm route-of-administration compatibility (inhalation delivery systems, dosing) — currently unassessed ("pending") in this evidence pack
- Clarify actual marketing/licensing status in the target market, since 0 authorizations are currently on record
- Reassess ranks 1–5 with manual mechanistic review before closing them out as false positives, given TxGNN scored them above the PAH prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

