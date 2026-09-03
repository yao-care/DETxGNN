---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

> Fulvestrant is an endocrine therapy that, based on the clinical trial evidence in this pack, is established for treating hormone receptor-positive (HR+), HER2-negative breast cancer.
> The TxGNN model's top-ranked prediction is **HIV infectious disease** (score **99.91%**),
> but this direction is currently supported by **0 clinical trials** and only **1 loosely related publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormone receptor-positive (HR+), HER2-negative advanced/metastatic breast cancer — inferred from the clinical trial context in this evidence pack (e.g., NCT01942135, NCT02107703, which describe fulvestrant/Faslodex as standard endocrine therapy for this cancer); no BfArM license text is available to confirm this directly |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for fulvestrant in this evidence pack. Based on public pharmacological knowledge, fulvestrant is a selective estrogen receptor degrader/antagonist (SERD), and it is established as endocrine therapy for hormone receptor-positive, HER2-negative breast cancer — a fact clearly reflected in the extensive breast-cancer clinical trial evidence retrieved elsewhere in this pack (see the rank-2 candidate, "multiple endocrine neoplasia," whose linked trials are overwhelmingly fulvestrant/breast-cancer studies rather than trials of endocrine neoplasia).

For the top-ranked prediction, **HIV infectious disease**, no mechanistic rationale is provided in the evidence pack, and there is no known biological pathway connecting estrogen receptor antagonism to HIV replication or immune control. The single retrieved publication (PMID 40343334) discusses HTLV-1-associated myelopathy — a different retrovirus causing a different disease — and mentions HIV-1 only in passing, as a reference point for borrowing treatment strategies, not as a study of fulvestrant itself.

This mismatch suggests the prediction likely reflects proximity in the model's embedding space (e.g., shared "retrovirus/immune" or "endocrine-immune" disease-node neighborhoods) rather than an established pharmacological rationale. Given the missing MOA data and the absence of any direct fulvestrant–HIV evidence, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Preprint | Research Square | Multi-omics analysis of HTLV-1-associated myelopathy (HAM), a distinct retroviral neuroinflammatory disease. HIV-1 is mentioned only as a source of borrowed therapeutic strategies, not as a subject of study; the article does not evaluate fulvestrant or its use in HIV infection. |

---

## Germany Market Information

No marketing authorization records are available in this evidence pack — fulvestrant is currently **not marketed** in Germany (0 authorizations on file).

---

## Cytotoxicity

Fulvestrant is an antineoplastic hormonal agent (used in breast cancer per the trial evidence above), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted endocrine therapy (Selective Estrogen Receptor Degrader/Antagonist) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Low — fulvestrant is a hormonal, non-cytotoxic agent; no drug-specific toxicity data is provided in this evidence pack, please refer to the package insert |
| Emetogenicity Classification | Low — consistent with the general profile of hormonal/endocrine anticancer agents; not confirmed by evidence-pack data |
| Monitoring Items | Liver function, lipid profile, injection-site reactions (intramuscular administration); please refer to the package insert for complete monitoring requirements |
| Handling Protection | Standard hazardous-drug handling precautions are generally recommended for antineoplastic agents; a specific protocol is not provided in this evidence pack |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HIV infectious disease) has no supporting clinical trials and only one tangentially related, unclassified publication that does not directly study fulvestrant in HIV. Combined with missing mechanism-of-action data, no German marketing authorization, and no safety/warning data, there is currently insufficient basis to proceed.

**To proceed, the following is needed:**
- Fulvestrant mechanism of action data (query DrugBank — data gap DG002)
- TFDA/BfArM package insert warnings and contraindications (data gap DG001)
- Direct mechanistic or preclinical evidence linking fulvestrant to HIV infection outcomes
- Manual review of the rank-2 candidate ("multiple endocrine neoplasia"), whose linked trial evidence appears to be a disease-ontology mismatch with fulvestrant's actual breast cancer indication and may warrant separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

