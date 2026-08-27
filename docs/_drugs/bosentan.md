---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan：藥物再利用評估 — 資料不足，無法完整評估

## One-Sentence Summary

Bosentan（DrugBank ID：DB00559）為本次老藥新用候選藥物，但目前 Evidence Pack 中**無 TxGNN 預測新適應症**、**無原始適應症記錄**、**無安全性資料**，且在臺灣尚未上市，現階段無法執行標準再利用評估流程。在補齊關鍵資料缺口之前，建議暫緩本候選案的評估推進。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| Original Indication | 現有資料中無記錄 |
| Predicted New Indication | 無（TxGNN 未產生預測結果） |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5（僅有模型層級，無任何實際研究） |
| Taiwan Market Status | ✗ 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

目前詳細的作用機轉資料無法取得。根據現有資料，Bosentan（DB00559）已透過 DrugBank 成功查詢到基本藥物記錄，但機轉欄位（MOA）仍為資料缺口，尚待透過 DrugBank API 補齊。

原始核准適應症亦未記錄於本次 Evidence Pack 中（`original_indications` 為空陣列），TFDA 藥品查詢回傳結果數為 0，顯示此藥物在臺灣並無核准上市紀錄可供參照。

由於 TxGNN 未產生任何預測適應症（`predicted_indications` 為空陣列），機轉關聯性分析與新適應症合理性評估均無法在現階段執行。

---

## Clinical Trial Evidence

目前無相關臨床試驗登錄資料。

---

## Literature Evidence

目前無相關文獻資料。

---

## Taiwan Market Information

Bosentan 目前在臺灣**未上市**，TFDA 查詢結果顯示無任何藥品許可證記錄（查詢日期：2026-03-29，查詢結果數：0）。

---

## Safety Considerations

請參閱藥品仿單之警語與禁忌事項。

> **注意**：TFDA 仿單查詢雖回傳成功（`result_count: 1`），但安全性欄位（警語、禁忌）尚未解析入 Evidence Pack。此為 **Blocking 級資料缺口（DG001）**，在補齊前無法進行 S1 安全性初評。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本 Evidence Pack 缺少 TxGNN 預測適應症、原始適應症、MOA 及安全性資料等核心欄位，現階段無法對 Bosentan 的再利用潛力進行有效評估；在主要資料缺口填補完畢前，建議暫緩推進。

**To proceed, the following is needed:**

- **\[DG001 — Blocking\]** 解析 TFDA 仿單 PDF，提取警語（key warnings）與禁忌（contraindications），以解除 S1 安全性初評封鎖
- **\[DG002 — High\]** 透過 DrugBank API 補齊作用機轉（MOA）資料，以支援機轉關聯性分析
- 重新執行 TxGNN 預測流程，確認是否產生 Bosentan 的新適應症預測結果；若仍為空，需釐清原因（節點未收錄、分數過低或已被過濾）
- 補齊原始核准適應症（`original_indications`），可從 DrugBank、EMA 或 FDA 標籤取得
- 重新查詢 DDI 資料庫（目前查詢狀態為 `not_found`），確認是否有藥物交互作用資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

