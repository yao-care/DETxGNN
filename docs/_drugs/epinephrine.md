---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Anaphylaxis to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a naturally occurring catecholamine classically used as first-line emergency treatment for anaphylaxis and cardiac arrest, and historically as a bronchodilator for asthma (e.g., OTC inhalers such as Primatene Mist).
The TxGNN model predicts it may also be effective for **Obstructive Lung Disease**,
with **10+ directly relevant clinical trials** (out of 50 retrieved) and **20 publications**, including two Cochrane systematic reviews, currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaphylaxis / cardiac arrest resuscitation (established emergency-use indications; no formal regulatory license record available in this dataset) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no formal drug-record mechanism-of-action (MOA) entry is available for epinephrine in this dataset (`original_moa: [Data Gap]`). However, based on well-established pharmacology cited in the repurposing analysis, epinephrine is a **non-selective adrenergic receptor agonist**: it directly activates β2-adrenergic receptors on bronchial smooth muscle to produce bronchodilation, and simultaneously activates α1 receptors to constrict airway mucosal blood vessels, reducing mucosal edema. This dual action is the pharmacological basis for the long-standing use of (racemic) epinephrine in croup and bronchiolitis — conditions that fall under the broader "obstructive lung disease" umbrella.

Epinephrine's original, well-established indications (anaphylaxis, cardiac arrest, and historically asthma/bronchospasm via inhaled formulations) already sit squarely within the same receptor pharmacology being invoked for the new prediction — this is not an indirect mechanistic leap but a direct extension of the same β2/α1-receptor activity to a related airway-obstruction phenotype.

Because obstructive lung disease (asthma, COPD, bronchiolitis) shares the core pathophysiology of reversible or partially reversible airway narrowing, the same receptor-mediated bronchodilation/decongestion effect that underlies epinephrine's approved emergency uses is directly applicable — and indeed several dedicated inhaled-epinephrine formulations (e.g., "E004", Epinephrine HFA/Primatene Mist) have already been clinically tested specifically in asthma and bronchiolitis, reinforcing that this is an established, not purely theoretical, mechanistic link.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | NA | Completed | 60 | Compared nebulized 3% hypertonic saline vs. nebulized adrenaline in bronchiolitis; direct epinephrine intervention trial (Grade A relevance). |
| [NCT00116584](https://clinicaltrials.gov/study/NCT00116584) | Phase 3 | Completed | 72 | Heliox-driven racemic epinephrine nebulization vs. conventional air-oxygen nebulization in moderate-to-severe pediatric bronchiolitis. |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Pilot RCT of epinephrine, dexamethasone, and hypertonic saline for reducing hospitalization in bronchiolitis. |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | Nebulized hypertonic saline plus epinephrine vs. normal saline plus epinephrine in hospitalized infants with bronchiolitis. |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | Multi-center, double-blind, placebo-controlled trial of Epinephrine Inhalation Aerosol (E004) vs. placebo in 4–11 year-old children with asthma. |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Single-dose, double-blind, placebo-controlled crossover study of E004 (epinephrine inhalation aerosol) in pediatric asthma. |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | Completed | 18 | Crossover study of intranasal epinephrine (ARS-1, needle-free route) vs. albuterol in persistent asthma. |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Pharmacokinetic study of Armstrong's Epinephrine Inhalation Aerosol (HFA-MDI, E004) using deuterium-labeled epinephrine in healthy volunteers. |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Pharmacokinetic and safety assessment of Epinephrine Inhalation Aerosol USP (HFA-MDI) under augmented-dose conditions. |
| [NCT01025648](https://clinicaltrials.gov/study/NCT01025648) | Phase 1/2 | Terminated | 9 | Six-arm crossover dose-ranging study of Epinephrine HFA-MDI (E004) vs. placebo and an active epinephrine CFC-MDI comparator in asthma patients; terminated early. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review on epinephrine for bronchiolitis; notes bronchodilators are commonly used despite uncertain overall effectiveness. |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic Review (Cochrane, prior version) | Cochrane Database Syst Rev | Earlier Cochrane review version; found modest short-term benefit of bronchodilators (incl. epinephrine) in mild-to-moderate bronchiolitis. |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Reviews the role of racemic epinephrine, systemic corticosteroids, hypertonic saline, and high-flow oxygen in pediatric bronchiolitis treatment. |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Overview of bronchiolitis, the most common lower respiratory tract infection in infants, including treatment approaches. |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review | BMJ Clinical Evidence | Earlier overview of bronchiolitis epidemiology and management. |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Pharmacology Study | Clin Pharmacol Ther | Directly compares bronchodilator effects of terbutaline and epinephrine in patients with obstructive lung disease. |
| [4551435](https://pubmed.ncbi.nlm.nih.gov/4551435/) | 1972 | Review | Annals of Allergy | Discusses nebulized bronchodilators (including epinephrine) in obstructive lung disease. |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Reviews acute bronchiolitis and croup, noting symptomatic benefit from nebulized adrenaline in croup. |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort/Mechanistic | Scand J Clin Lab Invest | Found elevated plasma noradrenaline in chronic obstructive lung disease patients, inversely correlated with arterial oxygen saturation. |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review (historical) | J Allergy Clin Immunol | Describes asthma as an obstructive airway disease driven by airway smooth muscle spasm, mucus secretion, and inflammation. |

---

## Germany Market Information

No marketing authorizations are recorded for epinephrine in the current regulatory dataset (market status: **Not Marketed**; total authorizations: **0**). As a result, no product name, dosage form, or approved-indication text is available for comparison in this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug–drug interaction data are all marked as data gaps or "not found" in the current evidence pack.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Epinephrine's β2/α1-adrenergic bronchodilator and decongestant mechanism is pharmacologically well established, and multiple completed trials (including dedicated inhaled-epinephrine formulation studies such as E004/ARS-1 in pediatric and adult asthma, and epinephrine-based nebulization trials in bronchiolitis) directly support activity in obstructive airway conditions. However, the two Cochrane systematic reviews explicitly flag "uncertain effectiveness," and the broad label "obstructive lung disease" spans distinct conditions (asthma, COPD, bronchiolitis) with differing evidence strength — warranting guardrails rather than unconditional advancement.

**To proceed, the following is needed:**
- Detailed, drug-record-level mechanism of action (MOA) documentation (currently a data gap)
- TFDA/regulatory package insert warnings, contraindications, and drug interaction data (currently all data gaps or not found)
- Clarification of which specific obstructive lung disease subtype (asthma vs. COPD vs. bronchiolitis) the repurposing claim should target, since trial evidence quality varies by subtype
- Additional validation given that this is a well-known, decades-old drug — regulatory/market data appears absent from the source dataset and should be reconciled with real-world label information
- Lower-confidence candidates from the same prediction set (e.g., food-dependent exercise-induced anaphylaxis, L3 evidence) may warrant separate, lower-priority follow-up, while "Rienhoff syndrome" (L5, zero evidence) should be treated as likely knowledge-graph noise pending manual review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

