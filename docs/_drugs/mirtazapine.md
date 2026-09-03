---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 3
---

# Mirtazapine
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a NaSSA-class antidepressant (noradrenergic and specific serotonergic antidepressant), historically used to treat depression. The TxGNN model predicts a possible role in **Ohdo syndrome and variants**, a rare developmental chromatin-remodeling disorder — but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is model-inference only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the current evidence pack. Known clinical class: NaSSA antidepressant (depression) — MOA and indication data are a confirmed gap (DG002) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (no clinical trials or literature; model prediction only) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Mirtazapine is known to act as a NaSSA — antagonizing α2-adrenergic autoreceptors/heteroreceptors to increase norepinephrine and serotonin release, along with 5-HT2/5-HT3 antagonism (efficacy in depression) and H1 antagonism (sedation, appetite stimulation).

Ohdo syndrome and its variants (including blepharophimosis–intellectual disability syndrome, Ohdo type, ranked #2 in this pack) are rare congenital disorders caused by mutations in genes such as *KAT6B* and *MED12*, with core pathology in chromatin remodeling and transcriptional regulation. This is mechanistically distinct from mirtazapine's monoaminergic pharmacology — there is **no direct etiological link**. Any theoretical benefit would be limited to symptomatic management of sleep disturbance or behavioral issues that can accompany the syndrome, not disease modification.

The third-ranked prediction, benign paroxysmal torticollis of infancy, is thought to involve channelopathy-related mechanisms (e.g., *CACNA1A*) rather than monoamine dysregulation. While mirtazapine has occasional off-label use in migraine prevention via 5-HT2/3 and α2 pathways, this indication concerns an infant population with no pediatric safety data available here.

Overall, all three predictions in this pack appear to reflect **disease-ontology similarity within the TxGNN knowledge graph** (the top two are subtypes of the same syndrome) rather than a substantiated pharmacological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Mirtazapine is currently **not marketed** in Germany under this evidence pack (0 authorizations on file, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — see DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications carry L5 evidence (no clinical trials, no literature) with a weak or absent mechanistic link to mirtazapine's known pharmacology, and the top two predictions likely reflect disease-ontology proximity rather than true drug-disease relevance. A blocking safety data gap (TFDA label warnings/contraindications) also prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) to close DG001 (Blocking)
- Confirmed mechanism of action via DrugBank API to close DG002 (High)
- Original indication/regulatory history (currently absent from `taiwan_regulatory.licenses`)
- Any preclinical, case-report, or mechanistic literature specifically linking mirtazapine to chromatin-remodeling disorders or infant paroxysmal syndromes, given the current absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

