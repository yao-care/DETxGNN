---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamivudine：從抗反轉錄病毒治療（HIV／慢性B型肝炎）到貓科後天免疫缺乏症候群（人類適用性存疑）

## 一句話摘要

Lamivudine（3TC）為核苷類反轉錄酶抑制劑（NRTI），文獻與試驗證據顯示其國際上已用於 HIV-1 感染及慢性 B 型肝炎的抗病毒治療。TxGNN 模型排名第一的預測適應症為**貓科後天免疫缺乏症候群（feline AIDS，FIV 感染）**，但這是**貓科獸醫疾病、非人類適應症**，不適用於人類藥物再利用管線；本候選整體證據品質偏低，5 個預測適應症中有多筆出現物種錯配或疾病標籤錯誤，建議 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 本地無核准資料；國際間已知用於 HIV-1 感染與慢性 B 型肝炎（NRTI 背景治療，依證據內文推得） |
| 預測新適應症 | Feline acquired immunodeficiency syndrome（貓科後天免疫缺乏症候群，非人類疾病） |
| TxGNN 預測分數 | 99.93%（0.9992823） |
| 證據等級 | L4（臨床前／機轉層級研究，且高度存疑） |
| 台灣上市狀態 | 未上市 |
| 核准許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測有其合理性（與疑慮）？

目前缺乏 DrugBank 完整 MOA 資料（DG002，High severity）。根據證據包內文可知，Lamivudine 是 NRTI 類藥物，其人類適應症證據集中在 HIV-1 感染及慢性 B 型肝炎的聯合療法背景藥物，機轉為抑制病毒反轉錄酶。

然而，排名第一的預測適應症「feline acquired immunodeficiency syndrome」是**貓科動物的 FIV（feline immunodeficiency virus）感染**，屬獸醫適應症。雖然 FIV 與 HIV 同屬慢病毒（lentivirus），反轉錄酶機轉相似，使得 lamivudine 理論上對 FIV 有體外抑制作用，但這不是人類疾病，**不應納入人類藥物再利用決策管線**，此點也已在證據包的 `repurposing_rationale.mechanistic_link` 中明確標註。

更需留意的是，本候選其餘 4 個預測適應症同樣存在系統性問題：
- **Rank 2（SIV 感染）**：為靈長類動物模型病毒，無臨床試驗、僅動物研究，屬臨床前訊號（L5）。
- **Rank 3（神經發育疾病）**：無任何文獻或試驗支持，純模型假說（L5）。
- **Rank 4（家族性混合型高血脂症）**：機轉方向與已知藥理相反（NRTI 已知會誘發血脂異常，而非治療），疑似模型誤判。
- **Rank 5（慢性C型肝炎）**：所列試驗與文獻實際多為慢性B型肝炎（HBV，具反轉錄步驟）相關研究，與標籤疾病 HCV（無反轉錄酶）存在系統性錯配，屬資料標註錯誤。

整體而言，此候選的知識圖譜訊號品質偏低，建議在資料層修正後重新評估。

---

## 臨床試驗證據

以下試驗來自 rank 1（feline AIDS）之證據集，**但全數為人類 HIV-1 試驗，與貓科疾病無關**（relevance grade C），僅因 lamivudine 共同出現而被誤關聯：

| 試驗編號 | 期別 | 狀態 | 收案數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | DTG+abacavir/lamivudine vs Atripla，人類 HIV-1 初治病人研究，與 FIV 無關 |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | DTG+ABC/3TC 之 CNS／血漿 PK 研究，人類 HIV-1，非動物試驗 |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Darunavir+lamivudine 對比方案，人類 HIV-1 初治病人 |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | DTG vs raltegravir（+ABC/3TC 或 TDF/FTC），人類 HIV-1 初治病人 |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | DTG 劑量選擇研究（+ABC/3TC 或 TDF/FTC），人類 HIV-1 初治病人 |

> ⚠️ 上述試驗均與貓科 FIV 感染無直接相關性，不構成本預測適應症之支持證據。

---

## 文獻證據

以下文獻確實針對貓科 FIV 感染（獸醫領域），與 rank 1 適應症標籤一致，但屬**動物研究**，不適用於人類藥證評估：

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro（獸醫） | Am J Vet Res | FIV 分子株與 3TC 抗藥突變株之體外複製動力學比較 |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Review | Vet Immunol Immunopathol | AZT/3TC 併用對 FIV 感染／免疫病理之療效評估 |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | 世代研究（獸醫） | J Feline Med Surg | FIV 感染貓長期抗反轉錄病毒治療追蹤 |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | 世代研究（獸醫） | Viruses | 不同抗反轉錄病毒方案於 FIV 無症狀晚期貓之療效評估 |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | 病例系列（獸醫） | Antiviral Res | ZDV+3TC+ABC 併用對體外 FIV 複製之抑制效果 |

---

## 台灣上市資訊

本藥品於台灣（本地市場）**未上市，無核准許可證資料**（`total_licenses = 0`）。無法提供劑型、產品名稱或核准適應症文字，此為資料缺口（DG001，Blocking severity）需透過 TFDA 官網下載仿單解析補齊。

---

## 安全性考量

請參考藥品仿單／說明書以取得完整安全性資訊。

> 目前 `key_warnings`、`contraindications` 均標記為資料缺口，DDI 查詢結果為 `not_found`（DG001，Blocking severity），無法完成 S1 安全性初評。

---

## 結論與後續建議

**決策：Hold**

**理由：**
本候選前五名預測適應症皆存在證據品質問題——排名第一為非人類（貓科）疾病，不適用於人類藥物再利用管線；其餘四項分別為臨床前動物模型訊號、無證據支持之模型假說、機轉方向矛盾、及疾病標籤系統性錯配（HBV 試驗被誤標為 HCV）。同時本地欠缺 TFDA 安全性資料（Blocking severity），無法進入 S1 安全性初評。

**若要繼續推進，需要：**
- 補齊 TFDA 仿單警語／禁忌資料（DG001，透過 TFDA 官網 PDF 解析）
- 補齊 DrugBank 作用機轉（MOA）資料（DG002，透過 DrugBank API 查詢）
- 修正知識圖譜中的物種錯配問題（feline/simian 疾病不應與人類適應症候選並列）
- 修正 rank 5（慢性 C 型肝炎）之疾病標籤與證據錯配問題，重新以 HBV 相關試驗／文獻進行標註
- 若欲評估人類 HIV／HBV 以外之新適應症，建議要求 TxGNN 團隊排除非人類物種節點後重新產生候選清單
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

