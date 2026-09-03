---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2-Positive Breast Carcinoma

## One-Sentence Summary

> Ocrelizumab is an anti-CD20 monoclonal antibody whose established use is B-cell depletion in multiple sclerosis; formal indication text is not available in this evidence pack because the drug is **not currently marketed in Germany**.
> The TxGNN model predicts it may be effective for **HER2-Positive Breast Carcinoma** with a very high raw score (**99.89%**), but this prediction is currently supported by **zero clinical trials** and **zero literature references**, and the reviewer-authored mechanistic rationale explicitly flags no known biological link between B-cell depletion and HER2/ERBB2-driven tumor signaling.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (based on known drug class/background; no formal German regulatory indication text is on file — drug is unmarketed) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no supporting clinical or literature data) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). Based on known background information, ocrelizumab is an anti-CD20 monoclonal antibody that depletes CD20-positive B lymphocytes to achieve immunomodulation, and is approved for multiple sclerosis. This mechanism is fundamentally an immune-cell-targeted therapy, not a tumor-signaling-pathway therapy.

HER2-positive breast carcinoma, by contrast, is driven by overexpression/amplification of the HER2 (ERBB2) receptor tyrosine kinase, which activates downstream proliferative signaling (PI3K/AKT, MAPK) independent of B-cell biology. There is no overlap between the CD20/B-cell depletion pathway and the HER2/ERBB2 signaling pathway, and no published evidence that B-cell-depleting therapy alters HER2-driven tumor growth.

Given the absence of any mechanistic bridge, any clinical trials, or any literature support, the reviewer assessment in this evidence pack concludes the high TxGNN score most likely reflects **model-side prediction noise** rather than a biologically grounded repurposing signal. This is an important caveat that should weigh heavily against acting on the score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

**Data quality note (from the same evidence pack, other candidate indications):** A related candidate, *"breast tumor luminal A or B,"* returned 19 PubMed hits during the automated search. On manual review, all 19 are unrelated to breast cancer — they concern B-cell development/maturation, hepatitis B vaccines, and HLA-B allele typing. This strongly suggests the literature search matched on the standalone letter "B" (from "luminal B") rather than the disease concept, and should be treated as a **false-positive artifact of the search pipeline**, not supporting evidence. The remaining three candidate indications (normal breast-like subtype, PR-positive breast cancer, PR-negative breast cancer) returned zero trials and zero literature. None of the five predicted indications in this pack currently have genuine supporting evidence.

---

## Germany Market Information

Ocrelizumab currently has **no marketing authorization on file in Germany** (0 licenses recorded). No product name, dosage form, or approved indication text is available from regulatory data for this drug in this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all flagged as data gaps in this evidence pack — notably DG001, a *Blocking*-severity gap for TFDA/label warnings and contraindications, which prevents this candidate from passing the S1 safety pre-screen.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only) with no clinical trials and no genuine literature support for HER2-positive breast carcinoma or any of the other four predicted breast-cancer-related indications in this pack. The proposed mechanism (CD20-mediated B-cell depletion) has no established biological link to HER2/ERBB2-driven tumor signaling, and one adjacent candidate's apparent literature support was found to be a search-pipeline false positive. Combined with a Blocking-severity safety data gap (DG001) and a High-severity MOA data gap (DG002), this candidate cannot currently pass even the initial safety and evidence screening stage.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for ocrelizumab from DrugBank/primary literature (resolves DG002)
- TFDA/BfArM package insert warnings and contraindications (resolves DG001, Blocking)
- A corrected, indication-specific literature and clinical trial search that filters out single-letter/keyword false matches (e.g., re-run the "luminal B" query with disease-specific MeSH terms)
- If pursued further, dedicated preclinical or mechanistic studies establishing any plausible link between B-cell depletion and HER2-driven tumor biology before any clinical hypothesis is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

