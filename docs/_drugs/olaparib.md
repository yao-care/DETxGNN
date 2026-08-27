---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is a PARP (poly-ADP ribose polymerase) inhibitor originally developed for maintenance treatment of platinum-sensitive, BRCA-mutated relapsed ovarian, fallopian tube, or peritoneal cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, and this direction is already supported by **50 clinical trials** and **20 publications**, including multiple completed Phase 3 randomized controlled trials (OlympiAD, OlympiA).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRCA-mutated, platinum-sensitive relapsed ovarian cancer (maintenance therapy) — extracted from clinical trial context (NCT05078671); no formal TFDA/BfArM label text available |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Germany Market Status | 未上市 (Not currently marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Olaparib is a PARP1/2 inhibitor. In tumors with BRCA1/2 mutations (germline or somatic, resulting in homologous recombination repair — HRR — deficiency), it works through **synthetic lethality**: PARP inhibition blocks base-excision repair of single-strand DNA breaks, and in HRR-deficient cells the resulting unrepaired double-strand breaks cannot be fixed, selectively killing cancer cells while sparing normal HRR-competent cells.

Ovarian cancer and breast cancer share substantial molecular biology overlap — both are frequently driven by germline BRCA1/2 mutations as part of hereditary breast and ovarian cancer (HBOC) syndrome. Since the synthetic lethality mechanism depends on the tumor's BRCA/HRR status rather than tissue of origin, a drug validated in BRCA-mutated ovarian cancer is mechanistically well-positioned to work in BRCA-mutated breast cancer as well.

This is not merely a theoretical extrapolation: the TxGNN prediction is corroborated by an extensive body of completed Phase 3 evidence (OlympiAD, OlympiA) demonstrating that olaparib improves progression-free and overall survival in both metastatic and early-stage BRCA-mutated, HER2-negative breast cancer. This substantially strengthens confidence in the model's prediction beyond a purely computational signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05078671](https://clinicaltrials.gov/study/NCT05078671) | Phase 4 | Recruiting | 160 | Pharmacokinetic boosting study to improve olaparib exposure, tolerability, and cost-effectiveness in patients already using it for BRCA-mutated breast/ovarian cancer — reflects routine post-marketing clinical use. |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | Rollover study allowing patients who completed prior olaparib oncology trials (including breast cancer) to continue treatment, indicating durable long-term clinical benefit. |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1/2 | Completed | 25 | Carboplatin-olaparib sequencing vs. capecitabine as first-line therapy in BRCA1/2-mutated, HER2-negative advanced breast cancer. |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Phase 2 | Active, not recruiting | 200 | PETREMAC trial — personalized treatment of high-risk breast cancer, evaluating predictive/prognostic biomarkers for olaparib response. |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recruiting | 2900 | ComboMATCH — large genomically-guided basket trial with an olaparib treatment arm for solid tumors including breast cancer. |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after response to trabectedin-liposomal doxorubicin in recurrent BRCA-related carcinoma. |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab + ablative radiotherapy ± olaparib in metastatic triple-negative/HR-positive, HER2-negative breast cancer. |
| [NCT07321015](https://clinicaltrials.gov/study/NCT07321015) | Phase 2 | Not yet recruiting | 72 | Maintenance fluzoparib (another PARP inhibitor) in platinum-sensitive advanced TNBC with/without BRCA1/2 mutation — indirect class-effect support. |
| [NCT06545942](https://clinicaltrials.gov/study/NCT06545942) | Phase 1 | Active, not recruiting | 220 | MOMA-313 monotherapy or combined with a PARP inhibitor (incl. olaparib) in HRR-deficient advanced/metastatic solid tumors. |
| [NCT05700669](https://clinicaltrials.gov/study/NCT05700669) | Phase 1b/2 | Completed | 3 | AsiDNA™ combined with olaparib in recurrent ovarian, breast, and prostate cancer previously progressed on PARP inhibitor therapy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | Overall survival results from the OlympiA Phase 3 trial of adjuvant olaparib in germline BRCA1/2-mutated, high-risk early breast cancer. |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | New England Journal of Medicine | OlympiA trial: adjuvant olaparib reduces recurrence in BRCA1/2-mutated early breast cancer. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | New England Journal of Medicine | OlympiAD: olaparib shows antitumor activity in metastatic breast cancer with germline BRCA mutation. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD final overall survival and tolerability: olaparib vs. chemotherapy of physician's choice in gBRCA-mutated HER2-negative metastatic breast cancer. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | European Journal of Cancer | OlympiAD extended follow-up confirming survival and safety findings for olaparib in gBRCA-mutated metastatic breast cancer. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT (Phase II) | Journal of Clinical Oncology | TBCRC 048: olaparib activity in metastatic breast cancer with somatic BRCA1/2 or other HRR-gene mutations beyond germline BRCA. |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (Phase II) | Cancer Cell | I-SPY2 trial: durvalumab + olaparib + paclitaxel increases pathologic complete response in high-risk HER2-negative breast cancer. |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Review | International Journal of Molecular Sciences | Molecular mechanisms and emerging therapies (including PARP inhibitors) for chemotherapy-resistant triple-negative breast cancer. |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors, including olaparib, approved/investigated for BRCA-mutated breast cancer. |
| [37253112](https://pubmed.ncbi.nlm.nih.gov/37253112/) | 2023 | Translational/Basic Science | Cancer Research | Functional characterization of RAD51C variants relevant to HRR-deficiency and PARP inhibitor sensitivity in breast/ovarian cancer. |

---

## Germany Market Information

Olaparib currently has **no marketing authorization records on file** for this evidence pack (market status: 未上市 / not marketed; total authorizations: 0). No product name, dosage form, or approved indication text is available at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) — acts via synthetic lethality in HRR-deficient tumor cells rather than as a conventional broad-spectrum cytotoxic agent |
| Myelosuppression Risk | Medium — anemia is the most frequently reported hematologic toxicity across olaparib trials (e.g., OlympiAD, OlympiA); neutropenia and thrombocytopenia occur less commonly but warrant monitoring |
| Emetogenicity Classification | Low to Moderate — nausea is commonly reported with oral PARP inhibitors but is generally manageable and not classified as highly emetogenic |
| Monitoring Items | Complete blood count (hemoglobin, neutrophils, platelets) at baseline and periodically during treatment; renal function; long-term surveillance for myelodysplastic syndrome/acute myeloid leukemia (a recognized class-related risk with prolonged PARP inhibitor exposure) |
| Handling Protection | Given the genotoxic/mutagenic potential associated with PARP inhibitors, handling per institutional hazardous drug protocols is advisable even though olaparib is administered orally |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1, supported by multiple completed Phase 3 RCTs (OlympiAD, OlympiA) directly demonstrating olaparib's efficacy in BRCA-mutated breast cancer, and the mechanistic rationale (BRCA/HRR-driven synthetic lethality) is well established. However, formal Taiwan/Germany regulatory data (marketing authorization, package insert warnings, contraindications, and DDI profile) are currently unavailable, so guardrails are required before any deployment or clinical decision-making.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings, precautions, and contraindications (currently a Blocking data gap, DG001)
- Formal DrugBank-sourced mechanism of action documentation (currently a High-severity data gap, DG002)
- Drug-drug interaction (DDI) data specific to local formulary (current query status: not found)
- Confirmation of local (Taiwan/Germany) marketing authorization status before considering repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

