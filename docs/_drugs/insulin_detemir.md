---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir：從糖尿病（原適應症資料缺失）到第一型糖尿病之訊號確認

## 一句話摘要

> Insulin Detemir（Levemir®）是一種長效基礎胰島素類似物，原始核准適應症資料在本資料集中缺失，但已知其為第一型與第二型糖尿病之基礎胰島素治療藥物。TxGNN 預測其對**第一型糖尿病（Type 1 Diabetes Mellitus）**具高度相關性（分數 99.77%），並有 **60 篇以上完成之臨床試驗**與 **20 篇文獻**支持——但需特別注意：此為藥物**既有核准適應症之訊號確認**，並非真正意義上的「老藥新用」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料未提供具體核准文字（`taiwan_regulatory.licenses` 為空、藥品未於德國上市）；已知為基礎胰島素，用於糖尿病血糖控制 |
| 預測新適應症 | 第一型糖尿病（Type 1 Diabetes Mellitus）——**註：此實為 Levemir® 既有上市適應症，非真正新用途** |
| TxGNN 預測分數 | 99.77%（rank 3222） |
| 證據等級 | L1（≥2 個已完成 Phase 3 RCT） |
| 德國市場狀態 | ✗ 未上市 |
| 授權數量 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為何此預測合理？

目前尚無詳細的作用機轉（MOA）資料。根據已知資訊，Insulin Detemir 屬於長效基礎胰島素類似物，透過與 14 碳脂肪酸側鏈可逆性結合白蛋白，達到緩慢吸收、作用時間延長至約 24 小時的效果，藥效學上較 NPH 胰島素穩定、低血糖風險較低。

Insulin Detemir 直接替代第一型糖尿病患者因自體免疫破壞胰臟 β 細胞而喪失的內生性胰島素分泌，機轉關聯為**直接且已臨床驗證**，而非透過間接路徑推論的老藥新用假說。

**重要說明**：本資料集中 `original_indications` 欄位為空，屬資料缺口，但 Insulin Detemir（商品名 Levemir®）在多國早已核准用於第一型與第二型糖尿病治療。因此 TxGNN 排名第 1 的「第一型糖尿病」預測，實質上是**確認既有已知適應症**，而非發現新用途。其分析與證據價值在於：驗證 TxGNN 模型在已知藥物-疾病關係上的預測準確性，可作為模型可信度的正向對照，但不構成商業上「老藥新用」的機會。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT00542399](https://clinicaltrials.gov/study/NCT00542399) | Phase 4 | 已完成 | 50 | 比較兒童與青少年 T1DM 患者每日一次 vs 兩次注射 Insulin Detemir 之代謝控制 |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | 已完成 | 131 | RCT 交叉試驗，比較 Detemir 與 NPH 胰島素於 T1DM 患者中低血糖發生頻率 |
| [NCT00537303](https://clinicaltrials.gov/study/NCT00537303) | Phase 4 | 已完成 | 296 | 每日一次 Detemir 加階梯式添加短效 Aspart 之安全性與有效性比較 |
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | 已完成 | 501 | 2 年期 Detemir 與 NPH 於 T1DM 之療效（HbA1c）與安全性（低血糖、體重、抗體）比較 |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | 已完成 | 347 | 兒童與青少年 T1DM，Detemir 一日一次或兩次 vs NPH 之療效安全性比較 |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | 已完成 | 470 | 妊娠合併 T1DM 婦女，Detemir 與 NPH 之血糖控制與安全性比較 |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | 已完成 | 752 | 6 個月期，T1DM 患者基礎-餐前療法下 Detemir（2400 nmol/mL 劑型）與 NPH 之療效安全性比較 |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | 已完成 | 114 | 成人 T1DM，Detemir + Aspart 與 NPH + Aspart 之療效安全性比較 |
| [NCT02922179](https://clinicaltrials.gov/study/NCT02922179) | N/A | 已完成 | 103,951 | 大型描述性分析，成人糖尿病患者使用長效/中效胰島素之特徵（間接支持性流行病學資料） |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | 已完成 | 4,464 | 大型上市後觀察性研究，評估 Levemir® 於 T1DM/T2DM 患者之安全性、血糖控制與體重 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 試驗：妊娠合併 T1DM 婦女，Insulin Degludec 與 Detemir（皆併用 Aspart）之非劣性比較 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧/網絡統合分析 | Value in Health | 成人 T1DM 基礎胰島素治療方案之相對療效與安全性網絡統合分析 |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane 系統性回顧 | Cochrane Database Syst Rev | (超)長效胰島素類似物於 T1DM 患者之系統性回顧 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 系統性回顧/統合分析 | Pol Arch Med Wewn | Detemir 與 NPH 於 T1DM 之系統性回顧與統合分析 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 系統性回顧/統合分析 | Clin Ther | Insulin Degludec 與其他長效基礎胰島素（含 Detemir）於 T1DM/T2DM 之療效耐受性比較 |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | 妊娠合併 T1DM 之生活型態、藥物治療與新技術管理更新 |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | 兒童青少年 T1DM 胰島素類似物製劑之應用回顧 |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin Detemir 於第一型與第二型糖尿病管理之應用回顧 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Insulin Detemir 於第一型與第二型糖尿病治療之回顧 |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Insulin Detemir 於第一型與第二型糖尿病之焦點回顧 |

---

## 德國市場資訊

Insulin Detemir 目前**未於德國上市**（`total_licenses = 0`），資料集中無任何授權紀錄可供列表。

---

## 安全性考量

請參閱藥品仿單以取得完整安全性資訊。

（本資料集之關鍵警語、禁忌症、藥物交互作用欄位均無可用資料，其中 TFDA/仿單警語與禁忌症已被列為 Blocking 等級資料缺口，須優先補齊。）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 針對第一型糖尿病，已有多個完成之 Phase 3 RCT（如 NCT01697657、NCT00184665、NCT03220425 等）與系統性回顧／Cochrane 回顧支持，證據等級達 L1，模型預測方向正確。
- 但此為 Insulin Detemir 之**既有核准適應症**，並非新發現用途，故不構成典型「老藥新用」商業機會；其價值在於驗證模型可信度，實際決策應聚焦於「是否推動德國上市」而非「新適應症開發」。

**推進前需補齊：**
- TFDA／德國仿單警語與禁忌症資料（Blocking，DG001）——為進入 S1 安全性初評之前提
- DrugBank 作用機轉（MOA）明確描述（High，DG002）
- 若考慮德國上市策略，需補齊 BfArM 申請所需之完整臨床資料包與藥物交互作用資料

**其餘 9 項預測適應症（rank 2–10）之處理建議：**
- Rank 4（thiamine-responsive dysfunction syndrome）與 Rank 7（pancreatic agenesis）屬機轉合理但無直接臨床證據之研究性問題（L4，Research Question），可作為未來個案研究方向，暫不投入資源。
- Rank 2、3、5、6（autoimmune oophoritis、opsismodysplasia、focal/classic stiff person syndrome 譜系）證據等級 L5，無機轉或臨床支持，建議 Hold。
- Rank 8、9、10（各類 lipodystrophy/lipoatrophy）存在**方向性疑慮**——這些極可能是胰島素注射部位脂肪代謝異常之已知不良反應，被 TxGNN 誤判為治療關聯，建議自候選清單移除或另行標記為安全性訊號，不宜按適應症流程處理。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

