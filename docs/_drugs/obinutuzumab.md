---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the drug-repurposing evaluation report template to convert this Evidence Pack into the required report.

**Note on indication selection:** `predicted_indications[0]` and `[1]` (CLL/SLL variants, TxGNN score 99.21%) both carry **zero** clinical-trial or literature records in this dataset (L5/Hold), and the evidence pack itself flags this as a likely data-collection gap rather than a true absence of evidence (Obinutuzumab/Gazyva is publicly known to be approved for CLL elsewhere). Since those two entries cannot be substantiated from the data provided, this report is built around **predicted_indications[2] — Follicular Lymphoma**, the only candidate in this pack with real trial/literature support (L1, "Proceed with Guardrails"). The CLL/SLL anomaly is flagged separately below rather than silently dropped.

---

# Obinutuzumab: From Anti-CD20 Antibody Therapy to Follicular Lymphoma

## One-Sentence Summary

Obinutuzumab is a glycoengineered type II anti-CD20 monoclonal antibody; this evidence pack contains no confirmed local original-indication or market record for the drug (currently **not marketed** in this jurisdiction). The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **50 clinical trials** and **20 publications** identified during evidence collection — of which the 10 most relevant of each are summarized below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication on file; the drug is not currently marketed in this jurisdiction |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Data-quality note:** The same evidence pack also ranks "CLL/SLL with IGHV somatic hypermutation" (score 99.21%) and "pregerminal-center CLL/SLL" (score 99.21%) as the top two TxGNN predictions, but both have 0 matched clinical trials and 0 literature records (Evidence Level L5, Decision: Hold). The evidence pack's own rationale text explicitly notes this conflicts with the publicly known fact that Obinutuzumab is approved for CLL in multiple countries, and recommends verifying the data source before making any decision on those two indications. They are not further analyzed in this report and should be re-queried rather than treated as true negatives.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not present in the structured `original_moa` field of this evidence pack (marked as a data gap). However, the supporting literature captured in the evidence base consistently describes Obinutuzumab as a recombinant, humanized, glycoengineered type II anti-CD20 monoclonal antibody (e.g., PMID 28324270, PMID 31360086) that enhances antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and direct B-cell killing more potently than first-generation anti-CD20 antibodies such as rituximab.

Follicular lymphoma is a germinal-center B-cell-derived indolent lymphoma whose malignant cells characteristically express CD20 on their surface — the same target class that anti-CD20 antibodies (rituximab, obinutuzumab, ofatumumab) already treat in other B-cell malignancies. This gives the TxGNN prediction strong biological plausibility even before considering trial data: it links a known drug target (CD20) to a disease defined by that target's expression.

Critically, this is not a purely computational prediction — it is corroborated by an unusually large and mature body of direct clinical evidence, including the pivotal Phase 3 GALLIUM trial (PMID 28976863, 29856692, 37404773), which directly compared obinutuzumab-based immunochemotherapy against rituximab-based immunochemotherapy in previously untreated follicular lymphoma and demonstrated superior progression-free survival. This makes follicular lymphoma the strongest-supported repurposing candidate in this evidence pack, in contrast to the two CLL/SLL predictions above, which currently have no matched evidence in this dataset.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | EPCORE™FL-2: epcoritamab + lenalidomide/rituximab vs. chemoimmunotherapy in previously untreated FL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | GAZEBO trial: radiotherapy alone vs. radiotherapy + obinutuzumab in early-stage FL |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Recruiting | 780 | Zanubrutinib + anti-CD20 antibody vs. lenalidomide + rituximab in relapsed/refractory FL/MZL |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | Zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL (ROSEWOOD) |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Phase 2 | Completed | 96 | Obinutuzumab + lenalidomide in previously untreated FL (Grade 1-3a, Stage II-IV) |
| [NCT01582776](https://clinicaltrials.gov/study/NCT01582776) | Phase 1b/2 | Completed | 317 | Obinutuzumab + lenalidomide across untreated and relapsed/refractory FL and other B-cell lymphomas |
| [NCT04450173](https://clinicaltrials.gov/study/NCT04450173) | Phase 2 | Active, not recruiting | 40 | Obinutuzumab + ibrutinib + venetoclax in previously untreated FL |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Completed | 114 | Obinutuzumab short-duration infusion safety in previously untreated advanced FL |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A (real-world) | Recruiting | 332 | Real-world efficacy/safety of obinutuzumab-based therapy in previously untreated FL |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | Active, not recruiting | 33 | Obinutuzumab + CC-99282 in previously untreated, high tumor-burden FL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | The New England Journal of Medicine | Pivotal GALLIUM trial: obinutuzumab- vs. rituximab-based chemotherapy in previously untreated advanced-stage FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM sub-analysis: influence of chemotherapy backbone (CHOP/CVP/bendamustine) on efficacy and safety |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM final analysis: durable PFS benefit of obinutuzumab vs. rituximab immunochemotherapy in FL/MZL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinib + obinutuzumab vs. obinutuzumab monotherapy in relapsed/refractory FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN study: obinutuzumab + lenalidomide in relapsed/refractory follicular B-cell lymphoma |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | RCT | Haematologica | Polatuzumab vedotin + bendamustine/rituximab or obinutuzumab in relapsed/refractory FL (Phase Ib/II) |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer: Targets and Therapy | Overview of obinutuzumab activity alone and in combination in FL |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Review of obinutuzumab in rituximab-refractory/relapsed FL, incl. GADOLIN study |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Comprehensive review of staging, prognosis, and treatment options in FL |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Frontiers in Pharmacology | Rapid review of efficacy, safety, and cost-effectiveness of obinutuzumab in FL |

---

## Germany Market Information

No authorization records are available — `taiwan_regulatory.market_status` is "未上市" (Not Marketed) with 0 total licenses on file. Obinutuzumab currently has no registered product entry in this jurisdiction's regulatory database.

---

## Cytotoxicity

Obinutuzumab is an antineoplastic agent (CD20-targeted monoclonal antibody used in B-cell malignancies including follicular lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody) — not conventional cytotoxic chemotherapy |
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
The predicted association between Obinutuzumab and follicular lymphoma is supported by a strong CD20-targeted mechanistic rationale and a mature evidence base including a pivotal Phase 3 RCT (GALLIUM) plus multiple completed and ongoing Phase 2/3 trials — meeting the L1 evidence threshold. However, the drug is currently unregistered/not marketed in this jurisdiction, and core safety, MOA, and regulatory data remain unconfirmed, so progression should proceed only with additional safeguards.

**To proceed, the following is needed:**
- Confirm mechanism-of-action and DrugBank category data (currently marked as a data gap, DG002)
- Obtain and parse the TFDA/local package insert for warnings, contraindications, and DDI data (currently marked as a blocking data gap, DG001)
- Verify local market registration pathway status, since 0 authorizations are currently on file
- Re-query the data source for the two CLL/SLL predictions (ranks 1–2) to resolve the apparent evidence-collection gap flagged above before any decision is made on those indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

