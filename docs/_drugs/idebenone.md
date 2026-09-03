---
layout: default
title: Idebenone
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Idebenone
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

Using no additional skill — this is a direct report-generation task per the provided template, not a coding/debugging workflow.

# Idebenone: Investigational Repurposing Toward Hepatic Porphyria

## One-Sentence Summary

> The evidence pack does not document Idebenone's original approved indication or mechanism of action (both flagged as data gaps).
> The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on topological model similarity alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Idebenone in the structured evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic notes attached to the TxGNN predictions, Idebenone is described as a **coenzyme Q10 analog** with mitochondrial electron-transport and antioxidant activity — this characterization comes from the model's rationale text rather than a confirmed MOA record, so it should be treated as provisional.

The original approved indication is also undocumented (`original_indications` is empty, and no Germany market authorizations exist to infer it from). Without a confirmed original indication, it is not possible to assess mechanistic continuity between "original use" and "hepatic porphyria" in the way this report normally would.

The model's own rationale for this candidate is explicit about the weakness of the link: hepatic porphyria involves disrupted heme biosynthesis and possible secondary oxidative stress, and while Idebenone's antioxidant/mitochondrial-support properties are theoretically compatible with mitigating oxidative injury, **there is no direct evidence connecting Idebenone to porphyrin metabolism or ALA/PBG regulation**. The high TxGNN score (99.92%) reflects network/topological similarity in the model's knowledge graph, not confirmed pharmacological or clinical relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No marketing authorizations are currently registered for Idebenone in Germany (0 licenses on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — the hepatic porphyria prediction is based solely on TxGNN model topology, with zero supporting clinical trials or literature, and the model's own rationale describes the mechanistic link as indirect/theoretical. Original indication and MOA data are both missing, and the drug currently has no market presence in Germany.

**To proceed, the following is needed:**
- TFDA/BfArM label data (warnings, contraindications) — currently a **Blocking** gap (DG001); required before any S1 safety screening
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Documentation of Idebenone's original approved indication(s), to enable mechanistic-continuity analysis
- Preclinical or mechanistic studies specifically linking mitochondrial/antioxidant activity to porphyrin metabolism or heme biosynthesis regulation
- Any real-world or case-level evidence of Idebenone use in porphyria patients, if it exists outside registered trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

