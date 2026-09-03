---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: From HIV-1 Infection to Feline Immunodeficiency Virus Infection (Feline AIDS)

## One-Sentence Summary

Elvitegravir is an HIV-1 integrase strand-transfer inhibitor (INSTI), and the Evidence Pack's own repurposing rationale describes its original clinical use as treatment of HIV-1 infection in humans; it is currently **not marketed in Germany** (0 authorizations). The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome (FIV)** — a veterinary, not human, indication — with a very high raw prediction score (**99.89%**) but **zero supporting clinical trials and zero publications**, meaning this is a pure model-prediction signal (L5) with no translational evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack — `original_indications` is empty and `original_moa` is flagged as a data gap (DG002). Rationale text within the pack indicates elvitegravir acts as an HIV-1 integrase strand-transfer inhibitor, implying its original human indication is HIV-1 infection, but this is not independently confirmed by a sourced field. |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (FIV) |
| TxGNN Prediction Score | 99.89% (rank 1781) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available as a sourced field (DG002, High severity). Based on the information present in this Evidence Pack's repurposing rationale, elvitegravir is an HIV-1 integrase strand-transfer inhibitor (INSTI) — its efficacy in HIV-1 infection is well established, and mechanistically this class of inhibitor targets the viral integrase enzyme responsible for inserting proviral DNA into the host genome.

The top-ranked prediction, FIV (feline immunodeficiency virus infection), is biologically plausible on a mechanistic basis: FIV is a lentivirus closely related to HIV-1, and its integrase shares structural and catalytic homology with HIV-1 integrase. In theory, elvitegravir's strand-transfer inhibition could cross-react with FIV integrase. However, this is a **pure mechanistic inference with no in vitro or in vivo data**, and — critically — FIV is a veterinary disease. It sits entirely outside the human drug-repurposing evaluation pathway (no human PK/PD, no human safety pathway, no regulatory route), so it does not constitute an actionable candidate for human indication expansion regardless of its model score.

The other two ranked predictions in this pack reinforce a "Hold" posture rather than supporting escalation. Rank 2 (simian immunodeficiency virus infection) is a well-known *non-human primate model* used to study HIV antiretrovirals — not an independent human or even standalone veterinary indication — and no elvitegravir-specific SIV data exists in this pack. Rank 3 (a rare genetic neurodevelopmental disorder) has no identifiable mechanistic link to integrase inhibition and is explicitly flagged in the pack's own rationale as a likely false positive arising from knowledge-graph embedding proximity rather than real biology. Taken together, none of the three top TxGNN predictions for elvitegravir currently point to an actionable human repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Elvitegravir is not marketed in Germany — `taiwan_regulatory.market_status` reports "未上市" (Not marketed) with 0 total licenses and no license records available in the Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI lookup all returned no data in this Evidence Pack. This is flagged in the pack as DG001 — a **Blocking** severity data gap — meaning TFDA/label-level warnings and contraindications must be obtained before this candidate can proceed to any S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (FIV) is a veterinary condition with no human translational pathway, despite a high raw TxGNN score; the remaining two predictions are either an animal research model (SIV) or a likely false-positive genetic-disorder association — none constitute an actionable human repurposing signal.
- Evidence level is L5 across all three predictions (no clinical trials, no literature), and a **Blocking** data gap (DG001: TFDA warnings/contraindications) prevents this candidate from entering safety pre-assessment (S1) at all.

**To proceed, the following is needed:**
- TFDA/label-sourced warnings and contraindications (resolve DG001) before any safety pre-assessment can begin
- Confirmed original indication and MOA data for elvitegravir (resolve DG002), ideally sourced directly from DrugBank/regulatory labeling rather than inferred from rationale text
- Re-screening of TxGNN outputs for elvitegravir to identify any human-relevant candidate indications, since the current top-3 predictions are not clinically actionable
- If FIV or SIV signals are retained for any exploratory purpose, they should be routed to a veterinary/translational research track rather than the human drug-repurposing evaluation pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

