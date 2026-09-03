---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: Original Indication Not Specified → Primary Hereditary Glaucoma

## One-Sentence Summary

> Latanoprost's original indication is not documented in the current evidence pack (data gap), and its detailed mechanism of action (MOA) record is also missing.
> The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
> supported by **1 completed Phase 2 clinical trial** and **no dedicated literature** currently on file.
> Notably, the trial-provided mechanistic rationale indicates this predicted indication largely overlaps with latanoprost's already-known ocular pharmacology (intraocular pressure lowering via uveoscleral outflow), so this is less a novel repurposing hypothesis and more a confirmation/extension within a related patient population (hereditary/pediatric glaucoma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap; no licenses or original_indications on file) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original MOA data for latanoprost is not available in this evidence pack. However, the repurposing rationale associated with the top prediction states that latanoprost is a **prostaglandin F2α analogue** that lowers intraocular pressure (IOP) by increasing uveoscleral (trabecular) outflow of aqueous humor. This is described as its core pharmacological mechanism.

Primary hereditary glaucoma — like other glaucoma subtypes — is pathophysiologically defined by impaired aqueous humor outflow leading to elevated IOP and subsequent optic nerve damage. Because latanoprost's known mechanism directly targets aqueous outflow, the predicted indication is mechanistically **congruent** rather than a distant extrapolation. As the evidence pack itself notes, "this indication substantially overlaps with the drug's known mechanism of action, and does not represent a novel mechanistic extrapolation."

The supporting clinical trial (NCT01527682) reinforces this: it tested latanoprost (combined with dorzolamide, a carbonic anhydrase inhibitor) specifically in **pediatric glaucoma refractory to surgery**, a population closely related to primary hereditary glaucoma. This strengthens plausibility, though the trial does not exactly match the "hereditary" subtype label, and no additional literature currently corroborates the finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed ocular hypotensive efficacy and safety of latanoprost + dorzolamide in pediatric glaucoma patients refractory to surgical procedures; direct head-to-head style evaluation of latanoprost's IOP-lowering effect in a glaucoma population closely related to the predicted indication. |

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorization records are available — latanoprost is currently **not marketed** in Germany per this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack; DrugBank/TFDA label extraction is flagged as a blocking data gap — DG001.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A single completed Phase 2 trial (L2 evidence) directly supports latanoprost's IOP-lowering effect in a glaucoma population mechanistically aligned with the predicted indication, but the drug is not currently marketed in Germany, and critical safety/labeling data are missing.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — currently blocking (DG001)
- Formal DrugBank-sourced MOA documentation (DG002)
- Confirmation of original approved indication(s), since none are currently on file
- Additional trials or literature specific to *hereditary* (vs. general pediatric) glaucoma subtypes to close the label-match gap
- Route/formulation compatibility assessment once market status is clarified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

