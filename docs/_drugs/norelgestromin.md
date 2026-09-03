---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 1
---

# Norelgestromin
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is the active metabolite of norgestimate, a third-generation progestin used as the progestogen component of a combined transdermal contraceptive patch. The TxGNN model predicts a potential new indication of **Amenorrhea**, but this direction is currently supported by **zero clinical trials** and **zero publications** — and the supplied rationale itself flags the prediction as a likely reverse-causality artifact, since amenorrhea is a documented *adverse effect* of this drug, not a condition it is known to treat.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack (no approved product license found); drug is clinically used as a component of a combined transdermal contraceptive patch |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Norelgestromin is the active metabolite of norgestimate and acts as a third-generation progestin. Clinically, it is used as a component of a combined transdermal contraceptive patch, where it suppresses gonadotropin secretion, inhibits ovulation, and alters the endometrium to prevent pregnancy. A formally structured DrugBank mechanism-of-action record was not available in this evidence pack; the description above is derived from the drug's known pharmacological class and the rationale accompanying the prediction.

The predicted new indication — amenorrhea — is mechanistically connected to norelgestromin only through its **already-established adverse effect profile**. Amenorrhea (absent or missed withdrawal bleeding) is a commonly reported reason patients discontinue combined hormonal contraceptives, including the norelgestromin/ethinyl estradiol patch. There is no known mechanism by which norelgestromin would be used *therapeutically* to treat amenorrhea; a progestin that suppresses the hypothalamic-pituitary-ovarian axis and thins the endometrium is pharmacologically far more consistent with **causing** amenorrhea than with correcting it.

For this reason, the evidence pack itself flags this prediction as a probable **reverse-causality artifact**: TxGNN, like other knowledge-graph models, can mislearn a drug–adverse-event edge ("norelgestromin causes amenorrhea") as a drug–indication edge ("norelgestromin treats amenorrhea") — a known pitfall for progestins, where amenorrhea is heavily coded in pharmacovigilance data. The high TxGNN score (99.51%) should therefore not be read as an endorsement of therapeutic plausibility; it more likely reflects the strength of the drug–amenorrhea association driven by adverse-event reporting rather than any treatment signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Norelgestromin currently has no marketing authorization on file (market status: **Not Marketed**, 0 authorizations). No product name, dosage form, or approved-indication data is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence level is L5 (model prediction only, no clinical trials or literature), and the decision stage is S0 — the earliest possible stage, with no safety pre-screening completed.
- The mechanistic rationale itself indicates this prediction is more likely a reverse-causality artifact (amenorrhea is a known adverse effect of norelgestromin, not a plausible treatment target) rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings and contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety pre-screening can begin
- Confirmed mechanism of action from the DrugBank API — currently a **High**-severity data gap (DG002)
- An independent pharmacovigilance/literature review to explicitly test and either confirm or refute the reverse-causality hypothesis before any further evaluation
- If the reverse-causality hypothesis is not resolved, this candidate should be deprioritized rather than advanced past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

