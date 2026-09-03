---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrolide antibiotic whose only established clinical use is treating *Clostridioides difficile* infection (CDI), acting locally in the gut with negligible systemic absorption.
The TxGNN model predicts it may be effective for **Staphylococcal Scalded Skin Syndrome (SSSS)**,
but currently **0 clinical trials** and **0 publications** support this specific prediction, and the underlying mechanism argues against systemic efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | *Clostridioides difficile* infection (per known clinical use; not registered in this market — no license data available) |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known clinical use, fidaxomicin is a narrow-spectrum macrolide antibiotic that inhibits bacterial RNA polymerase; its efficacy has been established specifically for *C. difficile*-associated diarrhea, where it acts almost entirely within the gut lumen — systemic absorption after oral dosing is less than 1%.

This pharmacokinetic profile is the central problem for the predicted indication. SSSS is a systemic dermatologic disease caused by exfoliative toxins from *Staphylococcus aureus*, requiring a drug with meaningful systemic (or at minimum, skin-penetrant) bioavailability and activity against staphylococci. Fidaxomicin achieves neither: its distribution is essentially confined to the gastrointestinal tract, and its antibacterial spectrum is oriented toward *C. difficile* and related anaerobic gram-positive organisms rather than typical cutaneous *S. aureus* strains.

Given this mismatch, the prediction should be interpreted as a statistical association surfaced by the TxGNN model rather than a mechanistically supported hypothesis. No pharmacokinetic, microbiological, or clinical evidence currently bridges the gap between fidaxomicin's known behavior and the requirements of SSSS treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

This drug currently holds no marketing authorizations in this jurisdiction (0 licenses on record); no product/authorization table can be generated.

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings, contraindications, and drug interaction data are currently unavailable (flagged as a **Blocking** data gap — DG001), which by itself prevents any S1 safety pre-assessment for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SSSS) has Evidence Level L5 — a TxGNN statistical score with no supporting clinical trials or literature — and the drug's known pharmacokinetics (gut-restricted, <1% systemic absorption) argue mechanistically against efficacy in a systemic staphylococcal skin disease. The drug is also unmarketed in this jurisdiction (0 authorizations), and safety data required for any S1 evaluation is currently blocked (DG001).

**To proceed, the following is needed:**
- TFDA/official label data on warnings, contraindications, and interactions (Blocking gap, DG001)
- Confirmed mechanism of action from DrugBank or primary literature (High-priority gap, DG002)
- Preclinical or in vitro evidence of fidaxomicin activity against *S. aureus* strains relevant to SSSS
- Pharmacokinetic data demonstrating adequate systemic/dermal exposure, if systemic use is to be considered
- Note: rank 8 (*S. aureus* pneumonia, L4, one review-level citation) is comparably weak and not a stronger alternative without primary evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

