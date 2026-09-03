---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 1
---

# Erenumab
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

> Erenumab is a CGRP-receptor monoclonal antibody used for migraine prevention.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**,
> a subtype historically excluded from most pivotal trials.
> Currently **0 clinical trials** are registered specifically for this subtype, but **20 publications**
> — including post-hoc vascular safety analyses and a dedicated aura-frequency study — support the mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic/chronic) — general known indication for this drug class; no Germany-approved indication text is available (0 licenses on file) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured `original_moa` field is not available in this Evidence Pack (data gap). Based on the accompanying repurposing rationale and literature, erenumab is known to act as a **CGRP-receptor monoclonal antibody**, blocking calcitonin gene-related peptide (CGRP) signaling — a pathway with well-established involvement in the neurovascular mechanism of migraine.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype of migraine, and CGRP pathway involvement is not thought to be subtype-specific. However, this subtype was typically **excluded or not separately analyzed** in the major pivotal Phase 3 RCTs (e.g., STRIVE, ARISE), because of a theoretical safety concern: CGRP blockade could interfere with compensatory vasodilation in patients whose aura symptoms are attributed to brainstem/posterior-circulation vascular mechanisms. This explains the direct-RCT evidence gap for this specific indication.

Mechanistically, the case for applicability remains reasonably strong: post-hoc and real-world vascular safety studies in aura populations (e.g., PMID 36942409, 32867533) have not identified a signal of impaired cerebral hemodynamics or endothelial dysfunction with erenumab, and a dedicated 2026 study (PMID 41888647) has directly examined erenumab's effect on aura frequency. Together, these findings support cautious extension of erenumab's mechanism to this aura subtype, while highlighting that dedicated prospective confirmation is still limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT subgroup/post-hoc analysis | JAMA Neurology | Secondary analysis of RCTs assessing erenumab safety/efficacy in migraine with vs. without aura, addressing elevated vascular risk concerns in the aura subgroup |
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT | Lancet | Pivotal randomized, double-blind, placebo-controlled trial establishing erenumab efficacy/tolerability in episodic migraine patients failing 2–4 prior preventives |
| [41888647](https://pubmed.ncbi.nlm.nih.gov/41888647/) | 2026 | Cohort (REFORM study) | J Headache Pain | Longitudinal characterization of migraine aura frequency changes during/after erenumab treatment in patients with prospectively confirmed aura |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohort (vascular risk evaluation) | Headache | Post-hoc analysis of pooled long-term trial data assessing cardiovascular safety of erenumab by degree of CV risk in aura vs. non-aura patients |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Cohort (hemodynamic study) | Cephalalgia | Found erenumab does not alter cerebral vasomotor reactivity or flow-mediated dilation, addressing theoretical vascular safety concerns |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic review | Int Immunopharmacol | Systematic review of erenumab efficacy in episodic and chronic migraine prophylaxis |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Mechanistic review | Handbook Exp Pharmacol | Reviews the role of CGRP in migraine pathophysiology, underpinning the mechanistic rationale for CGRP-targeted therapy across migraine subtypes |
| [35271240](https://pubmed.ncbi.nlm.nih.gov/35271240/) | 2022 | Real-world cohort | Zhurnal Nevrologii i Psikhiatrii | Russian real-life study assessing effectiveness/safety of erenumab in high-frequency episodic migraine |
| [35538414](https://pubmed.ncbi.nlm.nih.gov/35538414/) | 2022 | Real-world cohort (12-month safety) | J Headache Pain | Retrospective real-world study on 12-month safety, tolerability and adverse-event susceptibility of erenumab |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-world cohort | Clin Neurol Neurosurg | Croatian real-world experience on effectiveness/safety of erenumab in treatment-resistant chronic migraine |

---

## Germany Market Information

Erenumab is currently **not marketed in Germany** (0 authorizations on file), so no product/authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all currently unavailable — flagged as a Blocking data gap (DG001) requiring retrieval of the official label/package insert before this candidate can proceed through formal safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CGRP-blockade mechanism is biologically well-supported for migraine broadly, and available post-hoc/real-world vascular safety data in aura populations are reassuring, but this specific subtype (brainstem aura) has no dedicated RCT evidence — largely because it was excluded from pivotal trials over historical theoretical vascular-safety concerns — placing this candidate at Evidence Level L3.

**To proceed, the following is needed:**
- Official package insert / label data (warnings, contraindications) to close the Blocking data gap (DG001) and enable formal safety review
- Structured mechanism-of-action documentation (DG002) to strengthen the mechanistic linkage analysis
- A dedicated prospective study or registry specifically enrolling migraine-with-brainstem-aura patients, given this subgroup's historical exclusion from pivotal RCTs
- Clarification of regulatory pathway/timeline, since erenumab currently has no market authorization in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

