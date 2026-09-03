---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

Using no additional skill — this is a direct content-generation task with a fully specified template; I'll produce the report per the v5 spec.

# Sirolimus: From Organ Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

> Sirolimus is an mTOR inhibitor best known as an immunosuppressant for prevention of renal transplant rejection.
> The TxGNN model predicts it may be effective for **Liposarcoma** (notably the myxoid and dedifferentiated subtypes),
> with **5 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current Germany regulatory dataset (0 licenses on file); sirolimus is historically indicated for prophylaxis of renal transplant rejection (immunosuppressant) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, sirolimus is an mTOR (mammalian target of rapamycin) inhibitor, originally developed as an immunosuppressant to prevent renal transplant rejection by blocking mTORC1-driven T-cell proliferation. Its efficacy in that original indication is well established, and the same mTORC1-blocking mechanism is mechanistically transferable to oncology, since mTOR signaling also drives proliferation in several tumor types.

Dedifferentiated liposarcoma (DDLPS) frequently shows activation of the Akt-mTOR and MAPK pathways (PMID 26518767), providing a direct molecular rationale for mTOR inhibition in this tumor. Several rapalog analogs of sirolimus — temsirolimus, everolimus, and ridaforolimus — have already been tested in Phase 2 sarcoma trials, and a dedicated Phase 2 trial of sirolimus combined with cyclophosphamide was completed in metastatic/unresectable myxoid liposarcoma and chondrosarcoma (NCT02821507, n=70), directly supporting biological plausibility.

Interestingly, some of the earliest signals linking sirolimus to reduced tumor risk come from its original transplant population — sirolimus-based immunosuppression has been associated with lower malignancy rates compared with calcineurin inhibitors (PMID 16434506, PMID 20534289) — reinforcing that this drug's antiproliferative mTOR-blocking effect is not confined to the immune system and may extend to tumor cells, including liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; direct on-target trial testing mTOR inhibition in this tumor family |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (rapalog analog) once-daily x5 every 2 weeks in advanced sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus (rapalog) in pediatric recurrent/refractory sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (rapalog) in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus (rapalog) + liposomal doxorubicin in advanced soft tissue and bone sarcomas |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2) | Clin Cancer Res | Ribociclib + everolimus showed synergistic growth inhibition in dedifferentiated liposarcoma and leiomyosarcoma models and clinical activity |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Cohort/Mechanistic | Tumour Biology | Akt-mTOR and MAPK pathways are activated in dedifferentiated liposarcoma specimens, supporting mTOR inhibitor rationale |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel FDA-approved and emerging targeted therapeutics in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of molecular-targeted agents and recent clinical trial rationale for advanced sarcomas |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine + rapamycin combination synergistically inhibits autophagy and is effective against well-differentiated liposarcoma |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical | In Vivo | Rapamycin + chloroquine arrests tumor growth in a patient-derived orthotopic xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | ATP-competitive mTOR kinase inhibitor MLN0128 shows potent antitumor activity in bone/soft-tissue sarcoma, addressing rapalog resistance |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatment approaches for rare connective tissue tumors and sarcomas, including mTOR-pathway agents |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | Randomized trial: sirolimus after cyclosporine withdrawal reduces cancer risk in adult renal transplant recipients, supporting antitumor properties of sirolimus beyond immunosuppression |
| [20534289](https://pubmed.ncbi.nlm.nih.gov/20534289/) | 2010 | Case series | Transplant Proc | Conversion to rapamycin-based immunosuppression after malignancy diagnosis in kidney transplant recipients, illustrating antitumor rationale of mTOR inhibition |

---

## Germany Market Information

Sirolimus is currently **not marketed** in Germany under this dataset (0 authorizations on file; no product/license records available).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated, completed Phase 2 trial (NCT02821507) directly tested sirolimus in myxoid liposarcoma/chondrosarcoma, and this is reinforced by a broader body of Phase 1/2 trials and mechanistic literature on rapalog-class mTOR inhibitors in sarcoma — meeting L2 evidence (one completed Phase 2/3 trial) rather than the stronger L1 threshold, so guarded rather than unconditional progression is warranted.

**To proceed, the following is needed:**
- TFDA/BfArM-equivalent label data on warnings, contraindications, and drug interactions (currently a Blocking data gap, DG001)
- Confirmed mechanism of action documentation from DrugBank (currently a High-severity data gap, DG002)
- Published efficacy/safety outcomes from NCT02821507 once fully reported
- Route and formulation compatibility assessment for oncology dosing versus the drug's existing immunosuppressant formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

