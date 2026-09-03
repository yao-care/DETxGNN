---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 2
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

> Laronidase is a recombinant α-L-iduronidase enzyme replacement therapy already established internationally for **Mucopolysaccharidosis I (MPS I)**.
> TxGNN's top prediction, **Lysosomal Storage Disease with Skeletal Involvement**, is essentially the same disease viewed through its skeletal (dysostosis multiplex) manifestations rather than a genuinely new indication.
> Support currently on file consists of **4 publications** (no registered clinical trials in this evidence pack), and a second candidate — **Sanfilippo syndrome** — scored comparably high but was screened out as mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (MPS I) — laronidase's internationally recognized approved indication; not reflected in local regulatory data because the drug is not marketed here |
| Predicted New Indication | Lysosomal Storage Disease with Skeletal Involvement |
| TxGNN Prediction Score | 99.31% (rank 7521) |
| Evidence Level | L2 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data is not available in this evidence pack, but the repurposing rationale provides sufficient mechanistic detail: laronidase is a **recombinant human α-L-iduronidase**, delivered via enzyme replacement therapy. It is taken up by cells mainly through mannose-6-phosphate receptors, trafficked to lysosomes, and there breaks down the glycosaminoglycans (dermatan sulfate, heparan sulfate) that accumulate in MPS I patients due to their native enzyme deficiency.

Critically, the "new" indication predicted here — lysosomal storage disease with skeletal involvement — is not a distinct disease from a different pharmacological space. It corresponds to the skeletal phenotype (dysostosis multiplex) of MPS I itself, the disease laronidase was designed and approved to treat. In other words, TxGNN has essentially re-derived the drug's own core indication rather than surfaced a genuinely novel repurposing opportunity. This makes the mechanistic link direct and non-inferential, but it also means the clinical value of this "prediction" lies mainly in confirming model validity rather than opening new therapeutic ground.

It is worth noting that a pivotal Phase 3 randomized, double-blind, placebo-controlled trial of laronidase in MPS I (PMID 15126990) exists in the source literature pool but was filed under the second candidate entry (Sanfilippo syndrome) rather than this one. Had it been correctly attributed here, the evidence level for this indication would likely rise from L2 to L1, since laronidase's efficacy in MPS I is already established well beyond exploratory evidence.

**Note on the second candidate (Sanfilippo syndrome):** TxGNN assigned Sanfilippo syndrome (MPS III) a similarly high score (99.22%), but this pairing does not hold up mechanistically. Sanfilippo syndrome results from deficiencies in different enzymes in the heparan sulfate degradation pathway (sulfamidase, NAGLU, HGSNAT, or GNS depending on subtype) — not α-L-iduronidase. Supplementing α-L-iduronidase would not address the underlying substrate accumulation in Sanfilippo patients, and the disease is additionally CNS-predominant, which an IV-administered protein like laronidase cannot reach across the blood-brain barrier. This candidate is correctly flagged **Hold** (evidence level L5) and is treated as a TxGNN false positive, not a viable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Overview of laronidase development as recombinant α-L-iduronidase enzyme replacement therapy for MPS I, including orphan drug and fast-track status |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Describes MPS I disease spectrum (Hurler, Scheie, Hurler/Scheie) and diagnosis via urinary GAG pattern plus iduronidase enzyme assay |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In Vitro/Preclinical | Biological & Pharmaceutical Bulletin | Demonstrates dose-dependent cellular uptake of laronidase mainly via mannose-6-phosphate receptors, with lysosomal trafficking and processing |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Case Report | Pediatric Neurology | 6.5-year follow-up of a Scheie syndrome (attenuated MPS I) patient on ERT, documenting skeletal, cardiac, and other organ outcomes over time |

---

## Germany Market Information

Laronidase is currently **not marketed** in this jurisdiction (0 authorizations on file); no product-level licensing data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for laronidase in this indication is strong because it is, in substance, the drug's own established indication (MPS I with skeletal involvement) rather than a novel repurposing target. However, the evidence pack currently lacks registered clinical trials for this specific entry and is missing local safety labeling data, so it cannot yet clear a full safety review.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings and contraindications) — flagged as a **Blocking** gap (DG001); required before any S1 safety pre-assessment can proceed
- Structured mechanism-of-action data from DrugBank (DG002 — High severity) to formally document the MOA rather than relying on literature-derived rationale
- Correct attribution of the pivotal Phase 3 RCT (PMID 15126990) to this indication entry, which would likely upgrade the evidence level from L2 to L1
- No further action needed on Sanfilippo syndrome — recommend closing this candidate as a screened-out false positive rather than advancing it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

