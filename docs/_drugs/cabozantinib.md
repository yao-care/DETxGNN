---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: Drug Repurposing Candidate — Pending TxGNN Evaluation

## One-Sentence Summary

Cabozantinib (DB08875) is a small-molecule kinase inhibitor with established antineoplastic activity, currently **not marketed in Taiwan** and with no authorized indications on record in this Evidence Pack. The TxGNN predicted indications field is **empty** in the current Evidence Pack, meaning no repurposing target has been generated yet. This report cannot render a complete repurposing evaluation until the missing data — particularly TxGNN predictions, original indication records, and MOA details — are supplied.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction not yet generated |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Cytotoxicity

Cabozantinib is a well-characterized multi-kinase inhibitor (VEGFR2, MET, RET, AXL) used clinically in oncology, meeting the antineoplastic criterion by drug class. Although the current Evidence Pack does not carry DrugBank category tags or confirmed MOA text, the drug name and DrugBank ID (DB08875) unambiguously identify it as a targeted antineoplastic agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (targeted agents carry lower haematologic toxicity than conventional cytotoxics; confirm with package insert) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (AST/ALT), renal function, thyroid function, blood pressure, urine protein |
| Handling Protection | Standard targeted-agent precautions; confirm cytotoxic handling requirements against institutional protocol and approved labelling |

> Full toxicity details (myelosuppression incidence, specific thresholds) are not available in this Evidence Pack. Please refer to the approved package insert warnings and precautions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key warnings, contraindications, and drug-drug interaction data are all absent from this Evidence Pack (Data Gap DG001). The DDI query returned zero results and no TFDA labelling text has been parsed. No safety data can be reported here without risking inaccuracy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — the `predicted_indications` array is empty and two blocking/high-severity data gaps (DG001: TFDA label text; DG002: MOA) remain unresolved. There is no repurposing target to evaluate, and no safety signal summary is available for risk assessment.

**To proceed, the following is needed:**

- **TxGNN predictions** — re-run the TxGNN pipeline for DB08875 and populate `predicted_indications` with at least one candidate disease
- **Original indication data** — retrieve approved indication text from TFDA package insert (remediation: download and parse TFDA PDF)
- **Mechanism of action (MOA)** — query DrugBank API for DB08875 pharmacodynamics and target profile (remediation per DG002)
- **Safety label text** — parse TFDA 仿單 for key warnings and contraindications (remediation per DG001)
- **DDI data** — re-query DDI database; current result is `not_found` with zero interactions, which may reflect a query failure rather than a true absence of interactions
- **Regulatory cross-check** — although Taiwan shows 0 licenses, Cabozantinib holds approvals in other jurisdictions (EMA, FDA); a cross-jurisdictional lookup would enrich the regulatory context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

