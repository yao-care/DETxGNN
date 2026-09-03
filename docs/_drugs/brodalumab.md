---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab (DB11776): Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Brodalumab is a fully human monoclonal antibody targeting the interleukin-17 receptor A (IL-17RA), approved in the US and EU for moderate-to-severe plaque psoriasis (brand names: Siliq®, Kyntheum®).
The current Evidence Pack contains **no TxGNN-predicted new indications** for this compound, and several critical data fields — including mechanism of action, package insert warnings, and contraindications — are absent.
A full repurposing evaluation **cannot be completed** until these data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (from domain knowledge; not captured in Evidence Pack) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — TxGNN pipeline not yet executed |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Taiwan Market Information

Brodalumab currently has **no registered product authorizations in Taiwan** (TFDA). No approved products, dosage forms, or indication texts are on record as of this report's data cutoff (2026-04-20).

For reference, the drug is approved in other jurisdictions:

| Region | Brand Name | Holder | Approved Indication |
|--------|------------|--------|---------------------|
| United States | Siliq® | AstraZeneca / Bausch Health | Moderate-to-severe plaque psoriasis |
| European Union / UK | Kyntheum® | LEO Pharma | Moderate-to-severe plaque psoriasis |

> **Note:** The above global market data is drawn from domain knowledge, not from the Evidence Pack. It is provided as background context only.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The Evidence Pack records no key warnings, contraindications, or drug–drug interactions for brodalumab. The TFDA package insert query returned a result, but the parsed content was not included in this Evidence Pack version. Before any clinical evaluation proceeds, a complete review of the official prescribing information (particularly the **boxed warning for suicidal ideation and behaviour** associated with IL-17 pathway inhibitors) is mandatory.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is fundamentally incomplete — no TxGNN candidate indications have been generated, and the two blocking data gaps (TFDA package insert and MOA) remain unresolved. Without a predicted indication there is no repurposing hypothesis to evaluate.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** for Brodalumab (DB11776) to generate ranked candidate indications
- **Retrieve MOA from DrugBank API** (DB11776) — IL-17RA binding mechanism and downstream signalling pathway
- **Parse TFDA package insert** (query log ID 4 returned a result; content must be extracted) — particularly warnings, contraindications, and special populations
- **Confirm target disease scope** — if a specific repurposing indication is already of interest (e.g., inflammatory bowel disease, axial spondyloarthritis, asthma), specify it so a focused evidence search can be initiated
- **Re-run evidence collection** (clinical trials, literature) once a candidate indication is confirmed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

