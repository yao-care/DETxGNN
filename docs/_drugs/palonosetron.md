---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 5
---

# Palonosetron
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

# Palonosetron: From [Data Gap – Original Indication Not Provided] to Migraine Disorder

## One-Sentence Summary

> Palonosetron (DB00377) is a selective 5-HT3 receptor antagonist; its original approved indication is not documented in this evidence pack (data gap).
> The TxGNN model predicts a possible link to **Migraine Disorder** with a **99.74% confidence score**,
> but this is currently supported by only **1 case report** (no clinical trials), and that report actually describes palonosetron **inducing** migraine-type headache — a signal opposite to a therapeutic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and `original_moa` is flagged as a data gap in this evidence pack |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on what is known from the repurposing rationale in this evidence pack, palonosetron is a **selective 5-HT3 receptor antagonist**. This receptor class is not a primary therapeutic target in migraine — migraine treatment mechanistically centers on 5-HT1B/1D/1F receptors (e.g., triptans), not 5-HT3.

The only literature identified for this prediction is a single case report titled *"Palonosetron-induced migraine-type headache"* (PMID 21132477). Rather than supporting a therapeutic use of palonosetron in migraine, this report describes migraine-type headache as an **adverse reaction** to the drug — a direction contrary to the repurposing hypothesis. No clinical trials, preclinical mechanistic studies, or supportive literature were found.

Taken together, the mechanistic rationale and the available evidence do not align with the TxGNN prediction. The high TxGNN score appears to reflect embedding-space similarity rather than a validated pharmacological or clinical relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report | Canadian Journal of Anaesthesia | Describes migraine-type headache **induced** by palonosetron — an adverse-event report, not evidence of therapeutic benefit in migraine |

---

## Germany Market Information

Palonosetron is currently **not marketed** in Germany (BfArM) — no authorization records exist in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not yet available in this evidence pack (TFDA/BfArM label data collection is flagged as a Blocking gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L4, based on a single adverse-event case report rather than supportive clinical or mechanistic data; the only available literature actually points in the opposite direction (drug-induced headache, not treatment effect).
- The proposed mechanism (5-HT3 antagonism) has no established link to migraine pathophysiology, which is primarily mediated via 5-HT1B/1D/1F receptors.
- The drug is not currently marketed in Germany, and core safety data (warnings, contraindications, DDI) are unavailable (Blocking gap, DG001).

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank/primary literature (DG002)
- TFDA/BfArM label data (warnings, contraindications) to clear the S1 safety gate (DG001)
- Preclinical or mechanistic studies specifically evaluating 5-HT3 pathway relevance to migraine, given the contradictory adverse-event signal
- Re-evaluation if new supportive clinical trial or literature evidence emerges

**Note on other predicted indications:** The remaining four candidates for this drug (migraine with brainstem aura, migraine susceptibility, atrophoderma vermiculata, ulerythema ophryogenesis) are all rated L5 with no supporting clinical or literature evidence — the "migraine susceptibility" literature set consists of genetic/epilepsy studies unrelated to drug mechanism, and the two dermatologic predictions have no evidence at all. All are recommended **Hold** and are considered likely false positives from embedding-similarity scoring alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

