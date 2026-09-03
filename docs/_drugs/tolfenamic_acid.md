---
layout: default
title: Tolfenamic Acid
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Tolfenamic Acid
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

Using no specialized skill — this is a direct templated report-generation task; proceeding straight to the deliverable.

# Tolfenamic Acid: From Anti-Inflammatory Analgesic to Headache Disorder

## One-Sentence Summary

> Tolfenamic acid is a fenamate-class NSAID with a long clinical history as an anti-inflammatory analgesic (detailed original-indication data is not present in this evidence pack).
> The TxGNN model predicts it may be effective for **Headache Disorder** (migraine),
> with **0 registered clinical trials** but **20 supporting publications** — including at least 9 randomized controlled trials conducted between 1979 and 2002.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug not currently marketed; historically classified as an anthranilic acid/fenamate NSAID used for pain, inflammation and rheumatic disease) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action (MOA) record is available for tolfenamic acid in this evidence pack (Data Gap DG002). However, the supporting literature is informative: multiple publications describe tolfenamic acid as a fenamate-class NSAID that is "a potent inhibitor of prostaglandin biosynthesis" (PMID 6984358) and, unusually among NSAIDs, also suppresses leukotriene synthesis, which may reduce upper-GI side effects relative to pure COX inhibitors (PMID 7816786).

Because no original-indication text is on file, the exact starting point for this repurposing candidate cannot be stated precisely. What the literature does show is that tolfenamic acid already has an extensive, decades-long track record as an anti-inflammatory analgesic (rheumatic disease, general pain) — so its application to headache disorder is less a "novel leap" and more a well-documented, longstanding clinical use pattern that the TxGNN model has independently recovered from the underlying knowledge graph.

Mechanistically, prostaglandins are implicated in migraine pathophysiology — sensitizing nociceptors, promoting vasodilation, and modulating platelet-serotonin release (PMID 7816790). COX inhibition by tolfenamic acid directly addresses this pathway, which is consistent with the drug's high TxGNN prediction score and with the large body of comparative RCT evidence (vs. ergotamine, sumatriptan, propranolol, paracetamol, and pizotifen) summarized below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT (double-blind crossover) | Lancet | Tolfenamic acid as effective as ergotamine in acute migraine, with fewer side effects (less nausea) |
| [6984358](https://pubmed.ncbi.nlm.nih.gov/6984358/) | 1982 | RCT (double-blind, randomized order) | Cephalalgia | Tolfenamic acid + caffeine/metoclopramide/pyridoxine combinations tested across 60 acute migraine attacks |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | RCT (double-blind crossover vs placebo) | Acta Neurol Scand | Significant prophylactic benefit vs placebo: fewer attacks, shorter duration, less vomiting |
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT (controlled) | Cephalalgia | Compared tolfenamic acid, caffeine, metoclopramide and combinations for acute migraine |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT (double-blind crossover vs propranolol/placebo) | Acta Neurol Scand | Both tolfenamic acid and propranolol significantly reduced attack frequency and duration vs placebo |
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT (double-blind crossover vs paracetamol) | Acta Neurol Scand | Dose-ranging comparison (200/400 mg vs paracetamol 500/1000 mg) in common migraine |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT (randomized double-blind crossover vs propranolol) | Acta Neurol Scand | 76-patient trial; both drugs significantly effective in migraine prophylaxis |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT (double-blind, randomized, parallel-group vs sumatriptan) | Headache | Comparable efficacy to oral sumatriptan in acute migraine (77% response rate) |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT (prospective, randomized, double-blind, parallel-group vs pizotifen) | Medicina (Kaunas) | 192-patient migraine prophylaxis trial comparing tolfenamic acid 300 mg vs pizotifen |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacology & Toxicology | Reviews prostaglandin-mediated mechanism underlying tolfenamic acid's antimigraine effect |

---

## Germany Market Information

Tolfenamic acid is currently **not marketed** in Germany, and no BfArM authorization records are present in this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and DDI data are flagged as data gaps in this evidence pack — DG001, "TFDA/BfArM label warnings/contraindications," is marked as a **Blocking** severity gap.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Although no clinical trials are currently registered for headache disorder, the literature base is unusually strong for an older drug — at least 9 randomized controlled trials (1979–2002) consistently demonstrate efficacy in acute and prophylactic migraine, including head-to-head comparisons against ergotamine, sumatriptan, propranolol, and pizotifen. This meets L1 evidence criteria, but the drug's current unmarketed status in Germany and missing safety-label data mean guardrails are required before any regulatory or clinical action.

**To proceed, the following is needed:**
- Package insert / BfArM label data on warnings and contraindications (Blocking gap, DG001)
- Structured DrugBank MOA record (High priority gap, DG002)
- Confirmation of why the drug is currently unmarketed in Germany, and what registration pathway would be required to reintroduce it for a headache indication
- Updated drug-drug interaction (DDI) data, as none is currently on file
- A contemporary systematic review of the 1979–2002 RCT literature to formally grade study quality (risk of bias, sample sizes) before treating this as decision-grade evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

