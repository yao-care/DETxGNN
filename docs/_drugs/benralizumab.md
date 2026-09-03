---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
---

# Benralizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benralizumab: Evaluating Thrombocytopenia due to Immune Destruction as a New Indication

> Note: The evidence pack does not contain data on benralizumab's original approved indication (`drug.original_indications` is empty and `taiwan_regulatory.licenses` is empty). This report therefore does not state an original indication, to avoid presenting unverified information.

## One-Sentence Summary

> Benralizumab's original approved indication is not documented in this evidence pack, and the drug currently has no marketing authorization in this jurisdiction (0 licenses, not marketed).
> The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal (L5) with an explicitly flagged mechanistic mismatch.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack |
| Predicted New Indication | Thrombocytopenia due to Immune Destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action record is available for benralizumab in this evidence pack (`original_moa` = Data Gap). Based on the model's own repurposing rationale, benralizumab is described as an anti-IL-5Rα monoclonal antibody that depletes eosinophils and basophils primarily through antibody-dependent cell-mediated cytotoxicity (ADCC).

Immune thrombocytopenia (ITP), by contrast, is driven pathologically by autoantibody-coated platelets being cleared via Fc-receptor-mediated phagocytosis, together with dysregulated T- and B-cell responses. There is no established direct link between the IL-5/eosinophil axis and platelet autoantibody clearance.

The evidence pack's own mechanistic assessment is explicit on this point: the high TxGNN score most likely reflects indirect proximity between benralizumab and ITP through a shared "immune modulation" node in the knowledge graph, rather than a specific, biologically validated pathway. In other words, the model signal exists, but there is currently no mechanistic or clinical basis connecting IL-5Rα blockade to ITP pathophysiology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Germany Market Information

No marketing authorizations are on record. The drug's market status is listed as **not marketed** with **0 total licenses**, so no product/dosage-form information is available for this jurisdiction.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack; a formal TFDA/regulatory-label safety review has not yet been completed — see Blocking data gap DG001 below.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at decision stage S0 with evidence level L5 — a model prediction with no supporting clinical trials, no supporting literature, and no marketed formulation in this jurisdiction. The evidence pack's own mechanistic analysis further indicates the prediction likely reflects indirect knowledge-graph proximity rather than a validated biological pathway between IL-5Rα blockade and ITP.

**To proceed, the following is needed:**
- Package insert safety data (warnings/contraindications) — currently a **Blocking** gap (DG001); without this, the candidate cannot advance to S1 safety pre-assessment
- Verified mechanism-of-action data via DrugBank — currently a **High**-severity gap (DG002), needed to properly evaluate mechanistic plausibility
- Preclinical or case-level evidence directly linking eosinophil/IL-5Rα biology to ITP pathophysiology
- At minimum, case reports or observational data before this indication can be re-scored above L5

---

**Additional note (context, not part of the primary evidence chain):** Among the other TxGNN-predicted indications for benralizumab in this evidence pack, **dermatitis** (rank 2, score 99.16%) has substantially more evidence — 6 clinical trials and 20 publications, reaching evidence level L2/decision stage S1. However, the evidence is net-negative: the pivotal Phase 2 HILLIER trial (NCT04605094) was **terminated for insufficient efficacy**, and a companion publication (PMID 37178404, "Lack of effect of benralizumab on signs and symptoms of moderate-to-severe atopic dermatitis") confirms that eosinophil depletion in skin lesions (PMID 40781582) did not translate into clinical benefit. This indication is also scored **Hold**, but for a different reason — mechanism confirmed, efficacy disproven — rather than for lack of data. If evaluating benralizumab repurposing broadly, this dermatitis outcome is more informative than the ITP signal above and may warrant a separate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

