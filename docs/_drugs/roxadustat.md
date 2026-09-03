---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Roxadustat: From Renal Anemia to Dry Eye Syndrome

## One-Sentence Summary

> Roxadustat is a HIF prolyl-hydroxylase inhibitor (HIF-PHI) used to treat renal anemia in chronic kidney disease patients.
> The TxGNN model predicts it may be effective for **Dry Eye Syndrome**,
> but this is currently supported by only **1 observational clinical trial** and **no publications**, none of which directly test roxadustat's therapeutic effect on dry eye.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal anemia (anemia associated with chronic kidney disease) — inferred from clinical trial context; not present as a structured field in this evidence pack |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available for this drug (`original_moa` is flagged as a data gap, DG002). However, the evidence pack's own repurposing rationale identifies roxadustat as a **HIF prolyl-hydroxylase inhibitor (HIF-PHI)**, which stabilizes HIF-1α/2α to upregulate endogenous erythropoietin (EPO) production — the mechanism underlying its use in renal anemia.

The link to dry eye syndrome is weak and indirect. The only supporting clinical trial (NCT06287879) does not test roxadustat as a treatment for dry eye at all — it is an **observational study** examining meibomian gland function and morphology in renal anemia patients who happen to present with dry eye symptoms, with roxadustat mentioned only as one of the background anemia treatments these patients receive. There is no mechanistic or empirical evidence that HIF stabilization improves meibomian gland function or tear film stability; the co-occurrence is more plausibly explained by shared comorbidity (chronic kidney disease/uremia) rather than a drug effect.

Given the absence of an interventional trial or literature directly testing roxadustat for dry eye, this prediction should be treated as a hypothesis-generating signal from the knowledge graph rather than an evidence-backed repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | NA | Unknown | 50 | Observational study characterizing meibomian gland function and morphology in renal anemia patients with dry eye symptoms; roxadustat/EPO listed as background anemia treatments, not evaluated as a dry eye intervention (relevance grade: C) |

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Roxadustat is currently **not marketed** in this jurisdiction — 0 authorizations on record, and no license entries are available in the evidence pack.

---

## Safety Considerations

- **Key Warnings**: No formal package insert warning/contraindication data is currently available for this drug (blocking data gap; TFDA label has not yet been retrieved and parsed).
- **Important mechanistic safety signal (from evidence pack)**: A lower-ranked TxGNN prediction (squamous cell carcinoma, rank 4) surfaces a directionally opposite concern — HIF-1α/2α stabilization is a well-established driver of tumor growth, angiogenesis, and metastasis in many solid tumors, including squamous cell carcinoma. This is flagged in the evidence pack as a **known safety consideration for roxadustat use in patients with active or prior malignancy**, not as a therapeutic opportunity, and should be factored into any risk assessment for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence (one non-interventional, unknown-status trial rated relevance grade C) does not test roxadustat's effect on dry eye syndrome, and no literature supports this indication. Combined with a blocking data gap on TFDA safety labeling and the drug's non-marketed status, there is insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications (DG001, blocking)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- An interventional trial or preclinical study directly testing roxadustat's effect on dry eye/tear film outcomes
- Literature search specifically addressing HIF-PHI effects on ocular surface disease
- A formal safety review of the malignancy-related mechanistic signal (HIF stabilization and tumor promotion) before any further indication expansion is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

