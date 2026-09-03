---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Entecavir
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

Using the drug-repurposing report template provided in the prompt to synthesize the Entecavir evidence pack directly (this is a self-contained content-generation task with the full spec already given, not a coding/build task, so no additional skill invocation is needed).

I reviewed the evidence pack closely. One thing worth flagging before the report: `predicted_indications[0]` (chronic hepatitis C) is the disease the template's field-extraction rules point to for the title/Quick Overview — but the evidence pack's own `repurposing_rationale` explicitly labels this a TxGNN false positive (no shared drug target, all cited trials/literature are actually about HBV or HBV/HCV coinfection management, not HCV efficacy). I've written the report to follow the template structure exactly while reporting that finding honestly rather than dressing it up as a promising lead — that's what "Hold" and L5 mean here.

---

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

> Entecavir is a nucleoside analogue approved for chronic hepatitis B (HBV), where it inhibits the HBV reverse transcriptase.
> The TxGNN model's top-ranked signal predicts possible activity against **Chronic Hepatitis C Virus Infection**,
> but on review, none of the **40 clinical trials** or **20 publications** retrieved for this pairing actually test entecavir against HCV — they concern HBV treatment or HBV/HCV coinfection management, and the evidence level is **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis B (established indication, referenced in supporting evidence — no formal German market license record was available; see Germany Market Information) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Germany Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for entecavir was not available in the evidence pack. Based on the information present, entecavir is a deoxyguanosine nucleoside analogue whose established pharmacological target is the **hepatitis B virus (HBV) reverse transcriptase** — it blocks priming, pgRNA reverse transcription, and second-strand DNA synthesis, and this is the basis of its approved use in chronic hepatitis B.

Hepatitis C virus (HCV), by contrast, is a *Flaviviridae* RNA virus that replicates via an **RNA-dependent RNA polymerase (NS5B)**, a structurally and mechanistically distinct enzyme with no known cross-reactivity to entecavir's HBV-targeted reverse-transcriptase inhibition. The evidence pack's own mechanistic assessment concludes there is no pharmacological basis for cross-activity.

Consistent with this, the clinical trials and literature returned for the "entecavir + HCV" query do not actually test entecavir's efficacy against HCV. They are HBV treatment trials, or studies of HBV/HCV **coinfection management** (e.g., HBV reactivation risk during HCV direct-acting antiviral therapy) that surfaced only because "hepatitis B and C" appear together in the same abstracts. This pattern is characteristic of a TxGNN false positive driven by textual/semantic similarity between "viral hepatitis" disease nodes, rather than a genuine drug-target relationship. Notably, the model separately and correctly assigns entecavir to its **actual known indication, hepatitis B virus infection** (score 99.85%, evidence level L1, driven by real Phase 3 registration trials such as NCT00036608, NCT00410202, and NCT01079806) — which validates that the model can identify true relationships, but underscores that the HCV signal is not one of them.

---

## Clinical Trial Evidence

Of the 40 clinical trials returned for the "entecavir + chronic HCV" query, only a subset has been reviewed for relevance; all reviewed trials were graded low-relevance (C) because they involve entecavir treating HBV, not HCV. No trial in the retrieved set tests entecavir's efficacy against HCV itself.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Phase 4 | Withdrawn | 0 | Peginterferon alfa-2a ± entecavir in HBeAg-negative chronic hepatitis B — not an HCV trial; withdrawn with zero enrollment. |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs. lamivudine dose-response in Japanese chronic hepatitis B patients — HBV only, no HCV arm. |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | Placebo-controlled safety/PK study of RO7020531 in chronic hepatitis B — entecavir/HCV relevance could not be confirmed from available detail. |

The remaining ~37 trials in the retrieved set are unclassified (pending review) but, based on their titles and summaries, follow the same pattern — nucleos(t)ide analogue therapy for chronic hepatitis B, HBV/HCV coinfection reactivation monitoring, or unrelated hepatitis B pharmacology studies. None report an HCV efficacy endpoint for entecavir.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review (Tier 3) | Wiener medizinische Wochenschrift | Reviews chronic hepatitis B and C treatment as parallel but separate disease tracks; does not test entecavir against HCV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review (Tier 3) | Expert Opinion on Pharmacotherapy | Advances in managing HBV/HCV **coinfection**; entecavir discussed only as the HBV-directed component of coinfection care. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review (Tier 3) | Clinics and Research in Hepatology and Gastroenterology | Discusses the therapeutic challenge of HBV/HCV dual infection; no data on entecavir activity against HCV itself. |

The remaining literature hits (e.g., PMID 28487602, 32173307, 24868325) follow the same pattern — HBV/HCV are discussed together as co-occurring liver diseases or coinfection management topics, not as evidence of entecavir efficacy against HCV.

---

## Germany Market Information

Entecavir is currently **not marketed** in the source regulatory dataset (0 authorizations on record). No product license, dosage form, or approved-indication text was available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The chronic hepatitis C signal is not supported by mechanism (entecavir targets HBV reverse transcriptase; HCV replicates via an unrelated RNA polymerase) or by the retrieved evidence — every clinical trial and publication reviewed addresses HBV treatment or HBV/HCV coinfection management, not entecavir's efficacy against HCV. This is best interpreted as a TxGNN false positive arising from semantic proximity between hepatitis-virus disease nodes, at evidence level L5 (model prediction only, no confirmatory studies).

**To proceed, the following is needed:**
- In vitro evidence (e.g., HCV replicon assay) demonstrating any direct antiviral activity of entecavir against HCV, which is currently absent
- A review of the TxGNN knowledge-graph edges underlying this prediction to determine whether the hepatitis B/C node relationship reflects a data or embedding artifact
- Full DrugBank mechanism-of-action and TFDA/BfArM package insert data for entecavir, both currently unavailable (data gaps DG001, DG002 in this evidence pack), to support any future S1 safety pre-screen

**Additional note on other TxGNN-ranked candidates for entecavir:** across the 10 disease nodes evaluated in this evidence pack, only two show any evidentiary substance — the model's independent, high-confidence recovery of entecavir's **true indication, chronic hepatitis B** (L1, Proceed with Guardrails — useful as a model-validity check, not a new opportunity), and a preclinical signal in **animal hepadnaviral hepatitis** (L3, woodchuck model, PMID 11679911) reflecting entecavir's established antiviral mechanism in a related hepadnavirus. All other candidates (HIV, feline/simian immunodeficiency virus, a rare neurodevelopmental disorder, HEV, HAV) were assessed as Hold with L5 evidence and no plausible mechanistic link.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

