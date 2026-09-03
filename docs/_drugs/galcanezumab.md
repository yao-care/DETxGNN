---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor II Deficiency

## One-Sentence Summary

Galcanezumab is a CGRP (calcitonin gene-related peptide)-targeting monoclonal antibody; per the mechanistic notes in this evidence pack, it is used for migraine prevention (this is not confirmed by German/Taiwan regulatory records, as the product is not currently marketed there). TxGNN predicts a possible association with **Heparin Cofactor II Deficiency**, but the prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known biological mechanism connecting the two conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory data (mechanism notes reference migraine prevention, unconfirmed) |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on the mechanistic notes accompanying this evidence pack, Galcanezumab is an anti-CGRP monoclonal antibody that blocks pain signaling in the trigeminovascular system, and its established use is migraine prevention.

The three TxGNN-predicted indications in this evidence pack — heparin cofactor II deficiency, antithrombin deficiency type 2, and factor V excess with spontaneous thrombosis — are all rare, genetically-driven coagulation/thrombophilia disorders (SERPIN or coagulation factor gene defects). None of these involve the CGRP signaling pathway, and the evidence pack's own rationale explicitly states there is **no known shared molecular pathway, receptor, or downstream signaling overlap** between CGRP antibody pharmacology and coagulation cascade regulation.

In other words, this is a case where the TxGNN model assigned high similarity scores (>99%) without an identifiable biological mechanism to support them. This pattern — high score, zero real-world evidence, and an explicit mechanistic disclaimer — should be treated as a candidate requiring further scrutiny rather than a promising repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Galcanezumab is not currently marketed in Germany (0 authorizations on file in this evidence pack).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications (heparin cofactor II deficiency, antithrombin deficiency type 2, factor V excess with spontaneous thrombosis) lack any supporting clinical trials or literature, and the model's own mechanistic rationale states there is no biologically plausible link between CGRP-targeted therapy and these coagulation disorders. Combined with the drug's unconfirmed original indication and lack of market presence in Germany, there is insufficient basis to advance any of these candidates.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data (from DrugBank API or manufacturer labeling, per DG002)
- Package insert warnings/contraindications (TFDA/BfArM label parsing, per DG001 — currently blocking safety review)
- Any preclinical or mechanistic literature specifically linking CGRP pathway modulation to coagulation factor regulation, before this candidate can move beyond S0
- Reassessment of whether these three predictions represent a systematic TxGNN scoring anomaly (e.g., rare-disease embedding artifact) rather than genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

