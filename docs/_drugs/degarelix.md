---
layout: default
title: Degarelix
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix：從 GnRH 拮抗劑療法到多毛症（Hypertrichosis）

## 一句話總結

> Degarelix 是一種 GnRH（促性腺激素釋放激素）拮抗劑，本證據包未附上正式的原始適應症與作用機轉來源（資料缺口 DG001、DG002）。
> TxGNN 模型預測其可能對 **Hypertrichosis（多毛症）** 有效，
> 但目前 **無任何臨床試驗** 與 **無任何直接相關文獻** 支持此方向，機轉連結本身也被標註為「極弱推論」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 證據包未提供（`original_indications` 為空陣列） |
| 預測新適應症 | Hypertrichosis (multi-hair growth) |
| TxGNN 預測分數 | 99.99%（rank 275） |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻支持） |
| 上市狀態 | 未上市 |
| 核准張數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼此預測可能／不可能合理

目前資料庫未提供 degarelix 的正式作用機轉（MOA 標記為資料缺口，DG002，嚴重度 High）與原始適應症來源。根據公開藥理學分類，degarelix 屬於 GnRH 受體拮抗劑，藉由抑制垂體 LH/FSH 分泌以降低性腺激素（如睪固酮）濃度，但此背景知識並非本次證據包所附之來源資料，僅供理解模型輸出時參考，**不應作為安全性或適應症擴充之依據**。

排名第一的預測適應症 hypertrichosis（多毛症），其 `repurposing_rationale` 明確指出：若為雄激素驅動之後天性多毛症，理論上降壓睪固酮可能減緩毛髮生長，但此推論「極弱」，且多毛症病因異質性高，**無任何直接文獻或試驗佐證**。這代表此預測目前僅停留在 embedding 相似度層級（L5 / S0），尚未有可驗證的生物學或臨床證據支持。

值得留意的是，排名第 4 的候選適應症（牙周／齒列相關發育症候群）雖附有 20 篇文獻，但經檢視後確認全部為一般牙周病學研究（如糖尿病與牙周病關聯、牙周治療指引等），**完全未提及 degarelix 或 GnRH 拮抗劑**，屬於關鍵字匹配所產生的雜訊，並非藥物特異性證據。其餘候選適應症（Ambras 症候群、Dandy-Walker 畸形、毛幹基因異常、蕁麻疹、性早熟等）之機轉連結也均被評為無合理生物學基礎或機轉方向相反（如 familial male-limited precocious puberty 屬 gonadotropin-independent 病理，GnRH 拮抗劑理論上無法作用）。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## 上市資訊

目前查無上市許可資料（`total_licenses = 0`，市場狀態：未上市）。

---

## 安全性考量

請參閱仿單以獲取安全性資訊。

（本證據包所附之關鍵警語、禁忌症、藥物交互作用查詢結果均為資料缺口；`DG001` 已標註為 Blocking 等級，缺乏此資料代表**無法完成 S1 安全性初評**。）

---

## 結論與後續步驟

**決策：Hold**

**理由：**
本候選藥物之 10 個預測適應症全數為 L5 等級（純模型預測，無臨床試驗或可信文獻支持），排名第一的 hypertrichosis 其機轉連結本身也被評為「極弱推論」；同時原始適應症、MOA、仿單安全性資料皆為缺口，尚不足以支持任何一項適應症進入下一階段評估。

**若要繼續推進，需要補充：**
- TFDA（或適用主管機關）官方仿單警語與禁忌症資料（DG001，Blocking，需下載並解析官方 PDF）
- Degarelix 正式作用機轉來源，如 DrugBank API 查詢結果（DG002，High）
- 針對 hypertrichosis 或其他候選適應症之直接臨床試驗或機轉研究文獻（目前完全缺乏）
- 重新檢視排名第 4 候選之文獻匹配邏輯，避免關鍵字雜訊誤導後續證據收集資源分配
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

