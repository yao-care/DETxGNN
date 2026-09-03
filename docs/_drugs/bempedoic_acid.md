---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From LDL-Cholesterol Lowering to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor used to lower LDL-cholesterol in patients with hypercholesterolemia and elevated cardiovascular risk.
> Among the TxGNN model's top 10 predictions, most (hyperthyroidism, veterinary infections, oncogenic syndromes, etc.) show **no plausible mechanistic link** and are annotated as likely knowledge-graph noise.
> The one prediction with genuine biological rationale and real-world evidence is **Homozygous Familial Hypercholesterolemia (HoFH)**, supported by **1 real-world cohort study** and **17 additional publications**, though **no clinical trials** are currently registered for this specific population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured data (`original_indications` empty). Based on mechanistic evidence in this pack, bempedoic acid is used for LDL-C lowering / primary hypercholesterolemia |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (rank 6040 of the disease space) |
| Evidence Level | L3 (real-world cohort + review literature, no RCTs) |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on ranking:** TxGNN's #1-ranked prediction (hyperthyroidism, score 99.61%) and most other top-10 predictions were excluded from this report — the evidence pack itself flags them as having "no plausible mechanism" or being mismatched to unrelated drugs (e.g., tiratricol) or veterinary diseases. This report focuses on rank 6 (HoFH), the only candidate with a coherent mechanism and supporting literature.

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record for bempedoic acid is not available in this evidence pack (`original_moa: [Data Gap]`). However, the repurposing rationale attached to the HoFH prediction provides sufficient mechanistic detail to evaluate plausibility.

Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor that acts upstream of HMG-CoA reductase in the cholesterol biosynthesis pathway. It is a prodrug activated selectively in the liver (via VLACS1, an enzyme not expressed in skeletal muscle), which explains its favorable muscle-related side-effect profile compared to statins. This liver-selective inhibition upregulates LDL receptor (LDLR) expression, thereby lowering circulating LDL-C.

HoFH patients most commonly carry compound heterozygous or homozygous *LDLR* mutations that reduce — but do not always completely abolish — receptor function. Because bempedoic acid's mechanism depends on residual LDLR activity, patients with non-null LDLR genotypes may retain partial pharmacological response. This makes bempedoic acid mechanistically plausible as an **add-on therapy** for HoFH patients who remain above LDL-C targets despite statins and PCSK9 inhibitors, rather than as a monotherapy or first-line treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-world cohort | J Clin Lipidol | Direct real-world evaluation of bempedoic acid efficacy and tolerability specifically in HoFH patients |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expert consensus | J Clin Lipidol | National Lipid Association update on FH management, reflecting current LDL-C lowering strategies including bempedoic acid |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Reviews treatment advancements for HoFH, positioning bempedoic acid among add-on LDL-C lowering options |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Innovative therapies for HoFH management, covering LDLR-targeted and adjunct pharmacotherapies |
| [41694628](https://pubmed.ncbi.nlm.nih.gov/41694628/) | 2026 | Case report + review | Clin Case Rep | Case of catastrophic HoFH progression after interrupted follow-up; underscores need for continuous aggressive LDL-C control |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical | Arterioscler Thromb Vasc Biol | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient (LDLR+/- and LDLR-/-) miniature pig model, directly relevant to HoFH pathophysiology |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review (comparator drug) | Cardiol Rev | Discusses evinacumab for HoFH, referencing bempedoic acid among adjunct lipid-lowering therapies |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | JACC seminar on emerging LDL-C/ApoB-lowering therapies, discusses bempedoic acid's mechanism and clinical role |
| [35754818](https://pubmed.ncbi.nlm.nih.gov/35754818/) | 2022 | Review | Front Genet | Reviews treatment progression for refractory hypercholesterolemia including HoFH |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiol Rep | Reviews management updates beyond statins/PCSK9i for familial and refractory hypercholesterolemia |

---

## Germany Market Information

Bempedoic acid is currently not marketed in Germany under this evidence pack (`market_status: 未上市`, `total_licenses: 0`); no authorization records are available.

---

## Safety Considerations

Structured safety data for this drug is currently a **blocking data gap** (`DG001`, severity: Blocking) — TFDA/regulatory label warnings and contraindications have not yet been retrieved, and DDI screening returned no results (`query_status: not_found`). This gap must be resolved before the candidate can advance past initial safety screening (S1).

> Please refer to the package insert for safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the HoFH indication specifically; all other TxGNN top-10 predictions for this drug are **Hold** due to absent mechanistic rationale and no supporting evidence)

**Rationale:**
Bempedoic acid's liver-selective, LDLR-dependent mechanism is biologically compatible with HoFH as an adjunct therapy, and this is supported by one real-world cohort study plus consistent review-level literature — but no dedicated randomized controlled trial exists in this population, capping the evidence at L3.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain TFDA/regulatory label warnings and contraindications before any S1 safety evaluation
- Obtain drug-drug interaction (DDI) data (current query returned no results)
- Confirm structured mechanism-of-action data via DrugBank API (DG002)
- Seek prospective or controlled trial data in HoFH populations (currently only real-world/observational evidence exists)
- Given the drug is not currently marketed in Germany, clarify regulatory pathway/import status before pursuing local development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

