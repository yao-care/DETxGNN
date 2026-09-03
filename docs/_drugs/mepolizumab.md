---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Mepolizumab: From Original Indication (Not Specified) to Thrombocytopenia due to Immune Destruction

## One-Sentence Summary

> Mepolizumab is an anti-IL-5 monoclonal antibody; its original approved indication is not documented in this evidence pack (data gap), though supporting literature repeatedly references its use in hypereosinophilic syndrome.
> The TxGNN model predicts it may be effective for **Thrombocytopenia due to Immune Destruction**,
> but currently only **1 case report** supports this direction, with **no clinical trials** registered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap) |
| Predicted New Indication | Thrombocytopenia due to Immune Destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for mepolizumab is not available in this evidence pack (marked as data gap). Based on the mechanistic notes accompanying this prediction, mepolizumab is an anti-IL-5 monoclonal antibody that suppresses eosinophil production and activation — a mechanism that has no established, direct molecular link to immune-mediated platelet destruction (e.g., Fc-receptor-mediated macrophage clearance or anti-platelet antibody pathways).

The only supporting literature is a single case report describing a patient with steroid-resistant hypereosinophilic syndrome (HES) and concomitant thrombotic microangiopathy, in whom platelet counts improved after mepolizumab treatment. This improvement is best interpreted as a **secondary effect** of resolving the underlying hypereosinophilic process, rather than evidence that mepolizumab acts directly on immune platelet destruction pathways.

Given this, the high TxGNN score likely reflects a shared knowledge-graph neighborhood (HES and thrombocytopenia frequently co-occur as comorbid entities) rather than genuine mechanistic specificity. This prediction should be treated as hypothesis-generating only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | Resolution of steroid-resistant hypereosinophilic immune diathesis with mepolizumab, with concomitant improvement of a mixed thrombotic microangiopathy; platelet improvement appears secondary to eosinophil suppression rather than a direct antiplatelet mechanism. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between mepolizumab's IL-5 inhibition and immune-mediated platelet destruction is weak and indirect, and the evidence base consists of a single case report with no supporting clinical trials — insufficient to justify advancing past preliminary screening. In addition, the missing TFDA label/warning data (DG001, Blocking) independently prevents progression to the S1 safety evaluation stage regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA-approved label (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Dedicated preclinical or mechanistic studies directly testing IL-5/eosinophil pathways in immune thrombocytopenia, rather than incidental case-report findings
- If pursued further, prospective clinical evidence (even small pilot studies) specifically in immune thrombocytopenic populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

