---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Loxapine
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

# Loxapine: From Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Loxapine is a first-generation dibenzoxazepine antipsychotic historically used for schizophrenia and other psychotic disorders. The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, and while no clinical trials are yet structured into this evidence pack, **20 publications** support the direction — several of which reference two pivotal Phase III RCTs of the inhaled formulation (Adasuve) already approved in the US and EU for acute agitation in bipolar disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / psychotic disorders (established in literature; not present in the German regulatory registry data supplied) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formally structured MOA data from DrugBank is not available in this evidence pack (data gap DG002). Based on well-established pharmacological literature, however, loxapine is a dibenzoxazepine-class first-generation antipsychotic that acts as a dual antagonist at dopamine D2 receptors and serotonin 5-HT2A receptors — the same receptor profile shared by most atypical antipsychotics used across the psychotic-spectrum disorders.

Schizophrenia and bipolar mania are distinct diagnoses but share a common acute clinical problem: psychomotor agitation driven by dopaminergic/serotonergic dysregulation. D2/5-HT2A blockade is the core pharmacological mechanism for controlling this symptom regardless of the underlying primary diagnosis, which is the mechanistic bridge underlying this prediction.

Critically, this is not a purely novel hypothesis — the inhaled loxapine formulation (Adasuve, Staccato delivery system) is **already approved in the US and EU** specifically for acute agitation in both schizophrenia **and** bipolar I disorder, based on two pivotal Phase III RCTs (NCT00628589, NCT00721955) plus the head-to-head PLACID trial versus IM aripiprazole. This TxGNN prediction therefore represents a label-adjacent indication extension with strong real-world clinical precedent, rather than a speculative new mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack's structured `clinical_trials` field.

> Note: The literature evidence below references two named pivotal Phase III RCTs (**NCT00628589**, **NCT00721955**) and the **PLACID** trial as the basis for the existing US/EU approval of inhaled loxapine in bipolar agitation. These should be pulled into a structured trial registry entry as a priority remediation item.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT | Eur Neuropsychopharmacol | PLACID trial: inhaled loxapine vs. IM aripiprazole in acutely agitated schizophrenia/bipolar I patients across 23 centres (Czech Republic, Germany, Spain, Russia) |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | RCT (post-hoc analysis) | BJPsych Open | PANSS-EC responder analysis from two pivotal Phase III RCTs (NCT00628589, NCT00721955) in 344 schizophrenia and 314 bipolar I patients |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | RCT (effect-size analysis) | Int J Clin Pract | Effect-size re-analysis of inhaled loxapine efficacy from 2 Phase III RCTs in schizophrenia/bipolar disorder |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review / Meta-analysis | Hum Psychopharmacol | Systematic review and meta-analysis of pharmacologic agitation treatments in schizophrenia and bipolar disorder |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | Review of inhaled loxapine powder (Adasuve), approved in US/EU for acute agitation in bipolar disorder/schizophrenia; median Tmax ~2 min |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Expert Review/Consensus | Drugs in R&D | Expert commentary on inhaled loxapine for acute agitation management in bipolar disorder and schizophrenia |
| [27121764](https://pubmed.ncbi.nlm.nih.gov/27121764/) | 2016 | Review (incl. Phase 3 RCT summary) | Curr Med Res Opin | Review of urgent treatment efficacy/safety of inhaled loxapine, summarizing Phase 3 evidence |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatr Dis Treat | Safety, efficacy, and patient-acceptability review of inhaled loxapine in bipolar I disorder/schizophrenia agitation |
| [28376877](https://pubmed.ncbi.nlm.nih.gov/28376877/) | 2017 | RCT design paper | BMC Psychiatry | Rationale and design of the PLACID RCT comparing inhaled loxapine vs. IM aripiprazole |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Review | Expert Opin Pharmacother | Review on improving pharmacotherapy of agitation associated with bipolar disorder, including loxapine |

---

## Germany Market Information

Loxapine is currently **not marketed in Germany** (0 authorizations on record in the evidence pack). No product license table is available at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: `key_warnings`, `contraindications`, and drug interaction data are all flagged as data gaps in this evidence pack (DG001, severity: **Blocking**). This gap currently prevents entry into the S1 safety pre-screening stage and must be resolved before further progression.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic rationale is strong and the evidence level is L1 — inhaled loxapine already carries regulatory approval in the US and EU for acute agitation in bipolar I disorder, supported by two pivotal Phase III RCTs and a head-to-head trial (PLACID). This makes the prediction a near-label extension rather than a speculative hypothesis.
- However, the drug is not currently marketed in Germany and safety/contraindication data is a **Blocking** gap, so the recommendation cannot advance to full Go status without remediation.

**To proceed, the following is needed:**
- TFDA/German-market package insert warnings and contraindications (DG001 — Blocking; required before S1 safety pre-screening)
- Formal DrugBank MOA record (DG002 — High priority)
- Structured entry of the two pivotal Phase III trials (NCT00628589, NCT00721955) and the PLACID trial into the clinical trial evidence registry
- Route compatibility assessment — the approved indication relies on the inhaled Staccato delivery device (Adasuve); confirm whether this specific formulation, not just oral loxapine, is the intended repurposing candidate
- Regulatory pathway assessment for market entry, given zero existing authorizations in Germany

---

*Note: Ranks 2–10 of the predicted indications for this drug (retinal dystrophy, hydranencephaly, X-linked myopia variants, congenital glycosylation disorder, CMT type 1G, polymicrogyria syndrome, syndromic myopia, atypical glycine encephalopathy) were all scored **L5 / Hold** — no supporting literature or trials, and no plausible pharmacological link to loxapine's D2/5-HT2A mechanism. These are assessed as knowledge-graph embedding noise (likely driven by a shared rare-disease/ophthalmologic co-occurrence cluster) and require no further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

