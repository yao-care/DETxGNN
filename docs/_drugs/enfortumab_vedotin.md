---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Enfortumab Vedotin: From Urothelial (Bladder) Cancer to Leprosy

## One-Sentence Summary

> Enfortumab vedotin is an antibody-drug conjugate (ADC) whose established clinical use context in this evidence pack is advanced/metastatic **bladder (urothelial) cancer**.
> The TxGNN model's top-ranked prediction for this drug is **Leprosy**, with a raw score of 99.53%,
> but **zero clinical trials and zero publications** currently support this specific drug–disease pairing, and the model's own mechanistic rationale explicitly finds **no plausible biological link**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in structured `original_indications`/regulatory license data (data gap). Contextual literature evidence in this pack (PMID 41341429) identifies enfortumab vedotin as an ADC used in **advanced bladder cancer** patients — this is the only indication context available. |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% (raw score 0.9953; global candidate rank 5,642) |
| Evidence Level | L5 — model prediction only, no supporting clinical trials or literature |
| Germany Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, the structured mechanism-of-action field for enfortumab vedotin is a documented data gap (DG002, High severity). However, the model's own repurposing-rationale text consistently and independently describes the drug across multiple candidate entries as an **anti-Nectin-4 antibody-drug conjugate (ADC)**: an antibody targeting the Nectin-4 tumor surface antigen delivers a microtubule-disrupting cytotoxin (MMAE, monomethyl auristatin E) into antigen-expressing cells, producing direct cytotoxicity.

Leprosy, by contrast, is an infectious disease caused by *Mycobacterium leprae*, treated through antimycobacterial chemotherapy (e.g., multidrug therapy with dapsone, rifampicin, clofazimine) rather than targeted cytotoxic delivery. There is no known Nectin-4 involvement in *M. leprae* pathophysiology, and no receptor- or pathway-level overlap between an antimycobacterial mechanism and a tumor-antigen-directed cytotoxic payload.

**This is stated directly in the evidence pack's own repurposing rationale**: "Enfortumab vedotin ... shows no known association with antimycobacterial infection mechanisms, and no receptor/pathway overlap evidence exists." In other words, the source data itself concludes the mechanistic hypothesis is unsupported — this is a pure similarity-based model output (TxGNN rank 5,642, well outside typical high-confidence prediction territory) with no corroborating clinical, preclinical, or literature signal. This prediction should be treated as exploratory/noise-level rather than a genuine repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Enfortumab vedotin currently holds **no marketing authorizations** on record for this market (0 licenses; market status: Not Marketed). No authorization table can be produced.

---

## Cytotoxicity

Enfortumab vedotin's underlying drug class (per repurposing-rationale text embedded in this evidence pack) is an antibody-drug conjugate delivering a microtubule-inhibitor payload, i.e., a cytotoxic anticancer agent, so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (anti-Nectin-4 antibody + MMAE microtubule inhibitor payload) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

*(Detailed toxicity/warning data could not be retrieved — this is a documented Blocking data gap, DG001: TFDA/package-insert warnings and contraindications, required before any Stage 1 safety screening.)*

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction carries no clinical, preclinical, or literature support (0 trials, 0 publications), sits at evidence level L5, and the model's own mechanistic rationale explicitly states there is no known biological link between an anti-Nectin-4 ADC's cytotoxic mechanism and leprosy's infectious/antimycobacterial treatment paradigm. There is no basis to advance this candidate past initial screening.

**To proceed, the following is needed:**
- Formal DrugBank/regulatory mechanism-of-action (MOA) data (DG002)
- TFDA/package-insert warnings, contraindications, and drug-interaction data (DG001, Blocking — required before any safety evaluation can begin, for this drug in general, regardless of indication)
- Independent biological rationale (e.g., Nectin-4 expression or relevant target expression in leprosy-affected tissue, or any published case reports) before this pairing is worth further investment
- Given the complete absence of supporting evidence, this candidate is not recommended for further evaluation resources at this time

---

### Appendix: Other Model-Predicted Indications Reviewed (Ranks 2–9)

For completeness, the remaining top-9 TxGNN predictions in this evidence pack were also reviewed and show the same pattern — no supporting trials, and mechanistic rationales that consistently argue *against* biological plausibility:

| Rank | Predicted Disease | Score | Note |
|------|------|------|------|
| 2 | Multiple endocrine neoplasia | 99.43% | Genetic (MEN1/RET) endocrine tumor syndrome; no evidence of Nectin-4 expression relevance |
| 3 | Cytomegalovirus infection | 99.36% | Viral infection; cytotoxic ADC mechanism has no antiviral rationale and could theoretically worsen infection risk via myelosuppression |
| 4 | Candidiasis | 99.30% | Sole literature hit (PMID 41341429) is a FAERS pharmacovigilance signal describing candidiasis as an **adverse event** in ADC-treated bladder cancer patients — i.e., evidence of harm, not efficacy; this should not be read as supportive |
| 5 | Cerebral infarction | 99.23% | Ischemic vascular disease; no mechanistic overlap, and ADC-related toxicities (myelosuppression, neuropathy) run counter to this indication |
| 6 | HIV infectious disease | 99.19% | Antiretroviral mechanism unrelated to ADC cytotoxicity |
| 7 | Homozygous familial hypercholesterolemia | 99.18% | Lipid-metabolism/LDL-receptor disorder; no pharmacologic overlap |
| 8 | Malignant catarrh (malignant catarrhal fever) | 99.13% | **Veterinary disease** (bovine/ruminant herpesvirus) — likely a cross-species ontology mapping artifact, not a valid human indication |
| 9 | Infectious bovine rhinotracheitis | 99.13% | **Veterinary disease** (bovine herpesvirus-1) — same likely ontology artifact as rank 8 |

**Recommendation:** None of the top-9 candidates in this batch meet even preliminary plausibility thresholds. Ranks 8–9 in particular suggest a data-quality/ontology-mapping issue (veterinary vs. human disease terms) that may warrant a knowledge-graph data-cleaning review rather than clinical follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

