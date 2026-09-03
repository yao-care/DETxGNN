---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Established Tyrosine Kinase Inhibitor Indications to Liposarcoma

## One-Sentence Summary

> Sunitinib is a multi-targeted tyrosine kinase inhibitor with well-established use in gastrointestinal stromal tumour, advanced renal cell carcinoma, and pancreatic neuroendocrine tumour.
> The TxGNN model predicts it may also be effective for **Liposarcoma**,
> with **3 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local licensing data (drug not marketed in this jurisdiction); publicly known original indications include gastrointestinal stromal tumour, advanced renal cell carcinoma, and pancreatic neuroendocrine tumour |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack. Based on publicly known information, sunitinib is a multi-targeted receptor tyrosine kinase inhibitor acting on VEGFR1-3, PDGFRα/β, KIT, FLT3, and RET, and its efficacy in angiogenesis- and kinase-driven cancers such as GIST and renal cell carcinoma is well established.

Liposarcoma — particularly the myxoid subtype — shows angiogenesis dependence and partial PDGFR pathway activation, giving mechanistic plausibility for sunitinib's anti-angiogenic and anti-proliferative activity to extend into this tumour type. This is not purely theoretical: two independent completed Phase 2 trials have directly tested sunitinib in non-GIST sarcoma populations (including liposarcoma) and observed response signals, and a Tier-1 Phase 2 publication specifically evaluated sunitinib in relapsed/refractory liposarcoma, leiomyosarcoma, and malignant fibrous histiocytoma.

Because sunitinib's core anti-VEGFR/PDGFR mechanism is shared across its approved oncology indications and the proposed new indication, the repurposing hypothesis is biologically coherent rather than a purely data-driven correlation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of sunitinib in non-GIST sarcomas, including liposarcoma; direct evaluation of sunitinib's antitumour and antiangiogenic activity |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label trial of sunitinib malate in metastatic/unresectable soft tissue sarcoma (leiomyosarcoma, liposarcoma, fibrosarcoma, MFH); dosed until progression or toxicity |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 study of oral regorafenib (not sunitinib) in selected sarcoma subtypes; cites sunitinib's activity in soft tissue sarcoma as rationale for the class — indirect supporting evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | RCT/Phase 2 trial | International Journal of Cancer | Single-institution Phase 2 study of sunitinib malate in relapsed/refractory soft tissue sarcoma, focused on leiomyosarcoma, liposarcoma, and MFH; assessed safety and efficacy |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Reviews genetic, epigenetic, and transcriptomic alterations in liposarcoma to guide targeted therapy selection |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkológia | Reviews medical treatment of soft tissue sarcoma by histological subtype, including established and emerging targeted agents |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Reviews emerging therapies for adult soft tissue sarcoma, including subtype-specific drug sensitivity |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Discusses histology-driven therapy for soft tissue sarcoma; notes exceptionally high trabectedin activity in myxoid liposarcoma and related targeted approaches |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Review/genomic | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma; evaluates predictive factors for sunitinib benefit in a subset of patients |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series | American Journal of Surgical Pathology | Clinicopathologic analysis of 25 cases of a distinctive myofibroblastic sarcoma subtype with targetable molecular alterations |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Research | Long-lasting clinical benefit of sunitinib malate in a heavily pretreated patient with metastatic liposarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol (regorafenib) | BMC Cancer | REGOSARC trial protocol for regorafenib in advanced soft tissue sarcoma; cites sunitinib's role in sarcoma angiogenesis biology as background rationale |

---

## Germany Market Information

Sunitinib currently has **no marketing authorizations on record** in this jurisdiction (market status: Not Marketed; 0 authorizations). No product-level licensing data is available for review.

---

## Cytotoxicity

Sunitinib is an antineoplastic agent, originally developed and approved for oncology indications (GIST, advanced renal cell carcinoma, pancreatic neuroendocrine tumour), which brings this section into scope.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted receptor tyrosine kinase inhibitor: VEGFR1-3, PDGFRα/β, KIT, FLT3, RET) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 2 trials directly tested sunitinib in non-GIST soft tissue sarcoma populations including liposarcoma, and one Tier-1 Phase 2 publication specifically evaluated sunitinib in relapsed/refractory liposarcoma with a documented mechanistic basis (VEGFR/PDGFR inhibition). This is direct clinical evidence rather than model prediction alone, but it falls short of confirmatory randomized comparative data, so cautious, guardrail-bound advancement is appropriate rather than unrestricted "Go."

**To proceed, the following is needed:**
- Local regulatory data (approval status, licensed indications, dosage forms) since the drug is currently not marketed in this jurisdiction
- Mechanism-of-action documentation from DrugBank or the manufacturer's product information
- Local package insert warnings, contraindications, and drug interaction data (currently unavailable)
- A confirmatory, ideally randomized, trial specifically in liposarcoma populations to validate the signal seen in earlier non-GIST sarcoma studies
- Toxicity/monitoring data specific to this drug (e.g., myelosuppression, cardiovascular, hepatic) to complete the cytotoxicity risk profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

