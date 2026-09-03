---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam (Keppra®) is a well-established second-generation antiepileptic drug, widely used as adjunctive and monotherapy treatment for partial-onset seizures, myoclonic seizures, and primary generalized tonic-clonic seizures. The TxGNN model predicts it may also be effective for **Visual Epilepsy**, a reflex epilepsy subtype triggered by visual stimuli, with a very high prediction score (**99.98%**) but currently supported only by broadly related antiepileptic evidence rather than condition-specific trials.

> **Note on scope:** This evidence pack contains 10 TxGNN-predicted indications for levetiracetam, most of which are reflex-epilepsy subtypes (e.g., audiogenic seizures, startle epilepsy, reading seizures) that sit within the drug's already-known disease family. This report focuses on the top-ranked candidate, **Visual Epilepsy**, per the standard reporting format; see the Conclusion section for a note on the strongest alternative candidate in this pack (status epilepticus).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset seizures, myoclonic seizures, primary generalized tonic-clonic seizures (per literature evidence, e.g. PMID 21936590; official TFDA/BfArM indication text unavailable — see Data Gaps) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% (rank 544) |
| Evidence Level | L3 (systematic review / observational support, but not disease-specific — see rationale) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for levetiracetam is currently a data gap in this evidence pack. Based on the literature retrieved, levetiracetam is a second-generation antiseizure medication (ASM) that binds synaptic vesicle protein 2A (SV2A) and modulates neurotransmitter release, and it is broadly established for partial-onset seizures, myoclonic seizures, and generalized tonic-clonic seizures (PMID 21936590).

"Visual epilepsy" is a form of reflex epilepsy in which seizures are triggered by visual stimuli (e.g., flashing lights, patterns). Mechanistically, reflex epilepsies are thought to share the same cortical hyperexcitability and excitation–inhibition imbalance that levetiracetam's SV2A-mediated action addresses in other epilepsy subtypes, which provides a plausible rationale for extending its use to this condition.

However, none of the clinical trials or literature retrieved for this specific prediction directly studies "visual epilepsy" as a defined clinical entity. The evidence instead reflects levetiracetam's general use in seizure prophylaxis (intracerebral hemorrhage, TBI, neonatal seizures), migraine prevention, and psychiatric/cognitive research using visual-processing paradigms — none of which confirm efficacy in visually-triggered seizures specifically. This is a meaningful specificity gap that should be closed before further investment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Prophylactic LEV to reduce seizures and improve outcomes after intracerebral haemorrhage |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of LEV for prophylactic treatment of migraine with/without visual aura |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | LEV for control of neonatal seizures |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of new AEDs (incl. LEV) as first-choice bitherapy in focal epilepsy |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | LEV effect on hippocampal hyperactivity in psychosis, assessed via visual-scene fMRI task |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | Gene therapy trial for Canavan disease (LEV not primary intervention) |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | LEV effect on hippocampal hyperactivity in psychosis (visual-scene fMRI) |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1649 | LEV vs phenytoin for post-traumatic brain injury seizure prophylaxis (MAST trial) |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Randomized, double-blind, placebo-controlled safety study of LEV cognitive effects in children with refractory partial seizures |

**None of the above trials specifically studies visually-triggered ("visual") epilepsy** — they represent general antiepileptic and prophylactic use of levetiracetam.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3, PEACH) | The Lancet. Neurology | Prophylactic LEV did not clearly reduce acute seizure risk after intracerebral haemorrhage |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | LEV vs phenobarbital for neonatal seizures; efficacy and safety compared |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review & Meta-analysis | Neurocritical Care | LEV commonly used for seizure prophylaxis in ICH, TBI, SAH; efficacy/dosing remain unclear |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Clinical Practice Guideline | Neurocritical Care | Guidance on ASM prophylaxis (incl. LEV) in moderate-severe TBI |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review / Network Meta-analysis | Journal of Neurology | Comparative efficacy/safety of ASMs (incl. LEV) in idiopathic generalized epilepsies |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review & Meta-analysis | Epilepsy & Behavior | LEV efficacy for myoclonic seizures in idiopathic generalized epilepsy (incl. JME) |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | Open-label RCT | Seizure | Phenytoin vs LEV for acute symptomatic seizures in children with acute encephalitis syndrome |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of LEV's established indications: partial-onset, myoclonic, and primary GTC seizures |
| [30884401](https://pubmed.ncbi.nlm.nih.gov/30884401/) | 2019 | Systematic Review | Epilepsy & Behavior | LEV vs carbamazepine in rolandic epilepsy (children) |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | The New England Journal of Medicine | Initial management of seizure in adults (general reference, ASM overview) |

**None of the retrieved literature specifically addresses "visual epilepsy"** as a distinct clinical entity; the evidence base is broadly antiepileptic in nature.

## Germany Market Information

Levetiracetam is currently **not marketed** in Germany under this evidence pack's regulatory dataset, and **no authorizations (licenses)** were found (`total_licenses: 0`). No approved indication text, product names, or dosage forms are available.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are marked as data gaps in this evidence pack; DG001 — TFDA/BfArM label warnings — is flagged as a **Blocking** severity gap that must be resolved before any S1 safety pre-assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN prediction score for "visual epilepsy" is very high, but no clinical trial or publication in this evidence pack directly investigates levetiracetam for visually-triggered seizures specifically — all supporting evidence is general antiepileptic/prophylactic use extrapolated by disease-family proximity.
- Two Blocking/High-severity data gaps (TFDA/BfArM label warnings; detailed MOA) currently prevent even a basic safety pre-assessment (S1), and levetiracetam has zero market authorizations in Germany, meaning a full new regulatory pathway would be required regardless of indication.

**To proceed, the following is needed:**
- Clarify the clinical definition of "visual epilepsy" and confirm whether it maps to an established diagnostic category (e.g., photosensitive/reflex epilepsy) with a dedicated evidence base.
- Retrieve condition-specific clinical trials/literature (rather than general antiepileptic evidence) to support this indication.
- Resolve DG001 (TFDA/BfArM warnings/contraindications) and DG002 (mechanism of action) via label PDF parsing and DrugBank API query.
- Confirm German market/regulatory pathway status, since levetiracetam currently holds zero licenses in this dataset.

**Contextual note:** Within this same evidence pack, **status epilepticus** (rank 9) shows substantially stronger, disease-specific evidence — including a Phase 3 NEJM RCT (ESETT, PMID 31774955), a Lancet subgroup analysis (PMID 32203691), and multiple meta-analyses — and is already pre-scored as L1 / "Proceed with Guardrails." If a repurposing candidate for levetiracetam is being prioritized from this pack, status epilepticus is the stronger near-term candidate compared to visual epilepsy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

