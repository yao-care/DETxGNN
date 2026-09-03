---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 5
---

# Imiglucerase
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

> Imiglucerase is a recombinant human glucocerebrosidase used as enzyme replacement therapy for Gaucher disease.
> TxGNN predicts a possible new indication for **Hurler syndrome** (MPS I) with a score of **99.52%**,
> but this is currently supported only by **0 clinical trials** and **2 general (non-drug-specific) review articles** — the model's own rationale flags this as a likely false-positive driven by semantic clustering of "lysosomal storage disease," not true mechanistic overlap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (identified from literature evidence; no structured Taiwan/Germany regulatory record exists) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (flagged as a High-severity data gap). Based on known pharmacology, imiglucerase is a recombinant analogue of human **glucocerebrosidase**, and its established role is substrate-specific enzyme replacement for Gaucher disease, which is caused by glucocerebrosidase deficiency.

Hurler syndrome (Mucopolysaccharidosis type I) is caused by deficiency of a **different enzyme, alpha-L-iduronidase**, acting on a different substrate (glycosaminoglycans, not glucocerebroside). Both conditions belong to the broader "lysosomal storage disease" category, which is almost certainly why TxGNN scored them highly together — but this is a category-level (semantic) similarity, not an enzyme/substrate-level mechanistic link. The two supporting literature items are general reviews of enzyme replacement therapy across multiple lysosomal storage diseases; neither reports imiglucerase being tested or effective specifically in Hurler syndrome.

**Overall assessment: the mechanistic basis for this prediction is weak.** Unlike genuine repurposing candidates where a shared pathway plausibly explains cross-indication efficacy, here the target enzymes and substrates differ entirely, and imiglucerase would not be expected to have catalytic activity relevant to MPS I.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review (imaging methodology) | PNAS | General review of PET imaging for enzyme replacement therapy across lysosomal storage diseases (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); not specific to imiglucerase efficacy in Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of ERT history (alglucerase → imiglucerase for Gaucher disease) and its extension to other LSDs; does not report imiglucerase use in Hurler syndrome |

---

## Germany Market Information

Imiglucerase currently holds no marketing authorization in Germany (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (Hurler syndrome) and the other four candidates in this evidence pack (Scheie syndrome, adrenal gland benign neoplasm, autosomal ichthyosis syndrome, cholesteryl ester storage disease) are all scored L5 with a "Hold" recommendation. The drug-specific mechanistic rationale for each explicitly identifies enzyme/substrate mismatches with imiglucerase's known glucocerebrosidase activity, suggesting these high TxGNN scores reflect disease-category clustering ("lysosomal storage disease") rather than genuine target overlap.
- Foundational drug-level data (MOA, TFDA/German label warnings and contraindications) is missing and blocking (DG001, DG002), so this candidate cannot proceed even to a basic safety screen (S1) regardless of the repurposing hypothesis.

**To proceed, the following is needed:**
- Confirm full mechanism of action via DrugBank (resolve DG002)
- Obtain official label warnings/contraindications, e.g., from an EU/FDA-approved product (resolve DG001, blocking)
- Seek preclinical or biochemical evidence that imiglucerase has any catalytic or off-target activity relevant to alpha-L-iduronidase-deficient conditions (currently no such evidence exists)
- If no drug-specific mechanistic or preclinical support emerges, this candidate should be deprioritized as a likely model false-positive rather than advanced further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

