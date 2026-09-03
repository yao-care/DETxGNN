---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a fibrate-class lipid-lowering agent whose established use, per the literature in this evidence pack, is hyperlipidemia and mixed dyslipidemia (including fasting triglyceride reduction to prevent pancreatitis). The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with **1 registered clinical trial** and **11 publications** currently associated with this indication — though only a subset of that literature studies fenofibrate directly in HoFH patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia / Mixed Dyslipidemia (per literature evidence, e.g. PMID 37979722: fenofibrate monotherapy indicated for fasting TG >500 mg/dL) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 (1 completed Phase 3 RCT registered under this indication — but see caveat below) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> **Caveat on Evidence Level**: The single completed Phase 3 trial (NCT03510715) evaluates **alirocumab**, not fenofibrate, in HoFH. It was returned because it matches the disease term, not because it tests the candidate drug. Fenofibrate-specific evidence for HoFH in this pack is limited to one historical case series (PMID 6593751) describing a single HoFH patient.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field returned as Data Gap). Based on known information from the evidence pack, fenofibrate belongs to the fibrate class of lipid-lowering agents; its efficacy in hyperlipidemia and mixed dyslipidemia has been demonstrated across decades of literature, and mechanistically it may be applicable to genetic/familial cholesterol disorders such as HoFH.

HoFH and the other TxGNN-predicted indications in this pack (hyperlipoproteinemia, familial hypercholesterolemia, CETP deficiency, CYP7A1 deficiency, hepatic triglyceride lipase deficiency, autosomal dominant hypercholesterolemia) are not a departure from fenofibrate's known pharmacology — they are all genetic or rare subtypes within the same broader dyslipidemia disease family the drug already treats. This is reflected in the pack itself: multiple older studies (e.g., PMID 3924068, PMID 3829426, PMID 2918846) directly document fenofibrate's lipid-lowering effect in heterozygous FH patients, and one case series (PMID 6593751) includes a HoFH patient showing the greatest LDL-C reduction in the cohort.

The rationale therefore is less "novel repurposing" and more "TxGNN correctly recognizing a drug already active in an adjacent, more specific disease phenotype." However, dedicated prospective evidence of fenofibrate specifically in HoFH is thin — modern HoFH trials in this pack (alirocumab) reflect current standard-of-care shifting toward PCSK9 inhibitors and MTP inhibitors (e.g., lomitapide, PMID 24734312) rather than fibrate monotherapy, which is consistent with fenofibrate now serving as adjunct/triglyceride-focused therapy rather than a primary HoFH treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluates alirocumab (not fenofibrate) Q2W in children/adolescents (8–17y) with HoFH on top of background lipid-lowering treatment; assesses LDL-C reduction at 12, 24, 48 weeks. Included for disease-term relevance only — does not test fenofibrate directly. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Case series | Pharmacological Research Communications | 22 type II hyperlipoproteinemic patients treated with fenofibrate 300mg/day; one HoFH patient showed the greatest fall in total and LDL cholesterol among the cohort. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK study | Pharmacotherapy | Characterizes PK interaction between lomitapide (MTP inhibitor approved for HoFH) and commonly co-administered lipid drugs including fenofibrate. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | States fenofibrate's most definite monotherapy indication is fasting TG >500 mg/dL to prevent pancreatitis; positions fibrates among non-statin options. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | Reviews pharmacologic treatments for dyslipidemic children with FH, including fenofibrate among successful regimens. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Case report/Review | Internal Medicine Journal | Discusses liver transplantation for HoFH in the context of emerging lipid-lowering therapies; not fenofibrate-specific. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management guidelines, general framework covering fibrate-class agents. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidemia management in pregnancy; tangential to HoFH. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Overview of LDL-C reduction strategies (statins, PCSK9i); general context, not fenofibrate-focused. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe as a cholesterol absorption inhibitor; general dyslipidemia context, not fenofibrate-specific. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Reviews atorvastatin pharmacology and therapeutic potential in hyperlipidaemia; general comparator context. |

---

## Germany Market Information

Fenofibrate currently holds **no marketing authorizations** in the German dataset used for this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No product-level authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack (DG001: TFDA/BfArM label warnings and contraindications are a **Blocking** data gap — currently unable to complete an S1 safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (missing regulatory label safety/contraindication data) prevents any S1 safety pre-assessment, and the drug currently has zero marketing authorizations in Germany. In addition, the only Phase 3 trial associated with this indication tests a different drug (alirocumab), not fenofibrate — direct fenofibrate-specific evidence for HoFH is limited to a single 1984 case series.

**To proceed, the following is needed:**
- TFDA/BfArM label data: warnings, contraindications, and DDI profile (resolve DG001, Blocking)
- DrugBank MOA data to support mechanistic rationale (resolve DG002)
- Clarification of fenofibrate's German regulatory/market status, given 0 current authorizations
- Dedicated fenofibrate-specific clinical or observational evidence in HoFH (current standard of care has shifted toward PCSK9i/MTP inhibitors), to distinguish this from disease-term-matched but drug-mismatched trial evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

