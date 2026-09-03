---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 7
---

# Icatibant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Icatibant: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

> Icatibant (marketed as Firazyr) is a synthetic bradykinin B2-receptor antagonist established for treating acute attacks of Hereditary Angioedema (HAE) caused by C1-inhibitor deficiency.
> The TxGNN model's top prediction — **C1 inhibitor deficiency** — is not a genuinely new indication but essentially describes the disease icatibant already treats; the model has correctly re-identified the drug's known use rather than uncovering a novel repurposing opportunity.
> This top-ranked "prediction" is backed by **23 clinical trials** (many completed Phase 3 RCTs) and **20 publications**, but this reflects existing, well-established evidence rather than new discovery. Six lower-ranked predictions (serpinopathy, pseudo-von Willebrand disease, platelet disorders, immune myopathies) were also screened and found mechanistically unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE) due to C1-inhibitor deficiency *(inferred from clinical trial evidence; not populated in structured regulatory data — data gap)* |
| Predicted New Indication | C1 inhibitor deficiency *(effectively the same disease as the established indication above — see caveat below)* |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for icatibant is not available in DrugBank via this evidence pack. Based on information embedded in the clinical trial records themselves (e.g., NCT00097695), icatibant is described as "a bradykinin antagonist" — specifically, a selective bradykinin B2-receptor antagonist that blocks the vasodilatory and permeability-increasing effects of excess bradykinin, the mediator responsible for angioedema attacks in patients with C1-inhibitor deficiency.

**Important caveat:** the top-ranked TxGNN prediction, "C1 inhibitor deficiency," is not a distinct new indication — it is the underlying disease category for Hereditary Angioedema, which icatibant already treats as its primary approved use worldwide (e.g., under the brand Firazyr). The overwhelming clinical trial and literature evidence attached to this prediction confirms an *existing*, decades-old drug-disease relationship rather than identifying a novel repurposing candidate. This should be interpreted as a **model validation signal** (TxGNN correctly recovering a known true positive) rather than a business opportunity for repurposing.

By contrast, the model's lower-ranked predictions (ranks 2–7: serpinopathy, pseudo-von Willebrand disease, primary platelet release disorder, immune-mediated necrotizing myopathy, antisynthetase syndrome, Glanzmann thrombasthenia) have no clinical trials or literature support, and the evidence pack's own mechanistic rationale for each explicitly notes these are likely knowledge-graph proximity artifacts rather than biologically plausible links to the bradykinin B2 pathway.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Pivotal randomized, double-blind, placebo-controlled trial of SC icatibant for acute cutaneous/abdominal HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Randomized, double-blind, placebo-controlled trial (FAST-3) confirming efficacy vs placebo in acute HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | Randomized comparison of SC icatibant vs oral tranexamic acid for acute HAE attacks |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label study on safety, tolerability and efficacy of self-administered SC icatibant |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Open-label efficacy/PK/safety study of icatibant in Japanese HAE Type I/II patients |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | PK, tolerability and safety of single SC icatibant dose in pediatric/adolescent HAE patients |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Safety, efficacy and PK of icatibant in Japanese pediatric/adolescent HAE patients |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large prospective real-world registry across approved countries |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Real-world safety/efficacy of icatibant for bradykinin-induced angioedema (broader than classic HAE) |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | Completed | 115 | Real-world observational study of lanadelumab and icatibant in Chinese HAE patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Review | J Investig Allergol Clin Immunol | Comprehensive review of current and emerging therapies for C1-INH-HAE, including icatibant |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Disease burden of HAE due to C1-inhibitor deficiency in the Asia-Pacific region |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Review | Curr Opin Allergy Clin Immunol | Diagnostic and therapeutic management of C1-INH-HAE — Italian clinical experience |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Rev Clin Immunol | Efficacy and safety of icatibant in adolescents and children over 2 years with C1-INH-HAE |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Observational | Allergy Asthma Clin Immunol | Real-world icatibant outcomes in Spanish HAE patients from the IOS registry |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry Analysis | Clin Exp Allergy | Icatibant and C1-inhibitor use in treating laryngeal HAE attacks |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational | Allergy | Real-world use of icatibant in acquired (not hereditary) C1-inhibitor deficiency |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective Study | J Clin Pharmacol | High rate of off-label icatibant/C1-INH use in non-HAE bradykinin-mediated angioedema |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case Series | J Clin Immunol | Treatment of HAE attacks with icatibant and recombinant C1 inhibitor during pregnancy |
| [20496014](https://pubmed.ncbi.nlm.nih.gov/20496014/) | 2010 | Review | Intern Emerg Med | Classic review of angioedema due to C1-inhibitor deficiency and treatment approaches |

---

## Germany Market Information

Currently no marketing authorizations registered for icatibant in this market (`taiwan_regulatory.market_status` = 未上市 / Not Marketed; `total_licenses` = 0).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications and drug-interaction data are not currently available in the source registry (flagged as a **Blocking** data gap — TFDA/BfArM label warnings and contraindications must be sourced before this candidate can enter S1 safety review).

---

## Additional TxGNN Predictions (Low Confidence, Not Recommended)

The evidence pack also screened six lower-ranked predictions for icatibant. All were assessed as **L5 / Hold** — no clinical trials, no literature, and only weak or absent mechanistic plausibility relative to icatibant's bradykinin B2-antagonist pharmacology:

| Rank | Disease | Score | Verdict |
|------|---------|-------|---------|
| 2 | Serpinopathy with toxic serpin polymerization | 99.99% | Indirect graph link only (SERPING1 family); B2-antagonism does not affect serpin misfolding |
| 3 | Pseudo-von Willebrand disease | 99.21% | No known mechanistic overlap with bradykinin pathway |
| 4 | Primary platelet release disorder | 99.14% | No known biological link |
| 5 | Immune-mediated necrotizing myopathy | 99.06% | Complement/immune-driven; no overlap with B2 antagonism |
| 6 | Antisynthetase syndrome | 99.02% | Autoantibody-driven; no known kinin-system link |
| 7 | Glanzmann thrombasthenia | 99.00% | Congenital GPIIb/IIIa defect; unrelated pathway |

These should not be pursued further without new mechanistic or preclinical evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest predicted indication (C1 inhibitor deficiency) is not a novel repurposing opportunity — it is the drug's already-established use, so it does not represent new commercial or clinical value. Combined with the drug's absence from this market (0 authorizations) and a **Blocking** data gap on TFDA/BfArM label warnings and contraindications, the candidate cannot yet proceed to a safety evaluation stage regardless of its efficacy evidence.

**To proceed, the following is needed:**
- Obtain the official product label (warnings, contraindications) from TFDA/BfArM to close the Blocking safety data gap
- Retrieve DrugBank MOA data to formally document the bradykinin B2-antagonist mechanism
- Reframe the repurposing search: since rank-1 duplicates the known indication, prioritize deeper mining of off-label evidence (e.g., ACE-inhibitor-induced angioedema, acquired C1-INH deficiency — both already appearing in the literature set) as more genuine repurposing candidates than the six low-confidence graph predictions listed above
- If market entry (not repurposing) is the actual goal, initiate standard registration dossier submission for the existing HAE indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

