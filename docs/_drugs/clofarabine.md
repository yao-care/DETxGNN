---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a purine nucleoside antimetabolite historically used for relapsed/refractory paediatric acute lymphoblastic leukaemia (ALL).
The TxGNN model predicts it may also be effective for **Myeloid Leukemia**,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory paediatric acute lymphoblastic leukaemia (ALL) — approved in other markets (e.g., US FDA, 2004); no German marketing authorization on record |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed proprietary mechanism-of-action data (DrugBank field) is currently unavailable (data gap DG002). Based on the literature evidence collected for this candidate, clofarabine is a second-generation purine nucleoside analog designed to combine the favourable properties of cladribine and fludarabine. It acts through three main mechanisms: inhibition of ribonucleotide reductase, inhibition of DNA polymerase (blocking DNA synthesis and repair), and disruption of mitochondrial membrane integrity leading to apoptosis (see PMID 17852710, PMID 22957815).

Clofarabine's proven efficacy is in relapsed/refractory paediatric acute lymphoblastic leukaemia (ALL), where it received accelerated FDA approval in 2004. ALL and myeloid leukaemia (AML) are both aggressive haematologic malignancies driven by uncontrolled clonal proliferation of blast cells in the bone marrow, and both are treated with DNA-damaging cytotoxic backbones (cytarabine, anthracyclines, alkylators). Because clofarabine's anti-leukaemic action is independent of lymphoid- versus myeloid-lineage specificity — it targets the DNA replication machinery common to all rapidly dividing blasts — its mechanistic rationale extends naturally from ALL to AML.

This is further supported by extensive real-world use: clofarabine has already been studied in dozens of AML-focused trials (single-agent, combination with cytarabine/idarubicin/mitoxantrone, and as conditioning for allogeneic stem cell transplantation), including a completed randomized Phase II trial (CLARA vs. HDAC, n=735) and a completed multicentre randomized Phase III trial in childhood AML (AML08), reinforcing that the TxGNN prediction reflects an indication area with substantial pre-existing clinical investigation rather than a purely speculative signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02665065](https://clinicaltrials.gov/study/NCT02665065) | Phase 3 | Active, not recruiting | 153 | Pivotal trial of Iomab-B with reduced-intensity conditioning (incl. clofarabine-containing regimens) vs. conventional care in relapsed/refractory AML |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment-development programme for older AML/high-risk MDS patients evaluating multiple chemotherapy combinations |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Completed | 735 | Randomized trial: Clofarabine/intermediate-dose cytarabine (CLARA) vs. high-dose cytarabine (HDAC) as consolidation in newly-diagnosed AML |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 2 | Completed | 116 | Randomized comparison of Clofarabine+Ara-C vs. Clofarabine+Idarubicin vs. triple combination in relapsed/refractory AML, high-grade MDS, and CML blast phase |
| [NCT00373529](https://clinicaltrials.gov/study/NCT00373529) | Phase 2 | Completed | 116 | Single-agent clofarabine efficacy in elderly untreated AML patients unlikely to benefit from intensive induction |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML as bridge to allogeneic HCT |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Phase 2 | Completed | 50 | CLAM (clofarabine, cytarabine, mitoxantrone) as first salvage regimen for relapsed/refractory AML |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Completed | 50 | Clofarabine + high-dose cytarabine + G-CSF priming in newly diagnosed AML/advanced MDS/MPN |
| [NCT00044889](https://clinicaltrials.gov/study/NCT00044889) | Phase 2 | Completed | 40 | Open-label study of clofarabine monotherapy in adult refractory/relapsed AML |
| [NCT00299156](https://clinicaltrials.gov/study/NCT00299156) | Phase 2 | Completed | 65 | Oral clofarabine weekly dosing in myelodysplastic syndrome (MDS), a myeloid precursor condition |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT (Phase III) | J Clin Oncol | AML08 multicentre randomized Phase III trial: clofarabine can replace anthracyclines/etoposide in remission induction for childhood AML |
| [18565853](https://pubmed.ncbi.nlm.nih.gov/18565853/) | 2008 | RCT | Blood | Randomized study of clofarabine vs. clofarabine+low-dose cytarabine as front-line therapy in patients ≥60 with AML/high-risk MDS |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 study | Cancer Medicine | Clofarabine+cytarabine+mitoxantrone (CLAM) shows high response rates and effective bridge to allo-HCT in refractory/relapsed AML |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Comprehensive review of clofarabine's role in AML treatment |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Review of clofarabine's role in adult AML treatment, monotherapy and combination strategies |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Review | Leukemia & Lymphoma | "Clofarabine: past, present, and future" — mechanism and synergy with other chemotherapeutics |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Review | Future Oncology | Review of clofarabine for adult AML, favourable single-agent activity vs. standard agents |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Phase 1/2 trial | Am J Hematol | Multisite trial of optimally dosed clofarabine + low-dose TBI as non-myeloablative conditioning for AML transplant |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase 1B trial | Haematologica | Clofarabine + high-dose cytarabine + liposomal daunorubicin in paediatric relapsed/refractory AML |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Translational study | Cancers | Clofarabine-based consolidation improves relapse-free survival in AML with micro-complex karyotype |

---

## Germany Market Information

Clofarabine currently holds **no marketing authorization in Germany** (BfArM records: 0 licenses, market status "not marketed").

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog / antimetabolite) |
| Myelosuppression Risk | High — as a DNA synthesis/ribonucleotide reductase inhibitor, clofarabine consistently causes significant neutropenia, thrombocytopenia, and anaemia across the dose-finding and toxicity-focused trials in this evidence pack |
| Emetogenicity Classification | Moderate to high, consistent with other purine nucleoside analogs used in leukaemia induction regimens |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes (tumour lysis syndrome risk), signs of infection during neutropenic periods |
| Handling Protection | Must follow cytotoxic drug handling regulations (PPE, closed-system transfer devices) |

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed TFDA/BfArM warnings, contraindications, and drug interaction data are not yet available for this candidate (data gap DG001, marked as a **Blocking** severity item that must be resolved before formal safety review, S1).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clofarabine's antileukaemic activity in myeloid leukaemia is supported by an unusually deep evidence base — 50 clinical trials and 20 publications, including a completed randomized Phase 2 trial (CLARA vs. HDAC, n=735) and a completed multicentre randomized Phase III trial in childhood AML (AML08) — giving an evidence level of L2. However, the drug is not currently marketed in Germany, and formal safety labelling data is missing, so progression should proceed cautiously with explicit guardrails rather than as an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (resolve blocking data gap DG001)
- Confirmed mechanism-of-action data via DrugBank API (resolve data gap DG002)
- Assessment of the German/EU regulatory pathway for market entry, since clofarabine currently has zero authorizations in Germany
- Clarification of the target AML subpopulation (age, cytogenetic risk, relapsed/refractory status) to align with the strongest existing trial evidence (e.g., CLARA regimen, older-patient front-line studies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

