---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a fully human anti-TNF-α monoclonal antibody whose established use, as documented across the clinical trial and literature records reviewed here, is rheumatoid arthritis and related TNF-driven autoimmune inflammatory diseases. The TxGNN model predicts it may also be effective for **Rheumatoid Vasculitis**, with **0 clinical trials** and **20 publications** currently available — but the literature signal is directionally mixed, showing both therapeutic and drug-induced vasculitis reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (per literature/trial records; not confirmed via formal regulatory license data — see Germany Market Information below) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data from DrugBank is not yet available in this evidence pack (data gap DG002, High severity). Based on information embedded in the clinical trial and literature records reviewed here, adalimumab is repeatedly described as a fully human anti-TNF-α monoclonal antibody that binds and neutralizes tumor necrosis factor-alpha (TNF-α), thereby blocking TNF-induced inflammatory signaling. It is documented across these records as effective in rheumatoid arthritis (RA) and related TNF-driven autoimmune inflammatory diseases, including psoriatic arthritis, ankylosing spondylitis, and juvenile idiopathic arthritis.

Rheumatoid vasculitis (RV) is itself a severe extra-articular complication of rheumatoid arthritis, thought to involve TNF-α-mediated endothelial activation and immune-complex deposition in vessel walls. Because adalimumab already targets the shared upstream cytokine (TNF-α) in the parent disease, the TxGNN model's high similarity score for RV is mechanistically plausible — a signal echoed by the systematic review in this pack (PMID 33058033), which lists biologic agents, including anti-TNF drugs, as part of the RV treatment armamentarium.

However, the same TNF-α blockade mechanism carries a well-documented paradoxical safety signal: several case reports in this evidence pack (PMID 28719435, PMID 19482531, PMID 23559388, PMID 24558628) describe adalimumab *inducing* leukocytoclastic vasculitis, ANCA-associated glomerulonephritis, antiphospholipid syndrome, and lupus-like autoimmunity — effectively the opposite of the intended therapeutic effect. This "treat vs. induce" ambiguity is the central reason the mechanistic rationale, while plausible, does not yet translate into a confident recommendation, and is reflected in the L3 evidence level and Hold decision.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid vasculitis specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical rheumatology | Systematic review of biologic drugs in rheumatoid vasculitis treatment; supports biologics, including anti-TNF agents, as part of the RV therapeutic armamentarium. |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Systematic Review | Clinical and experimental rheumatology | Compared vasculitis characteristics in 2707 RA patients on anti-TNF therapy vs. untreated patients; identified 18 vasculitis cases, informing treat-vs-induce risk. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD open | BSRBR-RA registry analysis found TNF-inhibitor-treated RA patients carry a measurable, drug-specific risk of vasculitis-like events versus non-biologic DMARD users. |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case reports in rheumatology | A 42-year-old RA patient with digital vasculitis (necrotising fingertip ulcers) responded well to adalimumab, supporting a therapeutic signal. |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report (Adverse Event) | The American Journal of Dermatopathology | First reported case of leukocytoclastic vasculitis with dermal perivascular hemophagocytosis associated with adalimumab therapy for RA — a drug-induction signal. |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report (Adverse Event) | Nephrologie & therapeutique | Extracapillary/necrotizing glomerulonephritis with positive ANCA (MPO) developed in an RA patient during adalimumab therapy — vasculitis induction signal. |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Case Report / Review (Adverse Event) | Clinical rheumatology | First reported case of adalimumab-associated antiphospholipid syndrome, with a literature review of anti-TNF-associated vasculitis and APS. |
| [24558628](https://pubmed.ncbi.nlm.nih.gov/24558628/) | 2013 | Case Report (Adverse Event) | Case reports in nephrology | Adalimumab exacerbated IgA glomerulonephritis and induced lupus autoantibodies in a psoriasis patient — further evidence of vasculitis/autoimmune induction risk. |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report (Adverse Event) | Internal medicine (Tokyo, Japan) | Acute pulmonary hypertension crisis occurred in a rheumatoid vasculitis patient 8 months after adalimumab dose reduction, suggesting a protective effect of continued therapy. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report/Series (Adverse Event) | Internal medicine (Tokyo, Japan) | Tocilizumab successfully attenuated ANCA-associated nephritis that developed during combined abatacept/adalimumab therapy for RA. |

---

## Germany Market Information

Adalimumab is currently not marketed in Germany within this dataset (0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/German package-insert warnings and contraindications data are recorded as a **Blocking**-severity gap (DG001) in this evidence pack, and this is the reason the candidate cannot yet proceed past the initial safety-screening stage (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level L3 (a systematic review plus a registry cohort and multiple case reports) shows a directionally conflicting signal: some data suggest anti-TNF biologics benefit rheumatoid vasculitis, while several case reports document adalimumab *inducing* vasculitis, ANCA-associated nephritis, or lupus-like autoimmunity. Combined with a Blocking-severity gap in formal German/TFDA safety labeling (DG001), this candidate cannot yet advance past the S1 safety-screening stage.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/German package-insert warnings & contraindications) — Blocking gap, required before any S1 safety assessment can be completed.
- Resolve DG002 (confirmed mechanism of action from DrugBank or an official regulatory source) to formally substantiate the mechanistic rationale.
- Obtain confirmed German licensing/original-indication data, since adalimumab currently shows 0 licenses on file in this market dataset.
- Commission a targeted review or prospective cohort specifically addressing whether anti-TNF therapy nets a protective effect against, or induces, rheumatoid vasculitis, to resolve the treat-vs-induce contradiction.
- For near-term action, prioritize the two other candidates in this same evidence pack that already carry L1 evidence and a "Proceed with Guardrails" recommendation — **inflammatory spondylopathy** and **polyarticular juvenile rheumatoid arthritis** — while rheumatoid vasculitis remains on Hold pending the items above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

