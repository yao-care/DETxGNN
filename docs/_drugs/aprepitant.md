---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant：從止吐藥物到抗利尿激素分泌不當症候群（腎因型）的老藥新用探索

## 一句話總結

> Aprepitant（DB00673）為 NK1 受體拮抗劑類止吐藥物（目前尚未於台灣上市）。
> TxGNN 模型預測其可能對 **腎因型抗利尿激素分泌不當症候群（nephrogenic syndrome of inappropriate antidiuresis）** 有效，
> 但目前**沒有任何臨床試驗或文獻佐證**，僅為模型純預測分數，證據等級為 L5。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 未於本次 Evidence Pack 中提供（`original_indications` 為空） |
| 預測新適應症 | Nephrogenic syndrome of inappropriate antidiuresis（腎因型抗利尿激素分泌不當症候群） |
| TxGNN 預測分數 | 99.97%（rank 616） |
| 證據等級 | L5（僅模型預測，無臨床試驗、無文獻） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼此預測合理？

目前尚無作用機轉（MOA）資料（`original_moa: [Data Gap]`），此為本案的高嚴重度資料缺口（DG002），需另行查詢 DrugBank 補齊。在缺乏機轉資料與原始適應症紀錄的情況下，無法對「止吐藥物」與「腎因型抗利尿激素分泌不當症候群」之間的藥理連結做出實質評估。

`repurposing_rationale.mechanistic_link` 明確標註：「無已知機轉關聯，亦無任何臨床試驗或文獻資料，僅為模型預測分數。」這代表此預測目前完全依賴 TxGNN 的知識圖譜相似度推論，尚未有任何生物學或臨床層面的佐證支持。

**其他候選適應症觀察（供參考，非本次評估主軸）：**

| Rank | 適應症 | TxGNN 分數 | 備註 |
|------|--------|-----------|------|
| 3 | Pulmonary hypertension | 99.90% | 唯一附帶文獻為 pazopanib+cisplatin 治療腎細胞癌之 Phase I 試驗，與 aprepitant 及肺高壓皆無關聯，判定為檢索雜訊 |
| 6 | Malformation syndrome with odontal/periodontal component | 99.86% | 附帶 20 篇文獻皆為牙周病相關研究，與 aprepitant 無機轉關聯，同樣判定為檢索雜訊 |
| 9 | Subarachnoid hemorrhage | 99.85% | 文獻界已知 Substance P/NK1R 路徑參與 SAH 後血腦障壁破壞與腦水腫（多為動物模型證據），機轉上具理論可能性，但本次未檢索到任何實際臨床試驗或文獻，仍屬純模型分數 |

以上顯示：分數高並不等於證據強，rank 3、6 的附帶文獻經比對後均為不相關雜訊，rank 9 雖有理論機轉可能性但同樣缺乏實證，需列為未來優先文獻補查對象。

---

## 臨床試驗證據

目前無相關已註冊之臨床試驗。

## 文獻證據

目前無相關文獻資料可供評估。

## 台灣市場資訊

Aprepitant 目前**未於台灣上市**，無核准藥品許可證（`total_licenses: 0`），亦無劑型／給藥途徑資料。

---

## 安全性考量

- **仿單警語／禁忌**：TFDA 仿單資料尚未取得（DG001，Blocking 等級缺口），需下載官方仿單 PDF 解析後才能進行 S1 安全性初評。
- **藥品交互作用**：查詢結果為 `not_found`，目前無資料。

> 請注意：由於仿單資料缺失屬於 Blocking 等級缺口，本案**尚未能進行完整安全性評估**，暫以「請參考藥品仿單所載安全性資訊」為原則，待補齊後應重新評估。

---

## 結論與後續建議

**決策：Hold**

**理由：**
- 預測新適應症僅有 TxGNN 模型分數支持（L5），無任何臨床試驗或文獻證據；
- 原始適應症與作用機轉資料缺失，無法建立機轉關聯性論證；
- TFDA 仿單安全性資料為 Blocking 等級缺口，尚無法完成基本安全性初評；
- 藥品目前未於台灣上市，無許可證與劑型資訊。

**若要推進，需要補齊：**
- 下載並解析 TFDA 官方仿單，取得警語、禁忌、劑型資訊（DG001）
- 查詢 DrugBank API 取得 aprepitant 完整作用機轉資料（DG002）
- 針對 rank 9（subarachnoid hemorrhage）之 Substance P/NK1R 機轉假說進行專門文獻檢索，確認是否有可用實證
- 排除 rank 3、rank 6 之雜訊文獻，避免誤判為支持證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

