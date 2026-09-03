---
layout: default
title: Verteporfin
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using no skill — this is a direct report-generation task per explicit formatting instructions already supplied.

# Verteporfin: From Choroidal Neovascularization to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

> Verteporfin is a photosensitizing agent originally used in photodynamic therapy (PDT) for choroidal neovascularization (e.g., wet age-related macular degeneration).
> The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
> but this prediction is currently supported by **no clinical trials and no literature** — it is a model-only signal (L5) and requires manual mechanistic review before any further action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Choroidal neovascularization / wet age-related macular degeneration (photodynamic therapy) — based on known clinical use, not present in the supplied license data |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% (rank 5945) |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack (flagged as a Blocking/High-severity data gap — see Next Steps). Based on known information, verteporfin acts as a light-activated photosensitizer, generating reactive oxygen species upon laser activation to selectively damage neovascular endothelium — this is the basis of its approved use in PDT for choroidal neovascularization. Separately from its light-dependent activity, verteporfin has also been studied as a non-light-dependent inhibitor of the YAP/TAZ transcriptional co-activators in the Hippo signaling pathway, which has drawn interest in oncology and anti-fibrotic research.

Neither of these known mechanisms — photodynamic vascular ablation or YAP/TAZ inhibition — has an established biochemical link to nuclear-DNA-encoded oxidative phosphorylation (OXPHOS) complex assembly or function, which is the defect underlying the predicted indication. The very high TxGNN score (99.49%) most likely reflects **topological similarity in the knowledge graph** (e.g., shared genes, pathways, or co-occurring drug/disease neighbors) rather than a substantiated pharmacological rationale. This prediction should be treated as a hypothesis-generating signal only, pending manual review of the underlying knowledge graph paths and any mitochondrial-relevant pharmacology data for verteporfin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Verteporfin is currently **not marketed** in Germany, and no marketing authorizations are recorded in the evidence pack (total_licenses = 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by zero clinical trials and zero literature (L5, model-only), and no established mechanistic pathway connects verteporfin's known pharmacology to nuclear-DNA-related OXPHOS disorders. Without any product currently marketed in Germany and with a Blocking safety data gap (no TFDA/label warnings retrieved), this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA label warnings, contraindications, and DDI data (currently Blocking — DG001)
- Retrieve verified drug MOA data from DrugBank or primary literature (currently High severity — DG002)
- Manual review of the TxGNN knowledge-graph path(s) driving this prediction, to distinguish genuine mechanistic signal from graph topology artifact
- Preclinical/mechanistic evidence (e.g., mitochondrial function assays) before considering any clinical hypothesis generation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

