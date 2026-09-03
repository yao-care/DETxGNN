---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From NSAID Anti-Inflammatory Therapy to Juvenile Idiopathic Arthritis (RF-Positive Polyarticular)

## One-Sentence Summary

Meloxicam is a COX-2 preferential NSAID conventionally used for osteoarthritis, rheumatoid arthritis, and related inflammatory joint conditions. Of the 10 candidate indications predicted by TxGNN, only **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis** reaches meaningful evidence support (1 Phase 4 safety registry publication, **L3**), while the top-ranked prediction by raw score — acromesomelic dysplasia, Hunter-Thompson type (99.92%) — and most others are rare genetic/skeletal syndromes with no mechanistic or clinical linkage to NSAID pharmacology. Overall progression is currently **blocked** by a missing TFDA label safety dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Taiwan license data (0 licenses on file); by general pharmacology, meloxicam is an NSAID indicated for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis |
| Most Evidence-Supported Predicted Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| Top TxGNN Score (this indication) | 99.44% (rank 6423) |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (indication-level model recommends "Proceed with Guardrails," but overall workflow is gated by a Blocking data gap) |

---

## Predicted Indications Overview (All 10 Ranked Candidates)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---|---|---|---|---|---|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.92% | L5 | S0 | Hold |
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.92% | L5 | S0 | Hold |
| 3 | Myosclerosis | 99.90% | L5 | S0 | Hold |
| 4 | Brachyolmia | 99.89% | L5 | S0 | Hold |
| 5 | Pseudoachondroplasia | 99.81% | L5 | S0 | Hold |
| 6 | Spondyloarthropathy, susceptibility to | 99.52% | L4 | S1 | Research Question |
| 7 | Rheumatoid nodulosis | 99.51% | L4 | S1 | Research Question |
| **8** | **RF-positive polyarticular JIA** | **99.44%** | **L3** | **S2** | **Proceed with Guardrails** |
| 9 | WHIM syndrome | 99.38% | L5 | S0 | Hold |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.36% | L5 | S0 | Hold |

Six of ten candidates are rare monogenic skeletal or immune-deficiency syndromes with no plausible pathophysiological link to COX inhibition — these likely reflect knowledge-graph embedding noise rather than genuine repurposing signals and are correctly held at L5/Hold.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (original_moa: Data Gap). Based on general pharmacological knowledge, meloxicam is a **COX-2 preferential NSAID** that inhibits prostaglandin synthesis to reduce inflammation, pain, and swelling — a mechanism already central to its established use in osteoarthritis and rheumatoid arthritis.

Juvenile idiopathic arthritis (JIA), including the RF-positive polyarticular subtype, shares the same underlying inflammatory joint pathology as adult rheumatoid arthritis. NSAIDs (including meloxicam) are already a recognized first-line symptomatic therapy across JIA subtypes in clinical practice, so this "novel indication" largely represents a **class-effect extension** into a pediatric population rather than a mechanistically novel discovery. The supporting literature (a Phase 4 safety registry) evaluated nonselective NSAIDs and celecoxib as a class in JIA patients, not meloxicam specifically — so the evidence is indicative rather than drug-specific.

Two additional candidates — spondyloarthropathy (susceptibility) and rheumatoid nodulosis — sit at L4 for a similar reason: NSAIDs are standard symptomatic treatment for spondyloarthropathies (e.g., ankylosing spondylitis) and RA-related nodular disease, but the KG entries here represent genetic *susceptibility* or *subtype* labels rather than direct treatment indications, and no disease-specific trial or literature evidence has been captured yet.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid factor-positive polyarticular JIA (or any of the other 9 candidates).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Cohort (Phase 4 Registry) | Pediatric Rheumatology Online Journal | Long-term safety and developmental outcomes of celecoxib and nonselective NSAIDs (nsNSAIDs, class including meloxicam) in JIA patients treated in routine clinical practice |

No literature is currently available for the remaining 9 predicted indications, including the two L4 "Research Question" candidates.

---

## Taiwan Market Information

Meloxicam currently holds **0 authorizations** on file (market status: 未上市 / not marketed). No license records are available to summarize approved indications or dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack and could not be independently verified.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The most evidence-supported candidate (RF-positive polyarticular JIA, L3) has a plausible mechanistic basis and receives an indication-level "Proceed with Guardrails" recommendation, but the evidence is class-level (nsNSAIDs) rather than meloxicam-specific, and a **Blocking** data gap (missing TFDA label warnings/contraindications, DG001) prevents entry into the S1 safety preliminary assessment for any candidate. The remaining 9 predictions lack clinical, mechanistic, or literature support and should stay on Hold.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA label PDF for meloxicam to obtain warnings/contraindications (DG001, Blocking — required before S1 safety evaluation)
- Query DrugBank API to confirm mechanism of action (DG002, High)
- Seek meloxicam-specific (not just NSAID-class) clinical data for RF-positive polyarticular JIA
- Confirm whether "未上市/0 licenses" reflects true unregistered status in Taiwan or a data collection gap
- Run a targeted literature search on the two L4 "Research Question" candidates (spondyloarthropathy susceptibility, rheumatoid nodulosis) before advancing their decision stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

