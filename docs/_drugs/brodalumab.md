---
layout: default
title: Brodalumab
parent: Nur Modellvorhersage (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab (DB11776): Repurposing-Evaluierung — Keine TxGNN-Vorhersagen verfügbar

## Zusammenfassung in einem Satz

Brodalumab ist ein vollständig humaner monoklonaler Antikörper, der gegen den Interleukin-17-Rezeptor A (IL-17RA) wirkt und in den USA und der EU zur Behandlung mittelschwerer bis schwerer Plaque-Psoriasis zugelassen ist (Handelsnamen: Siliq®, Kyntheum®).
Das aktuelle Evidence Pack enthält **keine durch TxGNN vorhergesagten neuen Indikationen** für diese Verbindung, und mehrere kritische Datenfelder – einschließlich des Wirkmechanismus, der Warnhinweise in der Packungsbeilage und der Kontraindikationen – fehlen.
Eine vollständige Repurposing-Evaluierung **kann nicht abgeschlossen werden**, bis diese Datenlücken behoben sind.

---

## Schnellübersicht

| Eintrag | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Plaque-Psoriasis (aus Domänenwissen; nicht im Evidence Pack erfasst) |
| Vorhergesagte neue Indikation | Keine Vorhersagen generiert |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | N/A — TxGNN-Pipeline noch nicht ausgeführt |
| Taiwan-Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Informationen zum Taiwan-Markt

Brodalumab hat derzeit **keine registrierten Produktzulassungen in Taiwan** (TFDA). Keine genehmigten Arzneimittel, Darreichungsformen oder Indikationstexte sind bis zum Datenstichtag dieses Berichts (2026-04-20) dokumentiert.

Zur Referenz ist das Arzneimittel in anderen Rechtsgebieten zugelassen:

| Region | Handelsname | Inhaber | Genehmigte Indikation |
|--------|------------|---------|---------------------|
| Vereinigte Staaten | Siliq® | AstraZeneca / Bausch Health | Mittelschwere bis schwere Plaque-Psoriasis |
| Europäische Union / Vereinigtes Königreich | Kyntheum® | LEO Pharma | Mittelschwere bis schwere Plaque-Psoriasis |

> **Hinweis:** Die obigen Marktdaten stammen aus Domänenwissen und nicht aus dem Evidence Pack. Sie dienen nur zu Kontextzwecken.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Das Evidence Pack dokumentiert keine wesentlichen Warnhinweise, Kontraindikationen oder Arzneimittel-Wechselwirkungen für Brodalumab. Die Abfrage der TFDA-Packungsbeilage hat zwar ein Ergebnis zurückgegeben, aber der analysierte Inhalt war nicht in dieser Version des Evidence Pack enthalten. Vor jeder fortgesetzten klinischen Bewertung ist eine umfassende Überprüfung der offiziellen Verschreibungsinformationen erforderlich (insbesondere die **Kastenwarnung für Suizidgedanken und -verhalten** im Zusammenhang mit IL-17-Signalweg-Inhibitoren).

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack ist grundlegend unvollständig – es wurden keine TxGNN-Kandidaten-Indikationen generiert, und die beiden blockierenden Datenlücken (TFDA-Packungsbeilage und MOA) bleiben ungelöst. Ohne eine vorhergesagte Indikation gibt es keine Repurposing-Hypothese zur Evaluierung.

**Um fortzufahren, wird das Folgende benötigt:**

- **TxGNN-Vorhersage-Pipeline für Brodalumab (DB11776) ausführen**, um geordnete Kandidaten-Indikationen zu generieren
- **MOA von DrugBank API abrufen** (DB11776) — IL-17RA-Bindungsmechanismus und nachgelagerter Signalisierungsweg
- **TFDA-Packungsbeilage analysieren** (Abfrage-Protokoll-ID 4 hat ein Ergebnis zurückgegeben; Inhalt muss extrahiert werden) – besonders Warnhinweise, Kontraindikationen und spezielle Populationen
- **Zielkrankheitsbereich bestätigen** – wenn eine bestimmte Repurposing-Indikation bereits von Interesse ist (z. B. entzündliche Darmerkrankung, axiale Spondyloarthritis, Asthma), sollte dies angegeben werden, damit eine fokussierte Evidenzsuche eingeleitet werden kann
- **Evidenzsammlung erneut ausführen** (klinische Studien, Literatur), sobald eine Kandidaten-Indikation bestätigt ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

