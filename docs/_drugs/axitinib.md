---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Metastatic Renal Cell Carcinoma to TFE3/Xp11.2 Translocation-Associated Renal Cell Carcinoma

## One-Sentence Summary

Axitinib is an oral, potent VEGFR-1/2/3 tyrosine kinase inhibitor already established as second-line therapy for advanced/metastatic renal cell carcinoma (RCC), based on the extensive literature evidence in this pack.
The TxGNN model predicts it may also be effective for **renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions**, a rare molecularly-defined RCC subtype,
with **1 ongoing clinical trial** currently supporting this specific direction (no dedicated literature yet).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic renal cell carcinoma (second-line TKI therapy) — derived from literature evidence in this pack (e.g., PMID 29033542, 20072829); no BfArM license data available to confirm the German label text |
| Predicted New Indication | Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (one ongoing, non-completed Phase 2 RCT; no completed trials or dedicated literature) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data (DrugBank MOA field) is currently a data gap for this candidate. However, the literature evidence contained in this pack consistently describes axitinib as a potent, selective small-molecule inhibitor of VEGF receptors 1, 2, and 3 (with roughly 10-fold lower IC50 against VEGFR family receptors than sunitinib or sorafenib), acting through anti-angiogenic blockade of tumor vasculature (PMID 29033542, 20072829).

Axitinib's approved use is in clear-cell-predominant advanced/metastatic RCC, most robustly established through the KEYNOTE-426, JAVELIN Renal 101, and AXIS trials captured in this pack's literature (PMIDs 30779529, 30779531, 37500340, 40750932, 33284113). TFE3/Xp11.2-translocation RCC is a rare, molecularly distinct RCC subtype that, like clear-cell RCC, exhibits VHL/HIF-pathway-related angiogenic dependence, providing mechanistic plausibility for VEGFR-TKI activity across this related tumor family. This is reinforced by the ongoing dedicated trial (NCT03595124) directly testing axitinib plus nivolumab in TFE3/translocation RCC across all age groups.

Notably, several other predicted indications in this evidence pack (unclassified RCC, pediatric/childhood RCC, collecting duct carcinoma, and even myxoid liposarcoma) follow the same angiogenesis-dependent rationale, with liposarcoma evidence supported by a dedicated preclinical study (PMID 27822137) showing axitinib has antiangiogenic and antitumorigenic activity in myxoid liposarcoma cell lines — suggesting the anti-VEGFR mechanism may extend beyond kidney cancer to other vascularized soft-tissue tumors.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, not recruiting | 15 | Randomized trial of axitinib + nivolumab vs. single-agent nivolumab specifically in TFE/translocation RCC across all age groups; tests whether axitinib's anti-angiogenic activity combined with checkpoint inhibition benefits this molecular subtype |

---

## Literature Evidence

Currently no related literature available specific to Xp11.2 translocation/TFE3 gene fusion-associated renal cell carcinoma. (Broader RCC and pediatric RCC literature exists under related predicted indications in this pack, e.g., PMID 31012542 on advanced pediatric RCC and PMID 39326645 on axitinib outcomes in children/young adults with RCC, but none map directly to this specific TFE3-defined subtype.)

---

## Germany Market Information

Axitinib currently has no BfArM authorization records in this pack (0 licenses; market status: Not Marketed). No dosage form or approved-indication text is available to summarize.

---

## Cytotoxicity

Axitinib is an antineoplastic agent (approved oncology indication: advanced/metastatic renal cell carcinoma; class: VEGFR tyrosine kinase inhibitor per literature evidence in this pack).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR-1/2/3 tyrosine kinase inhibitor / anti-angiogenic small molecule) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Axitinib is not currently marketed in Germany (0 authorizations), and TFDA/BfArM label warnings and contraindications are a **blocking** data gap (DG001) that prevents any S1 safety pre-assessment. Combined with an early-stage, non-completed single trial as the only direct evidence for this specific indication (Evidence Level L4), the candidate is not yet ready to advance.

**To proceed, the following is needed:**
- Retrieve TFDA/BfArM package insert warnings, contraindications, and DDI data (DG001, blocking)
- Obtain structured DrugBank MOA data to formalize the mechanistic rationale (DG002)
- Monitor completion of NCT03595124 for outcome data in TFE3/translocation RCC
- Confirm German/EU market and licensing status before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

