---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutant AML to Bulbar Polio

## One-Sentence Summary

Ivosidenib (DB14568) is a mutant IDH1 (isocitrate dehydrogenase 1) inhibitor whose established global indication is IDH1-mutant acute myeloid leukemia (AML); this specific indication data point is not yet populated in the local regulatory dataset. The TxGNN model's top-ranked prediction is **Bulbar Polio**, but the evidence pack itself flags this as a likely false positive with no biological rationale. **Zero clinical trials and zero publications** currently support this direction — the model's embedding similarity does not translate into a plausible mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in local licenses; known global indication is IDH1-mutant Acute Myeloid Leukemia (per drug class/label information, not locally verified) |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Germany Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on the repurposing rationale accompanying the prediction, Ivosidenib is a selective inhibitor of mutant IDH1, blocking production of the oncometabolite 2-hydroxyglutarate (2-HG) — a metabolic/epigenetic pathway relevant to hematologic malignancy, not to neurological or infectious disease.

**This top-ranked prediction is not mechanistically reasonable.** Bulbar polio is a neurodegenerative condition caused by poliovirus infection of motor neurons. It shares no known pathway, target, or biological process with mutant-IDH1-driven oncogenesis. The evidence pack itself explicitly characterizes this as an embedding-similarity artifact ("false positive") with no supporting hypothesis — this is a case where a high TxGNN score does not indicate biological plausibility.

Two lower-ranked but more credible candidates exist in this evidence pack: **AML/MDS related to prior radiation therapy** and **AML/MDS related to prior alkylating-agent therapy** (both L4, "Research Question" stage). Both are therapy-related secondary leukemias that can, in a genotype-stratified subset, carry IDH1 R132 mutations analogous to Ivosidenib's approved primary-AML indication. However, TP53 mutation and complex karyotype — not IDH1 mutation — dominate these secondary leukemia subtypes, and no dedicated trials or case reports currently exist for this population. These remain hypothesis-generating extrapolations from the approved AML label rather than independently supported new indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

No marketing authorizations are currently registered for this drug in the local dataset (market status: 未上市 / Not Marketed; total authorizations: 0).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 enzyme inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (No warnings, contraindications, or drug-interaction data are currently available; TFDA label data is flagged as a Blocking data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Bulbar Polio) has no supporting mechanism, trials, or literature, and is explicitly identified within the evidence pack as a probable false positive. The two mechanistically plausible secondary candidates (therapy-related AML/MDS) remain at the Research Question stage (L4) with no direct clinical evidence, so no candidate in this pack currently justifies advancing beyond Hold.

**To proceed, the following is needed:**
- TFDA/manufacturer label data (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed MOA data from DrugBank (DG002) to support formal mechanistic-link scoring
- If pursuing the AML/MDS-related candidates: genotype-stratified case series or registry data confirming IDH1 R132 mutation prevalence in radiation- and alkylating-agent-related secondary AML/MDS
- Targeted literature search restricted to therapy-related AML/MDS with IDH1 mutation status, rather than relying on primary-AML label extrapolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

