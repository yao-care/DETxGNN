---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 4
---

# Palbociclib
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

# Palbociclib: From HR+/HER2- Breast Cancer to Four Candidate Indications (Screening Stage)

## One-Sentence Summary

> Palbociclib is a CDK4/6 inhibitor whose original indication (HR+/HER2- metastatic breast cancer) is not recorded in this evidence pack but is confirmed repeatedly in the supporting literature.
> This screening round produced **four TxGNN-predicted indications**, but only one — **rheumatoid arthritis** — has any mechanistic or case-level human evidence (L4);
> the other three (hyperthyroidism, thrombotic disease, THRB-mutant thyroid hormone resistance) have either **no supporting evidence** or evidence pointing in the **wrong direction** (increased thromboembolic risk rather than benefit).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured fields (data gap); literature within this pack repeatedly confirms **HR+/HER2- metastatic breast cancer** as the approved use of CDK4/6 inhibitors including palbociclib |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Number of Candidate Indications Screened | 4 |
| Blocking Data Gap | TFDA label warnings/contraindications not yet retrieved (DG001) — **blocks entry into S1 safety review for any candidate** |
| Overall Recommended Decision | **Hold** |

### Candidate Indications at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Hyperthyroidism | 99.44% | L5 | S0 | Hold |
| 2 | Rheumatoid arthritis | 99.36% | L4 | S1 | Research Question |
| 3 | Thrombotic disease | 99.32% | L4 | S0 | Hold |
| 4 | Resistance to thyroid hormone (THRB mutation) | 99.30% | L5 | S0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). Based on the literature evidence collected within the pack itself, palbociclib is consistently described as a **CDK4/6 (cyclin-dependent kinase 4/6) inhibitor**, approved for HR+/HER2- metastatic breast cancer, acting by blocking cell-cycle progression from G1 to S phase.

**Rheumatoid arthritis (rank 2)** is the only candidate with a coherent mechanistic story: synovial fibroblast overgrowth in RA is cell-cycle dependent, and CDK6 specifically has been shown to drive synovial hyperplasia in arthritic mouse models (PMID 39940918). A preclinical study combining CDK inhibition with cytokine blockade showed enhanced anti-arthritic effect without added immunosuppression (PMID 25165034), and a single human case report describes RA improvement in a breast cancer patient treated with palbociclib (PMID 33587021). This is biologically plausible but rests on one case report plus preclinical data — no prospective human trial exists.

**Thrombotic disease (rank 3)** is mechanistically **not supportive of repurposing**. The literature attached to this candidate is dominated by FAERS pharmacovigilance disproportionality analyses and real-world cohort/case data showing CDK4/6 inhibitors (including palbociclib) are **associated with increased thromboembolic risk**, not therapeutic benefit. The two attached clinical trials are unrelated to thrombosis as a treatment target (one is an oncology combination study, the other a withdrawn COVID-19 safety trial). This candidate should be read as a **safety signal**, not a repurposing opportunity.

**Hyperthyroidism (rank 1)** and **THRB-mutant thyroid hormone resistance (rank 4)** have **zero supporting trials or literature**. Both are flagged in the evidence pack itself as likely graph-embedding noise with no known biological rationale connecting CDK4/6 inhibition to thyroid receptor pathways.

---

## Clinical Trial Evidence

### Rheumatoid Arthritis
Currently no related clinical trials registered.

### Thrombotic Disease

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05468697](https://clinicaltrials.gov/study/NCT05468697) | Phase 1/2 | Active, not recruiting | 60 | Belzutifan + palbociclib vs. belzutifan alone in advanced renal cell carcinoma — an oncology combination-dosing study, not a thrombosis treatment trial (relevance grade C) |
| [NCT05371275](https://clinicaltrials.gov/study/NCT05371275) | Phase 2 | Withdrawn (0 enrolled) | 0 | Planned safety study of palbociclib in hospitalized moderate COVID-19 to prevent thromboinflammation; withdrawn before enrollment (relevance grade C) |

### Hyperthyroidism / Resistance to Thyroid Hormone (THRB)
Currently no related clinical trials registered.

---

## Literature Evidence

### Rheumatoid Arthritis

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case Report | Mod Rheumatol Case Rep | RA symptom improvement in a breast cancer patient treated with palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Review | The Oncologist | CDK4/6 inhibitors may influence immune function, potentially triggering or modulating autoimmune disease in HR+/HER2- breast cancer patients |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (animal model) | Ann Rheum Dis | CDK inhibition combined with cytokine blockade enhanced anti-arthritic effect in animal models without increasing immunosuppression |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical/Mechanistic (animal model) | Int J Mol Sci | CDK6-dependent (CDK4-independent) synovial hyperplasia identified in arthritic mice; notes palbociclib-induced myelosuppression in preclinical studies |

### Thrombotic Disease

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39123221](https://pubmed.ncbi.nlm.nih.gov/39123221/) | 2024 | Pharmacovigilance (FAERS) | BMC Pharmacol Toxicol | Comparative adverse event analysis across CDK4/6 inhibitors (palbociclib, abemaciclib, ribociclib) via FDA FAERS |
| [39083396](https://pubmed.ncbi.nlm.nih.gov/39083396/) | 2025 | Pharmacovigilance (FAERS) | Expert Opin Drug Saf | Disproportionality analysis of CDK4/6 inhibitor adverse events in FAERS |
| [41496429](https://pubmed.ncbi.nlm.nih.gov/41496429/) | 2026 | Pharmacovigilance (FAERS) | Breast | Age-stratified toxicity patterns of CDK4/6 inhibitors in older women, FAERS analysis |
| [35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/) | 2022 | Cohort | Cancer Manag Res | Real-world thromboembolic event data in HR+/HER2- metastatic breast cancer patients on ribociclib-based regimens |
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Pharmacovigilance + Systematic Review | Expert Opin Drug Saf | Thromboembolism profiles associated with CDK4/6 inhibitors — real-world pharmacovigilance plus systematic review |
| [38390439](https://pubmed.ncbi.nlm.nih.gov/38390439/) | 2024 | Case Report (ribociclib) | SAGE Open Med Case Rep | Cerebral venous sinus thrombosis case in a patient on ribociclib |
| [37994878](https://pubmed.ncbi.nlm.nih.gov/37994878/) | 2023 | Review | Expert Opin Drug Saf | Review of interstitial lung disease and other adverse events with CDK4/6 inhibitors |
| [39302147](https://pubmed.ncbi.nlm.nih.gov/39302147/) | 2025 | Mechanistic | Cardiovasc Res | dsDNA enhances platelet activation and thrombosis via cGAS — general platelet biology, not palbociclib-specific |
| [27098250](https://pubmed.ncbi.nlm.nih.gov/27098250/) | 2016 | Preclinical (animal model) | Circ Cardiovasc Genet | CDKN2A-deficiency and megakaryopoiesis/platelet activity in a hypercholesterolemic mouse model |
| [40623899](https://pubmed.ncbi.nlm.nih.gov/40623899/) | 2025 | Guidance (largely irrelevant) | Zhonghua Xue Ye Xue Za Zhi | Chinese hemophilia B gene-therapy guidance; palbociclib mentioned only in passing regarding recent China market approval |

### Hyperthyroidism / Resistance to Thyroid Hormone (THRB)
Currently no related literature available.

---

## Germany Market Information

Palbociclib currently has **no marketing authorization in Germany** (0 licenses on record), so no product-level table is available.

---

## Cytotoxicity

Palbociclib is an antineoplastic agent (approved use in HR+/HER2- metastatic breast cancer per literature within this pack; targeted small-molecule CDK4/6 inhibitor class).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Reported in preclinical literature (PMID 39940918); please refer to the package insert for graded frequency data (not available in this pack) |
| Emetogenicity Classification | Not specified in this evidence pack; please refer to the package insert |
| Monitoring Items | CBC with differential (myelosuppression); given the pharmacovigilance signal above, monitoring for thromboembolic symptoms is also advisable |
| Handling Protection | Cytotoxic/hazardous drug handling precautions should be followed pending confirmation via package insert |

---

## Safety Considerations

Formal safety data (key warnings, contraindications, DDI) are not available in this evidence pack — please refer to the package insert for safety information.

- **Evidence-derived signal (not from formal label data):** Multiple independent FAERS pharmacovigilance analyses and a real-world cohort study within the literature evidence (PMID 39123221, 39083396, 41496429, 36794339, 35300061) consistently associate CDK4/6 inhibitors, including palbociclib, with an **increased risk of thromboembolic events**. This should be treated as a safety signal requiring confirmation against the official label, not as supporting evidence for a thrombotic-disease indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Of the four TxGNN-predicted indications, three (hyperthyroidism, thrombotic disease, THRB-mutant thyroid hormone resistance) lack any indication-specific supportive evidence, and the thrombotic-disease candidate is contradicted by pharmacovigilance data pointing to increased risk rather than benefit. The remaining candidate, rheumatoid arthritis, has only preclinical and single-case-report support (L4) and has not entered controlled human testing. In addition, a **blocking data gap** (DG001: TFDA label warnings/contraindications not retrieved) prevents any candidate from formally entering S1 safety review.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA label warnings and contraindications (resolves blocking gap DG001)
- Confirm DrugBank mechanism-of-action record (DG002)
- For the rheumatoid arthritis hypothesis: identify or design a prospective controlled human trial before advancing past the "Research Question" stage
- Formally assess baseline thromboembolic risk against the official label before considering any further indication work, given the pharmacovigilance signal identified
- Deprioritize hyperthyroidism and THRB-mutant thyroid hormone resistance absent new supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

