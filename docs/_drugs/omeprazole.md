---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Omeprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

> Omeprazole is a proton pump inhibitor (PPI) established for acid-related gastrointestinal conditions such as peptic ulcer disease, GERD, and *H. pylori* eradication.
> The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
> with **1 clinical trial** and **20 publications** currently identified in relation to this direction — though the evidence is mixed, with some studies also raising a carcinogenesis safety signal (see below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in German regulatory data (drug not marketed in Germany). Per established PPI pharmacology and supporting literature in this pack (e.g., PMID 18679668), omeprazole is used for peptic ulcer disease, *H. pylori* infection, GERD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 (observational/clinical studies, no completed RCTs specific to this indication) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, omeprazole is a proton pump inhibitor that irreversibly blocks the H+/K+-ATPase in gastric parietal cells, suppressing acid secretion — a mechanism proven effective across peptic ulcer disease, GERD, and *H. pylori*-related conditions.

Duodenogastric reflux (DGR) involves retrograde flow of duodenal contents (bile, pancreatic enzymes) into the stomach, often co-occurring with acid-related GI disorders and contributing to mucosal injury in conditions like Barrett's esophagus. Several clinical studies in this evidence pack (e.g., PMID 9824338, 10994616, 19491829) directly examined omeprazole's effect on DGR/DGOR in reflux populations, providing a plausible mechanistic bridge from the original acid-suppression indication to this new target.

However, the mechanistic picture is not uniformly favorable: multiple animal studies (PMID 10389684, 8943968, 33027361, 15052437) report that gastric acid blockade with omeprazole (and other PPIs) may *potentiate* mucosal growth stimulation and gastric carcinogenesis when combined with DGR, since higher intragastric pH can increase bile cytotoxicity. This nuance should be weighed carefully rather than treated as a straightforward "efficacy" signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | Completed | 157 | Evaluated endoscopic Tri-Modal Imaging (NBI/AFI/WLI) to distinguish functional dyspepsia from acid/bile reflux disease; not a treatment-efficacy trial for omeprazole itself |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Clinical study | Gut | Omeprazole 20mg BID effect on duodenogastric and duodenogastro-oesophageal bile reflux in Barrett's oesophagus |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Clinical study | Scand J Gastroenterol | Effect of omeprazole on antral duodenogastric reflux in Barrett oesophagus |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Clinical study | Am J Gastroenterol | Compared degree of DGER/acid reflux between PPI responders and non-responders |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Clinical (prospective) | J Pediatr Gastroenterol Nutr | Prospective study of omeprazole for oesophageal bile reflux in children |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Description of primary duodenogastric reflux in children/adolescents |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Review of PPI clinical use and pharmacokinetics (contextualizes original indications) |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Preclinical (rat) | Acta Cir Bras | Investigated whether omeprazole is protective against gastric adenocarcinoma under induced DGR |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Preclinical (rat) | Dig Dis Sci | ⚠️ Gastric acid blockade with omeprazole promoted gastric carcinogenesis induced by DGR |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Preclinical (rat) | Dig Dis Sci | ⚠️ DGR-induced foregut mucosal growth stimulation potentiated by gastric acid blockade (omeprazole arm) |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Preclinical (rat) | Gastric Cancer | ⚠️ Related PPI (lansoprazole) promoted gastric carcinogenesis in rats with DGR — class-effect caution |

## Germany Market Information

Omeprazole currently has no marketing authorization records in the German regulatory dataset provided (0 licenses, market status: Not Marketed).

## Safety Considerations

> Please refer to the package insert for safety information.

**Important caveat:** The evidence pack flags a **Blocking** data gap (DG001) — TFDA/regulatory label warnings and contraindications have not yet been retrieved — which by definition prevents this candidate from entering the S1 safety pre-assessment stage. Additionally, DrugBank DDI query returned no results (`query_status: not_found`), so no drug interaction data could be evaluated at this time.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While duodenogastric reflux shows plausible mechanistic rationale and moderate (L3) observational clinical evidence, a **Blocking-severity data gap** on regulatory safety labeling (warnings/contraindications) prevents completion of the mandatory S1 safety screen. This is compounded by a notable safety signal in preclinical literature suggesting acid suppression may potentiate gastric carcinogenesis in the presence of chronic DGR — a risk that must be resolved before advancing.

**To proceed, the following is needed:**
- Retrieve TFDA (or equivalent) product label for warnings/contraindications (DG001, Blocking)
- Retrieve DrugBank MOA data to support formal mechanistic-link scoring (DG002, High)
- Complete a DDI database query (current status: not found)
- Formally reconcile the conflicting evidence base — clinical studies suggesting symptomatic benefit vs. animal studies suggesting a long-term carcinogenesis risk under chronic acid suppression with DGR
- Note: the secondary predicted indication (duodenal obstruction, rank 2) was already internally scored as L4/S0/**Hold** in this evidence pack, consistent with the overall conservative recommendation for this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

