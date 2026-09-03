---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tipranavir is a non-peptidic HIV-1 protease inhibitor clinically used (in combination with ritonavir) for treatment-experienced HIV-1 infection. The TxGNN model's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)**, a veterinary retroviral disease in cats — with **no clinical trials and no literature** currently supporting this as a human repurposing opportunity. The model appears to be capturing cross-species retroviral-protease homology rather than an actionable clinical signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (clinically known: HIV-1 infection, treatment-experienced adults, used with ritonavir boosting) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (veterinary) |
| TxGNN Prediction Score | 99.99% (rank 215 of full disease list) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, tipranavir is a non-peptidic HIV-1 protease inhibitor administered with ritonavir; its efficacy in treatment-experienced HIV-1 infection is well established.

The top-ranked predicted indication, feline acquired immunodeficiency syndrome (FIV), is a **veterinary retroviral disease**, not a human condition. The model's rationale explicitly notes that the high score likely reflects structural homology between the FIV and HIV proteases (a cross-species retroviral mechanism), rather than an actual therapeutic opportunity in humans — the source data itself states this "has no practical drug repurposing value."

The same pattern holds for most other top-10 predictions: simian immunodeficiency virus infection (research animal model), a rare neurodevelopmental disorder, familial hyperlipidemia (likely reflecting a known protease-inhibitor *adverse effect* rather than a treatable indication), and several unrelated benign neoplasms (prostate fibroma, Brenner tumor, phyllodes tumor) — all flagged internally as embedding noise with no biological plausibility. Two exceptions stand out: **AIDS related complex** (rank 6, evidence level L4) is mechanistically coherent because it sits on the same HIV/AIDS disease spectrum tipranavir already treats, though no trials specific to this legacy term were found; and **congenital HIV infection** (rank 5) is associated with 9 clinical trials, but these all concern other antiretroviral regimens (cabotegravir/rilpivirine, dolutegravir, maraviroc-class CCR5 antagonists) rather than tipranavir itself, so they do not directly support a new indication for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication (feline acquired immunodeficiency syndrome).

---

## Literature Evidence

Currently no related literature available for the predicted indication (feline acquired immunodeficiency syndrome).

---

## Germany Market Information

No marketing authorizations are currently on file for tipranavir (0 licenses recorded; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug interaction data are currently unavailable — TFDA label retrieval is flagged as a Blocking data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (feline AIDS) is a veterinary disease with no clinical trials, no literature, and an explicit mechanistic caveat that it carries no practical repurposing value in humans. No clinically actionable, sufficiently evidenced human indication emerges from the current prediction set.

**To proceed, the following is needed:**
- Retrieve TFDA-approved label (warnings/contraindications) — currently a Blocking gap (DG001)
- Obtain confirmed mechanism-of-action data from DrugBank — currently a High-severity gap (DG002)
- If pursuing repurposing further, redirect evaluation toward the more mechanistically coherent candidates within the same disease spectrum (e.g., "AIDS related complex") rather than the top TxGNN-ranked but biologically implausible/cross-species predictions
- Independently verify whether any tipranavir-specific trials exist for HIV-spectrum sub-indications, since the trials currently attached to "congenital HIV infection" involve other antiretroviral agents, not tipranavir
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

