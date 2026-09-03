---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 1
---

# Caspofungin
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

# Caspofungin: From Antifungal Therapy to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin-class antifungal agent; specific original indication data is not available in this evidence pack, though echinocandins are generally used for invasive fungal infections. The TxGNN model predicts a possible association with **Gastrin Secretion Abnormality**, but this prediction currently has **no supporting clinical trials** and **no supporting literature** — it rests solely on a model score of 99.44%.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap; drug class known as echinocandin antifungal) |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for caspofungin in this evidence pack. Based on known drug class information, caspofungin is an echinocandin antifungal that inhibits fungal cell wall β-(1,3)-D-glucan synthase — a mechanism with no established pharmacological pathway related to gastrin secretion regulation.

The repurposing rationale provided alongside this prediction explicitly notes that there is **no known biological link** between echinocandin antifungal activity and gastrin secretion. The absence of original MOA data further weakens confidence in any mechanistic connection. This prediction should be treated as a pure model output (TxGNN score 0.994, rank 6388) rather than a mechanistically grounded hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Caspofungin is not currently marketed in Germany under this evidence pack, and no authorization records are available (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data is flagged as a Blocking data gap — this must be resolved before any S1 safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score, this candidate has zero clinical trial or literature support, and the proposed mechanistic link between antifungal cell-wall inhibition and gastrin secretion regulation has no established biological basis. Combined with missing original indication, MOA, and safety data, this candidate remains at evidence level L5 and is not ready to advance.

**To proceed, the following is needed:**
- Resolve Blocking gap: TFDA label warnings/contraindications (source: TFDA official site, PDF parsing)
- Resolve High-priority gap: full MOA data via DrugBank API
- Identify any preclinical or mechanistic literature that could support a biological rationale for this indication
- If no plausible mechanistic link can be established, recommend deprioritizing this candidate rather than continuing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

