---
layout: default
title: Imatinib
parent: Hohe Evidenz (L1-L2)
nav_order: 197
evidence_level: L2
indication_count: 10
---

# Imatinib
{: .fs-9 }

Evidenzniveau: **L2** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Imatinib: Von der chronischen myeloischen Leukämie/GIST zum fibroblastischen Neoplasma (Dermatofibrosarcoma protuberans)

## Zusammenfassung in einem Satz

Imatinib ist ein BCR-ABL/KIT/PDGFR-Tyrosinkinase-Inhibitor, der ursprünglich für die chronische myeloische Leukämie (CML) und gastrointestinale Stromatumoren (GIST) entwickelt wurde; detaillierte Originalindikationstexte und MOA-Dokumentationen sind in diesem Evidence Pack nicht vorhanden (siehe Data Gaps DG001/DG002). Unter 10 von TxGNN vorhergesagten Indikationen, die für dieses Medikament gescreent wurden, hat das **fibroblastische Neoplasma** — das klinisch dem **Dermatofibrosarcoma protuberans (DFSP)** entspricht — bei weitem die stärkste Unterstützung mit **1 abgeschlossener Phase-2-Studie** und **20 zugehörigen Publikationen**, einschließlich einer 2025 europäischen interdisziplinären Behandlungsleitlinie. Beachten Sie, dass der einzelne höchste TxGNN-Score in diesem Pack („Herz-Fibrosarkom") fast keine unterstützenden Beweise hat und als Hold flagged wird; er wird separat unten diskutiert.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Originalindikation | Nicht verfügbar in diesem Evidence Pack (drug.original_indications ist leer; regulatorischer Lizenztext nicht verfügbar — DG001) |
| Vorhergesagte neue Indikation | Fibroblastisches Neoplasma (entspricht klinisch Dermatofibrosarcoma protuberans, DFSP) |
| TxGNN-Vorhersage-Score | 99.94% (Rang 1108 unter allen TxGNN-Kandidaten-Erkrankungen; Rang 2 von 10 in diesem Evidence Pack) |
| Beweisebene | L2 |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Mit Guardrails fortfahren |

---

## Warum ist diese Vorhersage berechtigt?

Derzeit sind detaillierte Wirkmechanismus-Daten für Imatinib in diesem Evidence Pack nicht verfügbar (Data Gap DG002). Basierend auf bekannter Pharmakologie ist Imatinib ein Kleinmolekül-Inhibitor der BCR-ABL-, KIT- und PDGFR-Tyrosinkinasen, und seine Wirksamkeit bei CML und GIST ist gut etabliert.

Für die Vorhersage des „fibroblastischen Neoplasmas" ist die mechanistische Begründung des Evidence Packs klar und spezifisch: Diese Krankheitskategorie entspricht wesentlich dem **DFSP**, das eine charakteristische **t(17;22)(q22;q13) COL1A1–PDGFB-Translokation** trägt, die zur konstitutiven PDGFRB-Aktivierung führt. Dies ist ein Schulbuch-Molekularziel für Imatinib, und der Wirkmechanismus-zu-Indikations-Link ist direkt und nicht abgeleitet — DFSP mit fibrosarkomatöser Transformation wurde tatsächlich bereits in der klinischen Praxis mit Imatinib behandelt.

Im Gegensatz dazu hat der Top-Kandidat nach reinem TxGNN-Score allein, „Herz-Fibrosarkom", nur einen einzelnen Arzneimittel-Kommentar von 2008 als Unterstützung, dessen Titel explizit angibt, dass die Beweise „nicht robust" sind. Dies veranschaulicht, warum TxGNN-Score-Rang und Beweiskraft separat bewertet werden müssen — siehe die vollständige Kandidaten-Screening-Tabelle am Ende dieses Berichts.

---

## Klinische Studien

| Versuchsnummer | Phase | Status | Rekrutierung | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Abgeschlossen | 17 | Imatinib bei lokal fortgeschrittenem/metastatischem DFSP und Riesenzell-Fibroblastom mit COL1A1/PDGFB-Fusion; Studie rekrutierte direkt molekular bestätigte Patienten (Evidence Grade A). |

---

## Literaturbeweise

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Übersicht/Leitlinie | Eur J Cancer | Europäische interdisziplinäre (EADO/EDF/UEMS/EADV) aktualisierte Leitlinie zur DFSP-Diagnose und -Behandlung. |
| [41236573](https://pubmed.ncbi.nlm.nih.gov/41236573/) | 2025 | Präklinisch | Human Cell | Etablierung einer imatinib-resistenten DFSP-Zelllinie (DFSP-DPH1) für Resistenzforschung. |
| [37610680](https://pubmed.ncbi.nlm.nih.gov/37610680/) | 2023 | Präklinisch | Human Cell | Multi-omische Profilierung und ex-vivo-Modellierung von imatinib-resistentem DFSP mit fibrosarkomatöser Transformation. |
| [36630365](https://pubmed.ncbi.nlm.nih.gov/36630365/) | 2023 | Übersicht | Clin Exp Dermatol | Übersicht der klinischen Merkmale von DFSP, Histologie und PDGFB-COL1A1-Fusion (>90% der Fälle). |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Übersicht | J Surg Oncol | Chirurgische Behandlung von DFSP; vermerkt Imatinib-Einsatz bei fortgeschrittener/nicht resezierbarer Erkrankung. |
| [33993132](https://pubmed.ncbi.nlm.nih.gov/33993132/) | 2021 | Übersicht | Curr Opin Otolaryngol Head Neck Surg | Diagnose, Arbeitsablauf und Behandlungsstrategien für DFSP. |
| [30297237](https://pubmed.ncbi.nlm.nih.gov/30297237/) | 2018 | Übersicht | Bull Cancer | DFSP-Management; identifiziert t(17;22)(q22;q13) COL1A1/PDGFB als spezifisches diagnostisches Merkmal. |
| [31466588](https://pubmed.ncbi.nlm.nih.gov/31466588/) | 2019 | Übersicht | Dermatol Clin | DFSP-klinische/histologische Charakterisierung; Strahlentherapie und systemische Therapie in nicht resezierbaren Fällen. |
| [28795284](https://pubmed.ncbi.nlm.nih.gov/28795284/) | 2017 | Übersicht | Curr Treat Options Oncol | Multidisziplinärer Behandlungsansatz für DFSP. |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Übersicht | Expert Rev Anticancer Ther | Aktuelle Behandlungsmöglichkeiten für DFSP; PDGF-autokrin/parakrin Mechanismus. |

---

## Marktinformationen in Deutschland

Imatinib ist derzeit **nicht vermarktet** in dieser Gerichtsbarkeit (`market_status: Not marketed`), und es sind keine Produktgenehmigungsdatensätze in diesem Evidence Pack vorhanden (`total_licenses: 0`). Regulatorische Zulassung und Produktlistungsdaten müssen separat bezogen werden, falls eine Umwidmung verfolgt wird.

---

## Zytotoxizität

Die ursprünglichen Indikationen von Imatinib (CML, Ph+ ALL, GIST) ordnen es in die Kategorie der Antineoplastika ein, obwohl es als gezielte Therapie eher als ein konventionelles Zytotoxikum wirkt.

| Element | Inhalt |
|------|------|
| Zytotoxizitäts-Klassifizierung | Gezielte Therapie (BCR-ABL/KIT/PDGFR-Tyrosinkinase-Inhibitor) — basierend auf bekannter Wirkstoffklasse; nicht abgeleitet von Toxizitätsdaten des Evidence Packs |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Fachinformation |
| Emetogenitäts-Klassifizierung | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Fachinformation |
| Überwachungselemente | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Fachinformation |
| Handhabungsschutz | Bitte beachten Sie die Warnungen und Vorsichtsmaßnahmen in der Fachinformation |

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Keine Schlüsselwarnungen, Kontraindikationen oder Arzneimittel-Wechselwirkungsdaten waren in diesem Evidence Pack verfügbar (flagged as Data Gap DG001, severity: Blocking, currently preventing S1 safety evaluation).

---

## Vollständige Übersicht aller vorhergesagten Indikationen

Zur Vollständigkeit sind alle 10 TxGNN-Kandidaten in diesem Evidence Pack unten nach Beweisqualität statt nach reinem Score eingestuft, da sich die beiden häufig unterscheiden:

| Rang (nach Score) | Krankheit | TxGNN-Score | Beweisebene | Entscheidungsphase | Empfehlung | Hinweis |
|---|---|---|---|---|---|---|
| 2 | Fibroblastisches Neoplasma (≈DFSP) | 99.94% | L2 | S3 | Mit Guardrails fortfahren | Stärkstes Signal; PDGFB-Fusion, direkte Phase-2-Studie |
| 3 | Konventionelles Fibrosarkom | 99.93% | L2 | S2 | Mit Guardrails fortfahren | Beweise überlappen sich weitgehend mit DFSP; echtes „konventionelles" Fibrosarkom entbehrt Daten zu PDGFR/KIT-Treiber — erfordert molekulare Subtypisierung vor der Anwendung |
| 6 | Liposarkom | 99.88% | L2 | S2 | Forschungsfrage | Gemischte Phase-2-Beweise; unkontrollierte Populationen zeigen begrenzte Reaktion; erfordert PDGFR/KIT-angereicherte Untergruppe |
| 1 | Herz-Fibrosarkom | 99.94% | L4 | S0 | Hold | Höchster roher Score, aber nur 1 nicht-robuster Kommentar von 2008 |
| 4 | Nieren-Fibrosarkom | 99.93% | L4 | S1 | Forschungsfrage | Nur Basket-Studie; Literaturübereinstimmung scheint ein Keyword-Mismatch zu sein (FSGS, nicht verwandte Nierenerkrankung) |
| 5 | Niedriggradiges fibromyxoides Sarkom | 99.93% | L5 | S0 | Hold | Falsches Treiber-Gen (FUS-CREB3L2); Literatur ist eine nicht verwandte Fallserie |
| 7 | Leber-Fibrosarkom | 99.86% | L5 | S0 | Hold | Keine Studien oder Literatur überhaupt |
| 8 | Mittelmeerfieber (familiär) | 99.86% | L5 | S0 | Hold | Kein plausible mechanistische Verbindung; wahrscheinlich falsch positiv im Wissensgraph |
| 9 | Myxoides Ovarial-Liposarkom | 99.85% | L5 | S0 | Hold | Keine unterstützenden Daten |
| 10 | Familiärer Rhabdoid-Tumor | 99.83% | L5 | S0 | Hold | Getrieben durch SMARCB1-Verlust, nicht verwandt mit Kinase-Inhibition |

---

## Fazit und nächste Schritte

**Entscheidung: Mit Guardrails fortfahren**

**Begründung:**
Das einzige gut unterstützte Signal in diesem Evidence Pack ist fibroblastisches Neoplasma/DFSP, gestützt durch eine abgeschlossene Phase-2-Studie mit einer molekular definierten Population (COL1A1-PDGFB-Fusion) und eine klinische Leitlinie von 2025. Alle anderen 9 Kandidaten sind entweder schwach unterstützt (L4) oder im Wesentlichen ununterstützte Modell-Artefakte (L5) und sollten in Abwartung stärkerer Beweise ausgesetzt werden.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA/regulatorische Labellingdaten (Warnungen, Kontraindikationen) — derzeit eine **Blocking**-Lücke (DG001), die die anfängliche Sicherheitsprüfung (S1) verhindert
- Formale MOA-Dokumentation von DrugBank (DG002)
- Molekulares Bestätigungsprotokoll (COL1A1-PDGFB-Test) zur Definition der Zielunterpopulation für fibroblastische Neoplasma-/konventionelle Fibrosarkom-Indikationen
- Für Liposarkom: PDGFR/KIT-Expressions-basierte Patientenbereichs-Strategie vor weiterer Evaluierung
- Bewertung des regulatorischen Pfads, da das Medikament derzeit nicht auf diesem Markt vermarktet wird (0 Genehmigungen)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

