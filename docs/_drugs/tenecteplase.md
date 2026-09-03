---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From STEMI Thrombolysis to Adjunctive Intracoronary Use in Coronary Stenosis

## One-Sentence Summary

Tenecteplase is a third-generation recombinant tissue plasminogen activator, established as a standard IV thrombolytic for ST-elevation myocardial infarction (STEMI). Among ten TxGNN-predicted indications, most (ranks 1–3, 6–10) are either anatomical ECG subtypes of STEMI already within its known mechanism, or disease-embedding false positives with no biological plausibility. The one candidate with real supporting evidence is **Coronary Stenosis** — low-dose intracoronary tenecteplase as an adjunct during primary PCI — backed by **1 completed Phase 2 RCT** and **12 supporting publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | STEMI thrombolysis (per repurposing rationale text; no official label text available — drug not marketed in Germany) |
| Predicted New Indication | Coronary Stenosis (adjunctive low-dose intracoronary use during primary PCI) |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L2 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, high severity). Based on the information present in this evidence pack, tenecteplase is a fibrin-specific tPA variant that activates plasminogen→plasmin to dissolve thrombus; it is already the standard thrombolytic for STEMI. In this context, "coronary stenosis" is not a wholly separate disease but a description of the culprit lesion treated during primary PCI — low-dose **intracoronary** (rather than systemic IV) tenecteplase given at the time of balloon angioplasty is hypothesized to dissolve residual thrombus at the lesion site and improve microvascular perfusion, reducing distal embolization.

It is worth noting that TxGNN ranked three other candidates higher by raw score — posterolateral, posteroinferior, and septal myocardial infarction (ranks 1–3). These are not independent diseases but ECG-based anatomical classifications of STEMI itself, so they fall squarely within tenecteplase's already-established indication rather than representing genuine repurposing. None of the three has direct supporting clinical trials, and only septal MI has tangential literature (a misdiagnosed PE case and a general PE-efficacy study). Ranks 6–10 (chromosomal deletion syndromes, thalassemia, red-cell enzyme deficiencies, hereditary pyropoikilocytosis) have no known link to the fibrinolytic pathway and are best treated as knowledge-graph embedding noise. Coronary stenosis (rank 5) is therefore the only candidate with real actionable evidence, and this report focuses on it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00604695](https://clinicaltrials.gov/study/NCT00604695) | Phase 2 | Completed | 40 | ICE-T trial: evaluated low-dose intracoronary tenecteplase as an adjunct during balloon angioplasty for STEMI; hypothesis that IC tenecteplase enhances clot breakdown at the culprit lesion, reducing myocardial damage. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17102829](https://pubmed.ncbi.nlm.nih.gov/17102829/) | 2006 | RCT | Canadian Journal of Cardiology | TRANSFER-AMI pilot: feasibility of urgent PCI transfer shortly after thrombolysis for STEMI. |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | RCT | Journal of the American College of Cardiology | CAPITAL AMI study: tenecteplase-facilitated angioplasty vs. tenecteplase alone in high-risk STEMI. |
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Cohort/Feasibility | American Journal of Cardiology | ICE-T-TIMI-49: feasibility and safety of low-dose IC tenecteplase (4 mg) vs. saline during primary PCI, randomized 40 patients. |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Cohort | Journal of the American College of Cardiology | Pre-procedural intracoronary fibrin-specific lytic infusion facilitates recanalization of chronic total occlusions. |
| [37199147](https://pubmed.ncbi.nlm.nih.gov/37199147/) | 2023 | Cohort | Circulation | Shorter door-to-needle times associated with better outcomes after IV thrombolysis + endovascular thrombectomy in acute ischemic stroke. |
| [11994554](https://pubmed.ncbi.nlm.nih.gov/11994554/) | 2002 | Cohort | Journal of Thrombosis and Thrombolysis | Precordial ST depression in inferior MI associated with slow flow in non-culprit LAD. |
| [23615379](https://pubmed.ncbi.nlm.nih.gov/23615379/) | 2013 | Review | Cerebrovascular Diseases | Historical perspective and future opportunities for thrombolytics in acute ischaemic stroke. |
| [37823944](https://pubmed.ncbi.nlm.nih.gov/37823944/) | 2023 | Case Report | Egyptian Heart Journal | Clopidogrel resistance leading to subacute stent thrombosis in a resource-limited setting. |
| [25733729](https://pubmed.ncbi.nlm.nih.gov/25733729/) | 2016 | Case Report | Human & Experimental Toxicology | Thrombolytic therapy in inferolateral MI following carbon monoxide poisoning. |
| [31020237](https://pubmed.ncbi.nlm.nih.gov/31020237/) | 2019 | Case Report | European Heart Journal Case Reports | Successful stent-retriever extraction of refractory thrombus from an ectatic coronary artery during primary angioplasty. |

---

## Germany Market Information

Tenecteplase currently has no marketing authorization on record in Germany (0 authorizations; market status: Not Marketed). No product-level licensing data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (key safety data and TFDA/BfArM label information are flagged as a **Blocking** data gap for the S1 safety review).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Coronary stenosis (adjunctive low-dose intracoronary tenecteplase during primary PCI) is the only candidate among the ten TxGNN predictions with actual clinical evidence — a completed Phase 2 RCT plus supportive cohort and RCT literature — reaching evidence level L2. However, this is an adjunctive procedural use with a narrow dose/route (low-dose intracoronary bolus) rather than a new systemic indication, and no head-to-head efficacy/outcome data exists yet for a formal "coronary stenosis" label.

**To proceed, the following is needed:**
- Official label/warnings data (TFDA or BfArM) to complete the S1 safety review — currently blocking
- Detailed mechanism of action documentation from DrugBank
- Dose-response and bleeding-risk safety data specific to low-dose intracoronary administration
- Drug-drug interaction data (currently not found)
- Formal exclusion of ranks 1–3 (STEMI ECG subtypes — mechanistically non-novel, no direct evidence) and ranks 6–10 (no mechanistic plausibility, likely embedding noise) from further repurposing consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

