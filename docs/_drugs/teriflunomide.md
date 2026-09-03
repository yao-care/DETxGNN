---
layout: default
title: Teriflunomide
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Teriflunomide: From No Recorded Original Indication to Relapsing-Remitting Multiple Sclerosis

## 一句話總結

> Teriflunomide（DB08880）目前在本轄區尚無上市紀錄，原始核准適應症資料亦缺失。
> TxGNN 模型預測其對 **Relapsing-Remitting Multiple Sclerosis（RRMS，復發緩解型多發性硬化症）** 具高度潛力，
> 目前已有 **33 筆臨床試驗**與 **20 篇文獻**支持此方向，其中包含多項完成的第三期隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無可用資料（本轄區未上市，無授權紀錄） |
| 預測新適應症 | Relapsing-Remitting Multiple Sclerosis |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L1（≥2 項已完成之第三期 RCT） |
| 市場狀態 | ✗ 未上市 |
| 授權件數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

結構化的 MOA 欄位目前為資料缺口，但文獻證據（NEJM, 2020, PMID 32757523）明確指出：teriflunomide 是一種口服的嘧啶合成抑制劑（pyrimidine synthesis inhibitor），透過抑制粒線體酵素 dihydroorotate dehydrogenase（DHODH），降低 T 細胞與 B 細胞的活化與增殖。這個機轉與多發性硬化症的自體免疫發炎、去髓鞘病理機制高度相關，具備明確的生物學合理性。

值得注意的是，RRMS 實際上已是 teriflunomide 在多數國際市場（如美國、歐盟，商品名 Aubagio）的**既有核准適應症**，而非全新的老藥新用推測。本轄區資料顯示該藥尚未上市、亦無授權紀錄，因此此預測更適合理解為「引進本地市場的候選適應症」，而非機轉層面的全新連結。大量已完成的頭對頭第三期試驗（如 TEMSO、TENERE、OPTIMUM、ASCLEPIOS、ULTIMATE 系列）進一步驗證了其在 RRMS 治療上的成熟地位。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1088 | TEMSO 試驗：安慰劑對照，評估 teriflunomide 降低復發頻率與延緩失能累積之效果 |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | TENERE 試驗：teriflunomide 與 interferon beta-1a 比較療效與安全性 |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | 長期延伸研究，記錄 7mg 與 14mg 兩劑量之長期安全性與失能進展 |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab 與第一線 DMT（含 teriflunomide）比較療效與耐受性 |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | HMR1726D/2001 延伸研究：長期安全性與療效評估 |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS：早期積極治療 vs 逐步升級治療策略比較 |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | 測定血清與腦脊髓液中 teriflunomide 14mg 每日劑量之濃度 |
| [NCT03768648](https://clinicaltrials.gov/study/NCT03768648) | N/A | Completed | 75 | 真實世界情境下，Aubagio 治療患者之日常認知功能與 MRI 標記評估 |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | 觀察性研究：常規臨床照護下 teriflunomide 之療效與有效性 |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | 機轉研究：調節性 B 淋巴球做為 teriflunomide 治療效果的中介機制 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab vs Teriflunomide（ASCLEPIOS I/II）：抗 CD20 單株抗體 vs 嘧啶合成抑制劑之比較 |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib vs Teriflunomide：BTK 抑制劑於復發型 MS 之療效安全性比較 |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab vs Teriflunomide：抗 CD20 單株抗體之 B 細胞清除療效比較 |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM 試驗：Ponesimod vs Teriflunomide 頭對頭第三期比較 |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | evolutionRMS1/2：Evobrutinib vs Teriflunomide 第三期試驗 |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | ASCLEPIOS I/II 次族群分析：新診斷未治療患者中 ofatumumab 優於 teriflunomide |
| [37691530](https://pubmed.ncbi.nlm.nih.gov/37691530/) | 2023 | RCT延伸 | Mult Scler | ALITHIOS 開放性延伸研究：Ofatumumab 四年治療之療效與安全性 |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Review | Cochrane Database Syst Rev | 網絡統合分析：RRMS 免疫調節與免疫抑制療法比較 |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | 多發性硬化症診斷與治療總覽 |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Teriflunomide 於 RRMS 治療之藥物評論 |

---

## 市場資訊

本藥物目前於本轄區**尚未取得任何上市授權**（授權件數：0），無法提供劑型與核准適應症明細。

---

## 安全性考量

請參考藥品仿單以獲取安全性資訊。

> ⚠ 注意：本轄區 TFDA 仿單警語與禁忌症資料目前為**阻斷性（Blocking）資料缺口**（DG001），
> 在取得官方仿單並完成解析前，無法進行 S1 安全性初評。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
雖然 teriflunomide 對 RRMS 之療效證據極為充分（L1 等級，多項已完成第三期 RCT，且為國際多國既有核准適應症），但本轄區缺乏 TFDA 仿單警語與禁忌症資料，此為阻斷性缺口，導致無法完成必要的 S1 安全性初評，故暫緩推進至下一階段。

**若要繼續推進，需要：**
- 取得 TFDA 官網仿單 PDF 並完成警語/禁忌症解析（DG001，阻斷性）
- 補齊 DrugBank 作用機轉（MOA）結構化資料（DG002）
- 確認是否有藥商規劃於本轄區申請上市授權
- 補充藥物交互作用（DDI）資料，目前查詢無結果（query_status: not_found）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

