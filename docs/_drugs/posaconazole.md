---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# POSACONAZOLE: From Antifungal Prophylaxis to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal agent whose established use is prophylaxis of invasive fungal disease (per literature evidence in this pack; no formal indication text was provided in the source data). The TxGNN model predicts it may be effective for **Pneumocystosis**, but this is currently supported only by indirect background evidence — **2 clinical trials** (neither testing posaconazole directly against pneumocystosis) and **5 publications** (mostly reviews/guidelines, no dedicated RCT).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug-level `original_indications` is empty); literature evidence references posaconazole as "mould-active" agent used for antifungal prophylaxis in high-risk haemato-oncological patients |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data (`original_moa`) is marked as a Data Gap in this evidence pack. However, the repurposing rationale field provided does describe posaconazole's mechanism: it inhibits fungal CYP51 (14α-demethylase), blocking ergosterol synthesis — the classic mode of action for broad-spectrum triazole antifungals.

The proposed link to pneumocystosis is mechanistically weak. *Pneumocystis jirovecii* is taxonomically a fungus, but its cell membrane is cholesterol-based rather than ergosterol-based, meaning the azole–ergosterol pathway that underlies posaconazole's antifungal activity does not straightforwardly apply. The available literature only mentions posaconazole in the broader context of invasive fungal disease management (including *Pneumocystis* pneumonia as one of several fungal diseases discussed in review articles), and as a possible alternative in patients who cannot tolerate TMP-SMX — this is an indirect inference, not a mechanistically or clinically validated claim.

Given the atypical target biology and the absence of any trial or study directly testing posaconazole against pneumocystosis, this prediction should be treated as a research hypothesis rather than a clinically actionable signal at this stage.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Tests **rezafungin** (an echinocandin, not posaconazole) vs. standard antimicrobial regimen for prevention of invasive fungal disease in allogeneic BMT patients; not focused on pneumocystosis and not a posaconazole trial — background relevance only (Grade C). |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens in mismatched unrelated donor transplant recipients; may include antifungal prophylaxis arms (possibly posaconazole) but primary endpoints are GVHD-related, not pneumocystosis efficacy/safety (Grade C). |

Neither trial provides direct efficacy or safety evidence for posaconazole in pneumocystosis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet. Infectious Diseases | UK best-practice update on diagnosis of serious fungal diseases; general diagnostic landscape, not posaconazole-specific therapy data. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of candidiasis, aspergillosis, cryptococcosis and *Pneumocystis* pneumonia; notes mould-active posaconazole prophylaxis reduced invasive candidiasis in high-risk haemato-oncology patients — the closest evidence link in this pack, but still a general review, not pneumocystosis-specific trial data. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review/Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 Chinese clinical practice guideline for invasive pulmonary fungal disease diagnosis/management; general guideline context. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | PK/PD Study | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal/antitubercular agents; pharmacokinetic background only, no efficacy data for pneumocystosis. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective cohort of infectious complications in acute GVHD after liver transplant; describes antimicrobial management patterns, not a posaconazole–pneumocystosis efficacy study. |

No RCT or dedicated clinical study directly evaluates posaconazole for pneumocystosis treatment or prophylaxis.

## Germany Market Information

Posaconazole currently has **no market authorization on record** in this evidence pack (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0; `licenses`: none provided). No authorization table can be generated.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug–drug interaction data are all marked as Data Gaps in this evidence pack (DDI query status: not found), and cannot currently be summarized.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between posaconazole and pneumocystosis is biologically weak (atypical, non-ergosterol target membrane) and unsupported by any direct clinical trial or study; all identified trials and literature are indirect background evidence (Evidence Level L4, decision stage S1 — "Research Question"). Additionally, safety data (TFDA/local warnings and contraindications) is a **Blocking** data gap (DG001), which by itself prevents progression to a formal safety evaluation (S1).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label warnings/contraindications before any S1 safety assessment can begin
- Resolve DG002 (High): confirm formal mechanism-of-action data via DrugBank API to properly assess mechanistic plausibility
- Identify or commission a study directly testing posaconazole in pneumocystosis (efficacy and safety), given no such trial currently exists
- Clarify pharmacological rationale given *Pneumocystis jirovecii*'s atypical (cholesterol-based) membrane biology relative to posaconazole's ergosterol-targeting mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

