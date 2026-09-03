---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

# Gimeracil：從 S-1 複方組成成分到大腸腫瘤（Colonic Neoplasm）

## 一句話摘要

Gimeracil 本身並非獨立的抗腫瘤藥物，而是 S-1 複方（tegafur + gimeracil + oteracil）中的 DPD（dihydropyrimidine dehydrogenase）抑制劑組成成分，透過阻斷 5-FU 代謝分解來提升療效。TxGNN 模型預測其（作為 S-1 複方一員）可能對**大腸腫瘤（Colonic Neoplasm）**有效，目前有 **8 項臨床試驗**與 **16 篇文獻**支持此方向，其中包含 2 項已完成的第三期隨機對照試驗。需特別注意：此證據體實為「S-1 複方」於大腸直腸癌之證據，並非 gimeracil 單一成分的獨立藥效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 無獨立核准適應症（Gimeracil 為 S-1 複方之藥理組成成分，非直接抗腫瘤藥物） |
| 預測新適應症 | 大腸腫瘤 Colonic Neoplasm |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1（≥2 項已完成第三期 RCT） |
| 德國/台灣市場狀態 | 未上市 |
| 核准許可證數量 | 0 |
| 建議決策 | Proceed with Guardrails（附條件推進） |

---

## 為什麼這個預測合理？

目前 DrugBank 尚未提供 gimeracil 正式的作用機轉（MOA）欄位資料。根據現有文獻與試驗證據推論，gimeracil 本身**無直接抗腫瘤活性**，其藥理角色是抑制 DPD 酵素，阻斷 tegafur 轉化而成之 5-FU 被分解代謝，藉此提升 5-FU 的血中濃度與腫瘤內暴露量，達到增效目的。因此 gimeracil 的藥效必須放在 S-1 複方（tegafur + gimeracil + oteracil）的脈絡下理解，而非單一藥物。

大腸腫瘤與 S-1 目前主要核准的適應症（如胃癌）同屬消化道腺癌，兩者對 5-FU 類藥物的敏感性機轉相似。事實上，S-1 複方已在日本與歐洲部分國家（含德國，於 capecitabine/5-FU 因手足症候群或心血管毒性而須停藥時）獲准使用於大腸直腸癌治療，這也是本次 TxGNN 預測獲得大量臨床試驗與文獻支持的主因。

需強調的限制是：本報告所引用的證據幾乎全部針對「S-1 複方整體」的療效與安全性，而非 gimeracil 單一成分的獨立藥理數據。在做出最終決策前，仍須釐清 gimeracil 是否有獨立於 S-1 複方之外的臨床定位。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+Leucovorin vs S-1 用於 Stage III 大腸癌輔助治療，並探討基因表現預測因子；直接支持 S-1（含 gimeracil）於此適應症之療效與安全性 |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO 研究：S-1 vs Capecitabine 一線治療轉移性大腸直腸癌，可併用 Bevacizumab |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX vs XELOX 用於 Stage III 大腸癌輔助治療的大型隨機對照試驗，惟狀態未知，需查證是否已發表結果 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 用於標準化療失敗之轉移性大腸直腸癌，主要終點為無疾病進展存活期 |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + 口服 Leucovorin + Oxaliplatin（SOL）用於未經治療之轉移性大腸直腸癌 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + Bevacizumab 用於經 Irinotecan、Oxaliplatin 治療失敗後之無法切除或復發大腸直腸癌 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | 評估 S-1 與 Capecitabine 併用 Oxaliplatin 對冠狀動脈血流的影響（安全性導向，非療效試驗，已終止） |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib 併用 S-1（含 gimeracil）用於第三線轉移性大腸直腸癌治療，尚未招募，僅為未來計畫 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Cohort/Review | 中華腫瘤雜誌 | Oxaliplatin + S-1 用於術後大腸直腸癌之療效與副作用觀察 |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohort | Gan to Kagaku Ryoho | S-1 + Irinotecan 治療 87 例晚期/復發大腸癌，第 3-4 級血液毒性發生率 16.1%，並建立風險分級模型 |
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Real-world population study | Eur J Cancer | 大腸癌輔助治療中，因手足症候群或心血管毒性而由 capecitabine 換用 S-1 之安全性與可行性評估 |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | PK study | Gan to Kagaku Ryoho | 以小鼠腹膜轉移模型探討 S-1 於大腸癌腹膜轉移之藥物動力學 |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical | Oncology Reports | Irinotecan 併用口服 S-1（含 gimeracil）於人類大腸癌異種移植模型中克服 5-FU 抗藥性 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | S-1 + CPT-11 治療大腸癌肝轉移達完全緩解並維持之個案報告 |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case report | Gan to Kagaku Ryoho | 大腸癌腹膜復發經腹腔鏡手術反覆切除，術後併用含 tegafur 類藥物輔助化療之個案 |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case report | Gan to Kagaku Ryoho | 橫結腸癌合併肝轉移與門脈腫瘤栓塞，經化療（含 S-1 類方案轉換）有效控制之個案 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan to Kagaku Ryoho | 升結腸癌多發雙葉肝轉移，經 SOX（tegafur-gimeracil-oteracil + Oxaliplatin）+ Panitumumab 降期化療後行分階段肝切除 |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | Case report | Gan to Kagaku Ryoho | 大腸癌術後復發疼痛，經 CT 導引腹腔神經叢阻斷術完全緩解之個案（術後輔助化療含 UFT 類藥物） |

---

## 細胞毒性資訊

Gimeracil 作為 S-1 複方（傳統細胞毒性化療、fluoropyrimidine 類藥物組合）的組成成分，本身雖非直接細胞毒性藥物，但其藥理功能是強化 5-FU 之細胞毒殺作用，故仍需依細胞毒性藥物規範處理與監測。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | S-1 複方（Fluoropyrimidine 類）組成成分；gimeracil 本身為 DPD 抑制劑，非直接細胞毒性藥物，作用為增強 5-FU 細胞毒殺效果 |
| 骨髓抑制風險 | 中度（S-1 + Irinotecan 併用之第 3-4 級血液毒性發生率約 16.1%，見 PMID 21084813） |
| 致吐性分類 | 低至中度（與其他口服 fluoropyrimidine 類藥物相近） |
| 監測項目 | 全血球計數（含分類）、腎功能（gimeracil/S-1 依腎功能調整劑量）、肝功能、電解質 |
| 處理防護 | 屬於細胞毒性化療複方之一部分，須依細胞毒性藥物操作規範處理 |

---

## 安全性考量

請參考藥品仿單以獲取安全性資訊。

（目前 TFDA/BfArM 仿單警語、禁忌症與藥物交互作用資料均為缺口，列為 Blocking 等級資料缺口 DG001，需優先補齊後方可進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails（附條件推進）**

**理由：**
- 已有 2 項已完成的第三期隨機對照試驗（NCT00660894, n=1535；NCT01918852, n=161）支持 S-1（含 gimeracil）於大腸直腸癌之療效，證據等級達 L1。
- 但此證據體係針對「S-1 複方整體」而非 gimeracil 單一成分，且 gimeracil 本身的正式 MOA 與台灣/德國仿單安全性資料（警語、禁忌症、DDI）目前皆為資料缺口，其中仿單警語/禁忌屬 Blocking 等級，尚無法進入 S1 安全性初評，因此不建議直接列為 Go。

**若要繼續推進，需要補充：**
- TFDA/BfArM 官方仿單 PDF，解析警語與禁忌症資訊（DG001，Blocking）
- DrugBank API 查詢 gimeracil 正式作用機轉資料（DG002，High）
- 釐清 gimeracil 是否具有獨立於 S-1 複方之外的臨床定位與藥效證據
- 藥物交互作用（DDI）資料庫查詢結果補充

*備註：TxGNN 對此藥物另預測 9 項候選適應症（如 cecum villous adenoma、malignant gastric granular cell tumor 等），但均無臨床試驗或文獻支持（證據等級 L5，僅為模型分數），建議標記為 Hold，暫不進一步推進。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

