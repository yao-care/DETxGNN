---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: Evaluation Report — Insufficient TxGNN Prediction Data

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor widely used as a pharmacokinetic booster in combination antiviral regimens (e.g., Paxlovid, lopinavir/ritonavir).
The current Evidence Pack contains **no TxGNN-predicted new indications**, and the drug is **not registered in Taiwan**.
Due to critical data gaps across prediction, regulatory, mechanism, and safety dimensions, a full repurposing evaluation **cannot be completed at this stage**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (general pharmaceutical knowledge; absent from regulatory data) |
| Predicted New Indication | Not available |
| TxGNN Prediction Score | Not available |
| Evidence Level | Undetermined — no prediction data present |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

No safety data is available for this Evidence Pack. All warning, contraindication, and drug interaction fields returned as empty or missing.

> Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Ritonavir is critically incomplete across all four evaluation dimensions — TxGNN prediction, regulatory status, mechanism of action, and safety profile. Without a predicted indication to evaluate, no repurposing case can be constructed or assessed.

**To proceed, the following is needed:**

- **TxGNN prediction results** — `predicted_indications` must be populated with at least one candidate indication and associated evidence (clinical trials, literature)
- **Mechanism of action (MOA)** — retrieve from DrugBank API (DG002: High severity gap)
- **Package insert safety data** — key warnings, contraindications, and drug interactions from TFDA or equivalent source (DG001: Blocking severity gap)
- **Original indication confirmation** — verify approved indications from Taiwan TFDA or international regulatory sources (EMA/FDA)
- **Drug interaction profile** — DDI query returned `not_found`; re-query with alternate sources (e.g., DrugBank DDI, clinical pharmacology databases)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

