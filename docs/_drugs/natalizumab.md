---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

Using the report template directly (task is domain-specific report generation, not a coding/debugging skill scenario).

# Natalizumab: From Multiple Sclerosis / Crohn's Disease to Bronchitis

## One-Sentence Summary

> Natalizumab is a monoclonal antibody used for multiple sclerosis and Crohn's disease, acting by blocking α4-integrin–mediated leukocyte migration across the blood-brain barrier and gut mucosa.
> The TxGNN model predicts it may be effective for **Bronchitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and mechanistically points in the opposite direction — immunosuppression would be expected to *increase* respiratory infection risk rather than treat it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis / Crohn's Disease (mentioned in mechanistic rationale text; not confirmed by an official label — this drug has no approved license record in this evidence pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (original MOA field is empty). Based on the information available, natalizumab is an α4-integrin monoclonal antibody that inhibits leukocyte trafficking across the blood-brain barrier and intestinal mucosa, and is used for multiple sclerosis and Crohn's disease — both conditions characterized by pathological immune cell infiltration into tissue.

Bronchitis, by contrast, is typically an infectious or irritant airway inflammation. There is no known mechanistic link between α4-integrin blockade and the resolution of bronchitis. If anything, natalizumab's immunosuppressive effect would be expected to *impair* clearance of respiratory pathogens and could plausibly increase susceptibility to bronchitis rather than treat it.

This prediction therefore appears to be a high-scoring artifact of the TxGNN model with no corroborating mechanistic, preclinical, or clinical rationale, and the evidence direction available for this drug (see Literature Evidence for related skin conditions, e.g., PMID 32470781, PMID 35646438) generally shows natalizumab **inducing or worsening** inflammatory conditions rather than resolving them — reinforcing that this candidate should not be interpreted as biologically plausible without further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Natalizumab currently has no marketing authorization on record in this evidence pack (0 licenses; market status: not marketed). No dosage form, product name, or approved indication data is available for the German market.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Official TFDA/BfArM label warnings, contraindications, and DDI data are flagged as a Blocking data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (bronchitis) has zero supporting clinical trials or literature, and its proposed mechanism directly contradicts natalizumab's known immunosuppressive pharmacology — an immunosuppressant is mechanistically more likely to *cause or exacerbate* respiratory infection/inflammation than treat it. This candidate does not meet even the minimum threshold (L4/S1) to advance past pure model prediction.

**To proceed, the following is needed:**
- Official drug label / TFDA warnings and contraindications (currently a Blocking data gap — DG001)
- Confirmed mechanism of action from DrugBank or primary literature (currently a High-severity data gap — DG002)
- Any preclinical or mechanistic evidence specifically linking α4-integrin/VLA-4 blockade to airway inflammation resolution, before this candidate can move beyond Hold
- Note: among the 5 predicted indications reviewed, **psoriasis** (rank 3) has richer literature (18 papers) but shows *directionally conflicting* signals (mostly drug-induced/aggravated psoriasis, one case series of improvement) — this may warrant a separate, dedicated safety-mechanism research question, but is not a basis to change the decision on bronchitis above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

