---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody originally developed for rheumatoid arthritis (and later juvenile idiopathic arthritis).
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, with a very high similarity score, but **9 clinical trials** and **19 publications** in the evidence pack show that this hypothesis has already been directly tested — and the two pivotal Phase III trials were **terminated for lack of efficacy**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis *(no structured license data available; confirmed by literature within this evidence pack, e.g. PMID 19368420, 28841363)* |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (Phase II/III RCT-level evidence — **negative** result) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for this drug (data gap). Based on the literature contained in this evidence pack, tocilizumab is a humanized monoclonal antibody that blocks the interleukin-6 receptor (IL-6R), inhibiting IL-6-mediated pro-inflammatory signaling. Its efficacy is well established for rheumatoid arthritis and juvenile idiopathic arthritis (confirmed elsewhere in this same evidence pack by pivotal trials such as NCT00988221, NCT00144625 and NCT00144664).

IL-6 is an acute-phase, pro-inflammatory cytokine that is also elevated with disease activity in ankylosing spondylitis (AS), which is why AS was historically considered a plausible extension of IL-6R blockade from RA. The very high TxGNN score likely reflects the close topological similarity between RA and AS as inflammatory joint diseases in the knowledge graph.

However, the evidence pack's own mechanistic assessment flags an important caveat: unlike RA, the dominant pathogenic axis in AS/axial spondyloarthritis is IL-17/IL-23–Th17 signaling rather than IL-6. This is precisely the mechanistic background behind the clinical failure of IL-6R antagonists (both tocilizumab and sarilumab) in AS. Two dedicated Phase II/III placebo-controlled RCTs — NCT01209702 (n=306) and NCT01209689 (n=113) — were both **terminated due to lack of efficacy**, and these results were subsequently published (PMID 23765873, BUILDER-1/2). This is real, direct negative clinical evidence rather than an absence of evidence, so despite the model's high prediction score, the repurposing hypothesis is not supported.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Placebo-controlled RCT of tocilizumab 8 mg/kg IV q4w in NSAID-refractory, TNF-naïve AS patients — **terminated for lack of efficacy** |
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | Placebo-controlled RCT of tocilizumab (4 or 8 mg/kg IV) in AS patients with inadequate response to prior TNF antagonists — **terminated for lack of efficacy** |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large registry study of incident immune-mediated inflammatory disease risk in biologic-treated patients; not AS-efficacy specific |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide biologics/tsDMARD registry covering RA, AS and PsA safety; observational, no efficacy hypothesis |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Cytokine/biomarker profiling across systemic inflammatory diseases; not an AS treatment trial |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab effect on T follicular helper cells in RA patients; not AS-specific |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in general rheumatology patients undergoing shoulder arthroplasty; not AS-efficacy specific |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world observational registry — note: evaluates infliximab (Inflectra), not tocilizumab |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Secukinumab in Takayasu arteritis — different drug and disease, low relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/2 RCTs assessing short-term symptomatic efficacy and safety of tocilizumab in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-analysis | Medicine | Comparative effectiveness of all available biologic regimens for AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis (Cohort) | Clin Rheumatol | Risk of serious infections with biologics in AS and non-radiographic axial SpA |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Semin Arthritis Rheum | Second-line biologic therapy optimization in RA, PsA and AS |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Short review specifically on antagonizing IL-6 in AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Biologic agents for AS beyond TNFα antagonists |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Treatment options for AS refractory to TNF inhibition |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clin Exp Rheumatol | Biologics in the treatment of RA and AS |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | Review | Curr Pharm Biotechnol | Biologics in inflammatory and immunomediated arthritis, including AS |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Front Med | Two cases of successful treatment of AA amyloidosis secondary to AS using tocilizumab |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two dedicated Phase II/III placebo-controlled RCTs of tocilizumab in ankylosing spondylitis (NCT01209702, NCT01209689) were both terminated for lack of efficacy, and this is consistent with the mechanistic rationale in the evidence pack — AS pathogenesis is driven primarily by the IL-17/IL-23–Th17 axis rather than IL-6. This is direct negative clinical evidence, not merely insufficient evidence, so this specific repurposing candidate should not advance.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety evaluation of tocilizumab for *any* indication
- Structured mechanism-of-action data from DrugBank API — **High**-priority data gap (DG002)
- If repurposing exploration continues for this drug, prioritize other candidates in this evidence pack with more favorable (or at least non-negative) evidence profiles, such as **rheumatoid vasculitis** (L4, flagged as "Research Question" rather than "Hold"), over further work on the AS hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

