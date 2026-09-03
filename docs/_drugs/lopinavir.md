---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir：從 HIV-1 感染 到 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)

## 一句話總結

> Lopinavir 是一款 HIV-1 蛋白酶抑制劑，通常與 Ritonavir 併用於 HIV-1 感染的抗反轉錄病毒治療。
> TxGNN 模型預測其可能對**猿猴免疫缺陷病毒感染 (SIV Infection)** 有效，
> 目前僅有 **3 篇動物臨床前文獻**支持此方向，**無任何臨床試驗**佐證，且該「適應症」本質上為猴類感染而非人類疾病。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | HIV-1 感染（依證據包機轉推論文字得知；正式 MOA 資料缺失） |
| 預測新適應症 | Simian Immunodeficiency Virus Infection（猿猴免疫缺陷病毒感染） |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L4（動物臨床前研究） |
| 台灣上市狀態 | 未上市 |
| 許可證數量 | 0 |
| 建議決策 | Hold |

---

## 為何此預測具合理性？

目前正式的作用機轉（MOA）資料尚未補齊（Data Gap）。根據證據包中之機轉推論文字，Lopinavir 為 **HIV-1 蛋白酶抑制劑**，其原始用途是抑制 HIV-1 protease 以阻斷病毒成熟複製，通常與 Ritonavir 併用（Lopinavir/Ritonavir 複方）治療人類 HIV-1 感染。

SIV（猿猴免疫缺陷病毒）與 HIV 同屬靈長類慢病毒屬（Lentivirus），兩者蛋白酶結構與功能具高度同源性，因此理論上 Lopinavir 可能對 SIV 蛋白酶也具有抑制活性，這是此預測的機轉合理性基礎。

然而需特別指出：現有 3 篇文獻的研究設計，多數是將 SIV/SHIV 感染獼猴**作為測試 HIV 蛋白酶抑制劑藥效的臨床前動物模型**，而非把「治療猴類 SIV 感染」本身當作獨立的藥物開發適應症。換言之，TxGNN 抓到的關聯很可能反映的是「這隻藥常被用在這種動物模型中測試」，而非真正意義上的人類新適應症。這點在後續決策評估時應特別留意。

---

## 臨床試驗證據

目前無相關已註冊之臨床試驗。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | 動物臨床前研究 | Journal of Virology | 4 隻感染 SIVmac251 之食蟹猴接受四合一抗病毒療法後，觀察到快速病毒量下降，用於建立 HIV-1 病毒動力學數學模型的比較基礎 |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | 動物臨床前研究 | Microbes and Infection | 建構帶有 HIV-1 蛋白酶基因之新型 SHIV-pr 病毒株，作為體內測試蛋白酶抑制劑藥效的工具 |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | 動物臨床前研究 | Journal of Virological Methods | 慢性感染 SHIV(89.6P) 之獼猴，經口服 AZT+3TC+Lopinavir/Ritonavir 治療 28 天後對 CD8 亞群之影響評估 |

---

## 台灣藥證資訊

Lopinavir 目前在台灣**未取得任何藥品許可證**（許可證數量：0），無法提供產品名稱、劑型與核准適應症資訊。

---

## 安全性考量

請參考仿單安全性資訊。

> 補充說明：本次評估發現 **Blocking 等級資料缺口**——TFDA 仿單警語/禁忌資料尚未取得，導致本案**無法進入 S1 安全性初評階段**。在此缺口解除前，不建議進行任何臨床或法規層面的後續動作。

---

## 其他次要預測（信心度較低，供參考）

同一批預測中另有兩項排名相近但證據強度極低的候選，均建議 Hold：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|------|-----------|-----------|---------|------|
| 2 | Feline acquired immunodeficiency syndrome（貓科後天免疫缺乏症） | 99.90% | L5 | FIV 蛋白酶與 HIV-1 同源性有限，無任何文獻或試驗佐證，缺乏機轉實證支持 |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter（罕見遺傳性神經發育疾患） | 99.90% | L5 | 與 HIV 蛋白酶抑制機轉無已知生物學關聯，判斷極可能為模型雜訊 (false positive) |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據僅止於動物臨床前模型，且多數研究目的是測試藥效而非開發 SIV 感染之獨立適應症；SIV/FIV 感染本質上為動物疾病，人類臨床應用價值有限。
- 安全性資料存在 **Blocking 等級缺口**（TFDA 仿單警語/禁忌未取得），依規定無法進入 S1 安全性初評，程序上不可推進。

**若要繼續推進，需要補齊：**
- TFDA 仿單完整警語與禁忌資料，以解除 S1 安全性初評之 Blocking 缺口（DG001）
- Lopinavir 正式作用機轉（MOA）資料，以強化機轉關聯性分析（DG002）
- 釐清 SIV/FIV 感染是否具備對應之人類臨床意義，或應將此預測方向重新定位為動物用藥/臨床前研究工具，而非人用老藥新用候選
- 若仍欲推進人用適應症方向，需取得實際人體臨床試驗證據，而非僅依賴動物模型文獻
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

