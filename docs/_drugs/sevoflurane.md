---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane：從全身麻醉到 Prinzmetal 心絞痛（Prinzmetal Angina）

## 一句話摘要

Sevoflurane 是臨床廣泛使用的吸入性全身麻醉劑，用於麻醉誘導與維持。
TxGNN 模型預測其可能對 **Prinzmetal 心絞痛（變異型心絞痛）** 具治療潛力，
但目前**無任何臨床試驗、無任何文獻**支持此方向，純屬模型網絡外插結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 全身麻醉誘導與維持（吸入性麻醉劑；本 Evidence Pack 未提供正式仿單原始適應症文字） |
| 預測新適應症 | Prinzmetal Angina（變異型心絞痛） |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5（純模型預測，無實際研究） |
| 台灣市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測看起來合理？

目前尚未取得 Sevoflurane 詳細作用機轉（MOA）之結構化資料（DrugBank 查詢待補），
但依已知臨床藥理學，Sevoflurane 作為吸入性麻醉劑，已知可透過活化 **ATP 敏感性鉀通道（K_ATP channel）**
誘發「麻醉預適應（anesthetic preconditioning）」，對心肌缺血具一定程度的保護作用，此為其在心臟麻醉領域的已知輔助效益。

然而，Prinzmetal angina 的病理核心是**冠狀動脈痙攣**，其治療機轉聚焦於血管平滑肌鈣離子通道調節（如鈣通道阻斷劑），
與麻醉預適應所保護的「心肌缺血耐受性」屬不同層次的機轉路徑。兩者之間僅存在間接的「心肌保護」概念連結，
並無直接證據顯示 Sevoflurane 可緩解或預防冠狀動脈痙攣本身。此預測應視為 TxGNN 知識圖譜的統計外插，
而非具實證基礎的機轉假說。

---

## 臨床試驗證據

目前無相關已註冊臨床試驗。

---

## 文獻證據

目前無相關文獻資料。

---

## 台灣市場資訊

Sevoflurane 於本資料集中**尚未於台灣上市**，無許可證資料可供列示（`total_licenses = 0`）。

---

## 安全性考量

本候選藥物的關鍵安全性資料（TFDA 仿單警語、禁忌症、藥物交互作用）**目前均尚未取得**，
且此缺口已被標記為 **Blocking（DG001）**——在補齊之前，無法進入下一階段的安全性初評（S1）。
建議優先向 TFDA 官網下載正式仿單並解析警語與禁忌內容。

在資料補齊前，請暫以原廠仿單（package insert）之警告與注意事項為準。

---

## 結論與下一步

**決策：Hold**

**理由：**
排名第一的預測適應症（Prinzmetal angina）完全缺乏臨床試驗或文獻證據支持，機轉連結薄弱且屬間接推論；
同時，本候選藥物尚缺少 TFDA 仿單安全性資料（Blocking 等級缺口），不具備進入安全性初評的條件。
補充說明：本 Evidence Pack 中其餘 9 項預測適應症（Tourette syndrome、fibromyalgia、tendinitis、
idiopathic granulomatous myositis、myositis fibrosa、nephrogenic SIAD、trichotillomania、
migraine disorder、inclusion body myositis）亦均為 Hold，且現有文獻多屬「病患因原疾病接受手術麻醉」之
個案報告或麻醉方式比較研究，屬藥名與病名共現造成的混淆（confounding），並非治療性證據，
其中 nephrogenic SIAD 甚至可能因 Sevoflurane 代謝產生的無機氟離子腎毒性而構成潛在禁忌方向。

**若要繼續推進，需要補充：**
- TFDA 正式仿單 PDF 解析，取得警語與禁忌症（DG001，Blocking）
- DrugBank API 查詢完整作用機轉資料（DG002，High）
- 若欲驗證 Prinzmetal angina 假說，需補充體外/動物層級的冠狀動脈平滑肌機轉研究，作為啟動前瞻性臨床觀察的前提
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

