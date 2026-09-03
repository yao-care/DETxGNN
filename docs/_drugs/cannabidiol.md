---
layout: default
title: Cannabidiol
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Cannabidiol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Cannabidiol: Preliminary Assessment — No TxGNN Prediction Data Available

## One-Sentence Summary

Cannabidiol (CBD) is a phytocannabinoid derived from *Cannabis sativa*, with established regulatory approval in major markets (FDA: Epidiolex; EMA: Epidyolex) for treatment-resistant epilepsy syndromes.
This Evidence Pack contains **no TxGNN predicted indications**, and critical data — including mechanism of action, Germany market authorization records, and safety profile — are flagged as blocking gaps.
**A full drug repurposing evaluation cannot be completed until these data gaps are resolved.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Treatment-resistant epilepsy (Dravet syndrome, Lennox-Gastaut syndrome) — based on expert knowledge; not confirmed in Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions generated |
| Germany Market Status | Not found (Evidence Pack: 未上市 / 0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Data Gap Summary

This Evidence Pack has **2 blocking/high-severity data gaps** that prevent a complete evaluation:

| Gap ID | Item | Severity | Impact | Remediation |
|--------|------|----------|--------|-------------|
| DG001 | Package insert warnings / contraindications | **Blocking** | Cannot pass S1 safety gate | Download EMA Epidyolex SmPC PDF and parse |
| DG002 | Mechanism of action (MOA) | High | Cannot perform mechanistic relevance analysis | Query DrugBank API for DB09061 |

---

## Why No Prediction Is Available

The TxGNN model returned **no predicted indications** for Cannabidiol (DB09061) in this run. Possible reasons include:

1. The compound is not present in the knowledge graph used during this prediction run
2. All candidate scores fell below the reporting threshold
3. A pipeline error occurred upstream of the evidence collection step

Without at least one TxGNN predicted indication, the core drug repurposing analysis cannot proceed. This must be investigated before any further evaluation steps are taken.

---

## Germany Market Information

No authorization records were found for Cannabidiol in the regulatory database within this Evidence Pack.

> **Discrepancy note:** Epidyolex (cannabidiol oral solution 100 mg/mL) received EMA approval on 19 September 2019 for adjunctive treatment of seizures associated with Lennox-Gastaut syndrome or Dravet syndrome in patients aged ≥2 years. The absence of records strongly suggests the regulatory query was run under the INN "CANNABIDIOL" but failed to match the approved brand name. The query should be re-run using alternative identifiers: **Epidyolex**, **Epidiolex**, or marketing authorisation number **EU/1/19/1375**.

---

## Safety Considerations

All safety data fields in this Evidence Pack are unavailable. Please refer to the official EMA Summary of Product Characteristics (SmPC) for Epidyolex for complete safety information.

> Blocking item outstanding before evaluation can proceed:
> **DG001** — Retrieve and parse the Epidyolex SmPC to extract contraindications, warnings, and key drug interactions (particularly with CYP3A4/CYP2C19 substrates and valproate).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing TxGNN predictions entirely, and two blocking/high-severity data gaps (MOA, safety profile) prevent any meaningful drug repurposing assessment from being conducted at this stage.

**To proceed, the following is needed:**

- **[Critical]** Re-run TxGNN prediction pipeline for DB09061 and confirm that output is non-empty; if still empty, verify compound is included in the knowledge graph
- **[DG001]** Retrieve the Epidyolex EMA SmPC (EU/1/19/1375) and extract warnings, contraindications, and drug interaction profile
- **[DG002]** Query DrugBank API for full MOA data for DB09061 (cannabidiol)
- **[Regulatory]** Re-run the Germany regulatory query using brand names **Epidyolex** / **Epidiolex** to retrieve actual market authorization records and approved indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

