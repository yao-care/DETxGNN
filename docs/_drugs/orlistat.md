---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Orlistat: From Unspecified Original Indication to Hypervitaminosis

## One-Sentence Summary

Orlistat's original approved indication is not documented in the current evidence pack, and its mechanism of action (MOA) is flagged as a high-severity data gap pending DrugBank verification. The TxGNN model predicts a possible application in **Hypervitaminosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on a theoretical, inverse-mechanism rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% (rank #6553) |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Orlistat's formal mechanism of action is not yet confirmed in this evidence pack (flagged as a High-severity data gap, DG002, pending DrugBank API verification). However, the repurposing rationale attached to this prediction describes Orlistat as a gastrointestinal lipase inhibitor that blocks hydrolysis of dietary triglycerides, thereby reducing intestinal fat absorption.

A well-known consequence of this mechanism — clinically treated as a side effect requiring supplementation — is reduced absorption of fat-soluble vitamins (A, D, E, K). The TxGNN prediction essentially inverts this known effect: if Orlistat reduces fat-soluble vitamin uptake, it could theoretically be repurposed to lower excess absorption in patients with hypervitaminosis A/D/E/K.

This is a mechanistically plausible hypothesis, not an evidence-backed therapeutic use. It has not been tested in any clinical trial or supported by any literature to date, and the underlying MOA data itself still requires formal verification before this rationale can be considered reliable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Orlistat currently holds no marketing authorization in Germany — market status is **not marketed**, with 0 registered licenses. No product, dosage form, or approved-indication records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a theoretical mechanistic inversion (L5, decision stage S0), with zero clinical trials or literature evidence. A blocking data gap on TFDA label warnings/contraindications (DG001) prevents any safety pre-assessment, and the drug's core MOA (DG002) is itself unverified.

**To proceed, the following is needed:**
- Confirm Orlistat's mechanism of action via DrugBank API (resolve DG002)
- Obtain and parse TFDA label PDF for warnings/contraindications (resolve DG001 — blocking)
- Identify at least preclinical or observational evidence directly linking Orlistat to hypervitaminosis management before advancing past S0
- Re-evaluate Germany regulatory pathway, given the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

