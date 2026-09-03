---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

Using the evidence pack as-is, here's the report:

---

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Levofloxacin is a broad-spectrum fluoroquinolone antibiotic already established for treating bacterial infections.
> The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
> but currently only **1 publication** supports this direction — and that report actually describes a *microsporidial* (non-bacterial) pathogen, a mechanistic mismatch that limits the strength of this specific signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibiotic class; no formal approved-indication text on file) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levofloxacin is a fluoroquinolone-class antibacterial agent, and its efficacy against bacterial infections is well established; mechanistically it could be applicable to *bacterial* forms of keratoconjunctivitis, where topical fluoroquinolones are already a common clinical choice.

However, the single piece of supporting literature in this evidence pack (PMID 30055152) does not actually describe a bacterial etiology — it reports an outbreak of **microsporidial** keratoconjunctivitis linked to contaminated swimming pool water in Taiwan. Microsporidia are eukaryotic pathogens outside levofloxacin's antibacterial spectrum, so this particular evidence does not mechanistically support the TxGNN prediction, even though the general drug class is plausible for bacterial keratoconjunctivitis.

It is also worth noting that among the 10 TxGNN-predicted indications in this evidence pack, two other candidates show substantially stronger evidence: **monoclonal gammopathy** (rank 6, evidence level L1, supported by a Phase 3 RCT — the TEAMM trial — for infection prophylaxis) and **septicemic plague** (rank 9, evidence level L2, an indication levofloxacin is already FDA-approved for via the Animal Rule). These may be more productive directions for further repurposing evaluation than the rank-1 candidate discussed here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak Report | American Journal of Ophthalmology | Describes an outbreak of **microsporidial** (non-bacterial) keratoconjunctivitis from contaminated swimming pools in Taiwan; pathogen type does not match levofloxacin's antibacterial mechanism |

## Taiwan Market Information

Levofloxacin currently has no TFDA marketing authorization on file (0 licenses) and is not marketed in Taiwan according to this dataset.

## Safety Considerations

Please refer to the package insert for safety information.

Note: Regulatory-grade labeling (warnings, contraindications) is flagged in this evidence pack as a **Blocking** data gap (DG001) — it must be resolved before this candidate can advance to any formal safety review (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature evidence for punctate epithelial keratoconjunctivitis describes a mechanistically mismatched pathogen (microsporidial, not bacterial), and evidence level L4 with no clinical trials does not support advancing this specific indication beyond a research question at this stage.

**To proceed, the following is needed:**
- TFDA-approved labeling (warnings/contraindications) — currently a Blocking gap (DG001)
- Formal mechanism of action documentation (DG002)
- Literature specifically evaluating levofloxacin against *bacterial* (not microsporidial) keratoconjunctivitis pathogens
- Consider redirecting repurposing evaluation toward the two higher-evidence candidates in this same pack: monoclonal gammopathy/plasma cell dyscrasia infection prophylaxis (L1, Phase 3 RCT) and septicemic plague (L2, FDA Animal Rule-approved)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

