---
layout: default
title: Carprofen
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Carprofen
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

# Carprofen: From Withdrawn Human NSAID to Rheumatoid Arthritis (Re-evaluation)

## One-Sentence Summary

Carprofen is a propionic-acid-derivative NSAID that was originally developed and marketed for human use in rheumatoid arthritis and related inflammatory conditions during the 1980s, but was withdrawn from the human pharmaceutical market after hepatotoxicity signals (including fatal fulminant hepatitis) and now survives commercially only as a veterinary drug (e.g., canine Rimadyl). The TxGNN model's top prediction — **Rheumatoid Arthritis** — is essentially a re-identification of the drug's own historical human indication, supported by **0 registered clinical trials** and **20 mostly historic (1980–1990) publications**, including two double-blind RCTs. Given the unresolved human hepatotoxicity signal behind its market withdrawal, current evidence is insufficient to support renewed human development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in structured registry data (taiwan_regulatory.licenses / drug.original_indications are empty). Per literature/rationale evidence: historically marketed as a human NSAID for rheumatoid arthritis and related inflammatory conditions in the 1980s–90s. |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug profile (DG002). Based on literature evidence within this evidence pack, carprofen is a propionic-acid-derivative NSAID that inhibits COX-1/COX-2 and lowers prostaglandin synthesis — a mechanism shared with comparator agents such as indomethacin, against which it was directly tested in several 1980s trials.

Importantly, this is not a conventional "repurposing" case in the sense of finding a genuinely new use. Carprofen was originally developed and marketed for human use in rheumatoid arthritis and related inflammatory/pain conditions. It was subsequently withdrawn from the human pharmaceutical market following post-marketing reports of hepatotoxicity, including fatal fulminant hepatitis, and today exists commercially only as a veterinary NSAID for canine osteoarthritis. TxGNN's top prediction of rheumatoid arthritis therefore reflects the model recovering the drug's own historical human indication rather than uncovering a novel therapeutic opportunity — the mechanistic plausibility is high and well-documented historically, but the human clinical development path is blocked by an unresolved safety signal that has never been formally resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7009441](https://pubmed.ncbi.nlm.nih.gov/7009441/) | 1980 | RCT (comparative) | Int J Clin Pharmacol Ther Toxicol | 6-week double-blind trial in 36 RA patients; carprofen (two dose ranges) vs. indomethacin 100mg/day, comparable efficacy with toxicity monitoring |
| [6340183](https://pubmed.ncbi.nlm.nih.gov/6340183/) | 1983 | RCT (double-blind crossover) | Scand J Rheumatol Suppl | 4-month crossover in 28 RA patients; carprofen 300mg/day vs. indomethacin 75mg/day, both effective |
| [3554157](https://pubmed.ncbi.nlm.nih.gov/3554157/) | 1987 | Review | Pharmacotherapy | Comprehensive review of carprofen pharmacology, clinical efficacy in RA/OA, and adverse effects; potency roughly 1/4 of indomethacin |
| [6431808](https://pubmed.ncbi.nlm.nih.gov/6431808/) | 1984 | Review (mechanistic) | Am J Med | Reviews NSAID mechanism of action in RA beyond simple COX inhibition, including immunomodulatory prostaglandin effects |
| [6759135](https://pubmed.ncbi.nlm.nih.gov/6759135/) | 1982 | Review | Eur J Rheumatol Inflamm | General review of clinical trials in rheumatoid arthritis (abstract not available) |
| [6573017](https://pubmed.ncbi.nlm.nih.gov/6573017/) | 1983 | PK study | Scand J Rheumatol Suppl | Serum/synovial fluid concentrations measured in 13 RA patients after 100mg oral dose |
| [7037867](https://pubmed.ncbi.nlm.nih.gov/7037867/) | 1981 | Cohort/comparative | J Clin Pharmacol | Renal salt/water homeostasis effects of carprofen vs. indomethacin in RA patients and healthy controls |
| [3293874](https://pubmed.ncbi.nlm.nih.gov/3293874/) | 1988 | PK/dose-response study | Clin Pharmacol Ther | Multiple-crossover dose-response study (100–800mg/day) in 38 RA patients; linear dose-response demonstrated for 6/9 efficacy measures |
| [2155476](https://pubmed.ncbi.nlm.nih.gov/2155476/) | 1990 | Mechanistic/lab study | Scand J Rheumatol | Synovial fluid white cell count, PGE2, LTB4, cAMP effects of carprofen vs. other NSAIDs/prednisolone in 53 RA patients |
| [3864577](https://pubmed.ncbi.nlm.nih.gov/3864577/) | 1985 | Mechanistic study | Clin Rheumatol | Compares effects of 9 NSAIDs on synovial fluid prostanoid concentrations in RA patients; carprofen reduced PGE2/TxB2 |

---

## Germany Market Information

No current marketing authorizations were found for carprofen in this dataset (`total_licenses: 0`, `market_status: 未上市`), consistent with its withdrawal from the human pharmaceutical market. It remains available only as a veterinary product (e.g., Rimadyl for dogs) outside the scope of this human-indication regulatory dataset.

---

## Safety Considerations

- **Historical Human Safety Signal**: Carprofen was withdrawn from the human NSAID market in the 1980s–90s following post-marketing reports of hepatotoxicity, including fatal fulminant hepatitis (per the repurposing rationale documented in this evidence pack). This is the primary reason it is no longer marketed for human use.
- No structured TFDA/German label data (key warnings, contraindications, drug interactions) is currently available (DG001, Blocking gap) — formal safety review cannot proceed until the package insert / regulatory hepatotoxicity case data is retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Carprofen has strong historical mechanistic and clinical-trial support for rheumatoid arthritis (two double-blind RCTs, multiple PK/dose-response studies), but this is essentially confirmation of its own original human indication rather than a novel repurposing signal. The drug's known hepatotoxicity-driven withdrawal from the human market is an unresolved safety issue that blocks any S1 safety evaluation, and no current clinical trials, regulatory filings, or structured safety data support renewed human development. Lower-ranked predictions (e.g., gout L3, tendinitis L4) show the same COX-inhibition rationale but weaker evidence and are also flagged Hold.

**To proceed, the following is needed:**
- Retrieval of historical hepatotoxicity case data and any TFDA/EMA withdrawal documentation (DG001, Blocking)
- Structured mechanism of action data from DrugBank (DG002)
- A formal risk-benefit reassessment specifically addressing the prior human hepatotoxicity signal before any renewed human clinical development is considered
- Confirmation of current regulatory/marketing status (human vs. veterinary only) in target jurisdictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

