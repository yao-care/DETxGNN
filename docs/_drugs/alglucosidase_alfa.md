---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

Using the drug-repurposing evaluation report template (per the v5 prompt) to generate this report. One important note before the output: for this candidate, **all 10 TxGNN-predicted indications carry the same profile** — L5 evidence, zero clinical trials, zero literature, and the evidence pack's own `repurposing_rationale` text explicitly argues that the mechanistic link is *not* biologically valid (it flags the connection as likely knowledge-graph noise from disease-name/phenotype similarity, not a real GAA-pathway mechanism). I'm reporting that faithfully rather than smoothing it into a positive narrative.

---

# Alglucosidase Alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is an enzyme replacement therapy that supplies acid α-glucosidase (GAA), originally developed for Pompe disease (glycogen storage disease type II). The TxGNN model predicts a possible effect on **Adult Polyglucosan Body Disease (APBD)**, but this is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis concludes the causative enzyme in APBD (GBE1) is unrelated to GAA — suggesting the prediction may be a knowledge-graph artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pompe disease (glycogen storage disease type II, GAA deficiency) — inferred from the rationale text in this evidence pack, as no formal `original_indications` or regulatory license text was returned |
| Predicted New Indication | Adult Polyglucosan Body Disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap (DG002) in this pack, so no formal MOA record is available. However, the evidence pack's repurposing rationale independently confirms the drug's known biology: alglucosidase alfa is a recombinant acid α-glucosidase (GAA) enzyme replacement, used to correct lysosomal glycogen accumulation in Pompe disease.

The predicted indication, adult polyglucosan body disease, is also a glycogen-metabolism disorder — but it is caused by a **deficiency of glycogen branching enzyme (GBE1)**, not GAA. According to the rationale text supplied, this is a fundamentally different enzymatic pathway: alglucosidase alfa replaces GAA, which does nothing to correct a GBE1 defect. The same disconnect applies to predictions #2 and #3 (GSD IV / GBE1-related disorders).

For predictions #4–#10 (congenital entropion, ectropion, Horner syndrome, ptosis-vocal cord paralysis syndrome, congenital cranial dysinnervation disorder, epiblepharon, ptosis-strabismus-ectopic pupils syndrome), the rationale text is explicit that these are eyelid/ocular or cranial-nerve developmental disorders with **no known biological connection** to lysosomal glycogen storage or GAA activity. The rationale itself characterizes these as likely artifacts of phenotype-name similarity in the knowledge graph (e.g., shared descriptors like ptosis/muscle weakness overlapping superficially with Pompe disease's myopathic presentation), rather than a real mechanistic signal.

**Conclusion of this section**: based on the evidence pack's own mechanistic assessment, none of the top 10 TxGNN predictions for this drug currently have a defensible pharmacological rationale. The high TxGNN scores (99.1–99.5%) reflect model confidence in the embedding space, not confirmed biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

(Confirmed via `query_log`: ClinicalTrials.gov and ICTRP searches for alglucosidase alfa against all 10 predicted indications, including adult polyglucosan body disease, returned 0 results on 2026-04-20.)

---

## Literature Evidence

Currently no related literature available.

(Confirmed via `query_log`: PubMed searches for alglucosidase alfa against all 10 predicted indications returned 0 results on 2026-04-20.)

---

## Germany Market Information

Alglucosidase alfa is currently **not marketed** in Germany under this evidence pack (`market_status: 未上市`), with **0 registered authorizations**. No license records are available to cite for approved indication text.

---

## Safety Considerations

The TFDA/package-insert warnings and contraindications data have **not yet been obtained** — this is flagged in the evidence pack as a **Blocking** data gap (DG001), meaning this candidate cannot yet proceed to the S1 safety pre-assessment stage. No DDI data was found (query status: not_found).

> Please refer to the package insert for safety information once the TFDA source document has been retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the 10 TxGNN-predicted indications for this drug carries an L5 evidence level (model prediction only), zero clinical trials, and zero literature. More importantly, the evidence pack's own mechanistic analysis concludes that the leading candidate (and #2, #3) involve a different causative enzyme (GBE1) than the one alglucosidase alfa targets (GAA), and the remaining candidates (#4–#10) are ophthalmologic/neuromuscular developmental disorders with no plausible link to glycogen metabolism. Combined with a Blocking safety data gap (TFDA warnings/contraindications not yet retrieved) and zero market authorizations in Germany, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert with warnings/contraindications, to close the Blocking gap (DG001) and enable S1 safety pre-assessment
- Formal DrugBank-sourced MOA documentation (DG002)
- An independent pharmacological review comparing the GBE1 vs. GAA pathways before investing further in evidence-gathering for APBD/GSD IV-related predictions
- Regulatory/licensing documentation, since Germany shows 0 authorizations and no approved-indication text is available for reference
- If any of these predictions are still to be pursued, preclinical/in-vitro evidence of GAA activity in the relevant disease models, given the complete absence of clinical or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

