---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab is an IGF-1R-blocking monoclonal antibody approved for **thyroid eye disease (TED)**. TxGNN assigns its top new-indication candidate, **Monosomy X**, a high raw score (99.79%), but this pack contains **zero supporting clinical trials or literature**, and the drug's own mechanistic rationale explicitly flags the link as likely graph noise rather than a genuine pharmacological hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid Eye Disease (TED) — derived from mechanistic rationale text; no formal indication record in this pack |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa`: [Data Gap]). However, the repurposing rationale confirms teprotumumab is an **IGF-1R antagonist monoclonal antibody**, approved for thyroid eye disease via blockade of the IGF-1R/TSHR signaling complex on orbital fibroblasts.

Monosomy X (the cytogenetic basis of Turner syndrome) is a **structural chromosomal abnormality**, not a signaling-pathway disease — there is no established causal link between IGF-1R blockade and chromosomal loss or its downstream phenotypes. The most plausible explanation for the high TxGNN score is that Turner syndrome carries an elevated prevalence of autoimmune thyroid disease (including Graves'/TED), and the knowledge graph likely clusters Monosomy X near TED through this comorbidity association — **not** through a genuine "teprotumumab treats Monosomy X" mechanism. Notably, IGF-1R blockade could theoretically be counterproductive for growth-related goals relevant to Turner syndrome management, further weakening the case.

In short: this is a **statistical/graph-topology artifact**, not a pharmacologically grounded hypothesis. The same pattern applies to the other 9 ranked candidates in this pack (esophageal varices, mixed gonadal dysgenesis, mitochondrial disease, varicose disease, etc.) — none have an identified mechanistic connection to IGF-1R antagonism, and all are scored L5/Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorizations are currently registered for teprotumumab in Germany (market status: 未上市, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable in this evidence pack — flagged as **Blocking** data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting this indication, and the drug's own mechanistic rationale identifies the association as a likely knowledge-graph artifact rather than a plausible pharmacological hypothesis. Combined with a Blocking data gap on TFDA/regulatory safety labeling, this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label / warnings & contraindications) before any safety pre-screen (S1) can occur
- Confirm formal MOA record from DrugBank (DG002) to replace the current rationale-derived summary
- Independently verify whether the TxGNN association reflects a real biological signal (e.g., check embedding neighbors/explainability) versus comorbidity-driven graph clustering
- If pursuing this candidate class at all, prioritize re-scoring/re-ranking against diseases with plausible IGF-1R-pathway involvement rather than the current chromosomal/vascular candidate set, none of which show mechanistic fit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

