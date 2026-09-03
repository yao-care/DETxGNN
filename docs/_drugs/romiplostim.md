---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Chronic Immune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

> Romiplostim is a thrombopoietin (TPO) receptor agonist whose established use is chronic immune thrombocytopenia (ITP). TxGNN's highest-scoring signal points to **Primary Release Disorder of Platelets** as a candidate new indication, but this rests on only **1 indirectly related clinical trial** and **2 mechanistic review articles** — the model itself flags the mechanistic link as weak and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Immune Thrombocytopenia (ITP) — noted in evidence rationale text; **not confirmed** via Taiwan regulatory filing (no license record exists) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% (score rank #3 among all TxGNN outputs) |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (evidence-pack label: "Research Question") |

---

## Why is This Prediction Reasonable?

Detailed MOA data for romiplostim is not yet available in DrugBank (flagged as data gap DG002). Based on information embedded in the evidence pack, romiplostim is a TPO receptor agonist that stimulates megakaryocyte proliferation and differentiation, thereby increasing platelet **production**. Its efficacy in chronic ITP — a disease of accelerated platelet destruction and impaired thrombopoiesis — is well established.

**Primary release disorder of platelets**, however, is a defect in platelet **release/degranulation function**, not in platelet count or production rate. The evidence pack's own mechanistic assessment states this directly: romiplostim's pathway can raise the *number* of platelets produced, but it cannot correct a release/degranulation defect. The link to ITP biology is therefore only partial — the two conditions share downstream platelet biology but not the specific dysfunction romiplostim's mechanism addresses. This is why the evidence level is capped at L4 (mechanism/observational only) despite the very high raw TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Large ITP registry study on thrombosis risk factors; does **not** test romiplostim as an intervention for this indication (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Overview of megakaryocytopoiesis/thrombopoiesis biology; TPO as primary growth factor for the megakaryocyte lineage |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Review/Mechanistic | Haematologica | Antiplatelet autoantibodies in ITP inhibit proplatelet formation and impair platelet production in vitro |

---

## Taiwan Market Information

Romiplostim currently holds **no marketing authorization in Taiwan** (0 licenses on file). No approved indication text, product name, or dosage form data is available from the regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

⚠️ **Data Gap Alert**: TFDA label warnings/contraindications have not yet been obtained (DG001, severity **Blocking**) — this must be resolved before any Stage 1 (S1) safety assessment can proceed. No drug-drug interaction records were found in the current query.

---

## Other Predicted Indications at a Glance

This evidence pack scored romiplostim against 10 candidate indications. For context, the full landscape:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Primary release disorder of platelets | 99.9998% | L4 | Research Question |
| 2 | Pseudo-von Willebrand disease | 99.9998% | L5 | Hold |
| 3 | Glanzmann thrombasthenia | 99.9995% | L5 | Hold |
| 4 | Fetal/neonatal alloimmune thrombocytopenia | 99.99% | L4 | Research Question |
| 5 | Scott syndrome | 99.97% | L5 | Hold |
| 6 | Hemorrhagic disorder (constitutional thrombocytopenia) | 99.95% | L5 | Hold |
| 7 | Bleeding diathesis (collagen receptor defect) | 99.95% | L4 | Hold |
| **8** | **Platelet-type bleeding disorder** | **99.93%** | **L1** | **Proceed with Guardrails** |
| 9 | Autosomal dominant macrothrombocytopenia | 99.88% | L3 | Research Question |
| 10 | Ehlers-Danlos syndrome, fibronectinemic type | 99.85% | L5 | Hold |

**Note:** Rank 8 ("platelet-type bleeding disorder") is backed by multiple completed Phase 3/4 trials (e.g. [NCT03362177](https://clinicaltrials.gov/study/NCT03362177) RECITE, [NCT05492409](https://clinicaltrials.gov/study/NCT05492409)) — but its own rationale states this cluster "essentially corresponds to romiplostim's core approved use (chronic ITP and related thrombocytopenia)." It is best read as a **validation signal confirming model accuracy**, not a novel repurposing opportunity. Ranks 2, 3, 5, 6, 10 have **zero** clinical trial or literature support and rest on TxGNN score alone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction (primary release disorder of platelets) has a self-identified weak, indirect mechanistic link, and its only clinical trial evidence does not test romiplostim as an intervention in this population. No genuinely novel candidate in this pack reaches L1/L2 evidence — the one indication with strong trial support (rank 8) largely overlaps with romiplostim's known indication rather than representing new territory.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently blocking any S1 safety evaluation
- Resolve DG002 (confirmed MOA from DrugBank API) to strengthen mechanistic-link analysis
- Confirm original approved indication via verified Taiwan regulatory filing (currently 0 licenses on record)
- If pursuing primary release disorder of platelets specifically: a dedicated interventional study in confirmed platelet-release-defect patients, since existing evidence is an unrelated ITP registry and general mechanism reviews
- Separately evaluate rank 8 (platelet-type bleeding disorder) as a line-extension/label-confirmation case rather than a new-indication repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

