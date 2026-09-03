---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis (Low-Confidence Signal)

## One-Sentence Summary

Gefitinib is an oral EGFR tyrosine kinase inhibitor established for EGFR-mutant non-small cell lung cancer (NSCLC), as confirmed by the literature embedded in this evidence pack. The TxGNN model's top-ranked new indication, **Gingival Fibromatosis**, has **no supporting clinical trials or literature** and no known mechanistic link to EGFR biology — the pack's own rationale flags this as a likely embedding-space artifact rather than a genuine drug-specific signal. Across all 10 predicted indications in this candidate set, only two (lung hilum carcinoma, pulmonary sulcus neoplasm — both anatomical subtypes of NSCLC) carry any literature relevance, and even those represent label-adjacent extensions rather than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in regulatory license data (drug not marketed in Germany); consistently described in the pack's own literature as therapy for EGFR-mutant non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.89% (rank 1785 in model's internal ranking) |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank MOA data is flagged as a blocking data gap (DG002) in this evidence pack. Based on literature embedded in the pack itself (e.g., PMID 24794908, 12841190), gefitinib is a selective, ATP-competitive small-molecule inhibitor of the epidermal growth factor receptor (EGFR) tyrosine kinase, used clinically to treat EGFR-mutant NSCLC by blocking downstream proliferation and survival signaling in tumor cells.

For the top-ranked prediction, **gingival fibromatosis**, there is no mechanistic bridge to this pathway. Gingival fibromatosis is a gingival connective-tissue overgrowth disorder linked to pathways such as TGF-β/fibroblast proliferation, not EGFR-driven epithelial malignancy. The repurposing rationale attached to this candidate explicitly states the high TxGNN score likely reflects clustering in the model's disease-embedding space rather than a drug-specific pharmacological signal.

Within the broader candidate set, the only two predictions with a coherent mechanistic story are **lung hilum carcinoma** (rank 5, L3) and **pulmonary sulcus neoplasm / Pancoast tumor** (rank 9, L4) — both are anatomical subtypes of NSCLC, gefitinib's already-approved indication. These are not novel repurposing hypotheses so much as label-adjacent anatomical extensions, and the attached evidence (a single case report, an ECOG NSCLC-stage review, an unrelated leptomeningeal metastasis case) does not specifically address these subtypes. The remaining 7 candidates (fibroma of lung, hamartoma of lung, IBMPFD, lung benign neoplasm, a rare genetic syndrome, lung germ cell tumor, junctional epidermolysis bullosa) show either mechanistic implausibility, literature-label mismatch, or in the case of junctional epidermolysis bullosa, a mechanism running in the *opposite* direction (EGFR inhibition is a known cause of skin barrier toxicity, not a treatment for a skin barrier defect).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Gefitinib currently has **no marketing authorizations on file** in Germany (market status: not marketed, total licenses: 0). No product table can be generated from this evidence pack.

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (EGFR-targeted therapy for NSCLC, per literature embedded in this pack), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low. Literature in this pack highlights interstitial lung disease (PMID 20942679, 20949670), QT prolongation (PMID 34474028, 37258113), and cutaneous toxicity (PMID 18931563) as characteristic adverse effects, rather than bone-marrow suppression typical of cytotoxic chemotherapy |
| Emetogenicity Classification | Low (oral small-molecule targeted agent) |
| Monitoring Items | Liver function tests, pulmonary symptoms/imaging (ILD risk), ECG/QTc, skin toxicity assessment; baseline CBC reasonable given oncologic use |
| Handling Protection | Gefitinib is an oral antineoplastic and typically appears on institutional hazardous-drug lists; standard oral hazardous-drug handling precautions apply, though it does not require IV cytotoxic reconstitution/compounding controls |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/German warnings and contraindications data is a blocking data gap — DG001 — and drug-drug interaction search returned no results in this pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 10 predicted indications in this candidate set is supported by adequate mechanistic or clinical evidence: 8 of 10 are L5 (model score only, no trials/literature) or mechanistically implausible/mismatched, and the two with any literature support (lung hilum carcinoma, pulmonary sulcus neoplasm) are anatomical subtypes of gefitinib's existing NSCLC indication rather than genuine new repurposing opportunities. Combined with a blocking safety data gap (DG001) and the drug's unmarketed status in Germany, this candidate does not meet the bar to advance past S0/S1.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/EU SmPC warnings and contraindications for gefitinib (Iressa)
- Resolve DG002: confirm formal MOA via DrugBank API rather than literature inference
- If pursuing lung hilum carcinoma or pulmonary sulcus neoplasm, clarify with regulatory/clinical review whether these are already covered under the existing NSCLC label — a "new indication" claim may not be warranted
- Re-screen or manually curate the TxGNN top-10 output before pharmacist review, given the high proportion of mechanistically implausible or label-mismatched candidates (rare genetic syndromes, benign tumors, and a barrier-defect skin disease paired with an EGFR inhibitor)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

