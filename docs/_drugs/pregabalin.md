---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pregabalin: From Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is a calcium-channel modulator widely used to treat neuropathic pain, epilepsy, and related conditions. The TxGNN model predicts it may be effective for **Tendinitis**, but currently **0 clinical trials** and **6 publications** support this specific link, and none of the existing literature directly studies tendinitis as a treatment target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (pregabalin is not currently marketed in this jurisdiction; 0 authorizations on file) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation for pregabalin was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale supplied alongside the prediction, pregabalin binds the α2δ subunit of voltage-dependent calcium channels, reducing release of excitatory neurotransmitters — a mechanism well suited to neuropathic pain and perioperative analgesia.

Tendinitis, however, is primarily a local inflammatory/mechanical injury pain condition rather than a neuropathic pain state, so the mechanistic overlap with pregabalin's calcium-channel action is weak. The supporting literature largely involves pregabalin used for **perioperative pain control after orthopedic surgery** (e.g., arthroscopic rotator cuff repair) or for **unrelated peripheral neuropathies** (piriformis syndrome, chemotherapy-induced neuropathy), rather than direct evidence of efficacy against tendinitis pathology itself. This is consistent with the model's own scoring, which places this candidate at evidence level L4 (mechanism/preclinical-level support only) with a "Hold" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT | J Orthop Sci | Retrospective cohort on pregabalin's analgesic efficacy and opioid-sparing effect after arthroscopic rotator cuff repair — perioperative pain control, not tendinitis treatment per se |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin produced pain scores comparable to interscalene brachial plexus block after rotator cuff repair |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Review/Commentary | Arthroscopy | Editorial on piriformis syndrome diagnosis and sciatic neurolysis; tendon involvement discussed but no pregabalin efficacy data |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case Report | Praxis | Describes fluoroquinolone-associated tendinopathy/disability; pregabalin not directly evaluated |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case Report | Pain Pract | Posterior femoral cutaneous nerve impingement from running-related tendonitis; nerve pain context, not a tendinitis efficacy study |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | Plant extract (not pregabalin) attenuates vincristine-induced peripheral neuropathy in rats |

## Germany Market Information

Pregabalin is currently **not marketed** in this jurisdiction; no authorization records are available (0 total licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. *(Note: TFDA label warnings and contraindications for pregabalin are a Blocking-severity data gap, DG001 — this must be resolved before any safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between pregabalin's calcium-channel modulation and tendinitis (a local inflammatory/mechanical condition) is weak, and no clinical trials or literature directly test pregabalin for tendinitis — existing evidence only covers perioperative pain control or unrelated neuropathies.

**To proceed, the following is needed:**
- TFDA/BfArM label warnings and contraindications (DG001, Blocking)
- Formal DrugBank-sourced mechanism-of-action documentation (DG002, High)
- A tendinitis-specific preclinical or pilot clinical study to establish direct biological plausibility before any trial design

**Additional note:** Among the six candidates in this evidence pack, **migraine disorder** (rank 5, TxGNN score 99.47%) has meaningfully stronger support — an L2 evidence level with multiple pediatric RCTs, a Cochrane systematic review, and preclinical imaging data showing pregabalin inhibits cortical spreading depression (the core pathology of migraine aura). A withdrawn Phase 3 adult trial (NCT00447369) indicates prior development interest but no completed confirmatory data. This candidate may warrant prioritization as a "Research Question" track ahead of tendinitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

