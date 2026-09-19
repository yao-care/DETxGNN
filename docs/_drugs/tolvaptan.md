---
layout: default
title: Tolvaptan
parent: Nur Modellvorhersage (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Tolvaptan: Von einer nicht dokumentierten ursprünglichen Indikation zur polyzystischen Nierenerkrankung (ADPKD)

## Zusammenfassung in einem Satz

> Das Evidenzpaket enthält nicht die ursprüngliche zugelassene Indikation von Tolvaptan (Arzneimittel nicht auf dem Markt in Deutschland, keine Lizenzeinträge; TFDA-Label-Daten als DG001 blockiert).
> Das Top-Ranking-Signal des TxGNN-Modells — **polyzystische Nierenerkrankung Typ 3, mit oder ohne polyzystische Lebererkrankung (ADPKD)** — wird durch **2 wegweisend abgeschlossene Phase-3-RCTs** und **20 Veröffentlichungen** unterstützt.
> Wichtig ist, dass das Modell selbst diese als **bereits etablierte, zugelassene Indikation von Tolvaptan** kennzeichnet (z. B. Jinarc/Samsca für ADPKD), anstelle einer neuen Umwidmungsentdeckung — dies ist ein Bestätigungssignal, keine neue Wissenschaft.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | In diesem Evidenzpaket nicht dokumentiert (Deutschland: nicht vermarktet, 0 Lizenzen) |
| Vorhergesagte neue Indikation | Autosomal-dominant vererbte polyzystische Nierenerkrankung (ADPKD), mit oder ohne polyzystische Lebererkrankung |
| TxGNN-Vorhersage-Score | 99.99% |
| Beweisstufe | L1 (≥2 abgeschlossene Phase-3-RCTs: TEMPO 3:4, REPRISE) |
| Marktatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Mit Schutzmaßnahmen fortfahren |

---

## Warum ist diese Vorhersage sinnvoll?

Derzeit ist das strukturierte Feld `original_moa` eine Datenlücke (DG002). Die Umwidmungsbegründung des Modells selbst liefert jedoch funktionsmechanistische Details: Tolvaptan ist ein **selektiver Vasopressin-V2-Rezeptor-Antagonist**. Durch Blockade von V2-Rezeptoren im renalen Sammelrohr unterdrückt es die cAMP-Generierung — den Schlüssel-Botenstoff, der die Zystenepithelproliferation und Flüssigkeitssekretion in ADPKD antreibt.

Entscheidend ist, dass dies **keine explorative Umwidmungshypothese** ist. Die Begründung besagt ausdrücklich, dass dies „eine bereits etablierte, mechanistisch gut definierte zugelassene Indikation" ist — Tolvaptan (als Jinarc/Samsca) ist bereits in mehreren Märkten (Japan, USA, EU) zur Verlangsamung der ADPKD-Progression zugelassen, basierend auf den in diesem Evidenzpaket angeführten Studien TEMPO 3:4 und REPRISE. Das TxGNN-Signal hier sollte als **Validierung bekannter Pharmakologie** gelesen werden, nicht als Entdeckung einer neuen Anwendung.

Da Deutschland „Nicht vermarktet" (nicht auf dem Markt) mit null Lizenzen anzeigt, deutet dieses Evidenzpaket darauf hin, dass der deutsche Markt entweder über keine aktuelle Tolvaptan-/ADPKD-Zulassung in den Unterlagen verfügt, oder der Eintrag einfach nicht erfasst wurde — dies erfordert behördliche Verifizierung (siehe Nächste Schritte) statt als echter behördlicher Mangel behandelt zu werden.

---

## Evidenz klinischer Studien

Derzeit gibt es keine verwandten klinischen Studien, die im strukturierten Feld `clinical_trials` für diese Indikation registriert sind (Daten pivotaler Studien werden stattdessen als Literatur erfasst — siehe unten).

---

## Literaturevidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | NEJM | TEMPO 3:4 — Tolvaptan verlangsamt das Wachstum des Gesamtniervolumens und den eGFR-Rückgang bei früher ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | NEJM | REPRISE — bestätigt Wirksamkeit/Sicherheit von Tolvaptan in später ADPKD |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT | Pediatr Nephrol | Randomisierte Studie (NCT02964273) zur Sicherheit/Pharmakodynamik von Tolvaptan bei pädiatrischer ADPKD (5–17y) |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematische Übersicht/Metaanalyse | Nefrología | Bestätigt Gesamtwirksamkeit und Sicherheitsprofil von Tolvaptan in ADPKD über Studien hinweg |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Übersicht/Konsens | NDT | ERA-Arbeitsgruppe-Konsens zum Zeitpunkt und zur Art der Tolvaptan-Einleitung bei ADPKD |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Übersicht | Clinics in Liver Disease | Tolvaptan verlangsamt renale Verschlechterung und Zystenwachstum in ADPKD/PCLD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematische Übersicht (Cochrane) | Cochrane Database Syst Rev | Übersicht über krankheitsmodifizierende Interventionen, einschließlich Tolvaptan, zur ADPKD-Progression |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Übersicht | JAMA | Zeitgenössischer Überblick über ADPKD-Epidemiologie und -Management |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Übersicht | Int J Mol Sci | ADPKD-Zystenogenese-Pathophysiologie und Behandlungsfortschritte |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Übersicht | Curr Opin Nephrol Hypertens | Neue ADPKD-Therapien jenseits von Tolvaptan, Positionierung von Tolvaptan als aktueller Behandlungsstandard |

---

## Marktinformationen Deutschland

In diesem Evidenzpaket sind keine Zulassungseinträge vorhanden (`taiwan_regulatory.market_status` = Nicht vermarktet, `total_licenses` = 0). Dies sollte unabhängig überprüft werden — Tolvaptan (Jinarc®) verfügt über eine EU-weit zentralisierte Zulassung für ADPKD, daher deutet das Fehlen hier wahrscheinlich auf eine Datenlücke hin anstatt auf eine echte Nicht-Verfügbarkeit in Deutschland.

---

## Weitere von TxGNN vorhergesagte Indikationen (nicht priorisiert)

Die Ränge 2–10 erreichten ähnlich hohe Werte (>99.9%), aber die Begründung des Modells selbst kennzeichnet die meisten als wahrscheinlich Embedding-Ähnlichkeits-Rauschen ohne mechanistische oder evidentielle Unterstützung:

| Rang | Krankheit | Beweisstufe | Empfehlung | Anmerkung |
|------|-----------|------|----------|------|
| 5 | Joubert-Syndrom mit Nierenfehler | L4 | Forschungsfrage | Gemeinsame Ziliopathie-/cAMP-Biologie mit ADPKD, aber keine direkte Tolvaptan-Evidenz |
| 4 | Thorakale Missbildung | L4 | Abwarten | Nur indirekte Fallberichte (Tolvaptan bei Flüssigkeitsüberbelastung, nicht Strukturdefekt) |
| 2, 3, 6, 7, 8, 10 | Verschiedene angeborene/strukturelle Syndrome | L5 | Abwarten | Keine Literatur- oder Studienunterstützung; wahrscheinlich Modellrauschen |
| 9 | Missbildungssyndrom mit parodontaler Komponente | L5 | Abwarten | Abgerufene Literatur ist nicht verwandte Parodontitis-Forschung; falscher Match |

Dies sind nicht umsetzbar und werden nur der Vollständigkeit halber aufgeführt.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Alle strukturierten Sicherheitsfelder (`key_warnings`, `contraindications`, `ddi`) sind Datenlücken in diesem Evidenzpaket (DG001, Blockiert).

Ein Punkt aus der Umwidmungsbegründung verdient Beachtung in Erwartung vollständiger Fachinformations-Daten: Hepatotoxizitätsüberwachung wird ausdrücklich als bekanntes Anliegen bei der Verwendung von Tolvaptan in ADPKD angeführt (konsistent mit der Kasten-Hepatotoxizitätswarnung, die mit dieser Arzneimittelklasse in anderen Märkten verbunden ist).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Mit Schutzmaßnahmen fortfahren**

**Begründung:**
Das ADPKD-Signal wird durch L1-Evidenz (zwei abgeschlossene Phase-3-RCTs — TEMPO 3:4 und REPRISE) unterstützt und stellt eine bereits etablierte Anwendung von Tolvaptan dar, anstelle einer spekulativen Umwidmung. Diesem Evidenzpaket fehlen jedoch TFDA-/Fachinformations-Sicherheitsdaten (DG001, Blockiert) und strukturierte MOA-Daten (DG002), und es zeigt keine deutsche Zulassung in den Unterlagen — all dies muss gelöst werden, bevor regulatorische oder klinische Maßnahmen ergriffen werden.

**Die folgenden Punkte sind zum Fortfahren erforderlich:**
- Abrufen der offiziellen TFDA-/deutschen (BfArM) Fachinformation PDF für Hepatotoxizitätswarnungen, Kontraindikationen und DDI-Daten (löst DG001)
- Bestätigung der strukturierten MOA über DrugBank-API-Abfrage (löst DG002)
- Unabhängige Überprüfung des aktuellen EU-/deutschen Zulassungsstatus für Tolvaptan/Jinarc, angesichts der Diskrepanz zwischen „Nicht vermarktet" hier und bekannter EU-weiter ADPKD-Zulassung
- Klärung mit Interessenträgern, dass dieser Kandidat ein Bestätigungssignal für eine bereits bestehende zugelassene Anwendung ist, nicht eine echte neue Umwidmungsmöglichkeit — dies beeinflusst, wie er intern positioniert werden sollte

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

