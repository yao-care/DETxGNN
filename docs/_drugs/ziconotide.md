---
layout: default
title: Ziconotide
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Ziconotide
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

# Ziconotide: From an Undocumented Original Indication to Predicted Migraine Disorder

## One-Sentence Summary

> Ziconotide (DrugBank DB06283) is an N-type (Cav2.2) voltage-gated calcium channel blocker; its officially approved indication and mechanism-of-action text are not available in this evidence pack, and the drug is currently **not marketed in Germany**.
> The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of **99.92%**, but this is currently supported by only **0 clinical trials** and **1 case report**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available — drug is not marketed in Germany, no approved indication text on record (data gap) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as data gap DG002, severity High). Based on the literature captured for this candidate, ziconotide is described as an N-type (Cav2.2) voltage-gated calcium channel blocker, administered intrathecally for the management of severe chronic pain — this description comes from a case report (PMID 26392785) rather than an official label source, and should be treated as supporting context only, not confirmed prescribing information.

The proposed rationale for migraine is mechanistic rather than clinical: N-type calcium channels in the dorsal horn regulate release of substance P and CGRP, and CGRP signaling is central to the pathophysiology of migraine via the trigeminovascular system. In theory, intrathecal calcium channel blockade could dampen this pain-signaling pathway. However, this remains a single-case, hypothesis-generating observation — there is a substantial practical gap between ziconotide's only approved route of administration (implanted intrathecal pump) and standard migraine treatment practice (oral, injectable, or nasal therapies), which limits real-world applicability even if the mechanistic hypothesis is directionally correct.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Case Report | Journal of Pain Research | Single case of resolution of chronic migraine headaches following intrathecal ziconotide, framed as an off-label observation in a chronic severe pain patient |

---

## Germany Market Information

No authorizations on record. Ziconotide is currently **not marketed in Germany** (`market_status: 未上市`, `total_licenses: 0`), so no product/indication table can be generated from this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: The safety module in this evidence pack (key warnings, contraindications, drug–drug interactions) is entirely unpopulated and flagged as a **Blocking** data gap (DG001 — TFDA/German label warnings and contraindications). This means a formal S1 safety pre-assessment cannot be completed until label data is retrieved.*

---

## Additional Note on Lower-Ranked Predictions

Nine other TxGNN-predicted indications (migraine with brainstem aura, cauda equina syndrome, obesity, TIA, glaucoma subtypes, neurogenic bladder, migraine susceptibility, preeclampsia) were also generated, all at evidence level L5 (model prediction only, no clinical trials or directly relevant literature) and all marked **Hold**. One of these — **cauda equina syndrome** — warrants explicit caution: this condition is a known adverse-event association with intrathecal ziconotide pump therapy, not a therapeutic target. It should be treated as a safety signal artifact from the knowledge graph rather than a repurposing candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (migraine disorder) rests on a single case report with no supporting clinical trials, and the drug's original indication, MOA, and safety label data are all missing from this evidence pack — including a **Blocking**-severity gap that prevents even a preliminary safety assessment (S1). The only approved route (intrathecal pump) is also poorly matched to standard migraine care.

**To proceed, the following is needed:**
- Retrieve official label/warnings and contraindications from the source regulatory agency (remediation for DG001) to unblock S1 safety review
- Retrieve confirmed original indication and MOA from DrugBank or official labeling (remediation for DG002)
- Identify any additional case series or preclinical mechanistic studies specifically linking N-type calcium channel blockade to migraine pathophysiology
- Evaluate feasibility of route-compatible delivery (current evidence is intrathecal-only; migraine treatment norms require non-invasive routes) before considering further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

