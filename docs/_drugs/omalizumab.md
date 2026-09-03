---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab (Xolair) is a recombinant humanized anti-IgE monoclonal antibody internationally approved for moderate-to-severe allergic asthma and chronic spontaneous urticaria (CSU); it is not currently marketed in Germany, so no local licensing text is available to confirm the original indication wording. The TxGNN model's top-ranked new-indication prediction for this drug is **Bronchitis**, supported by **2 clinical trials** and **8 publications** — but on review, essentially none of this evidence involves patients actually diagnosed with bronchitis, so the signal should be treated with caution rather than as an actionable repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in the Germany license registry (drug not marketed there); internationally approved for allergic asthma and chronic spontaneous urticaria (CSU) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% (internal rank 30 among all candidate diseases) |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The DrugBank-sourced mechanism-of-action field for Omalizumab is currently a data gap. Based on information distributed throughout this evidence pack's clinical trial and literature summaries, Omalizumab is a recombinant humanized monoclonal antibody that binds free serum IgE and blocks its interaction with the high-affinity FcεRI receptor on mast cells and basophils. This interrupts the IgE-mediated allergic inflammatory cascade and is the well-established mechanism underlying its approved use in allergic asthma and CSU — both conditions referenced repeatedly across the clinical-trial evidence in this pack, even though they do not appear in the `taiwan_regulatory.licenses` field because the drug is not marketed in Germany.

Bronchitis and allergic asthma share anatomical territory (the bronchi) and some overlapping symptoms (cough, airway inflammation), which is likely why the TxGNN embedding space places them close together. However, airway inflammation in bronchitis is typically driven by infection or irritant exposure rather than IgE-mediated type-I hypersensitivity, so the mechanistic rationale for extending an anti-IgE antibody to bronchitis specifically (as opposed to allergic asthma, which Omalizumab already treats) is weak.

Critically, when the retrieved evidence is inspected, it does not actually support a bronchitis-specific effect: both clinical trials enrolled asthma or CSU populations rather than bronchitis patients, and of the 8 literature items, only one explicitly discusses bronchitis (PMID 31478531), and that is a case report of *plastic bronchitis occurring as a complication of bronchial thermoplasty* — a procedural adverse event, not therapeutic evidence for Omalizumab treating bronchitis. This pattern is consistent with a disease-ontology proximity artifact rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Steroid-sparing effect of Omalizumab in patients with **asthma and persistent eosinophilic bronchitis** (add-on to prednisone). *Relevance grade C — study population is primarily asthma, not bronchitis as a standalone diagnosis.* |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding study of QGE031 (ligelizumab) vs. placebo as add-on therapy in **chronic spontaneous urticaria (CSU)**. *Relevance grade C — no bronchitis population; captured only via drug-class/mechanism adjacency.* |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opinion on Pharmacotherapy | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema, asthma-COPD overlap) and notes patients with these conditions are typically excluded from asthma biologic trials. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Safety Cohort | Current Medical Research and Opinion | Pooled safety analysis of Omalizumab in **children with allergic asthma**; no bronchitis-specific data. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical Reviews in Allergy & Immunology | Post-approval experience of Omalizumab in **moderate-to-severe persistent asthma**; establishes the drug's approved-use context, not bronchitis. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postępy Dermatologii i Alergologii | Omalizumab in older patients with severe **allergic asthma–COPD overlap**; airway obstruction context but not bronchitis specifically. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Narrative Review | Masui (Japanese J. Anesthesiology) | Preoperative management guidance for patients with bronchial asthma **or** chronic bronchitis; mentions Omalizumab only in the asthma-treatment context. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Revue des Maladies Respiratoires | French expert review of adult asthma exacerbations; general disease-management review, no bronchitis-specific efficacy data. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergologia et Immunopathologia | General pediatric overview of monoclonal antibodies (including anti-IgE) across allergic and neoplastic diseases; not bronchitis-focused. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J. Investigational Allergology & Clinical Immunology | Reports a rare case of **plastic bronchitis as a complication following bronchial thermoplasty** — a procedural adverse event, not evidence of Omalizumab efficacy against bronchitis. |

---

## Germany Market Information

Omalizumab is currently **not marketed in Germany** according to this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No BfArM authorization records are available to summarize product names, dosage forms, or approved indication wording.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable at this time (DDI query status: not found). Note that the underlying TFDA/BfArM package-insert warnings and contraindications are flagged in this evidence pack as a **Blocking**-severity data gap (DG001), meaning a formal safety pre-screen (S1) cannot yet be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top TxGNN-ranked new indication for Omalizumab, Bronchitis (score 99.9992%), is not substantiated by its supporting evidence: both retrieved clinical trials enrolled asthma/CSU populations (relevance grade C, not bronchitis), and 7 of 8 literature items are general asthma/airway-disease reviews with no bronchitis-specific efficacy data — the one item that does name bronchitis directly is a case report of a treatment-related complication, not a therapeutic finding.
- Evidence level is L4 (mechanism/preclinical-tier) with decision stage S0, indicating the signal likely reflects disease-ontology proximity in the model's embedding space (bronchitis sharing anatomical/symptom overlap with asthma) rather than a genuine pharmacological effect specific to bronchitis.

**To proceed, the following is needed:**
- TFDA/BfArM package insert (warnings, contraindications) — currently a Blocking data gap (DG001) required before any S1 safety pre-screen.
- A confirmed, structured original mechanism-of-action (MOA) record from DrugBank (DG002), rather than the pack's supplementary/inferred description.
- Clinical evidence enrolling patients with a confirmed bronchitis diagnosis (as opposed to asthma or CSU patients captured via keyword/ontology overlap) before this candidate can be re-scored.

---

### Additional Note: Other TxGNN-Predicted Indications in This Evidence Pack

This evidence pack evaluated Omalizumab against 10 candidate indications. While Bronchitis carries the highest TxGNN model score, it is not the strongest evidence-supported candidate in the set. For context:

| Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Obstructive lung disease | 99.97% | L1 | Proceed with Guardrails | Extensive Phase 3/4 RCT support (e.g., NCT00314574, n=850; NCT00401596, n=1899); mechanistically this largely reflects Omalizumab's *already-established* allergic asthma activity rather than a novel repurposing opportunity. |
| Atopic eczema | 99.97% | L2 | Research Question | One direct Phase 4 RCT (NCT02300701, n=62) plus mixed literature, including a case report of Omalizumab-*induced* dermatitis — efficacy signal is inconsistent. |
| Dermatitis | 99.97% | L2 | Research Question | Shares nearly the same evidence pool as atopic eczema; likely a duplicate signal from the same disease cluster rather than an independent finding. |
| Bronchial neoplasm | 99.95% | L5 | Hold | No mechanistic or clinical basis; both retrieved records are asthma-context only. |
| Acne keloid / acrodermatitis chronica atrophicans / hydroa vacciniforme / neonatal dermatomyositis / secondary childhood ILD | 99.9–99.94% | L5 | Hold | Zero clinical trials or literature; no mechanistic rationale. |

For future prioritization, "Obstructive lung disease" and, separately, "Atopic eczema"/"Dermatitis" (recommended to be evaluated jointly given overlapping evidence) merit more attention than Bronchitis alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

