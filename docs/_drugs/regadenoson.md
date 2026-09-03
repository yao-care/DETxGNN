---
layout: default
title: Regadenoson
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

The txgnn-pipeline skill covers pipeline management and doesn't alter the report-writing task. Proceeding with the evaluation report.

---

**Evidence Pack Analysis:**

| Field | Value |
|---|---|
| `predicted_indications` | **Empty** — no TxGNN output |
| `original_indications` | Empty |
| `original_moa` | [Data Gap] |
| `taiwan_regulatory.market_status` | 未上市 (0 licenses) |
| `safety` | All [Data Gap] |

Since `predicted_indications` is empty, the standard "From X → Y" report cannot be completed. The report below reflects the actual state of the pack with a **Hold** decision.

---

```markdown
# Regadenoson: Pharmacological Stress Agent — Repurposing Evaluation Incomplete

## One-Sentence Summary

Regadenoson (Lexiscan®) is a selective adenosine A2A receptor agonist approved in the
United States as a pharmacological stress agent for radionuclide myocardial perfusion
imaging (MPI).
This Evidence Pack **contains no TxGNN repurposing predictions** for Regadenoson, and
the drug is **not currently marketed in Taiwan**.
Evaluation cannot proceed to full repurposing analysis until the critical data gaps
documented below are resolved.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pharmacological stress agent for myocardial perfusion imaging (US; not approved in Taiwan) |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction absent; no supporting studies in pack |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack contains no TxGNN repurposing predictions for Regadenoson, and all
drug-level safety data (warnings, contraindications, drug interactions) are absent,
making a repurposing evaluation impossible at this stage.

**To proceed, the following is needed:**

- **TxGNN prediction output** — rerun the TxGNN pipeline with Regadenoson as input to
  obtain candidate repurposing indications and confidence scores
- **Mechanism of action (MOA)** — retrieve from DrugBank API (DB06213); severity
  flagged as High in this pack
- **Taiwan package insert safety data** — download and parse the TFDA package insert
  PDF to extract warnings and contraindications (flagged as Blocking)
- **Drug–drug interaction profile** — DDI query returned `not_found`; a targeted
  literature search or DrugBank DDI lookup is recommended
- **Original indication confirmation** — `original_indications` field is empty;
  confirm approved indication(s) from the authoritative label (FDA: MPI stress testing)
  and populate the Evidence Pack before resubmission
```

---

**報告說明：**

此 Evidence Pack（`TW-DB06213-multi v4`）存在兩個關鍵缺口：

1. **`predicted_indications` 為空陣列** — TxGNN 尚未對 Regadenoson 產生預測，標準「From X to Y」格式無法套用。
2. **所有安全性欄位均為 [Data Gap]** — TFDA 警語/禁忌（DG001，Blocking）尚未填入。

依照報告規則「有資料才列章節」，已省略：臨床試驗證據、文獻證據、台灣市場資訊（0 張許可證）、細胞毒性（非抗腫瘤藥物）等章節。建議補齊上述缺口後重新提交 Evidence Pack，再執行正式評估。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

