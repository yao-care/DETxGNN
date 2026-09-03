---
layout: default
title: Susoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa: From Acquired Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

> Susoctocog alfa (recombinant B-domain-deleted porcine Factor VIII, marketed elsewhere as Obizur®) is used to control bleeding in **acquired hemophilia A** — a fact confirmed by the evidence pack's own literature even though the `original_indications` field is empty (data gap).
> TxGNN's top-ranked prediction, **primary release disorder of platelets**, has **zero supporting clinical trials or publications**, and the model's own mechanistic rationale flags it as biologically implausible.
> The only predictions in this pack that carry real clinical evidence (hemophilia; acquired coagulation factor deficiency) largely overlap with the drug's known original use rather than representing a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acquired Hemophilia A (inferred from cited literature, e.g. PMID 27098420; `original_indications` field itself is empty — data gap) |
| Predicted New Indication (TxGNN rank #1) | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the drug class and the evidence pack's own literature, susoctocog alfa is a recombinant porcine Factor VIII product that restores thrombin generation by directly replacing FVIII activity — used clinically to stop bleeding in patients with acquired hemophilia A (autoantibody-mediated FVIII inhibition).

TxGNN's #1-ranked prediction, **primary release disorder of platelets**, is a defect in platelet granule release, a mechanism entirely upstream of and independent from the coagulation-factor cascade that susoctocog alfa acts on. The evidence pack's own `repurposing_rationale` explicitly states this: the mechanistic link is weak, and the high score is likely driven by a "bleeding tendency" semantic cluster in the TxGNN knowledge graph rather than genuine biological relevance. The same pattern holds for ranks 2, 3, 6, 7, 8, 9, and 10 (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen-receptor bleeding disorders, constitutional thrombocytopenia, congenital Factor XIII deficiency, and adenosine deaminase deficiency) — all are platelet-function, other-coagulation-factor, or entirely unrelated (immunodeficiency) disorders that FVIII replacement cannot mechanistically correct, and none have any clinical trial or literature support.

The only candidates with genuine mechanistic coherence and real-world evidence are **hemophilia** (rank 4) and **acquired coagulation factor deficiency** (rank 5) — but both are effectively restatements of the drug's known approved use for acquired hemophilia A, not novel repurposing opportunities. This suggests the evidence pack's `original_indications` field should have captured this indication, and its emptiness is a data-completeness issue rather than evidence that no original indication exists.

---

## Clinical Trial Evidence (Rank #1: Primary release disorder of platelets)

Currently no related clinical trials registered.

## Literature Evidence (Rank #1: Primary release disorder of platelets)

Currently no related literature available.

---

## Supplementary: Full TxGNN Ranking Overview

Because this evidence pack evaluates multiple candidate indications, the full ranking is summarized below for transparency:

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Note |
|------|----------------------|-------|-----------------|-----------------|------|
| 1 | Primary release disorder of platelets | 99.94% | L5 | Hold | No evidence; mechanistically weak |
| 2 | Pseudo-von Willebrand disease | 99.93% | L5 | Hold | No evidence; mechanistically weak |
| 3 | Glanzmann thrombasthenia | 99.88% | L5 | Hold | No evidence; mechanistically weak |
| 4 | Hemophilia | 99.74% | L3 | Proceed with Guardrails | 1 PMS trial + 21 publications, but overlaps with known original indication |
| 5 | Acquired coagulation factor deficiency | 99.64% | L3 | Proceed with Guardrails | Multiple real-world/cohort studies, same overlap caveat |
| 6 | Scott syndrome | 99.60% | L5 | Hold | No evidence; mechanistically weak |
| 7 | Bleeding diathesis (collagen receptor defect) | 99.17% | L5 | Hold | No evidence; mechanistically weak |
| 8 | Hemorrhagic disorder (constitutional thrombocytopenia) | 99.17% | L5 | Hold | No evidence; mechanistically weak |
| 9 | Congenital Factor XIII deficiency | 99.15% | L5 | Hold | No evidence; different clotting-cascade step |
| 10 | Adenosine deaminase deficiency | 99.04% | L5 | Hold | Likely spurious; no biological relevance to coagulation |

### Best-Evidenced Candidate: Hemophilia (Rank 4)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | Recruiting | 25 | Japan post-marketing all-case surveillance of IV susoctocog alfa for acquired hemophilia A bleeding events; observational safety/effectiveness data collection |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Phase II/III open-label | Int J Hematol | Efficacy/safety of rpFVIII in Japanese AHA patients (NCT04580407) |
| [37510704](https://pubmed.ncbi.nlm.nih.gov/37510704/) | 2023 | Case Series/Review | J Clin Med | Surgical prophylaxis with susoctocog-alfa in AHA |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | PK Study | J Thromb Haemost | PK-guided dosing strategies for precise FVIII control |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Real-world Registry | Blood Transfus | 9 elderly AHA patients, Italian multicentre real-world experience |
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review | Drugs | Comprehensive review, original pivotal Phase II/III trial (n=28) supporting approval |

---

## Market Information

Not marketed; no authorizations on record (`total_licenses: 0`, `licenses: []`).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/label warnings and contraindications data is flagged as a **Blocking** data gap (DG001) in this evidence pack — this alone prevents a full safety (S1) evaluation regardless of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-ranked prediction (primary release disorder of platelets) has no clinical trial or literature support and is flagged by the model's own rationale as a likely knowledge-graph artifact. The only mechanistically sound, evidence-backed candidates (hemophilia, acquired coagulation factor deficiency) are not genuinely novel — they overlap with the drug's known original indication — so this pack does not currently support a new repurposing opportunity. A Blocking safety data gap (label warnings/contraindications) further precludes proceeding.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/EMA label warnings, contraindications, and DDI data before any safety evaluation
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Correct the `original_indications` field to reflect the drug's actual approved use (acquired hemophilia A) so future TxGNN predictions are properly filtered against known indications
- If a genuinely novel indication is desired, re-run prediction excluding hemophilia-adjacent disease clusters and require ≥L3 evidence before advancing to guardrail review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

