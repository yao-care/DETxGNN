---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Paliperidone is a D2/5-HT2A receptor antagonist used clinically to treat schizophrenia.
> The TxGNN model's top-ranked prediction is **Retinal Dystrophy with or without Extraocular Anomalies**,
> but this candidate has **0 clinical trials** and **15 publications**, none of which mention paliperidone or its pharmacology — the drug's own evidence pack flags this as a likely embedding-similarity false positive rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in BfArM/regulatory data (product not marketed in Germany); known clinical use is schizophrenia, inferred from mechanism notes elsewhere in this evidence pack |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

**It is not.** Detailed MOA data is marked as a data gap in the drug record, but the evidence pack's own rationale field (drawn from the rank-10 candidate) confirms paliperidone is a D2/5-HT2A receptor antagonist — a centrally acting antipsychotic mechanism with no known connection to retinal developmental genes or ophthalmic structural pathways.

The retinal dystrophy prediction ranks #1329 out of the model's full output and carries a very high raw similarity score, but score magnitude alone does not establish biological plausibility. The 15 supporting publications retrieved for this candidate cover unrelated ophthalmology topics — orbital infections, diplopia, congenital ptosis, cryptophthalmia, congenital cranial dysinnervation disorders — and **none reference paliperidone, antipsychotics, or D2/5-HT2A signaling**. The evidence pack itself characterizes this as a probable false positive caused by embedding-space similarity rather than a real mechanistic link.

Candidates ranked #2–#9 (X-linked myopia, hydranencephaly, congenital disorders of glycosylation, Charcot-Marie-Tooth disease type 1G, etc.) share the same pattern: high TxGNN scores, zero supporting trials or literature, and no plausible mechanistic rationale given the drug's known pharmacology. By contrast, the #10-ranked candidate — **treatment-refractory schizophrenia** — is mechanistically coherent (it sits within paliperidone's known therapeutic class) and is the only candidate in this pack backed by real clinical trial and literature evidence (see Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review/Case | Semin Ultrasound CT MR | Orbital infections secondary to sinusitis; not related to paliperidone or retinal dystrophy pathophysiology |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Diagnostic approach to diplopia; unrelated to drug mechanism |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of pediatric congenital ocular pathologies; no drug relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital lens shape anomalies; no drug relevance |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis pathophysiology; no drug relevance |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Unilateral cryptophthalmia case series; no drug relevance |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome vitreoretinal degeneration; no drug relevance |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Cohort | Int J Mol Sci | Optic nerve/retinal findings in congenital fibrosis of extraocular muscles; no drug relevance |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders overview; no drug relevance |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmol | Maculopathy from cavitary optic disc anomalies; no drug relevance |

None of the retrieved literature mentions paliperidone, antipsychotics, or dopaminergic/serotonergic mechanisms — confirming these are topical co-retrieval matches rather than mechanistic evidence.

---

## Germany Market Information

Paliperidone is **not marketed in Germany**; no BfArM authorizations are on record in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** TFDA/BfArM label data (warnings, contraindications) is flagged as a **Blocking** data gap in this evidence pack (DG001) and could not be retrieved — this must be resolved before any S1 safety screening can proceed, regardless of which indication is pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (retinal dystrophy with or without extraocular anomalies) has no clinical trials, no relevant literature, and no plausible mechanistic link to paliperidone's D2/5-HT2A antagonism — the evidence pack itself identifies it as a likely false positive from embedding similarity. The same applies to candidates ranked #2–#9.

**To proceed, the following is needed:**
- Resolve the Blocking data gap: obtain TFDA/BfArM label (warnings, contraindications) before any safety screening
- Obtain confirmed MOA and original indication documentation for paliperidone (currently marked as data gaps)
- If pursuing repurposing work on this drug, redirect evaluation toward **rank #10 (treatment-refractory schizophrenia)**, which is the only candidate with real supporting evidence (L2, 4 clinical trials including one completed Phase 4 study, 2 literature reviews) — note this represents an indication-extension within paliperidone's existing therapeutic class rather than a novel repurposing signal, and would still require head-to-head comparative data against clozapine (the current standard for treatment-refractory schizophrenia) before advancing past S2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

