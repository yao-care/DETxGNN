---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Renal Cell Carcinoma to Liposarcoma and Other Rare Sarcomas

## One-Sentence Summary

Everolimus is an mTOR-pathway inhibitor with well-established oncology use (e.g., non-clear cell renal cell carcinoma, per the ASPEN and CABOSUN-era comparator literature in this evidence pack); its detailed original indication label and mechanism-of-action record are currently a data gap for this jurisdiction. TxGNN flags 10 candidate indications, the top-ranked being **Liposarcoma**, but the strength of supporting evidence varies sharply across candidates — from a single confounded Phase 2 combination trial (liposarcoma) to a mature multi-RCT evidence base (unclassified/non-clear cell renal cell carcinoma). Overall, **1 clinical trial + 5 publications** support the top-ranked liposarcoma prediction, while a stronger secondary candidate (unclassified RCC) is backed by **1 trial + 9 publications**, including two randomized Phase 2 trials (ASPEN).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local regulatory licenses (drug status: 未上市 / not marketed in this jurisdiction). Everolimus is a globally established mTOR inhibitor used in oncology (e.g., advanced/non-clear cell renal cell carcinoma), as referenced in the literature evidence below. |
| Predicted New Indication | Liposarcoma (dedifferentiated subtype) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (data pack labels this "Research Question" stage — evidence exists but is confounded by combination therapy) |

> **Note:** This drug has 10 TxGNN-predicted indications with markedly different evidence maturity. See the overview table below before reading the detailed sections, which focus on the three candidates with actual clinical evidence.

### Predicted Indications at a Glance (All 10 Candidates)

| Rank | Disease | TxGNN Score | Trials | Papers | Evidence Level | Recommendation |
|------|---------|------|------|------|------|------|
| 1 | Liposarcoma | 99.88% | 1 | 5 | L2 | Research Question |
| 2 | Ovarian myxoid liposarcoma | 99.84% | 0 | 0 | L5 | Hold |
| 3 | Dermatofibrosarcoma protuberans | 99.82% | 0 | 2 (off-target, imatinib) | L5 | Hold |
| 4 | Parameningeal embryonal rhabdomyosarcoma | 99.77% | 0 | 0 | L5 | Hold |
| 5 | Botryoid-type embryonal rhabdomyosarcoma (vagina) | 99.76% | 0 | 0 | L5 | Hold |
| 6 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.75% | 0 | 0 | L5 | Hold |
| 7 | Rhabdomyosarcoma (general) | 99.74% | 3 | 3 | L2 | Research Question |
| 8 | Prostate embryonal rhabdomyosarcoma | 99.74% | 0 | 0 | pending | pending |
| 9 | Renal cell carcinoma associated with neuroblastoma | 99.72% | 0 | 0 | L5 | Hold |
| 10 | Unclassified renal cell carcinoma | 99.72% | 1 (off-target) | 9 | **L2** | **Proceed with Guardrails** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for everolimus is not available in this evidence pack (Data Gap DG002). Based on known pharmacology, everolimus is an mTOR (mechanistic target of rapamycin) inhibitor — a rapalogue class agent. This is corroborated indirectly by the pack's own literature, which repeatedly frames everolimus as "the mTOR inhibitor" in combination and comparator studies (e.g., lenvatinib + everolimus, ribociclib + everolimus, everolimus vs. sunitinib).

The common thread across nearly all top-ranked TxGNN predictions is aberrant activation of the **PI3K–Akt–mTOR pathway**: dedifferentiated liposarcoma shows Akt-mTOR/MAPK pathway activation (PMID 26518767); spindle-cell rhabdomyosarcoma shows PI3KCA/PTEN mutations converging on the same pathway (PMID 35012940); and non-clear-cell/unclassified renal cell carcinoma has an established, RCT-validated mTOR-inhibitor treatment history (ASPEN trial). This mechanistic convergence explains why TxGNN ranks these rare, difficult-to-treat sarcomas and RCC subtypes highly for an mTOR inhibitor already active in oncology.

However, evidentiary maturity differs greatly by candidate. The top-ranked liposarcoma prediction rests entirely on a **combination** trial (ribociclib + everolimus) — the CDK4/6 inhibitor confounds attribution of efficacy to everolimus itself. By contrast, unclassified/non-clear-cell RCC (rank 10) has direct, randomized, everolimus-monotherapy evidence (ASPEN, PMID 26794930/26626617) and an FDA-approved combination regimen (lenvatinib + everolimus, PMID 33867192), making it mechanistically and clinically the most defensible candidate in this set despite ranking lower on the raw TxGNN score.

---

## Clinical Trial Evidence

### Primary Candidate: Liposarcoma (Rank 1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma; evaluates anti-tumor activity of the doublet, but does not isolate everolimus's independent contribution. |

### Additional High-Evidence Candidate: Rhabdomyosarcoma (Rank 7)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03245151](https://clinicaltrials.gov/study/NCT03245151) | Phase 1/2 | Completed | 64 | Lenvatinib + everolimus in recurrent/refractory pediatric solid tumors including rhabdomyosarcoma; established MTD/RP2D and antitumor activity. |
| [NCT01216839](https://clinicaltrials.gov/study/NCT01216839) | Phase 2 | Unknown | 20 | Everolimus **monotherapy** in refractory/relapsed pediatric rhabdomyosarcoma and other soft-tissue sarcomas; small sample, status unresolved. |
| [NCT00187174](https://clinicaltrials.gov/study/NCT00187174) | Phase 1 | Completed | 41 | Everolimus monotherapy in pediatric refractory solid/brain tumors (basket trial, low disease specificity). |

### Additional High-Evidence Candidate: Unclassified Renal Cell Carcinoma (Rank 10)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04134390](https://clinicaltrials.gov/study/NCT04134390) | Phase 2 | Completed | 25 | Cabozantinib (not everolimus) in elderly/frail metastatic RCC; cited only for context — everolimus is mentioned as the Checkmate-025 comparator, not the study drug. |

*(Note: the strongest RCT evidence for this candidate — ASPEN — is captured under Literature Evidence below rather than the trials registry excerpt provided.)*

---

## Literature Evidence

### Primary Candidate: Liposarcoma (Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Clinical Trial (Phase 2 report) | Clin Cancer Res | Full report of ribociclib + everolimus in advanced DDL/LMS; synergistic growth inhibition rationale (CDK4 + mTOR co-inhibition). |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse models support CDK inhibitor combinations (e.g., palbociclib) in sarcoma; supportive but not everolimus-specific. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/Preclinical | Tumour Biology | Confirms Akt-mTOR and MAPK pathway activation in dedifferentiated liposarcoma — the mechanistic basis for mTOR-inhibitor targeting. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical combination study | Anticancer Research | Eribulin combination screening in liposarcoma models; tangential, not everolimus-specific. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Mechanistic/Preclinical | Oncogene | XPO1 inhibitor (selinexor) mechanism in dedifferentiated liposarcoma; not everolimus-related, included for pathway context only. |

### Additional High-Evidence Candidate: Rhabdomyosarcoma (Rank 7)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40313040](https://pubmed.ncbi.nlm.nih.gov/40313040/) | 2025 | Clinical Trial (Phase 1/2 report) | Pediatr Blood Cancer | Full report of lenvatinib + everolimus in recurrent/refractory pediatric/young-adult solid tumors; defines RP2D and antitumor activity. |
| [35012940](https://pubmed.ncbi.nlm.nih.gov/35012940/) | 2022 | Functional/Preclinical | Cold Spring Harb Mol Case Stud | PI3KCA/GNAS/PTEN mutations in MYOD1-mutant spindle cell rhabdomyosarcoma — direct mechanistic rationale for mTOR pathway targeting. |
| [34295326](https://pubmed.ncbi.nlm.nih.gov/34295326/) | 2021 | Clinical Trial (not everolimus primary) | Front Immunol | PD-1 antibody ± combination in pediatric relapsed/refractory cancer; tangential, low direct relevance. |

### Additional High-Evidence Candidate: Unclassified Renal Cell Carcinoma (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26794930](https://pubmed.ncbi.nlm.nih.gov/26794930/) | 2016 | RCT (ASPEN, Phase 2) | Lancet Oncology | Everolimus vs. sunitinib in non-clear-cell RCC, multicentre randomized Phase 2 — primary RCT evidence for this indication. |
| [26626617](https://pubmed.ncbi.nlm.nih.gov/26626617/) | 2016 | RCT (Phase 2) | European Urology | Corroborating randomized Phase 2 (ESPN) comparing everolimus and sunitinib in metastatic non-clear-cell RCC. |
| [23180114](https://pubmed.ncbi.nlm.nih.gov/23180114/) | 2013 | Clinical Trial (Phase 2, monotherapy) | Ann Oncol | Everolimus monotherapy Phase 2 in non-clear-cell RCC. |
| [27601542](https://pubmed.ncbi.nlm.nih.gov/27601542/) | 2016 | Clinical Trial (Phase 2) | J Clin Oncol | Everolimus + bevacizumab in advanced non-clear-cell RCC with correlative genomic analysis. |
| [33867192](https://pubmed.ncbi.nlm.nih.gov/33867192/) | 2021 | Clinical Trial (Phase 2) | European Urology | Lenvatinib + everolimus in non-clear-cell RCC — this combination is already an approved regimen for advanced RCC after prior antiangiogenic therapy. |
| [32975815](https://pubmed.ncbi.nlm.nih.gov/32975815/) | 2020 | Cohort/Clinical study | Cancer | Everolimus + bevacizumab shows encouraging first-line activity in papillary/unclassified RCC. |
| [24458473](https://pubmed.ncbi.nlm.nih.gov/24458473/) | 2014 | Retrospective cohort | Ann Oncol | mTOR inhibitors (temsirolimus/everolimus) effective in non-clear-cell and sarcomatoid RCC histologies. |
| [34765076](https://pubmed.ncbi.nlm.nih.gov/34765076/) | 2021 | Correlative/Biomarker study | Kidney Cancer J | ASPEN trial biomarker sub-analysis in papillary/chromophobe/unclassified RCC. |
| [33593885](https://pubmed.ncbi.nlm.nih.gov/33593885/) | 2021 | Cohort/Biomarker study | Clin Cancer Res | Angiokine biomarkers associated with everolimus vs. sunitinib outcomes in non-clear-cell RCC. |

---

## Germany Market Information

Currently no marketing authorization records are available for everolimus in this jurisdiction (`taiwan_regulatory.market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license table can be produced from this evidence pack.

---

## Cytotoxicity

Everolimus is an oncology agent (mTOR inhibitor) and is therefore assessed under this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalogue) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Not specified in this evidence pack; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not specified in this evidence pack; please refer to the package insert warnings and precautions |
| Monitoring Items | Standard oncology monitoring recommended (CBC, renal and hepatic function, fasting glucose/lipids); confirm specifics against the package insert |
| Handling Protection | Not specified in this evidence pack; follow institutional hazardous-drug handling policy pending package insert confirmation |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all recorded as data gaps in this evidence pack — DG001, blocking severity — and DDI lookup returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold (top-ranked candidate) / Proceed with Guardrails (best-supported candidate — unclassified/non-clear-cell RCC)**

**Rationale:**
- The top-ranked prediction (liposarcoma) rests on a single combination trial that confounds everolimus's independent contribution — insufficient to proceed on its own.
- The strongest evidence in this entire prediction set belongs to **unclassified renal cell carcinoma** (rank 10): two randomized Phase 2 trials (ASPEN, ESPN) plus an FDA-approved combination regimen (lenvatinib + everolimus) justify a "Proceed with Guardrails" stance for that specific indication.
- Rhabdomyosarcoma (rank 7) has a plausible mechanistic basis and a completed Phase 1/2 combination trial, but the sole everolimus-monotherapy trial (NCT01216839) has unknown status and a small sample — remains at "Research Question" stage.
- The remaining 6 candidates (ranks 2–6, 9) have no clinical trial or literature support (L5) and should not be pursued without new primary evidence.

**To proceed, the following is needed:**
- Resolve Data Gap DG001 (TFDA/label warnings and contraindications) — currently a blocking gap for any safety evaluation.
- Resolve Data Gap DG002 (structured MOA from DrugBank) to formally validate the mechanistic rationale used above.
- For liposarcoma: seek an everolimus-monotherapy or attribution-designed trial to de-confound the ribociclib combination signal.
- For unclassified/non-clear-cell RCC: confirm local regulatory pathway feasibility (currently 未上市) before any guardrailed use, since no local license or safety label currently exists.
- For rhabdomyosarcoma: monitor completion/results of NCT01216839 and NCT03245151 (already completed — pull full trial results/publication if not yet captured).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

