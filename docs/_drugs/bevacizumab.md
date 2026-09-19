---
layout: default
title: Bevacizumab
parent: Nur Modellvorhersage (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab (DB00112): Evidence Pack Unvollständig — Umwidmungsanalyse Nicht Verfügbar

## Zusammenfassung in einem Satz

Bevacizumab (DrugBank: DB00112) ist ein antineoplastisches biologisches Agens, dessen ursprüngliche zugelassene Indikationen und Wirkmechanismus nicht im aktuellen Evidence Pack erfasst sind. Das TxGNN-Modell hat **noch keine vorhergesagten Indikationen** für diese Verbindung generiert, was bedeutet, dass die Umwidmungsanalysepipeline nicht abgeschlossen wurde. Dieser Bericht dokumentiert den aktuellen Datenzustand und beschreibt die erforderlichen Informationen, bevor eine vollständige Bewertung fortgesetzt werden kann.

---

## Schnelle Übersicht

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Nicht verfügbar im aktuellen Evidence Pack |
| Vorhergesagte neue Indikation | Keine — TxGNN-Vorhersageausgabe fehlt |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | L5 (Modellvorhersage noch nicht abgeschlossen) |
| Marktstatus | Nicht auf dem Markt (Nicht auf dem Markt) |
| Anzahl der Zulassungen | 0 |
| Empfehlung | **Halten** — kritische Datenlücken müssen zunächst behoben werden |

---

## Warum ist diese Vorhersage angemessen?

Dieser Abschnitt kann nicht abgeschlossen werden, da das `predicted_indications`-Array im Evidence Pack leer ist. Es wurde keine TxGNN-Vorhersageausgabe für Bevacizumab (DB00112) erhalten, daher gibt es keine vorhergesagte Indikation, um eine mechanistische Plausibilität zu bewerten.

Darüber hinaus ist das Feld Wirkmechanismus (MOA) derzeit nicht verfügbar (Data Gap DG002). Ohne MOA-Daten ist nicht einmal eine manuelle Überbrückungsanalyse zwischen der ursprünglichen Indikation und einer beliebigen kandidatischen neuen Indikation möglich.

Sobald die TxGNN-Pipeline Vorhersagen generiert und die MOA aus DrugBank abgerufen wird, wird dieser Abschnitt den Anti-VEGF-Weg und seine Anwendbarkeit auf die kandidatische Indikation beschreiben.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien mit einer TxGNN-vorhergesagten Umwidmungsindikation verbunden, da keine Vorhersage generiert wurde.

---

## Literaturbeweise

Derzeit ist keine verwandte Literatur für eine TxGNN-vorhergesagte Umwidmungsindikation verfügbar, da keine Vorhersage generiert wurde.

---

## Marktinformation

| Punkt | Status |
|------|--------|
| Marktstatus | Nicht auf dem Markt (Nicht auf dem Markt) |
| Gesamtzulassungen | 0 |
| Eingetragene Lizenzen | Keine |

Es sind keine Autorisierungsunterlagen verfügbar. Die behördliche Anfrage gab null Ergebnisse zurück.

---

## Zytotoxizität

Bevacizumab (DB00112) ist ein antineoplastisches biologisches Agens (Anti-VEGF-monoklonaler Antikörper). Obwohl die DrugBank-Kategorifelder nicht in diesem Evidence Pack vorhanden sind, ist bekannt, dass das Arzneimittel zur Klasse der zielgerichteten Therapie gehört.

| Punkt | Inhalt |
|------|---------|
| Zytotoxizität-Klassifizierung | Zielgerichtete Therapie — Anti-VEGF-monoklonaler Antikörper (keine konventionelle Zytotoxizität) |
| Myelosuppression-Risiko | Niedrig (der Mechanismus zielt nicht direkt auf hämatopoetische Zellen ab; Thrombozytopenie ist keine primäre Toxizität) |
| Emetogenität-Klassifizierung | Minimal bis niedrig |
| Überwachungselemente | Blutdruck (Hypertonie ist ein Klasseneffekt), CBC, Urinprotein, Wundheilungsstatus, Überwachung thromboembolischer Ereignisse |
| Handhabungsschutz | Standardbehandlung für biologische Arzneimittel; nicht als konventionelle Zytotoxin klassifiziert — keine geschlossene Arzneimittelübertragungseinrichtung erforderlich, aber Befolgung institutioneller biologischer Handhabungs-SOPs |

> **Anmerkung:** Die vollständige Zytotoxizitätscharakterisierung sollte auf die Packungsbeilage verweisen. Die Felder Warnungen und Kontraindikationen (Data Gap DG001) fehlen derzeit in diesem Evidence Pack.

---

## Sicherheitserwägungen

Alle wichtigen Warnungen und Kontraindikationsfelder gaben keine Daten im aktuellen Evidence Pack zurück. Es wurden keine Arzneimittel-Wechselwirkungsaufzeichnungen gefunden (DDI-Abfragestatus: nicht gefunden).

> Bitte beziehen Sie sich auf die Packungsbeilage für vollständige Sicherheitsinformationen.

---

## Schlussfolgerung und Nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack für Bevacizumab (DB00112) ist kritisch unvollständig: Das TxGNN-Modell hat keine vorhergesagten Indikationen erzeugt, sowohl der Wirkmechanismus als auch die behördlichen Sicherheitsdaten fehlen, und das Arzneimittel hat null Autorisierungsaufzeichnungen auf dem Zielmarkt. Es gibt derzeit keine Evidenzbasis, auf der eine Umwidmungsempfehlung aufgebaut werden kann.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[DG001 — Blockierend]** Packungsbeilage (仿單) von der Website der Regulierungsbehörde abrufen; Warnungen, Kontraindikationen und zugelassene Indikationstexte extrahieren
- **[DG002 — Hoch]** Abfrage der DrugBank-API für DB00112, um MOA, Arzneimittelkategorien und Toxizitätsdaten zu erfassen
- **TxGNN-Pipeline erneut ausführen** — bestätigen, dass Bevacizumab in der Vorhersage enthalten ist und dass die `predicted_indications`-Ausgabe korrekt in das Evidence Pack geschrieben wird
- **Marktbereich überprüfen** — bestätigen, ob die Zielaufsichtszuständigkeit für diesen Kandidaten Taiwan (TFDA) oder Deutschland (BfArM) ist, da die Evidence Pack-Feldnamen und der chinesischsprachige Statustext derzeit inkonsistent sind
- **DDI-Abruf** — Wiederholung der DDI-Datenbankabfrage, sobald das Arzneimittelprofil vollständiger gefüllt ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

