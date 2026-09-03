---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog Alfa：從凝血因子替代療法到 Primary Release Disorder of Platelets

## 一句話摘要

Turoctocog alfa 為重組 Factor VIII 製劑，本次 Evidence Pack 中 DrugBank 未提供其核准適應症與詳細作用機轉（資料缺口），但由模型 rationale 文字可知其臨床已知用途為凝血因子 VIII 替代療法。TxGNN 模型預測其可能對 **Primary Release Disorder of Platelets（血小板原發性釋放障礙）** 有效，但目前僅有 **0 篇臨床試驗** 與 **0 篇文獻** 支持，且模型自身給出的機轉論述已明確指出此連結缺乏生物學合理性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺口（DrugBank original_indications 為空；台灣未上市無許可證資料；公開已知用途為 Factor VIII 替代療法） |
| 預測新適應症 | Primary release disorder of platelets |
| TxGNN 預測分數 | 99.99%（原始分數 0.9999269，排名第 141） |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 台灣市場狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前無詳細作用機轉（MOA）資料可用。根據既有公開資訊，Turoctocog alfa 屬於重組 Factor VIII 類別藥品，其在凝血因子 VIII 缺乏（如血友病 A）之替代治療效果已獲臨床證實，機轉為補充內生性凝血路徑中缺乏的 Factor VIII 蛋白，恢復 tenase 複合物功能以促進凝血。

然而，本 Evidence Pack 中模型自身對此排名第一預測的機轉論述已明確表示：Primary release disorder of platelets 的病理核心是血小板顆粒釋放缺陷，並非凝血因子路徑異常，FVIII 與血小板釋放機制之間**無直接生理連結**。換言之，此預測分數雖高，但屬於 TxGNN 圖神經網路的模式匹配結果，缺乏機轉合理性佐證，亦無任何臨床或文獻證據支持。

值得注意的是，本 Evidence Pack 同時列出的第 5 名候選「acquired coagulation factor deficiency（後天性凝血因子缺乏）」機轉關聯性明顯較強——若該疾病定義涵蓋後天性 Factor VIII 缺乏，則與 turoctocog alfa 的已知藥理作用直接對應。但此仍屬藥物類別層級的已知用途外推，並非針對本藥物之臨床證據，證據等級僅達 L4（Research Question 階段），尚不足以支持積極推進。

---

## 其他預測適應症（Rank 2–10）總覽

為完整呈現本次 TxGNN 預測全貌，以下彙整其餘 9 項候選適應症：

| 排名 | 疾病名稱 | 分數 | 證據等級 | 建議 | 備註 |
|------|---------|------|---------|------|------|
| 2 | Pseudo-von Willebrand disease | 99.99% | L5 | Hold | 血小板 GPIb 受體缺陷，機轉間接推測，無臨床證據 |
| 3 | Glanzmann thrombasthenia | 99.99% | L5 | Hold | GPIIb/IIIa 缺陷，FVIII 不影響血小板膜醣蛋白功能 |
| 4 | Scott syndrome | 99.95% | L5 | Hold | 磷脂外翻缺陷，FVIII 無法修復缺陷本身 |
| 5 | Acquired coagulation factor deficiency | 99.95% | L4 | Research Question | 唯一機轉直接對應之候選，但無藥物特定證據 |
| 6 | Bleeding diathesis due to collagen receptor defect | 99.91% | L5 | Hold | GPVI 缺陷與凝血因子路徑無關 |
| 7 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.91% | L5 | Hold | 血小板數量不足，FVIII 無法提升血小板數 |
| 8 | Flood factor deficiency | 99.61% | L5 | Hold | 病名非標準醫學術語，疑資料轉譯誤差 |
| 9 | Thrombotic thrombocytopenic purpura | 99.54% | L5 | **Hold（安全性排除）** | ⚠️ TTP 屬血栓性疾病，給予促凝血 FVIII 可能加劇微血栓形成，機轉方向與疾病病理**相反**，應優先排除，不建議任何後續評估 |
| 10 | Hereditary thrombocytosis with transverse limb defect | 99.52% | L5 | Hold | 罕見發育性症候群，與 FVIII 無合理生理連結 |

**安全性標記**：第 9 名 Thrombotic Thrombocytopenic Purpura（TTP）為方向性禁忌候選，補充凝血因子可能惡化微血管血栓病理，應列入不可推進清單，避免任何後續研究誤用此預測方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## 台灣市場資訊

Turoctocog alfa 目前**未於台灣上市**，無許可證資料。

---

## 安全性考量

請參閱仿單警語與注意事項。

補充說明：本 Evidence Pack 標記 TFDA 仿單警語/禁忌為 **Blocking 等級資料缺口（DG001）**，於此缺口補齊前，本藥物無法進入 S1 安全性初評階段；作用機轉資料（DG002）亦屬 High 等級缺口，影響機轉關聯性分析之可靠度。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
- 排名第一預測（Primary release disorder of platelets）證據等級為 L5，無任何臨床試驗或文獻支持，且模型自身機轉論述已明確指出生物學合理性薄弱。
- 台灣未上市、無許可證資料，且 TFDA 安全性資料為 Blocking 等級缺口，尚無法完成 S1 安全性初評。

**若要推進，需補足：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking，需下載官方仿單 PDF 解析）
- DrugBank 作用機轉（MOA）詳細資料（DG002，High，需查詢 DrugBank API）
- 若考慮推進第 5 名候選（Acquired coagulation factor deficiency），需取得針對此藥物、此適應症之藥物特定臨床試驗或文獻證據，而非僅依賴藥物類別層級外推
- 明確排除第 9 名候選（TTP）進入任何後續開發流程，避免方向性禁忌風險
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

