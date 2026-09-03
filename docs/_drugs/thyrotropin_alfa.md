---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: From Thyroid Cancer (Diagnostic/Adjunct) to Migraine Disorder

## One-Sentence Summary

> Thyrotropin alfa (recombinant human TSH) is used clinically as a diagnostic and adjunctive agent in differentiated thyroid cancer — supporting radioiodine uptake scanning and ablation after thyroidectomy.
> The TxGNN model's top prediction suggests possible relevance to **Migraine Disorder**,
> but this is currently a **pure algorithmic prediction** — no clinical trials and no literature support this direction, and the evidence pack itself notes no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid cancer — diagnostic radioiodine scanning / ablation preparation (based on drug-class knowledge cited in the evidence pack; not confirmed via German market licenses, which are currently empty) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for thyrotropin alfa is not available in DrugBank. Based on general pharmacological knowledge referenced elsewhere in the evidence pack, thyrotropin alfa is a recombinant form of human thyroid-stimulating hormone (TSH) that acts as a **TSH-receptor agonist**, stimulating thyroid follicular cells to take up iodine and secrete thyroid hormones. Its established clinical role is diagnostic/adjunctive — supporting radioiodine uptake scanning and ablation therapy following thyroidectomy for differentiated thyroid cancer.

There is no known pathophysiological connection between TSH-receptor signalling in thyroid follicular cells and the trigeminovascular / CGRP pathways implicated in migraine. TxGNN assigned migraine disorder its highest prediction score (99.98%), but this reflects network-level pattern inference rather than a validated biological hypothesis — the evidence pack explicitly states that no mechanistic hypothesis, clinical trial, or literature currently supports this drug-disease pairing.

Given the absence of any mechanistic rationale, this prediction should be treated as a hypothesis-generation signal only, not as grounds for clinical consideration at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Thyrotropin alfa is currently **not marketed** in Germany, and no authorization records are available in this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (migraine disorder) is supported only by an L5 algorithmic score, with no clinical trials, no literature, and no plausible mechanistic link — the drug's known TSH-receptor agonism has no established connection to migraine pathophysiology. In addition, a blocking data gap (missing TFDA/label warnings and contraindications) prevents even an initial safety screen (S1), and the drug is not currently marketed in Germany.

**To proceed, the following is needed:**
- Package insert / regulatory label parsing for warnings and contraindications (currently blocking S1 safety evaluation)
- Confirmed mechanism of action data from DrugBank (currently unavailable)
- A validated mechanistic hypothesis linking TSH-receptor signalling to migraine pathophysiology, ideally supported by preclinical data
- Any prospective clinical or case-level evidence directly evaluating thyrotropin alfa in migraine patients
- Clarification of the regulatory pathway, given the drug is not currently marketed in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

