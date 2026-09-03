---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

> Tobramycin is an aminoglycoside antibiotic historically used to treat serious gram-negative bacterial infections (systemic, respiratory, and ophthalmic). The TxGNN model predicts it may be effective for **Exposure Keratitis**, with **2 clinical trials** and **7 publications** currently identified as supporting evidence — though most of this evidence is indirect (case reports and in vitro toxicity data rather than trials designed specifically for this indication).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from evidence pack (no licenses/approved indication text on file). Based on general pharmacological classification, tobramycin is an aminoglycoside antibiotic used for serious gram-negative bacterial infections. |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (observational case reports + non-RCT trials; no completed RCT specific to this indication) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tobramycin belongs to the aminoglycoside antibiotic class, and its efficacy against gram-negative bacterial infections (including *Pseudomonas aeruginosa*) has been well established in systemic, inhaled, and ophthalmic formulations. Mechanistically, this broad antibacterial activity may be applicable to exposure keratitis.

Exposure keratitis is a mechanical/neurological condition — typically caused by incomplete eyelid closure (e.g., in sedated, comatose, or facial-nerve-palsy patients) — that leaves the cornea chronically exposed and vulnerable to desiccation and **secondary bacterial infection**. Tobramycin is not expected to treat the underlying exposure mechanism itself, but rather to prevent or treat the secondary bacterial keratitis that frequently complicates it. This is directly illustrated in the literature evidence below, where a patient unable to close his eyes (vegetative state) developed bacterial keratitis requiring antibiotic management — a scenario structurally analogous to exposure keratitis.

Ophthalmic tobramycin already has an established, decades-long track record of off-label and on-label use for bacterial keratitis and corneal ulcers, which supports the biological plausibility of this prediction. However, the specific clinical trials linked to this indication (dendritic viral ulcer treatment, PRF membrane for ophthalmic diseases) do not directly test tobramycin for exposure keratitis, so the trial evidence should be interpreted as topically adjacent rather than confirmatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Evaluates treatment modalities for dendritic viral (HSV) corneal ulcers; addresses infectious keratitis management broadly, not tobramycin-specific exposure keratitis therapy. |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Investigates platelet-rich fibrin (PRF) membrane for ocular surface conditions including corneal ulcer; tobramycin not the primary intervention studied. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro mechanism study | Current Eye Research | Compares corneal epithelial cytotoxicity of aminoglycosides (including tobramycin) in a rabbit model — relevant to safety of topical use on compromised (exposed) corneal epithelium. |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Susceptibility/comparative study | Nippon Ganka Gakkai Zasshi | Compares MIC and postantibiotic effect of antibiotic eyedrops (including tobramycin) against infectious keratitis isolates in Japan. |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Describes bacterial keratitis in a patient unable to voluntarily close his eyes (vegetative state) — a direct clinical analogue of exposure keratitis with secondary infection. |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-associated *Bacillus cereus* keratitis and ulcer. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospective case series | Polish Journal of Veterinary Sciences | Seroprevalence, diagnosis, and treatment outcomes in feline ocular toxoplasmosis (60 cases); limited direct human relevance. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao / Eye Science | Reports paracentral corneal dellen as a rare sign of Graves ophthalmopathy — a corneal exposure-related condition, though not treatment-focused. |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This evaluation identified a **Blocking**-severity data gap — TFDA/official label warnings and contraindications for tobramycin are not currently on file — which must be resolved before formal safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale for using tobramycin in exposure-keratitis-associated secondary bacterial infection is biologically plausible and supported by one directly relevant case report, but the overall evidence base is L3 (case reports and non-specific trials) — not yet sufficient for a "Go" decision.
- A **Blocking** data gap exists: official label warnings/contraindications (DG001) are unavailable, which by definition prevents entry into the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- Obtain TFDA (or equivalent) approved product label — warnings, contraindications, dosing (DG001, Blocking)
- Obtain confirmed mechanism of action / DrugBank pharmacology data (DG002, High)
- Assess whether NCT05313828 and NCT06200727 include tobramycin-treated arms directly applicable to exposure keratitis, or seek trials with a more direct design
- Clarify current regulatory/market status, since the drug is presently recorded as "Not Marketed" with zero active authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

