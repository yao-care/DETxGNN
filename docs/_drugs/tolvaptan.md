---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From an Undocumented Original Indication to Polycystic Kidney Disease (ADPKD)

## One-Sentence Summary

> The evidence pack does not contain Tolvaptan's original approved indication (drug not marketed in Germany, no license records; TFDA label data blocked as DG001).
> The TxGNN model's top-ranked signal — **polycystic kidney disease type 3, with or without polycystic liver disease (ADPKD)** — is supported by **2 landmark completed Phase 3 RCTs** and **20 publications**.
> Importantly, the model's own rationale flags this as an **already-established, approved indication of tolvaptan** (e.g., Jinarc/Samsca for ADPKD) rather than a novel repurposing discovery — this is a confirmatory signal, not new science.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Germany: unmarketed, 0 licenses) |
| Predicted New Indication | Autosomal Dominant Polycystic Kidney Disease (ADPKD), with or without polycystic liver disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs: TEMPO 3:4, REPRISE) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, the structured `original_moa` field is a data gap (DG002). However, the model's own repurposing rationale supplies functional mechanism detail: tolvaptan is a **selective vasopressin V2-receptor antagonist**. By blocking V2 receptors in the renal collecting duct, it suppresses cAMP generation — the key second messenger driving cyst epithelial proliferation and fluid secretion in ADPKD.

Critically, this is **not an exploratory repurposing hypothesis**. The rationale explicitly states this is "an already-established, mechanistically well-defined approved indication" — tolvaptan (as Jinarc/Samsca) is already approved in multiple markets (Japan, US, EU) specifically for slowing ADPKD progression, based on the TEMPO 3:4 and REPRISE trials cited in this evidence pack. The TxGNN signal here should be read as **validation of known pharmacology**, not discovery of a new use.

Because Germany shows "未上市" (unmarketed) with zero licenses, this evidence pack suggests the German market either lacks a current tolvaptan/ADPKD authorization on file, or the record simply wasn't captured — this needs regulatory verification (see Next Steps) rather than being treated as a true regulatory gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the structured `clinical_trials` field for this indication (pivotal trial data is captured instead as literature — see below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | NEJM | TEMPO 3:4 — tolvaptan slows total kidney volume growth and eGFR decline in early ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | NEJM | REPRISE — confirms efficacy/safety of tolvaptan in later-stage ADPKD |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT | Pediatr Nephrol | Randomized trial (NCT02964273) of tolvaptan safety/PD in pediatric ADPKD (5–17y) |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review/Meta-analysis | Nefrología | Confirms overall efficacy and safety profile of tolvaptan in ADPKD across trials |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Review/Consensus | NDT | ERA Working Group consensus on when/how to initiate tolvaptan in ADPKD |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Tolvaptan slows renal deterioration and cyst growth in ADPKD/PCLD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Review of disease-modifying interventions, including tolvaptan, for ADPKD progression |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Contemporary overview of ADPKD epidemiology and management |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | Int J Mol Sci | ADPKD cystogenesis pathophysiology and treatment advances |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | Emerging ADPKD therapies beyond tolvaptan, positioning tolvaptan as current standard of care |

---

## Germany Market Information

No marketing authorization records are present in this evidence pack (`taiwan_regulatory.market_status` = 未上市, `total_licenses` = 0). This should be verified independently — tolvaptan (Jinarc®) holds an EU-wide centralized marketing authorization for ADPKD, so the absence here likely reflects a data-collection gap rather than true non-availability in Germany.

---

## Other TxGNN-Predicted Indications (Not Prioritized)

Ranks 2–10 scored similarly high (>99.9%) but the model's own rationale flags most as likely embedding-similarity noise, with no mechanistic or evidentiary support:

| Rank | Disease | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|
| 5 | Joubert syndrome with renal defect | L4 | Research Question | Shared ciliopathy/cAMP biology with ADPKD, but no direct tolvaptan evidence |
| 4 | Thoracic malformation | L4 | Hold | Only indirect case reports (tolvaptan for fluid overload, not structural defect) |
| 2, 3, 6, 7, 8, 10 | Various congenital/structural syndromes | L5 | Hold | No literature or trial support; likely model noise |
| 9 | Malformation syndrome with periodontal component | L5 | Hold | Retrieved literature is unrelated periodontitis research; false match |

These are not actionable and are listed only for completeness.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety fields (`key_warnings`, `contraindications`, `ddi`) are all data gaps in this evidence pack (DG001, Blocking).

One point from the repurposing rationale merits flagging pending full label data: hepatotoxicity monitoring is specifically called out as a known concern with tolvaptan use in ADPKD (consistent with the boxed hepatotoxicity warning associated with this drug class in other markets).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ADPKD signal is backed by L1-grade evidence (two completed Phase 3 RCTs — TEMPO 3:4 and REPRISE) and represents an already-established use of tolvaptan rather than speculative repurposing. However, this evidence pack is missing TFDA/label safety data (DG001, Blocking) and structured MOA data (DG002), and shows no German marketing authorization on file — all of which must be resolved before any regulatory or clinical action.

**To proceed, the following is needed:**
- Retrieve official TFDA/German (BfArM) label PDF for hepatotoxicity warnings, contraindications, and DDI data (resolves DG001)
- Confirm structured MOA via DrugBank API query (resolves DG002)
- Independently verify current EU/German marketing authorization status for tolvaptan/Jinarc, given the discrepancy between "未上市" here and known EU-wide ADPKD approval
- Clarify with stakeholders that this candidate is a **confirmatory signal** for an existing approved use, not a genuinely novel repurposing opportunity — this affects how it should be positioned internally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

