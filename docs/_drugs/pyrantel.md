---
layout: default
title: Pyrantel
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Pyrantel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Pyrantel: No TxGNN Predictions Available

## One-Sentence Summary

Pyrantel is an anthelmintic agent used to treat intestinal parasitic infections (roundworms, hookworms, and pinworms).
The TxGNN model did not generate any predicted new indications for this drug in the current pipeline run.
Meaningful drug repurposing evaluation cannot be completed until prediction data and key data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in dataset |
| Predicted New Indication | None (no TxGNN predictions generated) |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are available for Pyrantel at this time. Without a candidate indication, the mechanistic relevance analysis cannot be performed and the core repurposing evaluation framework does not apply.

Currently, detailed mechanism of action data is not available in this Evidence Pack. Pyrantel (DrugBank: DB11156) is a well-established anthelmintic of the tetrahydropyrimidine class, acting as a depolarising neuromuscular blocking agent that causes spastic paralysis in susceptible nematodes. This MOA is highly parasite-specific, which may explain why TxGNN — trained on a human disease knowledge graph — did not surface strong repurposing candidates. Retrieving the full DrugBank MOA record is required before drawing this conclusion definitively.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for a new repurposing indication.

---

## Literature Evidence

Currently no related literature available for a new repurposing indication.

---

## Taiwan Market Information

Pyrantel is currently **not marketed** in Taiwan. No TFDA product authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned zero predicted indications for Pyrantel, and two blocking data gaps (package insert safety data and MOA) remain unresolved, making a repurposing assessment premature at this stage.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** — confirm whether zero predictions reflect a true absence of signal or a pipeline/mapping issue (e.g., DrugBank ID not linked to KG node)
- **Retrieve MOA from DrugBank (DB11156)** — verify whether the parasite-specific mechanism genuinely limits human-disease repurposing candidates
- **Obtain TFDA package insert** — extract warnings, contraindications, and approved indications to complete the safety baseline (currently Blocking severity per DG001)
- **Assess Taiwan market viability** — Pyrantel is unregistered in Taiwan; a market-entry pathway analysis is needed before any repurposing programme is initiated
- **Verify KG coverage** — check whether Pyrantel appears in the TxGNN knowledge graph; if absent, the drug must be added before predictions can be generated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

