---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Vestronidase Alfa: From Mucopolysaccharidosis Type VII (Sly Syndrome) to Scheie Syndrome

## One-Sentence Summary

> Vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy, originally developed for **Mucopolysaccharidosis Type VII (Sly Syndrome)**.
> The TxGNN model predicts it may be effective for **Scheie Syndrome (MPS I)**,
> but **no clinical trials or literature** currently directly support this specific indication, and the underlying mechanistic rationale flags this as a likely false-positive prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis Type VII (Sly Syndrome) *(not present in German license data — drug not marketed; sourced from supporting literature)* |
| Predicted New Indication | Scheie Syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vestronidase alfa is a recombinant human β-glucuronidase (GUS) enzyme replacement therapy. Its only validated mechanism is to correct the enzymatic deficiency caused by **GUSB** gene mutations in MPS VII (Sly syndrome), restoring the breakdown of glycosaminoglycans (GAGs) that would otherwise accumulate in lysosomes.

Scheie syndrome, however, is a subtype of **MPS I**, caused by deficiency of **alpha-L-iduronidase (IDUA)** — a different enzyme acting on a different (though related) glycosaminoglycan substrate. There is no known biochemical cross-reactivity or substitutability between GUS and IDUA. According to the evidence pack's own mechanistic assessment, this high TxGNN score most likely reflects **knowledge-graph embedding similarity** between phenotypically related lysosomal storage diseases, rather than a genuine shared drug-target mechanism.

This concern is reinforced by the broader prediction list: eight of the nine top-ranked candidates (Hurler syndrome, Sanfilippo syndrome, and several unrelated congenital syndromes) show the same pattern — high similarity scores driven by lysosomal-storage-disease clustering in the graph, but no enzyme-level rationale and, in several cases, literature that on closer inspection actually pertains to the drug's *original* approved indication (MPS VII) rather than the predicted one. This suggests a possible disease-label mismatch issue in the underlying evidence database that warrants manual review before any of these candidates advance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Germany Market Information

Vestronidase alfa is **not currently marketed in Germany**; no BfArM authorization records exist for this evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: A blocking data gap exists — the official TFDA/BfArM label, warnings, and contraindications have not yet been retrieved, which prevents this candidate from entering the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials or literature directly support vestronidase alfa's use in Scheie syndrome; the prediction is supported only by a raw TxGNN similarity score (L5 evidence).
- The proposed mechanism (GUS replacement) does not match the enzymatic deficiency underlying Scheie syndrome (IDUA), indicating this is likely a false-positive driven by structural similarity among lysosomal storage diseases in the knowledge graph rather than a real pharmacological link.
- A blocking data gap (missing official label/warnings/contraindications) independently prevents progression to safety pre-assessment (S1).

**To proceed, the following is needed:**
- Retrieve the official TFDA/BfArM package insert (warnings, contraindications) to close the blocking data gap
- Obtain confirmed MOA and original indication data from DrugBank to replace the current "[Data Gap]" record
- Manually audit the literature associated with other candidates in this evidence pack (e.g., Sanfilippo syndrome) for possible disease-label mismatches before further use
- If pursuing this candidate further, commission a targeted literature/preclinical search specifically for GUS/IDUA cross-reactivity or any case reports of vestronidase alfa use in MPS I patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

