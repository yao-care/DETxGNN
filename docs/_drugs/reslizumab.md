---
layout: default
title: Reslizumab
parent: Nur Modellvorhersage (L5)
nav_order: 337
evidence_level: L5
indication_count: 2
---

# Reslizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Reslizumab: Eosinophilic Asthma Biologic — Repurposing Analysis Incomplete

## One-Sentence Summary

Reslizumab is a humanized anti-interleukin-5 (IL-5) monoclonal antibody approved internationally (US Cinqair, EU Cinqaero) for severe eosinophilic asthma in adults, but not yet registered in Taiwan.
The current Evidence Pack contains **no TxGNN prediction results**, meaning no repurposing candidate can be evaluated at this stage.
Two blocking data gaps — Taiwan package insert warnings and mechanism of action details — must be resolved before this analysis can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (add-on maintenance therapy in adults) |
| Predicted New Indication | Not available — TxGNN output absent from this Evidence Pack |
| TxGNN Prediction Score | — |
| Evidence Level | — |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Taiwan Market Information

No TFDA authorizations are on record. Reslizumab holds international approvals (FDA 2016, EMA 2016) for severe eosinophilic asthma, but has not obtained TFDA registration as of the data cutoff (2026-04-20). No authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan package insert data could not be retrieved in this pipeline run. The DDI database returned no interactions. Both warning and contraindication fields require supplementation before any safety assessment is possible.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing TxGNN prediction results and has two unresolved data gaps rated *Blocking* and *High* severity respectively; there is no candidate indication to evaluate, and no safety baseline to assess against.

**To proceed, the following is needed:**
- Run the TxGNN prediction pipeline for DB06602 and populate `predicted_indications`
- Download and parse the TFDA package insert PDF to extract warnings and contraindications (resolves DG001 — Blocking)
- Query DrugBank API to retrieve mechanism of action details (resolves DG002 — High)
- Re-generate Evidence Pack (v5+) with complete inputs before re-running this report
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

