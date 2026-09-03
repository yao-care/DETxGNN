---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog originally used for selective cytotoxic treatment of lymphoid hematologic malignancies such as hairy cell leukemia. TxGNN predicts potential activity against **Parameningeal Embryonal Rhabdomyosarcoma**, one of six closely related pediatric rhabdomyosarcoma subtypes ranked highly by the model. However, this prediction is currently supported by **no clinical trials and no directly relevant literature** — it is a model-only prediction (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy Cell Leukemia (mentioned in mechanistic narrative only; structured indication data unavailable) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on the mechanistic narrative accompanying this prediction, cladribine is a deoxyadenosine analog that inhibits ribonucleotide reductase and induces DNA strand breaks, producing high selective cytotoxicity against rapidly dividing lymphoid-lineage hematologic malignancies such as hairy cell leukemia.

Rhabdomyosarcoma, by contrast, is a solid tumor of muscle-cell origin, driven by distinct molecular pathways (e.g., PAX3/FOXO1 fusion in alveolar subtypes) that are mechanistically unrelated to lymphoid differentiation. The available rationale for this prediction explicitly notes that it can only be inferred from cladribine's "broad antiproliferative effect" rather than any pathway specific to rhabdomyoblasts. TxGNN's high score likely reflects a general "cytotoxic chemotherapy ↔ pediatric malignancy" association pattern in the knowledge graph, rather than a validated, disease-specific mechanistic link.

This same weak-mechanism caveat applies across all six ranked rhabdomyosarcoma subtypes (parameningeal, vaginal botryoid-type, extrahepatic bile duct, prostate, and the general rhabdomyosarcoma category), none of which have any supporting clinical or preclinical evidence. A seventh, lower-ranked prediction (liver sarcoma) does have one associated case report, but it describes cladribine treatment of systemic mastocytosis — a clonal mast-cell disorder unrelated to hepatic sarcoma pathology — and should be treated as tangential, low-relevance evidence rather than direct support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: Across all seven ranked predictions in this evidence pack, only one literature reference was identified — [PMID 15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) (2004, case report, *Der Hautarzt*) — describing cladribine treatment of systemic mastocytosis, associated with the lower-ranked "liver sarcoma" prediction, not with the top-ranked rhabdomyosarcoma indication. This reference is not directly relevant to the predicted indication above.*

---

## Germany Market Information

Cladribine currently holds **no marketing authorization in Germany** (0 authorizations, market status: Not Marketed).

---

## Cytotoxicity

Cladribine's mechanistic profile (selective lymphocyte cytotoxicity via DNA strand-break induction) is consistent with a conventional cytotoxic antineoplastic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard cytotoxic drug handling precautions apply, per antineoplastic classification |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications in this evidence pack — including the top-ranked parameningeal embryonal rhabdomyosarcoma — remain at evidence level L5 (model prediction only), with zero supporting clinical trials and no directly relevant literature. Cladribine also holds no marketing authorization in Germany, and the mechanistic link to rhabdomyosarcoma biology is explicitly characterized as weak/non-specific rather than pathway-validated.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (currently blocking — DG001)
- Structured mechanism of action and original indication data from DrugBank (currently high-severity gap — DG002)
- Preclinical or mechanistic studies linking cladribine activity to rhabdomyosarcoma-specific pathways (e.g., PAX3/FOXO1)
- Any case reports, compassionate-use data, or early-phase trials in pediatric sarcoma populations
- Pediatric-specific safety and dosing data, given the target population is predominantly children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

