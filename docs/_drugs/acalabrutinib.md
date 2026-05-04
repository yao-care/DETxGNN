---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 0
---

# Acalabrutinib
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

# Acalabrutinib: Drug Repurposing Evaluation Report

## One-Sentence Summary

Acalabrutinib (Calquence®) is a second-generation selective Bruton's tyrosine kinase (BTK) inhibitor, approved internationally for chronic lymphocytic leukaemia (CLL)/small lymphocytic lymphoma (SLL) and mantle cell lymphoma (MCL). The TxGNN model has **not generated any predicted new indications** for this drug at this time. The drug is **not marketed in Taiwan** and has **no TFDA authorizations** on record.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLL/SLL, Mantle Cell Lymphoma (not listed in TFDA; based on international approvals) |
| Predicted New Indication | — (No TxGNN predictions available) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not available |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, no TxGNN predicted indications have been generated for acalabrutinib. Therefore, a mechanistic plausibility assessment cannot be performed at this time.

For reference, acalabrutinib is a highly selective, covalent inhibitor of Bruton's tyrosine kinase (BTK), a key signalling molecule in the B-cell antigen receptor pathway. BTK inhibition disrupts B-cell proliferation, trafficking, chemotaxis, and adhesion — mechanisms central to B-cell malignancies. It was designed as a more selective successor to ibrutinib, with reduced off-target kinase inhibition (e.g., EGFR, ITK, TEC), resulting in a potentially improved safety profile.

Given its targeted mechanism on the BTK pathway, potential repurposing opportunities could theoretically extend to other BTK-dependent conditions, including certain autoimmune diseases (e.g., rheumatoid arthritis, lupus) and other B-cell-driven malignancies. However, without TxGNN model output, no specific assessment can be made.

---

## Clinical Trial Evidence

No TxGNN-predicted indications are available; therefore, no indication-specific clinical trial search was performed.

> Currently no related clinical trials registered for a predicted new indication.

---

## Literature Evidence

No TxGNN-predicted indications are available; therefore, no indication-specific literature search was performed.

> Currently no related literature available for a predicted new indication.

---

## Taiwan Market Information

Acalabrutinib currently holds **no TFDA authorizations** and is **not marketed in Taiwan (未上市)**.

> No Taiwan authorization records available.

---

## Cytotoxicity

Acalabrutinib is an antineoplastic agent (BTK inhibitor for haematological malignancies) and therefore requires cytotoxicity consideration.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Small-molecule kinase inhibitor — BTK selective) |
| Myelosuppression Risk | Moderate — neutropenia, anaemia, and thrombocytopenia reported; Grade ≥3 neutropenia occurs in ~10–15% of patients |
| Emetogenicity Classification | Low (oral targeted agent) |
| Monitoring Items | CBC with differential (regularly), liver function tests (ALT/AST/bilirubin), signs of infection, bleeding events, atrial fibrillation/flutter monitoring, second primary malignancies screening |
| Handling Protection | Standard oral targeted therapy handling; no special cytotoxic drug handling precautions required (non-cytotoxic mechanism — does not directly damage DNA) |

---

## Safety Considerations

The Evidence Pack contains no TFDA package insert data for acalabrutinib (drug not marketed in Taiwan). Based on internationally available prescribing information:

- **Key Warnings**: Serious haemorrhagic events (including fatal events) have been reported. Atrial fibrillation/flutter has been observed; monitor patients with cardiac risk factors. Serious infections (including opportunistic infections) may occur. Second primary malignancies have been reported.
- **Contraindications**: Please refer to the originator's package insert (AstraZeneca — Calquence®) for complete contraindications, as TFDA labelling is not available.
- **Drug Interactions**: Acalabrutinib is a CYP3A substrate. Strong CYP3A inhibitors (e.g., ketoconazole, clarithromycin) increase acalabrutinib exposure — dose adjustment required. Strong CYP3A inducers (e.g., rifampicin, phenytoin) decrease exposure — avoid concomitant use. Proton pump inhibitors reduce absorption — avoid co-administration; use H₂-receptor antagonists or antacids with staggered dosing. Anticoagulants/antiplatelets increase bleeding risk.

> ⚠️ TFDA-specific labelling is unavailable (DG001 — Blocking data gap). The above is based on international prescribing information and must be verified against local labelling before any clinical decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted indications have been generated for acalabrutinib. Additionally, the drug is not marketed in Taiwan, and critical data gaps exist (TFDA package insert, formal MOA data in the evidence pack). Without a predicted target indication, no repurposing evaluation can proceed.

**To proceed, the following is needed:**
1. **TxGNN prediction output** — Re-run the TxGNN model to generate predicted indications for acalabrutinib (DB11703)
2. **MOA data gap closure (DG002)** — Query DrugBank API to populate the mechanism of action field formally in the evidence pack
3. **TFDA labelling (DG001 — Blocking)** — If acalabrutinib obtains TFDA authorization in the future, download and parse the package insert for local safety data
4. **International label reference** — In the interim, integrate FDA/EMA prescribing information as a proxy for safety assessment
5. **Taiwan market access assessment** — Evaluate whether named-patient import or clinical trial access pathways exist for potential repurposing studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

