---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

# IDELALISIB: From B-cell Lymphoid Malignancies to Mantle Cell Lymphoma

## One-Sentence Summary

Idelalisib is a selective PI3Kδ inhibitor originally developed for B-cell lymphoid malignancies (chronic lymphocytic leukemia, follicular lymphoma, small lymphocytic lymphoma).
The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**,
with **9 clinical trials** and **20 publications** currently supporting this direction — though confirmatory Phase 2/3 evidence specific to MCL is still lacking.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in evidence pack (data gap — `drug.original_indications` is empty). Based on the drug's known identity (idelalisib/Zydelig®) referenced throughout the evidence pack's own mechanistic rationale, the drug's established indications are relapsed CLL, follicular lymphoma, and small lymphocytic lymphoma. |
| Predicted New Indication | Mantle Cell Lymphoma |
| TxGNN Prediction Score | 99.84% (rank 2395) |
| Evidence Level | L3 |
| Germany Market Status | 未上市 (Not marketed) — flagged internally as a likely data gap rather than a true absence of licensure (see rationale below) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `drug.original_moa` field (data gap, item DG002). Based on information embedded elsewhere in this evidence pack, idelalisib is a selective, orally bioavailable inhibitor of the δ-isoform of phosphatidylinositol 3-kinase (PI3Kδ). PI3Kδ signaling is a core component of the B-cell receptor (BCR) pathway, which drives survival and proliferation in multiple B-cell malignancies.

Mantle cell lymphoma is, like idelalisib's established indications (CLL, FL, SLL), a BCR-signaling-dependent B-cell lymphoma. This shared molecular dependency is the biological basis for the TxGNN prediction: a drug validated against one BCR-driven malignancy is mechanistically plausible against another. In vitro studies included in this evidence pack directly support this — idelalisib inhibits growth and induces apoptosis in MCL cell lines (PMID 27342398, PMID 33850273, PMID 40466505), and an early-phase clinical study reported measurable single-agent activity in relapsed/refractory MCL patients (PMID 24795031, PMID 24615778).

At the same time, the evidence pack itself notes that idelalisib shows *intrinsic resistance* in a subset of MCL cases (PMID 33850273), and several trials combining idelalisib with other agents in MCL were terminated early (e.g., NCT01796470, NCT02457598) — indicating that while the mechanistic rationale is sound, clinical translation in MCL specifically has not yet been confirmed at a definitive level.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Safety of idelalisib combined with anti-CD20 mAb, chemotherapy, mTOR/protease/antiangiogenic/immunomodulatory agents in relapsed/refractory iNHL, MCL, or CLL |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 | Completed | 106 | Idelalisib + lenalidomide in relapsed/refractory MCL — dedicated Phase I/randomized Phase II design |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 + idelalisib in follicular lymphoma and MCL; safety/tolerability primary endpoint |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib + idelalisib in relapsed/refractory hematologic malignancies incl. MCL |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with targeted anti-cancer therapies (incl. idelalisib) in B-cell malignancies incl. MCL |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell malignancies |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-world PK/toxicity correlation of ibrutinib and idelalisib in hematological malignancies including MCL |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality of life in lymphoma patients on oral therapies, including idelalisib for MCL |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib in CLL/SLL and NHL — idelalisib appears only as background/prior therapy, not the study drug |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Cohort | Cancer Discovery | Idelalisib showed measurable single-agent activity in heavily pretreated relapsed/refractory MCL patients |
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 clinical study | Blood | 48-week Phase 1 study of idelalisib (50–350 mg) in 40 patients with relapsed/refractory MCL; reported ORR, PFS, DOR |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Preclinical | Clin Cancer Res | Idelalisib disrupts translation-regulatory mechanisms to suppress MCL cell growth |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacol Sin | P300/CBP inhibitor A-485 overcomes intrinsic idelalisib resistance in MCL cells in vitro/in vivo |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL; propolis restores idelalisib sensitivity via ferroptosis |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances anti-tumor effect of CDK4/6 inhibitor palbociclib via PLK1 in relapsed/refractory MCL and DLBCL |
| [28295729](https://pubmed.ncbi.nlm.nih.gov/28295729/) | 2017 | Review | J Intern Med | Reviews BCR-pathway-targeted agents; notes idelalisib's established role across CLL and MCL |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | Br J Haematol | Overview of current and novel agents (incl. PI3K-pathway inhibitors) for MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opin Pharmacother | Review of treatment options for MCL, including targeted BCR-pathway agents |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Review | Curr Treat Options Oncol | Current and emerging therapies in MCL |

---

## Germany Market Information

No marketing authorizations are listed in the evidence pack (`total_licenses: 0`, `market_status: 未上市`). This most likely reflects an incomplete data pull rather than genuine absence from the market, since idelalisib (brand name Zydelig®) is externally documented as EMA-approved for CLL and relapsed follicular lymphoma — a discrepancy this evidence pack itself flags in the rationale for the "B-cell neoplasm" prediction. **This regulatory-status field should be independently verified (see DG001) before any go/no-go decision is finalized.**

---

## Cytotoxicity

Idelalisib is an antineoplastic agent (approved oncology indication; kinase-inhibitor class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ-selective small-molecule kinase inhibitor; non-cytotoxic mechanism) |
| Myelosuppression Risk | Not quantifiable from this evidence pack (safety data flagged as data gap). Literature in this pack references neutropenia and cytopenia monitoring in idelalisib-treated patients — please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. All structured safety fields in this evidence pack (`key_warnings`, `contraindications`, `ddi`) are marked as data gaps, and this is flagged as a **Blocking** gap (DG001) that prevents entry into the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to idelalisib in MCL is currently limited to completed Phase 1 trials and preclinical mechanistic studies (Evidence Level L3, decision stage S2, TxGNN's own recommendation is "Research Question"), with no completed Phase 2/3 confirmatory trial for this indication. Combined with a **blocking** data gap in TFDA/label safety information (DG001), a full safety and efficacy assessment cannot yet be completed.

**To proceed, the following is needed:**
- Retrieve and parse the official product label (TFDA/EMA) to resolve DG001 and enable S1 safety review
- Confirm mechanism-of-action documentation via DrugBank to resolve DG002
- Independently verify true German/Taiwan marketing and licensing status (current "not marketed / 0 licenses" appears inconsistent with idelalisib's known global approval history)
- Monitor for initiation of a dedicated Phase 2/3 trial in relapsed/refractory MCL
- Establish a safety monitoring plan addressing known class-effect toxicities of PI3Kδ inhibitors (hepatotoxicity, colitis/diarrhea, pneumonitis, opportunistic infection) once label data is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

