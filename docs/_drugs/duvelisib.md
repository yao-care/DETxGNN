---
layout: default
title: Duvelisib
parent: Mittlere Evidenz (L3-L4)
nav_order: 133
evidence_level: L4
indication_count: 10
---

# Duvelisib
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **10** 
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

# Duvelisib: Ein PI3K-δ,γ-Dualinhibitor — TxGNN-vorhergesagte Verbindung zum Hodgkin-Lymphom

## Zusammenfassung in einem Satz

Duvelisib ist ein oraler PI3K-δ,γ-Dualinhibitor; diese Evidenzbewertung enthält keine ursprüngliche zugelassene Indikation für diesen Markt (das Arzneimittel ist derzeit hier nicht auf dem Markt). TxGNNs am höchsten eingestufter Vorhersage ist **Hodgkin-Lymphom**, jedoch betreffen alle **11 klinischen Studien** und **16 Publikationen**, die als unterstützende Evidenz herangezogen wurden, ausschließlich nicht-Hodgkin-Lymphom-Subtypen (CLL/SLL, follikuläres Lymphom, Mantelzell-Lymphom, peripheres T-Zell-Lymphom) — keine untersucht direkt klassisches Hodgkin-Lymphom, daher liegt das Evidenzniveau für dieses spezifische Label nur bei **L4** mit einer **Abwarten**-Empfehlung.

---

## Kurzübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in diesem Datensatz verzeichnet — duvelisib ist derzeit nicht in dieser Gerichtsbarkeit zugelassen und kein zugelassener Indikationstext ist verfügbar |
| Vorhergesagte neue Indikation | Hodgkin-Lymphom |
| TxGNN-Vorhersage-Score | 99.94% |
| Evidenzniveau | L4 |
| Marktstatus in Deutschland | ✗ Nicht auf dem Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwarten |

---

## Warum ist diese Vorhersage angemessen?

Das offizielle Wirkmechanismus-Feld für Duvelisib ist eine Datenlücke in dieser Evidenzbewertung. Die Literatur, die als unterstützende Evidenz herangezogen wurde, beschreibt Duvelisib jedoch konsistent und unabhängig als **oralen Dualinhibitor der Phosphoinositid-3-Kinase δ und γ (PI3K-δ,γ)**, das stromabwärts des B-Zell-Rezeptor-Signalwegs wirkt, um die Proliferation und das Überleben maligner B-Zellen zu unterdrücken, während die PI3K-γ-Inhibition zusätzlich die Tumor-Mikroumgebung moduliert (Makrophagen/T-Zellen).

Die automatisierte Relevanzprüfung, die in diese Bewertung eingebettet ist, zeigt eine erhebliche Nichtübereinstimmung für diese Vorhersage mit Rang 1: **keine der 11 klinischen Studien oder 16 Publikationen**, die unter dem Label "Hodgkin-Lymphom" abgerufen wurden, haben tatsächlich klassisches Hodgkin-Lymphom (Reed-Sternberg-Zellbiologie) eingeschlossen oder untersucht. Jede Studie und jedes Papier betrifft stattdessen nicht-Hodgkin-Lymphom-Subtypen — CLL/SLL, follikuläres Lymphom, Mantelzell-Lymphom, peripheres/kutanes T-Zell-Lymphom — wo der Wirkmechanismus von Duvelisib gut etabliert ist. Dies deutet stark darauf hin, dass der TxGNN-Score "Hodgkin-Lymphom" ein Embedding-Ähnlichkeits-Artefakt zwischen Lymphom-Krankheitslabeln im Wissensgraph widerspiegelt, statt eines echten, spezifischen mechanistischen Signals für klassisches HL.

**Wichtiger Kontext:** dieselbe Evidenzbewertung enthält ein viel stärkeres, anders bezeichnetes Signal — "B-Zell-Neoplasma" (Rang 9) — verankert durch eine abgeschlossene pivotale Phase-3-Studie (DUO, NCT02004522, n=319, Duvelisib vs. Ofatumumab in rezidiviertem/refraktärem CLL/SLL) und bewertet L1/S3/"Mit Sicherheitsvorkehrungen fortfahren". Die Anmerkung der Bewertung für diesen Eintrag warnt jedoch davor, dass dies weitgehend duvelisibs **bereits etabliertem** therapeutischem Umfang (CLL/SLL/FL) entspricht, statt eines echten Umpositionierungssignals, und empfiehlt, die Datenlücken auf Wirkstoffebene (ursprüngliche Indikation, MOA) zu beheben, bevor dieses Programm als "Umpositionierung" versus "Bestätigung der primären Indikation" bewertet wird.

---

## Evidenz aus klinischen Studien

*Keine der folgenden Studien untersucht klassisches Hodgkin-Lymphom spezifisch; alle betreffen nicht-Hodgkin-Lymphom-Malignome, die unter dem Label "Hodgkin-Lymphom" abgerufen wurden.*

| Studiennummer | Phase | Status | Einschluss | Hauptergebnisse |
|---------|------|------|------|---------|
| [NCT02576275](https://clinicaltrials.gov/study/NCT02576275) | Phase 3 | Zurückgezogen | 0 | Duvelisib+Bendamustin/Rituximab vs. Placebo in vorbehandeltem indolentem NHL — zurückgezogen, keine Daten |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Ausgesetzt | 170 | Duvelisib-CHOEP vs. Standardregimen in unbehandeltem CD30-negativem peripherem T-Zell-Lymphom |
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unbekannt | 140 | PI3K-Klasse-Wirkstoff (YY-20394) Monotherapie in rezidiviertem/refraktärem follikulärem NHL |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Abgeschlossen | 129 | Duvelisib-Monotherapie in Rituximab/Chemo-refraktärem indolentem NHL (FL, Marginalzone, SLL) |
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Abgeschlossen | 103 | Intermittiertes vs. kontinuierliches Duvelisib-Dosierungsschema in indolentem NHL |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Abgeschlossen | 48 | Duvelisib + Rituximab oder Bendamustin/Rituximab in NHL/CLL |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Aktiv, nicht rekrutierend | 42 | Duvelisib nach CAR-T-Zell-Therapie, um CAR-T-Persistenz durch PI3K-Inhibition zu verbessern |
| [NCT02640833](https://clinicaltrials.gov/study/NCT02640833) | Phase 1 | Zurückgezogen | 0 | Duvelisib + Venetoclax in R/R CLL/SLL/NHL — zurückgezogen |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Zurückgezogen | 0 | Duvelisib + Acalabrutinib in R/R indolentem NHL — zurückgezogen |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Abgeschlossen | 14 | Duvelisib + BMS-986345 Kombination in lymphoider Malignität, Dosisfindung |

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Fachzeitschrift | Hauptergebnisse |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematische Übersicht/Metaanalyse | Frontiers in Immunology | Sicherheits-/Wirksamkeitsmeta-analyse von Duvelisib in verschiedenen rezidiv./refraktären lymphoiden Neoplasien |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Übersicht | The Lancet Oncology | Überblick über Duvelisib in indolentem nicht-Hodgkin-Lymphom |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase-1-Studie | Blood | Grundlegende Phase-1-Studie zur Festlegung der MTD (75 mg BID) und Aktivität von Duvelisib in fortgeschrittenen hämatologischen Malignomen |
| [31490009](https://pubmed.ncbi.nlm.nih.gov/31490009/) | 2019 | Kohorte/Phase 1 | American Journal of Hematology | Duvelisib + Rituximab oder Bendamustin/Rituximab in NHL/CLL |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Übersicht | Current Treatment Options in Oncology | PI3K-Inhibitoren, einschließlich Duvelisib, als Zieltherapie in Lymphomen |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Übersicht | Drugs | Neue therapeutische Ansätze, einschließlich Duvelisib, im follikulären Lymphom |
| [27872741](https://pubmed.ncbi.nlm.nih.gov/27872741/) | 2016 | Übersicht | Mediterranean Journal of Hematology and Infectious Diseases | Neue Arzneimittel, einschließlich Duvelisib, im follikulären Lymphom |
| [32658557](https://pubmed.ncbi.nlm.nih.gov/32658557/) | 2020 | Übersicht | Future Oncology | PI3K-Inhibitor-Klassenübersicht in der Behandlungslandschaft nicht-Hodgkin-Lymphom |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Übersicht | American Journal of Health-System Pharmacy | Zusammenfassung regulatorisch zugelassener gezielter Therapien für B- und T-Zell-Lymphome |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Präklinisch | Scientific Reports | PI3Kγ/δ-Rollen in Mantelzell-Lymphom-Proliferation/Migration und Duvelisib-Wirksamkeit |

---

## Informationen zum deutschen Markt

Duvelisib ist derzeit **nicht in Deutschland auf dem Markt** — es existieren keine BfArM-Zulassungsdatensätze in dieser Evidenzbewertung (0 Lizenzen in der Akte).

---

## Zytotoxizität

Duvelisib ist ein antineoplastisches Arzneimittel (oraler niedermolekularer Kinase-Inhibitor, entwickelt für hämatologische Malignomen).

| Element | Inhalt |
|---------|---------|
| Zytotoxizitätsklassifizierung | Zielgerichtete Therapie (PI3K-δ,γ-Dualinhibitor) — basierend auf konsistenter Beschreibung in der abgerufenen Literatur; formale DrugBank-Kategoriedaten nicht in dieser Evidenzbewertung verfügbar |
| Myelosuppressionsrisiko | Bitte beachten Sie die Gebrauchsinformationen zu Warnhinweisen und Vorsichtsmaßnahmen |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Gebrauchsinformationen zu Warnhinweisen und Vorsichtsmaßnahmen |
| Überwachungselemente | Bitte beachten Sie die Gebrauchsinformationen zu Warnhinweisen und Vorsichtsmaßnahmen |
| Schutzmaßnahmen bei der Handhabung | Bitte beachten Sie die Gebrauchsinformationen zu Warnhinweisen und Vorsichtsmaßnahmen |

---

## Sicherheitserwägungen

Bitte beachten Sie die Gebrauchsinformationen für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Die Vorhersage mit Rang 1 (Hodgkin-Lymphom) wird nicht durch relevante Evidenz gestützt — jede abgerufene klinische Studie und Publikation betrifft nicht-Hodgkin-Lymphom, was auf ein wahrscheinliches Embedding-Ähnlichkeits-Artefakt zwischen Lymphom-Krankheitslabeln im Wissensgraph hindeutet, statt auf ein echtes Umpositionierungssignal für klassisches HL. Parallel verhindern die Datenlücken auf Wirkstoffebene dieses Kandidaten (fehlende BfArM-Etikettwarnungen/Kontraindikationen — Blockiert; fehlende MOA — Hoch), dass er die S1-Sicherheitsvorprüfungs-Phase unabhängig von der Indikation besteht.

**Um fortfahren zu können, ist Folgendes erforderlich:**
- Beheben Sie DG001: Besorgen Sie sich BfArM-/Produktetikett-Warnungen und Kontraindikationen
- Beheben Sie DG002: Besorgen Sie sich bestätigte MOA von DrugBank
- Etablieren und dokumentieren Sie duvelisibs ursprüngliche/zugelassene Indikation(en), derzeit nicht in diesem Datensatz verzeichnet
- Spezifische Krankheitslabel-Neubewertung der Evidenz, um die Relevanz für klassisches Hodgkin-Lymphom zu bestätigen oder auszuschließen, bevor dieser spezifische Kandidat vorangetrieben wird
- Wenn Sie zum stärkeren Signal "B-Zell-Neoplasma" (Rang 9, L1/S3) umleiten, klären Sie zunächst, ob dies echtes Umpositionierungspotenzial oder Überschneidung mit duvelisibs bereits etabliertem Indikationsumfang widerspiegelt, und führen Sie eine Neuprüfung angrenzender CLL/SLL-Subtyp-Einträge mit niedriger Evidenz (Ränge 5–6) durch, um das gleiche Embedding-Artefakt-Muster zu suchen, das bei Rang 1 zu sehen ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

