---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Apixaban: From Anticoagulant Therapy to Migraine Disorder

## One-Sentence Summary

> Apixaban is a direct Factor Xa inhibitor used clinically for anticoagulation (e.g., stroke/systemic embolism prevention in atrial fibrillation, VTE prevention/treatment); detailed original indication text is not available in this evidence pack.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> but only **1 clinical trial** (not apixaban-specific) and **4 case-level publications** currently touch on this direction — and the literature signal is actually contradictory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (no licenses on file); known pharmacologically as an oral anticoagulant (Factor Xa inhibitor) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Data Gap, DG002, in the evidence pack). Based on known pharmacology, apixaban is a direct Factor Xa inhibitor used for anticoagulation, its efficacy in atrial fibrillation-related stroke prevention and VTE has been proven, and the TxGNN prediction likely draws on a broader anticoagulant-migraine association observed in the knowledge graph — some prior case reports describe migraine improvement in patients on warfarin.

However, the mechanistic rationale extracted from the underlying literature is a caution flag rather than a supporting signal. Multiple case reports show that patients whose migraine improved on warfarin experienced **recurrence or worsening of migraine after switching to apixaban**, suggesting the anti-migraine effect may be a warfarin-specific (vitamin K antagonist) mechanism — possibly related to vascular endothelial or inflammatory pathway effects — rather than a class effect shared by all anticoagulants including apixaban. Without confirmed MOA data, this mechanistic applicability to apixaban specifically remains unsupported and possibly contradicted by the available evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | Compared PFO closure vs. anticoagulants vs. antiplatelet therapy for stroke recurrence prevention; primary endpoint was stroke recurrence, not migraine outcomes, and the trial predates widespread apixaban use (relevance graded "C" — not a direct apixaban-migraine trial) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Cohort/Small Trial | Lupus | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies treated with antithrombotic therapy; supports a possible antithrombotic-migraine link but not apixaban-specific |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report | The Neurologist | Migraine with aura worsened after starting apixaban |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | Headache | Migraine with aura in remission on warfarin for 12 years relapsed within 3 weeks of switching to apixaban, and resolved again after resuming warfarin |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | Headache | Vestibular migraine resolved on warfarin plus topiramate (not apixaban) |

---

## Germany Market Information

Apixaban currently has **no marketing authorization on file** in this evidence pack (0 licenses recorded).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as gaps in this evidence pack — notably DG001, a **Blocking** severity gap, meaning this candidate cannot pass the S1 safety pre-screen until TFDA/BfArM label warnings and contraindications are obtained.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (mechanism/preclinical-tier only), there is no clinical trial directly testing apixaban for migraine, and the case-report literature actively points *against* efficacy — several reports show migraine recurrence/worsening on apixaban after improvement on warfarin, suggesting the mechanism may not generalize across anticoagulant classes.

**To proceed, the following is needed:**
- Confirmed apixaban MOA data to resolve DG002 and clarify the anticoagulant-class vs. warfarin-specific mechanism question
- TFDA/BfArM label warnings and contraindications to resolve the Blocking gap DG001 before any S1 safety review
- A dedicated apixaban (vs. warfarin or placebo) migraine outcome study, given the current signal is contradictory rather than merely absent
- Re-evaluation of TxGNN prediction rationale given the discordance between predicted score (99.02%) and the direction of the human literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

