---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma/Eyelash Hypotrichosis to Alopecia (Androgenetic & Areata)

## One-Sentence Summary

> Bimatoprost is a synthetic prostamide F2α analog originally developed for **glaucoma/ocular hypertension** and later approved internationally for **eyelash hypotrichosis** (Latisse™).
> Among the ten indications TxGNN predicted for this drug, most are top-score but mechanistically implausible "knowledge-graph noise" (e.g., periodontal malformation syndromes, Dandy-Walker malformation, pulmonary AV malformation) with zero supporting trials or literature.
> The one prediction with genuine, converging evidence is **Alopecia** (androgenetic and areata subtypes), supported by **11 clinical trials** (5 graded "A" relevance) and **22 publications**, making it the only candidate worth advancing.

> ⚠️ **Note on prediction selection**: The report below is built around **Alopecia (rank 8)** rather than the TxGNN top-ranked prediction (rank 1, "malformation syndrome with odontal/periodontal component"), because rank 1–6 and rank 10 are explicitly annotated in the evidence pack itself as mechanistically unrelated and evidence-free (score ≈99.99% but 0 trials, 0 relevant literature — classic embedding-space noise). Alopecia is the only prediction meeting a real decision-stage threshold (S2).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension; Eyelash Hypotrichosis (international approval — not derived from local license data, which is absent) |
| Predicted New Indication | Alopecia (androgenetic alopecia, female pattern hair loss, alopecia areata) |
| TxGNN Prediction Score | 99.99% (rank 136 of prioritized candidates) |
| Evidence Level | L2 |
| Local Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record (DrugBank MOA field is a data gap). Based on information recoverable from the evidence pack itself, bimatoprost is a **synthetic prostamide F2α analog**. Its approved ophthalmic use for glaucoma works by increasing aqueous humor outflow; its approved dermatologic use for eyelash hypotrichosis (Latisse™) works by prolonging the **anagen (growth) phase** of the eyelash hair cycle and increasing follicle density/diameter — an effect that was originally identified as a *side effect* in glaucoma patients using prostaglandin-analog eye drops.

This anagen-prolongation mechanism is not eyelash-specific: hair follicles in the scalp undergo the same growth-cycle biology. Multiple mechanistic and clinical studies in the evidence pack (PMID 23104985, PMID 28264599, PMID 29854658) directly describe bimatoprost's off-label extension from eyelash to scalp hair growth, and this has already been tested in dedicated Phase 2 trials for androgenetic alopecia (male and female pattern hair loss) and in smaller studies/case series for alopecia areata.

In short, the original indication (eyelash hypotrichosis) and the predicted new indication (scalp alopecia) share the *same target tissue type and the same growth-cycle mechanism* — this is a mechanistically coherent, clinically plausible repurposing hypothesis, not merely a statistical prediction. This distinguishes it sharply from the other TxGNN-ranked candidates in this evidence pack, which lack any mechanistic or tissue-level connection to prostamide biology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Direct mechanistic test of bimatoprost solution on androgen-dependent scalp follicles |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | 3 doses of bimatoprost vs. vehicle vs. OTC minoxidil 2% in women with female pattern hair loss |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Safety/efficacy of bimatoprost 0.03% for eyelash hypotrichosis in children — supports approved-indication safety extension |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in men with androgenic alopecia (AGA) |
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | 3 doses of bimatoprost vs. vehicle vs. OTC minoxidil 5% in men with androgenic alopecia |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety and pharmacokinetics of new bimatoprost formulations in alopecia patients |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Local scalp pharmacokinetics/tolerability of two bimatoprost formulations in AGA |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | Combined CO2 fractional laser + bimatoprost 0.03% for alopecia areata (adjunct therapy) |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | N/A | Completed | 14 | Randomized, investigator-masked comparison of latanoprost vs. bimatoprost for eyelash regrowth in alopecia areata |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose-escalation safety/PK study of bimatoprost topical solution in male AGA (terminated, incomplete data) |

*(One additional trial, NCT00999557, was withdrawn with zero enrollment and is excluded above.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Review/Network Meta-analysis (Tier 1) | J Dermatol Treat | Systematic comparison of non-surgical AGA monotherapies; contextualizes bimatoprost among evidence-graded options |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Guideline (Tier 1) | J Dermatol | Japanese guidelines for diagnosis/treatment of male- and female-pattern hair loss |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opin Investig Drugs | Comprehensive review of bimatoprost for eyelash, eyebrow, and scalp alopecia |
| [23104985](https://pubmed.ncbi.nlm.nih.gov/23104985/) | 2013 | Review | FASEB J | Original rationale paper proposing prostamide-based glaucoma therapy (bimatoprost) as a novel scalp alopecia treatment |
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | Cohort | Arch Dermatol Res | CO2 fractional laser + bimatoprost combination therapy improves hair regrowth in alopecia areata |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Cohort/Prospective open-label | Dermatol Ther | Topical bimatoprost for eyelash loss in alopecia totalis/universalis; 16/[cohort] responders reported |
| [32642317](https://pubmed.ncbi.nlm.nih.gov/32642317/) | 2020 | Review | Dermatol Pract Concept | Review of prevention/treatment options for chemotherapy-induced alopecia, including bimatoprost |
| [34304865](https://pubmed.ncbi.nlm.nih.gov/34304865/) | 2021 | Review | Bull Cancer | Alopecia pathophysiology and treatment pathways in oncology settings |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Curr Oncol | Prevention/treatment landscape for chemotherapy-induced alopecia |
| [27377163](https://pubmed.ncbi.nlm.nih.gov/27377163/) | 2016 | Case Report | Pediatr Dermatol | Successful treatment of steroid-resistant pediatric scalp alopecia areata with topical bimatoprost |

---

## Local Market Information

Bimatoprost currently holds **0 authorizations** and is **not marketed** in this jurisdiction (`taiwan_regulatory.market_status = 未上市`). No license records are available to summarize approved indications, dosage forms, or product names.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were retrievable at this time (`safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are all marked as data gaps in the source pack).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Alopecia indication is supported by an L2 evidence level — multiple completed Phase 2 RCTs (n=244–307) directly testing bimatoprost against vehicle and active comparator (minoxidil) in both male AGA and female pattern hair loss, plus a plausible, biologically grounded mechanism already validated in the drug's approved eyelash-growth indication. This is a categorically different evidence profile from the other nine TxGNN predictions in this pack, which have zero trials, zero literature, and no coherent mechanistic rationale.

**To proceed, the following is needed:**
- Retrieve TFDA/local regulatory label (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirm formal mechanism-of-action documentation via DrugBank API — currently a **High** severity data gap (DG002)
- Formal review of the four completed Phase 2 AGA/FPHL trial results (efficacy endpoints, adverse events) before any regulatory or clinical-use recommendation
- Given no local marketing authorization exists, any advancement would require a full new-indication filing pathway, not a label-extension pathway
- Do not pursue the remaining nine TxGNN-predicted indications (ranks 1–7, 9–10) without independent mechanistic validation — current evidence indicates they are graph-embedding artifacts rather than genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

