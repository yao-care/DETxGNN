---
layout: default
title: Reslizumab
parent: Nur Modellvorhersage (L5)
nav_order: 337
evidence_level: L5
indication_count: 2
---

# Reslizumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Reslizumab: Biologikum bei eosinophiler Asthma — Analyse zur Umwidmung unvollständig

## Zusammenfassung in einem Satz

Reslizumab ist ein humanisierter monoklonaler Antikörper gegen Interleukin-5 (IL-5) mit internationaler Zulassung (USA Cinqair, EU Cinqaero) für schwere eosinophile Asthma bei Erwachsenen, ist aber noch nicht in Taiwan registriert.
Das aktuelle Evidence Pack enthält **keine TxGNN-Prognoseergebnisse**, daher kann zum gegenwärtigen Zeitpunkt kein Kandidat für eine Umwidmung bewertet werden.
Zwei kritische Datenlücken — Warnhinweise der taiwanesischen Fachinformation und Details zum Wirkungsmechanismus — müssen behoben werden, bevor diese Analyse fortgesetzt werden kann.

---

## Schnellübersicht

| Element | Gehalt |
|---------|--------|
| Ursprüngliche Indikation | Schwere eosinophile Asthma (Erhaltungstherapie als Zusatz bei Erwachsenen) |
| Prognostizierte neue Indikation | Nicht verfügbar — TxGNN-Output fehlt in diesem Evidence Pack |
| TxGNN-Prognosescore | — |
| Evidenzstufe | — |
| Status auf dem Taiwan-Markt | Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Abwarten** |

---

## Informationen zum Taiwan-Markt

Es gibt keine aufgezeichneten TFDA-Genehmigungen. Reslizumab verfügt über internationale Genehmigungen (FDA 2016, EMA 2016) für schwere eosinophile Asthma, hat jedoch bis zum Datenstichtag (2026-04-20) keine TFDA-Registrierung erhalten. Es kann keine Genehmigungstabelle erstellt werden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

> **Hinweis:** Daten zur taiwanesischen Fachinformation konnten in diesem Pipelinelauf nicht abgerufen werden. Die DDI-Datenbank zeigte keine Wechselwirkungen. Sowohl Warn- als auch Kontraindikationsfelder erfordern eine Ergänzung, bevor eine Sicherheitsbewertung möglich ist.

---

## Fazit und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Das Evidence Pack enthält keine TxGNN-Prognoseergebnisse und es gibt zwei ungelöste Datenlücken mit dem Schweregrad *Blockierend* und *Hoch*; es gibt keinen Kandidaten für eine zu bewertende Indikation und keine Sicherheitsbasislinie zum Vergleich.

**Um fortzufahren, ist Folgendes erforderlich:**
- Führen Sie die TxGNN-Vorhersagepipeline für DB06602 aus und füllen Sie `predicted_indications`
- Laden Sie die TFDA-Fachinformations-PDF herunter und parsen Sie sie, um Warnhinweise und Kontraindikationen zu extrahieren (löst DG001 — Blockierend)
- Fragen Sie die DrugBank-API ab, um Wirkungsmechanismus-Details abzurufen (löst DG002 — Hoch)
- Generieren Sie das Evidence Pack (v5+) mit vollständigen Eingaben erneut, bevor Sie diesen Bericht erneut ausführen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

