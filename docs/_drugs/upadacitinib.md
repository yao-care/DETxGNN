---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Upadacitinib: From Autoimmune/Inflammatory Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Upadacitinib is a selective JAK1 inhibitor originally developed for autoimmune and inflammatory conditions; its detailed original indication and mechanism-of-action data are not yet available in this evidence pack. The TxGNN model assigns a high similarity score to **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital skeletal-ocular malformation syndrome, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic analysis flags it as likely model noise rather than a biologically plausible hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (JAK1 inhibitor class, typically autoimmune/inflammatory disease) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` is unpopulated). Based on the repurposing rationale provided, upadacitinib is a selective JAK1 inhibitor that modulates cytokine signaling (IL-6, IFN, IL-2 family, etc.), consistent with its known use in autoimmune/inflammatory disease.

The predicted indication — colobomatous microphthalmia-rhizomelic dysplasia syndrome — is a rare congenital disorder driven by embryonic developmental gene defects, not by chronic inflammatory or JAK-STAT-mediated pathology. The evidence pack's own mechanistic assessment states there is **no known biological link** between JAK1 inhibition and this structural developmental syndrome, and attributes the high TxGNN score to graph-embedding similarity artifacts rather than a genuine pharmacological hypothesis.

A second candidate, brachydactyly-syndactyly syndrome (score 99.58%, rank 5278), shows the same pattern: a limb-development disorder (typically HOX gene / BMP-Hedgehog pathway related) with no plausible connection to JAK1 inhibition, and no supporting trials or literature. Both top-ranked predictions in this batch should be treated as low-confidence model artifacts rather than actionable repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Upadacitinib currently holds **no marketing authorization** on record in this jurisdiction (market status: Not Marketed, 0 authorizations). No product/license data available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and DDI data are currently missing — see `DG001`, a Blocking-severity gap that prevents S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting clinical trials or literature (Evidence Level L5), and the evidence pack's own mechanistic analysis assesses the drug-disease link as biologically implausible, likely reflecting embedding-similarity noise rather than a genuine signal. Combined with a Blocking-severity safety data gap (TFDA label unavailable) and missing MOA/original-indication data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) to resolve DG001 (Blocking)
- Confirmed original MOA and approved indication(s) via DrugBank/regulatory source (DG002)
- Independent mechanistic or preclinical rationale linking JAK1 inhibition to this syndrome before allocating further review resources
- If no such rationale emerges, deprioritize both rank-1 and rank-2 candidates as low-value predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

