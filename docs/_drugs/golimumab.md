---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 5
---

# Golimumab
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

# Golimumab: From Approved Inflammatory Arthritis Indications to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody with established indications in inflammatory arthritis (rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, and polyarticular juvenile idiopathic arthritis per published literature). The TxGNN model's top-ranked prediction suggests potential efficacy for **Rheumatoid Vasculitis**, but the supporting evidence is mixed — **3 loosely related clinical trials** and **6 publications**, including case reports that describe anti-TNF therapy both *treating* and *paradoxically inducing* vasculitis. This evidence pack (`TW-DB06674-multi`) contains four additional candidate indications; two of them (ranked #3 and #5) are substantially better supported and are summarized at the end of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from formal license data (golimumab is not currently marketed in this jurisdiction); literature confirms approved use for rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, and polyarticular JIA elsewhere |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% (rank 3700 in model output) |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured DrugBank mechanism-of-action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the literature retrieved, golimumab is a fully human anti-TNF-α IgG1κ monoclonal antibody administered subcutaneously (or intravenously), approved for rheumatoid arthritis, psoriatic arthritis, and axial spondyloarthritis (PMID 28530020, 20065639).

Rheumatoid vasculitis is a severe extra-articular manifestation of long-standing, seropositive rheumatoid arthritis, driven by immune complex deposition and TNF-mediated vascular inflammation. Mechanistically, suppressing TNF-α could plausibly reduce this vasculitic process, and one case report notes that the incidence of rheumatoid vasculitis has declined since biologic DMARDs (including anti-TNF agents) entered practice (PMID 29075910).

However, the evidence is not one-directional. A case report of two patients who developed **Takayasu's arteritis while on anti-TNF therapy** (PMID 22999907) illustrates a recognized "paradoxical vasculitis" phenomenon associated with this drug class — anti-TNF agents can, in some patients, trigger or unmask vasculitic disease rather than treat it. This directionally inconsistent signal is the main reason the evidence level is capped at L4 (mechanism/case-report level) despite the very high TxGNN score, and why the current recommendation is to Hold pending safety clarification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Evaluates perioperative immunosuppressant (incl. anti-TNF) management in rheumatology patients undergoing shoulder arthroplasty; population overlap only, not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large real-world study on risk of new immune-mediated inflammatory disease (IMID) onset after biologic treatment for a single IMID; may capture vasculitis as an outcome but not as a primary endpoint |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional study of a biologic (tocilizumab, not golimumab) in RA patients with inadequate DMARD response; included for RA population overlap, not golimumab- or vasculitis-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-Analysis | Int J Mol Sci | Compares golimumab and other TNF inhibitors across 36 RCTs for radiographic joint destruction in RA; strong comparative efficacy data but no vasculitis endpoint |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Overview of biologic therapies (including anti-TNF agents) for autoimmune/rheumatologic disease, general efficacy/safety context |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Frequency and causes of end-stage renal disease in RA patients; relevant to extra-articular RA burden but not vasculitis-specific |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatol Int | Severe sepsis (pyoderma gangrenosum/pyogenic arthritis) in an RA patient on golimumab; notes rheumatoid vasculitis incidence has declined since anti-TNF agents were introduced |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | Two cases of **Takayasu's arteritis occurring under anti-TNF therapy** — paradoxical vasculitis-induction signal that contradicts the therapeutic hypothesis |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocul Immunol Inflamm | Behçet disease-associated uveitis (a vasculitis-related condition) successfully treated with golimumab — a positive counter-signal |

---

## Germany Market Information

Golimumab is currently **not marketed** in this jurisdiction — no authorization records are on file (`total_licenses: 0`).

---

## Safety Considerations

Structured safety data (key warnings, contraindications, DDI) is not currently available for this drug in this evidence pack.

**Evidence-derived safety signal (not from structured safety data):** Literature includes a case report of anti-TNF-associated **paradoxical vasculitis** (Takayasu's arteritis onset during anti-TNF therapy, PMID 22999907). This directly relevant safety signal should be resolved before pursuing rheumatoid vasculitis as an indication.

Please refer to the package insert for full safety information once available (see Data Gap DG001 below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for anti-TNF therapy in rheumatoid vasculitis is plausible but not consistently supported — literature evidence includes both a protective signal (declining vasculitis incidence since anti-TNF introduction) and a contradictory signal (anti-TNF-induced vasculitis case reports). No clinical trial directly and adequately evaluates golimumab for this indication. Evidence level is L4 (case report/mechanism only).

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (Data Gap DG001, Blocking — required before any S1 safety screening)
- Structured mechanism-of-action data from DrugBank (Data Gap DG002, High)
- A dedicated literature review to reconcile the therapeutic-vs-paradoxical vasculitis signal for anti-TNF agents
- A clinical trial or registry study with rheumatoid vasculitis as a primary or explicit secondary endpoint

---

## Other Candidate Indications in This Evidence Pack

This evidence pack evaluated 5 candidate indications for golimumab. The other four, ranked by TxGNN, are summarized below — two are substantially better supported than the top-ranked prediction above and warrant separate, dedicated evaluation.

| Rank | Indication | TxGNN Score | Evidence Level | Decision | Note |
|------|-----------|-------------|-----------------|----------|------|
| 3 | **Inflammatory spondylopathy** | 99.66% | **L1** | **Proceed with Guardrails** | Strongest candidate — golimumab is already an approved anti-TNF therapy for ankylosing spondylitis, nr-axSpA, and psoriatic arthritis, supported by numerous completed Phase 3/4 RCTs (e.g., NCT00265083, NCT02186873, NCT03270501) and systematic reviews (PMID 36270657, 38503473). This is largely an existing-indication extension rather than novel repurposing. |
| 5 | **Polyarticular juvenile rheumatoid arthritis** | 99.59% | **L1** | **Proceed with Guardrails** | Also strongly supported — golimumab (SC and IV) is already FDA-approved for polyarticular JIA, backed by completed Phase 3 RCTs (NCT01230827, NCT02277444) and long-term extension safety data (PMID 33493312, 28507219, 39089836). Continued monitoring needed for pediatric long-term immunosuppression risk (infection, malignancy). |
| 2 | Hypermobility of coccyx | 99.67% | L5 | Hold | No clinical trials or literature; no plausible biological link to TNF-α inhibition. Likely knowledge-graph noise. |
| 4 | Kummell disease | 99.61% | L5 | Hold | No clinical trials or literature; vertebral ischemic collapse has no mechanistic connection to golimumab. Likely knowledge-graph noise. |

**Recommendation:** Prioritize separate, dedicated evaluation reports for **inflammatory spondylopathy** and **polyarticular JIA** (rank 3 and 5) — these represent the strongest, most actionable findings in this evidence pack and are far more decision-ready than the top-ranked rheumatoid vasculitis prediction. Ranks 2 and 4 can be deprioritized as low-confidence model output.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

