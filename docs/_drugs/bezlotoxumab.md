---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: From Anti-*C. difficile* Toxin B Therapy to Acute Female Pelvic Peritonitis (Low-Confidence Prediction)

## One-Sentence Summary

Bezlotoxumab is a monoclonal antibody that neutralizes *Clostridioides difficile* toxin B; no approved indication or detailed mechanism-of-action data is recorded in this evidence pack, and the drug is not marketed in Taiwan.
The TxGNN model's top prediction is **acute female pelvic peritonitis**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states there is no known biological link between the drug's target and this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (drug not marketed in Taiwan) |
| Predicted New Indication | Acute Female Pelvic Peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa is a recorded data gap). Based on the model's own repurposing rationale, bezlotoxumab is a monoclonal antibody directed against *C. difficile* toxin B, used to neutralize this specific bacterial toxin.

The rationale text accompanying this prediction explicitly states there is **no known mechanistic connection** between toxin-B neutralization and acute female pelvic peritonitis, which is typically a polymicrobial/mixed bacterial infection unrelated to *C. difficile* toxin pathology. This pattern repeats across all ten top-ranked candidates in this evidence pack (ectopic pregnancy, tubal/uterine pathology, spinal stenosis, vascular and lymphatic conditions) — none have a stated biological rationale, and all are flagged internally as embedding-similarity outputs without mechanistic support.

Given this, the prediction should be treated as a pure model-similarity signal (L5) rather than a mechanistically grounded repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Bezlotoxumab is not currently marketed in Taiwan; no product authorizations are on record.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (and all nine runners-up) has no clinical trial or literature support (L5, model prediction only), and the pack's own mechanistic rationale explicitly states no known biological link exists between bezlotoxumab's target and acute female pelvic peritonitis.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a **blocking** gap that prevents entry into S1 safety pre-screening
- Detailed mechanism of action (MOA) data from DrugBank to properly evaluate mechanistic plausibility
- Independent literature or preclinical evidence specifically linking anti-toxin-B antibody activity to gynecological/pelvic infection pathology before this candidate can advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

