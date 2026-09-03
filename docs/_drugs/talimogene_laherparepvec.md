---
layout: default
title: Talimogene Laherparepvec
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
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

# Talimogene Laherparepvec: From Melanoma to CMM7 (Cutaneous Malignant Melanoma Susceptibility Subtype)

## One-Sentence Summary

> Talimogene laherparepvec (T-VEC) is a genetically modified HSV-1 oncolytic viral immunotherapy, publicly known to be approved for unresectable, injectable melanoma lesions of the skin, subcutaneous tissue, and lymph nodes (this original indication is not present in the current evidence pack and is cited from public regulatory knowledge only).
> The TxGNN model predicts it may be relevant to **CMM7** (a cutaneous malignant melanoma susceptibility subtype), with a prediction score of **99.20%**, but **no clinical trials or literature** are currently registered to support this specific link, and the mechanistic rationale for this top-ranked prediction has not yet been completed in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the current evidence pack (`original_indications` is empty; drug is not yet marketed in Taiwan). Publicly known indication: unresectable cutaneous/subcutaneous/nodal melanoma lesions. |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma, susceptibility subtype 7) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 (no clinical trials or literature identified; model prediction only) |
| Taiwan Market Status | ✗ 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on publicly known information, talimogene laherparepvec is an oncolytic herpes simplex virus type 1 (HSV-1) engineered to selectively replicate in tumor cells, causing lysis, and to express GM-CSF to stimulate local and systemic anti-tumor immune responses. It is administered exclusively by direct intralesional injection.

CMM7 is not a distinct disease entity in the usual sense — it refers to a cutaneous malignant melanoma susceptibility locus/subtype within the melanoma disease family, the same tumor lineage as T-VEC's known original indication. Mechanistically this proximity is plausible (same tumor cell type, same route-accessible lesion class), but the evidence pack leaves `mechanistic_link` and `similarity_to_original` for this top-ranked candidate marked **"pending"** — i.e., no completed rationale has been recorded, and no supporting clinical trials or literature have been retrieved.

By contrast, the six lower-ranked candidates (ranks 2–7, see below) have already been assessed and consistently flagged **Hold**, largely due to route-of-administration incompatibility (deep/inaccessible lesions, CNS or intraocular disease) or lack of mechanistic/histologic overlap with melanoma. Given that the top-ranked candidate (CMM7) itself lacks completed evidence and rationale, and the drug is not marketed in Taiwan with a blocking safety data gap (DG001), no candidate in this pack currently meets the threshold for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

---

## Other Predicted Indications (Ranks 2–7, Already Evaluated)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Rationale |
|------|---------|-------------|-----------------|-----------------|----------------|
| 2 | Pediatric leptomeningeal melanoma | 99.15% | L5 | Hold | Intralesional-only route cannot reach CNS/leptomeningeal space; no pediatric safety data |
| 3 | Epithelioid cell uveal melanoma | 99.13% | L5 | Hold | Different mutation landscape (GNAQ/GNA11 vs BRAF/NRAS), immune-privileged intraocular site, poor immunotherapy response history |
| 4 | Glottis squamous cell carcinoma | 99.07% | L5 | Hold | Different histology/immune profile; glottic anatomy limits intralesional injection feasibility |
| 5 | Lung occult squamous cell carcinoma | 99.05% | L5 | Hold | "Occult" tumor is by definition not localizable — fundamentally incompatible with intralesional delivery |
| 6 | Rectal cloacogenic carcinoma | 99.01% | L5 | Hold | Rare histologic subtype with no shared mechanism with melanoma; no supporting data |
| 7 | Gallbladder adenosquamous carcinoma | 99.01% | L5 | Hold | Deep-seated lesion, intralesional injection not feasible without invasive access; no supporting data |

All six candidates were already assessed as **Hold** in the evidence pack, primarily due to route-of-administration incompatibility with T-VEC's intralesional-only delivery, and the absence of any supporting clinical trial or literature evidence.

---

## Taiwan Market Information

No marketing authorizations found. `taiwan_regulatory.market_status` = 未上市 (Not Marketed), `total_licenses` = 0, `licenses` = empty. Talimogene laherparepvec is not currently authorized for sale in this jurisdiction.

---

## Cytotoxicity

Talimogene laherparepvec is an oncolytic viral immunotherapy for melanoma (a malignant neoplasm), so this section applies. No DrugBank toxicity or MOA data is present in the evidence pack; the table below reflects publicly known drug-class information only.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (Oncolytic viral therapy) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (mechanism is viral lysis + immune stimulation, not DNA-damaging chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Injection-site reactions, flu-like symptoms (fever, chills, fatigue), signs of herpetic infection/dissemination, immune-related adverse events |
| Handling Protection | Requires live-virus biosafety handling precautions (avoid contact with immunocompromised individuals/pregnant staff, needlestick precautions) rather than standard cytotoxic drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and `ddi` are all data gaps in the current evidence pack; DG001 — TFDA label warnings/contraindications — is flagged as Blocking, meaning this candidate cannot pass the S1 safety pre-screen until resolved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (CMM7) has no clinical trial or literature evidence and its mechanistic rationale is still marked "pending"; the six next-ranked candidates have already been formally assessed as Hold due to route-of-administration incompatibility or lack of mechanistic overlap. Combined with a Blocking safety data gap (TFDA label data unavailable) and zero marketing authorizations in Taiwan, no candidate in this pack currently supports proceeding.

**To proceed, the following is needed:**
- TFDA (or equivalent) approved package insert — warnings, contraindications, and DDI data (resolves DG001, currently Blocking)
- Confirmed mechanism of action from DrugBank or primary literature (resolves DG002)
- Completion of `mechanistic_link` / `similarity_to_original` rationale for the CMM7 candidate (currently "pending")
- Targeted literature/clinical trial search specific to CMM7 and melanoma susceptibility subtypes
- Confirmation of Taiwan market/registration status before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

