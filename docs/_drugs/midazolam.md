---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Midazolam
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

# Midazolam: Toward a Predicted Indication for Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine; the original approved indication is not documented in the current evidence pack (regulatory data shows no active market license). The TxGNN model predicts efficacy for **Insomnia**, a use that is already well supported by multiple older clinical studies rather than being a truly novel repurposing signal, with **31 clinical trials** and **11 publications** returned in the evidence search — though most trials use midazolam only as a comparator arm rather than as the primary intervention for insomnia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack — `taiwan_regulatory.licenses` is empty and no original indication text is provided (data gap) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (multiple historical double-blind RCTs directly testing midazolam in insomnia; no modern Phase 2/3-registered trials for this indication specifically) |
| Germany Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the evidence pack. Based on well-established pharmacological knowledge, midazolam is a short-acting benzodiazepine that acts as a positive allosteric modulator at GABA-A receptors, enhancing inhibitory GABAergic neurotransmission. This mechanism underlies its established clinical roles in sedation, anxiolysis, anesthesia induction, and — directly relevant here — sleep induction.

Because the evidence pack contains no original indication text (licenses array is empty; market status is "Not marketed"), we cannot state with certainty what the drug's originally approved indication was in this jurisdiction. However, midazolam's sedative-hypnotic pharmacology is inherently linked to sleep induction, which is consistent with the TxGNN-predicted indication of insomnia.

It is worth flagging that this prediction largely reconfirms an already well-known pharmacological use of benzodiazepines (short-term hypnotic therapy) rather than identifying a genuinely novel mechanistic repurposing opportunity — several of the supporting publications date from the 1980s–1990s and directly tested midazolam as a hypnotic. The clinical significance here is therefore less about scientific novelty and more about whether local regulatory/market re-entry for this specific indication is warranted.

---

## Clinical Trial Evidence

Most trials in the raw evidence set use midazolam only as a sedation comparator for unrelated primary endpoints (e.g., delirium prevention, headache, oncology). The following are the trials most directly relevant to midazolam and sleep/insomnia-related outcomes:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Compared postoperative sleep quality of IV dexmedetomidine vs. midazolam combined with spinal anesthesia in TURP patients |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Recruiting | 280 | Preoperative oral midazolam effect on postoperative pain in patients with pre-existing sleep disturbance/anxiety undergoing laparoscopic colorectal cancer resection |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Completed | 23 | Randomized double-blind study of transitioning benzodiazepine (midazolam) sedation to dexmedetomidine to facilitate ICU extubation |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | 24-hour polysomnography comparison of sleep quality/quantity and delirium incidence: dexmedetomidine vs. midazolam in mechanically ventilated ICU patients |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α2 agonists vs. GABA agonists (including midazolam) on sleep stages and total sleep time |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Sedation efficacy of dexmedetomidine vs. midazolam in critically ill ventilated children |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unknown | 285 | Remimazolam (benzodiazepine class) vs. standard sedation for ICU mechanical ventilation after oral/maxillofacial surgery |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | NA | Completed | 131 | RCT comparing remimazolam general anesthesia vs. propofol + midazolam control group |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Phase 2 | Recruiting | 110 | Midazolam-controlled RCT of internet-based CBT + IV ketamine for suicidality in treatment-resistant depression |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | NA | Completed | 178 | Effect of ketamine (add-on to midazolam-based sedation) on sleep quality in colonoscopy patients |

*Note: These trials are indirect evidence (midazolam largely used as an active comparator/sedation background), not trials designed to test midazolam as a primary treatment for a diagnosed insomnia disorder.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | Br J Clin Pharmacol | Double-blind study: midazolam 15 mg vs. Vesparax in insomnia secondary to neuromuscular disease; both effective, midazolam better tolerated with no hangover effect |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | J Clin Psychopharmacol | Multicenter randomized double-blind parallel-group study: 14-day midazolam vs. flurazepam in chronic insomniacs, assessing sleep, performance, and plasma levels |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | J Clin Psychopharmacol | Executive summary of the above 14-day multicenter midazolam vs. flurazepam trial in chronic insomnia |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT (dose-finding) | Arzneimittelforschung | Multicenter pilot study of oral midazolam (10–30 mg) in 75 patients with mild-to-moderate insomnia secondary to musculoskeletal/neurologic/allergic conditions |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Review of clinical use of hypnotics (including benzodiazepines) across insomnia subtypes |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | Review of insomnia pathogenesis, including hyperarousal and cerebral hypoperfusion mechanisms |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Pilot study | J Clin Med | Evaluated lemborexant for insomnia to reduce delirium risk in high-risk endoscopy patients; notes traditional benzodiazepine use for insomnia may worsen delirium |

---

## Germany Market Information

Midazolam currently holds **no active marketing authorization** on file in this dataset (`market_status`: 未上市 / Not marketed; `total_licenses`: 0). No product/license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All fields in `safety.key_warnings`, `safety.contraindications`, and `safety.ddi` are marked as data gaps in the evidence pack. Note also that data gap DG001 — TFDA label warnings/contraindications — is classified as **Blocking severity**, meaning safety review (S1) cannot currently proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (insomnia) is pharmacologically plausible and supported by several historical RCTs, but this evidence pack has a **Blocking**-severity data gap (missing TFDA label/safety data), which by definition prevents entry into the S1 safety initial assessment.
- The drug has no active market authorization in this jurisdiction (0 licenses), and no original indication text is available for comparison.
- The predicted "new" indication substantially overlaps with midazolam's already-known hypnotic pharmacology rather than representing a novel mechanistic finding, reducing the urgency/value of further repurposing investment relative to the missing safety data.

**To proceed, the following is needed:**
- Obtain TFDA (or relevant regulatory) package insert data — warnings, contraindications, drug interactions (DG001, Blocking)
- Confirm DrugBank-sourced MOA and drug categories directly (DG002, High)
- Clarify the drug's original/currently approved indication(s), if any, in the target market
- If pursuing further, identify or commission clinical trials that test midazolam as a primary intervention for diagnosed insomnia (current trial evidence is indirect/comparator-based)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

