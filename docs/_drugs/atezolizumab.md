---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is an anti-PD-L1 immune checkpoint inhibitor originally established in the treatment of urothelial carcinoma (bladder cancer) and other PD-L1-expressing solid tumors.
The TxGNN model predicts it may also be effective for **Prostatic Urethra Urothelial Carcinoma**, a rare anatomic subtype of urothelial carcinoma,
with **2 clinical trials** currently supporting this direction (no dedicated publications identified yet).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial Carcinoma (Bladder Cancer) — general drug knowledge; no local regulatory record found in this pack |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, atezolizumab is a monoclonal antibody that blocks PD-L1, restoring T-cell-mediated antitumor immunity. It is a class-defining anti-PD-L1 agent whose efficacy in urothelial carcinoma — including BCG-unresponsive non-muscle invasive bladder cancer — has been clinically validated.

Prostatic urethra urothelial carcinoma is an anatomic subtype of urothelial carcinoma arising from urothelium lining the prostatic urethra, sharing the same histogenesis and immune microenvironment characteristics (PD-L1 expression, tumor-infiltrating lymphocyte patterns) as bladder-origin urothelial carcinoma. Because the mechanism of immune checkpoint blockade is tissue-of-origin driven rather than anatomically restricted, extension of atezolizumab's activity to this rarer urothelial subtype is biologically plausible.

The strongest supporting evidence comes from a completed Phase 2 trial (NCT02844816) demonstrating atezolizumab monotherapy activity in BCG-unresponsive NMIBC — a closely related urothelial carcinoma population — lending indirect but mechanistically consistent support to the prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Single-arm trial of atezolizumab monotherapy in BCG-unresponsive recurrent non-muscle invasive bladder cancer; graded "A" relevance as direct urothelial carcinoma evidence, though non-randomized. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 (1b) | Active, not recruiting | 914 | Dose-escalation study of cabozantinib ± atezolizumab across multiple solid tumors including advanced urothelial carcinoma (bladder, renal pelvis, ureter, urethra); atezolizumab is a combination arm, not the primary study drug — graded "B" relevance. |

---

## Literature Evidence

No related literature currently available for this indication.

---

## Germany Market Information

No authorization records are available — atezolizumab is currently **not marketed** in this jurisdiction (0 licenses on file). Regulatory documentation (e.g., label warnings/contraindications) should be sourced directly from the manufacturer or the relevant health authority before any downstream use.

---

## Cytotoxicity

Atezolizumab is an antineoplastic agent (anti-PD-L1 immunotherapy), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (immune checkpoint inhibitor, anti-PD-L1 monoclonal antibody) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — unlike conventional cytotoxic chemotherapy, checkpoint inhibitors are not primarily myelosuppressive; risk instead centers on immune-related adverse events (irAEs) |
| Emetogenicity Classification | Low (minimal emetogenic potential relative to cytotoxic chemotherapy) |
| Monitoring Items | Liver function tests, thyroid function, renal function, and clinical monitoring for immune-related adverse events (colitis, pneumonitis, hepatitis, endocrinopathies) |
| Handling Protection | Standard IV biologic handling precautions; special cytotoxic drug handling protocols (as required for conventional chemotherapy) are generally not applicable |

Please refer to the package insert warnings and precautions for detailed toxicity data, as no drug-specific toxicity dataset was provided in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial in a closely related urothelial carcinoma population (BCG-unresponsive NMIBC) provides mechanistically consistent, indirect support, but no trial has directly enrolled patients with prostatic urethra urothelial carcinoma specifically — evidence is directionally supportive but not indication-specific.

**To proceed, the following is needed:**
- TFDA/local regulatory label data on warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action documentation from DrugBank (currently a gap — DG002)
- Dedicated trial or case-series evidence in prostatic urethra urothelial carcinoma specifically, rather than inferred from broader urothelial carcinoma data
- A defined safety monitoring plan for immune-related adverse events in this population prior to any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

