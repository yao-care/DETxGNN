---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost：從隅角開放性青光眼到 Visceral Calciphylaxis（內臟鈣化防禦症）

## 一句話摘要

Travoprost 是一種前列腺素 F2α（PGF2α）類似物，臨床上用於降低隅角開放性青光眼／眼壓過高患者的眼壓。TxGNN 模型將其最高分預測適應症列為 **Visceral Calciphylaxis（內臟鈣化防禦症）**，但目前**沒有任何臨床試驗或文獻證據**支持此關聯，機轉上也找不到已知連結，屬於純模型推論。

---

## 總覽表

| 項目 | 內容 |
|------|------|
| 原始適應症 | 隅角開放性青光眼／眼壓過高（依證據包中臨床試驗資料推斷，藥品資料庫 `original_indications` 欄位目前為空） |
| 預測新適應症 | Visceral Calciphylaxis（內臟鈣化防禦症） |
| TxGNN 預測分數 | 99.9998% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 德國市場狀態 | 未上市 |
| 授權數量 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

藥品資料庫中的 `original_moa` 欄位目前無資料。根據本證據包內重複出現的機轉描述，可知 Travoprost 為前列腺素 F2α（PGF2α）類似物，作用於 FP 受體，臨床上用於增加葡萄膜鞏膜外流以降低眼壓；部分文獻也指出其可誘導血管平滑肌鬆弛及局部血管重塑（MMP 上調）。

但對於本次排名第一的預測適應症「Visceral Calciphylaxis」，證據包本身的機轉分析明確指出：**FP 受體促效作用與血管鈣化／鈣化防禦症的病理機轉（副甲狀腺—鈣磷代謝失衡、血管平滑肌鈣化）之間並無已知連結**。這代表此預測是 TxGNN 知識圖譜中的關聯推論，而非藥理學上有依據的假說。

值得補充的是，本次候選清單共列出 10 個 TxGNN 高分預測適應症，其中僅「vascular disease」（排名第5）附有臨床試驗與文獻證據，但這些試驗絕大多數是青光眼/眼壓相關研究、被評為 Grade C（低相關性，屬適應症誤標），並非真正支持血管疾病治療效益的證據。其餘 8 個候選（含胸廓出口症候群、血管發育不良、藍趾症候群、自發性冠狀動脈剝離、血管內皮瘤等）均無任何臨床試驗或文獻支持，甚至部分機轉分析指出理論上可能有害（如 MMP 誘導對已有血管壁結構異常疾病的潛在風險）。整體而言，本藥物目前尚未發現具藥理學基礎且有實證支持的老藥新用方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 德國市場資訊

Travoprost 目前於德國**未上市**，無查驗登記或授權紀錄可供列示。

---

## 安全性考量

請參閱藥品仿單以取得安全性資訊。

（補充：`data_gaps` 中列有一項 Blocking 等級缺口 DG001——TFDA 仿單警語／禁忌尚未取得，此為進入 S1 安全性初評的必要前提，須優先補齊。）

---

## 結論與下一步

**決策：Hold**

**理由：**
本預測（Visceral Calciphylaxis）評為 L5，僅有 TxGNN 模型分數，無任何臨床試驗或文獻證據，且證據包自身的機轉分析已明確排除藥理學關聯。同時該藥於目標市場（德國）未上市，安全性資料（警語、禁忌、DDI）全數缺失，不具備進入下一階段評估的基礎。

**若要推進，需要補齊：**
- TFDA／原廠仿單之警語與禁忌資料（DG001，Blocking）
- DrugBank 或原廠資料確認正式 MOA（DG002，High）
- 針對「FP 受體促效作用是否影響鈣磷代謝或血管鈣化」進行機轉層級的文獻／體外研究搜尋，以確認或排除此預測的生物學合理性
- 若未來欲評估「vascular disease」方向，需重新以正確關鍵字檢索並排除誤標的青光眼試驗，取得真正相關的血管疾病證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

