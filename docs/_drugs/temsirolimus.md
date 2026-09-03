---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus: From Unspecified Oncology Indication to Liposarcoma

## One-Sentence Summary

Temsirolimus (DrugBank ID: DB06287) is an mTOR inhibitor (rapalog); however, its originally approved indication is not documented in the current evidence pack, and the drug is currently **not marketed in Germany**. The TxGNN model predicts it may be effective for **Liposarcoma**, supported by **5 clinical trials** (2 using temsirolimus directly) and **1 publication** currently on record.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no German license/indication text available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, pending DrugBank/TFDA verification). Based on the information available in this evidence pack, temsirolimus is an **mTOR inhibitor (rapalog)**. Liposarcoma — particularly the dedifferentiated and myxoid subtypes — frequently shows PI3K/AKT/mTOR pathway activation, and its downstream MDM2/CDK4 amplification signaling is often mTOR-dependent, providing a plausible mechanistic basis for repurposing.

Since the original approved indication of temsirolimus is not documented in this dataset, a direct disease-to-disease relationship cannot be established. However, same-class agents (sirolimus, ridaforolimus, everolimus) have already accumulated multiple completed Phase 2 trials in sarcoma populations, supporting a **class-effect rationale** for mTOR inhibition in this tumor type. Two of the listed trials use temsirolimus itself directly in sarcoma populations, strengthening the plausibility beyond class effect alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Combination of sirolimus (mTOR inhibitor, class-related) and cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (mTOR inhibitor, class-related), an mTOR inhibitor structurally distinct from temsirolimus, tested in advanced sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Temsirolimus combined with cixutumumab in pediatric patients with recurrent/refractory sarcoma — **direct temsirolimus evidence** |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib plus everolimus (mTOR inhibitor, class-related) in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) plus liposomal doxorubicin in advanced soft tissue and bone sarcoma — **direct temsirolimus evidence** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Reviews targeted treatment strategies for rare connective tissue tumors and sarcomas, classifying molecular subgroups relevant to targeted therapy selection |

---

## Germany Market Information

Temsirolimus is currently **not marketed in Germany**; no authorization or licensing records are available in this dataset.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed trials use temsirolimus directly in sarcoma populations (one Phase 2 pediatric trial, n=46; one Phase 1/2 trial, n=24), reaching Evidence Level L2, while additional Phase 2 trials support a broader mTOR-inhibitor class effect. However, the original indication, mechanism of action, and safety/label data are not yet documented in this dataset, so the recommendation cannot advance to an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/BfArM label warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action documentation from DrugBank (currently a High-severity data gap)
- Verification of the drug's original approved indication (not documented; drug not currently marketed in Germany)
- Larger-scale, temsirolimus-specific (not class-effect) Phase 2/3 trials in liposarcoma to strengthen direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

