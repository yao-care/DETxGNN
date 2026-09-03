---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 7
---

# Delamanid
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

# Delamanid: From Tuberculosis (MDR-TB) to Bovine Tuberculosis

## One-Sentence Summary

> Delamanid is a nitro-dihydro-imidazooxazole antimycobacterial, publicly known as a treatment for multidrug-resistant tuberculosis (MDR-TB), though no formal indication text is present in this evidence pack.
> The TxGNN model predicts it may also be effective for **Tuberculosis, Bovine (zoonotic *Mycobacterium bovis* infection)**,
> but currently **no clinical trials** and only **1 indirect publication** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally provided in this evidence pack. Delamanid is publicly known as an antimycobacterial approved for pulmonary MDR-TB; `original_indications` and `original_moa` fields are empty/Data Gap in the source data. |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only — no clinical trial, and the single available paper does not evaluate delamanid's efficacy) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa` = Data Gap). Based on generally known information, delamanid is a nitro-dihydro-imidazooxazole derivative developed as an antimycobacterial agent, used clinically for multidrug-resistant pulmonary tuberculosis caused by *Mycobacterium tuberculosis*.

The predicted new indication, "tuberculosis, bovine," is caused by *Mycobacterium bovis*, a member of the *Mycobacterium tuberculosis* complex that is closely related to *M. tuberculosis* and shares similar drug-target biology. This makes the TxGNN prediction biologically plausible on a mechanistic level. However, it is worth noting that this is not a novel disease *area* so much as a related pathogen/host variant of the drug's already-established anti-tuberculosis use — the prediction largely reflects known pharmacology rather than a genuinely new therapeutic direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Observational / Genomic (WGS) study | BMC Genomics | Whole-genome sequencing study characterizing genetic diversity and drug-resistance patterns of *M. bovis* isolates in zoonotic TB; does not directly evaluate delamanid efficacy, but provides pathogen background relevant to treatment target. |

---

## Germany Market Information

Delamanid currently holds **0 marketing authorizations** on record and has a market status of **Not Marketed** — no authorization table to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Formal safety data (warnings, contraindications, drug interactions) is not currently available in this dataset and is flagged as a **Blocking** data gap (DG001), preventing full S1 safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by the TxGNN score and one tangential publication that does not test delamanid's efficacy; no clinical trials directly address bovine/zoonotic TB with this drug. A **Blocking** safety data gap (missing label warnings/contraindications) also prevents a proper safety pre-assessment.

**To proceed, the following is needed:**
- Official label/package insert data (warnings, contraindications) — DG001
- Confirmed mechanism of action from DrugBank — DG002
- Direct evidence (in vitro/in vivo or clinical) evaluating delamanid specifically against *M. bovis*
- Clarification of true novelty: assess whether "bovine tuberculosis" represents a distinct regulatory indication or overlaps with delamanid's existing MDR-TB approval
- Confirmation of regulatory/market status before any repurposing pathway is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

