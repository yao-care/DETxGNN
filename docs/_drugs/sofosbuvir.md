---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide analogue inhibitor of the hepatitis C virus (HCV) NS5B RNA-dependent RNA polymerase, and its established efficacy is in chronic HCV infection. The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**, with **50 clinical trials** and **19 publications** tagged to this label — but on closer review, the great majority of this evidence concerns HCV treatment in patients who happen to also carry HBV (coinfection/reactivation contexts), not direct anti-HBV efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatitis C virus (HCV) infection *(derived from mechanism-of-action statements embedded in the evidence pack; no formal `original_indications`/label data was supplied)* |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data (`original_moa`) is not available in the structured drug record. However, the evidence pack's own repurposing rationale consistently identifies sofosbuvir as a nucleotide analogue that inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) — the enzyme HCV, a *Flaviviridae* family member, uses to replicate its genome. This is a well-established, clinically proven mechanism against HCV.

HBV, by contrast, is a *hepadnavirus* that replicates via a reverse-transcriptase (RT) domain in its own polymerase — a structurally and mechanistically distinct enzyme from HCV's NS5B RdRp. There is no known direct inhibitory activity of sofosbuvir against the HBV polymerase. The evidence pack's own mechanistic assessment states this explicitly: the two enzymes have "completely different" active sites and substrate specificity, and no direct HBV-polymerase inhibition mechanism is known.

Consistent with this, when the underlying clinical trial and literature evidence is examined, most of it does **not** test sofosbuvir's efficacy against HBV. Instead, it falls into two categories: (1) trials of sofosbuvir-based HCV regimens conducted in patient populations that happen to be HCV/HBV co-infected, where the treatment target remains HCV; and (2) case reports and cohort studies describing **HBV reactivation** as an adverse consequence of HCV clearance with direct-acting antivirals (DAA), which is a safety signal rather than evidence of anti-HBV efficacy. The one directly relevant study — a small, single-arm Phase 2 trial of ledipasvir/sofosbuvir in HBV-monoinfected subjects (NCT03312023, n=21) — was designed around a modest, previously observed reduction in HBsAg during HCV/HBV coinfection treatment, and represents a hypothesis-generating pilot rather than confirmed efficacy. Overall, the TxGNN score appears to be driven substantially by label co-occurrence (HCV/HBV coinfection and reactivation literature) rather than a validated antiviral mechanism against HBV itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label pilot of ledipasvir/sofosbuvir for 12 weeks in **HBV-monoinfected** subjects; primary/secondary endpoints were decline in HBsAg and HBV DNA, based on prior observation of modest HBsAg reduction in HCV/HBV coinfected patients. Most directly relevant trial in the dataset. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | Ledipasvir/sofosbuvir FDC for 12 weeks in Taiwanese adults with chronic genotype 1/2 HCV **and HBV coinfection**; assessed HCV antiviral efficacy/safety, HBV outcomes secondary. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of HBV reactivation incidence/risk factors during DAA treatment of HCV/HBV coinfected patients — a safety/reactivation study, not an HBV efficacy trial. |
| [NCT02349048](https://clinicaltrials.gov/study/NCT02349048) | Phase 2 | Completed | 68 | Simeprevir + daclatasvir + sofosbuvir for chronic HCV genotype 1 (6–8 weeks); **graded low relevance (C)** — HCV treatment only, no HBV endpoint. |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | Generic velpatasvir/sofosbuvir ± ribavirin for HCV in HIV-coinfected patients; **graded low relevance (C)** — no HBV linkage. |
| [NCT02717949](https://clinicaltrials.gov/study/NCT02717949) | Phase 4 | Terminated | 1 | Oral HCV therapy in patients with indolent lymphoma; **graded low relevance (C)**, terminated with minimal enrollment. |

*Note: the underlying evidence pack lists ~50 trials under this indication label; the remaining ~44 are predominantly conventional HCV direct-acting antiviral studies (efficacy, safety, drug interactions, special populations) with no direct bearing on HBV efficacy — they appear in this label mainly through HCV/HBV coinfection cohorts or population overlap, not because sofosbuvir was tested against HBV.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label trial | J Med Virol | Ledipasvir/sofosbuvir 12 weeks in HBV-monoinfected subjects; hypothesis was that HBsAg decline seen in HCV/HBV coinfection would recur — the only prospective interventional evidence for direct anti-HBV activity. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort (HCV/HBV coinfection) | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir-based therapy in Egyptian HCV and HCV/HBV coinfected patients; efficacy endpoint centered on HCV clearance. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir + ribavirin — a safety signal, not efficacy evidence. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort/registry | J Clin Gastroenterol | Risk of HBV reactivation among patients treated with ledipasvir-sofosbuvir for HCV. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infect Drug Resist | Management of HBV reactivation post-DAA treatment of HCV in HCV/HBV coinfected patients. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | HBV reactivation via a surface-antigen immune-escape mutant during sofosbuvir/velpatasvir treatment for HCV. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepat | HBV reactivation in cancer patients receiving DAAs for HCV/HBV coinfection. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | ADR report | Hospital Pharmacy | Notes a case of hepatitis B reactivation during HCV treatment with simeprevir and sofosbuvir. |

*Note: the majority of this literature documents HBV reactivation risk during HCV treatment with sofosbuvir-based regimens — a safety concern relevant to HCV/HBV coinfected patients — rather than evidence that sofosbuvir treats HBV infection.*

---

## Germany Market Information

Sofosbuvir is currently **not marketed** in Germany under this evidence record (`market_status`: 未上市 / Not Marketed), with **0 registered authorizations**. No license or product detail is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No structured warnings, contraindications, or DDI data were available in this evidence pack. Note, however, that the literature review above surfaced a recurring signal of **HBV reactivation risk** in HCV/HBV coinfected patients treated with sofosbuvir-based regimens — this should be a specific focus of any future formal safety review for this indication.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between sofosbuvir and HBV infection is not supported by a validated mechanism — HBV's reverse-transcriptase-based replication is structurally unrelated to the HCV NS5B RdRp that sofosbuvir inhibits. The high TxGNN score appears driven by label co-occurrence in HCV/HBV coinfection and reactivation literature rather than genuine anti-HBV activity, and the only direct interventional evidence is a single small Phase 2 pilot (n=21) with no confirmatory follow-up.

**To proceed, the following is needed:**
- Resolution of the blocking data gap on TFDA/BfArM label warnings and contraindications (DG001) before any safety assessment can proceed
- Confirmed mechanism-of-action data (DG002) to validate or refute a plausible anti-HBV pathway
- Outcome data (not just study design) from NCT03312023 to determine whether the observed HBsAg/HBV DNA signal was clinically meaningful
- An adequately powered, HBV-monoinfection-specific controlled trial with virologic endpoints, rather than reliance on coinfection/reactivation cohorts
- A dedicated review of the HBV reactivation risk signal identified in the literature before considering this indication further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

