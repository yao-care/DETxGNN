---
layout: default
title: Orbifloxacin
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Orbifloxacin
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

# Orbifloxacin: From Veterinary Bacterial Infections to Heart Disease

## One-Sentence Summary

Orbifloxacin is a fluoroquinolone antibacterial developed for veterinary use (no confirmed human indication or MOA data in this evidence pack). The TxGNN model's top-ranked prediction is **Heart Disease**, but this candidate has **zero clinical trials** and **zero relevant literature**, and the evidence pack's own mechanistic review flags it as likely model noise — fluoroquinolones are mechanistically unrelated to heart disease and are instead known to carry cardiac safety risk (QT prolongation).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (veterinary fluoroquinolone antibacterial, per drug class) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for orbifloxacin in this evidence pack. Based on known drug class information, orbifloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV — a mechanism with no established biological link to heart disease.

More importantly, the repurposing rationale supplied with this candidate explicitly identifies the prediction as likely **model noise**: fluoroquinolones as a class are associated with a known negative cardiac safety signal (QT interval prolongation and cardiotoxicity), which is the opposite of a therapeutic rationale for heart disease. All ten of TxGNN's top-ranked predictions for this drug (heart disease, several congenital/chromosomal syndromes, valve disorders) lack any supporting clinical trial or literature evidence, and the rationale text for each independently concludes there is no plausible mechanistic connection.

Given this, the prediction should not be interpreted as a genuine repurposing signal, but rather as an artifact of the embedding space that requires no further mechanistic justification at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: one unrelated pharmacokinetic study, PMID [22029792](https://pubmed.ncbi.nlm.nih.gov/22029792/), was returned for a lower-ranked, mechanistically unrelated prediction — "disorder of fucoglycosan synthesis" — and does not support the heart disease indication.)*

---

## Germany Market Information

Orbifloxacin has no marketing authorizations in Germany (0 licenses on record); the drug is not currently marketed.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings/contraindications and DDI data are currently unavailable (flagged as a Blocking data gap in the source evidence pack), which by itself precludes any safety pre-screening for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (heart disease, score 99.94%) has no supporting clinical trials or literature, and the evidence pack's own mechanistic analysis identifies it as likely model noise, contradicted by fluoroquinolones' known cardiotoxicity risk. All other top-10 predictions are similarly unsupported congenital/genetic syndromes with no plausible link to the drug's antibacterial mechanism. The drug is also not marketed in Germany and has no confirmed human indication.

**To proceed, the following is needed:**
- TFDA/official label data (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirmed mechanism of action via DrugBank (DG002)
- Any real-world or preclinical evidence specifically linking fluoroquinolone pharmacology to cardiovascular disease before this candidate is reconsidered
- Given current findings, recommend deprioritizing this candidate in the repurposing pipeline absent new evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

