---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

Using the report template as specified — no additional skill needed for this structured drafting task.

# Mycophenolate Mofetil: From Transplant Rejection Prophylaxis to HIV Infectious Disease

## One-Sentence Summary

> Mycophenolate mofetil (MMF) is an inosine monophosphate dehydrogenase (IMPDH) inhibitor established as an immunosuppressant for preventing organ transplant rejection.
> The TxGNN model predicts it may be effective against **HIV infectious disease**,
> with **10 clinical trials** and **20 publications** currently supporting this direction — though several trials ended in WITHDRAWN, UNKNOWN, or TERMINATED status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of organ transplant rejection (well-established clinical use; not captured in this evidence pack, as no license/indication records were returned) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Germany Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query pending). Based on known pharmacology, mycophenolate mofetil is metabolized to mycophenolic acid, an IMPDH inhibitor that blocks the de novo purine (guanosine) synthesis pathway required for lymphocyte proliferation. Its efficacy in preventing transplant rejection is well established.

Mechanistically, IMPDH inhibition also depletes intracellular deoxyguanosine triphosphate (dGTP) pools in activated T cells — the same nucleotide pool HIV reverse transcriptase depends on. This provides a biochemical rationale for using MMF as an adjunct to NRTIs (e.g., abacavir, didanosine), where MPA has been shown in vitro to potentiate antiretroviral activity. However, this is a double-edged mechanism: the same immunosuppressive property that prevents transplant rejection could further weaken immune function in an already immunocompromised HIV population, which is reflected in the mixed and often inconclusive clinical trial record below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn (n=0) | 0 | Designed to test MMF safety/tolerability + antiretroviral activity added to abacavir in treatment-experienced HIV patients; no data generated |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | Substudy of MAN2; evaluated MMF's effect on cardiovascular surrogate markers in HIV-1 patients; results unpublished |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study — MMF in ART-naive chronic HIV-1 patients, assessing CD4+ decline, plasma HIV-1 RNA, and safety; results unpublished |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | Completed | 56 | Randomized, double-blind, placebo-controlled: DAPD (amdoxovir) vs DAPD+MMF in treatment-experienced subjects |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Renal transplant follow-up in HIV-1 patients under raltegravir-based regimen; MMF used as standard anti-rejection agent, not to treat HIV |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Feasibility/safety of renal transplantation (with MMF as immunosuppressant) in HIV-infected patients with ESRD |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT with fludarabine/TBI conditioning plus cyclosporine+MMF for mixed chimerism induction in HIV-1 patients |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide, sirolimus, MMF for GVHD prophylaxis (hematologic malignancies, not HIV-specific) |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Thiotepa/busulfan/fludarabine conditioning for haplo-HSCT in high-risk AML; MMF as part of GVHD prophylaxis, unrelated to HIV indication |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine+MMF vs cyclophosphamide+prednisolone for anti-EPO PRCA; not an HIV trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF vs continued HAART during structured treatment interruption; assessed immune response and viral load in lymphatic tissue |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Comparative study | AIDS | HAART with vs without MMF in treatment-naive HIV-1 patients; examined effect on plasma HIV-1 RNA decay and latent reservoir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects observed when combining MMF with HAART in treatment-naive acute/chronic HIV-1 patients |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort | J Acquir Immune Defic Syndr | Adding MMF to abacavir-containing ART depleted intracellular dGTP and reduced plasma HIV-1 RNA in 5 patients |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD study | Clin Pharmacokinet | Pharmacokinetics/pharmacodynamics of low-dose MMF combined with abacavir, efavirenz, nelfinavir in HIV patients |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK/PD study | Clin Pharmacokinet | Effect of MMF on pharmacokinetics of antiretroviral drugs and intracellular nucleoside triphosphate pools |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | Open-label pilot in 7 multidrug-resistant AIDS patients: MMF + abacavir/ddI/amprenavir/ritonavir; well tolerated, no significant HIV RNA decline reported |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Reviews immunosuppressive drugs (including MMF) as adjuncts targeting chronic immune activation in HIV disease progression |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Comparative study | AIDS | Safety, tolerability, and antiretroviral activity of amdoxovir (DAPD) with or without MMF in drug-resistant HIV infection |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | Discusses "virostatics" (including MMF) as a strategy to target residual HIV replication in cellular reservoirs alongside HAART |

---

## Germany Market Information

Mycophenolate mofetil is currently **not marketed** in Germany under this evidence pack's data source (0 authorizations, no license records available). No German product-level dosage form or approved indication text could be extracted.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L2, but the strongest directly-relevant trials for MMF-in-HIV are either withdrawn (0 enrolled), of unknown/unpublished outcome (MAN2, cardiovascular substudy), or small pilot studies without confirmed efficacy — no trial demonstrates a clear positive antiviral benefit. Combined with a **Blocking** data gap on TFDA/BfArM warnings and contraindications (required for any S1 safety evaluation) and a High-severity gap on mechanism of action, this candidate cannot yet advance past the research-question stage.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse official package insert warnings/contraindications before any safety-stage review
- Resolve DG002 (High): confirm MOA via DrugBank API to support mechanistic-link analysis
- Follow up on unpublished/unknown-status trials (NCT00247494, NCT00120419) to determine whether results exist
- Formal DDI assessment against antiretroviral regimens (abacavir, NRTIs), given PK interaction signals in the literature (PMID 15355127, 15871638)
- Explicit risk-benefit assessment of adding an immunosuppressant in an immunocompromised HIV population before any further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

