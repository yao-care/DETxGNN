---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: From Iron Chelation Therapy to Hepatic Porphyria

## One-Sentence Summary

Deferiprone is an oral iron chelator; based on data within this evidence pack, its established clinical role is managing **transfusional iron overload** (e.g., in beta-thalassemia — see rank 8 candidate below), though the formal original indication and TFDA label are not documented in this pack.
The TxGNN model's top-ranked new prediction for this drug is **Hepatic Porphyria**, with a 99.20% prediction score — but **no clinical trials and no literature** currently support this specific direction, and the model's own mechanistic rationale flags the biological link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty; see DG001/DG002). Drug class context from pack: oral iron chelator, established use in transfusional iron overload (see beta-thalassemia candidate, rank 8) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`, flagged as DG002 in this pack). Based on information present elsewhere in this evidence pack (rank 8 rationale), deferiprone is an oral tris-hydroxypyridinone iron chelator that penetrates cell membranes, binds free ferric iron, and promotes its urinary excretion — a mechanism directly relevant to iron-overload states such as those seen in chronically transfused patients.

For **hepatic porphyria**, however, the model's own repurposing rationale explicitly states the mechanistic link is weak: hepatic porphyria arises from enzyme deficiencies in the heme biosynthesis pathway causing accumulation of toxic intermediates, not from tissue iron overload. Deferiprone's iron-chelating action has no established pathophysiological connection to this disease process. This top-ranked candidate therefore reflects a **statistical similarity signal from TxGNN**, not a mechanism- or evidence-based hypothesis.

**Note on this multi-candidate pack:** Among the 9 predicted indications evaluated for deferiprone, only **beta-thalassemia with other manifestations** (rank 8) is supported by actual literature (2 publications, evidence level L3) and carries a "Proceed with Guardrails" recommendation — consistent with deferiprone's real-world use in transfusion-dependent iron overload. The top-ranked-by-score candidate (hepatic porphyria, this report's subject) has neither trials nor literature and is recommended **Hold**. Reviewers should weigh evidence strength, not score rank alone, when prioritizing candidates from this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

No German/Taiwan marketing authorizations are currently held for this drug (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all marked as data gaps in this pack. DG001 — missing TFDA package insert warnings/contraindications — is flagged as a **Blocking** severity gap, meaning it currently prevents formal S1 safety review for any indication under this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hepatic porphyria prediction has no supporting clinical trials or literature, and the model's own mechanistic rationale rates the biological plausibility as weak (L5, no direct disease-mechanism overlap with iron chelation). Combined with a Blocking-severity TFDA safety data gap for the drug overall, this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — required to clear the Blocking gap (DG001) before any S1 safety review
- Documented mechanism of action (DG002) to properly evaluate mechanistic plausibility across all candidate indications
- Preclinical or mechanistic studies specifically linking iron chelation to heme biosynthesis pathway disorders, if this indication is to be pursued further
- As an alternative, consider redirecting evaluation resources to the **beta-thalassemia with other manifestations** candidate (rank 8), which already has literature support and a "Proceed with Guardrails" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

