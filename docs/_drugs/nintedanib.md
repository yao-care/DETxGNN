---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 3
---

# Nintedanib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nintedanib: From an Unrecorded Original Indication to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

> Nintedanib's original approved indication is not recorded in this evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
> with **0 clinical trials** and **1 supporting publication** currently identified — evidence remains at the mechanistic/preclinical level.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no records in evidence pack) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (preclinical / mechanism-level only) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Nintedanib is not available in this evidence pack (DG002, High severity). Based on the mechanistic rationale that is available, Nintedanib is described as a PDGFR-α/β inhibitor among its targets.

DFSP tumors are driven by a COL1A1-PDGFB fusion gene that causes constitutive PDGFRB activation. This overlaps mechanistically with Imatinib, the current standard of care for DFSP. Nintedanib's PDGFR inhibitory activity provides a plausible target-based rationale for this prediction, and the very high TxGNN score (0.9915) reflects strong network-level support. However, the only supporting literature identified (PMID 29408302) is a general review of PDGFR inhibitors as a drug class — it does not report Nintedanib-specific data in DFSP, and no clinical trials currently exist for this indication.

The other two predicted indications (liposarcoma, ovarian myxoid liposarcoma) are considerably weaker: both are pure TxGNN score-based extrapolations from the same PDGFR/FGFR pathway logic, with no supporting literature or trials at all (Evidence Level L5, recommendation "Hold" for both), and are not discussed further here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors (as a drug class) in treating neoplastic disorders; establishes PDGFR signaling as a therapeutic target but does not report Nintedanib-specific DFSP data. |

## Taiwan Market Information

Nintedanib is not currently marketed in Taiwan (0 authorizations on record). No license or approved-indication data is available for this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label/warning data (DG001) is flagged as a **Blocking** data gap — its absence directly prevents entry into the S1 safety pre-assessment stage.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The DFSP prediction rests on a plausible but indirect mechanistic argument (PDGFR pathway overlap with Imatinib) supported by a single drug-class review paper, with no Nintedanib-specific trials or preclinical data, and no original indication or MOA confirmed on file. A Blocking safety data gap (TFDA label unavailable) also prevents formal S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA/package insert data to resolve the Blocking safety gap (DG001)
- Confirmed MOA and original approved indication(s) for Nintedanib from DrugBank (DG002)
- Nintedanib-specific preclinical (e.g., PDGFRB-fusion cell line/xenograft) or case-level clinical data in DFSP
- Re-evaluation of liposarcoma and ovarian myxoid liposarcoma predictions if any supporting literature emerges (currently no basis to proceed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

