---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract Ocular Inflammation to Eye Disease

## One-Sentence Summary

> Nepafenac is a topical ophthalmic NSAID whose established use — evident throughout the clinical trial record — is the prevention and treatment of ocular inflammation and pain associated with cataract surgery.
> The TxGNN model predicts it may be effective for the broader category **Eye Disease**,
> with **39 clinical trials** and **21 publications** currently supporting this direction, most of which in fact document its *already-approved* ophthalmic use rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory license data (drug not marketed in Germany). Per the clinical trial evidence itself, nepafenac's established use is prevention/treatment of ocular inflammation and pain associated with cataract surgery. |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is a prodrug that is hydrolyzed by intraocular esterases to its active metabolite amfenac, a non-selective COX-1/COX-2 inhibitor. By suppressing prostaglandin synthesis, it reduces ocular inflammation and vascular permeability — a well-characterized mechanism directly relevant to postoperative and inflammatory eye conditions.

Critically, the evidence pack itself flags that this prediction is **not a novel repurposing hypothesis but a re-confirmation of nepafenac's existing indication**: the overwhelming majority of the supporting clinical trials (cataract surgery inflammation/pain, cystoid macular edema prophylaxis, PRK pain control) describe uses that are already part of nepafenac's known clinical profile. The "eye disease" label predicted by TxGNN is broad enough to capture this established use rather than pointing to a genuinely new therapeutic area.

Detailed mechanism of action data (`original_moa`) was not supplied in the regulatory dataset, and formal indication text is unavailable because the product is not currently marketed in Germany (0 authorizations). The mechanistic rationale above is derived from the evidence pack's own repurposing analysis rather than DrugBank MOA fields, and should be corroborated against DrugBank/label sources before use in a regulatory context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07162818](https://clinicaltrials.gov/study/NCT07162818) | Phase 4 | Completed | 61 | Direct assessment of 0.1% nepafenac on vitreous inflammatory biomarkers in rhegmatogenous retinal detachment/PVR — mechanism-level direct evidence. |
| [NCT02084576](https://clinicaltrials.gov/study/NCT02084576) | Phase 4 | Completed | 40 | Nepafenac 0.1% vs ketorolac 0.4% for prevention of cystoid macular edema after phacoemulsification. |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | Completed | 40 | Nepafenac reduces macular volume increase after epiretinal membrane surgery vs placebo. |
| [NCT00347204](https://clinicaltrials.gov/study/NCT00347204) | Phase 4 | Completed | 40 | Nevanac vs Acular LS for postoperative pain control after PRK. |
| [NCT00348582](https://clinicaltrials.gov/study/NCT00348582) | Phase 4 | Completed | N/A | Nepafenac vs ketorolac for postoperative inflammation after cataract surgery. |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1,342 | Large RCT comparing nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of ocular inflammation and pain after cataract surgery. |
| [NCT00865540](https://clinicaltrials.gov/study/NCT00865540) | Phase 4 | Unknown | 30 | Comparison of prednisolone acetate, nepafenac, and ketorolac for intra-operative mydriasis maintenance. |
| [NCT05847049](https://clinicaltrials.gov/study/NCT05847049) | N/A | Completed | 16 | Combined eplerenone + aflibercept + topical nepafenac for serous foveal detachment in CSCR. |
| [NCT01475877](https://clinicaltrials.gov/study/NCT01475877) | N/A | Completed | 20 | Bromfenac vs nepafenac for pain control and epithelial healing post-PRK. |
| [NCT01939691](https://clinicaltrials.gov/study/NCT01939691) | Phase 4 | Terminated | 9 | Difluprednate vs difluprednate+nepafenac vs prednisolone+nepafenac for uveitic macular edema; terminated, small sample. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone acetate 1% for postoperative inflammation control after micro-incisional cataract surgery. |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation control after laser peripheral iridotomy. |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic and therapeutic agents (incl. NSAIDs) for non-infectious corneal injury. |
| [16466612](https://pubmed.ncbi.nlm.nih.gov/16466612/) | 2006 | Review | Curr Med Res Opin | Expert review of ocular permeation and retinal anti-inflammatory activity of nepafenac. |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Cohort | Curr Eye Res | Intracameral nepafenac safety and efficacy in inhibiting prostaglandin synthesis during phacoemulsification. |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Cohort/Comparative | Acta Ophthalmol | Nepafenac vs preservative-free diclofenac for postoperative management in cataract surgery. |
| [25493620](https://pubmed.ncbi.nlm.nih.gov/25493620/) | 2016 | Cohort | J Glaucoma | Interaction of nepafenac with prostaglandin analogs in POAG patients (IOP effects). |
| [19897019](https://pubmed.ncbi.nlm.nih.gov/19897019/) | 2010 | Preclinical/Mechanistic | Brain Res Bull | Nepafenac/amfenac inhibit retinal angiogenesis in vitro and in a rat OIR model. |
| [24697218](https://pubmed.ncbi.nlm.nih.gov/24697218/) | 2014 | Preclinical | J Pharm Pharmacol | Effects of topical indomethacin, bromfenac, and nepafenac on LPS-induced ocular inflammation in rats. |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK/Distribution study | Exp Eye Res | Distribution of topical ocular nepafenac and active metabolite amfenac to the posterior segment. |

---

## Germany Market Information

No authorization records are available — nepafenac is currently **not marketed** in Germany under the reviewed regulatory dataset (0 authorizations, 0 licensed dosage forms).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in the source dataset (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all data gaps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is strong (L1, multiple completed Phase 2–4 RCTs) but largely reconfirms nepafenac's already-known role in ocular inflammation/pain management rather than revealing a genuinely new indication; the drug is also not currently marketed in Germany, so commercial and regulatory pathways still need to be established.

**To proceed, the following is needed:**
- TFDA/German package insert data on warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety assessment)
- Confirmed mechanism of action (MOA) documentation from DrugBank or the product label (**High** priority data gap)
- Clarification of why the product holds zero authorizations in Germany despite strong clinical evidence, to assess the regulatory/commercial path to market
- A sharper indication definition than the generic "eye disease" label (e.g., cystoid macular edema prophylaxis, diabetic macular edema, vitreoretinal surgery adjunct) to distinguish genuinely new signals from the existing approved use
- Separate, lower-priority evaluation of the weaker-evidence candidates in this pack (optic papillitis [L4], vitreous detachment [L3]) before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

