---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

> Simvastatin is an HMG-CoA reductase inhibitor from the statin class, established globally for treating hypercholesterolemia and dyslipidemia.
> The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia**,
> with **18 clinical trials** and **18 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia (general/primary) — not documented in local license registry for this market |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological classification, simvastatin is a member of the statin (HMG-CoA reductase inhibitor) class, its efficacy in lowering LDL-cholesterol for general hypercholesterolemia has been well established, and mechanistically this class of drug directly targets the same pathway implicated in familial hypercholesterolemia.

Familial hypercholesterolemia (FH) is caused by mutations in the LDL receptor pathway (LDLR/APOB/PCSK9) that impair hepatic clearance of LDL-cholesterol. Simvastatin's core mechanism — blocking hepatic cholesterol synthesis and upregulating LDL receptor expression — directly addresses this pathology, making it a mechanistically direct rather than speculative therapeutic target. This is corroborated by the fact that simvastatin, alone or combined with ezetimibe/PCSK9 inhibitors, has been extensively studied as background or comparator therapy across the FH clinical trial literature (e.g. the ENHANCE trial, NCT00552097).

Autosomal dominant hypercholesterolemia (rank 4 in the prediction list, score 99.36%) shares essentially the same LDLR-pathway biology as classic FH, and the two conditions largely share treatment evidence, further reinforcing the biological plausibility of this repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Large real-world re-examination study confirming clinical usefulness of Vytorin (ezetimibe/simvastatin) |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs. simvastatin in Fredrickson Type IIa/IIb dyslipidemia including heterozygous FH |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy (incl. simvastatin) in HeFH/high CV-risk patients |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab vs. placebo in heterozygous FH not adequately controlled on lipid-modifying therapy |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab in children/adolescents with HeFH on background statin therapy |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin efficacy/safety in adolescents with HeFH |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 in patients continuing statin (incl. simvastatin) therapy |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Long-term extension study of alirocumab safety/efficacy in HeFH |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial primary publication: simvastatin with or without ezetimibe in FH |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin treatment in FH reduces coronary artery disease events and all-cause mortality |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review | Cochrane Database of Systematic Reviews | Statins (including simvastatin) for children with familial hypercholesterolemia |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefits and risks assessment of simvastatin in familial hypercholesterolaemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice (AACE/ACE) | Guidelines for management of dyslipidemia and CVD prevention, statin-based |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation (ACC/AHA) | 2026 guideline on management of dyslipidemia, replacing 2018 cholesterol guideline |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in patients with familial hypercholesterolaemia |
| [21173733](https://pubmed.ncbi.nlm.nih.gov/21173733/) | 2010 | Cohort | International Angiology | Efficacy and safety of long-term ezetimibe/simvastatin treatment in FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | Journal of Clinical Medicine | Cellular immunity in children with FH treated with simvastatin |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Study | Nutrition, Metabolism and Cardiovascular Diseases | Atorvastatin vs. simvastatin in heterozygous FH: LDL-C and coagulation effects |

---

## Germany Market Information

No authorization records found — simvastatin is currently **not marketed** in this jurisdiction (0 licenses on file), so no product/dosage-form/indication table can be produced from the available registry data.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack; note that the underlying data gap for TFDA-equivalent label warnings is flagged as **Blocking** in the source evidence pack, meaning a formal S1 safety review cannot proceed without it.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between simvastatin (HMG-CoA reductase inhibition, LDL receptor upregulation) and familial hypercholesterolemia is direct and well established, and is backed by L1-level evidence — multiple completed Phase 3 RCTs (e.g. ENHANCE/NCT00552097, and the alirocumab HeFH program) using simvastatin as active/background comparator therapy. However, the drug is not currently marketed in this jurisdiction and key safety/label data are missing, so guardrails are required before any market or clinical action.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings/contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank — currently a **High**-severity data gap (DG002)
- Local regulatory/licensing status confirmation, since 0 authorizations are currently on file despite simvastatin's established global use
- Drug-drug interaction data (DDI query currently returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

