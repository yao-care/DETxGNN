---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Cerebral Artery Occlusion

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 (AT1) receptor blocker (ARB class) established for blood pressure control, though this evidence pack does not contain a formally documented original indication or structured MOA record.
Among TxGNN's top 10 predicted indications, the model's highest-scoring output (**Prinzmetal angina**, 99.98%) is explicitly flagged within the evidence pack itself as lacking mechanistic or empirical support and is not carried forward.
The most evidence-supported candidate is **Cerebral Artery Occlusion**, backed by **1 completed Phase 4 RCT (n=1,228)**, **2 terminated sub-studies with minimal enrollment**, and **17 preclinical/mechanistic publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records returned (see MOA note below) |
| Predicted New Indication | Cerebral Artery Occlusion |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (DrugBank query gap, DG002). Based on information present in this evidence pack's own rationale annotations, telmisartan is an AT1 receptor blocker whose established antihypertensive activity underlies its cardiovascular risk-reduction profile; however, no active marketing authorization or approved-indication text for Germany was returned (0 licenses).

Blood pressure control is a recognized secondary-prevention strategy against ischemic cerebrovascular events, giving a plausible pharmacological bridge between telmisartan's known antihypertensive/cardioprotective use and cerebral artery occlusion. Beyond BP lowering, AT1 blockade has been shown in numerous rodent transient middle cerebral artery occlusion (tMCAO) models to reduce infarct volume, oxidative stress, and neuroinflammation, partly via PPARγ agonism — a pleiotropic mechanism distinct from classical ARBs (PMID 19604102, 32992165, 20498620).

Clinically, this mechanistic plausibility is supported by NCT01075698, a completed Phase 4 RCT (n=1,228) evaluating telmisartan's effect on cardiovascular/biomarker outcomes in high-risk hypertensive patients. However, the TRIDENT-related sub-studies (NCT03783754, NCT03785067) were terminated after enrolling only 4 and 1 participants respectively, substantially limiting the clinical evidence base. Given the discrepancy between the model's top-ranked (but unsupported) prediction and this better-evidenced but still limited candidate, this report treats the finding as a research question rather than a ready-to-advance indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1,228 | PROBE-design trial comparing telmisartan (ARB) vs. standard therapy on cardiovascular biomarkers and events in high-risk hypertensive patients |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study of a fixed-dose BP-lowering "Triple Pill" in prior intracerebral haemorrhage patients — terminated for insufficient enrollment |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study (CANTAB memory decline outcome) — terminated at n=1, no usable data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Review/Animal | PLoS ONE | Head-to-head comparison of telmisartan vs. ramipril for stroke prevention and neuroprotection in rat stroke models |
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Animal study | J Neurotrauma | Telmisartan reduces cerebral infarct volume and peri-infarct cPLA2 levels in experimental stroke |
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | Animal study | J Stroke Cerebrovasc Dis | Reduces progressive oxidative stress and phosphorylated α-synuclein accumulation after tMCAO |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Animal study | J Stroke Cerebrovasc Dis | PPARγ-mediated Egr-1 inhibition benefits brain injury in ischaemic stroke model |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | Animal study | J Stroke Cerebrovasc Dis | Ameliorates inflammatory responses (MCP-1, TNF-α, Iba1) after tMCAO |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | Animal study | J Stroke Cerebrovasc Dis | Long-term amelioration of metabolic syndrome-related molecules (IR, PPAR-γ, AT1R) after tMCAO |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | Animal study | J Hypertension | Low-dose telmisartan prevents ischemic brain damage via PPAR-γ activation in diabetic mice |
| [29241675](https://pubmed.ncbi.nlm.nih.gov/29241675/) | 2018 | Animal study | J Stroke Cerebrovasc Dis | Prevents learning/memory deficits via PPAR-γ in MCAO-induced vascular dementia rats |
| [18360031](https://pubmed.ncbi.nlm.nih.gov/18360031/) | 2008 | Animal study | Hypertens Res | Attenuates focal brain ischemia in atherosclerotic ApoE-deficient mice |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Animal/In silico | Toxicology Reports | Attenuates cerebral ischemia-reperfusion neurotoxicity via Nrf2/HO-1 pathway modulation |

---

## Germany Market Information

Telmisartan is currently **not marketed in Germany** — no active marketing authorization records were returned in this evidence pack (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Key warnings, contraindications, and DDI data could not be retrieved for this drug (data gap DG001, marked **Blocking**). This gap prevents a full S1 safety evaluation and must be resolved before any development decision is finalized.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN model's single highest-ranked prediction (Prinzmetal angina) has no mechanistic or empirical support and was excluded from consideration. The best-evidenced candidate found (cerebral artery occlusion, L2) rests on one completed Phase 4 trial of unclear telmisartan-specific contribution plus two severely underpowered terminated sub-studies (n=1, n=4).
- A **Blocking** data gap (missing label warnings/contraindications, DG001) prevents safety evaluation, and telmisartan has no active marketing authorization in Germany, so no regulatory pathway currently exists to build on.

**To proceed, the following is needed:**
- Retrieve and parse the German/EU product label (SmPC) for warnings, contraindications, and DDI (resolve DG001)
- Retrieve structured MOA and original-indication data from DrugBank (resolve DG002)
- Clarify telmisartan's specific role and dosing within the TRIDENT combination-pill trial (NCT02699645) versus the pill's other components
- Assess the regulatory pathway/feasibility for obtaining German marketing authorization, given zero current licenses
- If pursuing the secondary candidate (intracerebral hemorrhage, L3), similarly disentangle telmisartan's independent contribution from the combination therapy design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

