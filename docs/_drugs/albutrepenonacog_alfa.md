---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the report data directly from the Evidence Pack (no code changes needed — this is a document-generation task). Below is the report following the specified template and section order.

---

# Albutrepenonacog Alfa: From Hemophilia B (Factor IX Replacement) to Pseudo-von Willebrand Disease

## One-Sentence Summary

> Albutrepenonacog alfa (rIX-FP, DrugBank DB13884) is a recombinant coagulation Factor IX Fc-fusion replacement product used in the management of Hemophilia B.
> The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, with a very high prediction score (**99.94%**),
> but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia B (Factor IX replacement therapy) — inferred from drug class; German license data is not available (0 authorizations on record) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known information, albutrepenonacog alfa is a recombinant coagulation Factor IX Fc-fusion protein (rIX-FP) — an extended half-life factor replacement product whose efficacy in Hemophilia B (Factor IX deficiency) is well established. Mechanistically, it would be expected to apply to bleeding disorders that share Factor IX's role in the coagulation cascade.

The original indication (Factor IX deficiency) and the predicted new indication (pseudo-von Willebrand disease) both fall under the broad category of "inherited bleeding disorders," which likely explains why the TxGNN knowledge graph assigns a high similarity score — the model may be picking up on shared phenotypic features (bleeding tendency, disease co-occurrence patterns) rather than a genuine shared pharmacological pathway.

Importantly, the evidence pack's own mechanistic analysis raises significant doubt about this specific prediction. Pseudo-von Willebrand disease is caused by a gain-of-function defect in the platelet GPIb receptor (increased affinity for von Willebrand factor) — a **primary hemostasis / platelet adhesion** disorder. This is mechanistically distinct from Factor IX replacement, which acts on the **secondary hemostasis / thrombin generation cascade**. No direct causal pharmacological link has been established, and the same caveat applies to the other five top-ranked predictions in this pack (primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome, collagen receptor-defect bleeding disorder, and constitutional thrombocytopenia) — all are platelet-function or platelet-count disorders mechanistically distinct from Factor IX replacement, and none have any supporting clinical or literature evidence. This pattern is consistent with **phenotypic confusion** (the model clustering diverse "bleeding disorders" together) rather than true mechanistic overlap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No German marketing authorization was found for albutrepenonacog alfa. The product is currently classified as **Not Marketed** in Germany, with 0 registered authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all currently unavailable — TFDA package insert data is flagged as a Blocking data gap (DG001) that prevents the S1 safety pre-screening stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN prediction score is very high (99.94%), but is backed by zero clinical trials and zero literature — evidence level is L5, the lowest tier.
- The mechanistic rationale itself flags this prediction (and all 5 runner-up predictions) as likely driven by phenotypic similarity among "bleeding disorders" rather than a real shared pharmacological pathway between Factor IX replacement and platelet-function/platelet-count disorders.
- Two data gaps currently block a rigorous evaluation: TFDA package insert / warnings data (DG001, Blocking) and mechanism of action data (DG002, High).

**To proceed, the following is needed:**
- TFDA/EMA package insert and safety data (resolve DG001 — required before any S1 safety pre-screening)
- Confirmed mechanism of action for albutrepenonacog alfa (resolve DG002)
- Preclinical or mechanistic studies establishing a plausible causal link between Factor IX replacement and platelet-function disorders (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, etc.)
- Any real-world or case-report evidence of off-label use in platelet disorders
- Clarification of German/EU regulatory status, since the product currently shows 0 marketing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

