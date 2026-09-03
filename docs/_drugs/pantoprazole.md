---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 6
---

# Pantoprazole
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

# Pantoprazole: From Established PPI Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI); no formal original-indication or market-authorization data is on file for this drug in the current jurisdiction, but the compound is globally recognized (per the literature in this evidence pack) as a treatment for acid-related disorders such as GERD, erosive esophagitis, and H. pylori eradication regimens.
The TxGNN model's top prediction is **Active Peptic Ulcer Disease**, supported by **3 clinical trials** and **19 publications** — importantly, this is a standard, already-established use of PPIs rather than a novel mechanistic extension.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this jurisdiction (no license records); pharmacologically an established PPI for GERD/erosive esophagitis/H. pylori eradication per literature evidence |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured DrugBank MOA field is available for this drug (marked as a data gap). However, the evidence pack's mechanistic rationale and supporting literature (e.g., PMID 19938880, PMID 9017763) consistently describe pantoprazole as a proton pump inhibitor that **irreversibly binds and inhibits the H+/K+-ATPase enzyme in gastric parietal cells**, thereby reducing gastric acid secretion at its final common step.

This mechanism is the well-established pharmacological basis for treating all acid-related disorders, including peptic ulcer disease. As the model's own rationale states directly: *"Pantoprazole irreversibly inhibits parietal cell H+/K+-ATPase, directly reducing gastric acid secretion — this is the standard, approved treatment mechanism for active peptic ulcer disease, not a novel mechanistic extension."*

In other words, this prediction largely **confirms known PPI pharmacology** rather than revealing a genuinely new therapeutic pathway. The practical significance here is less about mechanistic novelty and more about **regulatory/market status**: this drug has zero recorded local licenses, so the relevant question is market entry / filing for an indication that is already pharmacologically well-supported worldwide, rather than off-label repurposing risk.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial comparing Ilaprazole vs. Pantoprazole triple therapy for H. pylori eradication in gastric/duodenal ulcer patients (Grade A relevance) |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Prospective study identifying risk factors for poor SRH fading/early rebleeding after endoscopic hemostasis and high-dose PPI infusion, to guide second-look endoscopy criteria (Grade B relevance) |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated influence of PPIs (and statins) on clopidogrel antiplatelet effect in PCI patients — DDI-focused, not a direct ulcer-efficacy trial (Grade C relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective RCT comparing intermittent vs. continuous pantoprazole infusion for peptic ulcer bleeding after endoscopic therapy |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Compared three pantoprazole-based triple therapy regimens for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Prospective RCT of pantoprazole infusion as adjuvant therapy to endoscopic treatment for peptic ulcer bleeding outcomes |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | RCT comparing amoxycillin/clarithromycin plus sucralfate or pantoprazole for H. pylori eradication in duodenal ulcer |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Comparative Study | Hepatogastroenterology | Compared efficacy of lansoprazole and pantoprazole in active duodenal ulcer treatment and H. pylori eradication |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Clinical Study | Aliment Pharmacol Ther | Pantoprazole with amoxycillin and azithromycin/clarithromycin for H. pylori eradication in duodenal ulcer |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Clinical Study | Med Arch | Evaluated PPI efficacy after endoscopic hemostasis in bleeding peptic ulcer, role of H. pylori |
| [10228801](https://pubmed.ncbi.nlm.nih.gov/10228801/) | 1999 | Clinical Study | Hepatogastroenterology | Rapid symptomatic improvement with pantoprazole + amoxycillin + metronidazole in H. pylori-positive duodenal ulcer |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | Clinical Study | Aliment Pharmacol Ther | Two-week pantoprazole with 1-week amoxycillin/clarithromycin effective for H. pylori eradication and duodenal ulcer healing |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Overview of pantoprazole's mechanism (irreversible H+/K+-ATPase binding), long duration of action, and DDI profile |

---

## Germany Market Information

Pantoprazole currently holds **0 authorizations** in this jurisdiction's license registry — market status is recorded as **Not Marketed**, with no license entries available to summarize.

---

## Safety Considerations

⚠️ **Blocking data gap**: Package insert warnings and contraindications for this drug have not yet been retrieved (severity: Blocking). Per the evidence pack, this gap must be resolved before the candidate can formally enter the S1 safety pre-assessment stage.

Please refer to the package insert for detailed safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical trial/literature evidence for PPI efficacy in active peptic ulcer disease is extensive and well-established (Evidence Level L1) — this is not a mechanistically novel repurposing signal but a pharmacologically well-supported use. However, the drug currently has no local market authorization and a **blocking** safety data gap (missing label warnings/contraindications), so guardrails are warranted before advancing.

**To proceed, the following is needed:**
- Retrieve and parse official package insert (warnings, contraindications, DDI) to resolve the blocking safety data gap (DG001)
- Obtain structured DrugBank MOA data to formally document mechanism (DG002)
- Confirm regulatory filing/licensing pathway, since 0 local authorizations currently exist despite global PPI approval status
- Given the mechanistic overlap, evaluate whether the lower-ranked candidates (duodenal ulcer, L1; gastrojejunal ulcer, peptic ulcer perforation, L2) warrant a combined submission strategy rather than separate single-indication filings
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

