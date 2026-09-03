---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Tay-Sachs Disease (GM2 Gangliosidosis)

## One-Sentence Summary

Miglustat is a glucosylceramide synthase inhibitor (substrate reduction therapy) originally approved in the EU for type 1 Gaucher disease. Among the ten indications predicted by TxGNN, **Tay-Sachs disease (GM2 gangliosidosis)** is the only candidate backed by real-world data — **5 clinical trials** (including a completed randomized controlled study) and **20 publications** — even though it ranks lower on the raw TxGNN score than several mechanistically weaker, evidence-free candidates.

> **Note on candidate selection:** TxGNN's #1-ranked prediction ("autosomal ichthyosis syndrome with fatal disease course") has zero supporting trials or literature and, per the model's own rationale note, a "weak mechanistic link." Tay-Sachs disease (rank 7 by score) is the only prediction in this pack with substantive clinical evidence, so this report focuses on it as the actionable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease type 1 (per literature evidence in this pack; official regulatory indication text unavailable — see Data Gaps) |
| Predicted New Indication | Tay-Sachs disease (GM2 gangliosidosis) |
| TxGNN Prediction Score | 99.75% (rank 3492 of full candidate set) |
| Evidence Level | L2 (1 completed randomized controlled trial + supporting systematic review) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank MOA data is marked as a data gap in this pack, but the mechanism is well documented in the literature evidence collected: miglustat is an orally administered **glucosylceramide glucosyltransferase (glucosylceramide synthase) inhibitor**, working as a **substrate reduction therapy (SRT)** for glycosphingolipid (GSL) storage disorders (PMID 12808890, 11227045, 16763917).

Tay-Sachs disease is caused by β-hexosaminidase A deficiency, leading to lysosomal accumulation of GM2 ganglioside — a glycosphingolipid synthesized via the same upstream glucosylceramide pathway that miglustat inhibits. Because miglustat reduces the *production* of GSL substrates (including GM2 ganglioside precursors) rather than replacing the missing enzyme, the mechanistic rationale for extending it from Gaucher disease (glucosylceramide accumulation) to Tay-Sachs disease (GM2 ganglioside accumulation) is direct and biologically plausible — unlike most of the other TxGNN-predicted candidates in this pack, whose target diseases involve unrelated storage pathways (cholesterol esters, sulfatides, steroid sulfate).

This mechanistic plausibility is also reflected in the trial record: miglustat has already been studied in animal models and human patients with Tay-Sachs/Sandhoff (GM2 gangliosidosis) disease since the late 1990s, culminating in an RCT and a 2023 systematic review — making this the most mature repurposing candidate in the pack, notwithstanding mixed efficacy results (see below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | PK, safety and tolerability of miglustat in infantile-onset GM2 gangliosidosis (single/steady-state oral dosing) |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | PK and tolerability of miglustat in juvenile GM2 gangliosidosis, single and multiple oral doses |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Survey of miglustat's therapeutic effect on neurological/systemic symptoms in infantile Sandhoff and Tay-Sachs disease |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | Miglustat + ketogenic diet combination therapy for infantile/juvenile gangliosidoses (Syner-G study) |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety/efficacy of nizubaglustat in GM2 gangliosidosis/NPC patients, including those previously on miglustat |

**Note:** Two trials (NCT03822013, NCT02030015) were terminated, and the two completed Phase 2/3 studies were PK/tolerability studies rather than efficacy-driven RCTs — this tempers the strength of the clinical trial evidence despite the number of studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genet Med | 12-month randomized controlled study (+24-month extension) evaluating miglustat safety/efficacy in late-onset Tay-Sachs disease |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | Eur J Neurol | Systematic review finds prior studies on miglustat efficacy/safety in GM2 gangliosidosis are **inconsistent** |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | Int J Mol Sci | Overview of GM2 gangliosidosis clinical features, pathophysiology, and current therapies including SRT |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Review | Expert Rev Endocrinol Metab | Substrate reduction therapy with miglustat for glycosphingolipid storage disorders affecting the brain |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Review (Drug Profile) | Curr Opin Investig Drugs | Confirms EU approval of miglustat for Gaucher disease and its development for Tay-Sachs, Fabry, and NPC diseases |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Front Physiol | Reviews new therapeutic approaches to Tay-Sachs disease, including substrate reduction therapy |
| [11227045](https://pubmed.ncbi.nlm.nih.gov/11227045/) | 2001 | Review | Expert Opin Investig Drugs | Early review of substrate reduction therapy rationale for glycosphingolipid storage disorders |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilot Study | J Inherit Metab Dis | Neurocognitive testing pilot study in late-onset Tay-Sachs disease as a candidate outcome measure |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Case Report | Neurology | SRT with miglustat in 2 infantile Tay-Sachs patients: did **not** arrest neurologic deterioration, though CSF drug levels and macrocephaly prevention were observed |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Observational | Mol Genet Metab | Natural history mapping of infantile gangliosidosis; notes miglustat use limited by GI side effects |

---

## Germany Market Information

Miglustat is currently **not marketed** in this jurisdiction (`market_status: 未上市`) and no authorization records are present in this Evidence Pack (`total_licenses: 0`). No product/authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

⚠️ **Critical Data Gap:** Detailed TFDA package insert warnings and contraindications (DG001) are marked as a **Blocking** gap in this Evidence Pack, meaning this candidate **cannot yet proceed to S1 safety pre-assessment**. Known real-world safety issues with miglustat (from its approved use in Gaucher/NPC) include gastrointestinal side effects (diarrhea, weight loss) and peripheral neuropathy, but these are not sourced from this pack's structured safety fields and should be independently verified before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although miglustat has a mechanistically sound rationale and an unusually rich trial/literature record compared to other candidates in this pack, the evidence is mixed — two trials were terminated, the only RCT and the 2023 systematic review report inconsistent efficacy, and a completed case series found no arrest of neurologic decline in infantile Tay-Sachs disease. Combined with a **Blocking** data gap on TFDA safety labeling, the candidate is not yet ready to advance.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/official package insert warnings and contraindications
- Resolve DG002: obtain confirmed DrugBank MOA record (currently inferred only from literature)
- Independent efficacy assessment reconciling the 2023 systematic review's "inconsistent" findings with the 2009 RCT's positive extension data
- Root-cause review of why NCT03822013 and NCT02030015 were terminated (safety vs. enrollment vs. futility)
- Regulatory pathway assessment given the drug is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

