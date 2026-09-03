---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# MOROCTOCOG ALFA: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

> Moroctocog alfa is a B-domain–deleted recombinant human Factor VIII (rFVIII) replacement product, used for the treatment and prevention of bleeding in Hemophilia A (congenital Factor VIII deficiency).
> The TxGNN model's top-ranked prediction suggests possible effectiveness for **Primary Release Disorder of Platelets**,
> but this is currently supported only by **7 clinical trials** — none of which actually enrolled patients with this disease — and **no relevant literature**, indicating weak and likely spurious evidential support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (congenital Factor VIII deficiency) — inferred from drug class; no German market license data available to confirm |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, moroctocog alfa is a B-domain-deleted recombinant human Factor VIII replacement product; its efficacy in Hemophilia A has been well established, and mechanistically it works by restoring FVIII coagulation activity in patients who lack sufficient endogenous factor.

Primary Release Disorder of Platelets, however, is a **platelet granule secretion defect** — bleeding results from the platelets' inability to release their storage granule contents upon activation, not from a deficiency of a plasma coagulation factor. FVIII supplementation does not address this underlying secretory defect, so the mechanistic rationale for this prediction is weak.

This is corroborated by the supporting evidence itself: all 7 cited clinical trials were graded "C" for relevance, and none actually studied patients with a platelet release disorder. They instead cover Hemophilia A trials of unrelated FVIII products (BIVV001, BAX855), artificial liver support in acute-on-chronic liver failure, portal vein hemostasis during TIPS procedures, post-COVID-vaccination coagulation studies, and coagulation profiles in AML. This pattern suggests the TxGNN association likely reflects broad semantic proximity between "bleeding disorder" concepts in the knowledge graph rather than a genuine, drug-specific pharmacological link — consistent with the reviewer note flagging a possible database mismatch.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (PEGylated rFVIIIFc-VWF-XTEN) prophylaxis in severe Hemophilia A ≥12 yrs — not a platelet release disorder population |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) in severe Hemophilia A undergoing surgery — unrelated population |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system (DPMAS+TPE) in acute-on-chronic liver failure — no direct link |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis during TIPS placement — no direct link |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Post-COVID-19-vaccination syndrome symptom/lab evaluation — no direct link |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profiles in newly diagnosed AML on induction chemotherapy — no direct link |

*(All 7 trials retrieved were graded "C" relevance; none enrolled patients with a primary platelet release disorder.)*

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No German market authorizations found. `taiwan_regulatory` data indicates the drug is **not marketed** (0 licenses on file), so no product/dosage-form/indication details can be provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: German label warnings/contraindications (DG001) and MOA detail (DG002) are flagged as data gaps in this evidence pack — DG001 is a **Blocking** gap that prevents a full S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Primary Release Disorder of Platelets) lacks any mechanistically relevant clinical or literature evidence — all cited trials involve unrelated patient populations and different investigational products. The evidence pattern is more consistent with a knowledge-graph semantic artifact than a true pharmacological signal.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001 (German label warnings/contraindications) before any S1 safety review can proceed
- Resolve High-severity data gap DG002 (confirmed MOA) to support mechanistic-relevance analysis
- If this indication is pursued further, dedicated preclinical/translational evidence demonstrating a role for FVIII beyond coagulation in platelet granule release would be required
- **Separately worth noting:** among the 8 TxGNN-predicted indications reviewed for moroctocog alfa in this batch, *acquired coagulation factor deficiency* (rank 4) is mechanistically far more plausible (FVIII replacement is directly relevant to acquired Hemophilia A) and reached evidence level L3 / decision stage S2 with a "Research Question" recommendation. However, most of its supporting trials used porcine FVIII (Obizur/susoctocog alfa) rather than moroctocog alfa itself, so direct evidence transfer remains uncertain — this candidate merits a separate, dedicated evaluation rather than being pursued under the current top-ranked indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

