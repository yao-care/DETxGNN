---
layout: default
title: Eptinezumab
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 1
---

# Eptinezumab
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

# Eptinezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Eptinezumab is a CGRP-targeted monoclonal antibody established for migraine prevention. The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a migraine subtype, but this direction is currently supported only by **0 dedicated clinical trials** and **8 publications** (mostly post-hoc analyses, reviews, and case reports).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (see note below); literature context indicates general migraine prevention |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> Note: `taiwan_regulatory.licenses` is empty (drug not marketed in Germany), so no formal approved-indication text is available from regulatory records. The migraine-prevention context above is inferred solely from the supporting literature in this evidence pack, not from a regulatory source.

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action data (DrugBank `original_moa`) is not available for eptinezumab. Based on the mechanistic rationale provided with this prediction, eptinezumab is an anti-CGRP (calcitonin gene-related peptide) monoclonal antibody. CGRP plays a central role in activating the trigeminovascular system and in cortical spreading depression, the mechanism believed to underlie migraine aura — providing a plausible biological basis for extending eptinezumab's use to migraine subtypes involving aura.

However, the supporting literature also introduces an important caveat: PMID 40229719 (a 2025 RCT) found that PACAP38-induced migraine attacks can occur independently of CGRP signaling, suggesting that brainstem-related aura mechanisms may not be fully explained by the CGRP pathway alone. As a result, the mechanistic link between eptinezumab's known CGRP-blocking action and this specific aura subtype is best characterized as moderate and non-specific rather than a direct, proven mechanistic fit.

Overall, while the CGRP hypothesis provides a reasonable starting rationale — and post-hoc subgroup data (PMID 35302389) suggest some benefit in patients with self-reported aura — the evidence base is still preliminary and subtype-specific efficacy has not been confirmed in dedicated trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Post-hoc Analysis (Phase 3 RCT subgroup) | Cephalalgia | Post hoc analysis of PROMISE-1/2 evaluating eptinezumab efficacy and safety specifically in patients with migraine and self-reported aura |
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | RCT | The Journal of Headache and Pain | PACAP38-induced migraine attacks occur independently of CGRP signaling, suggesting a CGRP-independent pathway may contribute to aura-related attacks |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handbook of Experimental Pharmacology | Overview of CGRP's central role in migraine pathophysiology, including trigeminal system involvement and aura subgroup |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Case Report | Revista de Neurología | Successful management of "wearing-off" effect with eptinezumab in a chronic migraine patient refractory to two other CGRP antibodies |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Review | Headache | Genetic migraine disorders (including chronic migraine with visual aura features) responsive to CGRP antagonist therapy |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports + Literature Review | Journal of Clinical Medicine | Reviews evidence on whether anti-CGRP monoclonal antibodies (including eptinezumab) are effective specifically against migraine aura |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Review | Cureus | General review of CGRP antagonists in episodic and chronic migraine management |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review (different drug: rimegepant) | Pain Management | Broad overview of new acute/preventive migraine treatments; eptinezumab mentioned only as one of several preventive options |

## Germany Market Information

Eptinezumab is not currently marketed in Germany (`market_status`: 未上市). No BfArM marketing authorization records are available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. Note that key regulatory safety documentation (TFDA/BfArM label warnings and contraindications) is flagged as a **Blocking data gap (DG001)** in this evidence pack, meaning a preliminary safety assessment (S1) cannot currently be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no dedicated clinical trials for the "migraine with brainstem aura" subtype, and the supporting literature is limited to post-hoc analyses, reviews, and case reports (Evidence Level L3). A recent RCT (PMID 40229719) also raises the possibility that CGRP-independent mechanisms contribute to this aura subtype, weakening the mechanistic case. Combined with a Blocking data gap on safety labeling, a formal go decision cannot be supported at this stage.

**To proceed, the following is needed:**
- TFDA/BfArM package insert warnings and contraindications (DG001, blocking — required before any S1 safety assessment)
- Formal DrugBank mechanism-of-action data (DG002)
- Dedicated clinical trial(s) evaluating eptinezumab specifically in migraine with brainstem aura
- Further mechanistic clarification of the CGRP vs. PACAP38-independent pathway's role in aura-related attacks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

