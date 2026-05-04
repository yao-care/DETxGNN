---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Ripretinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ripretinib: From Gastrointestinal Stromal Tumor — Repurposing Evaluation Pending

## One-Sentence Summary

Ripretinib (Qinlock) is a switch-control kinase inhibitor targeting KIT and PDGFRA mutations, originally approved for advanced gastrointestinal stromal tumor (GIST) in patients who have received three or more prior kinase inhibitor therapies.
This Evidence Pack does not yet contain TxGNN-predicted repurposing candidates for Ripretinib, as two critical data gaps — TFDA safety labeling (blocking severity) and mechanism of action detail (high severity) — remain unresolved.
No new indication can be formally scored or recommended at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced gastrointestinal stromal tumor (GIST), ≥ 4th-line |
| Predicted New Indication | N/A — TxGNN predictions not yet available in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Authorized Market Status | Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is currently available for Ripretinib. The mechanism of action (MOA) data is flagged as a high-severity gap (DG002), which prevents formal mechanistic similarity mapping to candidate indications. Until the TxGNN pipeline is re-run with complete inputs, no graph-based prediction score can be assessed.

Based on publicly available pharmacology, Ripretinib is a broad-spectrum **switch-control inhibitor** of KIT and PDGFRA kinases. Unlike first- and second-generation KIT inhibitors (imatinib, sunitinib), Ripretinib simultaneously occupies both the activation loop and the switch pocket of these kinases, achieving inhibitory coverage across a wide spectrum of primary and acquired resistance mutations. This mechanism is the basis of its efficacy in advanced GIST, a tumour type overwhelmingly driven by gain-of-function KIT or PDGFRA alterations (>85% of cases).

This multi-conformational inhibition profile raises a mechanistic hypothesis for repurposing in other KIT- or PDGFRA-driven malignancies — including systemic mastocytosis, melanoma with KIT mutations, and certain subtypes of acute myeloid leukaemia with KIT overexpression. However, these remain untested hypotheses in the context of this Evidence Pack. Formal TxGNN graph-embedding predictions and DrugBank MOA data must be retrieved before any indication-specific evaluation can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a predicted new indication. (This Evidence Pack contains no TxGNN-predicted repurposing candidates; clinical trial evidence for new indications cannot be extracted.)

---

## Literature Evidence

Currently no related literature available for a predicted new indication. (Pending TxGNN prediction output before indication-specific literature can be identified.)

---

## Authorized Market Information

| Item | Status |
|------|--------|
| Market Status | Not marketed — 0 approved authorizations found |
| Total Authorizations | 0 |

> **Note:** Ripretinib has received marketing authorization outside this dataset's scope (FDA approval May 2020; EMA approval August 2021 under brand name Qinlock). The absence of a local authorization record should be cross-checked against current regulatory databases before concluding non-availability.

---

## Cytotoxicity

Ripretinib is an antineoplastic agent (targeted kinase inhibitor) indicated for a malignant condition.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Switch-control KIT / PDGFRA kinase inhibitor |
| Myelosuppression Risk | Low to moderate; anaemia and neutropenia reported as class effects of KIT inhibitors; CBC monitoring recommended |
| Emetogenicity Classification | Low (oral targeted agent, consistent with MASCC/ESMO classification for this drug class) |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST), blood pressure, thyroid function, ECG (QTc) |
| Handling Protection | Standard oral cytotoxic drug handling precautions apply; caregivers should avoid direct contact with capsule contents |

---

## Safety Considerations

Please refer to the package insert for safety information. (Data gap DG001 — TFDA safety labeling — is classified as **Blocking severity** and has not yet been resolved in this Evidence Pack. Key warnings and contraindications cannot be reported until the package insert PDF is retrieved and parsed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN-predicted repurposing indications for Ripretinib, and one blocking-severity data gap (DG001: safety labeling) prevents even a preliminary safety screen. The candidate cannot advance to any evaluation stage until the gaps below are resolved.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Download and parse the TFDA package insert PDF to extract warnings, contraindications, and special population restrictions — required before S1 safety screening can begin
- **Resolve DG002 (High):** Query the DrugBank API to retrieve full MOA, pharmacodynamics, and target profile for Ripretinib (DrugBank query on 2026-03-29 returned 1 result but data was not captured in the Evidence Pack)
- **Re-run TxGNN prediction pipeline:** Generate graph-based repurposing candidates with complete drug feature inputs; without predictions, no indication-specific evaluation is possible
- **Verify market authorization status:** Cross-check EMA and local regulatory databases to confirm whether Ripretinib is authorized under any jurisdiction relevant to this project, and update `total_licenses` accordingly
- **Retrieve DDI data:** The DDI query returned `not_found`; consider querying alternative sources (e.g., DrugBank interactions, FDA label interactions) given Ripretinib's CYP3A4 metabolism profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

