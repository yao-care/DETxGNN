---
layout: default
title: Relebactam Monohydrate
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 0
---

# Relebactam Monohydrate
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

# Relebactam Monohydrate: β-Lactamase Inhibitor — Repurposing Analysis Cannot Proceed

## One-Sentence Summary

Relebactam monohydrate is a β-lactamase inhibitor co-administered with imipenem-cilastatin, approved by the FDA in 2019 for serious hospital-acquired Gram-negative bacterial infections.
The current Evidence Pack contains **no TxGNN-predicted indications** and is missing critical inputs — mechanism of action and regulatory labeling — required to drive the repurposing pipeline.
Without predicted indications, a standard repurposing evaluation cannot be completed; **Hold** is the only defensible recommendation until data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hospital-acquired / ventilator-associated bacterial pneumonia; complicated intra-abdominal and urinary tract infections (with imipenem-cilastatin) |
| Predicted New Indication | — (No TxGNN prediction generated) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Drug Background

No TxGNN prediction was generated for relebactam monohydrate, so the standard "Why is this prediction reasonable?" analysis cannot be completed. The following background is provided from published literature to support future pipeline runs.

Relebactam is a bicyclic piperidine-based inhibitor of class A and class C serine β-lactamases (including KPC carbapenemases and AmpC enzymes). It does not possess intrinsic antibacterial activity; its function is to protect imipenem from enzymatic degradation, thereby restoring imipenem's potency against otherwise resistant organisms such as KPC-producing *Klebsiella pneumoniae* and imipenem-resistant *Pseudomonas aeruginosa*. The fixed-dose combination product (imipenem 500 mg / cilastatin 500 mg / relebactam 250 mg, brand name RECARBRIO™, Merck) was approved by the FDA in July 2019.

Mechanistic MOA data was not retrievable in this Evidence Pack (DG002). Until the MOA is formally encoded, the TxGNN knowledge graph cannot generate drug–disease link predictions for this compound.

---

## Taiwan Market Information

Relebactam monohydrate has **no TFDA-authorized products** in Taiwan as of the query date. No license records or dosage forms are available to display.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were retrievable from this Evidence Pack.

> **Note for analysts:** The TFDA package insert query returned a hit (query\_log ID 4, result\_count = 1), suggesting labeling text may be parseable. Extracting that content directly would resolve DG001 and unblock the safety section.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced no predicted indications because critical inputs — mechanism of action (DG002, severity: High) and TFDA package insert warnings (DG001, severity: Blocking) — were not successfully ingested. A repurposing evaluation built on an empty prediction set would carry no scientific validity.

**To proceed, the following is needed:**

1. **Resolve DG001 — Safety Labeling (Blocking):** The TFDA package insert query returned one result; parse that PDF to extract warnings, contraindications, and dosage information.
2. **Resolve DG002 — MOA (High):** Query DrugBank (query\_log ID 3 returned 1 result) to extract the pharmacological mechanism and encode it into the TxGNN knowledge graph.
3. **Re-run TxGNN pipeline:** Once MOA and labeling inputs are complete, regenerate `predicted_indications`.
4. **Improve database query matching:** Consider querying as plain `"relebactam"` (without the "monohydrate" salt suffix) in DrugBank, PubChem, and clinical trial registries to maximize retrieval hit rate.
5. **DDI lookup:** Retry drug–drug interaction query after resolving the INN suffix issue; current result is `not_found` with 0 interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

