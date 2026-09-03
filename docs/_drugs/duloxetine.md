---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Approved Antidepressant Uses to Obsessive-Compulsive Disorder

## One-Sentence Summary

Duloxetine (DB00476) is a serotonin-norepinephrine reuptake inhibitor (SNRI) whose formally licensed indications are not recorded in this evidence pack, but literature within the pack confirms it is an approved antidepressant used for major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia, and chronic musculoskeletal pain. Among 10 TxGNN-predicted indications, **Obsessive-Compulsive Disorder (OCD)** is the only candidate with substantive clinical evidence — **5 clinical trials** (including a completed Phase 4 trial and a double-blind RCT) and **19 publications**, giving it the strongest evidence tier (L2) of all candidates screened.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not populated in `taiwan_regulatory.licenses` (empty). Per literature in this pack (PMID 31749717): major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia, chronic musculoskeletal pain |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L2 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa`: [Data Gap]). Based on known information and the literature captured in this evidence pack, duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI), a pharmacological class whose serotonergic component overlaps with the mechanism believed to underlie OCD pathophysiology.

OCD is currently treated first-line with high-dose SSRIs and clomipramine, both of which act primarily through serotonin reuptake inhibition. Since duloxetine shares this serotonergic mechanism (plus additional noradrenergic activity), several independent groups have tested it directly in OCD, including as monotherapy and as an augmentation strategy in treatment-resistant cases. Two review articles in this pack (PMID 16669725, PMID 21779536) specifically discuss SNRIs — including duloxetine — as a rational pharmacological alternative to SSRIs in OCD, reinforcing the mechanistic plausibility of the TxGNN prediction.

It is worth noting that this is the strongest-evidence candidate among the 10 TxGNN predictions provided (see "Other Predicted Indications" below); most other top-ranked candidates in this evidence pack are explicitly flagged by the underlying rationale as likely graph noise with no supporting mechanism or clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Directly assessed efficacy of duloxetine in treating OCD (Grade A relevance) |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicted medication response in OCD; duloxetine arm offered to patients who had already tried clomipramine/escitalopram (Grade B) |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Individual-patient-data meta-analysis of antidepressant efficacy across anxiety disorders; not OCD-specific (Grade C) |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | Unknown | 1 | Single-case psychoanalytic treatment study in ASD with OCD comorbidity; weak relevance (Grade C) |
| [NCT01944657](https://clinicaltrials.gov/study/NCT01944657) | N/A | Withdrawn | 0 | TMS vs. medication monotherapy for depression; withdrawn with zero enrollment, no evidentiary value (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | RCT (double-blind) | Journal of Clinical Psychopharmacology | Duloxetine augmentation evaluated in treatment-resistant OCD |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label study | Int J Neuropsychopharmacology | Efficacy of duloxetine monotherapy for DSM-IV OCD |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case series | J Psychopharmacology | Switching from SSRIs to duloxetine in resistant OCD |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Review | Innovations in Clinical Neuroscience | SNRIs (incl. duloxetine) as pharmacological alternatives for OCD |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical review | J Clinical Psychiatry | Critical review of SNRIs in OCD treatment |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of serotonergic antidepressants in OCD |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Systematic review | Frontiers in Psychiatry | Duloxetine use expansions beyond MDD/GAD, including OCD |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | Journal of Affective Disorders | OCD shows reduced placebo/antidepressant response vs. other anxiety disorders |
| [19483491](https://pubmed.ncbi.nlm.nih.gov/19483491/) | 2009 | Case report | Clinical Neuropharmacology | High-dose duloxetine achieved sustained full remission in treatment-resistant OCD |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case report | Primary Care Companion J Clin Psychiatry | OCD case responding to duloxetine |

---

## Germany Market Information

Currently not marketed in Germany per this evidence pack (`taiwan_regulatory.market_status`: 未上市, `total_licenses`: 0). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and `ddi` are all unpopulated in this evidence pack — flagged as Blocking data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
OCD is the only predicted indication with substantive supporting evidence — a completed Phase 4 trial, a double-blind RCT, and multiple reviews specifically addressing SNRI use in OCD — reaching Evidence Level L2. However, the drug's original indication, MOA, and safety/label data are all data gaps in this pack, and the drug is not currently marketed in Germany, so this cannot yet proceed to a full go decision.

**To proceed, the following is needed:**
- TFDA/BfArM label warnings and contraindications (DG001, Blocking — required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank (DG002)
- Confirmation of original approved indications and any Germany market pathway
- Formal DDI review, since current query returned no interaction data

---

## Other Predicted Indications from TxGNN (Additional Candidates, Not Prioritized)

For transparency, the remaining 8 of 10 TxGNN-predicted indications in this evidence pack had no supporting clinical trials or literature and were scored L5/Hold, with the rationale text explicitly flagging several as likely **graph prediction noise** (no known mechanistic link to SNRI pharmacology): benign paroxysmal torticollis of infancy (rank 1, top TxGNN score but zero evidence), schizotypal/paranoid/schizoid/histrionic personality disorders, Ohdo syndrome and variants, ligneous conjunctivitis, and blepharophimosis-intellectual disability syndrome (Ohdo type).

**Agoraphobia** (rank 2, L3, decision stage S1, recommendation "Research Question") showed early-stage support — one open-label study and one biomarker RCT context, though the disease-definition overlap between panic disorder and agoraphobia narrowly-defined needs clarification before further investment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

