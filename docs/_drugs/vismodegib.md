---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Vismodegib is a first-in-class Hedgehog (Hh) pathway inhibitor originally developed for **basal cell carcinoma (BCC)**. The TxGNN model predicts it may also be effective for **medulloblastoma with extensive nodularity** (a SHH-activated pediatric brain tumour subtype), with a very high model confidence of **99.93%**. However, this evidence pack currently contains **0 clinical trials and 0 publications** specifically linked to this predicted indication — the model's own rationale flags this as a likely **data collection gap** rather than a true absence of evidence, since vismodegib has been studied in SHH-driven medulloblastoma in the real world.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal Cell Carcinoma (BCC) — confirmed via literature in this evidence pack (PMID 22653209, PMID 24756807); not captured in `taiwan_regulatory.licenses` because the drug is not marketed in Germany |
| Predicted New Indication | Medulloblastoma with Extensive Nodularity |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

`drug.original_moa` is marked as a data gap in DrugBank (DG002). However, literature within this evidence pack (PMID 22653209, *Nature Reviews Drug Discovery*; PMID 24756807) independently confirms the mechanism: vismodegib is an orally bioavailable small-molecule antagonist of **Smoothened (SMO)**, a key transmembrane component of the Hedgehog signalling pathway. By blocking SMO, it prevents downstream activation of GLI transcription factors, suppressing pathway-driven proliferation.

Basal cell carcinoma and SHH-activated medulloblastoma are mechanistically closely related: both are canonically driven by loss-of-function mutations in **PTCH1** or gain-of-function mutations in **SMO**, leading to constitutive Hedgehog pathway activation. In fact, PMID 24756807 explicitly states that "dysregulated Hh signalling results in uncontrolled proliferation in basal cell carcinoma and has also been found present in medulloblastoma," directly supporting the biological plausibility of this prediction even though it is attached to a different disease entry in this dataset (rank 9, "skin cancer").

Given this shared driver mutation biology, SMO inhibition is mechanistically a rational treatment strategy for the SHH-activated subtype of medulloblastoma. The absence of trial/literature records specifically indexed to "medulloblastoma with extensive nodularity" in this evidence pack is most plausibly a **data collection gap** — a hypothesis the TxGNN rationale itself raises — rather than a true absence of scientific interest, and should be manually verified against ClinicalTrials.gov and PubMed before any decision is finalized.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Note: This applies specifically to the "medulloblastoma with extensive nodularity" entry in this evidence pack. The evidence pack's own rationale flags this as a likely data gap given known real-world investigation of vismodegib in SHH-driven medulloblastoma.*

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Vismodegib is **not currently marketed in Germany** (0 authorizations on record; `market_status: 未上市`). No BfArM licenses or approved indication texts are available in this evidence pack.

---

## Cytotoxicity

Vismodegib is an antineoplastic agent (original indication: basal cell carcinoma; MOA: Hedgehog/SMO pathway inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / Smoothened [SMO] inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

*No toxicity/safety data is available in this evidence pack; the TFDA label (warnings/contraindications) is flagged as a Blocking data gap (DG001) preventing formal S1 safety assessment.*

---

## Safety Considerations

Please refer to the package insert for safety information.

*Key warnings, contraindications, and drug-drug interaction data are all recorded as data gaps in this evidence pack. DG001 (TFDA label warnings/contraindications) is classified as a **Blocking** severity gap — it must be resolved before this candidate can proceed to formal safety evaluation (S1).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is very high (99.93%) and the mechanistic rationale (shared PTCH1/SMO pathway biology between BCC and SHH-activated medulloblastoma) is scientifically sound, this evidence pack currently has **zero clinical trials and zero literature** directly supporting the "medulloblastoma with extensive nodularity" prediction, and a **Blocking** safety data gap (DG001) prevents any S1 assessment. Evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Manual search of ClinicalTrials.gov and PubMed for "vismodegib" + "SHH medulloblastoma" / "SHH-activated medulloblastoma" to close the suspected data collection gap
- TFDA/EU label PDF for warnings, contraindications, and dosing (remediation for DG001)
- DrugBank MOA data confirmation (remediation for DG002)
- Confirmation of vismodegib's actual German/EU regulatory status, since it is recorded as unmarketed with 0 authorizations here despite being an approved product (Erivedge®) elsewhere

**Note for reviewers:** the same evidence pack contains a separate, much better-evidenced entry — "skin cancer" (rank 9, 23 clinical trials incl. multiple completed Phase 2 BCC trials, 20 publications) — which appears to correspond to vismodegib's already-known original indication (BCC) rather than a novel repurposing candidate. This should be excluded from repurposing consideration but confirms the drug/evidence linkage in this dataset is functioning correctly for indications with real coverage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

