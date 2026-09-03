---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: From Unspecified Original Indication to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir's original approved indication is not available in the current evidence pack. The TxGNN model predicts potential efficacy for **Vulvovaginal Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags the connection as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (no license records) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% (rank 1959) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for letermovir is not available in this evidence pack (data gap DG002, marked High severity — remediation pending via DrugBank API query).

However, the model's own repurposing rationale already provides a mechanistic assessment, and it is negative: letermovir specifically inhibits the CMV (human herpesvirus 5) DNA terminase complex (pUL56/pUL89/pUL51 subunits), a viral-specific target with no counterpart in fungal pathogens such as *Candida* spp. Vulvovaginal candidiasis is a fungal infection typically treated by targeting ergosterol synthesis (e.g., azoles inhibiting CYP51/lanosterol demethylase) or fungal cell wall synthesis (echinocandins) — pathways unrelated to letermovir's antiviral mechanism.

The high TxGNN score (99.88%) most likely reflects an indirect knowledge-graph association — for example, both entities co-occurring frequently with immunocompromised/transplant patient populations in the underlying data — rather than genuine pharmacological similarity. This prediction should be treated as a graph-embedding artifact until independent mechanistic or clinical evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Letermovir is currently **not marketed** in Taiwan (0 licenses on record), so no authorization details are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a raw TxGNN score (L5, S0) with no clinical trials, no literature, and no marketed product in Taiwan to draw on. More importantly, the model's own mechanistic rationale explicitly finds no plausible pharmacological link between an antiviral DNA terminase inhibitor and an antifungal indication — this is a strong signal the association is spurious rather than a genuine repurposing lead.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/manufacturer labeling — warnings and contraindications) before any safety-stage (S1) review can begin
- Resolve DG002 (confirmed mechanism of action via DrugBank) to properly assess or rule out mechanistic plausibility
- Independent preclinical or in-vitro antifungal activity data for letermovir, given no biological rationale currently supports this indication
- Re-evaluate candidate priority — given the mechanistic mismatch, resources may be better directed to other predicted indications with stronger biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

