---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Fremanezumab
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

> Fremanezumab is a humanized anti-CGRP monoclonal antibody established as a preventive treatment for episodic and chronic migraine.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**,
> a rare migraine subtype that is typically excluded from pivotal trials, currently supported only by preclinical mechanistic studies, case reports, and general-migraine real-world cohorts — **no dedicated clinical trials or subtype-specific RCTs exist yet**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic/chronic migraine) — inferred from supporting literature; official Taiwan regulatory license text unavailable |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (preclinical/mechanistic + non-subtype-specific observational studies) |
| Taiwan Market Status | Not yet marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed drug-specific mechanism-of-action data is not currently available for fremanezumab (data gap). Based on published literature, fremanezumab is a fully humanized IgG2Δa monoclonal antibody that selectively binds and neutralizes calcitonin gene-related peptide (CGRP), a neuropeptide central to migraine pathophysiology through trigeminovascular activation and vasodilation.

Migraine with brainstem aura (formerly basilar-type migraine) is a subtype of migraine with aura, and CGRP is broadly implicated across migraine subtypes. This provides a plausible rationale for extending fremanezumab's use beyond typical episodic/chronic migraine into aura-associated subtypes.

However, two preclinical animal studies (PMID 31127003, 31895266) specifically show that fremanezumab does **not** prevent the onset of cortical spreading depression (CSD) — the physiological correlate of aura — and only modestly affects its propagation/recovery parameters. This suggests the mechanistic link is to downstream headache symptoms rather than to the aura mechanism itself, making the connection moderate rather than direct. Clinically, patients with hemiplegic and brainstem-type migraine are systematically excluded from major anti-CGRP RCTs, so current supporting evidence comes from case reports, small case series, and post-hoc/observational subgroup analyses rather than dedicated trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | RCT post-hoc subgroup (Phase 3b FOCUS) | European Journal of Neurology | Fremanezumab showed efficacy and QoL improvement in difficult-to-treat migraine patients with/without aura or associated neurological dysfunction |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Report/Review | Journal of Clinical Medicine | Reviews evidence on anti-CGRP mAbs (incl. fremanezumab) for migraine aura specifically; notes scarce data on aura prevention despite proven headache efficacy |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual patient quantitative analysis | The Journal of Headache and Pain | Anti-CGRP mAbs show effectiveness/safety signals in hemiplegic migraine, a related aura subtype systematically excluded from RCTs |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report/Review | Frontiers in Neurology | Case of hemiplegic migraine responding to anti-CGRP mAb; literature review of limited existing data |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational case series | CNS Neuroscience & Therapeutics | Anti-CGRP-targeted therapy's effect on migraine aura evaluated; limited clinical evidence noted |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Observational | Cephalalgia | Evaluates effect of anti-CGRP mAbs (incl. fremanezumab) on central/prodromal migraine symptoms |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Cohort (real-world) | Frontiers in Neurology | Confirms real-world efficacy/tolerability of fremanezumab in chronic migraine (general population, not aura-specific) |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical/Animal | The Journal of Neuroscience | Fremanezumab does not block CSD-induced arterial dilation/plasma extravasation, questioning direct CGRP role in aura mechanism |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical/Animal | Pain | Fremanezumab slows CSD propagation and shortens cortical recovery but does not prevent CSD occurrence |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handbook of Experimental Pharmacology | Foundational review of CGRP's role across migraine subtypes, supporting general mechanistic rationale |

---

## Taiwan Market Information

Fremanezumab is **not currently marketed in Taiwan** (0 authorizations on record). No license/product data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are marked as data gaps in the current evidence pack — see DG001 below.)

---

## Secondary Prediction (Not Actionable)

The evidence pack also includes a rank-2 prediction, **atrophoderma vermiculata** (a rare follicular keratotic skin disorder), with TxGNN score 99.04% but **zero supporting clinical trials or literature**. There is no known mechanistic link between the CGRP pathway and this dermatologic condition. This is assessed as a likely knowledge-graph false positive (Evidence Level L5) and is **not recommended for further evaluation**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The CGRP–migraine mechanistic link is well established, and post-hoc/observational data suggest benefit in aura-associated migraine subgroups. However, no dedicated clinical trials exist for migraine with brainstem aura specifically, preclinical data suggest fremanezumab does not block the core aura mechanism (CSD), and this patient population is systematically excluded from pivotal RCTs. Combined with missing Taiwan regulatory safety data, the evidence is not yet sufficient to proceed.

**To proceed, the following is needed:**
- **[Blocking]** Taiwan (TFDA) package insert data — warnings, contraindications, DDI (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A dedicated prospective or registry study in migraine-with-brainstem-aura patients (currently excluded from RCTs)
- Clarification of regulatory pathway, since the drug is not yet marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

