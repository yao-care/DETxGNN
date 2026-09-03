---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# AZATHIOPRINE: From Immunosuppressant Therapy to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a thiopurine immunosuppressant; this evidence pack does not record its original approved indication, but pharmacologically it belongs to the purine-analog immunosuppressant class.
Among 10 TxGNN-predicted indications, the only one with substantial supporting evidence is **Inflammatory Bowel Disease (IBD)** — a use already well established in clinical practice — backed by **~47 clinical trials** and **20 publications**, including multiple Cochrane systematic reviews.
The other 9 predictions (mostly rare congenital/genetic syndromes) carry very high TxGNN scores but **zero supporting clinical trials or literature**, and are flagged by the evidence pack itself as likely model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (drug class: thiopurine/purine-analog immunosuppressant) |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's Disease / Ulcerative Colitis) |
| TxGNN Prediction Score | 99.52% (overall model rank 5,720) |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (pending safety data) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for azathioprine is not available in this evidence pack (flagged as data gap DG002). Based on the pharmacological information embedded in the evidence records, azathioprine is a purine-analog prodrug that is metabolized to 6-mercaptopurine (6-MP), which inhibits purine synthesis and suppresses the proliferation of activated T- and B-lymphocytes. This antiproliferative, immune-suppressing mechanism is the basis for azathioprine's long-standing, well-established role as a steroid-sparing maintenance therapy in inflammatory bowel disease (both Crohn's disease and ulcerative colitis), where chronic T-cell–mediated mucosal inflammation drives disease activity.

Because IBD pathophysiology is fundamentally an aberrant immune/inflammatory process, azathioprine's mechanism is directly and plausibly applicable — this is reflected in the evidence pack by decades of RCTs, Cochrane systematic reviews, and pharmacogenetic studies (TPMT/NUDT15-guided dosing) specifically evaluating azathioprine in IBD. It should be noted that this is less a "novel repurposing signal" and more a **model-validated confirmation of an already-recognized therapeutic use** — TxGNN correctly re-derived a known, clinically mainstream indication for this drug.

By contrast, the 8 other top-ranked TxGNN predictions in this pack (e.g., colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, osteoarthritis susceptibility, WHIM syndrome, chronic granulomatous disease variants, acromesomelic dysplasia) are rare congenital/genetic disorders with **no mechanistic link, no clinical trials, and no literature support**. Several (WHIM syndrome, chronic granulomatous disease) are primary immunodeficiency syndromes where adding an immunosuppressant would plausibly *worsen* infection risk — the opposite of a therapeutic rationale. These are correctly scored L5/S0/Hold in the pack and should be treated as network-prediction artifacts rather than genuine candidates.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Unknown | 84 | RCT comparing low-dose azathioprine + allopurinol vs. azathioprine monotherapy in ulcerative colitis; tests strategy to reduce treatment failure/adverse events |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Infliximab vs. infliximab+azathioprine vs. azathioprine alone in immunomodulator/biologic-naive Crohn's disease (SONIC-type design) |
| [NCT01015391](https://clinicaltrials.gov/study/NCT01015391) | N/A (RCT) | Unknown | 100 | Open-label RCT: T2 vs. azathioprine for maintaining remission after surgical resection in Crohn's disease |
| [NCT03464136](https://clinicaltrials.gov/study/NCT03464136) | Phase 3b | Completed | 386 | Ustekinumab vs. adalimumab in biologic-naive Crohn's; azathioprine as prior/background immunomodulator |
| [NCT00577538](https://clinicaltrials.gov/study/NCT00577538) | N/A | Completed | 7 | Safety study on lymphoproliferative disease risk associated with azathioprine/6-MP in IBD |
| [NCT02929706](https://clinicaltrials.gov/study/NCT02929706) | N/A | Unknown | 400 | NUDT15 R139C genotype-guided thiopurine dose optimization to reduce azathioprine-induced leucopenia in IBD |
| [NCT00113503](https://clinicaltrials.gov/study/NCT00113503) | Phase 2 | Terminated | 50 | Multi-site trial comparing weight-based vs. metabolite-guided azathioprine dosing in Crohn's disease |
| [NCT05584228](https://clinicaltrials.gov/study/NCT05584228) | N/A | Not Yet Recruiting | 150 | SMART trial: azathioprine + subcutaneous infliximab vs. surgical resection in symptomatic small bowel Crohn's disease |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | MIRACLE trial: top-down mirikizumab vs. standard-of-care azathioprine in newly diagnosed moderate-to-severe ulcerative colitis |
| [NCT00796250](https://clinicaltrials.gov/study/NCT00796250) | Phase 3 | Terminated | 9 | Infliximab as "bridging therapy" in corticodependent Crohn's disease under standard azathioprine treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art clinical review of thiopurine (azathioprine/mercaptopurine/thioguanine) use in IBD |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Improved molecular insight into azathioprine's mechanism and clinical implications in IBD |
| [33305616](https://pubmed.ncbi.nlm.nih.gov/33305616/) | 2021 | Review | Pharmacogenomics | Pharmacogenetics of IBD, with focus on thiopurine treatment optimization |
| [30954317](https://pubmed.ncbi.nlm.nih.gov/30954317/) | 2019 | Review | Gastroenterol Hepatol | Evidence review on discontinuing aminosalicylates, thiopurines and methotrexate in IBD |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Cohort/Pharmacogenetics | Biomed Pharmacother | TPMT gene methylation and azathioprine pharmacokinetics in very-early-onset IBD children |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Cohort/Pharmacogenetics | J Gastroenterol Hepatol | Azathioprine/6-MP pharmacogenetics and metabolite monitoring in IBD |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Mechanism study | Cell Reports Medicine | Gut commensal bacteria (Blautia wexlerae) linked to azathioprine therapy failure via reduced 6-MP bioavailability |
| [10499471](https://pubmed.ncbi.nlm.nih.gov/10499471/) | 1999 | Clinical review | Scand J Gastroenterol Suppl | Update on azathioprine clinical efficacy and safety in IBD |
| [40126153](https://pubmed.ncbi.nlm.nih.gov/40126153/) | 2025 | Epidemiology | Scand J Gastroenterol | Temporal trends in IBD characteristics and treatment patterns |
| [27688654](https://pubmed.ncbi.nlm.nih.gov/27688654/) | 2016 | Review | World J Gastroenterol | IBD in India — past, present and future, including thiopurine treatment context |

---

## Germany Market Information

No marketing authorizations are on record for this drug in the current dataset. Market status is reported as **Not Marketed**, with **0 total licenses**.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** This evidence pack flags a **Blocking** data gap (DG001) — TFDA/BfArM label warnings and contraindications are unavailable. This prevents a formal S1 safety pre-assessment for azathioprine, independent of the efficacy evidence summarized above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The efficacy evidence for azathioprine in IBD is strong (L1: multiple RCTs and Cochrane systematic reviews spanning decades), and the mechanistic rationale is sound — but this reflects an already well-established use rather than a novel repurposing opportunity.
- A **Blocking**-severity data gap (missing label warnings/contraindications) prevents safety pre-assessment (S1), and the drug currently has **no market authorization** in this jurisdiction (0 licenses, "Not Marketed"), so a "Proceed with Guardrails" call cannot yet be responsibly made.
- Eight of the ten TxGNN-predicted indications in this pack (rare congenital/genetic syndromes) have no clinical or literature support and should not be pursued.

**To proceed, the following is needed:**
- Retrieve TFDA/BfArM package insert (warnings, contraindications, DDI) to complete S1 safety pre-assessment
- Confirm original/current approved indications and MOA via DrugBank or regulatory source
- Clarify regulatory pathway for market authorization given current "Not Marketed" status
- If proceeding, implement TPMT/NUDT15 genotype-guided dosing and routine CBC/liver monitoring per the pharmacogenetic literature identified above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

