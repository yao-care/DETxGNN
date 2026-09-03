---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Esomeprazole: From Acid-Related Gastrointestinal Disease to Duodenogastric Reflux

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor (PPI) with an extensive, well-established evidence base for acid-related gastrointestinal conditions such as duodenal ulcer, GERD, and *H. pylori*-associated disease. The TxGNN model's top-ranked new prediction is **Duodenogastric Reflux**, but this direction is currently supported by only **0 clinical trials** and **1 general review article**, and the mechanistic link is explicitly flagged as indirect. A separate, much better-supported signal in this evidence pack — duodenal ulcer — largely overlaps with the drug's already-established use rather than representing true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from German licensing records (0 authorizations on file). Per the literature evidence in this pack, esomeprazole is an established therapy for reflux esophagitis/GERD, gastric and duodenal ulcer (including NSAID-associated), *H. pylori* eradication, and Zollinger-Ellison syndrome |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (original MOA marked as a data gap). Based on known pharmacology, esomeprazole is the S-isomer of omeprazole and inhibits the gastric parietal cell H⁺/K⁺-ATPase, reducing acid secretion. This mechanism underlies its well-documented efficacy across the acid-related disease spectrum, and in principle could extend to any condition where the gastric acid environment contributes to mucosal injury.

However, the rationale provided for duodenogastric reflux is explicitly characterized as **weak and indirect**: duodenogastric reflux is driven primarily by bile and duodenal contents rather than gastric acid, so PPI therapy does not address the underlying reflux mechanism and can only indirectly mitigate acid-related mucosal symptoms. This is reflected in the evidence level (L4) and decision stage (S1, "Research Question").

Notably, a separate prediction in this pack — duodenal ulcer (rank 3) — carries much stronger evidence (L1, S3, "Proceed with Guardrails," 40+ clinical trials including multiple completed Phase 3 RCTs) but is annotated in the evidence pack itself as effectively **the drug's original indication rather than genuine repurposing**. This is a useful sanity check on model calibration but should not be mistaken for a novel signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General PPI class review: PPIs are first-line for peptic ulcer, *H. pylori* infection, GERD, NSAID-induced GI lesions, and Zollinger-Ellison syndrome; does not specifically address duodenogastric reflux |

---

## Germany Market Information

Esomeprazole currently holds no marketing authorizations in the German dataset (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: per the evidence pack's data gap log, TFDA/label warnings and contraindications (DG001, **Blocking** severity) have not yet been retrieved, which by definition **prevents completion of the S1 safety pre-assessment** for this candidate. DDI query also returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (duodenogastric reflux) has only L4 evidence — a single general PPI review and no dedicated clinical trials — combined with an explicitly indirect mechanistic rationale. A Blocking-severity data gap (missing label warnings/contraindications) also prevents completion of the required S1 safety pre-assessment, and the drug has zero current marketing authorizations in Germany.

**To proceed, the following is needed:**
- Retrieve TFDA/German label warnings and contraindications (DG001) to complete S1 safety screening
- Obtain esomeprazole's detailed MOA data from DrugBank (DG002) to strengthen the mechanistic case
- Identify dedicated clinical or preclinical evidence specific to duodenogastric reflux (currently none)
- Clarify current/planned licensing status in Germany, given zero authorizations on file
- Treat the duodenal ulcer signal (rank 3) as confirmatory of model calibration only, not as a repurposing opportunity, since it overlaps with esomeprazole's established use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

