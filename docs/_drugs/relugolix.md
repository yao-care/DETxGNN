---
layout: default
title: Relugolix
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 0
---

# Relugolix
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

# RELUGOLIX: Repurposing Evaluation — Pending TxGNN Predictions

## Summary

Relugolix (DrugBank: DB11853) is an orally active GnRH receptor antagonist approved in multiple markets (USA, EU, Japan) for advanced prostate cancer, and in combination for uterine fibroids and endometriosis. The current Evidence Pack is critically incomplete: TxGNN repurposing predictions have not yet been generated, and both safety labeling and MOA data are absent. **A Hold decision is required until the two upstream data gaps are resolved.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Predicted New Indication | Pending — TxGNN predictions not yet generated |
| Recommended Decision | Hold |

---

## About This Drug

Relugolix is a non-peptide, orally active GnRH (gonadotropin-releasing hormone) receptor antagonist. By competitively blocking pituitary GnRH receptors, it rapidly suppresses LH and FSH secretion, driving testosterone (men) or estradiol (women) to castrate levels. This distinguishes it from GnRH agonists, which cause an initial hormone flare before suppression.

Key approved indications outside Germany:

- **Advanced prostate cancer** — Orgovyx® (FDA, EMA, PMDA approved)
- **Uterine fibroids / endometriosis** — Myfembree® (in combination with estradiol + norethindrone acetate)

Because relugolix is approved for hormone-sensitive cancer and works via hormonal axis suppression, it qualifies for the cytotoxicity section as a targeted hormonal agent.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — GnRH receptor antagonist (hormonal agent) |
| Myelosuppression Risk | Low (non-cytotoxic mechanism; no direct bone marrow effect) |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum testosterone / estradiol, cardiovascular risk (QTc, lipids, blood pressure), bone mineral density (long-term ADT) |
| Handling Protection | Standard handling — not a conventional cytotoxic; no special cytotoxic waste handling required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN repurposing candidates and is missing both MOA details and safety labeling, making it impossible to assess any new indication at this stage. No evaluation can proceed until upstream data collection is complete.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve and parse the EMA/TFDA package insert for warnings and contraindications (Data Gap DG001)
- **[High]** Complete MOA data integration from DrugBank API (Data Gap DG002)
- **[Required]** Execute TxGNN inference pipeline to generate repurposing candidate predictions for RELUGOLIX (DB11853)
- **[Required]** Collect clinical trial and literature evidence for the top-ranked predicted indication
- **[Required]** Re-submit a complete Evidence Pack (v5+) once all data gaps are resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

