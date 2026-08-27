---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: From Major Depressive Disorder to a Multi-Indication Candidate Portfolio

## A Note on Scope

This Evidence Pack (`TW-DB06594-multi`) is a **multi-indication scan** — TxGNN generated 10 ranked candidate indications for agomelatine rather than a single top prediction. Applying the standard single-indication template to rank #1 alone (*benign paroxysmal torticollis of infancy*) would be misleading: the evidence pack itself flags that prediction as a likely knowledge-graph false positive. This report therefore covers the full candidate set as a portfolio, then drills into the two indications with the strongest supporting evidence.

---

## One-Sentence Summary

Agomelatine is a melatonergic (MT1/MT2 agonist) and serotonergic (5-HT2C antagonist) antidepressant, with **major depressive disorder (MDD)** as its established use per the literature (no formal regulatory indication text was retrievable — see Data Gaps below). TxGNN surfaced **10 candidate indications**, but only **2 of the 10** (melancholia, neurotic depression) reach a high evidence level (**L1**), and both are essentially restatements of agomelatine's known antidepressant activity rather than genuine new indications; the remaining candidates are either weakly-supported psychiatric spectrum disorders (**L4**) or unsupported rare genetic syndromes (**L5**) that the evidence pack itself classifies as model noise.

---

## Quick Overview

**Drug-level facts**

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (derived from literature context, e.g. EMA approval review PMID 19777735; not present in formal regulatory data — see Data Gaps) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Overall Recommendation | **Hold** (portfolio-level; see per-indication table) |

**Predicted indications portfolio (all 10, ranked by TxGNN score)**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|----------------|-----------------|
| 1 | Benign paroxysmal torticollis of infancy | 99.96% | L5 | S0 | Hold |
| 2 | Agoraphobia | 99.95% | L4 | S1 | Research Question |
| 3 | Neurotic disorder | 99.90% | L4 | S1 | Research Question |
| 4 | Melancholia | 99.88% | L1 | S3 | Proceed with Guardrails |
| 5 | Neurotic depression | 99.88% | L1 | S3 | Proceed with Guardrails |
| 6 | Ohdo syndrome and variants | 99.87% | L5 | S0 | Hold |
| 7 | Dysthymic disorder | 99.86% | L4 | S1 | Research Question |
| 8 | Ligneous conjunctivitis | 99.83% | L5 | S0 | Hold |
| 9 | Blepharophimosis–intellectual disability syndrome, Ohdo type | 99.82% | L5 | S0 | Hold |
| 10 | Keppen-Lubinsky syndrome | 99.81% | L5 | S0 | Hold |

Note: TxGNN scores cluster tightly (99.81–99.96%) and do **not** track evidence quality here — several of the highest-scored candidates (rank 1, 6, 8, 9, 10) have zero clinical trials, zero literature, and no plausible mechanistic link, per the evidence pack's own rationale text.

---

## Why Are These Predictions Reasonable (or Not)?

Currently, detailed mechanism of action data from a structured source (e.g. DrugBank MOA field) is not available — this is logged as data gap **DG002 (High severity)**. Based on the literature reviewed for this pack, agomelatine acts as an **MT1/MT2 melatonergic receptor agonist and a 5-HT2C serotonergic receptor antagonist**, which resynchronizes disrupted circadian rhythms, improves slow-wave sleep, and enhances dopamine/noradrenaline release in the prefrontal cortex — mechanisms established through its approved use in major depressive disorder.

The 10 candidates split into two clearly distinct clusters:

- **Mood/anxiety-spectrum cluster** (agoraphobia, neurotic disorder, melancholia, neurotic depression, dysthymic disorder): these are mechanistically coherent, since all fall within or adjacent to the depressive/anxiety spectrum where agomelatine's monoaminergic and circadian mechanisms are directly applicable. However, **melancholia** and **neurotic depression** are clinical subtypes/older nosological labels for MDD itself — the strong (L1) evidence behind them reflects agomelatine's *already-established* antidepressant efficacy, not a novel repurposing signal. The genuinely distinct candidates in this cluster — **agoraphobia**, **neurotic disorder**, **dysthymic disorder** — only reach L4, supported by indirect, class-level, or single non-specific studies rather than agomelatine-specific trials.
- **Rare-genetic-syndrome cluster** (Ohdo syndrome and its variants ×2, Keppen-Lubinsky syndrome, ligneous conjunctivitis): these have no clinical trials, no literature, and no plausible receptor-level connection to melatonergic/serotonergic pharmacology. The evidence pack's own rationale explicitly attributes these to embedding-proximity artifacts in the knowledge graph rather than real biological signal. They should be treated as noise, not candidates for further work.

---

## Clinical Trial Evidence

Across all 10 predicted indications, **no clinical trials are registered** on ClinicalTrials.gov or ICTRP (confirmed via 30 separate zero-result queries in the query log, IDs 5, 8, 11, 14, 17, 20, 23, 26, 29, 32).

---

## Literature Evidence

Literature was queried per-indication; results overlap heavily between melancholia and neurotic depression (both map to the same MDD literature base). Below are the 10 most relevant, deduplicated publications across the portfolio, prioritized by study tier and agomelatine-specificity.

| PMID | Year | Type | Journal | Related Indication(s) | Key Findings |
|------|-----|------|------|------|---------|
| [39684343](https://pubmed.ncbi.nlm.nih.gov/39684343/) | 2024 | Systematic Review/Meta-analysis (agomelatine-specific) | Int J Mol Sci | Melancholia, Neurotic depression | Efficacy and safety of agomelatine in depressed patients with comorbid diabetes |
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Network Meta-analysis (21 antidepressants incl. agomelatine) | Lancet | Melancholia, Neurotic depression | Comparative efficacy/acceptability ranking of antidepressants for acute MDD treatment |
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis of placebo-controlled RCTs | J Clin Psychiatry | Dysthymic disorder | Antidepressant efficacy for dysthymia vs MDD, class-level (not agomelatine-specific) |
| [32568567](https://pubmed.ncbi.nlm.nih.gov/32568567/) | 2020 | Review (agomelatine-specific) | Expert Opin Drug Discov | Melancholia, Neurotic depression | Preclinical discovery and development of agomelatine; first antidepressant acting beyond monoaminergic pathways |
| [30759026](https://pubmed.ncbi.nlm.nih.gov/30759026/) | 2019 | Review (agomelatine-specific) | Expert Opin Pharmacother | Neurotic depression | Agomelatine's dual MT-agonist/5-HT2C-antagonist action; use in depression comorbid with somatic disorders |
| [19777735](https://pubmed.ncbi.nlm.nih.gov/19777735/) | 2009 | Review (agomelatine-specific) | Med Monatsschr Pharm | Melancholia | Reports EMA approval of agomelatine (Valdoxan) for adult MDD, February 2009 |
| [26560173](https://pubmed.ncbi.nlm.nih.gov/26560173/) | 2015 | Cochrane Systematic Review | Cochrane Database Syst Rev | Melancholia | Agomelatine and melatonin evaluated for prevention of seasonal affective disorder |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review/Network Meta-analysis | Mol Psychiatry | Melancholia, Neurotic depression | Antidepressant efficacy/safety in MDD maintenance phase (class-level) |
| [25911132](https://pubmed.ncbi.nlm.nih.gov/25911132/) | 2015 | Systematic Review | J Affect Disord | Melancholia, Neurotic depression | Evidence-based antidepressant dose-equivalence recommendations from RCTs |
| [21183900](https://pubmed.ncbi.nlm.nih.gov/21183900/) | 2010 | Cohort/Observational | Zh Nevrol Psikhiatr Im S S Korsakova | Agoraphobia | Clinical predictors of therapeutic response to agomelatine (Valdoxan) in moderate-to-severe depression; not agoraphobia-specific |

---

## Germany Market Information

Agomelatine is currently **not marketed** in Germany per available regulatory data (`market_status: 未上市`), with **0 authorizations** on record. No BfArM license details were retrievable for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data were retrievable for this evidence pack (DDI query returned `not_found`).

---

## Conclusion and Next Steps

**Decision: Hold** (portfolio-level)

**Rationale:**
- The two highest-evidence candidates (melancholia, neurotic depression; L1) are not genuine repurposing opportunities — they are alternate clinical labels for agomelatine's already-approved indication (MDD), so they add limited new commercial or clinical value.
- The three candidates with plausible mechanistic novelty (agoraphobia, neurotic disorder, dysthymic disorder) only reach L4, supported by indirect, non-agomelatine-specific, or class-level literature — insufficient to justify proceeding without dedicated studies.
- Five candidates (benign paroxysmal torticollis of infancy, Ohdo syndrome and its two variants, ligneous conjunctivitis, Keppen-Lubinsky syndrome) have no clinical, literature, or mechanistic support and should be deprioritized as likely model artifacts.
- A **Blocking**-severity data gap (DG001) means TFDA/BfArM-equivalent label warnings and contraindications are unavailable, which by itself prevents this candidate from clearing the S1 safety pre-assessment stage regardless of indication.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official package insert (warnings/contraindications) from the relevant regulatory source.
- Resolve DG002 (High): obtain a structured mechanism-of-action record from the DrugBank API to support mechanistic-link scoring.
- For agoraphobia, neurotic disorder, and dysthymic disorder: seek agomelatine-specific (not class-level) clinical evidence — ideally a registered trial or a dedicated systematic review — before advancing past the "Research Question" stage.
- Deprioritize further evidence-gathering on the five L5 rare-syndrome candidates unless a future model version surfaces a credible mechanistic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

