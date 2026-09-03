---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab: From Unspecified Original Indication to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

The original approved indication for mogamulizumab is not captured in this evidence pack (mogamulizumab is publicly known as an anti-CCR4 monoclonal antibody used in T-cell malignancies, but this is not sourced from the pack itself).
The TxGNN model's top prediction is **Prostatic Urethra Urothelial Carcinoma**, with a score of **99.44%**,
but this candidate — and all 6 other predicted indications in this pack — currently has **zero supporting clinical trials and zero published literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.44% (rank 6358) |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured MOA field of this pack. However, the rationale text embedded in the prediction itself describes mogamulizumab as an anti-CCR4 monoclonal antibody that depletes CCR4+ T cells — including tumor-infiltrating regulatory T cells (Tregs) — via ADCC (antibody-dependent cellular cytotoxicity).

All seven predicted indications share a common speculative thread: tumors with CCR4+ Treg infiltration or T-cell–mediated immune evasion could theoretically benefit from Treg depletion, restoring anti-tumor immunity. This applies most plausibly to the four urothelial/renal-pelvis carcinoma variants (ranks 1–4) and to HHV-8-related tumors (rank 5), where immune dysregulation is a recognized feature of the tumor microenvironment. It applies much more weakly to ectomesenchymoma (rank 6) and malignant cutaneous granular cell tumor (rank 7), which have no known association with the CCR4 pathway.

It is important to note that although all seven scores exceed 99%, their model ranks (6358–8822) place them in the mid-to-lower range of TxGNN's overall prediction pool rather than among top-tier candidates. Absent any clinical trial or literature corroboration, these should be treated as computational hypotheses only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other TxGNN-Predicted Indications (Ranks 2–7)

| Rank | Disease | Score | Model Rank | Mechanistic Basis |
|------|---------|-------|-----------|-------------------|
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.42% | 6569 | CCR4+ Treg depletion hypothesis (speculative) |
| 3 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.40% | 6724 | CCR4+ Treg depletion hypothesis (speculative) |
| 4 | Renal pelvis papillary urothelial carcinoma | 99.37% | 6945 | CCR4+ Treg depletion hypothesis (speculative) |
| 5 | Human herpesvirus 8-related tumor | 99.24% | 8121 | Treg-mediated immune restoration (speculative) |
| 6 | Ectomesenchymoma | 99.15% | 8822 | No known CCR4 pathway link |
| 7 | Malignant cutaneous granular cell skin tumor | 99.15% | 8825 | No known CCR4 expression evidence |

## Germany Market Information

Mogamulizumab is not currently marketed in Germany, and no authorization records are on file (0 authorizations).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CCR4 monoclonal antibody, ADCC-mediated), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications are Evidence Level L5 (model prediction only), with no supporting clinical trials or literature identified for any candidate. Critical inputs needed for even a preliminary safety assessment — TFDA warnings/contraindications (Blocking) and confirmed MOA (High severity) — are marked as data gaps in the pack itself.

**To proceed, the following is needed:**
- TFDA/package insert warnings and contraindications (currently blocking safety evaluation)
- Confirmed mechanism of action from DrugBank
- Confirmed original approved indication(s) for mogamulizumab (currently not captured in this pack)
- Targeted literature and clinical trial search for CCR4/Treg biology in urothelial carcinoma and HHV-8-related tumors, since none were found via automated evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

