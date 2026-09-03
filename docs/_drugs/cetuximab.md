---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: From EGFR-Targeted Cancer Therapy to Cystic Neoplasm (Salivary Gland Adenoid Cystic/Mucoepidermoid Carcinoma)

## One-Sentence Summary

> This evidence pack evaluates **10 TxGNN-predicted indications** for cetuximab, an anti-EGFR monoclonal antibody. Evidence pack literature (PMID 39415301) confirms cetuximab's established use is "**head and neck squamous cell carcinoma and metastatic colorectal cancer**."
> Among the 10 candidates, most (7/10) are pure model predictions with **no supporting trials or literature** (Evidence Level L5, Hold). The strongest candidate is **Cystic Neoplasm** — specifically salivary gland adenoid cystic carcinoma / mucoepidermoid carcinoma — supported by **5 clinical trials and 6+ relevant publications**, reaching Evidence Level **L2**.
> However, a **Blocking data gap** (missing TFDA/BfArM label safety data) prevents any candidate from entering formal safety pre-assessment (S1), so the overall recommendation is **Hold** at the drug level.

---

## Quick Overview (Primary Candidate: Cystic Neoplasm)

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset (`original_indications` empty; `original_moa` = data gap). Per evidence-pack literature (PMID 39415301), cetuximab is documented as being "used to treat head and neck squamous cell carcinoma and metastatic colorectal cancer." |
| Predicted New Indication | Cystic Neoplasm (rank 9) — primarily supported evidence relates to salivary gland adenoid cystic carcinoma (ACC) and mucoepidermoid carcinoma (MEC) |
| TxGNN Prediction Score | 99.95% (score 0.999487, model rank 921) |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (blocked by missing safety/label data, see below) |

---

## All 10 Predicted Indications — Portfolio Overview

Because this evidence pack covers a multi-candidate ranking (`TW-DB00002-multi`), the full landscape is summarized before drilling into the strongest candidate:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Chondroid hamartoma | 99.95% | L5 | S0 | Hold |
| 2 | Non-seminomatous lesion | 99.95% | L5 | S0 | Hold |
| 3 | Ductal or ductular proliferation | 99.95% | L5 | S0 | Hold (20 mechanistic liver-fibrosis papers, none drug-relevant) |
| 4 | Bronchial adenomas/carcinoids (childhood) | 99.95% | L5 | S0 | Hold |
| 5 | Tumor of testis and paratestis | 99.95% | L5 | S0 | Hold |
| 6 | Odontogenic cyst | 99.95% | L4 | S0 | Hold (2 indirect case reports) |
| 7 | Thyroglossal duct cyst | 99.95% | L5 | S0 | Hold |
| 8 | Epiglottis neoplasm | 99.95% | L4 | S1 | Research Question (class-level HNSCC extrapolation, no direct evidence) |
| **9** | **Cystic neoplasm** | **99.95%** | **L2** | **S2** | **Research Question** (best-supported candidate) |
| 10 | Pre-malignant neoplasm | 99.95% | L3 | S1 | Research Question (chemoprevention rationale, disease-mapping mismatch in trials) |

**Interpretation:** 7 of 10 candidates are pure TxGNN score artifacts with zero supporting evidence and should not be pursued. Only ranks 8, 9, and 10 warrant further research attention, and rank 9 (Cystic Neoplasm) is the only one with a completed Phase II trial directly relevant to the mechanism.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cetuximab is not available in this evidence pack (`original_moa` = data gap). Based on the trial and literature content actually present, cetuximab is a chimeric anti-EGFR monoclonal antibody: multiple trial summaries in this pack describe it as blocking EGFR signaling to inhibit tumor cell growth and spread (e.g., NCT00397384, NCT01637194), and it is documented as a treatment for head and neck squamous cell carcinoma and metastatic colorectal cancer (PMID 39415301).

Salivary gland tumors — including adenoid cystic carcinoma (ACC) and mucoepidermoid carcinoma (MEC), both of which fall under the TxGNN-predicted category "cystic neoplasm" — are known in the evidence pack literature to frequently overexpress EGFR (PMID 18804410, PMID 18366287). This provides a direct mechanistic bridge from cetuximab's established EGFR-blocking activity to this new indication, distinct from the purely statistical, no-evidence predictions elsewhere in this pack (e.g., chondroid hamartoma, thyroglossal duct cyst).

The supporting evidence includes a completed Phase II study of cetuximab in recurrent/metastatic salivary gland carcinomas (PMID 18804410), a Phase I/II feasibility trial combining cetuximab with particle therapy specifically in adenoid cystic carcinoma (NCT01192087, relevance grade A), and case reports of clinical response in ACC and MEC (PMID 22144378, PMID 32518035). This is a substantially stronger evidentiary basis than the other 9 candidates in this pack.

---

## Clinical Trial Evidence (Cystic Neoplasm)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Unknown | 49 | ACCEPT trial: cetuximab combined with IMRT plus carbon-ion boost specifically in adenoid cystic carcinoma (ACC) — directly relevant (relevance grade A) |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | Completed | 43 | Combined EGFR blockade with erlotinib and cetuximab in advanced GI, head & neck, NSCLC, and colorectal cancer (relevance grade B) |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | Completed | 12 | Cetuximab plus everolimus (RAD001) in solid tumors, including head & neck cancer (relevance grade B) |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Completed | 66 | Erlotinib + cetuximab ± bevacizumab across renal, colorectal, head & neck, pancreatic, and NSCLC (relevance grade B) |
| [NCT00896896](https://clinicaltrials.gov/study/NCT00896896) | N/A | Completed | 538 | Immunoreactivity/hypersensitivity to cetuximab in head & neck and colorectal cancer patients (relevance grade C, safety-focused) |

---

## Literature Evidence (Cystic Neoplasm)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase II Trial | Oral oncology | Cetuximab in 30 patients with recurrent/metastatic salivary gland carcinoma (23 ACC, 7 non-ACC); clinical benefit rate assessed based on EGFR overexpression rationale |
| [22144378](https://pubmed.ncbi.nlm.nih.gov/22144378/) | 2013 | Case Report | Head & neck | Metastatic adenoid cystic carcinoma of the salivary gland responding to cetuximab plus weekly paclitaxel after failure of paclitaxel alone |
| [22246397](https://pubmed.ncbi.nlm.nih.gov/22246397/) | 2012 | Preclinical | Oncology reports | Cetuximab inhibits growth of mucinous ovarian carcinoma (cystic tumor) cell lines lacking KRAS mutations |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Case Report | Oral oncology | Cetuximab monotherapy for relapsing high-grade mucoepidermoid carcinoma |
| [18366287](https://pubmed.ncbi.nlm.nih.gov/18366287/) | 2008 | Review | Expert review of anticancer therapy | Systemic therapies for recurrent/metastatic salivary gland cancers, including cetuximab in ACC |
| [39415301](https://pubmed.ncbi.nlm.nih.gov/39415301/) | 2024 | Case Report | Journal of medical case reports | Successful cetuximab administration via dose-escalation to manage infusion reactions; confirms established use in HNSCC and metastatic colorectal cancer |

---

## Germany Market Information

Currently no marketing authorizations for cetuximab are recorded in this dataset (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No product, dosage form, or approved indication data is available.

---

## Cytotoxicity

Cetuximab is an antineoplastic agent (anti-EGFR chimeric monoclonal antibody, used across multiple cancer indications per trial and literature evidence in this pack).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — anti-EGFR monoclonal antibody (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Not directly documented in this evidence pack; as an antibody-based targeted agent, myelosuppression is not the class-typical toxicity signal (unlike cytotoxic chemotherapy). Please refer to the package insert. |
| Emetogenicity Classification | Please refer to the package insert (no data in evidence pack) |
| Monitoring Items | Based on evidence-pack literature: infusion-related hypersensitivity reactions (NCT00896896), dermatologic/skin toxicity (PMID 30141310); general CBC and liver/renal function monitoring recommended when combined with cytotoxic chemotherapy regimens |
| Handling Protection | Monoclonal antibody IV infusion — standard infusion safety protocols apply (premedication for hypersensitivity); not classified as a hazardous cytotoxic drug under conventional chemotherapy handling regulations |

---

## Safety Considerations

Formal safety data (`key_warnings`, `contraindications`, DDI) is not available in this evidence pack — please refer to the package insert for safety information.

Supplementary signals identified in the literature/trial evidence (not verified against an official label):
- Infusion-related hypersensitivity reactions (NCT00896896, PMID 39415301)
- Dermatologic toxicity/skin disorders, associated with prognosis in colorectal cancer patients (PMID 30141310)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Data gap **DG001** (TFDA/BfArM label warnings and contraindications) is classified as **Blocking severity** and explicitly prevents entry into the S1 safety pre-assessment stage — no candidate in this pack can proceed regardless of scientific merit until this is resolved.
- Of 10 predicted indications, 7 have zero supporting evidence (pure model score, L5) and should be deprioritized. Only Cystic Neoplasm (L2, S2) shows real Phase II/case-report support and merits continued monitoring as a research question, not immediate action.
- Cetuximab is currently unmarketed in Germany (0 authorizations), adding a regulatory barrier independent of the scientific evidence.

**To proceed, the following is needed:**
- Retrieve TFDA/BfArM label PDF and parse warnings/contraindications (DG001 remediation)
- Query DrugBank for confirmed MOA data (DG002 remediation)
- If pursuing the Cystic Neoplasm lead, commission a focused literature/trial review scoped specifically to salivary gland ACC/MEC (rather than "cystic neoplasm" broadly, which pulled in unrelated ovarian/pancreatic cystic entities)
- Reassess German/EU market access pathway given current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

