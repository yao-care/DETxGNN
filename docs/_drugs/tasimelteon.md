---
layout: default
title: Tasimelteon
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From Non-24-Hour Sleep-Wake Disorder to Insomnia

## One-Sentence Summary

Tasimelteon is a melatonin MT1/MT2 receptor agonist currently approved for Non-24-Hour Sleep-Wake Disorder, acting on the suprachiasmatic nucleus to regulate circadian rhythm and sleep onset. The TxGNN model predicts it may also be effective for **Insomnia**, with **4 clinical trials (including one completed Phase 3 RCT)** and **6 supporting publications** currently identified. Note: TxGNN generated 9 other candidate indications for tasimelteon (e.g., ALS, polymicrogyria, endogenous depression), but all except insomnia lack meaningful clinical or literature support and are rated Hold (L5) or Research Question (L4) — this report focuses on the insomnia candidate, which has by far the strongest evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-24-Hour Sleep-Wake Disorder (existing approved indication, referenced in evidence rationale) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap, DG002). However, the evidence pack's repurposing rationale confirms that tasimelteon is a melatonin MT1/MT2 receptor agonist, acting directly on the suprachiasmatic nucleus (SCN) — the body's circadian pacemaker — to regulate circadian rhythm and promote sleep initiation.

Insomnia and Non-24-Hour Sleep-Wake Disorder are both circadian-rhythm-related sleep disorders sharing the same underlying pathophysiology: dysregulation of the sleep-wake cycle. Since tasimelteon's approved indication already targets this pathway, its predicted efficacy in insomnia represents a mechanistically coherent extension within the same therapeutic class, rather than a novel unrelated use. This is consistent with the broader melatonergic drug class (ramelteon, agomelatine), which is also used across both circadian rhythm disorders and primary insomnia.

It is worth noting this significant overlap means the "repurposing" value here may be incremental rather than transformative, since the mechanistic rationale for insomnia is essentially an extension of the drug's existing chronobiotic action rather than a discovery of a novel therapeutic pathway.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Multicenter, double-blind, placebo-controlled 5-week trial of VEC-162 (tasimelteon) 20mg/50mg in primary insomnia; highest-quality evidence to date. |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Multicenter, double-blind, randomized study evaluating tasimelteon vs. placebo in pediatric insomnia disorder. |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in travelers with jet lag disorder; related but not core primary insomnia population. |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Single-center, open-label pilot study of tasimelteon in REM Behavior Disorder, also assessing insomnia symptom scales (ISI, PSQI); terminated, low evidentiary value. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | Int J Mol Sci | Reviews therapeutic effects of melatonin receptor agonists (including tasimelteon) on sleep and comorbid disorders. |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | J Med Chem | Reviews MT1/MT2 receptor pharmacology and therapeutic potential of melatonergic drugs including tasimelteon. |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatr Dis Treat | Discusses management of insomnia with prolonged-release melatonin and synthetic melatoninergic agonists. |
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Curr Drug Saf | Discusses melatonin and tasimelteon in the context of Alzheimer's disease-related insomnia and cognitive decline. |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Ther Adv Neurol Disord | Reviews melatonin analogs' therapeutic potential for sleep disorders in Parkinson's disease. |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinol Lett | Discusses circadian sleep disruption and possible therapeutic value of melatonin in obesity-related sleep disorders. |

## Germany Market Information

No market authorization records are currently registered in Germany — tasimelteon is not marketed (0 authorizations found).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are currently unavailable — flagged as Blocking data gap DG001, requiring TFDA/BfArM label retrieval before safety evaluation can proceed.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The insomnia prediction is supported by L1 evidence, including one completed Phase 3 RCT (NCT00548340, n=322) and an ongoing pediatric Phase 3 trial, plus a mechanistically coherent link to tasimelteon's existing approved indication. However, the drug is not currently marketed in Germany, and safety labeling data remains an unresolved blocking gap.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): Retrieve official TFDA/BfArM product labeling for warnings, contraindications, and DDI data before any S1 safety evaluation.
- Resolve DG002 (High): Confirm formal mechanism-of-action documentation via DrugBank API to validate the mechanistic rationale currently derived only from repurposing_rationale text.
- Clarify degree of indication overlap with the existing Non-24-Hour Sleep-Wake Disorder approval, to determine whether this constitutes a genuine label extension or requires a distinct regulatory pathway.
- Monitor completion of NCT06953869 (pediatric Phase 3, est. completion 2028-01) for confirmatory evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

