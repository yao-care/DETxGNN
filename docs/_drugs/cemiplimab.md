---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Approved Immuno-Oncology Indications to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab is an anti-PD-1 immune checkpoint inhibitor whose evidence-pack rationale references prior approvals in squamous and immunogenic skin/lung cancers. The TxGNN model's top-ranked new prediction is **Gallbladder Adenosquamous Carcinoma**, but this is currently supported by **0 clinical trials** and **0 publications**, placing it at the earliest, purely computational evidence stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack (no approved-indication records; drug not authorized in this dataset) |
| Predicted New Indication | Gallbladder Adenosquamous Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cemiplimab is not available in the structured DrugBank record used for this pack (data gap DG002, severity: High). However, the repurposing rationale text embedded in this evidence pack consistently describes cemiplimab as an **anti-PD-1 monoclonal antibody** and references its prior approvals in cutaneous squamous cell carcinoma, basal cell carcinoma, and metastatic NSCLC — indicating it acts by blocking the PD-1/PD-L1 checkpoint to restore T-cell antitumor activity.

For the top-ranked candidate, gallbladder adenosquamous carcinoma, the rationale is explicitly weak: this is a **mixed-histology tumor**, where only the squamous component might theoretically respond to PD-1 blockade, while the adenocarcinoma component's responsiveness is unknown. There is no clinical or literature evidence supporting this specific link — the prediction rests entirely on the TxGNN graph-embedding score.

By contrast, among the other nine candidates in this pack, **External Ear Basal Cell Carcinoma** (rank 4) has a much stronger mechanistic case: it is simply an anatomical-site variant of BCC, a tumor type cemiplimab's rationale states is already an approved indication after Hedgehog-inhibitor failure, and it is supported by a real-world case report (see "Other Predicted Indications" below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: A supporting case report (PMID 34157152) exists for a different candidate in this pack — External Ear Basal Cell Carcinoma (rank 4) — see the table below.*

---

## Germany Market Information

No German market authorizations found. Cemiplimab's market status in this dataset is **Not Marketed**, with 0 licenses recorded.

---

## Other Predicted Indications Considered in This Evidence Pack

This candidate bundle (`TW-DB14707-multi`) contains 10 TxGNN-predicted indications. For transparency, all are listed below:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Gallbladder Adenosquamous Carcinoma | 99.99% | L5 | S0 | Hold |
| 2 | Glottis Squamous Cell Carcinoma | 99.99% | L5 | S0 | Hold |
| 3 | Rectal Cloacogenic Carcinoma | 99.99% | L5 | S0 | Hold |
| 4 | External Ear Basal Cell Carcinoma | 99.99% | L4 | S1 | Research Question |
| 5 | Adenosquamous Prostate Carcinoma | 99.99% | L5 | S0 | Hold |
| 6 | Urethral Verrucous Carcinoma | 99.99% | L5 | S0 | Hold |
| 7 | Lung Occult Squamous Cell Carcinoma | 99.99% | L5 | S0 | Hold |
| 8 | Pancreatic Adenosquamous Carcinoma | 99.99% | L5 | S0 | Hold |
| 9 | Non-keratinizing Sinonasal Squamous Cell Carcinoma | 99.99% | L5 | S0 | Hold |
| 10 | Supraglottis Squamous Cell Carcinoma | 99.99% | L5 | S0 | Hold |

Rank 4 (External Ear BCC) is the only candidate with any supporting real-world evidence (a case report describing lasting response after cemiplimab discontinuation in advanced BCC).

---

## Cytotoxicity

Cemiplimab is an oncology therapeutic (immune checkpoint inhibitor); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor), based on mechanism descriptions in this evidence pack |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/regulatory warnings and contraindications data are marked as a Blocking data gap (DG001) in this evidence pack and could not be retrieved.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gallbladder Adenosquamous Carcinoma) has no supporting clinical trials or literature and rests solely on an L5 model score with an acknowledged mechanistic gap (mixed histology, uncertain response). Combined with the Blocking-severity absence of official safety/label data (DG001) and the High-severity absence of MOA data (DG002), the evidence base is insufficient to proceed on this candidate.

**To proceed, the following is needed:**
- TFDA/BfArM label data — warnings, contraindications (DG001, Blocking)
- DrugBank mechanism-of-action detail for cemiplimab (DG002, High)
- Any preclinical or case-level evidence specifically on adenosquamous gallbladder carcinoma before advancing beyond S0
- Consider redirecting research priority toward **External Ear Basal Cell Carcinoma** (rank 4), which already has L4 evidence and a "Research Question" stage — this candidate merits a literature/registry search update rather than being placed on Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

