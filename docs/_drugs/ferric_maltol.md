---
layout: default
title: Ferric Maltol
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 3
---

# Ferric Maltol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ferric Maltol: From Iron Deficiency to Plummer-Vinson Syndrome

## One-Sentence Summary

> Ferric maltol is a novel oral trivalent iron complex, believed to be used for the treatment of iron deficiency (original indication data not provided in this evidence pack).
> The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**,
> with **0 clinical trials** and **0 publications** currently supporting this direction — the case rests entirely on mechanistic reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` is empty) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa`: Data Gap), and no original indication is recorded either. Based on publicly known drug information, ferric maltol is a next-generation oral iron replacement therapy (a ferric iron–maltol complex) used to correct iron deficiency in adults, including patients who do not tolerate conventional ferrous salts.

Plummer-Vinson (Paterson-Kelly) syndrome's core pathology is long-standing iron deficiency anemia accompanied by esophageal webs and dysphagia. Iron repletion is the established causal treatment for this syndrome, so the mechanistic link is strong. However, this represents an extension of an already-known pharmacological action into a rare clinical presentation, rather than a genuinely novel drug-disease pairing.

For context, two lower-ranked predictions in the same evidence pack illustrate the range of plausibility: **IRIDA syndrome** (TMPRSS6-driven hepcidin dysregulation causing resistance to conventional oral iron) has a biologically coherent rationale — ferric maltol's distinct absorption pathway may partially bypass hepcidin-mediated inhibition — but no confirmatory evidence exists yet. **Vitamin B12/folate-independent megaloblastic anemia**, by contrast, involves a DNA-synthesis defect unrelated to iron status; the mechanistic link is weak and likely reflects a non-specific "anemia" association in the knowledge graph rather than a real signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

No German market authorization records available — the drug is not marketed in Germany (`total_licenses`: 0).

---

## Other Predicted Indications (Lower Priority)

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 2 | Vitamin B12/folate-independent constitutional megaloblastic anemia | 99.98% | L5 | S0 | Hold (mechanistically weak) |
| 3 | IRIDA syndrome | 99.33% | L4 | S1 | Research Question |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A Blocking-severity data gap (DG001 — TFDA label warnings/contraindications) currently prevents this candidate from entering formal S1 safety evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Plummer-Vinson syndrome prediction has strong mechanistic logic (iron repletion for iron-deficiency-driven pathology) but zero supporting clinical trials or literature, and the drug is not marketed in Germany. Combined with a Blocking data gap on TFDA safety labeling, the case cannot advance past a research question at this time.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/BfArM label warnings and contraindications for ferric maltol
- Resolve DG002: retrieve confirmed MOA and original approved indication from DrugBank
- Targeted literature search for case reports/series of ferric maltol use in Plummer-Vinson syndrome and IRIDA
- If evidence remains absent, monitor via periodic re-screening rather than active investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

