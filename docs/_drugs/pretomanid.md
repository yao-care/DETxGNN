---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 5
---

# Pretomanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pretomanid: From Multidrug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

> Pretomanid is an antimycobacterial prodrug used as part of the BPaL regimen for drug-resistant tuberculosis.
> The TxGNN model predicts it may be effective for **Candidiasis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying rationale itself indicates the mechanism does not translate to fungal pathogens.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-resistant tuberculosis, as part of the BPaL regimen (not recorded in the supplied regulatory dataset — inferred from literature evidence) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed official mechanism-of-action data is currently unavailable (blocking data gap). Based on information available in the accompanying literature evidence, pretomanid is a nitroimidazooxazine prodrug that requires activation by the deazaflavin-dependent nitroreductase (Ddn), an enzyme specific to mycobacteria. Once activated, it generates reactive nitrogen species that inhibit mycolic acid synthesis (aerobic conditions) or act as a respiratory poison releasing nitric oxide (anaerobic conditions). This activation pathway is unique to the *Mycobacterium* genus.

Candidiasis is caused by *Candida* species (fungi), which lack the Ddn enzyme system and mycolic acid synthesis pathway entirely. There is therefore no plausible mechanistic bridge between pretomanid's known target biology and fungal infection. The high TxGNN score most likely reflects the model connecting pretomanid to a broad "antimicrobial/anti-infective" node cluster in the knowledge graph rather than any target-specific evidence for antifungal activity.

This concern is reinforced by the model's next-ranked prediction, **leprosy** (rank 2, score 99.27%), which — despite sharing the *Mycobacterium* genus with the original indication and therefore appearing more biologically plausible — is directly contradicted by experimental evidence in the evidence pack itself (PMID 17005816: *M. leprae* is naturally resistant to PA-824/pretomanid, likely due to insufficient Ddn activity). The remaining top-5 predictions (coronary artery disease, myocardial ischemia, ALCAPA) have no mechanistic basis at all and in the case of cardiovascular indications actively conflict with pretomanid's known QT-prolongation liability. Taken together, none of the top 5 TxGNN predictions for this drug currently have credible mechanistic or empirical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Germany Market Information

Pretomanid is **not currently marketed in Germany** — no marketing authorization dossiers are present in the regulatory dataset (0 authorizations, 0 dosage forms recorded).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note (from evidence-pack context, not a formal safety database entry):** the repurposing rationale for cardiovascular predictions (ranks 3–4) references a known QT-interval prolongation risk associated with pretomanid. This should be treated as a signal to verify against official labeling once available, rather than a confirmed finding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (candidiasis) has zero supporting clinical trials or literature, and the drug's known mechanism of action does not extend to fungal pathogens. The next most-evidenced prediction (leprosy) is directly refuted by in vitro resistance data, and lower-ranked predictions (cardiovascular indications) lack any mechanistic basis and conflict with a known cardiac safety liability. There is no credible evidence pathway to advance any of the current top-5 predictions.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TFDA/BfArM label warnings and contraindications before any S1 safety screening can occur
- Resolve DG002: confirm mechanism of action via DrugBank API query
- If candidiasis is to be pursued further, generate or locate preclinical in vitro antifungal susceptibility data for pretomanid against *Candida* spp.
- Given the leprosy resistance finding, deprioritize further leprosy investigation unless new experimental evidence emerges
- No further action recommended on cardiovascular-related predictions (ranks 3–5) absent a plausible mechanistic hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

