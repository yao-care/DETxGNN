---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Hypercholesterolemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

> Alirocumab is a PCSK9-inhibiting monoclonal antibody originally developed for hypercholesterolemia and cardiovascular risk reduction. Among 10 TxGNN-predicted indications screened for this drug, **Cholesterol Catabolic Process Disease** stands out as the only candidate with meaningful supporting evidence — the other 9 candidates (e.g. X-linked ichthyosis, dappled diaphyseal dysplasia, neutral lipid storage disease) had no mechanistic plausibility and no clinical or literature evidence, and are held. This candidate is supported by **1 completed Phase 3 trial** and **19 relevant publications**, several of which report data from alirocumab's own pivotal outcomes trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / Atherosclerotic Cardiovascular Disease (ASCVD) risk reduction *(general drug-class indication; Germany-specific license text unavailable — see Market Information below)* |
| Predicted New Indication | Cholesterol Catabolic Process Disease |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: This candidate was selected from 10 TxGNN-predicted indications as the only one reaching decision stage S3. The remaining 9 candidates (all L5, decision stage S0) had no clinical trials, no literature, and no plausible mechanistic link to the PCSK9/LDL pathway — they are excluded from further evaluation below and recommended for Hold.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap requiring DrugBank API lookup). Based on general pharmacological knowledge, however, alirocumab is a human monoclonal antibody that inhibits PCSK9 (proprotein convertase subtilisin/kexin type 9), preventing PCSK9 from binding to and degrading hepatic LDL receptors. This increases LDL receptor recycling and availability on the hepatocyte surface, thereby enhancing clearance of circulating LDL cholesterol.

"Cholesterol catabolic process disease" broadly corresponds to disorders of cholesterol clearance and metabolism — including familial hypercholesterolemia (FH) and ASCVD-related dyslipidemia — a disease category mechanistically identical to alirocumab's established core indication. This is not a distant repurposing hypothesis; it sits at the center of PCSK9-inhibitor pharmacology.

The mechanistic link is strong because the LDL receptor upregulation pathway targeted by alirocumab directly governs cholesterol catabolism/clearance. This is reinforced by the fact that alirocumab already has proven, large-scale outcomes evidence (ODYSSEY OUTCOMES, N=18,924, and its multiple post-hoc analyses) in populations defined by disordered cholesterol clearance — even though this specific trial registry entry is not separately listed in the clinical trial evidence table below, it is referenced repeatedly in the supporting literature (PMIDs 38658193, 39913634) and is the basis for the L1 evidence assignment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | EPIC-HIV: evaluated PCSK9 inhibition (alirocumab-class) for cardiovascular risk in treated HIV infection, using noninvasive imaging to assess plaque and vascular inflammation outcomes relevant to cholesterol clearance |

*Additional supporting Phase 3 evidence: the ODYSSEY OUTCOMES cardiovascular outcomes trial (alirocumab, completed, N=18,924) is not independently registered in this evidence pack's clinical trial set but is referenced through its post-hoc publications below.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Post-hoc RCT Analysis | Eur Heart J Cardiovasc Pharmacother | 47,296 patient-years of alirocumab safety data from ODYSSEY OUTCOMES; confirms sustained LDL-C lowering and reduced ischemic events with an acceptable long-term safety profile |
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | Post-hoc RCT Analysis | Diabetes Care | ODYSSEY OUTCOMES post-hoc analysis: lowering Lp(a) and LDL-C with alirocumab was not associated with increased risk of new-onset diabetes |
| [29526502](https://pubmed.ncbi.nlm.nih.gov/29526502/) | 2018 | Clinical Study | Kidney International | Alirocumab retained LDL-C-lowering efficacy and an acceptable safety profile in patients with chronic kidney disease and impaired renal function |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Review | Pharmacology & Therapeutics | Reviews alirocumab and evolocumab (extracellular PCSK9-binding mAbs) versus intracellular-acting agents like inclisiran, framing mechanism-based differences relevant to cholesterol clearance disorders |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduction and Targeted Therapy | Comprehensive review of PCSK9 biology and therapeutic targeting, extending beyond cardiovascular disease to broader lipid metabolism disorders |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Current Opinion in Lipidology | Update on PCSK9-directed therapies confirming that antibody inhibition (alirocumab) markedly reduces LDL cholesterol and cardiovascular risk |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Reviews novel LDL-C-lowering pharmacotherapies, including PCSK9 inhibitors, for homozygous familial hypercholesterolemia — a core cholesterol-catabolism disorder |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Literature analysis of familial hypercholesterolemia diagnostics and treatment, including PCSK9-targeted therapy as a key management pathway |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review | Kardiologia Polska | Reviews evidence for PCSK9 inhibitors' effect on lipid parameters and reduction in cardiovascular events |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review | International Journal of Molecular Sciences | Broad review of dyslipidemia treatment approaches, situating PCSK9 inhibition within current LDL-C-lowering strategy |

*9 additional publications in the evidence pack (general PCSK9-inhibitor reviews and safety literature) were not included above to keep the table to the 10 most relevant entries.*

---

## Germany Market Information

Alirocumab is not currently marketed in Germany — the evidence pack lists 0 active authorizations and no license records to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. *(No key warnings, contraindications, or drug interaction data are currently available in this evidence pack; DG001 — TFDA/BfArM package insert warnings and contraindications — is flagged as a Blocking data gap that must be resolved before any safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication "Cholesterol Catabolic Process Disease" is mechanistically well-aligned with alirocumab's established PCSK9-inhibition/LDL-receptor pathway, and is supported by one completed Phase 3 trial plus consistent literature — including post-hoc data from alirocumab's own large outcomes trial (ODYSSEY OUTCOMES). However, the disease label itself is broad and non-standard (not a precise clinical diagnosis), and this drug is not yet marketed in Germany, so a guarded, evidence-gathering pathway is appropriate rather than an unconditional Go. The 9 other TxGNN-predicted candidates for this drug lack any clinical or mechanistic support and should remain on Hold.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/BfArM package insert warnings, precautions, and contraindications before any safety pre-assessment (S1) can begin
- Resolve DG002 (High): confirm detailed mechanism of action via DrugBank API to strengthen the mechanistic rationale
- Clarify the precise clinical/ICD mapping of "cholesterol catabolic process disease" against recognized diagnostic categories (e.g. FH, ASCVD dyslipidemia) to define an actionable indication scope
- Assess whether the ODYSSEY OUTCOMES trial data (referenced only via literature in this pack) can be formally incorporated as a second completed Phase 3 trial in the evidence registry
- Evaluate German/EU market entry pathway given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

