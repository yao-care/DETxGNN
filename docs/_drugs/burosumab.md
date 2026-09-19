---
layout: default
title: Burosumab
parent: Nur Modellvorhersage (L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Burosumab
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

# BUROSUMAB: Kandidat zur Umwidmung — Keine TxGNN-Vorhersagen verfügbar

## Zusammenfassung in einem Satz

BUROSUMAB (DrugBank ID: DB14012) ist ein biologisches Arzneimittel ohne TFDA-Zulassungsunterlagen in Taiwan.
Das aktuelle Evidenzpaket enthält **keine TxGNN-vorhergesagten Indikationen**, was eine formale Neubewertung zu diesem Zeitpunkt unmöglich macht.
Zwei blockierende Datenlücken – Wirkmechanismus und Sicherheitsdaten aus der Packungsbeilage – müssen geklärt werden, bevor dieser Kandidat vorangebracht werden kann.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar (keine TFDA-Zulassungsunterlagen) |
| Vorhergesagte neue Indikation | Keine generiert |
| TxGNN-Vorhersagepunktzahl | N/A |
| Evidenzstufe | N/A |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar, und die TxGNN-Pipeline hat keine vorhergesagten Indikationen für diesen Kandidaten generiert. Ohne eine Zielindikation kann keine mechanistische Plausibilitätsanalyse durchgeführt werden. Die folgenden Abschnitte dokumentieren die zwei blockierenden Lücken, die diese Bewertung am Fortschritt hindern.

**Lücke 1 — Wirkmechanismus (MOA) · Schweregrad: Hoch**
Ohne MOA-Daten ist es nicht möglich zu bewerten, ob die pharmakologische Aktivität von BUROSUMAB für eine neue Zielindikation relevant ist. Abhilfe: Abfragen der DrugBank API für DB14012 und Extraktion des Wirkmechanismus-Feldes.

**Lücke 2 — Sicherheitsdaten aus der Packungsbeilage · Schweregrad: Blockierend**
Ohne TFDA-gestützte Warnungen und Kontraindikationen kann der Kandidat das erste Sicherheits-Screening nicht bestehen, das eine Voraussetzung für alle nachfolgenden Bewertungsschritte ist. Abhilfe: Herunterladen und Auswertung der TFDA-Packungsbeilage PDF für BUROSUMAB.

---

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert – keine vorhergesagte Indikation verfügbar zum Durchsuchen.

---

## Literaturevidenz

Derzeit ist keine verwandte Literatur verfügbar – keine vorhergesagte Indikation verfügbar zum Durchsuchen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidenzpaket für BUROSUMAB ist strukturell unvollständig: Die TxGNN-Pipeline hat keine vorhergesagten Indikationen generiert, und zwei als blockierend und hochgradig eingestufte Datenlücken verhindern jegliche Fortsetzung der Bewertung.

**Um fortzufahren, ist Folgendes erforderlich:**
- Erneutes Ausführen der TxGNN-Vorhersage-Pipeline für BUROSUMAB (DB14012) zur Generierung von Kandidaten-Krankheitsindikationen
- Abruf von Wirkmechanismus-Daten über die DrugBank API (DB14012)
- Herunterladen und Auswertung der TFDA-Packungsbeilage PDF zur Extraktion von Warnungen, Kontraindikationen und Dosierungssicherheitsinformationen
- Durchführung eines Screenings auf Arzneimittel-Wechselwirkungen nach Bestätigung grundlegender Sicherheitsdaten
- Neuausgabe des Evidenzpakets und erneute Auslösung der Berichtsgenerierung nach Beseitigung der oben genannten Lücken

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

