---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Prostate Cancer — Repurposing Evaluation (Predictions Pending)

## One-Sentence Summary

Cabazitaxel (Jevtana®) is a semi-synthetic taxane derivative approved internationally for metastatic castration-resistant prostate cancer (mCRPC) after prior docetaxel-based therapy.
This Evidence Pack **does not yet contain TxGNN repurposing predictions** — the prediction pipeline has not been completed due to unresolved data gaps (MOA and regulatory package insert).
Without prediction outputs, no new indication can be evaluated at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), second-line after docetaxel |
| Predicted New Indication | Not available — TxGNN predictions not yet generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (model predictions not yet run) |
| Market Status | Not marketed in this jurisdiction |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** — complete data pipeline before assessment |

---

## Drug Background

Cabazitaxel is a microtubule-stabilising agent belonging to the taxane class. It was developed specifically to overcome resistance to docetaxel, as it shows low affinity for P-glycoprotein — the efflux pump responsible for taxane resistance in many tumour cell lines.

Its primary mechanism involves binding to tubulin and inhibiting microtubule depolymerisation, thereby arresting cell division at the G2/M phase. This mechanism is broadly applicable across tumour types that rely on rapid cell division, making it a candidate of interest for repurposing beyond prostate cancer.

Cabazitaxel is approved by the FDA (2010) and EMA (2011) under the brand name Jevtana® for mCRPC. It is not currently marketed in this jurisdiction (0 local authorizations), which means importation or local registration would be required for any clinical application.

> **Note on MOA data gap:** The Evidence Pack lists MOA as a High-severity data gap (DG002). The background above is based on established pharmacological literature and should be formally confirmed via DrugBank API before proceeding to a full repurposing analysis.

---

## Why No Repurposing Assessment is Possible Yet

The Evidence Pack is incomplete:

| Data Gap | Severity | Impact |
|----------|----------|--------|
| TFDA package insert (warnings/contraindications) | **Blocking** | Cannot complete S1 safety screening |
| Mechanism of action (MOA) | High | Cannot perform mechanistic similarity analysis |
| TxGNN prediction output | Critical | No new indication predicted — `predicted_indications: []` |

The `predicted_indications` array is empty, which means either:
1. The TxGNN prediction step has not yet been run for this drug, **or**
2. The prediction pipeline was blocked by the upstream data gaps above.

Until TxGNN produces a ranked list of candidate indications, there is no repurposing target to evaluate.

---

## Cytotoxicity

Cabazitaxel is a cytotoxic chemotherapy agent. The following applies regardless of repurposing target.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class |
| Myelosuppression Risk | **High** — Febrile neutropenia is the most common serious adverse event; G-CSF prophylaxis is standard of care |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during first cycle), liver function, renal function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system transfer devices required |

---

## Safety Considerations

The Evidence Pack contains no actionable safety data for this drug in this jurisdiction. Before any clinical or regulatory work proceeds:

> Please refer to the EMA SmPC (Jevtana®) and current TFDA package insert for complete warnings, contraindications, and drug interaction information. The most critical known risks are febrile neutropenia, severe hypersensitivity reactions, and gastrointestinal toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Cabazitaxel is missing both its TxGNN repurposing predictions and the blocking safety data required for S1 screening. There is no new indication to evaluate, and no safety baseline to assess against.

**To proceed, the following is needed:**

1. **Resolve DG001 (Blocking):** Download and parse the TFDA package insert PDF to extract warnings and contraindications — required to unlock the S1 safety gate.
2. **Resolve DG002 (High):** Query DrugBank API for formal MOA data to enable mechanistic similarity analysis.
3. **Re-run TxGNN prediction pipeline** for DB06772 — the `predicted_indications` array must be populated before any repurposing evaluation can begin.
4. **Review EMA SmPC** for Jevtana® as a supplementary safety reference, given the drug is approved in Europe but not in this jurisdiction.
5. Once predictions are available, reassess evidence level and decision recommendation per standard L1–L5 criteria.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

