---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Unspecified Oncology Indication to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class antineoplastic agent; the specific original indication on file is not documented in this evidence pack (data gap), though paclitaxel is a globally established cytotoxic chemotherapy agent for solid tumors.
The TxGNN model's top prediction identifies **Female Breast Carcinoma** as the leading candidate indication, with **83 clinical trials** and **20 publications** captured as supporting evidence.
Importantly, the underlying mechanistic rationale explicitly notes this reflects paclitaxel's **existing standard-of-care mechanism in breast cancer chemotherapy, not a novel repurposing hypothesis** — the prediction is therefore best read as evidence-base confirmation rather than discovery of a new therapeutic use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap — see DG001/DG002 below) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.99% (rank 93 of predicted disease space) |
| Evidence Level | L1 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for paclitaxel is not available from this evidence pack (flagged as data gap DG002, High severity). Based on general pharmacological classification, paclitaxel is a taxane — a microtubule-stabilizing agent that blocks mitotic spindle disassembly and induces apoptosis in rapidly dividing cells. This mechanism is the pharmacological basis for its established role across multiple solid-tumor chemotherapy regimens.

For the top-ranked candidate, the repurposing rationale states directly: *"Paclitaxel stabilizes microtubules and blocks mitotic spindle disassembly, inducing apoptosis in rapidly dividing breast cancer cells; this is an existing standard chemotherapy mechanism in breast cancer, not a novel repurposing hypothesis."* In other words, the mechanistic link between paclitaxel and breast carcinoma is well-established clinical knowledge rather than an emergent, TxGNN-discovered association — the model has effectively recovered a known, high-confidence indication.

This has an important implication for interpretation: the very large and mature clinical trial/literature base (83 trials, 20 publications, including multiple completed Phase 3 RCTs) reflects decades of accumulated breast cancer chemotherapy research rather than early-stage exploratory signal. The evidence strength (L1) is therefore driven by depth of existing standard-of-care literature, and the primary open question for this candidate is not "does it work" but rather regulatory/administrative: confirming the drug's actual approved indication history and current label status, both of which are currently data gaps.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00016406](https://clinicaltrials.gov/study/NCT00016406) | Phase 3 | Completed | 399 | AC ± filgrastim followed by weekly paclitaxel as neoadjuvant therapy for inflammatory/locally advanced breast cancer; direct supportive evidence (Grade A) |
| [NCT00014222](https://clinicaltrials.gov/study/NCT00014222) | Phase 3 | Completed | 2104 | Large adjuvant trial comparing EC+filgrastim+epoetin→paclitaxel vs AC→paclitaxel vs CEF in node-positive/high-risk breast cancer |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Neoadjuvant carboplatin+docetaxel or carboplatin+paclitaxel followed by AC in Stage I-III triple-negative breast cancer (Grade B) |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel+carboplatin+trastuzumab (Herceptin) as first-line therapy in HER2-overexpressing metastatic breast cancer (Grade B) |
| [NCT01973660](https://clinicaltrials.gov/study/NCT01973660) | Phase 2 | Completed | 151 | PAMELA study: PAM50 HER2-enriched phenotype predicts response to neoadjuvant lapatinib+trastuzumab in HER2+ breast cancer |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly 1-hour paclitaxel plus trastuzumab in metastatic breast cancer |
| [NCT01307891](https://clinicaltrials.gov/study/NCT01307891) | Phase 2 | Completed | 64 | Abraxane (nab-paclitaxel) ± tigatuzumab in metastatic triple-negative breast cancer |
| [NCT00005649](https://clinicaltrials.gov/study/NCT00005649) | Phase 2 | Completed | N/A | Capecitabine + standard paclitaxel as first- or second-line therapy in metastatic breast carcinoma |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Nab-paclitaxel + carboplatin vs nab-paclitaxel + capecitabine in advanced triple-negative breast cancer |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Paclitaxel-trastuzumab adjuvant therapy pilot in early-stage HER2-overexpressing breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Clinical trial (Tier 1) | Cancer | Phase II trial of doxorubicin + paclitaxel in advanced/metastatic breast carcinoma; importance of prior adjuvant anthracycline exposure |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review/Clinical (Tier 1) | Drug and Therapeutics Bulletin | Foundational review of paclitaxel/docetaxel licensing extension to breast and ovarian cancer |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review (Tier 1) | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects, and resistance mechanisms, in breast cancer |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Pending | Chemical Biology & Drug Design | Paclitaxel combination therapeutic potential and in vivo biomarkers in breast carcinoma |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Pending | J Immunother Cancer | Paclitaxel's effect on tumor-associated macrophages enhancing PD-1 blockade efficacy in TNBC |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Pending | BioMed Research International | Real-world efficacy of epirubicin/cyclophosphamide + weekly paclitaxel + trastuzumab in HER2+ breast carcinoma |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Pending | Nature Communications | TEKT4 germline variation enrichment associated with breast cancer resistance to paclitaxel |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Pending | Molecular Pharmacology | Reversal of stathmin-mediated resistance to paclitaxel and vinblastine in breast carcinoma cells |
| [14508823](https://pubmed.ncbi.nlm.nih.gov/14508823/) | 2003 | Pending | Cancer | Combined trastuzumab + paclitaxel more effectively inhibits ErbB-2-mediated angiogenesis via Akt inhibition |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | Pending | Cancer | GONO randomized trial: concomitant vs sequential epirubicin + paclitaxel as first-line therapy in metastatic breast carcinoma |

---

## Germany Market Information

No marketing authorizations for paclitaxel were found in the regulatory registry underlying this evidence pack as of the data cutoff (2026-09-03). Market status is recorded as **Not Marketed**, with **0 total licenses** on file. No product name, dosage form, or approved-indication text is currently available for this jurisdiction.

---

## Cytotoxicity

Paclitaxel is classified as antineoplastic based on its established taxane/cytotoxic chemotherapy drug class and its use across multiple oncology indications reflected throughout the predicted-indication evidence (breast, ovarian, and other carcinomas).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia (including febrile neutropenia) is a well-recognized dose-limiting toxicity of paclitaxel-based regimens |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (absolute neutrophil count), hepatic function, hypersensitivity reaction monitoring during infusion, peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations (PPE, closed-system transfer devices) |

Specific quantitative toxicity data (e.g., DrugBank-sourced myelosuppression grading) was not available in this evidence pack — please refer to the package insert for detailed dosing and toxicity monitoring guidance.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (query status: not found; 0 interactions returned).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The clinical/literature evidence base for paclitaxel in female breast carcinoma is extensive and mature (L1, multiple completed Phase 3 RCTs), but this largely confirms an already well-established chemotherapy use rather than validating a genuinely novel repurposing hypothesis. More critically, a **Blocking** data gap (DG001 — TFDA/regulatory label, warnings, and contraindications) currently prevents completion of the initial safety review (S1), and the drug shows no current marketing authorization in this jurisdiction (0 licenses, Not Marketed).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official product label/PI (warnings, contraindications) from the relevant regulatory source before advancing past S1 safety screening
- Resolve DG002 (High): retrieve confirmed mechanism-of-action data via DrugBank API to properly document the mechanistic linkage
- Clarify paclitaxel's actual historical/approved original indication(s), since `original_indications` is empty in this pack
- If pursuing this indication commercially, confirm the regulatory pathway given current "Not Marketed" status (0 authorizations on file)
- Reassess candidate novelty: given the rationale explicitly notes this is standard-of-care rather than a new hypothesis, confirm whether this candidate belongs in a genuine repurposing pipeline versus an evidence-documentation exercise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

