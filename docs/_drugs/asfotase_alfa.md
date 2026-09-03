---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# ASFOTASE ALFA：從低磷酸酶症（HPP）到粒線體氧化磷酸化障礙（核 DNA 異常型）

## One-Sentence Summary

> Asfotase alfa 為重組人類組織非特異性鹼性磷酸酶（TNSALP）酵素替代療法，原用於治療低磷酸酶症（Hypophosphatasia, HPP）。
> TxGNN 模型預測其可能對 **粒線體氧化磷酸化障礙（核 DNA 異常所致）** 有效，
> 但目前**無任何臨床試驗與文獻**支持此方向，且證據包中的機轉分析本身已指出兩者病理生理無已知關聯。

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 低磷酸酶症（Hypophosphatasia, HPP）※依證據包中機轉敘述整理，非正式適應症清單（`original_indications` 欄位為空） |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5（僅模型預測，無實際研究） |
| Germany Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

`drug.original_moa` 欄位標記為資料缺口，但證據包中第一名預測項的 `repurposing_rationale` 已提供機轉描述可供引用：Asfotase alfa 為重組人類組織非特異性鹼性磷酸酶（TNSALP），作用機轉為水解焦磷酸鹽（PPi）以促進骨骼礦化，主要用於低磷酸酶症（HPP）——一種細胞外基質礦化障礙。

粒線體氧化磷酸化障礙（核 DNA 異常型）屬於粒線體呼吸鏈缺陷，病理軸線與骨骼礦化／磷酸鹽代謝完全不同。證據包本身即明確指出：「與粒線體氧化磷酸化路徑（核DNA突變導致的呼吸鏈缺陷）無已知機轉關聯，兩者病理生理完全不同軸線，此為知識圖譜統計關聯，缺乏生物學合理性支持。」

換言之，此預測是 TxGNN 知識圖譜上的統計關聯，而非機轉驅動的假說。第 2–10 名候選（Steel syndrome、外分泌胰腺功能不全、MPS I 系列、Hurler/Scheie syndrome、家族性 ApoC-II 缺乏症、食道靜脈曲張、胱胺酸儲積症等）也均被證據包自陳為「表型層次關聯」或「無生物學合理性」，僅少數（如胱胺酸儲積症、Hurler/Scheie syndrome、溶酶體儲積病合併骨骼病變）在骨骼表型上有間接相似性，但分子機轉不重疊。

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

目前無查獲之藥證授權紀錄（`total_licenses = 0`，市場狀態為「未上市」）。

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
排名前 10 名之預測適應症皆為 L5 等級（僅有 TxGNN 模型分數，無臨床試驗、無文獻支持），且第一名候選的機轉分析已由證據包本身指出缺乏生物學合理性，屬於知識圖譜統計關聯而非機轉驅動假說，目前不具備進入下一階段評估的證據基礎。

**To proceed, the following is needed:**
- 補齊 TFDA 仿單警語／禁忌資料（DG001，Blocking，目前無法進行 S1 安全性初評）
- 查證 DrugBank 之 asfotase alfa 完整作用機轉（MOA）（DG002，High）
- 針對排名較合理之候選（如胱胺酸儲積症、MPS I 系列等骨骼表型相關疾病）進行文獻／試驗檢索，確認是否有超出知識圖譜關聯的實際證據
- 若無法補齊機轉合理性或實證支持，建議維持 Hold，不進入 S1 以後階段
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

