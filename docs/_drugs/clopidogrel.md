---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 8
---

# Clopidogrel
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

# Clopidogrel: From Antithrombotic Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

> Clopidogrel is a P2Y12 platelet inhibitor established for prevention of atherothrombotic events (its specific TFDA-approved indication text is not present in this evidence pack — see data gap DG001).
> The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
> with **17 supporting publications** but **no trials specifically tagged to this ICHD subtype**.
> A closely related, higher-confidence prediction — general **Migraine Disorder** — is backed by **8 registered clinical trials**, including one completed Phase 4 RCT (CANOA, published in *JAMA*), and is discussed alongside this indication for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antithrombotic prevention (ACS, ischemic stroke, peripheral arterial disease) — specific TFDA-approved wording not available in this evidence pack (regulatory data gap, DG001) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Germany Market Status | Not marketed (per this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DG002). Based on known pharmacology, clopidogrel is an irreversible P2Y12 ADP-receptor antagonist that inhibits platelet aggregation; its efficacy in preventing atherothrombotic events (ACS, stroke, PAD) is well established.

The mechanistic rationale for migraine centers on patients with patent foramen ovale (PFO) / right-to-left shunt: paradoxical micro-embolization and platelet-released serotonin/inflammatory mediators are thought to trigger cortical spreading depression, the physiological correlate of migraine aura. By inhibiting platelet aggregation, clopidogrel may reduce micro-embolic load and downstream aura-triggering events. This link is best supported for **migraine with aura in general** and for **PFO-associated migraine**, not specifically for the ICHD subtype "migraine with brainstem aura." The evidence pack itself flags this caveat: most supporting studies enrolled general aura populations, and mechanistic extrapolation to the brainstem-aura subtype should be treated cautiously.

Notably, the closely related prediction "Migraine Disorder" (rank 2, score 99.43%) has substantially stronger direct evidence — including a completed Phase 4 RCT (CANOA, n=220) showing clopidogrel + aspirin reduced new-onset migraine after transcatheter ASD closure compared with aspirin alone. This trial supports the biological plausibility of the same mechanism proposed for the brainstem-aura subtype, even though no trial has isolated that specific ICHD phenotype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication (Migraine with Brainstem Aura).

### Context: Related Indication — Migraine Disorder (General)

The broader, closely related TxGNN prediction "Migraine Disorder" has direct trial support and helps explain the mechanistic plausibility above:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA trial: clopidogrel + aspirin vs. aspirin alone significantly reduced new-onset migraine after transcatheter ASD closure (published in JAMA) |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1000 | Large comparison of anticoagulation vs. antiplatelet vs. standard migraine therapy in PFO-associated migraine |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective evaluation of clopidogrel for migraine relief in patients with right-to-left shunt |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING trial: PFO closure vs. medical therapy (incl. antiplatelet) for migraine relief |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | PFO closure device study for migraine relief; clopidogrel used as adjunctive antiplatelet therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: multicentre RCT of percutaneous PFO closure vs. medical therapy in migraine-with-aura patients refractory to treatment |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT | Cephalalgia | Pilot randomised controlled study testing clopidogrel as prophylactic treatment for migraine, based on prior anecdotal reports |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Review | Headache | Systematic review of antithrombotic drugs, including clopidogrel, as migraine preventive therapy |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Cohort (open-label pilot) | Neurology | TRACTOR pilot study: follows finding that thienopyridines (clopidogrel, prasugrel) reduced migraine in PFO patients; tested ticagrelor for similar effect |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Cohort (retrospective) | Neurology | Retrospective review of off-label thienopyridine (clopidogrel/prasugrel) therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Cohort (retrospective) | Cephalalgia | Retrospective review of clopidogrel as primary therapy for migraineurs with right-to-left shunt lesions; proposes platelet activation/paradoxical embolization link |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after transcatheter closure of PFO/ASD via altered anticoagulation regimen |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case series | Journal of Interventional Cardiology | Abrupt, severe migraine developed post-ASD closure in 5/13 patients; dramatic relief achieved with 300 mg clopidogrel |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Case series | Journal of Investigative Medicine | Clopidogrel 75 mg/day added to existing prophylaxis for drug-refractory PFO-associated migraine; PFO found in 56.8% of migraineurs studied |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case series | Cephalalgia | De novo/aggravated migraine after ASD closure; antiplatelet drugs including clopidogrel associated with migraine amelioration |

---

## Germany Market Information

No German market authorization data is available in this evidence pack (market status recorded as "Not marketed," 0 licenses returned).

---

## Safety Considerations

Detailed prescribing warnings, contraindications, and drug-interaction data for clopidogrel are flagged as a **Blocking data gap (DG001)** in this evidence pack — TFDA label warnings/contraindications have not yet been retrieved, and no DDI query results were found.

The following safety-relevant signals appeared incidentally within the collected literature and warrant attention during any further evaluation:
- **Bleeding risk with concomitant NSAIDs**: a case report describes intracerebral hemorrhage following concomitant celecoxib and clopidogrel use (PMID 11793622).
- **Spontaneous bleeding events**: a case of spontaneous knee hemarthrosis was reported with clopidogrel + aspirin combination therapy (PMID 12624808).
- **Possible arthritis association**: a case report describes inflammatory arthritis temporally associated with clopidogrel initiation (PMID 38107217) — a signal in the opposite direction of the joint-disease predictions in this evidence pack (osteoarthritis, rheumatoid arthritis) and worth noting as a caution rather than support for those predictions.

Please refer to the official package insert for complete, authoritative safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence directly supporting clopidogrel for the specific ICHD subtype "migraine with brainstem aura" is limited to observational/mechanistic literature (L3, Research Question stage), with no trials specifically isolating this phenotype. The mechanistic case is plausible and is reinforced by stronger, trial-level evidence (completed Phase 4 CANOA RCT) for the closely related, broader "Migraine Disorder" / PFO-associated migraine indication — but that stronger evidence has not yet been shown to generalize to the brainstem-aura subtype specifically.

**To proceed, the following is needed:**
- Retrieve TFDA/official label warnings and contraindications for clopidogrel (DG001, blocking) before any S1→S2 progression
- Obtain formal MOA documentation from DrugBank (DG002) to firm up the mechanistic rationale
- Determine whether existing or planned trials (e.g., NCT05546320, NCT04946734/SPRING) report subgroup data specific to migraine-with-aura or brainstem-aura phenotypes
- If pursuing this indication, prioritize the better-evidenced "Migraine Disorder" pathway (S2, Proceed with Guardrails) and treat the brainstem-aura subtype as a subgroup hypothesis requiring dedicated study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

