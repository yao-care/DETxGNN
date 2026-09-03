---
layout: default
title: Ketorolac
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
---

# Ketorolac
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

# Ketorolac: From Acute Pain to Headache Disorder

## One-Sentence Summary

Ketorolac is a nonsteroidal anti-inflammatory drug (NSAID) originally used for short-term management of moderate to severe acute pain (e.g., postoperative pain).
The TxGNN model predicts it may be effective for **Headache Disorder** (primarily migraine and tension-type headache),
with **37 clinical trials** and **19 publications** currently supporting this direction — though the drug is not currently marketed in Germany.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute pain management (NSAID; short-term treatment of moderately severe pain) |
| Predicted New Indication | Headache Disorder (migraine / tension-type headache) |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on known information, ketorolac is a pyrrolizine-carboxylic-acid class NSAID that acts through non-selective inhibition of COX-1/COX-2, reducing prostaglandin synthesis. Its efficacy in acute pain has been well established for decades, and mechanistically this same anti-prostaglandin action may extend to headache disorders, since prostaglandin-mediated neurogenic inflammation and trigeminovascular activation are recognized contributors to migraine and tension-type headache pain.

Acute pain and headache disorder are pharmacologically related: both involve peripheral and central sensitization driven partly by prostaglandins, and NSAIDs are already a first-line class for both. This mechanistic overlap is likely why the TxGNN model connects ketorolac's original acute-pain profile to headache disorder with a very high score.

Real-world clinical practice already supports this link — parenteral ketorolac (IV/IM/intranasal) has been used off-label as a standard emergency-department treatment for acute migraine and tension-type headache for over 30 years, and is explicitly included as a comparator/standard therapy in the 2025 American Headache Society guideline update for parenteral migraine treatment in the ED. In this sense, the TxGNN prediction largely formalizes an already-established off-label clinical pattern rather than proposing a novel mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | IV valproate vs metoclopramide vs ketorolac for acute migraine |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine, including nausea/allodynia outcomes |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Intranasal vs IV ketorolac non-inferiority trial for pediatric migraine |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: intranasal ketamine vs standard therapy (ketorolac) for ED headache |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Metoclopramide/diphenhydramine vs ketorolac alone for tension-type headache |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac + metoclopramide combination for pediatric migraine in ED |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Randomized, placebo-controlled trial of intranasal ketorolac for acute migraine |
| [NCT01138150](https://clinicaltrials.gov/study/NCT01138150) | Phase 4 | Completed | 36 | Inflammatory marker changes during acute migraine attacks treated with ketorolac |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal ketorolac + oral adjuncts vs IV ketorolac for pediatric migraine |
| [NCT02664116](https://clinicaltrials.gov/study/NCT02664116) | Phase 4 | Unknown | 40 | IM ketorolac vs oral diclofenac potassium for severe migraine |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9484382](https://pubmed.ncbi.nlm.nih.gov/9484382/) | 1998 | RCT | Neurology | IM ketorolac 60mg significantly more effective than meperidine+promethazine or saline for tension-type headache over 6 hours |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Annals of Emergency Medicine | IM ketorolac compared with meperidine+hydroxyzine for acute migraine |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | Adding IV ketorolac to metoclopramide for pediatric migraine in the ED |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurological Sciences | Compared dexamethasone, metoclopramide, ketorolac, and chlorpromazine for migraine pain relief and recurrence prevention |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 AHS guideline update on parenteral migraine pharmacotherapy in the ED |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Review | Headache | AHS evidence assessment of migraine pharmacotherapies |
| [39674934](https://pubmed.ncbi.nlm.nih.gov/39674934/) | 2025 | Systematic Review/Meta-analysis | Annals of Emergency Medicine | Bayesian network meta-analysis of ED pharmacologic therapies for migraine |
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic Review/Meta-analysis | Academic Emergency Medicine | Efficacy of parenteral ketorolac for acute migraine attack |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic Review/Meta-analysis | Adv Clin Exp Med | IV ketorolac vs metoclopramide for adult migraine headaches |
| [8240554](https://pubmed.ncbi.nlm.nih.gov/8240554/) | 1993 | Observational (Patient-evaluated) | American Journal of Emergency Medicine | Ketorolac reduced migraine pain/nausea rapidly per patient self-assessment at 30/60/90 min |

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug-interaction data could be extracted for this evidence pack (data gap DG001, flagged **Blocking** — this must be resolved before any S1 safety pre-screening can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence is unusually strong for a repurposing candidate — dozens of completed Phase 2–4 RCTs, multiple systematic reviews/meta-analyses, and inclusion in the 2025 American Headache Society ED migraine guideline (Evidence Level L1). However, the drug currently has **zero market authorizations in Germany**, and safety labeling data (warnings, contraindications, DDI) is completely unavailable — a **Blocking** data gap that prevents entry into the S1 safety pre-screening stage regardless of efficacy strength.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert with full warnings, contraindications, and precautions (resolve DG001)
- Detailed mechanism of action / pharmacology profile from DrugBank or primary literature (resolve DG002)
- Confirmation of feasible administration route (IV/IM/intranasal) aligned with ED migraine treatment protocols
- Assessment of regulatory pathway given the drug's current unmarketed status in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

