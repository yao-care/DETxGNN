---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor originally developed for influenza A/B treatment, working by blocking the viral surface enzyme required for virion release.
> The TxGNN model predicts it may be effective for **Pyelonephritis**, but currently **0 clinical trials** and **0 publications** support this specific link, and the evidence pack's own mechanistic review flags the prediction as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (neuraminidase inhibitor; no formal license record available — drug not marketed in Germany) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available for this candidate (flagged as a High-severity data gap). However, the evidence pack's repurposing rationale confirms zanamivir acts exclusively as a neuraminidase inhibitor against influenza virus surface glycoprotein — it has no antibacterial activity of any kind.

Pyelonephritis is a bacterial upper urinary tract infection, most commonly caused by gram-negative organisms such as *E. coli*. There is no known pharmacological overlap between viral neuraminidase inhibition and bacterial pyelonephritis pathogenesis. The evidence pack itself states that the high TxGNN score likely reflects a **knowledge-graph semantic proximity artifact** (both indications are broadly linked to "infection") rather than a genuine mechanistic relationship.

A second, lower-ranked prediction ("disorder of tyrosine metabolism," score 99.02%) shows the same pattern: the only supporting literature discusses the H274Y/H275Y neuraminidase resistance mutation, which involves a histidine→tyrosine amino acid substitution — an incidental naming overlap, not a link to inherited tyrosine metabolism disorders (e.g., tyrosinemia). Neither prediction currently has a credible mechanistic or clinical basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Zanamivir is currently **not marketed** in Germany, and no authorization records (BfArM license numbers, product names, or approved indication texts) are available in the database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (pyelonephritis) has zero supporting clinical trials or literature, and the evidence pack's own mechanistic review assesses the drug–disease link as biologically implausible and likely a knowledge-graph artifact rather than a genuine pharmacological signal. Evidence level is L5, the lowest tier (model prediction only).

**To proceed, the following is needed:**
- Resolve the blocking data gap (DG001): TFDA/BfArM label warnings and contraindications, required before any S1 safety pre-assessment
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Independent pharmacological or preclinical rationale connecting neuraminidase inhibition to bacterial pyelonephritis, if this candidate is to be pursued further
- Re-evaluation of TxGNN scoring methodology to address potential semantic-proximity false positives for infection-related indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

