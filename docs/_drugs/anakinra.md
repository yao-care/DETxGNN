---
layout: default
title: Anakinra
parent: 中證據等級 (L3-L4)
nav_order: 30
evidence_level: L3
indication_count: 10
---

# Anakinra
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Anakinra：邁向家族性地中海熱與其他 IL-1 介導自體發炎症候群

## 一句話摘要

> Anakinra 為重組型 IL-1 受體拮抗劑（IL-1 receptor antagonist），本證據包未提供其原始核准適應症之結構化資料。
> TxGNN 模型針對此藥物產出 **10 個候選新適應症**，多數屬自體發炎（autoinflammatory）疾病家族；
> 其中證據支持度最高者為 **家族性地中海熱（Familial Mediterranean Fever, FMF，體染色體隱性遺傳型）**，
> 目前有 **20 篇文獻**支持（無註冊臨床試驗），另有 **膿皰性自體發炎症候群（PAPA/PSTPIP1 相關疾病群）** 同樣達到可推進評估的證據等級。

---

## 快速總覽

> 本評估為多候選適應症證據包（`TW-DB00026-multi`），下表以證據等級最高、可行動性最強的候選 **FMF** 作為代表呈現；完整 10 項候選請見下方「所有預測適應症總覽」。

| 項目 | 內容 |
|------|------|
| 原始適應症 | 本證據包未提供（`original_indications` 為空、無台/德藥證資料） |
| 代表性預測新適應症 | Autosomal recessive familial Mediterranean fever（家族性地中海熱） |
| TxGNN 預測分數 | 99.89%（rank 1819） |
| 證據等級 | L3 |
| 德國市場狀態 | ✗ 未上市 |
| 藥證數量 | 0 |
| 建議決策 | Proceed with Guardrails（限定條件下推進） |

---

## 所有預測適應症總覽

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | Extracutaneous mastocytoma | 99.93% | L5 | S0 | Hold |
| 2 | Hepatic infarction | 99.89% | L5 | S0 | Hold |
| 3 | **Familial Mediterranean fever (AR)** | 99.89% | **L3** | S3 | **Proceed with Guardrails** |
| 4 | Aggressive systemic mastocytosis | 99.88% | L4 | S1 | Research Question |
| 5 | Hepatic veno-occlusive disease | 99.88% | L5 | S0 | Hold |
| 6 | Peliosis hepatis | 99.85% | L5 | S0 | Hold |
| 7 | Oligoarticular JIA (ANA-negative) | 99.85% | L4 | S1 | Research Question |
| 8 | Oligoarticular JIA (ANA-positive) | 99.85% | L4 | S1 | Research Question |
| 9 | **Pyogenic autoinflammatory syndrome (PAPA/PSTPIP1 群)** | 99.83% | **L3** | S3 | **Proceed with Guardrails** |
| 10 | Unclassified autoinflammatory syndrome | 99.81% | L4 | S1 | Research Question |

**關鍵觀察**：TxGNN 分數本身區辨力有限（前 10 名分數差距僅 0.13 個百分點），實際可行動性取決於文獻證據是否支持機轉——分數最高的前兩名（mastocytoma、hepatic infarction）反而完全無文獻／試驗佐證，屬純模型臆測（L5）；真正達到可推進門檻的是排名第 3 與第 9 的兩個自體發炎疾病家族。

---

## 為什麼這個預測合理？

本證據包未提供 anakinra 結構化的作用機轉（MOA）資料（`original_moa: [Data Gap]`，對應 `DG002`），但由各候選適應症的機轉關聯分析（`repurposing_rationale.mechanistic_link`）可還原其藥理基礎：**anakinra 為重組型 IL-1 受體拮抗劑（IL-1Ra），透過競爭性阻斷 IL-1 受體，抑制 IL-1α/IL-1β 介導之發炎訊息傳遞**。

這個機轉解釋了為何模型高度聚焦於「自體發炎症候群（autoinflammatory syndrome）」這一疾病家族：

- **FMF（rank 3）**：由 *MEFV* 基因突變導致 pyrin inflammasome 過度活化、IL-1β 大量釋放，是體染色體隱性遺傳的自體發炎疾病。IL-1 受體拮抗劑的機轉與此病理直接對應，臨床上 anakinra 早已是 colchicine-resistant FMF 的成熟真實世界用法（雖非本證據包收錄之官方適應症）。
- **Pyogenic autoinflammatory syndrome / PAPA 光譜（rank 9）**：由 *PSTPIP1* 基因突變導致 pyrin-PSTPIP1 交互作用異常、inflammasome 過度活化、IL-1β 過量分泌，機轉同樣直接對應 anakinra 之藥理作用，已有多篇病例系列與系統性回顧支持其臨床療效。

相對地，分數同樣極高的 mastocytoma（KIT 突變驅動）、hepatic infarction（血管阻塞）、hepatic veno-occlusive disease（內皮損傷／凝血活化）、peliosis hepatis（機轉未明）等候選，其病理核心並非 IL-1 介導發炎，機轉關聯薄弱，屬於模型分數與生物學合理性脫鉤的情況，**不建議僅憑 TxGNN 分數推進**。

Mastocytosis（rank 4）的文獻證據需特別注意：現有 2 篇文獻皆為 **Schnitzler syndrome**（IL-1 驅動之慢性蕁麻疹合併單株丙種球蛋白病）病例報告，並非典型 KIT D816V 驅動之 aggressive systemic mastocytosis，屬疾病實體錯配，不能直接視為該適應症的支持證據。

---

## 臨床試驗證據

目前所有 10 項預測適應症皆**無已註冊的相關臨床試驗**（`clinical_trials` 與 `ictrp_trials` 皆為空陣列）。這也是 FMF 與 PAPA 兩項候選僅達 L3（觀察性研究／病例系列層級）而非更高等級的主因。

---

## 文獻證據

### 適應症 3：家族性地中海熱（FMF）— 20 篇文獻，列前 10 篇

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | IL-1β 生物製劑治療 FMF 之回顧 |
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Review/Case series | Semin Arthritis Rheum | IL-1 標靶藥物於 FMF 之病例系列與文獻回顧 |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohort | Rheumatol Int | Canakinumab 對 colchicine/anakinra 抗藥或不耐受之 FMF 有效 |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Case series | JPMA | Anakinra／canakinumab 成功治療 4 名 colchicine 抗藥兒童 FMF |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case report | Joint Bone Spine | FMF 合併 spondyloarthritis 肌炎，anakinra 治療成功 |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case report | Nephrol Dial Transplant | Anakinra 成功治療 FMF 並於腎移植後追蹤 |
| [25945034](https://pubmed.ncbi.nlm.nih.gov/25945034/) | 2015 | Case series | Drug Des Devel Ther | Canakinumab 作為傳統治療無效 FMF 之搶救治療 |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case series | Nephrol Dial Transplant | IL-1 抑制劑於合併澱粉樣變性、腎衰竭之 FMF 效果顯著 |
| [26861613](https://pubmed.ncbi.nlm.nih.gov/26861613/) | 2016 | Cohort/Genetic | Gene | IL-1Ra 與 IL-4 基因多型性與 FMF 風險關聯（土耳其族群） |
| [30686512](https://pubmed.ncbi.nlm.nih.gov/30686512/) | 2019 | Review | Presse Med | FMF 疾病總論，含 pyrin/MEFV 機轉說明 |

### 適應症 9：膿皰性自體發炎症候群（PAPA/PSTPIP1 相關疾病群）— 19 篇文獻，列前 10 篇

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Systematic Review | Front Immunol | Anakinra／canakinumab 於 PSTPIP1 相關自體發炎疾病之療效與安全性系統性回顧 |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Case report/Review | Cureus | Anakinra 治療 PAPASH 光譜疾病之病例與文獻回顧 |
| [27448064](https://pubmed.ncbi.nlm.nih.gov/27448064/) | 2016 | Review | Hautarzt | 自體發炎疾病所致重症痤瘡，anakinra 治療角色 |
| [21745697](https://pubmed.ncbi.nlm.nih.gov/21745697/) | 2012 | Case report | J Am Acad Dermatol | PASH 症候群首次描述，與 PAPA 症候群之區辨 |
| [22161697](https://pubmed.ncbi.nlm.nih.gov/22161697/) | 2012 | Cohort | Arthritis Rheum | 5 名 PAPA 症候群患者之基因型／表型／臨床病程 |
| [21532836](https://pubmed.ncbi.nlm.nih.gov/21532836/) | 2010 | Review | Curr Genomics | PAPA 症候群臨床、分子與遺傳特徵回顧 |
| [38006373](https://pubmed.ncbi.nlm.nih.gov/38006373/) | 2023 | Review | Acta Dermatovenerol Croat | PAPA 症候群長期緩解之治療挑戰 |
| [34778321](https://pubmed.ncbi.nlm.nih.gov/34778321/) | 2021 | Case report/Review | Front Med | PSTPIP1 相關自體發炎疾病之腎臟侵犯 |
| [25683018](https://pubmed.ncbi.nlm.nih.gov/25683018/) | 2015 | Case report | Clin Exp Dermatol | PSTPIP1 新突變患者合併壞疽性膿皮病、痤瘡與潰瘍性結腸炎 |
| [28628471](https://pubmed.ncbi.nlm.nih.gov/28628471/) | 2017 | Case report | Clin Exp Rheumatol | PSTPIP1 E250K 突變之血液學表現與輕度自體發炎表型 |

其餘 8 項候選適應症（mastocytoma、hepatic infarction、aggressive systemic mastocytosis、hepatic VOD、peliosis hepatis、兩型 oligoarticular JIA、unclassified autoinflammatory syndrome）文獻證據為 0～2 篇，且多屬疾病實體不完全匹配或通論性回顧，暫不足以支持推進，詳見「所有預測適應症總覽」表。

---

## 德國市場資訊

Anakinra（DB00026）於本資料庫中標示為 **未上市（`market_status: 未上市`，`total_licenses: 0`）**，無可用藥證資料，故無法提供劑型／核准適應症文字。

---

## 安全性考量

本證據包之安全性欄位（`key_warnings`、`contraindications`）皆為資料缺口，且 `DG001`（TFDA 仿單警語/禁忌）標記為 **Blocking** 等級缺口，明確影響本案是否能進入 S1 安全性初評。

> 請參閱藥品仿單以獲取安全性資訊；在補齊仿單警語與禁忌症資料前，本案安全性尚無法完成初步評估。

---

## 結論與下一步

**決策：Proceed with Guardrails（限 FMF 與 PAPA/PSTPIP1 相關適應症）／Hold（其餘 8 項候選）**

**理由：**
- FMF 與 pyogenic autoinflammatory syndrome（PAPA 光譜）兩項候選機轉關聯明確（IL-1 驅動之 inflammasome 過度活化）、有多篇真實世界文獻支持，且為臨床已成熟採用之 off-label 用法，達 L3／S3，可在限定條件下推進。
- 其餘 8 項候選（含 TxGNN 分數最高的 mastocytoma、hepatic infarction）機轉關聯薄弱或完全無文獻／試驗佐證，屬 L4-L5，應維持 Hold，不宜僅憑模型分數推進。

**推進前需補齊：**
- **`DG001`（Blocking）**：TFDA／原廠仿單警語與禁忌症全文（下載並解析 PDF），此為進入 S1 安全性初評之前提。
- **`DG002`（High）**：DrugBank API 查詢完整 MOA 結構化資料，補強機轉關聯分析之嚴謹度。
- 原始核准適應症資料（本包 `original_indications` 為空），以利進行原適應症與新適應症之相似性比對。
- 針對 aggressive systemic mastocytosis 候選，需釐清文獻中 Schnitzler syndrome 與目標疾病實體（KIT D816V 驅動）之錯配問題，避免誤用個案證據。
- 若後續要推進 FMF／PAPA 候選之正式臨床評估，建議優先檢索是否存在相關前瞻性研究或註冊試驗（目前皆為 0）。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

