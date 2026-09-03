---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

> Velpatasvir is an NS5A inhibitor originally developed as part of the sofosbuvir/velpatasvir (Epclusa) combination for chronic hepatitis C virus (HCV) infection. The TxGNN model predicts potential efficacy against hepatitis B virus (HBV) infection with a very high score, but of the **26 clinical trials** and **20 publications** retrieved for this candidate, virtually all describe HCV treatment — the sole item directly linking the drug to HBV is a case report of HBV reactivation during HCV therapy, which is a safety signal rather than efficacy evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (component of sofosbuvir/velpatasvir combination) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for velpatasvir is flagged as a data gap in this evidence pack. Based on information embedded in the trial and literature records, however, velpatasvir is a **hepatitis C virus (HCV) NS5A inhibitor**, marketed in combination with the NS5B polymerase inhibitor sofosbuvir (Epclusa) as a pan-genotypic treatment for chronic HCV infection.

The predicted new indication — hepatitis B virus infection — does not share this mechanistic target. HBV is a hepadnavirus that replicates via reverse transcription of pregenomic RNA and depends on persistent nuclear cccDNA, a biology entirely distinct from the HCV NS5A protein that velpatasvir inhibits. Despite the strong TxGNN score, this prediction most likely reflects surface-level similarity (both are hepatotropic viruses causing chronic liver disease) rather than shared drug-target biology.

Notably, the one piece of literature that directly connects velpatasvir to HBV (PMID 31542053) describes **HBV reactivation** in a patient who was hepatitis B core antibody-positive while being treated with sofosbuvir/velpatasvir for HCV — a well-recognized DAA-class safety concern about unmasking latent HBV, not evidence of anti-HBV efficacy. This should be read as a caution flag for HBV/HCV co-infected patients, not as support for repurposing velpatasvir to treat HBV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL with prophylactic TAF in treatment-naïve HCV/**HBV co-infected** patients — designed to prevent HBV reactivation during HCV therapy, not to treat HBV itself |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | SOF/VEL ± ribavirin in HIV/HCV co-infected patients (graded C: unrelated to HBV) |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | SOF/VEL ± ribavirin in HCV decompensated cirrhosis (graded C: unrelated to HBV) |
| [NCT02994056](https://clinicaltrials.gov/study/NCT02994056) | Phase 2 | Completed | 32 | SOF/VEL + ribavirin in HCV Child-Pugh-Turcotte Class C cirrhosis (graded C: unrelated to HBV) |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV co-infected patients |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completed | 803 | Simplified HCV testing/treatment strategy in Myanmar, integrated with HIV care |
| [NCT03086044](https://clinicaltrials.gov/study/NCT03086044) | Phase 4 | Unknown | 148 | Organ transplantation from HCV-positive donors to HCV-uninfected recipients |
| [NCT03987503](https://clinicaltrials.gov/study/NCT03987503) | Phase 4 | Completed | 87 | Community-based point-of-diagnosis HCV treatment feasibility study |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Vosevi (SOF/VEL/VOX) efficacy in patients who failed prior DAA therapy for HCV |
| [NCT01457768](https://clinicaltrials.gov/study/NCT01457768) | N/A | Completed | 570 | Long-term registry of HCV patients who failed to achieve sustained virologic response |

**Note:** None of these trials directly evaluate velpatasvir for treatment of hepatitis B; HBV appears only as a co-infection or reactivation-monitoring context.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of Medical Case Reports | HBV reactivation (immune-escape mutant) in an HBcAb-positive patient during sofosbuvir/velpatasvir treatment for HCV — a safety signal, not efficacy evidence |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohort | Lancet Gastroenterology & Hepatology | SOF/VEL safety/efficacy in treatment-naïve HCV genotype 4 patients in Rwanda (SHARED-3) |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort (pending) | Lancet Gastroenterology & Hepatology | SOF/VEL/VOX re-treatment in HCV patients with prior DAA failure in Rwanda (SHARED-3) |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Pending | Journal of Viral Hepatitis | Simplified HCV treatment strategy in Myanmar; **HBV co-infected participants treated concurrently with tenofovir**, not velpatasvir |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Pending | World Journal of Gastroenterology | Review of pediatric viral hepatitis management, covering both HBV and HCV DAAs as separate disease entities |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Pending | Annals of Hepatology | Cross-sectional comparison of HBV and HCV antiviral drug pricing (health-economics focus, not efficacy) |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Pending | Journal of Gastroenterology and Hepatology | Real-world SOF/VEL ± ribavirin efficacy/safety in HCV genotype 3 |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Pending | Cureus | SOF/VEL efficacy in HCV patients with chronic kidney disease |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Pending | European Journal of General Practice | General review of chronic HCV diagnosis and treatment |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Pending | Clinical Pharmacokinetics | Review of HCV DAA pharmacokinetics/pharmacodynamics, including SOF/VEL |

**Note:** No literature reports velpatasvir being used or studied as a treatment for hepatitis B infection itself.

---

## Taiwan Market Information

Velpatasvir currently holds **no marketing authorization in Taiwan** (未上市, 0 licenses on record). No product listing or approved indication text is available for review.

---

## Safety Considerations

- **Formal safety data (warnings, contraindications, drug interactions) are not available** in the current evidence pack — please refer to the international package insert (e.g., Epclusa US/EU labeling) for authoritative safety information.
- **Evidence-derived safety signal:** One case report (PMID 31542053) documents HBV reactivation, driven by an HBsAg immune-escape mutant, in a patient who was HBcAb-positive during sofosbuvir/velpatasvir treatment for HCV. This is consistent with the well-established DAA-class warning that HBV/HCV co-infected or HBV-exposed patients require HBV monitoring (and often antiviral prophylaxis, as reflected in NCT04997564) when receiving sofosbuvir/velpatasvir — **not** an indication that velpatasvir treats HBV.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no mechanistic or empirical basis for velpatasvir as an HBV treatment. All available clinical trial and literature evidence pertains to HCV therapy (with HBV appearing only as a co-infection/reactivation-monitoring context), and the sole HBV-specific literature finding is a reactivation safety signal that argues for caution, not efficacy.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (DG002) to formally assess target relevance to HBV
- TFDA label warnings/contraindications (DG001) — currently a blocking data gap for any S1 safety review
- Preclinical or in vitro evidence of anti-HBV activity for velpatasvir, which does not currently exist in the evidence pack
- If pursued at all, reframe the research question toward **HBV reactivation risk management** in HCV/HBV co-infected patients rather than HBV treatment efficacy

*Note: Lower-ranked candidates in this evidence pack (hepatitis E, hepatitis A, HIV, and various zoonotic/rare-disease predictions) show even weaker or no supporting evidence and are not analyzed further in this report; all carry "Hold" recommendations.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

