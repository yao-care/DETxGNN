---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the drug-repurposing evaluation report template to convert this Evidence Pack into the required Markdown report. Note: this pack is a "multi" candidate file (7 predicted indications for aliskiren), so per the template's primary-indication rules I feature `predicted_indications[0]` in the Quick Overview/Title, and add one summary table covering all 7 candidates so the very different evidence quality across them (including a safety-relevant RCT signal) isn't lost.

---

# Aliskiren: From Hypertension to Pulmonary Hypertension Due to Lung Disease/Hypoxia

## One-Sentence Summary

> Aliskiren is a direct renin inhibitor originally used to treat essential hypertension. The TxGNN model's top-ranked prediction is **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia**, but this direction is currently supported only by **0 clinical trials** and **20 publications**, none of which specifically studied aliskiren, renin inhibition, or pulmonary hypertension. This Evidence Pack actually contains **7 predicted indications** for aliskiren with widely varying evidence quality — from a mechanistically direct but untested hypothesis (renovascular hypertension) to a well-studied RCT signal that points toward **harm rather than benefit** (cerebrovascular disease, via the ALTITUDE trial).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (essential hypertension) — general drug-class knowledge; no formal licensing text is available since the product is not marketed in Germany in this dataset |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.98% (rank 466 of full prediction list) |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Overview of All Predicted Indications in This Pack

This candidate pack (`TW-DB09026-multi`) contains 7 TxGNN-predicted indications for aliskiren. Evidence quality differs sharply between them and should be read together rather than in isolation:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.98% | L5 | S0 | Hold |
| 2 | Pulmonary hypertension with unclear multifactorial mechanism | 99.98% | L5 | S0 | Hold |
| 3 | Malignant hypertensive renal disease | 99.98% | L4 | S0 | Hold |
| 4 | Malignant renovascular hypertension | 99.98% | L3 | S1 | Research Question |
| 5 | Braddock syndrome | 99.97% | L5 | S0 | Hold |
| 6 | Chronic pulmonary heart disease (cor pulmonale) | 99.78% | L5 | S0 | Hold |
| 7 | Cerebrovascular disorder | 99.19% | **L1** | S1 | Hold — **RCT evidence shows harm, not benefit** |

Note that the raw TxGNN score alone is not discriminating here — all 7 candidates score above 99%. The real differentiator is the evidence review below, especially rank 7, where the strongest clinical trial evidence in the entire pack (Phase 3 RCT, ALTITUDE) points *against* repurposing rather than for it.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for aliskiren is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on the literature captured in this pack (e.g., PMID 17485026, "Aliskiren, the first renin inhibitor for treating hypertension"), aliskiren is a first-in-class **direct renin inhibitor**: it blocks the rate-limiting step of the renin-angiotensin-aldosterone system (RAAS), and its efficacy in essential hypertension is well established.

The 7 predicted indications above cluster around conditions in which RAAS overactivation is thought to play a role — renal, pulmonary vascular, and cerebrovascular pathology. The mechanistic plausibility, however, is far from uniform:

- **Most direct** (rank 4, malignant renovascular hypertension): renal-artery-stenosis-driven hypertension is pathophysiologically defined by excess renin secretion from the underperfused kidney, so a renin inhibitor targets the upstream driver directly. The one supporting reference (PMID 17485026) is drug-specific but also warns that *reactive* renin secretion may blunt aliskiren's long-term antihypertensive effect in exactly this setting.
- **Plausible but indirect** (rank 3, malignant hypertensive renal disease; rank 6, chronic pulmonary heart disease): RAAS activation is a recognized contributor to glomerular pressure injury and to right-heart volume overload, but the cited literature is not aliskiren-specific (a complement-pathway fibrosis study, and an ARNI heart-failure post-hoc analysis using a different drug class).
- **Weak/generic** (ranks 1–2, hypoxia-driven pulmonary hypertension): hypoxia-induced pulmonary vascular remodeling does involve RAAS signaling in some preclinical reports, so the hypothesis is not implausible in principle. However, all 20 retrieved publications are general hypoxia-biology papers (neurodegeneration, cognition, tumor metabolism, high-altitude physiology) — **none mention aliskiren, renin inhibitors, or pulmonary hypertension treatment**, so this link is currently speculative rather than evidenced.
- **Likely noise** (rank 5, Braddock syndrome): a CHARGE-like ciliopathy with no known RAAS/renin biology and zero supporting literature or trials — most plausibly a spurious knowledge-graph connection via a shared hypertension-comorbidity node.
- **Evidenced, but negative** (rank 7, cerebrovascular disorder): this is the one candidate with genuine Phase 2/3 RCT data (ALTITUDE trial and its post-hoc analyses). The trial was terminated early because aliskiren, when combined with ACE inhibitors or ARBs in diabetic patients with renal impairment, **increased** rates of stroke, hypotension, and hyperkalemia rather than providing cerebrovascular protection — despite favorable preclinical (rodent) neuroprotection data.

---

## Clinical Trial Evidence

Only two of the seven candidate indications have any registered trials.

**Chronic pulmonary heart disease (rank 6):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | Completed | 19 | Pharmacist-led, data-driven prescribing-safety QI program in primary care (Scotland). Grade C relevance — no direct link to aliskiren pharmacology or this indication; likely a low-relevance pipeline match. |

**Cerebrovascular disorder (rank 7):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01417104](https://clinicaltrials.gov/study/NCT01417104) | Phase 2/3 | **Terminated** | 71 | ALPINE trial: aliskiren vs. placebo for slowing atherosclerotic plaque progression in thoracic/abdominal aorta by MRI. Grade A relevance (drug- and mechanism-specific) but terminated well short of target enrollment — timing coincides with the 2011–2012 ALTITUDE safety signal that led Novartis to halt related aliskiren combination trials; termination reason should be verified directly. |
| [NCT01454583](https://clinicaltrials.gov/study/NCT01454583) | N/A | Completed | 15,337 | German 3A-Register: large real-world observational registry of RAS-inhibitor (including aliskiren) outpatient treatment patterns in hypertension. Grade B relevance — observational, not designed around cerebrovascular endpoints. |

For pulmonary hypertension (ranks 1–2), malignant hypertensive renal disease (rank 3), malignant renovascular hypertension (rank 4), and Braddock syndrome (rank 5): **currently no related clinical trials registered.**

---

## Literature Evidence

### Cerebrovascular disorder (rank 7) — strongest and most drug-specific evidence in this pack

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26523993](https://pubmed.ncbi.nlm.nih.gov/26523993/) | 2015 | RCT subgroup (ALTITUDE/AQUARIUS) | Atherosclerosis | Aliskiren's effect on coronary atheroma progression and MACE in diabetic vs. non-diabetic CAD patients; reinforces the diabetic-population harm signal. |
| [23418282](https://pubmed.ncbi.nlm.nih.gov/23418282/) | 2013 | RCT post-hoc safety analysis | J Renin Angiotensin Aldosterone Syst | Hypotension and ischemic stroke associated with aliskiren in ALTITUDE, proposed mechanism via Bezold-Jarisch reflex sensitization. |
| [26188211](https://pubmed.ncbi.nlm.nih.gov/26188211/) | 2015 | RCT post-hoc (ALTITUDE) | European Heart Journal | Mortality following a cardiovascular or renal event in T2DM patients in ALTITUDE — establishes the high-risk population where aliskiren + ACEi/ARB is harmful. |
| [24621979](https://pubmed.ncbi.nlm.nih.gov/24621979/) | 2013 | Clinical review/analysis | JACC: Heart Failure | Examines whether dual RAAS blockade (including aliskiren combinations) is associated with increased stroke risk. |
| [23541666](https://pubmed.ncbi.nlm.nih.gov/23541666/) | 2013 | Real-world database study | Canadian J Cardiology | Ontario administrative-data study found **no** increase in adverse events with aliskiren + ACEi/ARB in routine practice — offers a partially reassuring, contrasting real-world signal to the RCT findings. |
| [40013543](https://pubmed.ncbi.nlm.nih.gov/40013543/) | 2025 | Cochrane systematic review/meta-analysis | Cochrane Database Syst Rev | Renin inhibitors vs. ARBs for primary hypertension — comparable BP-lowering, favorable tolerability, but not focused on cerebrovascular outcomes. |
| [37439548](https://pubmed.ncbi.nlm.nih.gov/37439548/) | 2023 | Cochrane systematic review | Cochrane Database Syst Rev | First-line diuretics vs. other antihypertensive classes — general comparative-effectiveness context, not aliskiren-specific. |
| [23541659](https://pubmed.ncbi.nlm.nih.gov/23541659/) | 2013 | Review | Canadian J Cardiology | Combination treatment with aliskiren and RAAS blockers — "reassurance but with a note of caution," commentary anticipating the ALTITUDE findings. |
| [21859961](https://pubmed.ncbi.nlm.nih.gov/21859961/) | 2011 | Preclinical (mouse model) | Hypertension | Direct renin inhibition attenuated brain damage and cognitive impairment in chronic cerebral hypoperfusion mice — supportive mechanistic/preclinical signal, contradicted by later human RCT data. |
| [27180190](https://pubmed.ncbi.nlm.nih.gov/27180190/) | 2016 | Preclinical (mouse model) | Neurochemical Research | Aliskiren showed neuroprotective effects (PI3K/AKT/Bcl-2 pathway) in experimental ischemic stroke — again preclinical only. |

### Pulmonary hypertension owing to lung disease and/or hypoxia (rank 1) — non-drug-specific hypoxia biology literature

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | General review of hypoxia's role in brain aging and neurodegeneration; not aliskiren- or pulmonary-hypertension-specific. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Clinical and molecular mechanisms of hypoxia-induced cognitive impairment. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cellular Biochemistry | General hypoxia-mediated biological control across organ systems. |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumor hypoxia in oncology; unrelated to pulmonary vascular disease. |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Deubiquitinases and hypoxia signaling in cancer. |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics of North America | Mechanisms of hypoxemia (ventilation-perfusion mismatch, shunt, etc.) — background respiratory physiology only. |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | High-altitude hypobaric hypoxia and physiological adaptation. |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hypoxia's role in multiple sclerosis pathology. |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Preclinical | Advanced Science | ac4C/NAT10/HIF-1α feedback loop driving glycolysis in gastric cancer under hypoxia. |
| [24557798](https://pubmed.ncbi.nlm.nih.gov/24557798/) | 2014 | Editorial | J Applied Physiology | Brief editorial framing on hypoxia research ("translation in progress"); no abstract available. |

**None of these 10 (or the remaining 10 in the full retrieval set) discuss aliskiren, renin inhibition, or pulmonary hypertension treatment.** This is the key limitation behind the L5/Hold rating for rank 1–2.

### Malignant hypertensive renal disease (rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37919077](https://pubmed.ncbi.nlm.nih.gov/37919077/) | 2023 | Preclinical (mechanism study) | Frontiers in Bioscience | C3aR antagonism restores mitochondrial fatty-acid oxidation and reduces tubular profibrotic changes in renin-dependent hypertension — a complement-pathway mechanism study, not an aliskiren efficacy study. |

### Malignant renovascular hypertension (rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17485026](https://pubmed.ncbi.nlm.nih.gov/17485026/) | 2007 | Drug-specific pharmacology review | American Journal of Hypertension | Review of 6 clinical trials (>5,000 patients) — aliskiren is no more effective than ACEi/ARB/diuretics for BP lowering; warns that reactive renin secretion may limit long-term effectiveness, directly relevant to the renovascular-hypertension hypothesis. |

### Chronic pulmonary heart disease (rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | RCT post-hoc | JAMA Cardiology | Sacubitril/valsartan (ARNI — a different drug class) effect on all-cause hospitalization in heart failure (PARADIGM-HF/PARAGON-HF); not a renin-inhibitor study. |
| [17890152](https://pubmed.ncbi.nlm.nih.gov/17890152/) | 2007 | Conference review | European Journal of Heart Failure | ESC 2007 heart-failure trial roundup (3CPO, ALOFT, PROSPECT, statins); general background only. |

---

## Germany Market Information

Aliskiren is currently **not marketed in Germany** according to this dataset (`market_status: 未上市`, `total_licenses: 0`). No marketing authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information — the structured safety fields in this Evidence Pack (`key_warnings`, `contraindications`, `ddi`) are all marked as data gaps, and the TFDA/BfArM package insert has not yet been retrieved (see `DG001`, Blocking).

**⚠️ Important safety signal identified from literature evidence (not from the formal safety data fields above):** Multiple publications retrieved for the cerebrovascular-disorder candidate (rank 7) reference the **ALTITUDE trial**, a Phase 3 RCT that was **terminated early** because aliskiren, when combined with an ACE inhibitor or ARB in patients with type 2 diabetes and renal impairment, significantly increased rates of stroke, hypotension, and hyperkalemia (PMID 23418282, 26188211, 26523993). This is a well-documented, drug-specific harm signal and should be treated as a hard constraint on any repurposing work involving renal or cardiovascular comorbidity populations until the formal package insert warnings are retrieved and reviewed.

---

## Conclusion and Next Steps

**Decision: Hold** (top-ranked candidate, and program-level default pending further data)

**Rationale:**
- The featured top prediction (pulmonary hypertension owing to lung disease/hypoxia) has no aliskiren-specific clinical trial or literature support (L5) — the TxGNN score alone is not sufficient to advance it.
- Across all 7 candidates in this pack, only **malignant renovascular hypertension (rank 4)** has a mechanistically direct, drug-specific rationale and is rated **Research Question** rather than Hold — but even there, the literature itself cautions that reactive renin secretion may limit aliskiren's effectiveness.
- The candidate with the strongest clinical evidence, **cerebrovascular disorder (rank 7, L1)**, should **not** be pursued: its Phase 3 RCT evidence (ALTITUDE) shows increased stroke and renal harm in the relevant patient population, not benefit.
- A Blocking data gap exists (`DG001`): TFDA/BfArM package insert warnings and contraindications have not been retrieved, so no candidate can proceed past initial safety screening (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA/BfArM package insert (warnings, contraindications) — currently Blocking (`DG001`)
- Obtain confirmed mechanism-of-action data from DrugBank (`DG002`) to firm up the mechanistic rationale sections above
- If pursuing rank 4 (malignant renovascular hypertension) as a Research Question, commission a targeted literature/trial search specific to that indication (current evidence base is a single 2007 review)
- Verify the termination reason for NCT01417104 (ALPINE) to confirm whether it relates to the ALTITUDE safety signal
- Treat rank 7 (cerebrovascular disorder) as closed/Do-Not-Pursue pending any new evidence that overturns the ALTITUDE findings
- Disregard rank 2 (no evidence) and rank 5 (Braddock syndrome, biologically implausible) as likely knowledge-graph noise unless new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

