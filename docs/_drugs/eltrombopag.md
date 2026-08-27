---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 1
---

# Eltrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Eltrombopag: From Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is a thrombopoietin (TPO) receptor agonist historically used to raise platelet counts in thrombocytopenic disorders (e.g., immune thrombocytopenia, aplastic anemia, hepatitis C-associated thrombocytopenia). The TxGNN model predicts it may also be relevant to **HIV infectious disease**, with **5 clinical trials** and **10 publications** currently available as supporting context — though none of the trials directly target HIV as the primary indication, and the evidence is largely indirect (comorbidity-based).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in formal registry data; pharmacologically known as a treatment for thrombocytopenic disorders (ITP, aplastic anemia, HCV-related thrombocytopenia) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known pharmacology, eltrombopag is a small-molecule TPO receptor (MPL) agonist that stimulates megakaryocyte production to raise platelet counts. Its established uses are all in thrombocytopenic disorders — it is not classified as an antiretroviral or antiviral agent.

The connection to HIV infectious disease appears to arise from two distinct pathways, and it is important not to conflate them. First, a **comorbidity pathway**: HIV infection and its treatment are frequently associated with immune thrombocytopenia (ITP) and immune reconstitution inflammatory syndrome (IRIS)-related thrombocytopenia. Multiple case reports and a case series in the literature describe eltrombopag being used successfully off-label to manage HIV-associated ITP and aplastic anemia, including one report noting a possible immunomodulatory effect (reduced Th1/Th17 proinflammatory T-helper populations). Second, an **independent mechanistic hypothesis**: a single in-vitro drug-repurposing screen (PMID 32977702) identified eltrombopag as a modulator of HIV-1 proviral transcription, possibly related to its zinc-finger-binding chemistry — but this finding has not been validated in cell-infection models or clinical studies.

Taken together, the TxGNN high score most likely reflects the knowledge graph's strong "HIV – thrombocytopenia – eltrombopag" co-occurrence pattern rather than a direct, validated antiviral mechanism. Readers should clearly distinguish between "treating HIV-associated thrombocytopenia" (reasonably well supported) and "treating HIV infection itself" (speculative, preclinical only).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Rollover safety/tolerability study of eltrombopag for maintaining platelet counts in HCV-related thrombocytopenia; not HIV-specific |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | RCT evaluating eltrombopag's ability to enable HCV antiviral therapy initiation via sustained virologic response; not HIV-specific |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | RCT assessing eltrombopag to reduce platelet transfusion needs in chronic liver disease patients undergoing invasive procedures; trial terminated, not HIV-specific |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | RCT assessing eltrombopag for maintaining platelet counts to enable HCV antiviral therapy (SVR endpoint); not HIV-specific |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | Open-label study of eltrombopag (research code SB-497115-GR) raising platelet counts in HCV-related compensated cirrhosis; not HIV-specific |

**Note:** None of the above trials enrolled HIV patients or used HIV-related endpoints. All five support eltrombopag's established efficacy in thrombocytopenia associated with hepatitis C/chronic liver disease; TxGNN links this evidence to HIV via the shared "thrombocytopenia" comorbidity node rather than a direct HIV trial.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematology/Oncology Clinics of North America | Chronic HCV, HIV, and H. pylori infections are recognized causes of secondary immune thrombocytopenia; treating the underlying infection often improves platelet counts |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Discusses therapeutic strategies for infection-related immune thrombocytopenia, including HCV and HIV as recognized secondary causes |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Review | Internal Medicine Journal | Reviews thrombopoietin receptor agonist use in immune thrombocytopenia of less than 6 months' duration |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | Preclinical/In-vitro Screening | Viruses | Drug-repurposing screen of FDA-approved compounds identifies eltrombopag as a modulator of HIV-1 proviral transcription; in-vitro only, no infection-model or clinical validation |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort | Platelets | Danish cohort of TPO-receptor agonist use in refractory ITP, including secondary ITP cases (e.g., chronic lymphocytic leukemia); real-world off-label use patterns |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case Series | Journal of the International Association of Providers of AIDS Care | Case series on TPO receptor agonists (eltrombopag, romiplostim) as salvage therapy for refractory HIV-associated immune thrombocytopenic purpura |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case Report | AIDS | Successful use of eltrombopag without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case Report | AIDS | First reported successful treatment of HIV-associated severe aplastic anemia with eltrombopag, with evidence of an immunomodulatory effect (reduced Th1/Th17 cells) |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case Report | Journal of the College of Physicians and Surgeons Pakistan | Case of hepatitis B (not HIV) leading to megaloblastic anemia and severe thrombocytopenia; included as a related infection-thrombocytopenia case |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case Report | Farmacia Hospitalaria | Two case reports of eltrombopag used for thrombocytopenia in chronic hepatitis C patients |

---

## Germany Market Information

No marketing authorizations are currently on file for eltrombopag in this market (0 licenses recorded; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Key warnings, contraindications, and drug-drug interaction data could not be retrieved for eltrombopag in this evaluation (see Data Gap DG001, classified as *Blocking* — this currently prevents progression to the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV infectious disease prediction is currently supported only by indirect, comorbidity-based evidence (case reports/case series of eltrombopag treating HIV-associated thrombocytopenia) and a single unvalidated in-vitro screening finding on HIV-1 proviral transcription — no trial has evaluated eltrombopag against HIV infection itself. Combined with a blocking data gap in safety/label information and the absence of any market authorization, the evidence base is not yet sufficient to advance past the research-question stage.

**To proceed, the following is needed:**
- TFDA/package insert warnings and contraindications (Data Gap DG001 — currently blocking S1 safety pre-assessment)
- Confirmed mechanism of action data from DrugBank or equivalent source (Data Gap DG002)
- Cell-infection-model (not just in-vitro screen) validation of the HIV-1 proviral transcription modulation reported in PMID 32977702
- A clearly scoped clinical study (or at minimum a retrospective cohort) evaluating antiviral/virologic outcomes in HIV patients, distinct from existing thrombocytopenia-support evidence
- Regulatory pathway and market authorization assessment before any local development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

