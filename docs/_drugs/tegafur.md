---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: From Gastrointestinal Cancers to Colonic Neoplasm

## One-Sentence Summary

> Tegafur is a prodrug of 5-fluorouracil (5-FU), traditionally used as a component of fluoropyrimidine combination regimens (UFT, S-1) for gastrointestinal malignancies including gastric cancer.
> The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
> with **30 clinical trials** and **20 publications** currently supporting this direction — though the evidence largely confirms an *already-established* use rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastrointestinal cancers (e.g. gastric cancer), as prodrug component of UFT (tegafur+uracil) and S-1 (tegafur+gimeracil+oteracil) — no formal Germany/Taiwan license record available |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal MOA record is not available in the drug-level field, but the evidence pack's mechanistic rationale is clear: tegafur is a prodrug of 5-fluorouracil, metabolically activated via hepatic **CYP2A6**. Once converted to 5-FU, it inhibits thymidylate synthase, blocking DNA synthesis — a classical antimetabolite chemotherapy mechanism.

Tegafur is never used alone clinically; it is formulated into combination products — **UFT** (tegafur + uracil, where uracil blocks 5-FU catabolism via DPD) and **S-1** (tegafur + gimeracil + oteracil, adding DPD inhibition and gastrointestinal toxicity reduction). Both combinations are already established standard adjuvant/palliative chemotherapy regimens for colorectal cancer in multiple countries (notably Japan), as reflected by the very large body of Phase 3 trials below.

This means the TxGNN prediction is not identifying a truly novel indication, but rather **recovering an already-approved use** — the mechanism (antimetabolite disruption of DNA synthesis in rapidly dividing epithelial cells) is directly applicable to colonic adenocarcinoma, and the clinical evidence base is mature rather than exploratory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | UFT+LV vs 5-FU+LV in resected stage II/III colon cancer |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant UFT vs observation in curatively resected stage II colon cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+LV vs S-1 as adjuvant treatment for stage III colon cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs capecitabine in first-line metastatic colorectal cancer |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | Completed | 89 | Crossover comparison of capecitabine vs UFT+folinic acid in advanced/metastatic CRC |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | NSAS-CC: postoperative UFT vs surgery alone in Dukes C colorectal cancer |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | Completed | 47 | Cetuximab + irinotecan + oxaliplatin + UFT in first-line metastatic CRC |
| [NCT00439517](https://clinicaltrials.gov/study/NCT00439517) | Phase 2 | Completed | 302 | FOLFOX-4+Cetuximab vs UFOX+Cetuximab in metastatic colorectal cancer |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | Unknown | 380 | UFT+PSK vs UFT+LV as adjuvant therapy for stage IIB/III colorectal cancer |
| [NCT02887365](https://clinicaltrials.gov/study/NCT02887365) | Phase 4 | Unknown | 300 | Tegafur-uracil as metronomic maintenance therapy in stage II MSI-L/MSS colon cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 5-year update: S-1+oxaliplatin not superior to UFT/LV in high-risk stage III colon cancer |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 phase III trial establishing UFT/LV as adjuvant comparator standard |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06: oral UFT+LV vs IV 5-FU+LV in stage II/III colon carcinoma |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT | Ann Oncol | JFMC33-0502: optimal duration of UFT/LV adjuvant chemotherapy in stage IIB/III colon cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy vs chemotherapy using UFT combinations in colorectal cancer |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | RCT | Am J Clin Oncol | Oral tegafur vs IV 5-FU in metastatic colorectal cancer |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT/Cohort | Medicine | Taiwan NHIRD nationwide cohort: UFT vs 5-FU as postoperative adjuvant chemotherapy in stage II/III colon cancer |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Cohort | BMC Cancer | JFMC46-1201: UFT/LV efficacy in high-risk stage II colon cancer (propensity score matched) |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Cohort | Int J Clin Oncol | JFMC46-1201 final analysis: updated 5-year OS and risk factors |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus guideline for metastatic colorectal cancer management |

---

## Germany Market Information

No authorization records are available — tegafur (or its combination products UFT/S-1) is currently **not marketed** in Germany under this evidence pack (0 licenses on file).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine class, 5-FU prodrug) |
| Myelosuppression Risk | Moderate — consistent with fluoropyrimidine class effects (neutropenia, thrombocytopenia); no drug-specific toxicity dataset provided |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function; **DPD/DPYD genotype screening recommended prior to initiation** (per fluoropyrimidine safety evidence, e.g. NCT05266300) |
| Handling Protection | Must follow standard cytotoxic drug handling and disposal regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (n up to 2025) consistently support tegafur-based combination regimens (UFT, S-1) as effective adjuvant/palliative therapy for colon cancer, and this use is already standard practice in several markets — this is evidence consolidation of an existing indication rather than a speculative new use. However, the drug currently has zero marketing authorizations in Germany and lacks formal safety/label data.

**To proceed, the following is needed:**
- Official TFDA/BfArM package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed drug-level MOA documentation from DrugBank to formally close the mechanism data gap
- DPD/DPYD deficiency screening protocol before recommending clinical use, given fluoropyrimidine class toxicity risk
- Regulatory pathway assessment given the drug is not currently marketed in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

