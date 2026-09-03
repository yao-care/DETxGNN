---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From No Standalone Indication (S-1 Combination Component) to Colonic Neoplasm

## One-Sentence Summary

> Oteracil has no independent antineoplastic indication — it exists solely as a fixed component of the S-1 fluoropyrimidine combination (tegafur + gimeracil + oteracil), where it protects the gastrointestinal tract from 5-FU toxicity.
> The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
> supported by **8 clinical trials** and **20 publications** — though this evidence largely confirms the S-1 combination's already-established role in colorectal cancer rather than a novel repurposing signal for oteracil itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No standalone indication — Oteracil is not an independently marketed API; it is used only as a fixed component of the S-1 combination, and no German license/indication text is available in this evidence pack |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for oteracil is not available (Data Gap). Based on known information, oteracil is part of the S-1 combination (tegafur + gimeracil + oteracil). Within this combination, oteracil potassium has no independent antitumour activity — its role is to inhibit intestinal orotate phosphoribosyltransferase (OPRT), which reduces premature activation of 5-FU (derived from tegafur) in the gut. This lowers gastrointestinal toxicity and allows higher effective systemic doses of 5-FU to reach tumour tissue.

Colonic neoplasm and gastric cancer (S-1's core indication) are both gastrointestinal malignancies that share the same fluoropyrimidine-sensitive pathway (thymidylate synthase inhibition). S-1 has already been approved in Japan and across Asia for colorectal cancer (adjuvant stage III colon/rectal cancer and metastatic disease), making the mechanistic extrapolation to colonic neoplasm biologically coherent.

**Important caveat:** the clinical trial and literature evidence assembled here almost entirely evaluates the *S-1 combination as a whole*, not oteracil in isolation. As explicitly noted in the underlying evidence, this is best understood as **confirmation of an already-established combination product's indication**, not a novel drug-repurposing discovery. This distinction matters for how the "Go/Hold" decision should be interpreted — the pharmacology is sound, but the regulatory/commercial pathway concerns the S-1 product, not oteracil as a standalone entity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+Leucovorin vs S-1 (TS-1) as adjuvant treatment for stage III colon cancer, with gene-expression-based predictive factor analysis |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO study: S-1 vs capecitabine as first-line treatment for metastatic colorectal cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (oxaliplatin+S-1) vs XELOX as adjuvant chemotherapy for stage III colorectal cancer |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 for metastatic colorectal cancer after failure of standard chemotherapy |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) in untreated metastatic colorectal cancer |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after failure of irinotecan/oxaliplatin regimens |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + tegafur/gimeracil/oteracil as third-line treatment for advanced metastatic CRC |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1/capecitabine + oxaliplatin effects on coronary microvascular blood flow in metastatic GI adenocarcinoma (safety-focused, not efficacy) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: S-1+oxaliplatin (SOX) vs UFT/LV as adjuvant chemotherapy in high-risk stage III colon cancer |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Ann Oncol | ACTS-RC (JFMC35-C1): S-1 vs UFT as adjuvant chemotherapy for stage II/III rectal cancer |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Ann Oncol | ACTS-CC trial: S-1 noninferior to UFT/LV as adjuvant chemotherapy for stage III colon cancer |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | RCT sub-study (safety) | Br J Cancer | Planned safety analysis of ACTS-CC phase III trial comparing UFT/LV and S-1 |
| [26976971](https://pubmed.ncbi.nlm.nih.gov/26976971/) | 2016 | RCT biomarker sub-study | Anticancer Res | Genome-wide DNA copy-number analysis within the ACTS-CC phase III trial |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | Phase II/III efficacy study | Int J Clin Oncol | KSCC1303: 3-year DFS analysis of S-1+oxaliplatin (C-SOX) adjuvant therapy for stage III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus guidelines for management of metastatic colorectal cancer, incorporating S-1-based regimens |
| [17496461](https://pubmed.ncbi.nlm.nih.gov/17496461/) | 2007 | Review | Gan To Kagaku Ryoho | Current state and issues of adjuvant chemotherapy for colorectal cancer in Japan |
| [10897209](https://pubmed.ncbi.nlm.nih.gov/10897209/) | 2000 | Review | Gan To Kagaku Ryoho | Conceptual basis for S-1's biochemical modulation of 5-FU (self-rescuing concept, includes oteracil's role) |
| [20500514](https://pubmed.ncbi.nlm.nih.gov/20500514/) | 2010 | Preclinical | Cancer Sci | Anti-lymph-node-metastasis efficacy of oral S-1 vs UFT/LV in a colon cancer xenograft model |

---

## Germany Market Information

Oteracil currently holds **no marketing authorization in Germany** — `taiwan_regulatory.market_status` is recorded as "未上市 (Not marketed)" with **0 total licenses**. No license records, product names, or approved-indication text are available in this evidence pack. Note that oteracil is not intended to be marketed as a standalone product; it is only clinically relevant as a fixed component within combination products (e.g., S-1-type formulations), for which no separate license data was provided here.

---

## Cytotoxicity

Oteracil is evaluated here as a required cytotoxic-chemotherapy adjunct because it is a fixed, non-separable component of the fluoropyrimidine combination S-1, used exclusively in antineoplastic regimens for gastrointestinal cancers.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine combination adjunct (component of S-1; oteracil itself is not independently cytotoxic but modulates 5-FU activation) |
| Myelosuppression Risk | Moderate — S-1-based regimens are commonly associated with neutropenia and thrombocytopenia in reported case series and trial safety analyses |
| Emetogenicity Classification | Low to Moderate (consistent with oral fluoropyrimidine class) |
| Monitoring Items | CBC with differential, liver and renal function, serum triglycerides (hypertriglyceridemia reported, PMID 32936722), skin/mucosal surveillance (severe cutaneous reactions reported, PMID 28414195) |
| Handling Protection | Must follow cytotoxic drug handling regulations, as oteracil is only used as part of cytotoxic chemotherapy regimens |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available for oteracil in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 RCTs (ACTS-CC, ACTS-RC, SALTO) demonstrating efficacy of the S-1 combination in colorectal cancer. However, this evidence pertains to the S-1 combination as a whole rather than oteracil in isolation, and critical safety/regulatory data specific to oteracil (German label warnings, MOA) remain unresolved (Blocking Data Gap DG001).

**To proceed, the following is needed:**
- German (BfArM) package insert warnings and contraindications for oteracil/S-1-containing products (currently a Blocking data gap)
- Independent MOA documentation for oteracil (High-severity data gap, from DrugBank)
- Clarification of whether the repurposing target is oteracil as an API or the S-1 combination product, since oteracil has no standalone marketing pathway
- Confirmation of drug-drug interaction profile, given DDI query currently returns no data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

