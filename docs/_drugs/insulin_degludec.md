---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
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

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus (Confirmatory Signal)

## One-Sentence Summary

> Insulin degludec is an ultra-long-acting basal insulin analogue, internationally approved for Type 1 and Type 2 Diabetes Mellitus, but it is not currently marketed in Taiwan.
> The TxGNN model's top prediction — **Type 1 Diabetes Mellitus** — is essentially the drug's already-established, globally approved indication rather than a novel repurposing target,
> supported by **59 clinical trials** and **20 publications**, including large landmark Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan (未上市); internationally approved for Type 1/2 Diabetes Mellitus as basal insulin replacement therapy |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacology, insulin degludec is an ultra-long-acting basal insulin analogue that acts directly on the insulin receptor, providing exogenous insulin replacement — its efficacy in Type 1 Diabetes Mellitus has been extensively proven in clinical practice worldwide.

**Important caveat:** this top-ranked prediction is not a novel repurposing signal. Type 1 Diabetes Mellitus is insulin degludec's already-established, globally approved indication (marketed as Tresiba® in most markets). The TxGNN model here is confirming a known drug-disease relationship rather than uncovering a new therapeutic opportunity. The "not marketed" status recorded under Taiwan regulatory data reflects a **market-access gap** (the product has not been registered/launched in Taiwan), not a clinical efficacy or safety gap.

Given this, the practical value of this evidence pack is less about validating a new indication and more about supporting a potential **Taiwan market-entry** decision for a drug with an already mature global evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | Completed | 1,108 | Faster-acting insulin aspart vs NovoRapid®, both combined with insulin degludec, in adults with T1DM |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1,392 | PRONTO-T1D: LY900014 vs insulin lispro, both with glargine or degludec, in T1DM |
| [NCT05904743](https://clinicaltrials.gov/study/NCT05904743) | Phase 4 | Completed | 141 | INHALE-3: inhaled insulin + degludec vs usual care in T1DM (Grade B relevance) |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2: degludec vs glargine safety/efficacy comparison, ± OADs (Grade A relevance) |
| [NCT01959529](https://clinicaltrials.gov/study/NCT01959529) | Phase 3 | Completed | 7,637 | DEVOTE: cardiovascular safety of degludec vs glargine in high-CV-risk diabetes — landmark outcomes trial |
| [NCT01984372](https://clinicaltrials.gov/study/NCT01984372) | N/A (PMS) | Completed | 6,163 | Long-term (3-year) post-marketing safety/effectiveness surveillance of Tresiba® |
| [NCT02662114](https://clinicaltrials.gov/study/NCT02662114) | N/A | Completed | 2,302 | EU-TREAT: real-world effectiveness of degludec after switching basal insulin, T1/T2DM |
| [NCT04450394](https://clinicaltrials.gov/study/NCT04450394) | Phase 2 | Completed | 278 | LY3209590 vs degludec (active comparator) in insulin-naïve T2DM (Grade B relevance) |
| [NCT03557892](https://clinicaltrials.gov/study/NCT03557892) | N/A | Completed | 28 | CSII+CGM vs MDI using degludec as basal insulin, crossover trial in T1DM (Grade C relevance) |
| [NCT01046110](https://clinicaltrials.gov/study/NCT01046110) | Phase 3 | Completed | 458 | BEGIN™ EARLY: degludec vs sitagliptin add-on in insulin-naïve T2DM (Grade B relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: degludec vs detemir (both + aspart) in pregnant women with T1DM, non-inferiority |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg: degludec vs glargine U100 in T1DM prone to nocturnal severe hypoglycaemia |
| [36610544](https://pubmed.ncbi.nlm.nih.gov/36610544/) | 2023 | RCT | Diabetes Res Clin Pract | INEOX: degludec 100 IU/mL vs glargine 300 IU/mL efficacy/safety in T1DM |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | Phase 3a RCT | Lancet | ONWARDS 6: once-weekly icodec vs once-daily degludec in T1DM basal-bolus regimen |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | Phase 3 RCT | Lancet | QWINT-5: once-weekly efsitora alfa vs degludec in T1DM, non-inferiority |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review/Meta-analysis | Clin Ther | Efficacy/tolerability of degludec vs other long-acting basal insulins in T1D/T2D |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | Systematic Review | Int J Clin Pharm | Indirect comparison: degludec U100 vs glargine U300 in T1D — safety, efficacy, cost-effectiveness |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network Meta-Analysis | Value Health | Basal insulin regimens for adults with T1DM: systematic review and network meta-analysis |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | Current status of degludec in T1D and T2D based on randomized and observational trials |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Review | Endocrinol Nutr | Degludec, a new ultra-long-acting basal insulin: advances in clinical research |

---

## Taiwan Market Information

Insulin degludec currently holds **no marketing authorization in Taiwan** (0 licenses on record; market status: 未上市). No product entries are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug interaction data are currently available in this evidence pack (TFDA label data flagged as a Blocking data gap, DG001).

---

## Other Predicted Indications (Not Pursued)

Ranks 2–6 (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome) all carry **L4–L5 evidence** with **zero supporting clinical trials or literature**. These reflect knowledge-graph co-occurrence patterns (e.g., shared GAD65 autoimmunity or diabetes comorbidity) rather than direct pharmacological rationale. All are recommended **Hold**.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (T1DM) is backed by an extensive, mature L1-level global evidence base (multiple large Phase 3/4 RCTs and landmark outcome trials), but it confirms an already-approved indication rather than a novel repurposing opportunity. The practical decision here is a **Taiwan market-access** question, not a repurposing-validation question — and it is currently blocked by missing TFDA-specific regulatory data.

**To proceed, the following is needed:**
- TFDA-approved package insert (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Clarification of Taiwan registration/import status and any planned market-entry timeline for insulin degludec (Tresiba®)
- If market entry is pursued, no additional indication-validation studies are needed given the existing global L1 evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

