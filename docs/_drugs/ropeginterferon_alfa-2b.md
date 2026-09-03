---
layout: default
title: Ropeginterferon Alfa-2B
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Ropeginterferon Alfa-2B
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

# 洛培格干擾素 Alfa-2b（Ropeginterferon Alfa-2b）：原始適應症資料缺失 → 疑似假陽性訊號 Laubry-Pezzi Syndrome

## 一句話摘要

> 本藥物（DrugBank ID: DB15119）目前缺乏完整的原始適應症與作用機轉資料，且在德國尚未上市。
> TxGNN 模型將 **Laubry-Pezzi syndrome**（室中隔缺損合併主動脈瓣脫垂）列為第一預測適應症，
> 但**無任何臨床試驗與文獻支持**，且證據包內附之機轉分析已明確指出此為**無生物學合理性的假陽性預測**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（`original_indications` 為空、`original_moa` 未提供） |
| 預測新適應症 | Laubry-Pezzi syndrome |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 德國市場狀態 | ✗ 未上市 |
| 授權證號數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼此預測合理？

目前無法取得本藥物的作用機轉（MOA）資料，`original_indications` 欄位亦為空，故無法依標準流程比對原始適應症與新適應症之機轉關聯性。

**更關鍵的是，證據包本身提供的機轉分析已明確否定此預測的合理性**：Laubry-Pezzi syndrome 為室中隔缺損合併主動脈瓣脫垂的先天性結構性心臟病，屬解剖構造異常，與干擾素類藥物已知的免疫調節、抗病毒、JAK-STAT 路徑調控機轉並無生物學關聯。TxGNN 給出的高分（99.93%）僅反映知識圖譜中的節點嵌入相似度，並非機轉或臨床上的實質關聯，應判定為**假陽性預測**。

排名 2–5、7–10 的其餘候選適應症（室中隔動脈瘤、Pierre Robin 症候群、染色體 7q/22q 部分缺失、Jeune 症候群併內臟逆位、唇顎裂症候群、肺動脈瓣疾病）皆為先天性結構或發育性疾病，同樣缺乏機轉合理性與任何實證支持，性質與排名 1 相同。

值得特別提出的是**排名 6「disorder of fucoglycosan synthesis」**：此為罕見醣基化代謝疾病，但其附帶的 4 篇文獻主題**全部為真性紅血球增多症（polycythemia vera, PV）與 IFN-α／JAK2V617F 路徑研究**，與標記疾病名稱完全不符。這強烈提示知識圖譜中存在**疾病實體對應錯誤（label mismatch）**——真正有實證支持的疾病應是 PV（本藥物目前已知的臨床適應症之一），而非此罕見代謝疾病標籤。此發現不構成有效的「老藥新用」訊號，但應回報作為知識圖譜資料品質問題。

---

## 臨床試驗證據

目前無相關臨床試驗登記（Laubry-Pezzi syndrome）。

---

## 文獻證據

目前無相關文獻資料（Laubry-Pezzi syndrome）。

> 註：排名 6 候選（disorder of fucoglycosan synthesis）雖附有 4 篇文獻（PMID 33476571、32034662、40770048、32814349），但經核對主題均為 PV／IFN-α 治療研究，與該疾病標籤不符，判定為知識圖譜標籤錯配，不予採計為本次適應症之支持證據。

---

## 德國市場資訊

本藥物於德國**尚未上市**，無任何授權證號或核准適應症資料可供列示。

---

## 安全性考量

請參閱藥品仿單以取得安全性資訊。

> 補充：本候選案 Data Gap 清單標示 TFDA 仿單警語/禁忌（DG001，Blocking）與作用機轉（DG002，High）均缺失，前者已直接阻擋進入安全性初評（S1）階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名 1–10 的所有預測適應症證據等級均為 L5（僅模型預測、無實際研究支持），且排名 1 的機轉分析已明確判定為假陽性。
- 唯一附有文獻的候選（排名 6）經核實為知識圖譜疾病標籤錯配，實際文獻內容對應的是本藥物既有的 PV 適應症，非真正的新適應症訊號。
- 缺乏 MOA、TFDA 仿單警語與禁忌等關鍵藥物層級資料，無法進行機轉關聯性與安全性初評。

**若要繼續推進，需要補充：**
- 作用機轉（MOA）資料（DrugBank API 查詢）
- TFDA 仿單警語/禁忌資料（PDF 解析）
- 原始適應症正確清單（目前為空，實務上本藥物已知用於真性紅血球增多症，需以官方來源確認並補入）
- 知識圖譜疾病實體對應校驗，優先修正排名 6 之標籤錯配問題
- 若後續要重新評估，建議排除本批次 10 個候選，等待模型下一輪或人工複核產出具生物學合理性的新訊號
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

