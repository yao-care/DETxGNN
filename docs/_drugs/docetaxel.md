---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Established Solid-Tumour Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

> Docetaxel is a taxane chemotherapeutic already used across multiple solid tumours (lung, gastric, prostate, bladder and breast cancer, per trial-level references in this dataset).
> The TxGNN model assigns its highest-ranked signal to **Female Breast Carcinoma** (score **99.90%**),
> supported by **50 clinical trials** and **20 publications** — however, this indication is already an established, approved use of docetaxel rather than a genuinely novel repurposing candidate (see caveat below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug is not currently marketed in Germany per this dataset; docetaxel is broadly established across solid-tumour chemotherapy, per NCT01814150) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (with important caveat — see below) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is flagged as a data gap in this evidence pack (DG002). Based on the mechanistic annotation provided alongside the top prediction, docetaxel is a **taxane** that stabilizes microtubules and blocks their depolymerization, arresting cells at the G2/M phase of mitosis and inducing apoptosis. Breast cancer cells, like other rapidly proliferating tumour cells, are highly dependent on microtubule dynamics for division, which is the pharmacological basis for taxane activity in this tumour type.

**Important caveat:** the evidence pack itself flags that female breast carcinoma is **not a true "old drug, new use" candidate**. Docetaxel is already a globally approved, guideline-standard chemotherapy for breast cancer (neoadjuvant, adjuvant, and metastatic settings), as confirmed by dozens of completed Phase 3 trials in this dataset (e.g., TAC/TCX, AC→docetaxel, TCHP regimens). The TxGNN model appears to have re-identified an already-confirmed indication rather than surfaced a genuinely novel signal. This does not invalidate the evidence quality (which is very high, L1), but it does mean the "repurposing" framing should be understood as **confirmatory validation of the model**, not a new clinical opportunity.

For genuine repurposing value from this candidate list, **Ewing sarcoma (rank 2, evidence level L2)** is a more meaningful signal: docetaxel is not a first-line approved therapy for Ewing sarcoma, yet the gemcitabine–docetaxel (GEMDOX) combination has accumulated Phase 2 trial and cohort-level evidence as a salvage regimen in relapsed/refractory disease, representing more legitimate off-label/expansion-of-use evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Weekly docetaxel vs. CMF in adjuvant treatment of high-risk breast cancer patients ≥65 years or anthracycline-ineligible |
| [NCT00003565](https://clinicaltrials.gov/study/NCT00003565) | Phase 2 | Completed | 109 | Population pharmacokinetics of docetaxel (Taxotere) across Caucasian and African-American solid tumour patients |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2,411 | Preoperative AC vs. AC followed by docetaxel (pre/postoperative) in operable breast cancer |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Phase 3 | Completed | 2,611 | Adjuvant AC followed by Taxotere ± Xeloda in high-risk breast cancer — overall survival endpoint |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | TC/AC→paclitaxel vs. chemo+trastuzumab in node-positive/high-risk HER2-low breast cancer |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC vs. TCX adjuvant chemotherapy in high-risk HER2-negative breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C→docetaxel vs. paclitaxel adjuvant therapy in node-positive breast cancer |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Neoadjuvant TCHP (docetaxel/carboplatin/trastuzumab/pertuzumab) ± estrogen deprivation in HR+/HER2+ breast cancer |
| [NCT03252431](https://clinicaltrials.gov/study/NCT03252431) | Phase 3 | Completed | 393 | F-627 vs. Neulasta supportive care in breast cancer patients receiving myelotoxic (docetaxel-based) chemotherapy |
| [NCT02748213](https://clinicaltrials.gov/study/NCT02748213) | Phase 2 | Completed | 225 | Trastuzumab + docetaxel ± capecitabine in HER2-overexpressing advanced/metastatic breast cancer |

*(50 registered trials in total; the 10 above represent the largest and most directly relevant completed studies.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | TC (docetaxel/cyclophosphamide) vs. anthracycline-taxane regimens in early breast cancer (ABC trials, NRG Oncology) |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Early review of paclitaxel and docetaxel in breast and ovarian cancer |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Review | The Oncologist | Clinical experience review of docetaxel and paclitaxel in breast cancer treatment |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Clinical study | Cancer | Capecitabine + docetaxel + epirubicin (TEX) as first-line therapy for advanced breast carcinoma |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Dose-finding study | Tumori | Docetaxel + gemcitabine dose-finding study in metastatic breast carcinoma |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase 2 (interim) | Breast Cancer (Tokyo) | CEF followed by docetaxel as preoperative chemotherapy for early-stage breast carcinoma |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Clinical study | Breast Cancer (Tokyo) | Docetaxel/cyclophosphamide/trastuzumab as neoadjuvant therapy for HER2-positive breast cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Weekly docetaxel + gemcitabine as first-line treatment for metastatic breast cancer |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Foundational preclinical/clinical review of docetaxel (Cortes & Pazdur) |

*(20 publications in total for this indication; the 10 above are prioritized by study type — RCT > cohort > review.)*

---

## Germany Market Information

Currently no marketing authorizations for docetaxel are recorded in this evidence pack (market status: **Not marketed**; total licenses: **0**). No product/authorization-level data is available to populate a market table.

---

## Cytotoxicity

Docetaxel is a taxane and a well-established antineoplastic/cytotoxic agent (mechanism confirmed via the repurposing rationale in this dataset, despite the DrugBank MOA field itself being a data gap — DG002).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (drug-specific toxicity/label data is a documented data gap — DG001) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function — standard monitoring practice for cytotoxic chemotherapy regimens |
| Handling Protection | Must follow standard cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack (documented as data gap DG001 — TFDA/German label warnings and contraindications pending retrieval).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for docetaxel in female breast carcinoma is exceptionally strong (L1, 50 trials, 20 publications, multiple completed Phase 3 RCTs), but this indication is already an approved, standard-of-care use — not a genuine repurposing opportunity. "Proceed with Guardrails" here should be interpreted as confirming the model's validity rather than initiating new regulatory or clinical development work for this specific disease pairing.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/German product label — warnings, contraindications) before any safety-relevant decision-making
- Resolve DG002 (confirm docetaxel MOA via DrugBank API) to properly document mechanistic rationale
- Reassess whether "female breast carcinoma" should be excluded from the repurposing pipeline as an already-approved indication, and prioritize evaluation of **rank 2 (Ewing sarcoma, L2)** and **rank 8 (rhabdomyosarcoma, L2)** instead, which show genuine off-label/expansion-of-use signal
- Manually verify disease-label mapping for rank 4 (small cell lung carcinoma) and rank 5 (primary pulmonary lymphoma), where the supplied trial/literature evidence appears to actually describe NSCLC/ALK-positive NSCLC rather than the labeled indications — likely a TxGNN ontology mismatch requiring correction before further use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

