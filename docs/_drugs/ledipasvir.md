---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Ledipasvir is the NS5A inhibitor component of the fixed-dose combination Ledipasvir/Sofosbuvir (Harvoni), originally developed and extensively studied for chronic Hepatitis C virus (HCV) infection.
The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**, with **20 clinical trials** and **20 publications** currently retrieved — but on closer review, the vast majority of this evidence describes HCV treatment in HCV/HBV-coinfected patients or HBV *reactivation risk* during HCV therapy, not direct antiviral efficacy against HBV itself.
Only one small, uncontrolled Phase 2 pilot study directly tested Ledipasvir/Sofosbuvir as HBV monoinfection therapy. Nine other TxGNN-predicted indications for this drug (rank 2–10) carry weaker evidence (L4–L5) and are not addressed further here.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (as part of Ledipasvir/Sofosbuvir fixed-dose combination; not formally licensed in Germany per available data) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Germany Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Based on the evidence pack's mechanistic notes, Ledipasvir is an NS5A protein inhibitor used within the Ledipasvir/Sofosbuvir combination, and its efficacy in chronic HCV infection is well established through numerous Phase 2–3 trials. However, Ledipasvir has **no known direct inhibitory activity against HBV polymerase or cccDNA** — its target protein (HCV NS5A) has no structural or functional counterpart in HBV.

The relationship between the original and predicted indications is therefore largely a matter of shared patient populations rather than shared drug mechanism: HCV and HBV frequently co-infect the same individuals (shared transmission routes), so almost all retrieved trials and publications involve HCV/HBV-coinfected cohorts being treated with Ledipasvir/Sofosbuvir *for their HCV*, with HBV monitored only as a safety endpoint. Several of these publications (e.g., PMID 29334502, PMID 34864948, PMID 27486112) specifically study **HBV reactivation risk** during DAA-based HCV therapy — a safety signal, not a therapeutic effect.

The one exception is a Phase 2 open-label pilot study (NCT03312023 / PMID 36045503) that directly administered Ledipasvir/Sofosbuvir to HBV-infected (not HCV-coinfected) subjects and observed a modest reduction in HBsAg. This is the only piece of evidence offering a plausible efficacy signal, but it is a small, single-arm, uncontrolled study, and given that Ledipasvir/Sofosbuvir has separately been explored for Hepatitis D virus (HDV) — which depends on the HBV envelope but replicates via an HBV-independent RNA mechanism more plausibly affected by NS5A-class inhibitors — this trial's true target disease (HBV vs. HDV) should be verified before drawing conclusions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Only trial directly testing LDV/SOF as therapy in HBV-infected (not HCV-coinfected) subjects; assessed HBsAg/HBV DNA decline as primary/secondary endpoints |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF FDC in Taiwanese subjects with chronic genotype 1/2 HCV **and** HBV coinfection; primary endpoint remains HCV antiviral efficacy |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of HBV reactivation incidence/morbidity during DAA treatment of HCV/HBV coinfection — a safety, not efficacy, endpoint |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Phase 4 | Completed | 64 | Prison-population screening/treatment program covering HCV, HBV and HIV; HBV prevalence characterized but treatment targeted at HCV |
| [NCT02597166](https://clinicaltrials.gov/study/NCT02597166) | Phase 3 | Completed | 14 | Antiviral therapy effects on decompensated cirrhosis in HCV genotype 1 population; may include HBV-exposed patients but HCV-focused (Grade B relevance) |
| [NCT01384383](https://clinicaltrials.gov/study/NCT01384383) | Phase 2 | Terminated | 248 | Response-guided GS-5885/GS-9451+peg-IFN regimen in genotype 1 HCV; population includes HCV/HBV coinfection, primary endpoint is HCV SVR (Grade C relevance) |
| [NCT02219685](https://clinicaltrials.gov/study/NCT02219685) | Phase 2 | Completed | 40 | LDV/SOF drug-interaction/neurocognition study in chronic HCV; not HBV-related (Grade C relevance) |

*Note: The remaining 13 trials retrieved for this candidate (e.g., NCT03823911, NCT02605304, NCT02421211) are HCV-only treatment or retreatment studies with no direct HBV therapeutic endpoint and have been excluded as low relevance.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | RCT (Phase 2) | Journal of Medical Virology | Only study directly testing LDV/SOF in HBV-monoinfected subjects; modest reduction in HBsAg/HBV DNA reported at Week 12 — key primary evidence for this indication |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort | Clinical Infectious Diseases | Taiwan HCV/HBV coinfection cohort treated with LDV/SOF; 108-week follow-up on HBV reactivation, not HBV cure |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | Journal of Clinical Gastroenterology | Examined HBV reactivation risk in HCV patients (previously/actively HBV-infected) treated with LDV/SOF for HCV |
| [27486112](https://pubmed.ncbi.nlm.nih.gov/27486112/) | 2016 | Cohort | Clinical Infectious Diseases | Taiwan/Korea LDV/SOF trial cohort (103/173 HBV pre-exposed); no evidence of HBV reactivation observed |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort/Observational | Journal of Viral Hepatitis | HBV reactivation risk in cancer patients receiving DAAs for HCV |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Pilot study | Antiviral Therapy | LDV/SOF for HCV suppression in HBV-coinfected patients; not an HBV efficacy endpoint |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Prospective study | Gastroenterology | Prospective assessment of HCV treatment efficacy and HBV reactivation risk/outcome in coinfected patients |
| [37254310](https://pubmed.ncbi.nlm.nih.gov/37254310/) | 2024 | In silico | Journal of Biomolecular Structure & Dynamics | Molecular docking study of antiviral compounds against HBx protein — mechanistic/computational only, does not include ledipasvir directly tested against HBV target |

---

## Germany Market Information

Ledipasvir is currently **not marketed in Germany** (market status: "未上市" / Not marketed), and no marketing authorizations were found in the available regulatory dataset. No product listings, dosage forms, or approved indication texts are on file for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: while no structured safety/warning/contraindication data was available in this evidence pack, the clinical evidence above surfaced an important safety-relevant signal: multiple studies describe HBV reactivation occurring in HBV/HCV-coinfected patients during Ledipasvir/Sofosbuvir treatment of HCV. This is a known class effect of DAA therapy and should be explicitly addressed once formal safety documentation is obtained — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using Ledipasvir against HBV is weak — Ledipasvir's target (HCV NS5A) has no known role in HBV replication, and the great majority of retrieved evidence reflects HBV *reactivation risk* during HCV treatment rather than antiviral efficacy against HBV. Only one small, uncontrolled Phase 2 pilot study directly supports an HBV efficacy signal, and its true target disease (HBV vs. HDV) requires verification. Combined with the drug's absence from the German market, current evidence does not support progression beyond a research question at this time.

**To proceed, the following is needed:**
- Confirm whether NCT03312023 / PMID 36045503 truly evaluated HBV monoinfection or HDV (given Ledipasvir/Sofosbuvir's established mechanistic plausibility for HDV) — this may redirect the repurposing hypothesis entirely
- Obtain TFDA/EMA package insert data (Data Gap DG001) to enable a formal S1 safety screen, particularly regarding HBV reactivation risk
- Obtain confirmed mechanism-of-action documentation from DrugBank (Data Gap DG002) to formally assess mechanistic plausibility
- If HBV monoinfection remains the target, a larger controlled trial with virologic cure endpoints (not just HBsAg decline) is needed before advancing past L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

