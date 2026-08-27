---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# EPTIFIBATIDE: From Acute Coronary Syndrome to Hemoglobinopathy (Sickle Cell Disease)

> **Note on indication selection:** This Evidence Pack (`TW-DB00063-multi`) contains 10 TxGNN-predicted indications for eptifibatide. The #1-ranked prediction by raw score (**rheumatoid arthritis**, 99.99%) has **zero clinical trials, zero literature, and an unfilled ("pending") rationale** — it is an unvalidated model output only. By contrast, rank #7 (**hemoglobinopathy / sickle cell disease**) is the only prediction in this pack with a completed evidence review (1 clinical trial + 4 publications, evidence level L2, decision stage S1). To make this report actually useful for decision-making, it is built around that candidate. All 10 predictions — including rheumatoid arthritis — are listed for transparency in the "Other TxGNN-Predicted Indications" section below.

---

## One-Sentence Summary

Eptifibatide is a GPIIb/IIIa (αIIbβ3) platelet receptor antagonist; based on the literature contained in this evidence pack, it is established for use in **acute coronary syndrome (ACS)**.
The TxGNN model predicts it may also be effective for **hemoglobinopathy (sickle cell disease)**, and — unlike the other 9 predictions in this pack — this direction is backed by **1 terminated Phase 1/2 clinical trial** and **4 publications**, including two studies that directly tested eptifibatide in sickle cell disease patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in structured regulatory data (drug is not marketed; 0 licenses). Literature in this pack indicates established use in **acute coronary syndrome (ACS)** as a GPIIb/IIIa antagonist. |
| Predicted New Indication | Hemoglobinopathy (sickle cell disease spectrum) |
| TxGNN Prediction Score | 99.98% (rank 485 in model output) |
| Evidence Level | **L2** (per pipeline scoring — see caveat below) |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

**Caveat on Evidence Level:** the sole trial (NCT00834899) was Phase 1/2 but **Terminated** with only 13 of a planned larger cohort enrolled, and the earliest human study (PMID 17916103) tested only 4 patients. Per the formal rule set (L2 = "1 completed Phase 2/3 RCT"), this evidence is better described as *preliminary/early-phase* rather than a fully completed confirmatory trial — the L2 label reflects that real human testing exists, not that it is conclusive.

---

## Why is This Prediction Reasonable?

Eptifibatide is a synthetic cyclic heptapeptide that antagonizes the platelet αIIbβ3 (GPIIb/IIIa) receptor, blocking the final common pathway of platelet aggregation. This mechanism is well established in acute coronary syndrome, where inhibiting platelet-mediated thrombus formation reduces ischemic complications during and after percutaneous coronary intervention.

Sickle cell disease (and the broader hemoglobinopathy spectrum) shares a pathophysiological feature with ACS: vaso-occlusion. In sickle cell disease, painful crises are driven in part by abnormal platelet activation, platelet-leukocyte-endothelial interactions, and CD40 ligand release, which together promote microvascular occlusion and inflammation — a process mechanistically analogous to the platelet-driven thrombosis eptifibatide is designed to block in ACS. This shared mechanism is the rationale investigators used to test eptifibatide directly in sickle cell patients, rather than a purely computational inference.

Because this exact hypothesis has already been tested in humans (Phase 1 pharmacodynamic study, a pilot efficacy trial, and a terminated Phase 1/2 RCT), this is a case where TxGNN's prediction converges with pre-existing, real clinical investigation — strengthening confidence relative to the other 9 predictions in this pack, all of which are pure graph-based inferences with no clinical follow-up.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00834899](https://clinicaltrials.gov/study/NCT00834899) | Phase 1/2 | Terminated | 13 | Randomized, double-blind, placebo-controlled study evaluating safety of eptifibatide for acute pain episodes in sickle cell disease. Hypothesis: platelet activation and resultant inflammation contribute to vaso-occlusive crises. Terminated early with only 13 of the planned cohort enrolled, indicating feasibility/recruitment challenges. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/) | 2007 | Phase 1 trial | British Journal of Haematology | First human test of eptifibatide in sickle cell anaemia (4 patients, non-crisis/steady-state). Rationale: platelet reactivity and CD40 ligand release in SCD parallel ACS pathophysiology; safety and pharmacodynamic data were obtained following infusion. |
| [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/) | 2013 | Pilot clinical study | Thrombosis Research | Pilot study of eptifibatide (αIIbβ3 antagonist) for treatment of acute pain episodes in SCD, evaluating safety and efficacy; contribution of platelet activation to SCD pathogenesis remained uncertain going in. |
| [29322543](https://pubmed.ncbi.nlm.nih.gov/29322543/) | 2018 | Clinical sub-analysis | American Journal of Hematology | Companion analysis examining the effect of eptifibatide on inflammatory markers during acute pain episodes in SCD (linked to the pilot trial above). |
| [22156199](https://pubmed.ncbi.nlm.nih.gov/22156199/) | 2012 | In vitro / microfluidic model | The Journal of Clinical Investigation | Developed an "endothelialized" microfluidic microvasculature model recapitulating microvascular occlusion and thrombosis seen in SCD and hemolytic uremic syndrome. Supports the underlying mechanistic rationale but does not test eptifibatide directly. |

---

## Germany Market Information

Eptifibatide currently has **no marketing authorization on file** for this market (未上市 / Not Marketed, 0 licenses recorded). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were retrievable for this evidence pack — this is flagged as a **Blocking-severity data gap (DG001)** in the source metadata, meaning this candidate **cannot proceed to formal S1 safety evaluation** until TFDA/BfArM package insert data is obtained and parsed.

---

## Other TxGNN-Predicted Indications for This Drug

For transparency, the remaining 9 predictions in this multi-indication evidence pack are summarized below (all substantially lower in evidence maturity than hemoglobinopathy):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Rheumatoid arthritis | 99.99% | L5 (no trials/literature; rationale unfilled) | Pending |
| 2 | Hereditary persistence of fetal hemoglobin–sickle cell disease syndrome | 99.98% | L5 | Hold |
| 3 | Sickle cell–hemoglobin C disease syndrome | 99.98% | L4 (1 tangential ACS bleeding-risk paper, not disease-specific) | Hold |
| 4 | Sickle cell–hemoglobin E disease syndrome | 99.98% | L5 | Hold |
| 5 | Sickle cell–beta-thalassemia disease syndrome | 99.98% | L5 | Hold |
| 6 | Sickle cell–hemoglobin D disease syndrome | 99.98% | L5 | Hold |
| **7** | **Hemoglobinopathy (this report)** | **99.98%** | **L2** | **Research Question / Hold** |
| 8 | Female breast carcinoma | 99.97% | L4 (in vitro pro-apoptotic effect on MCF-7 cells; no in vivo/clinical data) | Research Question |
| 9 | Beta-thalassemia with other manifestations | 99.97% | L5 | Hold |
| 10 | Partial deletion of the short arm of chromosome 16 | 99.96% | L5 (mechanistic link considered weak — likely a genomic-proximity artifact, not a pharmacological one) | Hold |

Notably, all 10 scores cluster within a narrow 99.96%–99.99% band, so TxGNN's raw ranking should not be read as a meaningful ordering of clinical plausibility — the evidence level differences (L2 vs. L4 vs. L5) are the more decision-relevant signal here.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hemoglobinopathy/sickle cell disease is the only prediction in this pack supported by actual human testing (a Phase 1 pharmacodynamic study and a pilot efficacy trial), but the confirmatory RCT (NCT00834899) was terminated early with a small cohort, and a Blocking-severity data gap (missing TFDA/BfArM label and safety data, DG001) prevents this candidate from entering formal safety evaluation regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the TFDA/BfArM package insert (warnings, contraindications, DDI) — currently blocking
- Resolve DG002: obtain detailed mechanism of action data from DrugBank to strengthen the mechanistic-link analysis
- Determine why NCT00834899 was terminated (recruitment, safety signal, or sponsor decision) before considering any renewed trial
- If pursuing further research, prioritize hemoglobinopathy/sickle cell disease over the other 9 predictions, given it is the only one with real prior human data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

