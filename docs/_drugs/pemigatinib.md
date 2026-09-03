---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From Unknown Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib's original approved indication is not documented in this evidence pack (no German market license on file). TxGNN predicts a possible link to **Multiple Endocrine Neoplasia**, but this is currently a pure model prediction — **no clinical trials** and **no published literature** support this specific direction (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (no German license record) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

No confirmed original indication or DrugBank MOA record exists in this evidence pack. Based on the mechanistic notes attached to related candidate predictions, Pemigatinib is described as a selective **FGFR1/2/3 (fibroblast growth factor receptor) inhibitor**, consistent with its known class as a kinase-targeted agent.

For the top-ranked prediction, Multiple Endocrine Neoplasia (MEN), the underlying rationale is weak: MEN pathogenesis is driven mainly by **RET** and **MEN1** gene abnormalities, which have no established mechanistic overlap with the FGFR1–3 signaling pathway targeted by Pemigatinib. The prediction score is high, but it is not anchored by any known biological connection, clinical trial, or literature — it reflects the TxGNN model's statistical association only.

For context, a lower-ranked candidate (HER2 positive breast carcinoma, rank 3) has a more plausible mechanistic story — FGFR1/2 amplification is a known resistance mechanism to anti-HER2 therapy — but even that candidate is only supported by a general 2021 kinase-inhibitor review (PMID 33513356), not indication-specific evidence, and sits at Evidence Level L4 / decision stage S1 ("Research Question").

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No German market authorization currently exists for Pemigatinib (market status: Not Marketed, 0 licenses on file).

## Cytotoxicity

Pemigatinib is a kinase-targeted antineoplastic agent (FGFR1/2/3 inhibitor class), based on the mechanistic description available in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1/2/3 selective kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has no clinical trial or literature support and lacks a credible mechanistic link (Evidence Level L5). This is compounded by two data gaps: the TFDA/package-insert safety data is missing (Blocking severity — required before any S1 safety pre-assessment), and confirmed MOA data is not yet retrieved from DrugBank (High severity).

**To proceed, the following is needed:**
- Retrieve TFDA package insert (warnings/contraindications) to clear the Blocking data gap (DG001)
- Confirm DrugBank MOA record for Pemigatinib (DG002)
- If pursuing repurposing, prioritize the HER2 positive breast carcinoma candidate (rank 3) over MEN, as it has a more defensible mechanistic rationale, though it still requires indication-specific clinical or preclinical evidence before advancing past "Research Question" stage
- Confirm original approved indication and any existing market license status before drafting a repurposing strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

