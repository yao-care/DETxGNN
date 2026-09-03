---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Tacrolimus (topical) was originally developed for atopic dermatitis, where it works as a non-steroidal calcineurin inhibitor.
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **2 clinical trials** and **20 publications** currently supporting this direction, including a Phase 3 and a Phase 4 completed trial specifically designed for facial seborrheic dermatitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis (topical formulation; per repurposing rationale — structured `original_indications` field itself is empty in the evidence pack) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action (MOA) data is currently a documented data gap (DG002, High severity). However, the evidence pack's repurposing rationale contains established mechanistic reasoning: tacrolimus is a **calcineurin inhibitor**. It suppresses T-cell activation and downstream inflammatory cytokine release, which is the basis for its approved use in atopic dermatitis.

Seborrheic dermatitis shares a similar inflammatory pathophysiology with atopic dermatitis — it involves an exaggerated immune-inflammatory response to *Malassezia* yeast colonization combined with impaired skin barrier function. Because tacrolimus dampens this T-cell-mediated inflammatory cascade without causing the skin atrophy associated with long-term topical corticosteroid use, it is mechanistically well suited to chronic, relapsing facial dermatoses that require long-term maintenance therapy — exactly the profile of seborrheic dermatitis.

This is a clear "drug repurposing within dermatology" scenario: the drug is not being moved to an unrelated organ system, but extended from one chronic inflammatory facial dermatosis (atopic dermatitis) to a mechanistically related one (seborrheic dermatitis), which is reflected in the strength and volume of both clinical and observational evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated 0.1% tacrolimus ointment (Protopic®) as maintenance treatment for severe facial seborrheic dermatitis, aiming to reduce relapse frequency, prolong remission, and reduce topical steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed proactive (once/twice weekly) 0.1% tacrolimus ointment use to maintain remission and reduce exacerbation incidence in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter double-blind RCT comparing tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT | J Am Acad Dermatol | Single-blind RCT: hydrocortisone 1% ointment vs. tacrolimus 0.1% ointment for facial seborrheic dermatitis in adults |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Comparative trial | Ann Parasitol | Compared sertaconazole 2% cream vs. tacrolimus 0.03% cream efficacy in 60 seborrheic dermatitis patients |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative trial | Indian J Dermatol Venereol Leprol | Oral itraconazole (2 days) plus topical tacrolimus vs. topical tacrolimus alone for maintenance treatment of seborrheic dermatitis (Vietnam) |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort (Tier 1) | Ann Dermatol | Topical calcineurin inhibitor maintenance therapy with 0.1% tacrolimus ointment for facial seborrheic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review (Tier 1) | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, calcineurin inhibitors) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Review of topical calcineurin inhibitors' pathophysiology, safety, and efficacy in seborrheic dermatitis |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label pilot study | J Am Acad Dermatol | 18 patients treated with 0.1% tacrolimus for up to 28 days; 61% achieved complete clearance |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic Review/NMA (Tier 1) | Clin Exp Allergy | Cochrane network meta-analysis of topical anti-inflammatory treatments for eczema, relevant to calcineurin inhibitor comparative efficacy/safety |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis status and therapeutic horizons, including calcineurin inhibitors |

---

## Taiwan Market Information

Tacrolimus is currently **not marketed** in Taiwan (`market_status: 未上市`), and there are **0 registered authorizations**. No product licenses, dosage form, or approved-indication records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-drug interaction data were available in the current evidence pack — this is tracked as data gap DG001, marked "Blocking" for safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by a completed Phase 3 and a completed Phase 4 trial specifically designed for facial seborrheic dermatitis maintenance therapy, reinforced by 20 publications including multiple RCTs directly comparing tacrolimus to standard-of-care agents (hydrocortisone, ciclopiroxolamine, sertaconazole). The mechanistic rationale is also well established. However, the drug is not currently marketed in Taiwan and core safety documentation is missing, so guardrails are required before further action.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (DG001, Blocking — required before S1 safety pre-assessment can proceed)
- Structured mechanism-of-action (MOA) data from DrugBank (DG002, High)
- Regulatory pathway assessment for Taiwan market entry, given 0 current authorizations
- Formal DDI query (current query status: `not_found`) to support safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

