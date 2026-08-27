---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

The `txgnn-pipeline` skill covers infrastructure/pipeline work, while this task is pure report generation as defined by the system prompt. I'll proceed directly with producing the Markdown report from the Evidence Pack.

---

# Buprenorphine: Repurposing Candidate — No Prediction Data Available

## One-Sentence Summary

Buprenorphine (DB00921) is a registered pharmaceutical compound, but this Evidence Pack contains no recorded original indications and no TxGNN-predicted new indications.
Without a target indication, a formal drug repurposing assessment cannot be completed at this stage.
Data remediation is required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN-predicted indications and no original indication data, making it impossible to conduct a repurposing assessment or evaluate mechanistic plausibility.

**To proceed, the following is needed:**

- **TxGNN prediction output** — `predicted_indications` is currently empty; the model must be re-run or results ingested for this candidate
- **Original indication data** — `original_indications` is empty; retrieve from TFDA or DrugBank approved indication fields
- **Mechanism of action (MOA)** — flagged as Data Gap (DG002, High severity); query DrugBank API (DB00921) to populate `original_moa`
- **Safety data** — `key_warnings` and `contraindications` are both flagged as Data Gap (DG001, Blocking severity); download and parse the TFDA package insert PDF to unblock S1 safety screening
- **DDI data** — drug–drug interaction query returned `not_found`; consider querying additional sources (e.g., DrugBank interactions endpoint, Lexicomp)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

