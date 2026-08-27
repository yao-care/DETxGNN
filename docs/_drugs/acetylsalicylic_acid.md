---
layout: default
title: Acetylsalicylic Acid
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 9
---

# Acetylsalicylic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acetylsalicylic Acid: From Pain/Fever Relief and Antiplatelet Prophylaxis to Migraine with Brainstem Aura

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a long-established analgesic, antipyretic, anti-inflammatory, and antiplatelet agent. The TxGNN model's top-ranked prediction for this candidate is **Migraine with Brainstem Aura**, currently supported by **0 dedicated clinical trials** and **19 relevant publications**, most of which are observational or mechanistic rather than confirmatory. Note that this evidence pack also flagged eight other candidate indications for aspirin, ranging from strong (Thrombotic Disease, L1; Thrombophilia, L2) to purely speculative (several rare dermatologic/coagulation disorders, L5) — this report focuses only on the top-ranked TxGNN prediction as specified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Analgesic / antipyretic / anti-inflammatory / antiplatelet prophylaxis (general use; no formal BfArM/TFDA license record found in this dataset) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity data gap). Based on known pharmacology, aspirin irreversibly inhibits cyclooxygenase (COX-1/COX-2), reducing thromboxane A2 (TXA2) and inflammatory prostaglandin production; this antiplatelet/anti-inflammatory action is well proven in pain, fever, and cardiovascular risk-reduction settings, and may mechanistically extend to migraine with brainstem aura.

The proposed rationale is that COX inhibition may reduce platelet activation and vascular inflammatory cascades associated with cortical spreading depression (CSD), the mechanism thought to underlie migraine aura. Because vasoconstrictive agents such as triptans are contraindicated in migraine with brainstem aura (given the theoretical risk of provoking brainstem ischemia), aspirin — which lacks vasoconstrictive activity — is mechanistically attractive as a potential alternative. Supporting this, a retrospective cohort (PMID 25729594) and an observational case series (PMID 29017164) both specifically evaluated low-dose ASA prophylaxis in migraine-with-aura populations, and a 2025 systematic review (PMID 39989443) examined antithrombotic drugs broadly as migraine preventives.

However, nearly all existing evidence comes from the general "migraine with aura" population rather than the specific brainstem-aura subtype, which carries distinct diagnostic and safety considerations (e.g., need to exclude stroke, arterial dissection, and other brainstem pathology before attributing symptoms to migraine). This gap between the studied population and the predicted indication is the main reason the evidence is rated L3 rather than higher.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura specifically.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448545](https://pubmed.ncbi.nlm.nih.gov/10448545/) | 1999 | RCT | Cephalalgia | Double-blind, double-dummy RCT (n=275) comparing IV lysine acetylsalicylate (ASA), subcutaneous sumatriptan, and placebo in acute migraine with/without aura |
| [25729594](https://pubmed.ncbi.nlm.nih.gov/25729594/) | 2014 | Retrospective Cohort | Current Health Sciences Journal | Retrospective review of 203 migraine-with-aura patients; 95 treated with low-dose ASA prophylaxis, evaluating efficacy/tolerability vs. other preventive therapies |
| [29017164](https://pubmed.ncbi.nlm.nih.gov/29017164/) | 2017 | Observational Case Series | European Neurology | Case series evaluating aspirin prophylaxis specifically in patients with migraine with aura |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Systematic review of antithrombotic drugs (including aspirin) as migraine preventive medication |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Evidence Assessment | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including aspirin among evidence-based options |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: percutaneous PFO closure in migraine with aura refractory to medical treatment; relevant to shared PFO/stroke-risk mechanisms in aura |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Case Series | Heart | Clopidogrel (antiplatelet) reduces migraine with aura after transcatheter PFO/ASD closure, supporting an antiplatelet-mechanism link to aura |
| [34384631](https://pubmed.ncbi.nlm.nih.gov/34384631/) | 2021 | Review | Revue Neurologique | Review of migraine-with-aura pathophysiology, emphasizing cortical spreading depression (CSD) as the underlying mechanism |
| [30291554](https://pubmed.ncbi.nlm.nih.gov/30291554/) | 2018 | Review | Current Pain and Headache Reports | Comparison of pathophysiology, epidemiology, and clinical management of episodic migraine with vs. without aura |
| [18806984](https://pubmed.ncbi.nlm.nih.gov/18806984/) | 2008 | Review | Der Nervenarzt | Review of preventive alternatives to beta-blockers in migraine, including antiplatelet and other prophylactic options |

## Germany Market Information

Not currently marketed in Germany under this candidate record; no BfArM authorization data available (0 total licenses on file).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this dataset — notably, TFDA/BfArM package-insert warnings and contraindications are flagged as a **Blocking** data gap (DG001), which must be resolved before any safety-based decision.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to migraine with brainstem aura is limited to observational/retrospective studies and reviews (L3) with no dedicated clinical trials, and the underlying population studied (general migraine with aura) does not precisely match the predicted brainstem-aura subtype, which carries distinct safety considerations (e.g., triptan contraindication, need to exclude stroke/arterial dissection). Combined with the missing package-insert safety data (Blocking gap), this candidate is not yet ready to proceed.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Detailed mechanism of action (MOA) data from DrugBank (DG002)
- A prospective study or trial specifically enrolling migraine-with-brainstem-aura patients (current data is drawn from broader "migraine with aura" populations)
- Clear diagnostic criteria/protocol to exclude stroke, arterial dissection, and other secondary causes before considering aspirin use in this subtype
- Confirmation of aspirin's approved dosage forms and route compatibility for this indication (currently unassessed — "pending" in route_compatibility)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

