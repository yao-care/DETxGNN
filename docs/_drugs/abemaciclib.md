---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Abemaciclib
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

# ABEMACICLIB: Drug Repurposing Evaluation Report

## One-Sentence Summary

Abemaciclib is a selective CDK4/6 inhibitor, primarily approved internationally for the treatment of HR-positive, HER2-negative advanced or metastatic breast cancer. The TxGNN model has **not yet generated predicted new indications** for this compound, and the evidence pack currently contains **no clinical trial or literature evidence** for repurposing candidates. This report serves as a baseline assessment pending completion of the prediction pipeline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current evidence pack (internationally approved for HR+/HER2− breast cancer) |
| Predicted New Indication | — (No TxGNN prediction available) |
| TxGNN Prediction Score | — |
| Evidence Level | **L5** (No prediction or supporting studies available) |
| Taiwan Market Status | ❌ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the TxGNN model has not produced a predicted new indication for abemaciclib, so a mechanistic plausibility assessment cannot be performed at this time.

Based on publicly available pharmacological knowledge, abemaciclib (brand name Verzenio®, Eli Lilly) is a selective inhibitor of cyclin-dependent kinases 4 and 6 (CDK4/6). These kinases play a critical role in cell cycle progression from G1 to S phase. By inhibiting CDK4/6, abemaciclib blocks the phosphorylation of retinoblastoma protein (Rb), thereby arresting tumour cell proliferation. It is approved by the US FDA, EMA, and other regulatory authorities for HR+/HER2− advanced breast cancer, both as monotherapy and in combination with endocrine therapy.

> ⚠️ **Data Gap:** The evidence pack lists the mechanism of action (MOA) as unavailable. The above description is based on established pharmacological literature. Once the DrugBank API query is completed (remediation item DG002), the MOA field should be populated for formal assessment.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted clinical trial search has been performed for repurposing candidates.

> To proceed, the TxGNN prediction pipeline must first generate candidate indications, after which clinical trial evidence can be systematically collected.

---

## Literature Evidence

Currently no TxGNN-predicted indication is available; therefore, no targeted literature search has been performed for repurposing candidates.

---

## Taiwan Market Information

Abemaciclib is currently **not marketed in Taiwan** (未上市). No TFDA drug licenses were found in the regulatory database query (queried 2026-03-29).

> **Note:** Abemaciclib is marketed internationally under the brand name **Verzenio®** (Eli Lilly) and is approved by the US FDA, EMA, and multiple other regulatory authorities.

---

## Cytotoxicity

Abemaciclib is an antineoplastic agent (CDK4/6 inhibitor, targeted therapy class). The following cytotoxicity profile is based on established pharmacological knowledge:

| Item | Content |
|------|------|
| Cytotoxicity Classification | **Targeted therapy** (selective CDK4/6 inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | **High** — Neutropenia is a very common adverse effect (reported in >40% of patients in pivotal trials); dose modifications may be required |
| Emetogenicity Classification | **Low to moderate** — Diarrhoea is more clinically significant than nausea/vomiting |
| Monitoring Items | CBC with differential (neutrophils particularly), liver function tests (ALT, AST, bilirubin), renal function, signs of venous thromboembolism, signs of interstitial lung disease |
| Handling Protection | Standard precautions for oral anticancer agents; no IV cytotoxic handling required (oral dosage form) |

> ⚠️ Detailed toxicity data from DrugBank was not available in this evidence pack. Please refer to the Verzenio® package insert for comprehensive warnings and precautions.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) is **not yet available** in the current evidence pack due to the following data gaps:

- **DG001 (Blocking):** TFDA package insert warnings/contraindications have not been retrieved — abemaciclib is not marketed in Taiwan, so no local labelling exists.
- **DG002 (High):** DrugBank MOA and safety detail query is pending.

> Please refer to the international package insert (Verzenio® US PI or EMA SmPC) for complete safety information. Key known safety concerns from international labelling include: diarrhoea, neutropenia, hepatotoxicity, venous thromboembolism, and interstitial lung disease/pneumonitis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted new indication has been generated for abemaciclib. Without a candidate indication, the repurposing evaluation cannot proceed to evidence assessment. Additionally, the drug is not marketed in Taiwan, and critical safety data (TFDA labelling) is unavailable.

**To proceed, the following is needed:**
- **Run TxGNN prediction pipeline** for abemaciclib (DB12001) to generate candidate repurposing indications
- **Resolve DG002:** Complete DrugBank API query to populate mechanism of action data
- **Resolve DG001:** Since abemaciclib is not marketed in Taiwan, consider using the US FDA or EMA labelling as a surrogate for safety assessment
- **Re-evaluate market access:** Determine whether abemaciclib has any pending TFDA applications or if the repurposing evaluation should reference international regulatory data
- **Re-run evidence collection** (clinical trials + literature) once a predicted indication is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

