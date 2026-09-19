---
layout: default
title: Ranolazine
parent: Nur Modellvorhersage (L5)
nav_order: 326
evidence_level: L5
indication_count: 1
---

# Ranolazine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Ranolazine: Bewertung der Arzneimittelumwidmung unvollständig — Unzureichende Evidenzpaketdaten

## Zusammenfassung in einem Satz

Ranolazine (DrugBank-ID: DB00243) ist ein kardiovaskuläres Arzneimittel ohne aktuelle Zulassung durch taiwanische Behörden.
Das TxGNN-Modell hat **keine Umwidmungsprognosen** für diesen Kandidaten generiert,
und zwei kritische Datenlücken — einschließlich einer Abwesenheit von TFDA-Sicherheitsdaten mit **blockierendem Schweregrad** und einer Abwesenheit des Wirkmechanismus mit **hohem Schweregrad** — verhindern zum gegenwärtigen Zeitpunkt eine vollständige Bewertung.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht verfügbar (keine taiwanische Lizenz auf Rekord) |
| Prognostizierte neue Indikation | Keine — TxGNN-Prognosen nicht generiert |
| TxGNN-Prognosewert | Nicht verfügbar |
| Evidenzstufe | L5 (keine Prognosen oder Studien verfügbar) |
| Marktstatus Taiwan | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Prognose angemessen?

Für Ranolazine wurde in diesem Evidenzpaket keine TxGNN-Umwidmungsprognose generiert. Ohne eine prognostizierte Indikation kann kein mechanistisches Rationale konstruiert werden.

Der Wirkmechanismus (MOA) ist als **hohes Datenlückenproblem (DG002)** gekennzeichnet. Ohne zu wissen, wie Ranolazine seine therapeutische Wirkung ausübt, ist es nicht möglich, Rückschlüsse darauf zu ziehen, welche anderen Krankheitswege es möglicherweise ansprechen könnte. Die DrugBank-API-Abfrage, die im Abfragelog aufgezeichnet ist (ID: 3), gab ein Ergebnis zurück, aber MOA-Inhalte wurden nicht in das Evidenzpaket eingefügt — dies sollte durch erneutes Parsen der DrugBank-Antwort behoben werden.

Die TFDA-Packungsbeilage-Abfrage (Abfragelog-ID: 4) gab ebenfalls ein Ergebnis zurück, doch es wurden keine genehmigten Indikationen, Warnungen oder Kontraindikationen in das Evidenzpaket extrahiert. Bis diese beiden Abhilfemaßnahmen abgeschlossen sind, ist die mechanistische Analyse blockiert.

---

## Markkinformationen Taiwan

Ranolazine hat keine genehmigten Arzneimittellizensen in Taiwan. Es sind keine Genehmigungsdatensätze zur Überprüfung verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> **Datenlücken-Hinweis:** Wichtige Warnungen, Kontraindikationen und Daten zu Arzneimittel-Wechselwirkungen sind alle in diesem Evidenzpaket nicht verfügbar. Insbesondere existiert eine **Datenlücke mit blockierendem Schweregrad (DG001)** für TFDA-Packungsbeilage-Warnungen und Kontraindikationen — dies verhindert den Eintritt in die S1-Phase der Sicherheits-Vorprüfung. Die DDI-Abfrage (Abfragelog-ID: 2) gab `not_found` zurück.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Rationale:**
Dieser Kandidat kann zum gegenwärtigen Zeitpunkt nicht für eine Arzneimittelumwidmung bewertet werden. Die Abwesenheit von TxGNN-Prognosen, der fehlende MOA und die ungeklärte Datenlücke mit blockierendem Schweregrad verhindern zusammen jede sinnvolle Bewertung von Nutzen, Risiko oder mechanistischer Plausibilität.

**Um fortzufahren, wird Folgendes benötigt:**

- **[DG001 — Blockierend]** Erneutes Parsen des TFDA-Packungsbeilagen-PDF (Abfrage bereits erfolgreich; Extraktions-Pipeline muss überprüft werden) zum Ausfüllen von Warnungen und Kontraindikationen
- **[DG002 — Hoch]** Erneute Abfrage der DrugBank-API und Extraktion von MOA, Arzneimittelkategorien und Toxizitätsfeldern für Ranolazine (DB00243)
- **TxGNN-Pipeline erneut ausführen** nach dem Ausfüllen von MOA- und Indikationsdaten, um Umwidmungsprognosen zu generieren
- **DDI-Abfrage erneut ausführen** gegen eine alternative Quelle (z. B. DrugBank-Interaktions-Endpunkt) zum Ausfüllen von Arzneimittel-Wechselwirkungsdaten
- Nach Verfügbarkeit von Prognosen dieses Evidenzpaket bei v5+ für vollständige Bewertung erneut generieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

