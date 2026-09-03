---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

> Nitisinone (NTBC) is the standard therapy for hereditary tyrosinemia type 1 (HT-1), where it blocks a toxic tyrosine-metabolism intermediate.
> The TxGNN model predicts it may also address **Renal Tubular Acidosis**, a known renal complication of HT-1,
> with **2 supporting publications** and a mechanistically direct rationale, though no dedicated clinical trials exist yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (inferred from repurposing rationale; official label text not available — see Data Gaps) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack (original_moa: Data Gap). However, the repurposing rationale supplied for the top-ranked prediction describes the mechanism in enough detail to assess plausibility: Nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), an enzyme in the tyrosine degradation pathway. By blocking this step, it prevents the accumulation of succinylacetone and other toxic intermediates that are the root cause of HT-1 pathology.

Renal tubular acidosis (RTA), specifically a Fanconi-syndrome-like proximal tubulopathy, is itself a well-recognized clinical manifestation of untreated or under-treated HT-1 — it is caused by succinylacetone toxicity to proximal tubular epithelial cells. This means the "new indication" is not an unrelated disease but rather a **downstream complication of the drug's already-approved indication**. Since Nitisinone directly reduces the toxic metabolite responsible for this tubulopathy, its potential benefit in RTA follows logically from its established mechanism, and this is supported by early clinical observations (below) rather than by network-topology inference alone.

By contrast, the other nine predicted indications in this evidence pack (galactosemia, serpinopathy, C1 inhibitor deficiency, glycogen storage diseases, etc.) lack this direct mechanistic overlap with HPPD/tyrosine metabolism — their high TxGNN scores likely reflect broader disease-similarity clustering (e.g., "rare inherited metabolic/hepatic disease") rather than a specific pharmacological link, and all carry an L4–L5 evidence level with a "Hold" recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort/Case Series | Molecular Genetics and Metabolism | Describes early improvement in renal tubular dysfunction after starting NTBC therapy in patients with HT-1 |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Cohort/Case Series | Indian Journal of Gastroenterology | Case series of children with tyrosinemia showing clinical response to NTBC, including resolution of renal tubular abnormalities |

---

## Germany Market Information

Nitisinone is currently **not marketed** in Germany under this regulatory dataset (0 authorizations on record). No marketing authorization details are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Nitisinone's known action (HPPD inhibition, reduction of succinylacetone) and renal tubular acidosis is direct and biologically coherent, and is supported by two case-series publications showing clinical improvement — but no controlled clinical trials exist, and the drug is not currently marketed in the target jurisdiction.

**To proceed, the following is needed:**
- Official label/warnings and contraindications data (currently a Blocking data gap — required before any S1 safety assessment)
- Formal mechanism-of-action documentation from DrugBank or equivalent source
- Confirmation of whether "renal tubular acidosis" here should be scoped strictly as an HT-1-associated complication (label extension) rather than a standalone indication
- Drug-drug interaction data (currently not found)
- Assessment of feasibility/need for Germany market authorization given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

