---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

> Aztreonam is a monobactam antibiotic historically used against serious Gram-negative bacterial infections.
> TxGNN generated 10 candidate new indications for this drug; of these, only **Gonococcal Urethritis** is backed by real clinical and literature evidence — **1 completed Phase 2/3 trial** and **8 publications** (including one historical RCT).
> The nine other top-scoring candidates (e.g., hyperamylasemia, congenital analbuminemia, polyclonal hyperviscosity syndrome) have no supporting evidence and no plausible mechanism, and are rated **L5 / Hold**. This report focuses on the one indication with an actionable evidence base.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-negative bacterial infections (monobactam antibiotic class) — not formally recorded in this evidence pack |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Germany Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation for aztreonam is currently a data gap in this evidence pack. However, based on the pharmacological information available (drawn from the repurposing rationale), aztreonam is a **monocyclic β-lactam (monobactam) antibiotic** that inhibits **penicillin-binding protein 3 (PBP3)** in Gram-negative bacteria, blocking cell wall synthesis. *Neisseria gonorrhoeae* is a Gram-negative diplococcus, so this is a direct extension of aztreonam's known antibacterial spectrum rather than a novel or speculative mechanism.

This is not a cross-disease repurposing story in the traditional sense — it is closer to **indication expansion within the same pharmacological class of activity** (Gram-negative bactericidal action). The clinical rationale is driven by the global antimicrobial resistance (AMR) crisis: cephalosporins are now the only consistently reliable class against *N. gonorrhoeae*, and reevaluating older, underused antibiotics such as aztreonam is being actively pursued as a stopgap therapy.

By contrast, the model's top-ranked prediction (hyperamylasemia, score 99.73%) and several other high-scoring candidates (congenital analbuminemia, polyclonal hyperviscosity syndrome) have **no known mechanistic link** to an antibacterial cell-wall synthesis inhibitor and **zero supporting clinical or literature evidence** — these are flagged internally as likely embedding-space artifacts rather than genuine repurposing signals, and are excluded from further development (Hold).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Open-label demonstration study of aztreonam for pharyngeal gonorrhea, motivated by the CDC-designated urgent AMR threat of antimicrobial-resistant *N. gonorrhoeae*; reevaluates an older antibiotic as cephalosporin resistance emerges. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | RCT | Genitourinary Medicine | Single 1g IM dose cleared *N. gonorrhoeae* in 61 men and 26 women at all sites (except one pharyngeal case); well tolerated, effective against both penicillin-sensitive and -resistant strains. |
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Single-arm clinical trial | Antimicrobial Agents and Chemotherapy | Single-dose 2g IM aztreonam evaluated as a repurposed treatment for gonorrhea amid the threat of ceftriaxone resistance; companion publication to NCT03867734. |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Cohort/Therapeutic | Journal of Infectious Diseases | Demonstrated effectiveness of aztreonam against penicillinase-producing (penicillin-resistant) gonococci (PPNG). |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Cohort/Therapeutic | Antimicrobial Agents and Chemotherapy | 1g IM aztreonam compared with 2g IM spectinomycin for uncomplicated gonorrhea; no treatment failures with either drug. |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Cohort/Bacteriological-clinical | Japanese Journal of Antibiotics | Bacteriological and clinical evaluation of aztreonam in 30 men with gonorrheal urethritis, including PPNG strains. |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Cohort/Therapeutic | Hinyokika Kiyo (Acta Urologica Japonica) | Epidemiologic and one-shot therapeutic study of aztreonam in gonorrheal infections in Japan. |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Cohort/Therapeutic | Giornale Italiano di Dermatologia e Venereologia | Study of aztreonam in patients with acute gonococcal urethritis. |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Surveillance/Resistance | Journal of Infection and Chemotherapy | Documents emergence of cephem- and aztreonam-highly-resistant *N. gonorrhoeae* not producing beta-lactamase — an important resistance-monitoring caveat for this indication. |

---

## Germany Market Information

Aztreonam currently has **no marketing authorization in Germany** under this evidence pack (0 authorizations, status: Not marketed). No product-level dosage form or label data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data was returned for this query (query status: not found).

> **Note:** A blocking data gap has been identified — TFDA/BfArM label warnings and contraindications are not yet available, which prevents this candidate from entering the S1 initial safety review stage. This must be resolved before any further development decision is finalized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Aztreonam's antibacterial activity against *N. gonorrhoeae* is directly explained by its known mechanism (PBP3 inhibition) rather than a novel repurposing hypothesis, and is supported by one historical RCT plus a completed modern Phase 2/3 demonstration trial (NCT03867734) conducted specifically to address emerging cephalosporin resistance. However, most supporting literature predates modern resistance patterns (1983–1986), and the recent trial has a small, non-randomized sample (n=32).

**To proceed, the following is needed:**
- TFDA/BfArM package insert data (warnings, contraindications) — currently a **blocking** gap preventing S1 safety review
- Formal MOA documentation from DrugBank to replace the current data gap
- Updated resistance surveillance data on cross-resistance between aztreonam and third-generation cephalosporins in contemporary *N. gonorrhoeae* isolates
- A larger randomized controlled trial (particularly addressing pharyngeal eradication rates) to upgrade evidence beyond the current single small trial
- Regulatory/market feasibility assessment, given 0 current marketing authorizations in Germany
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

