---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the given Evidence Pack, I've noted this is a **multi-candidate** pack (`TW-DB08899-multi`) — of the 7 TxGNN-predicted indications, only one (rank 5, "benign reproductive system neoplasm") carries any real trial/literature evidence that represents a genuinely *novel* repurposing signal; rank 6 is flagged inside the pack itself as a re-detection of Enzalutamide's already-known indication (prostate cancer) rather than a repurposing candidate, and ranks 1–4/7 have zero supporting evidence. I've built the report around the one defensible candidate (rank 5) per the template, and added a portfolio table so the other 6 predictions aren't silently dropped.

---

# Enzalutamide: From Prostate Cancer to Benign Reproductive System Neoplasm

## One-Sentence Summary

> Enzalutamide is a next-generation androgen receptor (AR) antagonist whose approved use — referenced throughout this evidence pack's own model rationale — is (metastatic/castration-resistant) **prostate cancer**.
> Of the seven new indications the TxGNN model surfaced for this drug, the only one supported by actual trial and literature evidence is **Benign Reproductive System Neoplasm**,
> with **1 clinical trial** and **5 publications** identified — all of them, however, drawn from *malignant* prostate cancer populations rather than the benign-neoplasm population itself, so the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate Cancer *(derived from the model's own repurposing rationale, which repeatedly cites this as "Enzalutamide 之核准適應症"; formal Taiwan/BfArM licensed indication text is not available — see Data Gap DG001/DG002)* |
| Predicted New Indication | Benign Reproductive System Neoplasm |
| TxGNN Prediction Score | 99.53% (global model rank #5656) |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is marked as a data gap (`original_moa: [Data Gap]`), but the model's own rationale text consistently describes Enzalutamide as a **next-generation AR antagonist** that blocks AR nuclear translocation, DNA binding, and co-activator recruitment — the core mechanism by which it suppresses androgen-driven prostate cancer growth.

Prostate cancer (the drug's approved use) and "benign reproductive system neoplasm" both fall under AR-influenced growth pathways within the prostate/reproductive organ system. Several of the supporting publications (e.g., PMID 26926093, PMID 31266892) describe AR signaling and androgen biotransformation as active in **both benign and malignant** prostate tissue, which is the theoretical basis for extrapolating AR blockade to non-malignant proliferative lesions.

The key limitation is that **none of the identified trials or literature actually studied a benign-neoplasm population** — all clinical and mechanistic data come from malignant, metastatic, or castration-resistant prostate cancer cohorts. The link to "benign reproductive system neoplasm" is therefore a plausible mechanistic extrapolation, not a directly demonstrated effect, which is why the evidence level is capped at L4 (preclinical/mechanistic) rather than higher.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05701007](https://clinicaltrials.gov/study/NCT05701007) | N/A (observational) | Completed | 1,083 | Real-world epidemiology and treatment-pattern study of **metastatic (malignant)** prostate cancer patients in Finland; provides population-level background only — study population and design do not match a benign-neoplasm indication (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26926093](https://pubmed.ncbi.nlm.nih.gov/26926093/) | 2016 | Review | Pharmacological Research | Reviews androgen biotransformation and the AR/UGT regulatory network active in **both benign and malignant** prostate cells, supporting a shared hormonal growth-control pathway. |
| [35227084](https://pubmed.ncbi.nlm.nih.gov/35227084/) | 2022 | Translational/Biomarker Cohort | The Journal of Urology | Shows PSMA as a biomarker for residual disease after neoadjuvant androgen deprivation, demonstrating androgen blockade's measurable effect on prostate tissue histology. |
| [33771918](https://pubmed.ncbi.nlm.nih.gov/33771918/) | 2021 | Preclinical/Mechanistic | PNAS | ERβ activation inhibits nuclear EGFR translocation in the prostate, pointing to estrogen-receptor-linked regulation of prostate epithelial growth relevant to non-malignant proliferation. |
| [31266892](https://pubmed.ncbi.nlm.nih.gov/31266892/) | 2019 | Preclinical/Mechanistic | PNAS | PARP-2 inhibition disrupts FOXA1-driven AR signaling and suppresses prostate growth — mechanistic support for AR-pathway targeting of prostate tissue growth in general. |
| [30864728](https://pubmed.ncbi.nlm.nih.gov/30864728/) | 2019 | Preclinical/Mechanistic | Oncology Reports | PLCε knockdown sensitizes castration-resistant prostate cancer cells to enzalutamide by suppressing AR signaling — a resistance-reversal mechanism, not benign-tissue data. |

---

## Other Predicted Indications (Portfolio Overview)

Because this evidence pack contains 7 model-predicted indications for Enzalutamide, they are summarized here for completeness rather than silently discarded:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Note |
|------|---------|-------------|-----------------|----------|------|
| 1 | Prostate cancer/brain cancer susceptibility | 99.71% | L5 | Hold | Compound ontology term; no CNS mechanistic link, no evidence. Enzalutamide has limited blood-brain-barrier penetration and reported CNS AEs (seizure) — a safety signal, not an efficacy rationale. |
| 2 | Prostate leiomyoma | 99.57% | L5 | Hold | Rare benign stromal tumor; growth driver unclear and not established as AR-dependent. No evidence. |
| 3 | Brenner tumor | 99.55% | L5 | Hold | Predominantly an ovarian tumor; organ-system link to Enzalutamide's approved use is weak. No evidence. |
| 4 | Fibroma of prostate | 99.53% | L5 | Hold | Rare benign stromal tumor; no literature establishing AR-pathway involvement. No evidence. |
| **5** | **Benign reproductive system neoplasm** | **99.53%** | **L4** | **Hold (Research Question)** | **Headline candidate above — only entry with real, if indirect, supporting evidence.** |
| 6 | Male reproductive organ cancer | 99.51% | L2 | *Excluded* | This is essentially Enzalutamide's **already-approved indication** (prostate cancer) — 50 trials and 20 publications confirm this, but the pack itself flags it as a positive-control signal confirming model accuracy, **not a novel repurposing candidate**, and recommends excluding it from the candidate list. |
| 7 | Benign prostate phyllodes tumor | 99.48% | L5 | Hold | Extremely rare biphasic tumor, typically breast-origin; essentially no prostate-specific literature. No evidence. |

---

## Cytotoxicity

*(Included because the drug's approved indication is oncologic — prostate cancer — even though Enzalutamide is not a conventional chemotherapeutic.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — next-generation androgen receptor (AR) signaling inhibitor; not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data provided in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (no data provided) |
| Monitoring Items | Please refer to the package insert warnings and precautions. Note: the pack's own rationale (rank 1) flags a reported CNS safety signal (seizure) associated with Enzalutamide, suggesting neurological monitoring is relevant where applicable |
| Handling Protection | Please refer to the package insert warnings and precautions (no cytotoxic-handling data provided; oral targeted agent, not classic IV cytotoxic chemotherapy) |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this pack. Note that DG001 — TFDA/BfArM package-insert warnings and contraindications — is flagged as a **Blocking** severity gap: the pack itself states this data must be resolved before the candidate can enter the S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only novel, evidence-backed candidate in this pack (Benign Reproductive System Neoplasm, rank 5) is supported solely by indirect, mechanistic/preclinical evidence drawn from **malignant** prostate cancer populations (L4) — no trial or publication studies the benign-neoplasm population directly.
- The drug is currently unmarketed in the relevant regulatory jurisdiction (0 licenses), and a Blocking-severity data gap (TFDA/BfArM package-insert warnings and contraindications, DG001) prevents even a basic safety pre-screen.
- The remaining five low-scoring candidates (ranks 1–4, 7) have zero supporting trials or literature; rank 6 duplicates the drug's already-approved indication and should be excluded from the candidate list rather than pursued as "new."

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — resolves DG001 (Blocking)
- Confirmed mechanism-of-action documentation from DrugBank — resolves DG002
- A direct preclinical or translational study evaluating AR blockade in benign (non-malignant) reproductive-tract neoplasm tissue, to move rank 5 beyond mechanistic extrapolation
- Clarification of German/Taiwan regulatory and licensing status, given the drug is currently unmarketed with 0 authorizations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

