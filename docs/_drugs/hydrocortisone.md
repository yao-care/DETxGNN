---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid Anti-Inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid long used systemically for adrenal insufficiency replacement and topically/locally for its anti-inflammatory and immunosuppressive effects across a range of dermatological and inflammatory conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **4 clinical trials** and **20 publications** currently supporting this direction, including a completed Phase 3 RCT directly comparing hydrocortisone to a higher-potency steroid in this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No structured original-indication data available in this evidence pack (DrugBank original indication field empty) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on known pharmacology, hydrocortisone belongs to the corticosteroid (glucocorticoid) class, and its efficacy as an anti-inflammatory/immunosuppressive agent across inflammatory and autoimmune skin conditions is well established in clinical practice.

For alopecia areata specifically, the mechanistic rationale is that topical corticosteroids suppress the local T-cell–mediated autoimmune attack on hair follicles — hydrocortisone is a lower-potency option within a drug class (alongside agents such as clobetasol propionate) that is already a standard dermatological treatment for this condition.

It is worth noting that this is not a truly novel repurposing signal in the traditional sense: topical hydrocortisone has long been used clinically for alopecia areata. It surfaces as a "new" prediction in this system primarily because the original indication data for this drug entry is incomplete (data gap), not because the underlying clinical use is unprecedented.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | RCT in children directly comparing clobetasol propionate 0.05% cream vs hydrocortisone 1% cream for alopecia areata; addresses the lack of high-quality evidence on which topical steroid potency is preferred. |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not Yet Recruiting | 72 | Planned 4-arm, double-blind, placebo-controlled dose-response study of hair growth formulations in mild-to-moderate androgenic alopecia; not yet enrolling. |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studies abnormal steroid metabolism and its effects on bone strength/density in patients with mild autonomous cortisol secretion; indirectly relevant (steroid physiology, not alopecia treatment). |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluates adrenal-axis effects of intralesional triamcinolone (a related corticosteroid, not hydrocortisone) in alopecia areata patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Randomized clinical trial: clobetasol propionate 0.05% vs hydrocortisone 1% for alopecia areata in children (published report of NCT01453686). |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Systematic Review/Meta-analysis | Journal of Cosmetic Dermatology | Reviews fractional laser (alone or combined) treatments for alopecia areata, contextualizing steroid and non-steroid options. |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | J Eur Acad Dermatol Venereol | Examines hypothalamic-pituitary-adrenal axis activity and cortisol production in alopecia areata patients. |
| [29227263](https://pubmed.ncbi.nlm.nih.gov/29227263/) | 2017 | Review | Georgian Medical News | Discusses adaptive neuroendocrine/immune regulatory mechanisms (cortisol, insulin) in alopecia areata pathogenesis. |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort/Case Series | Clinical and Experimental Dermatology | Retrospective single-centre analysis of topical corticosteroid treatment under occlusion for severe alopecia areata in children. |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Exploratory Clinical Study | Journal of Cosmetic Dermatology | Explores chronic psychological stress and cortisol/epinephrine release as triggers for alopecia areata and other dermatoses. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case Report | J Am Acad Dermatol | Reports 4 cases of congenital alopecia areata, including topical steroid treatment among therapies used. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case Series (historical) | Medical Times | Early case series on treating alopecia areata/totalis with cortisone, hydrocortisone, prednisone and prednisolone. |
| [24326563](https://pubmed.ncbi.nlm.nih.gov/24326563/) | 2013 | Animal Study | J Investig Dermatol Symp Proc | Investigates parathyroid hormone-collagen binding domain fusion proteins as a novel alopecia areata therapy in mice (mechanistic context). |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review (historical) | J Med Soc New Jersey | General review of alopecia areata and other common scalp problems. |

---

## Germany Market Information

Hydrocortisone currently holds **no registered market authorizations** in this jurisdiction (market status: Not Marketed; 0 licenses on file). No approved indication text is available to compare against the predicted new indication.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data are currently available in this evidence pack (see data gap DG001: TFDA/label warnings and contraindications — flagged as Blocking for the safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top-ranked prediction (alopecia areata) is supported by a completed Phase 3 RCT directly comparing hydrocortisone to an active comparator in this exact indication, plus a substantial literature base spanning decades — this is an evidence level L1 signal reflecting established clinical practice rather than a purely novel hypothesis. However, the drug currently lacks MOA data and any market authorization in this jurisdiction, and formal safety/label data are missing, so guardrails are warranted before advancing.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications before any S1 safety pre-assessment
- Resolve DG002: retrieve confirmed MOA data from DrugBank to strengthen the mechanistic rationale
- Confirm original approved indication(s) and licensing history for hydrocortisone in the target market
- Clarify regulatory pathway given current "Not Marketed" status before considering label extension or off-label guidance
- Lower-ranked predictions (ranks 2–10) remain at L3–L5 evidence with Hold/Research Question status and are not ready to advance without additional targeted studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

