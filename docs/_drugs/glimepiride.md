---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a second-generation sulfonylurea, pharmacologically classified as an insulin secretagogue used to manage type 2 diabetes mellitus. The TxGNN model assigns a high prediction score to **Focal Stiff Limb Syndrome**, an autoimmune, GABAergic neurological disorder, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack explicitly flags the mechanistic link as unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on known pharmacological classification as a sulfonylurea; no formal regulatory indication text available in this dataset) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glimepiride was not directly available in the structured evidence pack (`original_moa` = Data Gap). However, based on known pharmacological classification, glimepiride is a second-generation sulfonylurea that binds SUR1 subunits to close ATP-sensitive K⁺ channels on pancreatic β-cells, promoting insulin secretion.

Focal Stiff Limb Syndrome (a localized variant of Stiff Person Syndrome) is an autoimmune neurological disorder driven by anti-GAD65 antibodies and impaired GABAergic neurotransmission. While ATP-sensitive K⁺ channels are also expressed in central neurons, there is currently no evidence that sulfonylurea-class drugs modulate GABAergic signaling or autoimmune GAD65-mediated pathology. The evidence pack itself characterizes this as a "high TxGNN score without a mechanistic basis" — i.e., the predicted link appears to be a graph-embedding artifact rather than a biologically grounded hypothesis.

Given the absence of mechanistic plausibility, clinical trial data, and literature support, this candidate should be interpreted as a low-confidence model output rather than a scientifically substantiated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Glimepiride is not currently marketed in the jurisdiction covered by this regulatory dataset (market status: 未上市 / Not Marketed; 0 authorizations on record). No license or product information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Focal Stiff Limb Syndrome) carries an L5 evidence level — a TxGNN score with no supporting clinical trials, literature, or plausible mechanistic connection to glimepiride's known sulfonylurea pharmacology. Combined with the drug's non-marketed status in this jurisdiction and blocking safety data gaps, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed drug label / warnings and contraindications from the local regulatory authority (currently a Blocking data gap — required before any S1 safety evaluation)
- Verified mechanism of action data from DrugBank or primary literature (High-severity data gap)
- Independent mechanistic or preclinical evidence linking sulfonylurea pharmacology to GABAergic/autoimmune neurological pathology, if this indication is to be pursued further
- Monitoring of lower-ranked candidates (e.g., thiamine-responsive dysfunction syndrome, rank 4) which show a somewhat more plausible — though still unverified — link to insulin secretion pathways, and may warrant a lower-priority literature search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

