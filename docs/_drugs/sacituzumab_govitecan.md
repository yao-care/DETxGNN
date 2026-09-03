---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Sacituzumab Govitecan: From Original Indication Not on File to Drug-Induced Osteoporosis

## One-Sentence Summary

The original indication and mechanism of action for sacituzumab govitecan are not available in the current dataset. Based on the repurposing rationale provided, this drug is a Trop-2-targeted antibody-drug conjugate (ADC) delivering SN-38, a cytotoxic topoisomerase I inhibitor. The TxGNN model predicts possible efficacy for **drug-induced osteoporosis**, but with **no clinical trials and no literature** currently supporting this direction — this is a model-prediction-only signal (L5) that the rationale itself flags as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (drug not yet marketed; no approved indication on file) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for sacituzumab govitecan. Based on the repurposing rationale supplied with this evidence pack, the drug is a Trop-2-targeted antibody-drug conjugate whose payload, SN-38 (the active cytotoxic metabolite of irinotecan), is a topoisomerase I inhibitor — a conventional cytotoxic chemotherapy agent. No original indication is on file in this dataset, so a direct comparison between the original and predicted indication cannot be made.

More importantly, the rationale text itself argues **against** biological plausibility for this prediction: there is no known mechanistic link between Trop-2/SN-38 activity and bone remodeling pathways (RANKL/OPG signaling, osteoclast–osteoblast balance). The TxGNN score of 99.78% appears to reflect a graph-embedding association rather than a mechanistically grounded hypothesis. Additionally, the drug's known toxicity profile — myelosuppression and severe diarrhea — represents a disproportionate risk for a non-life-threatening condition like osteoporosis, making the risk-benefit case unfavorable even if a mechanistic link were later established.

Given the absence of supporting clinical trials, literature, and mechanistic rationale, this prediction should be treated as a low-confidence, exploratory signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

This drug is currently not marketed in the jurisdiction covered by this dataset (0 authorizations on file). No product authorization records are available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ADC) with conventional cytotoxic payload — SN-38, a topoisomerase I inhibitor (active metabolite of irinotecan) |
| Myelosuppression Risk | High — the repurposing rationale explicitly cites myelosuppression as part of the known toxicity profile |
| Emetogenicity Classification | Moderate (typical for irinotecan/SN-38-class topoisomerase I inhibitors) |
| Monitoring Items | CBC with differential (especially neutrophil count), assessment for diarrhea/dehydration, renal and hepatic function |
| Handling Protection | Yes — as a cytotoxic ADC, institutional hazardous/cytotoxic drug handling, reconstitution, and disposal protocols apply |

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings and contraindications for this candidate have not yet been collected (a blocking data gap), and formal S1 safety review cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four top-ranked TxGNN predictions for this drug (drug-induced osteoporosis, severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract) are L5 (model-prediction-only), and each is explicitly flagged in its own repurposing rationale as lacking mechanistic plausibility and clinical/literature support. The drug's known cytotoxic payload profile (myelosuppression, severe diarrhea) creates an unfavorable risk-benefit balance for all four candidate indications, none of which are life-threatening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap) — required before any S1 safety review
- Confirmed mechanism of action and the drug's original approved indication(s)
- Preclinical or mechanistic evidence specifically linking Trop-2/SN-38 activity to bone metabolism or retinal/lens pathology, if this repurposing direction is to be pursued further
- Given the poor biological plausibility across all four ranked predictions, consider deprioritizing this candidate pending new mechanistic evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

