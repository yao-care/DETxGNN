---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazole: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal agent used systemically to treat and prevent invasive fungal infections. The TxGNN model predicts it may be effective against **pneumocystosis** (Pneumocystis jirovecii pneumonia), but this prediction is currently supported only by indirect literature — **no clinical trials** directly test itraconazole for this indication, and the underlying mechanistic rationale is considered weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan/Germany licence data (drug is unmarketed); itraconazole is generally known as a systemic triazole antifungal |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.34% (rank 7232) |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for itraconazole is not available in this evidence pack (`original_moa: [Data Gap]`). Based on known pharmacology, itraconazole inhibits fungal CYP51 and blocks ergosterol synthesis — the classic mode of action for triazole antifungals, effective against dimorphic and mould pathogens (e.g. Histoplasma, Aspergillus).

However, *Pneumocystis jirovecii* has atypical membrane sterol metabolism compared with conventional fungi, and clinically it responds poorly to azole antifungals. Standard first-line therapy for pneumocystosis (TMP-SMX, pentamidine) does not include any triazole agent. The literature evidence identified here largely reflects itraconazole's role as **broad-spectrum antifungal prophylaxis in immunocompromised populations** (HIV, transplant recipients) where pneumocystosis is one of several co-occurring opportunistic infections — not direct evidence of anti-Pneumocystis activity.

Given this, the mechanistic basis for the prediction should be treated as an **unvalidated hypothesis** rather than an established pharmacological link, and further preclinical or *in vitro* activity data against *P. jirovecii* would be needed before further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT (Phase 3) | HIV Medicine | Double-blind, placebo-controlled trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients — prophylactic context, not specific to pneumocystosis |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Single-centre experience of invasive fungal infections after kidney transplantation |
| [17594870](https://pubmed.ncbi.nlm.nih.gov/17594870/) | 2007 | Cohort | Allergologia et Immunopathologia | 25-year experience of chronic granulomatous disease in paediatric patients, including fungal complications |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian Journal of Medical Microbiology | Profile of respiratory fungal pathogens in immunocompetent vs immunocompromised hosts, correlated with CD4+ counts |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | Talaromyces marneffei and Pneumocystis jirovecii coinfection in a child with STAT1 mutation |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Overview of therapy/prophylaxis for systemic protozoan and Pneumocystis carinii infections |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis for opportunistic infections in HIV |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection (including fungal) after lung transplantation |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Pulmonary epithelial lining fluid penetration of antifungal and other anti-infective agents |

---

## Germany Market Information

Itraconazole is currently **not marketed** in Germany under the available regulatory data (0 authorizations recorded). No product/licence table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are marked as a **Blocking** data gap in this evidence pack and must be resolved before any safety evaluation can proceed — see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by indirect prophylaxis literature in immunocompromised populations, not by direct evidence of anti-*Pneumocystis* activity, and the proposed mechanism (ergosterol/CYP51 inhibition) is pharmacologically inconsistent with the atypical sterol biology of *P. jirovecii*. Combined with L5 evidence level (model prediction only) and a Blocking data gap on safety labelling, there is insufficient basis to advance.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical or *in vitro* evidence of itraconazole activity specifically against *Pneumocystis jirovecii*
- Any registered clinical trials evaluating itraconazole in pneumocystosis prevention/treatment, if they emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

