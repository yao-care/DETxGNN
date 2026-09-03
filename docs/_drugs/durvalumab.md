---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From PD-L1-Directed Oncology Indications to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab is an anti-PD-L1 monoclonal antibody used across several PD-L1-driven solid tumours; specific original indication data is not yet on file for this profile.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**,
but this specific indication currently has **no clinical trials** and **no published literature** — the rationale rests entirely on class-level mechanistic reasoning from durvalumab's approved urothelial carcinoma activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (original indication list and MOA are data gaps) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, durvalumab is an anti-PD-L1 monoclonal antibody, and its efficacy in checkpoint-inhibitor-responsive urothelial carcinoma has been established as a drug class. Prostatic urethra urothelial carcinoma shares the same urothelial histological origin as bladder urothelial carcinoma — a tumour family with characteristically high tumour mutational burden and PD-L1 expression, and one where durvalumab (or class peers) has demonstrated activity.

NCCN and AJCC staging frameworks frequently group prostatic urethral urothelial carcinoma with bladder urothelial carcinoma for treatment planning purposes, given the shared epithelial lineage and mutational signature. This provides indirect, class-level mechanistic support for extrapolating anti-PD-L1 activity to this specific anatomic subsite. However, no trial or publication has directly tested durvalumab in this particular tumour subtype — the link is inferred rather than demonstrated.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

Durvalumab is currently **not marketed** in Germany under this profile, with no authorizations on file (`total_licenses: 0`). No product-level licensing details are available to summarize.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 immune checkpoint inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low — checkpoint inhibitors typically do not directly suppress bone marrow, unlike cytotoxic chemotherapy |
| Emetogenicity Classification | Low (minimal emetogenic potential, consistent with immune checkpoint inhibitor class) |
| Monitoring Items | Thyroid function (TSH, free T4), liver function (AST/ALT/bilirubin), renal function, pulmonary symptoms (pneumonitis), and GI symptoms (colitis) for immune-related adverse events (irAEs) |
| Handling Protection | Standard IV biologic infusion handling; special cytotoxic drug handling protocols are not required as this is a non-cytotoxic monoclonal antibody |

*Note: No drug-specific toxicity data was available in this evidence pack; the above reflects general immune checkpoint inhibitor class characteristics. Please refer to the package insert for definitive warnings and precautions.*

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (prostatic urethra urothelial carcinoma) has no supporting clinical trials or literature — only class-level mechanistic inference — and a blocking data gap (missing TFDA/label safety information) prevents even an initial safety screen (S1). Combined with the drug's current unmarketed status in Germany, there is insufficient basis to advance.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Direct clinical trial or publication evidence specific to prostatic urethra urothelial carcinoma
- Confirmation of original approved indications and Germany licensing status

**Note:** Among the ten candidates in this pack, **endocervical carcinoma** (rank 6) shows meaningfully stronger evidence — one completed Phase 1 and one active Phase 2 trial (ATARI, n=174) plus supporting literature, reaching evidence level L2. If a single indication needs to be prioritized for further evaluation, this is the stronger candidate and warrants a separate S2-stage review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

