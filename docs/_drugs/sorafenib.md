---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Sorafenib is a multi-target tyrosine kinase inhibitor originally developed for advanced renal cell carcinoma, later expanded to hepatocellular carcinoma and differentiated thyroid cancer.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> currently supported by **2 clinical trials** (1 directly using sorafenib) and **8 publications**, most of which are preclinical or review-level evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma / hepatocellular carcinoma (based on drug's known regulatory history; not present in current dataset) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known information, sorafenib is a multi-target tyrosine kinase inhibitor that blocks RAF/MEK/ERK signaling as well as VEGFR-1/2/3, PDGFR-β, c-KIT, and FLT3. Its efficacy in renal cell carcinoma and hepatocellular carcinoma is well established.

Liposarcoma, particularly the dedifferentiated subtype, has been shown to exhibit PTEN down-regulation and PDGFR pathway activation — both of which overlap with sorafenib's known targets. This provides a plausible mechanistic rationale for repurposing.

However, soft tissue sarcomas are highly heterogeneous, and not all subtypes respond uniformly to VEGFR/PDGFR-targeted therapy. The strongest direct clinical evidence comes from the SWOG S0505 trial, a Phase 2 study of sorafenib in advanced soft tissue sarcomas (not liposarcoma-specific), which supports biological activity but does not confirm subtype-specific efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Sorafenib (BAY 43-9006) in advanced soft tissue sarcomas, including liposarcoma subtypes; direct sorafenib evidence, corresponds to S0505 publication (PMID 21751200) |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 protocol testing **regorafenib** (not sorafenib) in selected sarcoma subtypes; included as indirect class-effect evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 Trial (SWOG S0505) | Cancer | Sorafenib evaluated in advanced soft tissue sarcomas; multitargeted TKI activity against RAF, VEGFR1-3, PDGFR-β, FLT3, c-KIT |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 Trial | Annals of Surgical Oncology | Neoadjuvant sorafenib + radiotherapy in extremity soft tissue sarcoma; synergistic antiangiogenic effect explored |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven sarcoma therapy; trabectedin highly active in myxoid liposarcoma, context for targeted agents |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Histological subtype-based medical treatment of soft tissue sarcomas |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX models identify CDK inhibitor combinations for sarcoma; broader targeted therapy rationale |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (PDX) | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models show PTEN down-regulation as malignant signature, sensitive to PI3K pathway inhibition |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth and MAPK signaling in malignant peripheral nerve sheath and dedifferentiated liposarcoma cell lines |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case Report (trabectedin, non-sorafenib) | Anti-Cancer Drugs | Response to trabectedin (not sorafenib) in synovial sarcoma; included for sarcoma treatment context only |

---

## Germany Market Information

Sorafenib is currently **not marketed** in Germany per this dataset, with no authorization records available (0 licenses on file).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to Moderate — TKI-class drugs typically cause less myelosuppression than conventional cytotoxics; skin toxicity (hand-foot skin reaction) is a more prominent class effect |
| Emetogenicity Classification | Low — oral TKIs generally carry minimal emetogenic potential |
| Monitoring Items | Blood pressure, liver function tests, CBC, skin/dermatologic assessment, thyroid function |
| Handling Protection | As an oral antineoplastic agent, standard institutional hazardous-drug handling precautions apply; please refer to the package insert warnings and precautions for detailed guidance |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial directly using sorafenib (SWOG S0505) demonstrates biological activity in advanced soft tissue sarcomas, and the PDGFR/PTEN pathway rationale for dedifferentiated liposarcoma is mechanistically plausible. However, evidence is limited to a single Phase 2 study without liposarcoma-subtype stratification, and one of the two listed trials (SARC024) actually tested regorafenib rather than sorafenib.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA/BfArM package insert warnings and contraindications before any S1 safety review
- Resolve High-priority data gap DG002: confirm detailed MOA via DrugBank API query
- Liposarcoma subtype-specific clinical data (dedifferentiated vs. myxoid vs. pleomorphic), as current trial evidence is not subtype-stratified
- Comparative efficacy data versus current standard-of-care agents (trabectedin, eribulin) in liposarcoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

