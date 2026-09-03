---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI), a class developed to treat HIV-1 infection in humans. TxGNN's top-ranked prediction is **feline acquired immunodeficiency syndrome (FIV)** — a veterinary disease of cats — with **0 clinical trials** and **0 publications** currently supporting this direction. This prediction should be treated as a low-confidence computational signal rather than an actionable repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (based on known drug classification; not present in evidence pack) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (FIV) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, doravirine is an NNRTI approved for human HIV-1 infection (marketed as Pifeltro, and combined with lamivudine/tenofovir disoproxil fumarate as Delstrigo). It works by binding non-competitively to HIV-1 reverse transcriptase, blocking conversion of viral RNA to DNA.

Feline immunodeficiency virus (FIV) is a lentivirus related to but structurally distinct from HIV-1; it causes an AIDS-like syndrome in cats. While both viruses share the lentivirus family and rely on reverse transcriptase, NNRTIs such as doravirine are generally not cross-reactive against FIV reverse transcriptase due to sequence and binding-pocket differences. The TxGNN score likely reflects a broad "immunodeficiency virus / RT inhibitor" association embedded in the knowledge graph rather than a validated pharmacological mechanism. Critically, FIV is a veterinary indication in cats, not a human clinical indication — making this prediction non-actionable for human drug repurposing regardless of mechanistic plausibility.

The two other candidates in this evidence pack were already flagged as low value: simian immunodeficiency virus infection (rank 2) is supported only by a review article about *islatravir* — a different drug with a different mechanism (NRTTI, not NNRTI) — so it does not constitute evidence for doravirine; and the rare neurodevelopmental disorder (rank 3) has no plausible mechanistic link to reverse transcriptase inhibition and is most likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

Doravirine is not currently marketed in Germany (0 authorizations on record); no BfArM license data is available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature support any of the three TxGNN-predicted indications. The top-ranked prediction (FIV) is a veterinary disease with no established mechanistic cross-reactivity to doravirine's NNRTI activity, and the drug is not currently marketed in Germany.

**To proceed, the following is needed:**
- TFDA/BfArM 官方仿單警語與禁忌資料（DG001，Blocking，目前無法進入安全性初評）
- Doravirine 完整作用機轉 (MOA) 官方資料來源（DG002）
- 若欲評估人類可行之老藥新用方向，需針對人類相關疾病重新查詢 TxGNN 預測結果——目前三項候選皆非可行之人類臨床標的
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

