---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Anagrelide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Anagrelide：從 Essential Thrombocythemia 到 Reactive Thrombocytosis

## 摘要

Anagrelide 是用於治療 essential thrombocythemia（ET，一種克隆性骨髓增生性腫瘤）的口服藥物。TxGNN 模型預測其可能對 **Reactive Thrombocytosis（反應性血小板增多症）** 有效，目前有 **0 項臨床試驗**與 **10 篇相關文獻**支持此方向，但證據性質多為間接外推。

## 概覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | Essential thrombocythemia (ET)（國際核准適應症；台灣未上市，無本地仿單資料） |
| 預測新適應症 | Reactive Thrombocytosis（反應性血小板增多症） |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L4（僅回顧性文獻/機轉研究，無直接針對此適應症之臨床試驗） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold（暫緩）** |

## 這個預測合理嗎？

官方 MOA 欄位為資料缺口，但根據文獻佐證的機轉描述，anagrelide 透過抑制 PDE3（磷酸二酯酶第 3 型），干擾巨核細胞成熟與血小板生成，藉此降低血小板數量。理論上，此機轉不分病因皆可降低血小板數，因此對克隆性（ET）與反應性血小板增多症皆有藥理學上的可行性。

然而，anagrelide 目前核准適應症與絕大多數文獻證據都集中在 ET，而非反應性血小板增多症。兩者病理本質不同：ET 血小板具功能異常、血栓栓塞風險高；反應性血小板增多症通常血小板功能正常，會隨潛在病因（感染、發炎、缺鐵、脾切除等）緩解而自行恢復。國際治療指引並不建議對反應性血小板增多症常規使用細胞減量藥物，因其血栓風險本身較低，用藥反而須承擔心律不整、體液滯留等副作用風險。因此，現有 10 篇文獻多屬對 ET 的回顧性描述，僅間接提及「reactive thrombocytosis」作為鑑別診斷概念，並非直接支持此新適應症的療效證據。

## 臨床試驗證據

目前無相關已註冊臨床試驗。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | Anagrelide 作用機轉與治療潛力更新，聚焦克隆性血小板增多症治療選項 |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leukemia & Lymphoma | 反應性血小板增多症通常無須治療；克隆性血小板增多症才需細胞減量治療 |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Australia | ET 診斷需排除其他骨髓增生性疾病與反應性血小板增多症 |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | 血小板增多症與血小板增多之臨床光譜綜述，涵蓋反應性與克隆性成因 |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review (case-based) | Leukemia Research | 骨髓增生性腫瘤極端血小板增多之當代處置，藥物治療為主流 |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Jpn J Clin Hematol | ET 診斷治療綜述，anagrelide 為抑制巨核細胞增生藥物之一 |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective Cohort | Pediatr Blood Cancer | 兒童 ET 與反應性血小板增多症之回溯性比較，12 例分析 |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srp Arh Celok Lek | ET 合併僵直性脊椎炎個案，以 anagrelide 併用治療 |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | Eur J Case Rep Intern Med | ET 患者使用 anagrelide 治療期間發生急性心肌梗塞之個案 |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | 脾切除後血小板增多症患者之斷指再植個案 |

## 台灣上市資訊

Anagrelide 目前在台灣**未上市**，無許可證資料。

## 安全性考量

請參閱藥品仿單以取得安全性資訊（目前尚無 TFDA 仿單警語、禁忌症及藥品交互作用資料）。

## 結論與後續建議

**決策：Hold（暫緩）**

**理由：**
現有 10 篇文獻皆非直接針對「反應性血小板增多症」的療效證據，多為 ET 相關回顧或個案報告；且國際指引不建議對反應性血小板增多症常規使用細胞減量藥物，證據強度僅達 L4。此外，安全性資料（仿單警語、禁忌症）與 MOA 官方資料均為缺口，尚無法通過 S1 安全性初評（DG001 為 Blocking 等級）。

**如欲推進，需補充：**
- TFDA 仿單 PDF 解析，取得正式警語與禁忌症（DG001）
- DrugBank 官方 MOA 資料以強化機轉關聯性分析（DG002）
- 針對反應性血小板增多症族群的直接臨床證據（目前為零筆試驗）
- 釐清此適應症之臨床必要性（是否符合治療指引建議介入之族群）

---

*附註：第二候選適應症「inverse Klippel-Trenaunay syndrome」（TxGNN 分數 99.59%）無任何文獻或試驗支持，證據等級 L5，機轉上與 anagrelide 之 PDE3 抑制作用無合理連結，建議直接排除，不進入後續評估。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

