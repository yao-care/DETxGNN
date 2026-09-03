---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase Alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

> Sebelipase alfa (Kanuma®) is a recombinant human lysosomal acid lipase (rhLAL) enzyme replacement therapy originally developed for **Lysosomal Acid Lipase (LAL) Deficiency**, including Wolman disease and cholesteryl ester storage disease (CESD).
> The TxGNN model's top-ranked new candidate is **Scheie syndrome** (a mild form of Mucopolysaccharidosis type I),
> but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no mechanistic corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication* | Lysosomal Acid Lipase (LAL) Deficiency (incl. Wolman disease, CESD) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

\* No BfArM license record exists for this product (drug is not marketed in Germany, `total_licenses = 0`). The original indication above is reconstructed from the literature evidence attached to this evidence pack (e.g., PMID 26452566 "Sebelipase alfa: first global approval"), not from a formal license text.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the structured drug database (`original_moa: [Data Gap]`). Based on literature evidence contained in this dossier, sebelipase alfa is a recombinant human lysosomal acid lipase (rhLAL) enzyme replacement therapy. Its efficacy in LAL deficiency — encompassing the infantile-onset Wolman disease phenotype and the later-onset CESD phenotype — is well documented through completed Phase 2/3 trials (e.g., the ARISE study, NCT01757184) and is globally approved in the EU, US, and Japan.

Scheie syndrome, however, is a distinct lysosomal storage disease caused by deficiency of **alpha-L-iduronidase**, an enzyme responsible for glycosaminoglycan (GAG) degradation — an entirely different lysosomal enzyme system from LAL, which hydrolyzes cholesteryl esters and triglycerides. The two conditions share only broad phenotypic features common to lysosomal storage disorders (organomegaly, multisystem accumulation), which is consistent with the pattern already flagged elsewhere in this same prediction set: other candidates such as Gaucher disease and Tay-Sachs disease received the same **Hold** verdict for the same reason — TxGNN appears to be clustering on lysosomal-storage-disease phenotype similarity rather than genuine enzyme-substrate overlap.

Mechanistically, enzyme replacement therapy is highly enzyme-specific: sebelipase alfa can only replace the missing LAL enzyme and cannot compensate for an alpha-L-iduronidase deficit. There is no biochemical rationale supporting efficacy in Scheie syndrome, and this is reflected in the complete absence of clinical or literature evidence for this specific pairing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Scheie syndrome) has zero supporting clinical trials or literature, and the underlying enzyme deficiency (alpha-L-iduronidase) is mechanistically unrelated to sebelipase alfa's LAL-replacement mechanism. This is a pure model-signal (L5) with no corroborating biological or clinical rationale.

**To proceed, the following is needed:**
- Preclinical or biochemical evidence that rhLAL has any cross-reactivity or GAG-pathway relevance in MPS I/Scheie syndrome (currently none identified)
- TFDA/BfArM label and safety data (currently `[Data Gap]` — blocking for any S1 safety pre-screen)
- Confirmed DrugBank MOA record to replace the current data gap

**Note for pipeline review:** Rank 4 in this same prediction set (cholesteryl ester storage disease) already carries a completed Phase 3 RCT (ARISE, NCT01757184) and 9 registered trials — this is not a novel repurposing candidate but the drug's known, already-approved indication. Recommend flagging this as a triage/data-quality item rather than presenting it as a new signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

