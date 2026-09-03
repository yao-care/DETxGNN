---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Actinic Keratosis/External Genital Warts to Pre-Malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical Toll-like receptor 7 (TLR7) agonist whose approved uses include actinic keratosis, external genital warts, and superficial basal cell carcinoma. The TxGNN model predicts it may also be effective for **Pre-Malignant Neoplasm** (broadly, epithelial intraepithelial lesions such as CIN/VIN/AIN and lentigo maligna), with **19 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Actinic keratosis / external genital warts (per mechanistic rationale text in the evidence pack; **not confirmed via structured license data — this field is a data gap**) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity gap). Based on the information present in the evidence pack, imiquimod is a TLR7 agonist that, when applied topically, induces local production of IFN-α, TNF-α, and other cytokines from keratinocytes and resident immune cells, activating both innate and adaptive immunity to clear virus-infected or abnormally proliferating epithelial cells.

This mechanism is already the pharmacological basis for imiquimod's existing approved uses in skin conditions such as actinic keratosis and external genital warts. Extending it to other epithelial intraneoplastic lesions — cervical, vulvar, and anal intraepithelial neoplasia (CIN/VIN/AIN), lentigo maligna, and superficial basal cell carcinoma — is mechanistically well supported, since all of these are HPV-related or UV-related premalignant/superficial epithelial lesions amenable to local immune-mediated clearance.

Notably, this biological plausibility is backed by real clinical data: two completed Phase 3 studies (lentigo maligna neoadjuvant treatment, n=259; actinic keratosis cream regimen) and a Phase 3 RCT directly testing imiquimod in high-grade CIN, giving this prediction stronger-than-average support relative to a pure model-score-only candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Neoadjuvant imiquimod to reduce excision size/risk of incomplete excision in lentigo maligna of the face |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade cervical intraepithelial neoplasia (CIN 2-3) vs. LLETZ; terminated early, review recruitment/safety reasons before use |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | RCT evaluating topical imiquimod efficacy in high-grade cervical intraepithelial lesions |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream (3x/week, 1-2 cycles) for actinic keratoses of the head |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Imiquimod 3.75% cream after cryotherapy for hypertrophic actinic keratoses on hands/forearms |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT: surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Immune escape mechanisms and imiquimod efficacy in HPV-associated VIN 2/3 and anogenital warts |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | RCT comparing 5% imiquimod, 0.05% imiquimod, and 0.05% nanoencapsulated imiquimod gel for actinic cheilitis |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Neoadjuvant topical TLR7 agonist (imiquimod) immunotherapy pilot in early-stage oral squamous cell carcinoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of interventions (including imiquimod) for anal canal intraepithelial neoplasia |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of medical interventions (including imiquimod) for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Photodynamic therapy combined treatments for non-melanoma skin cancer, including imiquimod-based regimens |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, including topical field therapies |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical treatment strategies for non-melanoma skin cancer and precursor lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK | Urol Oncol | PK/PD of TLR7 agonists (imiquimod-related compounds) in rat model, relevant to intravesical premalignant lesion delivery |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful treatment of high-grade VIN with imiquimod 5% in a renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Hautarzt | OCT imaging case with actinic porokeratosis and multiple (pre)malignant skin lesions |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis successfully treated with topical imiquimod 5% cream |

---

## Market Information

No marketing authorization records are available for this evidence pack — the product is recorded as **Not Marketed** with **0 authorizations**, so no license table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack (DG001, Blocking severity — TFDA/equivalent-agency package insert warnings and contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 studies and two Cochrane systematic reviews directly support imiquimod's mechanistic and clinical applicability to epithelial pre-malignant lesions (CIN, VIN, AIN, lentigo maligna, actinic keratosis), giving this an L1 evidence level. However, one pivotal Phase 3 RCT (NCT02329171) was terminated early and several supporting trials have small sample sizes, so guardrails are warranted rather than an unconditional Go.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official package insert warnings/contraindications before any S1 safety evaluation can proceed
- Resolve DG002: obtain confirmed mechanism of action data from DrugBank
- Clarify original approved indications via structured license data (currently absent from `taiwan_regulatory.licenses`)
- Review reason for early termination of NCT02329171 before relying on it as supportive evidence
- Define target lesion subtype (e.g., CIN vs. lentigo maligna vs. actinic keratosis) given heterogeneity across the trial evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

