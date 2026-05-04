---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: Repurposing Evaluation — Pending Predicted Indication

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically established for chronic myelogenous leukemia (CML) and pre-transplant conditioning regimens prior to hematopoietic stem cell transplantation (HSCT). The current evidence pack contains **no TxGNN-predicted new indications**, and critical data including mechanism of action and safety information remain unresolved. This report documents the current data status and defines the remediation steps required before repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myelogenous leukemia / pre-transplant conditioning (based on established pharmacological knowledge; Taiwan package insert not retrieved) |
| Predicted New Indication | None generated in current evidence pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | Cannot be determined |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Since the TxGNN pipeline returned no predicted indications in this evidence pack, a formal mechanistic bridge analysis cannot be performed at this stage.

From established pharmacological knowledge, busulfan is a bifunctional alkylating agent that cross-links DNA strands, disrupting replication in rapidly dividing cells. This mechanism underlies its long-standing use in CML (myelosuppression as therapeutic intent) and its role as a myeloablative conditioning agent before HSCT to eliminate residual haematopoietic cells prior to donor engraftment.

To evaluate whether this mechanism is applicable to any new indication, TxGNN predictions must first be generated and reviewed. Once candidate disease associations are available, mechanistic plausibility can be assessed in the context of shared biological pathways.

---

## Cytotoxicity

Busulfan is an antineoplastic alkylating agent; cytotoxicity assessment applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (bifunctional alkyl sulphonate) |
| Myelosuppression Risk | High — severe, prolonged myelosuppression is the primary dose-limiting toxicity; nadir typically at 11–30 days |
| Emetogenicity Classification | Moderate (standard-dose oral regimen); High (high-dose IV conditioning) |
| Monitoring Items | CBC with differential (daily during conditioning), liver function tests, renal function, busulfan plasma levels (therapeutic drug monitoring for IV conditioning), serum electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV formulation requires dedicated closed-system drug transfer device |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Taiwan package insert retrieval returned a positive result in the query log (query ID 4, status: success), but the parsed content was not included in this evidence pack. Warnings and contraindications should be extracted from that source as the next remediation step.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is missing TxGNN predictions entirely, and both MOA and safety data remain unresolved — making it impossible to evaluate any repurposing hypothesis or perform a safety pre-screen at this stage.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** — generate candidate disease associations for Busulfan (DB01008) so that a repurposing hypothesis can be identified
- **Extract Taiwan package insert content** — the query log confirms a successful retrieval (query ID 4); parse warnings, contraindications, and dosage information from the retrieved document
- **Query DrugBank API for full MOA data** — populate mechanism of action to enable target-pathway analysis
- **Retrieve DDI data** — query drug interaction databases (DDI query returned not_found; broaden search scope or use alternative sources)
- **Re-submit evidence pack** — once the above four items are resolved, re-generate the evidence pack and proceed to full repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

