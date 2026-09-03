---
layout: default
title: Metreleptin
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin：原始適應症資料缺失 → Familial Generalized Lentiginosis（家族性泛發性雀斑樣痣）

## 一句話摘要

Metreleptin（DrugBank ID: DB09046）為 leptin 受體促效劑，但本次 Evidence Pack 未提供其原始核准適應症與詳細作用機轉資料。TxGNN 模型將 **familial generalized lentiginosis** 列為排名第一的預測新適應症（分數 99.71%），但**目前無任何臨床試驗或文獻佐證**，屬純模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（Evidence Pack 未提供，licenses 為空） |
| 預測新適應症 | Familial generalized lentiginosis（家族性泛發性雀斑樣痣） |
| TxGNN 預測分數 | 99.71%（rank 3992） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前無法取得 metreleptin 詳細作用機轉資料（original_moa 為資料缺口）。根據一般已知資訊，metreleptin 是重組人類 leptin 類似物，作用於 leptin 受體，主要用於 leptin 缺乏相關之脂肪失養症（lipodystrophy）族群；然而本 Evidence Pack 中並未提供此原始適應症的正式核准文字，故無法在此報告中確認並列出。

排名第一的預測適應症 familial generalized lentiginosis 屬於 LEOPARD/Noonan 症候群譜系（RASopathy，色素沉著相關遺傳症候群），與 leptin 訊號通路之間**沒有已知的機轉關聯**。Evidence Pack 中的 repurposing rationale 也明確指出，此分數可能反映知識圖譜中罕見疾病節點資料稀疏所產生的雜訊關聯，而非具生物學合理性的預測。

進一步檢視排名 2–10 的候選適應症（gastrocutaneous syndrome、Moynahan syndrome、rhabdoid tumor、OPD-白瀏海症候群、CAL-SCE 症候群、acromelanosis、LAAN 症候群、腎上腺良性腫瘤、周邊神經鞘瘤），皆為極罕見遺傳症候群或與 leptin 生理學無已建立連結之腫瘤，且**全數無任何臨床試驗或文獻支持**，evidence level 均為 L5、建議皆為 Hold。整體而言，此批預測目前僅具探索性質，不具備進入臨床評估的證據基礎。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻可查。

---

## 台灣上市資訊

Metreleptin 目前未在台灣上市，無許可證資料。

---

## 安全性考量

請參考仿單以獲取安全性資訊。

（註：TFDA 仿單警語/禁忌資料為 **Blocking** 等級缺口 DG001，尚未取得；此為進入 S1 安全性初評前必須補齊之前提條件。）

---

## 結論與下一步

**決策：Hold**

**理由：**
前十名預測適應症之證據等級皆為 L5（僅模型分數，無臨床試驗或文獻佐證），且藥物本身之原始適應症、作用機轉、台灣仿單安全性資料均缺失（含 1 項 Blocking 缺口），目前無法進行任何安全性初評，故建議 Hold。

**若要推進，需要補齊：**
- TFDA 仿單警語/禁忌資料（DG001，Blocking，需下載仿單 PDF 解析）
- DrugBank MOA 詳細資料（DG002，需查詢 DrugBank API）
- Metreleptin 原始核准適應症之正式來源文字，以建立與預測適應症之機轉比對基礎
- 針對排名前 1–3 候選適應症，執行 PubMed／ClinicalTrials.gov／ICTRP 補充檢索，確認是否存在目前資料庫未收錄之間接證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

