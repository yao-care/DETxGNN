---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is an anti-BAFF/BLyS monoclonal antibody originally used to treat Systemic Lupus Erythematosus (SLE) by suppressing B-cell survival and autoantibody production.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but this direction is currently supported by only **1 clinical trial** (mechanistically unrelated) and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic Lupus Erythematosus (SLE) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is not available for belimumab in this evidence pack. Based on the mechanistic rationale accompanying the predictions, belimumab is known to act as an anti-BAFF/BLyS monoclonal antibody that inhibits B-cell survival and reduces autoantibody generation, and on this basis it is approved for SLE.

Primary release disorder of platelets is a hereditary defect in platelet granule secretion — a structural/functional platelet abnormality, not a B-cell- or antibody-mediated disease. There is no established biological pathway connecting BAFF/B-cell inhibition to platelet granule release. The TxGNN model's high score for this indication is therefore most plausibly a knowledge-graph association artifact rather than a genuine mechanism-driven hypothesis.

Notably, among the six indications predicted for belimumab, **fetal and neonatal alloimmune thrombocytopenia (rank 4)** has a comparatively more plausible mechanistic rationale, since it is an antibody-mediated condition — but it likewise has no supporting clinical or literature evidence at this time. All six predictions remain at evidence level L5.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Study of belimumab in PLA2R-antibody-positive idiopathic membranous glomerulonephropathy — **not related to platelet disorders**; database indication mismatch, graded C (non-supportive) |

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Belimumab is not marketed in Germany under this evidence pack (0 authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, the only associated clinical trial addresses an unrelated indication, no supporting literature exists, and the proposed mechanism (BAFF/B-cell inhibition) has no established link to platelet granule release disorders. The evidence base is insufficient to justify further evaluation.

**To proceed, the following is needed:**
- Confirmed MOA and DDI/contraindication data from DrugBank/manufacturer (currently flagged as Blocking/High data gaps)
- Preclinical or mechanistic studies directly linking BAFF/B-cell pathways to platelet granule secretion defects
- Real disease-matched clinical trials or case reports in platelet release disorder populations
- If pursuing an alternative candidate, prioritize re-evaluation of **fetal and neonatal alloimmune thrombocytopenia**, which has a more coherent (though still unproven) mechanistic hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

