---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 5
---

# Carfilzomib
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

# Carfilzomib: From [Original Indication Not Confirmed] to CMM7

## One-Sentence Summary

> Carfilzomib's original indication is not documented in this evidence pack (a blocking-severity data gap — TFDA labeling has not yet been retrieved); literature evidence in this pack incidentally identifies it as a "frontline anti-myeloma drug."
> The TxGNN model's top-ranked prediction is **CMM7** (a rare cutaneous malignant melanoma susceptibility subtype), with a prediction score of **99.37%**, but **zero clinical trials and zero literature** currently support this specific prediction — evidence level is L5 (model prediction only).
> Notably, a lower-ranked prediction in this same set — general **melanoma** — is backed by 5 mechanistic/preclinical publications, making it a stronger candidate than the top-ranked CMM7 for any further evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` empty; DG002 flags missing MOA data) |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma, susceptibility locus 7) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for carfilzomib is not available at the drug level (DG002, High severity). Based on information present elsewhere in this evidence pack (mechanistic notes attached to the rank-5 "melanoma" prediction), carfilzomib is understood to be a second-generation, irreversible epoxyketone-class proteasome inhibitor that selectively blocks the chymotrypsin-like activity of the 20S proteasome, inducing ER stress and apoptosis. One literature entry (PMID 27016342) additionally refers to carfilzomib as a "frontline anti-myeloma drug," consistent with its known clinical use, though this was not formally captured in the `original_indications` field.

For the **top-ranked prediction, CMM7**, there is no independent literature or trial evidence in this pack. The stated rationale is that TxGNN scored it highly among melanoma-spectrum diseases, and the mechanistic argument is borrowed by analogy from general melanoma (proteasome inhibition → apoptosis induction), not from any CMM7-specific data. This is a materially weaker basis than a directly-evidenced prediction.

By contrast, rank 5 in this same evidence pack — **general melanoma** — is supported by in vitro evidence that carfilzomib combined with bortezomib enhances apoptosis in B16-F1 melanoma cells, plus computational docking studies and mechanistic papers on proteasome-pathway regulation in melanoma survival. This suggests that if a melanoma-spectrum indication is to be pursued, the evidence currently favors the general "melanoma" entity over the unevidenced CMM7 subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(This applies to the top-ranked prediction, CMM7. No clinical trial or ICTRP evidence was found for any of the 5 predicted indications in this pack, including melanoma.)*

---

## Literature Evidence

Currently no related literature available for CMM7 (rank 1).

**Note — related but lower-ranked prediction:** the general "melanoma" prediction (rank 5, score 99.03%) in this same pack does have literature support:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro (preclinical) | Biology | Carfilzomib + bortezomib enhances apoptotic cell death in B16-F1 melanoma cells via caspase 3/8/9/12 activation |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational (docking/MD) | J Biomol Struct Dyn | Molecular docking/dynamics support carfilzomib binding across multiple cancer kinase targets, including melanoma |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Mechanistic/in vitro | Matrix Biology | Carfilzomib (with bortezomib) activates NF-κB pathway, triggering heparanase expression linked to aggressive tumor phenotype |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Mechanistic | Mol Cancer Res | ZFAND2A/cIAP2 regulation of melanoma cell survival, relevant to proteasome-pathway drugs |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Mechanistic (PROTAC design) | Leukemia | Proteasomal-degradation-targeting chimeric molecules active in preclinical myeloma models |

None of these are RCTs or clinical trials; all are preclinical/mechanistic/computational (Tier 3), which caps the evidence level at L4 even for the best-supported prediction in this set.

---

## Taiwan Market Information

Carfilzomib is **not marketed in Taiwan**. No drug licenses are currently registered (`total_licenses: 0`).

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor class, established anti-myeloma use per literature context in this pack).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard hazardous/antineoplastic drug handling precautions are expected to apply; official confirmation pending resolution of DG001 |

---

## Safety Considerations

Please refer to the package insert for safety information.

TFDA labeling data (warnings, contraindications, and drug interactions) is currently unavailable and flagged as a **Blocking**-severity data gap (DG001), which prevents this candidate from entering the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (CMM7) has no clinical trial or literature support (L5, model prediction only), and its mechanistic rationale is indirect, borrowed from a different, lower-ranked prediction (general melanoma).
- Safety pre-assessment (S1) cannot proceed because TFDA labeling data is missing (DG001, Blocking severity).
- The drug is not currently marketed in Taiwan (0 authorizations).

**To proceed, the following is needed:**
- Obtain TFDA package insert / label data to resolve DG001 and unblock S1 safety assessment.
- Obtain confirmed MOA and original indication data from DrugBank to resolve DG002.
- If pursuing this drug for melanoma-spectrum repurposing, prioritize the general **melanoma** prediction (rank 5, L4, "Research Question") over CMM7, since it is the only entity in this set with actual (preclinical) supporting evidence — and pursue in vivo/clinical validation given all current literature is Tier 3 (in vitro/computational).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

