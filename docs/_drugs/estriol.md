---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Estriol: From [Indication Not Specified] to Amenorrhea

## One-Sentence Summary

> Estriol is a weak, naturally occurring estrogen; no approved indication or mechanism-of-action data is on record in this evidence pack, and the drug is **not currently marketed in Germany**.
> The TxGNN model predicts potential efficacy for **Amenorrhea** (specifically functional hypothalamic amenorrhea, FHA), with a prediction score of **99.18%**.
> However, supporting evidence is thin and partly mismatched: only **3 clinical trials** were retrieved, all graded low relevance (two are very likely Estetrol/drospirenone contraceptive trials, not Estriol), alongside **13 literature** records, most lacking abstracts or direct focus on Estriol.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no indication data on record (drug not marketed, `original_indications` empty) |
| Predicted New Indication | Amenorrhea (functional hypothalamic amenorrhea / FHA) |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Estriol. Based on known pharmacology, Estriol is a naturally occurring, comparatively weak estrogen. The repurposing rationale here is not an Estriol-specific mechanism but a general estrogen-class mechanism: exogenous estrogen supplementation may modulate hypothalamic-pituitary-ovarian (HPO) axis feedback and restore pulsatile LH secretion, which is the therapeutic principle underlying hormone replacement in functional hypothalamic amenorrhea (FHA) or premature ovarian insufficiency (POI).

Importantly, this mechanistic link is shared across the estrogen class and is not unique to Estriol — the evidence supporting it is largely indirect, drawn from general FHA/POI hormone-replacement literature rather than Estriol-specific comparative trials with amenorrhea as a primary efficacy endpoint. One cohort/pilot study (PMID 22137494) directly examines Estriol's effect on LH secretion in FHA patients, which is the strongest direct data point available, but it stands alone without confirmatory RCTs.

A caveat on the clinical trial evidence: two of the three retrieved trials (NCT04090957, NCT04209543) have titles and design characteristics (Phase 3, large enrollment, "Estetrol") strongly suggesting they concern **Estetrol (E4)**, a different estrogen, likely in a combined oral contraceptive — not Estriol. These should be treated as low-confidence matches pending manual verification, not as direct support for this candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Phase 2 | Withdrawn (N=0) | 0 | Studied photobiomodulation (not Estriol) for postmenopausal vulvovaginal atrophy; trial withdrawn, no data generated. Low relevance (Grade C). |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Phase 3 | Completed | 1,015 | Evaluated Estetrol (E4), likely in a combined oral contraceptive, for vasomotor symptoms; amenorrhea/bleeding profile likely a secondary endpoint. Drug identity mismatch suspected — **not confirmed to be Estriol** (Grade C). |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Phase 3 | Completed | 1,570 | Sister trial to above (Estetrol/E4Comfort Study I); same drug-identity concern (Grade C). |

**Note:** None of the three trials provide confirmed, direct evidence of Estriol's efficacy in treating amenorrhea. Manual verification of drug identity is recommended before these are used as supporting evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Cohort/Pilot | Fertility and Sterility | Estriol administration modulated LH secretion in women with functional hypothalamic amenorrhea — the most directly relevant Estriol-specific finding. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Review | Biomedicines | Reviews low-dose estrogens as neuroendocrine modulators in FHA, discussing triggering of positive feedback mechanisms restoring gonadotropin pulsatility. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Cohort | Medicinski pregled | Estro-progestagen therapy improved lipid/hormonal profile in premature primary ovarian failure (hypergonadotropic amenorrhea). |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | pending | J Obstet Gynaecol Br Commonw | Historical trial of gonadotrophins in idiopathic secondary amenorrhoea; no abstract available. |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Case Report | Lancet | Endocrinological findings in two patients with premature ovarian failure; no abstract available. |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observational | Zhong Xi Yi Jie He Za Zhi | Observations on gonadal function changes in women with amenorrhea/oligomenorrhea; no abstract available. |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | pending | J Clin Endocrinol Metab | Mechanism of action of anti-ovulatory compounds; no abstract available. |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Case Report | Br J Psychiatry | Case discussion of anorexia nervosa (a recognized cause of FHA); no abstract available. |
| [4307531](https://pubmed.ncbi.nlm.nih.gov/4307531/) | 1969 | pending | Fertility and Sterility | Comparative effects of estrogens on cervical mucus amylase levels; no abstract available. |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Review | Clin Obstet Gynecol | General review on neoplasia and hormonal contraception; only tangentially related. |

**Note:** Only 2 of the 10 listed items (PMID 22137494, 37371858) are directly and specifically about Estriol/low-dose estrogen in FHA. The remainder are older, low-tier records without abstracts, included for completeness but of limited independent evidentiary value.

---

## Germany Market Information

Estriol is currently **not marketed in Germany** — no BfArM authorizations are on record in this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all marked as data gaps in this evidence pack — see DG001, a Blocking-severity gap that prevents initial safety assessment (S1) until TFDA/BfArM label data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, and one directly relevant pilot study (PMID 22137494) supports a plausible mechanism, but overall evidence quality is weak: no confirmed Estriol-specific RCT exists, two of the three retrieved clinical trials likely concern a different drug (Estetrol) and should not be counted as support, and a Blocking-severity safety data gap (DG001) prevents any initial safety evaluation. This aligns with the evidence pack's own S1 "Research Question" staging.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/BfArM label warnings and contraindications for Estriol
- Resolve DG002: obtain confirmed mechanism-of-action data from DrugBank
- Manually verify drug identity for NCT04090957 and NCT04209543 (Estriol vs. Estetrol) before counting them as evidence
- Identify or commission an Estriol-specific controlled trial in FHA/POI patients with amenorrhea resolution as a primary endpoint
- Confirm original approved indication(s) for Estriol, currently missing from this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

