---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Eftrenonacog Alfa：從血友病 B 到 Pseudo-von Willebrand Disease

## 一句話總結

Eftrenonacog alfa（重組 Factor IX-Fc 融合蛋白）原用於血友病 B 患者的凝血因子替代治療。
TxGNN 模型預測其可能對 **Pseudo-von Willebrand Disease** 有效，
但目前**無任何臨床試驗與文獻**支持此方向，且機轉分析顯示兩者病理路徑並不重疊。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 血友病 B（Hemophilia B，凝血因子 IX 缺乏） |
| 預測新適應症 | Pseudo-von Willebrand Disease |
| TxGNN 預測分數 | 99.48%（排名第 6035） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 台灣上市狀態 | 未上市 |
| 藥證數量 | 0 |
| 建議決策 | Hold |

## 這個預測合理嗎？

Eftrenonacog alfa 是重組 Factor IX 與 Fc 片段的融合蛋白，作用機轉為補充內生性凝血因子 IX，
促成凝血瀑布下游 Factor X 的活化，用於血友病 B 患者的出血預防與治療。
由於是替代療法而非調節性藥物，其藥理作用高度侷限於凝血因子路徑本身。

Pseudo-von Willebrand disease 的病理機轉是血小板 **GPIb 受體**先天性突變，
導致對 von Willebrand factor（vWF）的親和力異常增高，屬於血小板功能異常疾病，
與凝血因子 IX 缺乏在病理生理上並無交集。TxGNN 給出的高分很可能反映知識圖譜中
「出血性疾病」的語意群聚效應，而非真正的機轉關聯。

本次 Evidence Pack 中另兩個候選適應症（primary release disorder of platelets、
Glanzmann thrombasthenia）同樣屬於血小板功能異常，而非凝血因子缺乏，
機轉論述皆指出 Factor IX 補充無法糾正血小板聚集或顆粒釋放缺陷。三者一致顯示，
此輪 TxGNN 預測在機轉層面的合理性偏低。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻資料

## 台灣市場資訊

Eftrenonacog alfa 尚未於台灣取得藥證，無授權資訊可供揭露。

## 安全性考量

請參考藥品仿單以取得完整安全性資訊。

> 註：TFDA 仿單警語/禁忌資料目前為關鍵缺口（Blocking），在補齊前無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
三個候選適應症證據等級皆為 L5（僅模型預測，無臨床試驗或文獻佐證），
且機轉分析顯示凝血因子 IX 替代療法與血小板功能異常疾病之病理路徑不重疊，
機轉合理性不足以支持進一步投入資源。

**若要推進，需要補齊：**
- TFDA 仿單警語與禁忌資料（Blocking，現階段無法進行安全性初評）
- DrugBank 完整作用機轉（MOA）資料，以確認是否存在未被目前分析捕捉的間接機轉路徑
- 至少一項體外或動物模型研究，驗證 Factor IX 補充是否對血小板-vWF 交互作用有任何影響
- 待上述缺口補齊後，重新評估是否晉升至更高決策階段（S1 以上）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

