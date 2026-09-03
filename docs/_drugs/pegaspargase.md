---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

> Pegaspargase is a PEGylated asparaginase enzyme long used as a backbone agent in the treatment of acute lymphoblastic leukemia (ALL) and lymphoblastic lymphoma (LBL).
> The TxGNN model's top-ranked prediction — **Precursor Lymphoblastic Lymphoma/Leukemia** — is, in reality, a restatement of the drug's already-established core indication rather than a genuinely novel use.
> This signal is supported by **60+ clinical trials** (many Phase 3) and **20 publications**, but the evidence confirms known pharmacology rather than opening a new therapeutic direction. Several lower-ranked, more genuinely "new" candidates (e.g., Hodgkin lymphoma, lymphoid neoplasm broadly) carry much weaker and partly mismatched evidence and are flagged separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) / Lymphoblastic Lymphoma — internationally established use; not documented in German license data (drug not marketed) |
| Predicted New Indication | Precursor Lymphoblastic Lymphoma/Leukemia *(essentially overlaps with the original approved use — see caveat below)* |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

⚠️ **Important caveat**: "Precursor lymphoblastic lymphoma/leukemia" is clinically synonymous with the drug's existing core indication (ALL/LBL), not a new disease area. The repurposing rationale in the evidence pack explicitly confirms this is "an existing approved mechanism, not a new use." Guardrails here concern management of known toxicities (hypersensitivity, pancreatitis, thrombosis), not de-novo indication risk.

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available from DrugBank in this evidence pack (marked as a Data Gap). Based on the accompanying repurposing rationale and known pharmacology, pegaspargase hydrolyzes circulating asparagine. Lymphoblasts in ALL/LBL characteristically have low or absent asparagine synthetase expression, making them dependent on exogenous asparagine; depleting it starves these cells and drives apoptosis. This is a textbook, decades-established mechanism — not a newly discovered pathway.

Because the top-ranked TxGNN prediction (precursor lymphoblastic lymphoma/leukemia) and the 5th-ranked prediction (acute lymphoblastic leukemia) both describe the drug's own approved indication, the model is essentially reproducing known biology rather than surfacing a repurposing opportunity. This is a useful sanity check on model validity but should not be reported to stakeholders as a "new indication."

The more interesting signals sit further down the ranked list — Hodgkin lymphoma (rank 8) and the broader "lymphoid neoplasm" category (rank 7) — where evidence is thinner and, on closer inspection, largely derived from a *different* disease entity (extranodal NK/T-cell lymphoma, a non-Hodgkin subtype) rather than classical Hodgkin lymphoma itself. This mismatch is explicitly called out in the rationale text and should be resolved before any further evaluation.

---

## Clinical Trial Evidence

*(from predicted_indications[0]: precursor lymphoblastic lymphoma/leukemia)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03020030](https://clinicaltrials.gov/study/NCT03020030) | Phase 3 | Active, not recruiting | 560 | Large pediatric/adolescent newly-diagnosed ALL protocol with pegaspargase as backbone (Grade A relevance) |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2044 | French national pediatric ALL protocol optimizing L-asparaginase (pegaspargase) dosing/use (Grade A relevance) |
| [NCT04954326](https://clinicaltrials.gov/study/NCT04954326) | Phase 2 | Completed | 89 | PK comparison of liquid vs lyophilized pegaspargase (S95014) formulations in newly diagnosed pediatric ALL |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Completed | 649 | Large observational study forecasting hypersensitivity to PEG-asparaginase to optimize ALL outcomes |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Recruiting | 440 | Randomized trial of levocarnitine to prevent asparaginase-associated hepatotoxicity in AYA ALL/LBL patients |
| [NCT00187083](https://clinicaltrials.gov/study/NCT00187083) | Phase 3 | Completed | 40 | Native vs PEG-asparaginase comparison during induction for relapsed/refractory childhood ALL |
| [NCT00003437](https://clinicaltrials.gov/study/NCT00003437) | Phase 3 | Unknown | 1800 | UK national childhood ALL trial comparing steroid/chemotherapy regimens |
| [NCT01665001](https://clinicaltrials.gov/study/NCT01665001) | Phase 2 | Unknown | 200 | Individualized MRD-adapted therapy for adults with precursor lymphoid neoplasms (PALG) |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Completed | 37 | Methotrexate/vincristine/pegylated-asparaginase/dexamethasone salvage regimen in relapsed ALL |
| [NCT00882206](https://clinicaltrials.gov/study/NCT00882206) | Phase 2 | Terminated | 15 | Decitabine + vorinostat + VPLD chemo (incl. PEG-asparaginase) in relapsed/refractory ALL/LBL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort (Tier 1) | Blood Advances | GIMEMA LAL1913: pegaspargase-modified risk-oriented program improves outcomes in adult ALL/LBL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort (Tier 1) | J Clin Oncol | DFCI 11-001: efficacy/toxicity of pegaspargase vs calaspargase pegol in childhood ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review (Tier 2) | Haematologica | Expert consensus on recognition/prevention/management of asparaginase-associated adverse events in adults |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Cohort/Phase 2 | Int J Hematol | Phase 2 multicenter study of pegaspargase in Japanese patients with untreated ALL |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Phase 3 RCT | J Clin Oncol | COG AALL1231: bortezomib in newly diagnosed T-ALL/T-LL (pegaspargase as backbone) |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | Phase 3 RCT | J Clin Oncol | COG AALL0434: nelarabine in newly diagnosed T-ALL (pegaspargase-containing backbone) |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 (long-term f/u) | Leukemia | Venetoclax + hyper-CVAD/nelarabine/pegylated asparaginase in T-ALL/LBL |
| [35987855](https://pubmed.ncbi.nlm.nih.gov/35987855/) | 2022 | Consensus/Review | Bulletin du Cancer | French Society recommendations for prevention/management of pegaspargase toxicities |
| [31571395](https://pubmed.ncbi.nlm.nih.gov/31571395/) | 2020 | Case series | Pediatr Blood Cancer | Rapid desensitization protocol allowing continued pegaspargase use in hypersensitive pediatric patients |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opin Pharmacother | Foundational pharmacology review of PEG-asparaginase in leukemia treatment |

---

## Other TxGNN-Predicted Indications (Full Candidate List)

This evidence pack scored 10 candidate indications for pegaspargase. For transparency, given the multi-candidate nature of this pack, the full ranking is summarized below:

| Rank | Disease | Score | Evidence Level | Recommendation | Note |
|------|---------|-------|-----------------|-----------------|------|
| 1 | Precursor lymphoblastic lymphoma/leukemia | 99.96% | L1 | Proceed with Guardrails | = existing approved indication, not novel |
| 2 | Pre-germinal center CLL/SLL | 99.95% | L5 | Hold | No mechanistic support; likely graph-structure artifact |
| 3 | CLL/SLL with IGHV somatic hypermutation | 99.95% | L5 | Hold | Same as above |
| 4 | Follicular lymphoma | 99.90% | L5 | Hold | Mature B-cells; not asparagine-dependent; no evidence |
| 5 | Acute lymphoblastic leukemia | 99.89% | L1 | Proceed with Guardrails | = existing approved indication, not novel |
| 6 | Methylcobalamin deficiency (cblE) | 99.74% | L5 | Hold | Mechanistically unrelated; likely data/ontology noise |
| 7 | Lymphoid neoplasm (broad category) | 99.71% | L3 | Research Question | Evidence is ALL-specific, not generalizable to all lymphoid tumors |
| 8 | Hodgkin lymphoma | 99.71% | L2 | Research Question | ⚠️ Most cited evidence is actually for NK/T-cell lymphoma (a different NHL subtype), not classical Hodgkin lymphoma — label mismatch needs resolution |
| 9 | CLL/SLL | 99.68% | L5 | Hold | No mechanistic support; no evidence |
| 10 | CML blast phase, BCR-ABL1+ | 99.61% | L4 | Research Question | Plausible only for lymphoid blast crisis subtype; not distinguished from myeloid blast crisis in evidence |

**Interpretation**: Only ranks 1 and 5 have strong (L1) evidence, and both simply restate the known indication. Ranks 7, 8, and 10 are genuine "Research Question" candidates but have weak, partially mismatched evidence. Ranks 2, 3, 4, 6, and 9 should be held — no plausible mechanism and zero supporting trials/literature.

---

## Germany Market Information

Pegaspargase currently has **no marketing authorization in Germany** in this dataset (`market_status: 未上市`, `total_licenses: 0`). No product listings are available to summarize.

---

## Cytotoxicity

Pegaspargase is an antineoplastic agent (asparagine-depleting enzyme), used as a core component of ALL/LBL chemotherapy regimens — it meets the antineoplastic criteria via original indication and established drug class.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme-based (asparagine-depleting), distinct from DNA-damaging or targeted agents |
| Myelosuppression Risk | Low direct myelosuppression from pegaspargase itself; however, it is almost always combined with myelosuppressive agents (vincristine, anthracyclines, corticosteroids), so combination-regimen myelosuppression risk is high |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Coagulation panel (fibrinogen, antithrombin III), liver function tests, lipase/amylase (pancreatitis), fasting glucose/triglycerides, signs of hypersensitivity, CBC (regimen-wide) |
| Handling Protection | Yes — standard cytotoxic/antineoplastic drug handling precautions apply during preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack; no DDI records were found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for the top-ranked candidate — with the caveat that this is confirmatory, not a new indication)*

**Rationale:**
- The top TxGNN prediction restates pegaspargase's already-established, guideline-standard use in ALL/LBL, backed by multiple Phase 3 trials and consistent literature — evidence is strong, but there is no new indication value to capture here.
- Genuinely exploratory candidates (Hodgkin lymphoma, lymphoid neoplasm broadly, CML lymphoid blast crisis) remain at the "Research Question" stage with thin or mismatched evidence and should not proceed further without additional work.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/BfArM package insert warnings and contraindications before any S1 safety pre-assessment can proceed.
- Resolve DG002 (High): obtain structured MOA data from DrugBank to support formal mechanistic-link scoring.
- For the Hodgkin lymphoma candidate (rank 8): clarify whether the underlying evidence (NK/T-cell lymphoma trials) was mis-mapped to Hodgkin lymphoma before any further evaluation.
- For "lymphoid neoplasm" (rank 7): narrow the evidence base to disease subtypes with actual asparagine-synthetase-deficiency data, rather than treating it as a single broad category.
- Given the drug is not marketed in Germany, confirm regulatory pathway/relevance before allocating further evaluation resources to this market.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

