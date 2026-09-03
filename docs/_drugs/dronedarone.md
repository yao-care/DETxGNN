---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is a Class III antiarrhythmic originally used to maintain sinus rhythm in patients with paroxysmal or persistent atrial fibrillation (AF)/atrial flutter. The TxGNN model predicts it may also reduce the risk of **stroke** (a downstream complication of AF), with **19 clinical trials** and **20 publications** currently informing this direction — though the evidence is population-specific and includes a major safety caveat.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation / atrial flutter (sinus rhythm maintenance in paroxysmal or persistent AF) |
| Predicted New Indication | Stroke Disorder (stroke risk reduction in AF patients) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dronedarone is a benzofuran derivative and non-iodinated analogue of amiodarone. It acts as a multi-channel blocker (sodium, potassium, calcium) with additional antiadrenergic activity, and is already approved for maintaining sinus rhythm in AF/atrial flutter.

The proposed new indication — stroke risk reduction — is not a separate disease area but a downstream consequence of the drug's approved mechanism: by lowering AF burden and restoring/maintaining sinus rhythm, dronedarone theoretically reduces atrial thrombus formation and the risk of cardioembolic (ischemic) stroke. This is not a novel target discovery; it reflects a class effect already partly captured in the pivotal **ATHENA** trial (Phase 3 RCT), whose post-hoc analyses suggested a reduction in stroke incidence among patients with paroxysmal/persistent AF. One mechanistic study (PMID 28992468) further suggests dronedarone may have direct anticoagulant/antiplatelet effects independent of its antiarrhythmic action, offering a possible additional pathway for stroke reduction.

However, this rationale has an important population boundary: the **PALLAS trial** (PMID 22082198, NCT01151137), conducted in patients with **permanent** AF and additional risk factors, found dronedarone *increased* stroke, myocardial infarction, and cardiovascular death, leading to early termination. This means the stroke-benefit signal applies specifically to paroxysmal/persistent AF, not permanent AF — a critical guardrail for any repurposing pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | Observational | Completed | 1,015 | Real-world comparative effectiveness of dronedarone vs. other antiarrhythmic drugs for AF (Germany, Spain, Italy, USA) |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs. usual care in first-detected AF |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | **PALLAS trial** — dronedarone 400mg BID added to standard therapy in permanent AF with risk factors; terminated early after dronedarone *increased* stroke, CV death, and hospitalization vs. placebo |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | Systematic review/NMA | Completed | 87,810 | Systematic literature review/network meta-analysis of dronedarone (Multaq®) vs. sotalol safety and effectiveness in AF |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA trial — dronedarone vs. placebo post-catheter ablation; assessed AF recurrence and atrial fibrosis progression |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1,898 | Planned multicenter study on efficacy, safety, and quality-of-life outcomes of dronedarone for early rhythm control |
| [NCT07242326](https://clinicaltrials.gov/study/NCT07242326) | Observational | Enrolling by invitation | 1,000 | Registry assessing label-concordant dosing and adherence for oral anticoagulants/antiarrhythmics in elderly AF patients |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | RCT comparing amiodarone vs. dronedarone for maintenance of sinus rhythm post-cardioversion |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST trial — early structured rhythm control (AADs incl. dronedarone + ablation) vs. usual care to prevent AF-related complications, including stroke |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1,746 | Planned RCT of early rhythm control therapy after acute ischemic stroke with AF to prevent recurrent cardiovascular events |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT | N Engl J Med | **PALLAS trial**: dronedarone in high-risk permanent AF increased risk of stroke, MI, and CV death; trial terminated early |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT (EAST-AFNET4 analysis) | Clin Res Cardiol | Long-term safety/efficacy of amiodarone and dronedarone for early rhythm control in the EAST-AFNET4 cohort |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atrial Fibrillation | Real-world comparison: dronedarone vs. amiodarone/other AADs — risk of CV events, stroke, CHF, interstitial lung disease, liver injury |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Veterans database: dronedarone vs. sotalol effectiveness/safety head-to-head in AAD-naive AF patients |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc analysis | Eur J Heart Fail | ATHENA post-hoc analysis: dronedarone in AF with HFpEF/HFmrEF |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Curr Cardiol Rev | Stroke prevention in atrial fibrillation: concepts and controversies |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Dronedarone approval and efficacy, including post-hoc stroke risk reduction from ATHENA |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic | Atherosclerosis | Dronedarone exerts anticoagulant/antiplatelet effects independent of its antiarrhythmic action |
| [24469871](https://pubmed.ncbi.nlm.nih.gov/24469871/) | 2013 | Review | Cardiol J | Efficacy and tolerability of dronedarone in clinical practice for AF |
| [25428811](https://pubmed.ncbi.nlm.nih.gov/25428811/) | 2015 | Pharmacoeconomic review | Kardiol Pol | Cost-effectiveness of dronedarone vs. amiodarone, propafenone, and sotalol (Serbia) |

---

## Germany Market Information

Dronedarone is currently **not marketed** in Germany, and no active marketing authorizations were found in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for formal safety information — detailed warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as data gaps DG001/DG002 below).

That said, two important safety signals emerged directly from the clinical evidence reviewed:

- **Permanent AF is a high-risk population**: The PALLAS trial (NCT01151137) found that adding dronedarone to standard therapy in patients with permanent AF and additional risk factors *increased* stroke, MI, and cardiovascular death, leading to early termination. Any stroke-prevention benefit appears limited to paroxysmal/persistent AF.
- **Digoxin interaction risk**: A real-world data study (PMID 33888353) found that concomitant dronedarone and digoxin use is associated with increased risk of digitalis intoxication (likely via P-glycoprotein inhibition), warranting monitoring in patients on combined therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple real-world cohort studies and ATHENA post-hoc analyses support a stroke-risk-reduction signal for dronedarone in paroxysmal/persistent AF, but the PALLAS trial demonstrates clear harm in permanent AF with additional risk factors — the predicted benefit is population-specific, not universal.

**To proceed, the following is needed:**
- Formal safety data: TFDA/EU package insert with warnings and contraindications (currently a **Blocking** data gap, DG001)
- Formal mechanism-of-action documentation from DrugBank (currently a **High**-severity data gap, DG002)
- A protocol that explicitly restricts the stroke-prevention claim to paroxysmal/persistent AF and excludes permanent AF
- A monitoring plan for known interactions (e.g., digoxin) and cardiac safety (heart rate/QT, hepatic function)
- Clarification of German market entry pathway, given the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

