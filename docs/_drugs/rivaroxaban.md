---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation Therapy to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a Factor Xa inhibitor anticoagulant, referenced in the evidence pack primarily for venous thromboembolism (DVT/PE) and atrial fibrillation-related anticoagulation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this prediction is currently supported by **0 directly relevant clinical trials** and **4 publications, none of which address RA treatment itself** — the literature instead covers VTE management, thrombin generation assays, DOAC adherence, and a case report where RA was only an incidental patient characteristic.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (data gap — see DG001/DG002); drug class context in the evidence pack indicates anticoagulant use (e.g., DVT/PE treatment per referenced trial NCT00786422) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on the mechanistic notes embedded in the evidence pack, rivaroxaban is a direct Factor Xa inhibitor used for anticoagulation. It has no known anti-inflammatory or immunomodulatory activity that would plausibly intervene in the synovitis or autoimmune pathology underlying rheumatoid arthritis.

The retrieved literature does not support a treatment relationship: it consists of a VTE management review, a methodological paper on thrombin generation assays in autoimmune disease, a DOAC adherence comparison in atrial fibrillation, and a perioperative case report in which RA was merely a comorbidity of the patient on oral corticosteroids — none evaluate rivaroxaban as a therapy for RA itself. The most likely explanation for this TxGNN prediction is an indirect network association (RA patients carry elevated thrombotic risk and may require anticoagulation), rather than a genuine disease-modifying mechanism.

Given the absence of a plausible mechanistic link, target-relevant trials, or supportive literature, this prediction should be treated as exploratory only and not advanced without new mechanistic evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Compared adherence rates between rivaroxaban and apixaban in non-valvular AF patients; not related to RA treatment. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of DVT/PE diagnosis and treatment; no RA content. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | Discusses thrombin generation assay as a tool to assess hypercoagulability in autoimmune diseases (e.g., antiphospholipid syndrome); does not evaluate rivaroxaban for RA. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case Report | Cureus | Case of thromboembolic stroke in an 88-year-old AF patient with RA on oral steroids; RA is an incidental comorbidity, not a treatment target. |

## Germany Market Information

No marketing authorization records are available for rivaroxaban in this dataset (market status: Not Marketed, 0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are currently unavailable — see data gap DG001, classified as Blocking, which prevents S1 safety screening.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted RA indication has no plausible mechanistic basis, no supporting clinical trials, and literature that is entirely off-target; evidence level is L5 (model prediction only). This is consistent with the other three TxGNN-predicted indications for rivaroxaban in this evidence pack (gout, HIV infectious disease, brachydactyly-syndactyly syndrome), all of which are also scored Hold with L4–L5 evidence and no mechanistically relevant support.

**To proceed, the following is needed:**
- TFDA/BfArM label data (warnings, contraindications) to close the Blocking data gap (DG001) before any S1 safety screening can occur
- DrugBank-sourced mechanism of action data (DG002) to properly evaluate mechanistic plausibility
- If pursuing the RA hypothesis further: preclinical or mechanistic studies directly testing Factor Xa inhibition in RA-relevant pathways (e.g., synovial inflammation models), since current literature only touches on RA as an incidental comorbidity
- Formal original indication and licensing data, currently absent from the registry, to properly frame the repurposing rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

