---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Certolizumab pegol is a PEGylated anti-TNFα Fab fragment used to treat rheumatoid arthritis and related inflammatory autoimmune diseases.
> The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
> but the supporting evidence is thin and partly contradictory — **3 tangentially related clinical trials** and **8 case-level publications**, several of which describe anti-TNF agents (including certolizumab itself) *inducing* vasculitis rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in structured licensing data (drug not marketed in Germany); per literature within this evidence pack, certolizumab pegol is indicated for rheumatoid arthritis, axial spondyloarthritis, psoriatic arthritis, and Crohn's disease |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formal, structured mechanism-of-action entry is not available for this drug (data gap). However, the evidence pack's own literature consistently describes certolizumab pegol as a PEGylated antigen-binding (Fab') fragment of a humanized monoclonal antibody that selectively neutralizes TNFα. Unlike full-length anti-TNF antibodies, it lacks an Fc region, which theoretically reduces complement fixation and antibody-dependent cytotoxicity while still blocking soluble and membrane-bound TNFα.

Rheumatoid vasculitis is a rare, severe extra-articular manifestation of rheumatoid arthritis, driven in part by immune-complex deposition and TNF-mediated vascular inflammation. On this basis, TNFα blockade is a mechanistically plausible approach to controlling the disease — and this is reflected in the one available positive case report (PMID 34786446), where certolizumab was used to treat leg ulcers caused by rheumatoid vasculitis.

However, the majority of the literature evidence points in the **opposite direction**: multiple independent case reports describe anti-TNF agents — including certolizumab pegol itself — *paradoxically inducing* vasculitis (leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, medium-vessel vasculitis, and even rapidly progressive glomerulonephritis) in patients being treated for RA. This is a recognized anti-TNF class effect. The mechanistic hypothesis is therefore genuinely contested by the drug's own known adverse-event profile, not merely under-studied.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; not vasculitis-specific |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional RA registry study on tocilizumab (not certolizumab); general RA safety/efficacy patterns only |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study on incident risk of additional immune-mediated inflammatory diseases in patients on biologics; not a causal or interventional test for vasculitis |

None of these trials directly test certolizumab pegol for rheumatoid vasculitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Review | RMD Open | Comparative review of infection risk across immune-modulatory drugs including certolizumab |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Cohort | RMD Open | 80-patient multicentre study of certolizumab for uveitis due to IMIDs — effectiveness/safety data, not vasculitis-specific |
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | Certolizumab pegol used to treat leg ulcers caused by rheumatoid vasculitis (the one positive-direction case) |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case Report (ADR) | J Clin Pharm Ther | Hypocomplementemic urticarial vasculitis developed *during* certolizumab treatment for RA |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case Report (ADR) | Proc (Baylor Univ Med Ctr) | Leukocytoclastic vasculitis as a drug reaction to certolizumab pegol |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case Report (ADR) | Cureus | Anti-TNF-induced medium-vessel vasculitis in a seronegative RA patient switched to certolizumab |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case Report (ADR) | Mod Rheumatol Case Rep | Rapidly progressive glomerulonephritis following certolizumab pegol initiation |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Case Series (ADR) | Clin Med Res | Single-center experience of cutaneous adverse events (including vasculitic reactions) with biologic agents |

**Note:** 5 of the 8 publications describe certolizumab (or the anti-TNF class) as a *cause* of vasculitis, not a treatment — this is the dominant signal in the current literature.

---

## Germany Market Information

Certolizumab pegol currently has **no marketing authorization in Germany** (0 licenses on file), so no authorization table is available.

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug interactions) for this candidate is not available in the current evidence pack.

**Literature-derived safety signal:** Independent of the structured safety fields, the literature evidence above indicates a recognized class effect in which anti-TNF agents — including certolizumab pegol — can paradoxically induce vasculitis (leukocytoclastic vasculitis, urticarial vasculitis, medium-vessel vasculitis) and, in at least one case, glomerulonephritis. This should be treated as an active safety consideration for any exploration of the rheumatoid vasculitis indication, not merely a data gap.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base is sparse (L4, no dedicated clinical trials) and internally conflicted — most publications describe certolizumab pegol as a cause of vasculitis rather than a treatment for it, which directly undermines the repurposing hypothesis rather than merely leaving it unproven.

**To proceed, the following is needed:**
- TFDA/German label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- A formally sourced mechanism-of-action record (currently a High-severity data gap)
- A systematic review (not case-report-level) specifically distinguishing certolizumab-induced vasculitis from therapeutic use in RA-associated vasculitis, to resolve the directional conflict in current evidence
- If pursued further, a defined pharmacovigilance/monitoring plan given the documented paradoxical vasculitis signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

