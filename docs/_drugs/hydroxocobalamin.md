---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Hydroxocobalamin: From Vitamin B12 Deficiency to Esophageal Variceal Bleeding

## One-Sentence Summary

> Hydroxocobalamin is a vitamin B12 analogue, clinically established for B12 deficiency and as the active ingredient of the cyanide-poisoning antidote Cyanokit.
> The TxGNN model predicts it may be effective for **Esophageal Varices with Bleeding**,
> but currently **no clinical trials or publications** support this direction — the prediction rests on model score and mechanistic hypothesis alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no German market authorization in evidence pack); publicly known uses are vitamin B12 deficiency and cyanide-poisoning antidote |
| Predicted New Indication | Esophageal Varices with Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, hydroxocobalamin is a hydroxyl-form vitamin B12 analogue used for B12 deficiency and, at high doses, as a nitric oxide (NO) scavenger in the cyanide-poisoning antidote Cyanokit.

The repurposing rationale is purely mechanistic: hydroxocobalamin's NO-scavenging activity can induce vasoconstriction — a property already exploited in vasoplegic shock. Standard pharmacologic therapy for bleeding esophageal varices (terlipressin, octreotide, vasopressin) works by splanchnic vasoconstriction to lower portal pressure, so there is a theoretical pathway overlap.

However, this link is speculative. There is no animal, pharmacodynamic, or clinical evidence that hydroxocobalamin lowers portal pressure or controls variceal bleeding, and no data on its safety/metabolism in cirrhotic patients with impaired hepatic clearance. A second, closely related prediction — esophageal varices *without* bleeding (same TxGNN score) — is mechanistically even weaker, since that indication calls for chronic prophylactic pressure reduction (typically non-selective beta-blockers) rather than an acute vasoconstrictive agent, and no long-term safety data exist for this use case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Hydroxocobalamin is currently not marketed in Germany under this evidence pack; no BfArM authorization records are available (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5) and a theoretical NO-scavenging/vasoconstriction mechanism, with zero clinical trials, literature, or preclinical data confirming efficacy or safety in portal hypertension/variceal bleeding.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (currently Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action (DrugBank API query, currently High-severity data gap)
- Preclinical/pharmacodynamic evidence of portal pressure reduction with hydroxocobalamin in cirrhotic models
- Any early clinical or case-level data before advancing beyond model-prediction stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

