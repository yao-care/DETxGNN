---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

> Vortioxetine is a multimodal serotonergic antidepressant reported in the literature as approved for Major Depressive Disorder (MDD); no local regulatory indication text is available since the product is not currently marketed.
> The TxGNN model's top-ranked prediction is **Neurotic Disorder**,
> but this specific label is currently supported by only **1 clinical trial** and **1 publication**, both of low direct relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the regulatory dossier (no licenses on file); per supporting literature (PMID 29189941), Vortioxetine is approved for **Major Depressive Disorder** |
| Predicted New Indication | Neurotic Disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this candidate is not available in the evidence pack (`original_moa: [Data Gap]`). Based on the supporting literature retrieved for this candidate (PMID 25016186, PMID 29189941), Vortioxetine is a multimodal antidepressant acting as a serotonin transporter (SERT) inhibitor combined with 5-HT3, 5-HT7, and 5-HT1D receptor antagonism, 5-HT1B partial agonism, and 5-HT1A agonism — increasing serotonergic, noradrenergic, dopaminergic, cholinergic, histaminergic, and glutamatergic neurotransmission in brain regions implicated in mood regulation. Its efficacy in Major Depressive Disorder has been demonstrated across multiple Phase 3 registration trials cited elsewhere in this evidence pack.

"Neurotic disorder" is a broad, largely obsolete diagnostic category historically encompassing anxiety, depressive, and somatoform symptom clusters. There is conceptual overlap between this category and MDD, which provides a plausible — but non-specific — mechanistic rationale for TxGNN's prediction. However, the evidence pack itself flags this: the only linked trial (NCT04446039) is a large real-world retrospective cohort comparing antidepressants generally, not a study designed around "neurotic disorder" as an inclusion criterion, and the only linked publication is a single case-based review of "neurotic depression" (a related but distinct label). The model's own rationale field explicitly notes the evidence is "insufficient to support a specific clinical decision" for this label.

**Note:** Within this same evidence pack, the rank-3 candidate — **Melancholia** — is substantially better supported (6 completed Phase 3 RCTs directly testing Vortioxetine in MDD, evidence level L1, recommendation "Proceed with Guardrails"). Melancholia is a recognized severe/biological MDD subtype and may represent a more actionable repurposing signal than the top-ranked "Neurotic Disorder" label; this should be considered when prioritizing next steps.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completed | 370,212 | Real-world retrospective cohort study using nationwide claims data comparing medication utilization patterns and adverse-outcome risk across commonly used antidepressants; not designed around "neurotic disorder" specifically (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review (case report) | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case report on neurotic depression, discussing personal predisposition and clinical features; advocates a combined antidepressant + CBT approach. Does not directly evaluate Vortioxetine. |

---

## Germany Market Information

Not currently marketed in Germany — no product authorizations are on file for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the TFDA label/warnings data required for a full S1 safety review is currently a blocking data gap in this evidence pack — see next steps below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction ("Neurotic Disorder") is supported only by a non-specific real-world cohort study and a single case-report-level review, corresponding to evidence level L4. This is insufficient to justify progression beyond initial screening for this specific indication label.

**To proceed, the following is needed:**
- Retrieve TFDA/BfArM label warnings and contraindications (currently a Blocking data gap; required before any S1 safety assessment)
- Obtain confirmed mechanism-of-action documentation from DrugBank (currently a High-severity data gap)
- Clarify whether "Neurotic Disorder" maps to a modern, actionable diagnostic entity, or whether effort should instead be redirected to the better-evidenced **Melancholia** candidate (L1, 6 Phase 3 RCTs) identified in the same prediction batch
- If pursuing Neurotic Disorder specifically, seek trials or studies with inclusion criteria matching this diagnostic label rather than general antidepressant-comparison cohorts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

