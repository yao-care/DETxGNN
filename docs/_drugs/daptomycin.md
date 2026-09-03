---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic used to treat Gram-positive infections (e.g., complicated skin/skin-structure infections, *S. aureus* bacteraemia). TxGNN's top-ranked prediction is **Osteoarthritis** (score 99.86%), but the underlying literature almost entirely concerns treatment of *infected* joints (prosthetic joint infection, osteoarticular infection) rather than osteoarthritis itself — a likely knowledge-graph conflation. A lower-ranked but mechanistically far more credible signal, **Rheumatoid Arthritis** (rank 2, score 99.84%), is supported by two independent preclinical studies showing daptomycin suppresses inflammatory cytokines and NF-κB signalling in collagen-induced arthritis mice. **No clinical trials exist for either indication; both remain at the hypothesis-generation stage.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in this evidence pack (drug not marketed in this market); internationally approved for complicated skin/skin-structure infections and *S. aureus* bacteraemia, including right-sided infective endocarditis |
| Predicted New Indication | Osteoarthritis (top TxGNN rank; **flagged as likely artifact — see below**) |
| TxGNN Prediction Score | 99.86% (rank 2173) |
| Evidence Level | L4 (per source pack) — but literature is largely off-target (infection studies, not OA pathology) |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacology, daptomycin is a cyclic lipopeptide antibiotic that binds bacterial cell membranes in a calcium-dependent manner, causing membrane depolarization and rapid bactericidal killing of Gram-positive organisms. This mechanism has no established, direct link to the cartilage-degradation and joint-inflammation pathology of osteoarthritis.

Critically, when the top-ranked literature (10 papers) is examined, essentially all of it concerns **daptomycin's antimicrobial use in infected joints** — prosthetic joint infection, osteoarticular infection following *S. aureus* bacteraemia, and *in vitro* susceptibility testing — not osteoarthritis as a degenerative disease entity. This strongly suggests the knowledge graph has conflated "joint infection" and "osteoarthritis" as related joint-disease nodes, producing a high similarity score without genuine mechanistic relevance. **We therefore treat the OA signal as likely spurious.**

### Signal Triage Note: Rheumatoid Arthritis Is the More Credible Candidate

A more scientifically defensible signal appears at rank 2 (Rheumatoid Arthritis, score 99.84%). Two independent, on-target preclinical studies (Tier 2) directly tested daptomycin in the collagen-induced arthritis (CIA) mouse model:

- **PMID 39571268** (2025) — daptomycin suppressed inflammatory cytokines and NF-κB signalling, alleviating CIA in mice, proposed as a novel anti-inflammatory mechanism independent of its antibacterial activity.
- **PMID 40923559** (2025) — a follow-up structure-optimization study synthesizing daptomycin-derived cyclic lipopeptides with improved anti-RA activity in the same model.

This represents a genuinely novel, mechanistically distinct hypothesis (immunomodulation via NF-κB inhibition) rather than a data-conflation artifact, and in our judgment merits a "Research Question" designation for further preclinical validation — well ahead of the top-ranked OA signal in terms of biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (neither for osteoarthritis nor for rheumatoid arthritis).

---

## Literature Evidence

*(Primary table below reflects predicted_indications[0] = Osteoarthritis, per evidence pack structure)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | High-dose daptomycin + rifampicin in Gram-positive osteoarticular *infections* |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Daptomycin for knee/hip periprosthetic joint *infections* |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin for complicated bone/joint and implant-associated *infections* |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy for osteoarticular infection with *S. aureus* bacteraemia |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Antimicrobial susceptibility of staphylococci from prosthetic joint infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry/Cohort | Med Clin (Barc) | EU-CORE registry: real-world daptomycin use in Spain across Gram-positive infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | Case Rep Orthop | *Corynebacterium* septic arthritis misdiagnosed as osteoarthritis |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Cohort | Int J Antimicrob Agents | Survey of prosthetic joint infection management practices |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surg Infect | 10-year microbiologic profile of staphylococci in osteoarticular infections |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | ASM Case Rep | *Corynebacterium propinquum* septic arthritis, first synovial fluid isolation |

**Note on Rheumatoid Arthritis (rank 2, alternative candidate):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Animal preclinical (CIA mouse) | Int Immunopharmacol | Daptomycin suppresses inflammatory cytokines and NF-κB pathway, alleviates collagen-induced arthritis |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Animal preclinical (CIA mouse) | J Med Chem | Daptomycin-derived cyclic lipopeptides with enhanced anti-RA activity in vitro/in vivo |

---

## Germany Market Information

Daptomycin is **not currently marketed** in this jurisdiction (0 authorizations on file); no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or DDI data were available in this evidence pack — flagged as a Blocking data gap, DG001, that must be resolved before any S1 safety evaluation.)

*Contextual note:* one adverse-event case report in the evidence set (PMID 36693494) describes daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis — this is a known safety signal (CPK elevation/myopathy) relevant to musculoskeletal monitoring, not a repurposing opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (osteoarthritis) is not supported by mechanistically relevant evidence — the underlying literature addresses joint *infection* treatment, not osteoarthritis pathology, and no clinical trials exist. This is very likely a knowledge-graph conflation rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001 (drug label warnings/contraindications) before any safety evaluation can begin
- Resolve High-severity data gap DG002 (confirmed mechanism of action) to support mechanistic rationale review
- **Recommend opening a separate research track for Rheumatoid Arthritis** (rank 2): commission or review additional preclinical replication of the CIA mouse model findings (PMID 39571268, 40923559) before considering any clinical-stage investment
- If pursuing RA further, obtain dose-response and toxicity data specific to the anti-inflammatory (non-antibacterial) mechanism, since this would represent off-label, immunomodulatory use distinct from daptomycin's approved antibacterial indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

