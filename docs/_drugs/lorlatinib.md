---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor clinically established for ALK-positive metastatic non-small cell lung cancer (this evidence pack itself does not document the original indication or MOA — see note below). The TxGNN model's top-ranked prediction for this candidate is **Gingival Fibromatosis**, but this prediction is supported by **zero clinical trials** and **zero publications** — it is a pure computational signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (0 licenses on file; `original_moa` and `original_indications` are both data gaps). Clinically, lorlatinib is known to be an ALK/ROS1 TKI approved for ALK-positive NSCLC, but this is external knowledge, not sourced from this pack. |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% (rank 2729 among all predictions) |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, lorlatinib is an ALK/ROS1 tyrosine kinase inhibitor whose efficacy in ALK-rearranged NSCLC is well established (e.g., the Phase 3 CROWN trial), but this pack contains no data linking that mechanism to gingival tissue biology.

Gingival fibromatosis is typically an autosomal-dominant hereditary condition or a drug-induced gingival overgrowth (classically associated with calcineurin inhibitors like cyclosporine, or agents like phenytoin) — it is not known to involve ALK or ROS1 signaling. The evidence pack's own rationale for this prediction explicitly states there is **no known mechanistic link** and characterizes it as likely **TxGNN prediction noise**, i.e., an artifact of the embedding/similarity model rather than a genuine biological signal.

**Broader data-quality caveat:** Reviewing all 10 TxGNN-ranked predictions in this pack, none constitute a credible repurposing signal. Six of ten (ranks 1, 2, 3, 7, 8, 9) have zero supporting evidence. The remaining four (ranks 4, 5, 6, 10) do carry substantial literature — but on inspection, that literature is almost entirely about lorlatinib's **already-approved malignant NSCLC indication** (e.g., CROWN Phase 3 RCT data attached to "lung benign neoplasm"), **ALK-driven neuroblastoma** (attached to "lung germ cell tumor"), or **lorlatinib's known adverse-effect profile** (hyperlipidemia, ARDS, metabolic syndrome — attached to an unrelated rare genetic syndrome). These appear to be disease-ontology mapping errors in the underlying database, not real repurposing signals. This should be corrected before the dataset is used for further scoring or reporting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Lorlatinib currently has no marketing authorization on file in Germany (0 licenses; market status: not marketed). No product/dosage-form data is available in this evidence pack.

---

## Cytotoxicity

Lorlatinib is an antineoplastic agent (third-generation ALK/ROS1 tyrosine kinase inhibitor), based on the drug class described in the literature evidence attached elsewhere in this pack (e.g., CROWN trial references). It is not a conventional cytotoxic chemotherapeutic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 TKI) |
| Myelosuppression Risk | Low — TKIs of this class are not typically associated with significant myelosuppression; no specific hematologic toxicity data present in this pack |
| Emetogenicity Classification | Low (typical for oral small-molecule TKIs) |
| Monitoring Items | Lipid panel (hypercholesterolemia/hypertriglyceridemia reported in literature associated with this drug), liver function, weight/metabolic parameters, mood/CNS effects |
| Handling Protection | Standard oral oncolytic handling precautions; please refer to institutional policy and the official package insert for specific requirements |

---

## Safety Considerations

Formal safety fields (`key_warnings`, `contraindications`, `ddi`) are data gaps in this evidence pack. However, literature attached elsewhere to other (mismatched) predicted indications in this pack does contain genuine lorlatinib safety signals worth noting for awareness, pending confirmation against the official label:

- Reports of lorlatinib-associated hyperlipidemia/dyslipidemia and metabolic syndrome (PMIDs [40287137](https://pubmed.ncbi.nlm.nih.gov/40287137/), [40157899](https://pubmed.ncbi.nlm.nih.gov/40157899/), [39537504](https://pubmed.ncbi.nlm.nih.gov/39537504/), [33789526](https://pubmed.ncbi.nlm.nih.gov/33789526/))
- A case report of lorlatinib-associated ARDS (PMID [31985497](https://pubmed.ncbi.nlm.nih.gov/31985497/))
- A pragmatic adverse-event management guide for lorlatinib (PMID [38554546](https://pubmed.ncbi.nlm.nih.gov/38554546/))

These findings relate to lorlatinib's known safety profile in its approved oncology use, not to gingival fibromatosis specifically, and are not sufficient to support the predicted indication in this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has no clinical trial or literature support and no plausible mechanistic rationale — the pack itself flags it as likely model noise. No other prediction in this pack constitutes a genuine, evidence-backed repurposing signal once the ontology-mismatched entries are excluded.

**To proceed, the following is needed:**
- Resolve the two Blocking/High data gaps (TFDA/BfArM label warnings & contraindications; confirmed original MOA/indication)
- Correct disease-ontology mapping for ranks 4, 5, 6, and 10, which currently misattribute existing ALK+ NSCLC, neuroblastoma, and drug-safety literature to unrelated candidate diseases
- Re-run TxGNN scoring/evidence retrieval after ontology correction before considering this candidate for further staging
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

