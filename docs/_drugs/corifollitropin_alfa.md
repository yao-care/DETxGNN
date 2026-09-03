---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 8
---

# Corifollitropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Corifollitropin Alfa: From Controlled Ovarian Stimulation to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa is a long-acting FSH receptor agonist used clinically for controlled ovarian stimulation (COS) during IVF cycles. The TxGNN model's top prediction suggests possible efficacy for **Gastroduodenitis**, but this signal is supported by **0 clinical trials** and **0 publications**, and the drug is not currently marketed in Taiwan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Controlled Ovarian Stimulation (COS) in IVF *(inferred from rationale; not present in formal Taiwan license data — none exist)* |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap, DG002). Based on the repurposing rationale provided, corifollitropin alfa is a long-acting FSH receptor agonist acting on ovarian granulosa cells to promote follicular development, used for controlled ovarian stimulation in IVF.

There is **no known biological pathway connecting FSH receptor signaling to gastroduodenitis** (mucosal inflammation/injury). The model's own rationale explicitly states that the high TxGNN score likely reflects an indirect knowledge-graph path (e.g., shared comorbidity or protein nodes) rather than direct mechanistic evidence, and that no clinical trials or literature support this pairing. This prediction should therefore be treated as a hypothesis-generation signal only, not as mechanistically validated repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Corifollitropin alfa currently holds **0 licenses** in Taiwan and is **not marketed**. No product, dosage form, or approved indication text is available for reference.

---

## Safety Considerations

- **Data Gap (Blocking):** TFDA package insert warnings/contraindications are not currently available. This is flagged as a **Blocking** severity gap (DG001) — it prevents this candidate from entering the S1 safety pre-assessment stage.
- **Drug Interactions:** Query returned no results (not found in current DDI database).

Please refer to the official package insert for safety information once available; no substantive safety data currently exists in this evidence pack.

---

## Other Predicted Indications (Same Drug)

This evidence pack included 7 additional TxGNN predictions for corifollitropin alfa, all similarly unsupported:

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|----------------|------|
| 2 | Migraine disorder | 99.63% | L5 | Only theoretical hormonal-withdrawal link; no direct study |
| 3 | Peptic ulcer disease | 99.61% | L5 | No known FSH-related mechanism |
| 4 | Migraine with brainstem aura | 99.59% | L5 | Mechanism mismatch (ion channel/brainstem pathology) |
| 5 | Raynaud disease | 99.59% | L5 | No vascular/FSH mechanistic overlap |
| 6 | Pulmonary hypertension | 99.44% | L5 | OHSS is an adverse effect, not therapeutic rationale |
| 7 | Kyphoscoliotic heart disease | 99.36% | L5 | Structural cardiopulmonary disorder, unrelated mechanism |
| 8 | Migraine susceptibility | 99.11% | L4 | 20 literature hits, all on epilepsy genetics/neuroinflammation — none about FSH or corifollitropin alfa |

All 8 predictions carry a **Hold** recommendation at decision stage S0.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications for corifollitropin alfa are supported only by TxGNN model scores (L5, or L4 with irrelevant literature) with zero clinical trials and no drug-specific publications. The drug is not marketed in Taiwan, and critical safety data (TFDA warnings/contraindications) is a Blocking data gap that prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/FDA/EMA package insert data for warnings and contraindications
- Resolve DG002 (High): obtain confirmed mechanism of action from DrugBank or primary literature
- Conduct a targeted literature search specifically linking FSH receptor signaling to gastroduodenitis (or any top-ranked candidate) before advancing beyond S0
- If no mechanistic or empirical support emerges, close out this candidate as knowledge-graph noise rather than a genuine repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

