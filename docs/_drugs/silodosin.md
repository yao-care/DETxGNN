---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using no additional skill — this is a direct content-generation task against a fully specified template; proceeding straight to the report.

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Silodosin is a highly selective α1A-adrenergic receptor antagonist, pharmacologically used for benign prostatic hyperplasia (BPH)/lower urinary tract symptoms.
> The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita** (score 99.99%),
> but this prediction is currently supported by **zero clinical trials** and **zero publications**, with no known mechanistic pathway connecting α1A blockade to hair follicle biology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia / lower urinary tract symptoms (inferred from drug class and repurposing rationale text; not present in evidence pack — `original_indications` is empty) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% (model rank 168) |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the drug class and the rationale field embedded in the prediction, silodosin is a highly selective α1A-adrenergic receptor antagonist acting primarily on prostatic and lower urinary tract smooth muscle, and it is presumed to be used for BPH.

Ambras type hypertrichosis universalis congenita is a rare congenital disorder linked to chromosomal rearrangements and hair follicle developmental genes. There is no established biological pathway connecting peripheral α1A-receptor blockade to hair follicle growth regulation — drug-induced hypertrichosis is more commonly associated with potassium-channel openers (e.g., minoxidil), not α-adrenergic antagonism. The evidence pack's own rationale field explicitly flags this as a high-score/no-mechanism case, meaning the TxGNN association likely reflects embedding-space noise rather than a biologically grounded signal.

All five other candidates in this evidence pack (hypertrichosis, periodontal malformation syndrome, Dandy-Walker malformation, hair shaft abnormality, familial trichomegaly) share the same pattern: very high TxGNN scores paired with no clinical trial evidence and, where literature exists, matched publications unrelated to the drug (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: rank 3 candidate "malformation syndrome with odontal/periodontal component" returned 20 periodontitis-related publications, but none mention silodosin or α1-antagonists — these are considered irrelevant co-occurrence matches, not supporting evidence for the top prediction.)*

---

## Germany Market Information

Silodosin currently has no market authorization records in Germany (`total_licenses: 0`, `licenses: []`). This drug is not marketed in the German dataset covered by this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` are both flagged as data gaps in this evidence pack — item DG001, severity "Blocking," specifically blocks S1 safety pre-assessment pending TFDA label retrieval.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but zero clinical or literature support, no plausible mechanistic link, and the drug is not currently marketed in Germany. Combined with a Blocking-severity safety data gap (DG001) and missing MOA data (DG002), this candidate does not meet the minimum bar to proceed to safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) retrieval to resolve DG001 (Blocking)
- Confirmed MOA from DrugBank to resolve DG002 and enable mechanistic evaluation
- Confirmed original indication and Germany/Taiwan market status (currently absent from source data)
- Any preclinical or case-level evidence linking α1-adrenergic antagonism to hair follicle or congenital hypertrichosis pathways — none currently exists
- If no such evidence emerges, this candidate should be deprioritized in favor of other TxGNN predictions with actual trial/literature backing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

