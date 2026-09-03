---
layout: default
title: Fenbendazole
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Fenbendazole
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

# Fenbendazole: From Anthelmintic Use to Urinary Bladder Carcinoma

## One-Sentence Summary

Fenbendazole is a benzimidazole-class anthelmintic (deworming agent), not currently approved for human use in Germany.
The TxGNN model predicts it may be effective for **Urinary Bladder Carcinoma** (and 9 other bladder cancer subtypes, all with similarly high scores),
but this top-ranked prediction currently has **no supporting clinical trials or literature** — evidence exists only for a closely related indication (urinary bladder neoplasm), and only at the preclinical level.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack; fenbendazole is a veterinary/human antiparasitic (anthelmintic) benzimidazole, no oncology indication on record |
| Predicted New Indication | Urinary Bladder Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism of action data (original_moa) is not available for fenbendazole. Based on the TxGNN model's repurposing rationale, fenbendazole belongs to the benzimidazole anthelmintic class, and its proposed antitumour mechanism is binding to the colchicine-like site on β-tubulin, inhibiting microtubule polymerization. This disrupts mitotic spindle formation, causing G2/M-phase cell cycle arrest, and may additionally downregulate GLUT glucose transporters and inhibit hexokinase, interfering with tumour cell metabolism — a mechanism conceptually similar to taxanes/vinca alkaloids, though at a distinct binding site.

There is no established relationship between fenbendazole's original antiparasitic use and bladder cancer; the connection is purely mechanistic (microtubule disruption affecting rapidly dividing urothelial carcinoma cells), inferred by the TxGNN network rather than derived from clinical precedent.

Notably, the top-ranked prediction (urinary bladder carcinoma, this report's focus) has **no direct literature or trial evidence** — its rationale explicitly states this is "purely a TxGNN network prediction score" extrapolated from the closely related indication "urinary bladder neoplasm" (rank 2, score 99.99%), which does have two preclinical literature citations: one on fenbendazole combined with CRISPR-Cas13a in an intravesical instillation model for bladder cancer, and one on an unrelated carcinogenesis mechanistic pathway (UBD activation) not specific to fenbendazole treatment. Eight further bladder cancer subtypes (ranks 3–10) carry the same unsupported mechanistic rationale with no direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Germany Market Information

Fenbendazole is currently **not marketed** in Germany (0 authorizations on record). No product licenses or approved human indications are available in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A blocking data gap (DG001) has been identified — TFDA/label warnings and contraindications have not yet been retrieved, which prevents any preliminary safety (S1) assessment.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (urinary bladder carcinoma) is supported only by a TxGNN network score (L5, model prediction only) with zero direct clinical trials or literature. Even the best-evidenced related indication (urinary bladder neoplasm) reaches only L4 (preclinical/mechanistic), and the drug is not marketed for human use in Germany. Combined with a blocking data gap on safety warnings, there is currently insufficient evidence to proceed.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve/confirm human-use warnings and contraindications, since fenbendazole is currently only established as a veterinary/antiparasitic agent
- Resolve DG002 (High): obtain confirmed mechanism of action data from DrugBank to validate the microtubule-inhibition hypothesis
- In vitro/in vivo confirmation of antitumour activity specifically in bladder carcinoma models (beyond the single combination-therapy preclinical study found for the related "urinary bladder neoplasm" indication)
- Human pharmacokinetic/safety data, given no existing approved human formulation or dosing precedent
- Re-evaluation once any Phase 1/2 trial or additional peer-reviewed literature becomes available for this specific indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

