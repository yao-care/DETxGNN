---
layout: default
title: Cannabidiol
parent: Nur Modellvorhersage (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Cannabidiol
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# Cannabidiol: Vorläufige Bewertung — Keine TxGNN-Prognosedaten verfügbar

## Zusammenfassung in einem Satz

Cannabidiol (CBD) ist ein Phytocannabinoid aus *Cannabis sativa*, mit etablierter behördlicher Zulassung in großen Märkten (FDA: Epidiolex; EMA: Epidyolex) zur Behandlung therapieresistenter Epilepsie-Syndrome.
Dieses Evidence-Paket enthält **keine vorhergesagten TxGNN-Indikationen**, und kritische Daten – einschließlich Wirkmechanismus, Deutschland-Marktzulassungsunterlagen und Sicherheitsprofil – sind als Blockierungslücken gekennzeichnet.
**Eine vollständige Arzneimittel-Umwidmungsevaluierung kann erst nach Schließung dieser Datenlücken abgeschlossen werden.**

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Therapieresistente Epilepsie (Dravet-Syndrom, Lennox-Gastaut-Syndrom) – basierend auf Expertenwissen; nicht im Evidence-Paket bestätigt |
| Vorhergesagte neue Indikation | Keine Vorhersagen verfügbar |
| TxGNN-Prognosescore | N/A |
| Evidenzebene | N/A – keine Vorhersagen generiert |
| Deutschland-Marktstatus | Nicht gefunden (Evidence-Paket: Nicht vermarktet / 0 Zulassungen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Zusammenfassung der Datenlücken

Dieses Evidence-Paket hat **2 Blockierungs-/hochschwere Datenlücken**, die eine vollständige Evaluierung verhindern:

| Lücken-ID | Punkt | Schweregrad | Auswirkung | Abhilfe |
|-----------|-------|-------------|-----------|--------|
| DG001 | Warnhinweise in der Gebrauchsinformation / Kontraindikationen | **Blockierend** | Kann S1-Sicherheitsprüfung nicht bestehen | EMA-Epidyolex-SmPC-PDF herunterladen und analysieren |
| DG002 | Wirkmechanismus (MOA) | Hoch | Mechanistische Relevanzanalyse nicht möglich | DrugBank-API für DB09061 abfragen |

---

## Warum es keine Vorhersage gibt

Das TxGNN-Modell hat in diesem Durchlauf **keine vorhergesagten Indikationen** für Cannabidiol (DB09061) zurückgegeben. Mögliche Gründe sind:

1. Die Verbindung befindet sich nicht im Knowledge Graph, der während dieses Prognoselaufs verwendet wurde
2. Alle Kandidaten-Scores fielen unter den Meldeschwellenwert
3. Ein Pipeline-Fehler ist einem vorgelagerten Schritt der Evidenzsammlung aufgetreten

Ohne mindestens eine TxGNN-Vorhersage kann die Kern-Arzneimittel-Umwidmungsanalyse nicht fortgesetzt werden. Dies muss vor weiteren Evaluierungsschritten untersucht werden.

---

## Deutschland-Marktinformationen

In der behördlichen Datenbank innerhalb dieses Evidence-Pakets wurden keine Zulassungsunterlagen für Cannabidiol gefunden.

> **Hinweis auf Diskrepanz:** Epidyolex (Cannabidiol-Orallösung 100 mg/mL) erhielt am 19. September 2019 die EMA-Zulassung als Zusatzbehandlung für Anfälle, die mit dem Lennox-Gastaut-Syndrom oder dem Dravet-Syndrom bei Patienten ab 2 Jahren verbunden sind. Das Fehlen von Unterlagen deutet stark darauf hin, dass die behördliche Abfrage unter dem INN „CANNABIDIOL" durchgeführt wurde, aber nicht mit dem genehmigten Markennamen abgeglichen wurde. Die Abfrage sollte mit alternativen Kennzeichnern erneut durchgeführt werden: **Epidyolex**, **Epidiolex** oder Zulassungsnummer **EU/1/19/1375**.

---

## Sicherheitsaspekte

Alle Sicherheitsdatenfelder in diesem Evidence-Paket sind nicht verfügbar. Bitte konsultieren Sie die offizielle EMA-Zusammenfassung der Merkmale der Zubereitung (SmPC) für Epidyolex für vollständige Sicherheitsinformationen.

> Blockierendes Element ausstehend, bevor die Evaluierung fortgesetzt werden kann:
> **DG001** – Epidyolex-SmPC abrufen und analysieren, um Kontraindikationen, Warnhinweise und wichtige Arzneimittelwechselwirkungen (besonders mit CYP3A4/CYP2C19-Substraten und Valproat) zu extrahieren.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Das Evidence-Paket enthält überhaupt keine TxGNN-Vorhersagen, und zwei Blockierungs-/hochschwere Datenlücken (MOA, Sicherheitsprofil) verhindern, dass zu diesem Zeitpunkt eine aussagekräftige Arzneimittel-Umwidmungsbewertung durchgeführt werden kann.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[Kritisch]** TxGNN-Prognosepipeline für DB09061 erneut ausführen und bestätigen, dass die Ausgabe nicht leer ist; wenn immer noch leer, verifizieren, dass die Verbindung im Knowledge Graph enthalten ist
- **[DG001]** Epidyolex-EMA-SmPC (EU/1/19/1375) abrufen und Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsprofil extrahieren
- **[DG002]** DrugBank-API für vollständige MOA-Daten für DB09061 (Cannabidiol) abfragen
- **[Regulatorisch]** Deutschland-Regulierungsabfrage mit Markennamen **Epidyolex** / **Epidiolex** erneut durchführen, um tatsächliche Marktzulassungsunterlagen und genehmigte Indikationen abzurufen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

