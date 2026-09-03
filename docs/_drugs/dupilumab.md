---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: Th2-Driven Inflammatory Disease to Bronchitis

## One-Sentence Summary

> Dupilumab is a biologic that blocks IL-4Rα signalling to suppress Th2-driven (eosinophilic) inflammation; its established original indication data is not available in this evidence pack (drug not yet marketed in Taiwan).
> The TxGNN model predicts it may be effective for **Bronchitis**,
> with **1 clinical trial** and **6 publications** currently identified, though most of this evidence addresses asthma rather than bronchitis directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license record exists for this drug (`taiwan_regulatory.licenses` is empty) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is flagged as a Data Gap and Taiwan-specific original indication data is unavailable because no license record exists for this drug. However, the evidence pack's own repurposing rationale describes dupilumab as an **IL-4Rα antagonist** that blocks IL-4/IL-13 signalling, thereby suppressing Th2-type eosinophilic inflammation — a mechanism with strong, well-documented support in eosinophilic asthma (see literature evidence below).

The link to "bronchitis" is mechanistically plausible but indirect: bronchitis is a broad diagnostic category, and the strongest supportive evidence in this pack (e.g., the TRAVERSE long-term asthma extension study, and the asthma meta-analysis) actually concerns **moderate-to-severe asthma**, not bronchitis per se. The single directly relevant clinical trial (NCT04362501) targets chronic rhinosinusitis without nasal polyps (CRSsNP), not bronchitis, and was itself graded "C" relevance by the internal reasoning engine — providing only indirect Th2-pathway support.

Given that eosinophilic/Th2-driven airway inflammation underlies both asthma and certain bronchitis phenotypes (e.g., eosinophilic or asthma-COPD overlap bronchitis), the mechanistic extension to bronchitis is biologically reasonable as a research hypothesis, but direct clinical evidence specific to bronchitis remains sparse at this time.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP); provides indirect Th2-pathway evidence but does not directly study bronchitis (relevance graded "C"). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT (open-label extension) | Lancet Respir Med | Long-term safety/efficacy of dupilumab in moderate-to-severe asthma beyond 1 year (TRAVERSE study). |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review/Meta-analysis | J Asthma | Pooled RCT data show dupilumab improves efficacy and safety outcomes in uncontrolled asthma. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Cohort/Imaging study | Chest | MRI-based ventilation defects in severe eosinophilic asthma respond to anti-T2 (dupilumab-class) therapy. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberc Respir Dis | Comprehensive review of pharmacologic therapies, including biologics, for preventing COPD exacerbations. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses treatment challenges in smoking-induced airway disease including chronic bronchitis and asthma-COPD overlap. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review/Case-based | Pediatric Pulmonology | Novel therapies for eosinophilic pediatric plastic bronchitis. |

---

## Taiwan Market Information

This drug is currently **not marketed in Taiwan**, and no license records are available in this evidence pack (`total_licenses = 0`). No approved indication text can be extracted at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data are all flagged as Data Gaps (DG001 — TFDA package insert not yet retrieved) or "not_found" in this evidence pack, and cannot be summarized here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence directly supporting dupilumab for bronchitis is currently limited to a single Phase 2 trial with low relevance (Grade C, studied a different disease — CRSsNP) plus mechanistic extrapolation from asthma literature. This corresponds to Evidence Level L3 and the "Research Question" stage — not yet sufficient to support progression toward regulatory or clinical development for this specific indication.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation via DrugBank (DG002)
- Dedicated clinical trials or real-world evidence in a defined bronchitis population (e.g., eosinophilic or asthma-COPD overlap bronchitis) rather than adjacent respiratory/sinus indications
- Taiwan regulatory/licensing status confirmation, since the drug is currently not marketed here

---

**Note:** Among the 10 candidate indications in this evidence pack, **dermatitis (atopic dermatitis)** — ranked #2 by TxGNN — shows substantially stronger evidence (Evidence Level L1, multiple completed Phase 3 RCTs, recommendation "Proceed with Guardrails") and is a globally recognized approved indication for dupilumab. If the goal is to prioritize the strongest repurposing/registration opportunity for this drug candidate, a separate evaluation report on the dermatitis indication is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

