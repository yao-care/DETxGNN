---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using no specific skill here — this is a direct content-generation task governed by the detailed report template already provided in the system prompt, so I'll follow it directly.

**Note before the report:** This evidence pack contains 6 TxGNN-predicted indications for zidovudine with widely varying evidence quality (from feline/monkey animal-model literature to a genuine human RCT base). Per the Evidence Level rules, only **AIDS-related complex (ARC)** clears L1 with an actionable "Proceed with Guardrails" call — the others are explicitly scored `Hold`/L4–L5 or lack real clinical relevance to humans (e.g., feline AIDS, SIV in macaques). I built the report around ARC as the primary candidate and summarized the rest as screened-and-held, rather than mechanically using rank #1 (feline AIDS), which would produce a clinically meaningless report.

---

# Zidovudine: From HIV Infection to AIDS-Related Complex

## One-Sentence Summary

> Zidovudine (AZT) was the first antiretroviral drug ever approved, originally developed to suppress HIV replication in patients with symptomatic HIV infection.
> Among six indications flagged by the TxGNN model for this drug, **AIDS-Related Complex (ARC)** is the only one backed by substantial human clinical evidence,
> with **50 clinical trials** and **10+ publications** — including the landmark 1987 NEJM placebo-controlled trial — supporting its use in this early symptomatic stage of HIV disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS (zidovudine's originally approved indication; the regulatory license text was not available in this evidence pack) |
| Predicted New Indication | AIDS-Related Complex (ARC) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L1 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available in this evidence pack. Based on established pharmacology, zidovudine is a thymidine-analogue **nucleoside reverse transcriptase inhibitor (NRTI)**: after intracellular phosphorylation to its triphosphate form, it competitively inhibits HIV reverse transcriptase and causes DNA chain termination, blocking viral replication.

AIDS-Related Complex is not a distinct disease from HIV infection — it is the historical clinical staging term (pre-1993 CDC classification) for symptomatic but not yet AIDS-defining HIV disease. Zidovudine's original approval already covered this disease stage; the TxGNN "prediction" here largely re-identifies the drug's own founding indication rather than a novel repurposing target. This is reflected in the evidence pack's own rationale note: *"this is not strict repurposing but a continuation of the historically approved indication."*

The mechanistic applicability is therefore self-evident — the same reverse-transcriptase-inhibition mechanism that defines zidovudine's approved use in HIV/AIDS directly extends to ARC, a milder stage of the same underlying infection.

**Other TxGNN candidates screened and held:** The model also flagged feline acquired immunodeficiency syndrome and simian immunodeficiency virus infection (both non-human veterinary/primate model diseases used only in translational AZT research, not independent human indications, L4–L5, Hold), an unrelated rare neurodevelopmental disorder and "obsolete familial combined hyperlipidemia" (no supporting literature; the latter contradicts known NRTI-associated mitochondrial toxicity/lipodystrophy, judged a likely false positive), and congenital HIV (evidence pending classification). None of these met the bar for further action at this time.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001011](https://clinicaltrials.gov/study/NCT00001011) | Phase 3 | Completed | 538 | Safety and usefulness of AZT specifically in patients with early symptomatic HIV/early ARC |
| [NCT00002334](https://clinicaltrials.gov/study/NCT00002334) | Phase 3 | Completed | 3000 | AZT alone vs. AZT+ddC vs. AZT+saquinavir vs. triple combination in AZT-naive patients |
| [NCT00000736](https://clinicaltrials.gov/study/NCT00000736) | Phase 3 | Completed | 3200 | AZT delays onset of AIDS/ARC in asymptomatic HIV-infected individuals; dose-comparison for toxicity |
| [NCT00001022](https://clinicaltrials.gov/study/NCT00001022) | Phase 3 | Completed | 1200 | AZT vs. AZT+ddI vs. AZT+ddC in delaying AIDS-related conditions |
| [NCT00000625](https://clinicaltrials.gov/study/NCT00000625) | Phase 2 | Completed | 2100 | AZT monotherapy vs. combination nucleoside analogs in patients with CD4 200–500/mm³ |
| [NCT00000751](https://clinicaltrials.gov/study/NCT00000751) | Phase 3 | Completed | 1600 | HIVIG plus intrapartum/newborn AZT for prevention of mother-to-child HIV transmission |
| [NCT00000637](https://clinicaltrials.gov/study/NCT00000637) | Phase 3 | Completed | 819 | AZT vs. ddI vs. AZT+ddI in symptomatic HIV-infected children |
| [NCT00002035](https://clinicaltrials.gov/study/NCT00002035) | RCT | Completed | 300 | Double-blind comparison of continued AZT vs. ddI in patients failing AZT (Grade A relevance) |
| [NCT00002290](https://clinicaltrials.gov/study/NCT00002290) | RCT | Completed | N/A | Multi-center double-blind trial of AZT + acyclovir vs. AZT alone in early symptomatic HIV (Grade A) |
| [NCT00001104](https://clinicaltrials.gov/study/NCT00001104) | Phase 3 | Completed | 538 | Placebo-controlled trial of AZT in HIV-infected hemophilic patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3299089](https://pubmed.ncbi.nlm.nih.gov/3299089/) | 1987 | RCT | New England Journal of Medicine | Landmark double-blind, placebo-controlled trial (N=282) establishing AZT efficacy in AIDS/advanced ARC |
| [2677429](https://pubmed.ncbi.nlm.nih.gov/2677429/) | 1989 | RCT | JAMA | Long-term AZT therapy in 229 AIDS/ARC patients; survival benefit maintained over ~21 months |
| [1777174](https://pubmed.ncbi.nlm.nih.gov/1777174/) | 1991 | RCT | AIDS | European-Australian trial (N=199): AZT ± acyclovir for ARC; no added benefit from acyclovir |
| [8096703](https://pubmed.ncbi.nlm.nih.gov/8096703/) | 1993 | RCT | AIDS | Double-blind randomized trial confirming AZT ± acyclovir efficacy/safety in AIDS and ARC |
| [2159707](https://pubmed.ncbi.nlm.nih.gov/2159707/) | 1990 | RCT | American Journal of Medicine | ACTG Phase I/II combination AZT + ddC in AIDS/advanced ARC |
| [2159705](https://pubmed.ncbi.nlm.nih.gov/2159705/) | 1990 | RCT | American Journal of Medicine | Alternating/intermittent AZT + ddC dosing regimens to reduce toxicity in AIDS/ARC |
| [2191113](https://pubmed.ncbi.nlm.nih.gov/2191113/) | 1990 | RCT | J Acquir Immune Defic Syndr | Quality-of-life substudy of placebo-controlled AZT trial; improved Karnofsky/QWB scores vs. placebo |
| [3059187](https://pubmed.ncbi.nlm.nih.gov/3059187/) | 1988 | RCT | New England Journal of Medicine | Double-blind, placebo-controlled trial (N=281) assessing neuropsychological outcomes of AZT in AIDS/ARC |
| [1894937](https://pubmed.ncbi.nlm.nih.gov/1894937/) | 1991 | Clinical study | Journal of Infectious Diseases | AZT-treated AIDS/ARC patients show improved antibody response to pneumococcal vaccine |
| [2224694](https://pubmed.ncbi.nlm.nih.gov/2224694/) | 1990 | Review | CMAJ | Comprehensive review of AZT efficacy across HIV disease stages, including ARC |

## Germany Market Information

No marketing authorizations are on record for zidovudine in this evidence pack — market status is **未上市 (Not Marketed)**, with 0 registered licenses. No product/dosage-form/indication-text data is available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information. (Structured key warnings, contraindications, and drug-interaction data were not available in this evidence pack; note, however, that the literature evidence above documents zidovudine's well-known hematologic toxicity — see PMID 2224694 and related tolerability reports — which should be factored into any monitoring plan.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- ARC is supported by L1-level evidence — multiple completed Phase 3 RCTs, including the foundational 1987 NEJM trial — but this reflects zidovudine's original approved use rather than a genuinely novel repurposing opportunity, and the drug is not currently marketed in this jurisdiction.

**To proceed, the following is needed:**
- Confirm whether "new indication" framing is appropriate given ARC is a historical HIV disease stage already within zidovudine's original label
- TFDA/BfArM package insert data to complete the S1 safety review (currently a blocking data gap per this pack's `data_gaps`)
- Structured DrugBank MOA and DDI data (also flagged as a data gap)
- Regulatory/licensing pathway assessment given current "Not Marketed" status and 0 authorizations
- Hematologic monitoring plan (CBC with differential) given AZT's known myelosuppressive profile, since it would now only be used within combination ART, not as monotherapy

**Not pursued further at this time (Hold):** feline immunodeficiency syndrome, SIV infection (non-human models only), the unrelated rare neurodevelopmental disorder, "obsolete familial combined hyperlipidemia" (likely false positive, contradicts known NRTI lipid/mitochondrial toxicity), and congenital HIV (evidence classification incomplete).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

