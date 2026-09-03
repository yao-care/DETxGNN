---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Anti-PD-L1 Immunotherapy to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

> Avelumab is an anti-PD-L1 monoclonal antibody (immune checkpoint inhibitor); the specific original approved indication is not available in this evidence pack (no German marketing license on file).
> The TxGNN model's top-ranked prediction for this candidate is **Human Herpesvirus 8-Related Tumor** (score 99.97%),
> but currently there are **no clinical trials** and **no publications** in this evidence pack supporting this specific direction — the prediction is at model-inference level only (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no BfArM license record; drug class: anti-PD-L1 immunotherapy) |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on general drug-class knowledge, avelumab is an anti-PD-L1 monoclonal antibody belonging to the immune checkpoint inhibitor class, used in oncology to block the PD-1/PD-L1 pathway and restore T-cell–mediated antitumor immunity.

HHV8-related tumors (e.g., Kaposi sarcoma, primary effusion lymphoma) typically arise in immunosuppressed or AIDS populations. The theoretical rationale is that PD-L1 blockade could restore antiviral and antitumor immune surveillance in these patients, which is mechanistically plausible for a checkpoint inhibitor in general. However, per the rationale provided for this specific candidate, **this link is derived purely from the TxGNN prediction network and is not supported by any direct or indirect clinical evidence** — no trials, case reports, or reviews on avelumab in HHV8-related tumors exist in this dataset.

Given the complete absence of supporting evidence and the missing MOA/original-indication data, this specific prediction should be treated as an early-stage hypothesis only, not a validated mechanistic extension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Avelumab currently holds no marketing authorization in Germany (0 licenses on file); market status is **Not Marketed**.

---

## Cytotoxicity

Avelumab is an antineoplastic agent (anti-PD-L1 immune checkpoint inhibitor used in oncology).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (Anti-PD-L1 immune checkpoint inhibitor) |
| Myelosuppression Risk | Low — checkpoint inhibitors are not classically myelosuppressive; the dominant toxicity concern is immune-related adverse events rather than bone marrow suppression (specific toxicity data not available in this evidence pack) |
| Emetogenicity Classification | Low — immune checkpoint inhibitors are generally classified as minimal emetogenic risk |
| Monitoring Items | Thyroid, liver, and renal function; clinical monitoring for immune-related adverse events (colitis, pneumonitis, hepatitis, endocrinopathy) — general class-based guidance, as no drug-specific toxicity data is available |
| Handling Protection | As a monoclonal antibody (biologic), avelumab is not subject to conventional cytotoxic drug handling regulations; standard institutional infusion safety protocols should still apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not available in this evidence pack — data gap DG001, blocking severity.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (Human Herpesvirus 8-Related Tumor) has a very high TxGNN score but zero supporting clinical trials or literature, and both original indication and MOA data are missing, so it cannot pass even an initial safety/plausibility screen.

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — blocking gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- At least preclinical or case-level evidence specifically linking avelumab to HHV8-related tumors before advancing beyond L5
- **Note:** within this same candidate set, ranks 9–10 (*prostatic urethra urothelial carcinoma*, *kidney pelvis sarcomatoid transitional cell carcinoma*) show stronger mechanistic plausibility, since avelumab is already an approved class for urothelial carcinoma maintenance therapy, and rank 10 has one completed observational trial (NCT05431777). These may be more tractable candidates for near-term follow-up than the current top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

