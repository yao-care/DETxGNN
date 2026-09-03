---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Nevirapine (DB00238) is a non-nucleoside reverse transcriptase inhibitor (NNRTI) whose established clinical use is treatment of HIV-1 infection in humans.
> The TxGNN model's top-ranked prediction points to **Feline Acquired Immunodeficiency Syndrome** — a veterinary condition in cats caused by FIV, not a human disease —
> currently supported by **0 clinical trials** and only **1 preclinical/mechanistic publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (per literature evidence in this pack; not confirmed by Germany regulatory data — drug is not marketed) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection in cats) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (single preclinical/in vitro mechanistic study, no clinical trials) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nevirapine is not available in this evidence pack (flagged as a High-severity data gap). Based on known information referenced in the supporting literature, nevirapine is a first-generation NNRTI that binds directly to HIV-1 reverse transcriptase, and its efficacy in HIV-1 infection is well established in clinical practice.

The predicted indication, feline acquired immunodeficiency syndrome, is caused by Feline Immunodeficiency Virus (FIV) — a lentivirus structurally and functionally related to HIV. The rationale for TxGNN's prediction is mechanistic proximity: both viruses rely on a reverse transcriptase enzyme for replication, and researchers have directly tested whether HIV-1-specific NNRTIs (nevirapine, efavirenz, rilpivirine) could cross-inhibit FIV reverse transcriptase.

However, an important caveat: this is a **veterinary indication (cats), not a human disease**. NNRTIs are known to be highly virus-specific due to differences in the reverse transcriptase binding pocket across lentivirus species (a limitation also documented for nevirapine against SIV/HIV-2 in the rank-2 prediction of this pack). No data in this pack demonstrates that nevirapine effectively inhibits FIV RT in vitro or in vivo — the cited study only investigated the *potential* of NNRTIs for this purpose. This prediction should therefore be treated as a low-confidence, non-human signal rather than a human drug repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical / in vitro biochemical-structural study | Journal of Veterinary Science | Compared nevirapine, efavirenz, and rilpivirine (HIV NNRTIs) against feline and human immunodeficiency virus reverse transcriptase to assess potential utility of NNRTIs for treating FIV-infected cats; no effective FIV treatment currently exists. |

---

## Germany Market Information

Nevirapine is currently not marketed in Germany; no marketing authorization records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/BfArM label warnings and contraindications are recorded as a **Blocking** data gap (DG001) in this evidence pack, meaning this candidate cannot yet proceed to the S1 safety pre-assessment stage regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction targets a veterinary disease (feline AIDS) rather than a human indication, and is supported by only a single preclinical/mechanistic publication with no clinical trials. This is further compounded by a Blocking-severity gap in TFDA/BfArM safety labeling data, which prevents any safety pre-assessment. Nevirapine's other TxGNN predictions in this pack (simian immunodeficiency virus infection — an animal research model; and a rare neurodevelopmental disorder with no supporting evidence at all) are similarly non-actionable for human repurposing, reinforcing a Hold across the candidate set.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) to resolve the Blocking gap (DG001)
- Confirmed mechanism of action (MOA) and original approved human indication from DrugBank (DG002)
- Clarification of clinical relevance — the current top prediction is a non-human/veterinary condition and requires re-scoring against genuinely human disease targets
- If pursuing the FIV signal for translational/veterinary purposes only, in vitro efficacy data (IC50/binding affinity of nevirapine against FIV reverse transcriptase) beyond the single exploratory publication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

