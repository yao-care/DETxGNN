---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glucagon: From Severe Hypoglycemia to Irritable Bowel Syndrome

## One-Sentence Summary

> Glucagon is an endogenous pancreatic hormone conventionally used to treat severe hypoglycemia by raising blood glucose.
> The TxGNN model predicts a possible link to **Irritable Bowel Syndrome (IBS)** with a **99.24%** prediction score,
> but the underlying evidence — **11 clinical trials** and **20 publications** — is almost entirely about **GLP-1 receptor agonists**
> (ROSE-010, liraglutide, exendin‑4), a mechanistically opposite drug class, not glucagon itself. This is very likely a
> **false-positive signal driven by name similarity** between "Glucagon" and "Glucagon-Like Peptide-1 (GLP-1)."

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (no license or indication text on file; glucagon is clinically established for severe hypoglycemia management) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.24% (rank 8077 among model-wide candidates) |
| Evidence Level | L5 – model prediction only, no actual studies of glucagon in IBS |
| Germany Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for glucagon is not available in this evidence pack. However, glucagon's mechanism is well established in the literature: it binds the **glucagon receptor** (a distinct GPCR from the GLP-1 receptor) and raises blood glucose by stimulating hepatic glycogenolysis and gluconeogenesis — the physiological opposite of insulin and of GLP-1.

**This prediction does not hold up mechanistically.** Every clinical trial and publication supporting the IBS association involves **GLP-1 (Glucagon-Like Peptide-1) or its receptor agonists** (ROSE-010, liraglutide, exendin-4, native GLP-1) — not glucagon. While glucagon and GLP-1 both derive from cleavage of the same precursor gene (proglucagon), they act on different receptors and produce opposite physiological effects (glucagon raises blood glucose and accelerates gastric emptying; GLP-1 lowers blood glucose and *inhibits* gastric emptying/motility). Treating them as pharmacologically equivalent is not scientifically valid.

The evidence pack's own repurposing rationale reaches the same conclusion: no mechanistic link between glucagon (DB00040) and IBS was found. This pattern is consistent with a **retrieval false positive caused by shared substring/name overlap** ("glucagon" appearing inside "glucagon-like peptide-1") rather than a genuine drug-repurposing signal.

---

## Clinical Trial Evidence

⚠️ **None of the trials below study glucagon itself.** All involve GLP-1 or GLP-1 receptor agonists, listed here for transparency about what the underlying evidence actually supports.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (GLP-1 receptor agonist, **not glucagon**) effect on GI motor function in constipation-predominant IBS |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 vs. ROSE-010 inhibition of upper GI motility — no glucagon arm |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1 RA) for bowel frequency post-IPAA — mechanistically opposite to glucagon |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise effect on GLP-1 hormone and gut dysbiosis in IBS — no drug intervention |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low-energy diet + intragastric balloon for obesity — no glucagon or GLP-1 drug tested |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Fructo-oligosaccharide effect on reactive hypoglycemia — no glucagon intervention |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Butyrate mechanism in colon health (IBS-linked) — unrelated to glucagon |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Eating rate of ultra-processed foods on metabolic response — unrelated to glucagon |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completed | 33 | Whole grain rye bread effect on gut-brain axis peptides — unrelated to glucagon |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Gut-microbiota nutritional intervention at high altitude — unrelated to glucagon |

**Relevance assessment:** All graded **C** (not directly relevant) by the underlying evidence pack — none tested glucagon as the study drug.

---

## Literature Evidence

⚠️ **All publications below concern GLP-1 physiology or GLP-1 receptor agonists, not glucagon.**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scand J Gastroenterol | ROSE-010 (GLP-1 RA, **not glucagon**) reduced pain during IBS attacks |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | RCT | Am J Physiol GI Liver Physiol | Randomized double-blind study of ROSE-010 (GLP-1 analog) on GI motor function in IBS-C |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review/Meta-analysis | Front Endocrinol | GLP-1 receptor agonists improve IBS symptoms — glucagon not evaluated |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Endocrine role of GLP-1 (not glucagon) in IBS pathophysiology |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription/discontinuation patterns of GLP-1 RAs in IBS patients |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Review of investigational IBS-C drugs; glucagon not among candidates discussed |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical | Neurogastroenterol Motil | Exendin-4 (GLP-1 RA) improved GI dysfunction in rat IBS model |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical correlation | Clin Res Hepatol Gastroenterol | Serum GLP-1 (not glucagon) inversely correlated with abdominal pain in IBS-C |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclinical | Int J Mol Med | GLP-1's role in rat models of IBS pathogenesis |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 (not glucagon) for diabetes and IBS |

---

## Germany Market Information

No marketing authorization records are available for this drug in the current registry (market status: 未上市 / Not Marketed; 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this dataset (flagged as Blocking data gap DG001 — TFDA label warnings/contraindications, pending retrieval).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is very likely a **false-positive prediction caused by entity confusion** between "Glucagon" and "Glucagon-Like Peptide-1 (GLP-1)" — two hormones with opposing receptors and opposing physiological effects. Every piece of supporting clinical trial and literature evidence involves GLP-1 or GLP-1 receptor agonists, none involves glucagon itself, and the evidence pack is independently scored L5 ("model prediction only, no actual studies").

**To proceed, the following is needed:**
- Verify and correct entity disambiguation in the TxGNN knowledge graph (glucagon vs. GLP-1 node/edge separation) before this candidate is re-scored
- If a genuine preclinical rationale exists for glucagon (not GLP-1) in IBS, obtain actual glucagon-specific study data
- Resolve blocking data gap DG001 (TFDA label warnings/contraindications) and high-priority gap DG002 (MOA via DrugBank) before any further safety evaluation
- Given the drug is unmarketed in this registry, a market-access assessment would be required only if the mechanistic concern above is resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

