---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Evolocumab: From Unconfirmed Original Indication to Symptomatic Hemophilia in Female Carriers (Low-Confidence Prediction)

## One-Sentence Summary

> Evolocumab is an anti-PCSK9 monoclonal antibody; its confirmed original indication is not present in this evidence pack (data gap), though the drug's known mechanism — enhancing LDLR recycling to lower LDL-C — is referenced in the model's own rationale text.
> The TxGNN model's top-ranked prediction is that evolocumab may be effective for **symptomatic hemophilia in female carriers**, but the model's own mechanistic rationale explicitly finds **no biological plausibility** and even suggests an opposing pharmacological direction (PCSK9 inhibition tends to reduce thrombotic tendency, not promote hemostasis).
> There are **0 clinical trials** and **0 publications** supporting this prediction — this is a pure model-output signal (Evidence Level L5), with no human or preclinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap); rationale text indicates known MOA relates to LDL-C lowering via PCSK9/LDLR pathway |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for evolocumab is officially flagged as a data gap in this evidence pack (DG002, High severity). Based on the mechanistic rationale text that accompanies the prediction itself, evolocumab is an anti-PCSK9 monoclonal antibody that reduces LDL-C by preventing PCSK9-mediated degradation of the LDL receptor (LDLR), thereby increasing LDLR recycling and hepatic clearance of LDL cholesterol.

There is no known mechanistic pathway connecting PCSK9/LDLR biology to hemophilia, a disorder caused by deficiency or dysfunction of coagulation factors (e.g., Factor VIII/IX in classic hemophilia). The evidence pack's own rationale text goes further and notes that some preliminary literature suggests PCSK9 inhibition may actually **reduce** thrombotic tendency — a direction opposite to what would be therapeutically useful in a bleeding disorder. This strongly suggests the TxGNN score reflects a graph-topology artifact (e.g., shared comorbidity nodes or proxy connections in the knowledge graph) rather than a genuine pharmacological signal.

In short: this is a high-scoring model output with an explicit negative mechanistic assessment attached to it. It should not be treated as evidence of therapeutic potential without independent confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No TFDA-approved licenses are on file for evolocumab in this evidence pack (`total_licenses: 0`). The drug's market status is recorded as **未上市 (Not marketed)** in Taiwan as of the data cutoff (2026-09-03).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA label warnings and contraindications could not be retrieved for this evaluation (DG001, Blocking severity) — this gap must be resolved before any S1 safety pre-screening can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (and all five other candidates in this pack) has zero supporting clinical trials or literature, and the model's own mechanistic rationale explicitly argues against biological plausibility — in several cases citing a pharmacologically opposing direction. Additionally, a Blocking-severity data gap (missing TFDA label/warnings) prevents any safety pre-screening. There is no basis to advance past model-output-only evidence at this time.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse TFDA label PDF for warnings/contraindications
- Resolve DG002 (High): retrieve confirmed MOA and original indication(s) from DrugBank API
- If pursued further, commission a targeted literature/preclinical search specifically testing PCSK9 inhibition in bleeding-disorder models, given the rationale text's explicit concern about opposing mechanism of action
- Given all 6 ranked candidates in this pack share L5 evidence and Hold status with weak-to-negative mechanistic support, consider deprioritizing this candidate (DB09303) relative to other repurposing candidates with stronger biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

